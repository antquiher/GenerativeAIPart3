
import os
import asyncio
from dotenv import load_dotenv

# Load variables from .env file
# Don't miss GOOGLE_API_KEY
load_dotenv()

# Import ADK components --------------------------------------------------------------------
from google.genai import types

from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import AgentTool
from google.adk.plugins.logging_plugin import LoggingPlugin
from count_invocation_plugin import CountInvocationPlugin
from metrics_w_example import compute_metrics, ReadabilityMetrics

print("✅ ADK components imported successfully.")

os.environ["GOOGLE_API_KEY"] = "AIzaSyCiOS_F56hzvWrYTMfIT5bdydSqokob1sE"

print("✅ Gemini API key setup complete.")

# Configure HTTP retry options for API calls ------------------------------------------------
retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)

print("✅ Helper functions defined.")

def _ensure_api_key() -> None:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "Falta GOOGLE_API_KEY. Define la variable en el entorno o en .env."
        )

# Define a custom tool to compute text readability metrics --------------
#        @AgentTool.from_function(retry_options=retry_config)
def get_text_metrics(text: str) -> dict:
    """Computes comprehensive readability metrics for Spanish text.

    Args:
        text: The Spanish text to analyze. Should contain at least one sentence.

    Returns:
        Dictionary with status and metrics information.
    """
    try:
        metrics = compute_metrics(text)

        return {
            "status": "success",
            "num_sentences": metrics.num_sentences,
            "num_words": metrics.num_words,
            "num_syllables": metrics.num_syllables,
            "lmo": round(metrics.lmo, 2),
            "std_sentence_len": round(metrics.std_sentence_len, 2),
            "cv_sentence_len": round(metrics.cv_sentence_len, 3),
            "z_normality": round(metrics.z_normality, 2),
            "flesch_szigriszt": round(metrics.flesch_szigriszt, 2),
            "passive_ratio": round(metrics.passive_ratio, 2),
        }
    except ValueError as e:
        return {
            "status": "error",
            "error_message": f"Error al procesar el texto: {str(e)}",
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error inesperado: {str(e)}",
        }

print("✅ Text metrics function created")

# Define a custom tool to evaluate text quality based on metrics ------------------------
#        @AgentTool.from_function(retry_options=retry_config)
def evaluate_text_quality(text: str) -> dict:
    """Evaluates the quality of Spanish text based on readability metrics."""
    try:
        metrics = compute_metrics(text)

        score = 0.0
        recommendations = []

        flesch = metrics.flesch_szigriszt
        if flesch >= 80:
            score += 40
        elif flesch >= 65:
            score += 35
        elif flesch >= 50:
            score += 30
        elif flesch >= 35:
            score += 20
        else:
            score += 10
            recommendations.append(
                "El texto es muy dificil de leer. Usa oraciones mas cortas y palabras simples."
            )

        lmo = metrics.lmo
        if 15 <= lmo <= 25:
            score += 25
        elif 10 <= lmo < 15 or 25 < lmo <= 30:
            score += 20
        elif lmo > 30:
            score += 10
            recommendations.append(
                f"Oraciones demasiado largas (promedio: {lmo:.1f} palabras). Divide algunas oraciones."
            )
        else:
            score += 15

        cv = metrics.cv_sentence_len
        if 0.3 <= cv <= 0.6:
            score += 20
        elif 0.2 <= cv < 0.3 or 0.6 < cv <= 0.8:
            score += 15
        elif cv < 0.2:
            score += 10
            recommendations.append(
                "Varia la longitud de las oraciones para mejorar el ritmo."
            )
        else:
            score += 12

        passive = metrics.passive_ratio
        if passive <= 10:
            score += 15
        elif passive <= 20:
            score += 12
        elif passive <= 30:
            score += 8
            recommendations.append(
                f"Alto uso de voz pasiva ({passive:.1f}%). Usa mas voz activa."
            )
        else:
            score += 5
            recommendations.append(
                f"Excesivo uso de voz pasiva ({passive:.1f}%). La voz activa es mas directa."
            )

        if score >= 85:
            quality_level = "Excelente"
        elif score >= 70:
            quality_level = "Bueno"
        elif score >= 55:
            quality_level = "Aceptable"
        elif score >= 40:
            quality_level = "Mejorable"
        else:
            quality_level = "Deficiente"

        if not recommendations:
            recommendations.append("Excelente legibilidad del texto.")

        return {
            "status": "success",
            "quality_score": round(score, 2),
            "quality_level": quality_level,
            "recommendations": recommendations,
        }

    except ValueError as e:
        return {
            "status": "error",
            "error_message": f"Error al evaluar el texto: {str(e)}",
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error inesperado: {str(e)}",
        }

print("✅ Text quality evaluation function created")

# Text quality agent with custom function tools -------------------------------
text_quality_agent = LlmAgent(
    name="text_quality_agent",
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    instruction=(
        "Eres un asistente experto en analisis de calidad de textos en espanol.\n\n"
        "Para analizar textos:\n"
        "1. Usa get_text_metrics() para obtener metricas detalladas de legibilidad\n"
        "2. Usa evaluate_text_quality() para obtener una evaluacion con puntuacion y recomendaciones\n"
        "3. Verifica el campo 'status' en cada respuesta para detectar errores\n"
        "4. Presenta los resultados de forma clara y estructurada\n"
        "5. Si el texto es de alta calidad, felicita al usuario\n"
    ),
    tools=[get_text_metrics, evaluate_text_quality],
)

