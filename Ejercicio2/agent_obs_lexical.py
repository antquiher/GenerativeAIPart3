import os
import asyncio
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Import ADK components --------------------------------------------------------------------
from google.genai import types

from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import AgentTool
from google.adk.plugins.logging_plugin import LoggingPlugin
from count_invocation_plugin import CountInvocationPlugin
from lexical_metrics import compute_lexical_metrics, LexicalMetrics
import re

print("✅ ADK components imported successfully.")

os.environ["GOOGLE_API_KEY"] = "AIzaSyCiOS_F56hzvWrYTMfIT5bdydSqokob1sE"

print("✅ Gemini API key setup complete.")

# Configure HTTP retry options for API calls ------------------------------------------------
retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)

print("✅ Helper functions defined.")

def _ensure_api_key() -> None:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "Falta GOOGLE_API_KEY. Define la variable en el entorno o en .env."
        )

# Define a custom tool to compute lexical richness metrics --------------
def get_lexical_metrics(text: str) -> dict:
    """Computes lexical richness and vocabulary diversity metrics for Spanish text.

    Args:
        text: The Spanish text to analyze.

    Returns:
        Dictionary with status and lexical metrics information.
    """
    try:
        metrics = compute_lexical_metrics(text)

        return {
            "status": "success",
            "num_words": metrics.num_words,
            "num_unique_words": metrics.num_unique_words,
            "ttr": round(metrics.ttr, 3),
            "rttr": round(metrics.rttr, 2),
            "hapax_count": metrics.hapax_count,
            "hapax_ratio": round(metrics.hapax_ratio, 2),
            "avg_word_length": round(metrics.avg_word_length, 2),
            "avg_syllables_per_word": round(metrics.avg_syllables_per_word, 2),
            "content_density": round(metrics.content_density, 2),
            "lexical_diversity": round(metrics.lexical_diversity, 2),
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

print("✅ Lexical metrics function created")

# Define a custom tool to evaluate vocabulary richness ------------------------
def evaluate_vocabulary_richness(text: str) -> dict:
    """Evaluates vocabulary richness and lexical diversity of Spanish text."""
    try:
        metrics = compute_lexical_metrics(text)

        score = 0.0
        recommendations = []

        # 1. Diversidad léxica (0-35 points)
        diversity = metrics.lexical_diversity
        if diversity >= 70:
            score += 35
        elif diversity >= 55:
            score += 30
        elif diversity >= 40:
            score += 25
        elif diversity >= 30:
            score += 20
        else:
            score += 15
            recommendations.append(
                f"Baja diversidad lexica ({diversity:.1f}/100). Intenta usar sinonimos y evitar repeticiones."
            )

        # 2. Type-Token Ratio (0-25 points)
        ttr = metrics.ttr
        if ttr >= 0.7:
            score += 25
        elif ttr >= 0.6:
            score += 22
        elif ttr >= 0.5:
            score += 18
        elif ttr >= 0.4:
            score += 14
        else:
            score += 10
            recommendations.append(
                f"TTR bajo ({ttr:.3f}). Hay mucha repeticion de palabras. Varia tu vocabulario."
            )

        # 3. Densidad de contenido (0-20 points)
        content = metrics.content_density
        if content >= 60:
            score += 20
        elif content >= 50:
            score += 17
        elif content >= 40:
            score += 14
        else:
            score += 10
            recommendations.append(
                f"Densidad de contenido baja ({content:.1f}%). Demasiadas palabras funcionales."
            )

        # 4. Complejidad de palabras (0-20 points)
        avg_len = metrics.avg_word_length
        avg_syl = metrics.avg_syllables_per_word
        
        if 5.5 <= avg_len <= 7.5 and 2.5 <= avg_syl <= 3.5:
            score += 20
        elif 4.5 <= avg_len <= 8.5 and 2.0 <= avg_syl <= 4.0:
            score += 16
        elif avg_len < 4.5:
            score += 12
            recommendations.append(
                f"Palabras muy cortas (promedio: {avg_len:.2f} caracteres). Usa vocabulario mas variado."
            )
        elif avg_len > 8.5:
            score += 14
            recommendations.append(
                f"Palabras muy largas (promedio: {avg_len:.2f} caracteres). Puede dificultar la lectura."
            )
        else:
            score += 14

        # Determine quality level
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
            recommendations.append("Excelente riqueza lexica y diversidad de vocabulario.")

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

print("✅ Vocabulary richness evaluation function created")

# Lexical quality agent with custom function tools -------------------------------
lexical_quality_agent = LlmAgent(
    name="lexical_quality_agent",
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    instruction=(
        "Eres un asistente de analisis de riqueza lexica.\n"
        "Usa get_lexical_metrics() y evaluate_vocabulary_richness() para analizar el texto.\n"
        "Devuelve solo un resumen conciso con la evaluacion y score de calidad.\n"
    ),
    tools=[get_lexical_metrics, evaluate_vocabulary_richness],
)

print("✅ Lexical quality agent created with custom function tools")
print("🔧 Available tools:")
print("  • get_lexical_metrics - Computes vocabulary richness metrics")
print("  • evaluate_vocabulary_richness - Evaluates lexical diversity with score and recommendations")

def _extract_response_text(result) -> str | None:
    """Extract actual response text from run_debug() result events.
    
    Looks specifically for text responses from the agent, avoiding input text.
    
    Args:
        result: List of events returned by run_debug()
        
    Returns:
        The response text or None if not found
    """
    if not isinstance(result, list):
        return None
    
    # Look for the final event that should contain the agent's text response
    for event in reversed(result):
        if hasattr(event, 'content') and event.content is not None:
            # Check if this event has text parts (not function_call or function_response)
            if hasattr(event.content, 'parts') and event.content.parts:
                for part in event.content.parts:
                    if hasattr(part, 'text') and part.text:
                        return part.text
    
    return None

# Test the lexical quality agent with LoggingPlugin for observability ------------------------------------------------
if __name__ == "__main__":
    import asyncio

    async def main():
        _ensure_api_key()
        print("\n" + "="*80)
        print("Testing lexical_quality_agent")
        print("="*80 + "\n")

        lexical_quality_runner = InMemoryRunner(
            agent=lexical_quality_agent,
            plugins=[LoggingPlugin(), CountInvocationPlugin()],
        )
        print("📊 LoggingPlugin enabled for observability")
        print("📈 CountInvocationPlugin enabled for call tracking")

        sample_text = (
            "En la medida en que la complejidad inherente a la problematica, que ya de por si "
            "se manifiesta en multiples niveles de interpretacion y que, ademas, se ve incrementada "
            "por la falta de concrecion en los planteamientos, se pretende abordar sin delimitar "
            "los conceptos principales ni establecer un marco claro, resulta inevitable que la "
            "comprension se diluya y que el lector, en un intento poco fructifero de encontrar un "
            "hilo conductor, termine por perderse en una sucesion de ideas vagamente conectadas."
        )

        result = await lexical_quality_runner.run_debug(
            "Analiza la riqueza lexica y calidad del siguiente texto:\n\n"
            f"{sample_text}"
        )

        response_text = _extract_response_text(result)
        
        if response_text:
            print(f"\n📊 Resultado:\n{response_text}")
        else:
            print("\n⚠️ No se obtuvo respuesta del agente.")

    asyncio.run(main())