print("✅ Text quality agent created with custom function tools")
print("🔧 Available tools:")
print("  • get_text_metrics - Computes detailed readability metrics")
print("  • evaluate_text_quality - Evaluates text quality with score and recommendations")

def _extract_response_text(result) -> str | None:
    priority_keys = (
        "text",
        "content",
        "output_text",
        "response",
        "final_response",
        "result",
        "message",
        "payload",
    )

    visited_ids: set[int] = set()
    candidates: list[str] = []

    def _walk(obj, depth: int = 0) -> None:
        if obj is None or depth > 6:
            return
        obj_id = id(obj)
        if obj_id in visited_ids:
            return
        visited_ids.add(obj_id)

        if isinstance(obj, str):
            text = obj.strip()
            if text:
                candidates.append(text)
            return

        if isinstance(obj, dict):
            for key in priority_keys:
                if key in obj:
                    _walk(obj.get(key), depth + 1)
            for val in obj.values():
                _walk(val, depth + 1)
            return

        if isinstance(obj, (list, tuple)):
            for item in obj:
                _walk(item, depth + 1)
            return

        for attr in priority_keys:
            if hasattr(obj, attr):
                _walk(getattr(obj, attr), depth + 1)

        if hasattr(obj, "events"):
            _walk(getattr(obj, "events"), depth + 1)

        if hasattr(obj, "__dict__"):
            _walk(obj.__dict__, depth + 1)

    _walk(result)

    if not candidates:
        return None

    candidates.sort(key=len, reverse=True)
    return candidates[0]

# Test the text quality agent with LoggingPlugin for observability ------------------------------------------------
if __name__ == "__main__":
    import asyncio

    async def main():
        _ensure_api_key()
        print("\n" + "="*80)
        print("Testing text_quality_agent")
        print("="*80 + "\n")

        text_quality_runner = InMemoryRunner(
            agent=text_quality_agent,
            plugins=[LoggingPlugin(), CountInvocationPlugin()],
        )
        print("📊 LoggingPlugin enabled for observability")
        print("📈 CountInvocationPlugin enabled for call tracking")


        # este texto es intencionadamente complejo para probar las métricas de legibilidad
        # sample_text = (
        #     "En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion y que, ademas, se ve incrementada por la falta de concrecion en los planteamientos, se pretende abordar sin delimitar los conceptos principales ni establecer un marco claro, resulta inevitable que la comprension se diluya y que el lector, en un intento poco fructifero de encontrar un hilo conductor, termine por perderse en una sucesion de ideas vagamente conectadas, donde cada afirmacion parece depender de otra que no se explica y donde la precision brilla por su ausencia."
        # )
        
        # Este texto es técnico pero claro, con buena puntuación y estructura, para probar una evaluación de calidad alta
        sample_text = (
            "El caso que se nos plantea tiene como base diferentes problemas de gran envergadura de manera individual, pero en su conjunto es problema de índole mayor. Según datos del PMI, los proyectos de desarrollo de software en formato waterfall presentan altos porcentajes de retrasos, sobrecostes y retrabajos, mientras que los enfoques ágiles reducen parcialmente estos riesgos. En el proyecto MedSys Online ya se han materializado varios de estos factores de riesgo."
        )
        
        # Este es un texto literario con oraciones largas y uso de voz pasiva, para probar una evaluación de calidad media
        # sample_text = (
        #     "En la penumbra de la habitación, donde las sombras danzaban al ritmo de la brisa nocturna, se encontraba un anciano de mirada profunda y voz pausada, quien relataba historias de tiempos pasados con una melancolía que parecía envolver cada palabra en un manto de nostalgia, mientras el fuego crepitaba suavemente en la chimenea, creando un ambiente propicio para la introspección y el recuerdo."
        # )
        
        # Este texto es historico con oraciones muy largas, uso excesivo de voz pasiva y vocabulario complejo, para probar una evaluación de calidad baja
        # sample_text = (
        #     "Durante el periodo comprendido entre los siglos XVI y XVIII, se llevaron a  cabo una serie de eventos que, aunque aparentemente desconectados, contribuyeron a moldear el curso de la historia de manera significativa, siendo la Revolución Industrial uno de los hitos más destacados, ya que no solo transformó las estructuras económicas y sociales, sino que también dio lugar a un cambio paradigmático en la forma en que las personas vivían y trabajaban, marcando el inicio de una era caracterizada por avances tecnológicos sin precedentes y por una creciente interconexión global."
        # )

        result = await text_quality_runner.run_debug(
            "Por favor, analiza la calidad y legibilidad del siguiente texto:\n\n"
            f"{sample_text}"
        )

        response_text = _extract_response_text(result)
        if response_text:
            print("✅ Respuesta de Gemini:\n" + response_text)
        else:
            print("⚠️ No se pudo extraer el texto de respuesta desde run_debug().")
            print(f"ℹ️ Tipo de resultado: {type(result).__name__}")
            if isinstance(result, dict):
                print(f"ℹ️ Claves disponibles: {list(result.keys())}")
            elif hasattr(result, "__dict__"):
                print(f"ℹ️ Atributos disponibles: {list(result.__dict__.keys())}")

    asyncio.run(main())

