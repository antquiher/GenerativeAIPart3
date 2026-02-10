import os
import asyncio
from dataclasses import dataclass
from dotenv import load_dotenv
import re

# Load variables from .env file
load_dotenv()

# Import ADK components
from google.genai import types
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import AgentTool
from google.adk.plugins.logging_plugin import LoggingPlugin
from count_invocation_plugin import CountInvocationPlugin

print("✅ ADK components imported successfully.")

os.environ["GOOGLE_API_KEY"] = "AIzaSyCiOS_F56hzvWrYTMfIT5bdydSqokob1sE"

print("✅ Gemini API key setup complete.")

# Configure HTTP retry options for API calls
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

# Quality metrics data class
@dataclass
class TextQualityMetrics:
    readability_score: float
    clarity_score: float
    coherence_score: float
    grammar_score: float
    overall_score: float
    recommendation: str

# Define custom tools for text quality analysis
def analyze_text_readability(text: str) -> dict:
    """Analyzes text readability using multiple indices.
    
    Args:
        text: The text to analyze.
        
    Returns:
        Dictionary with readability metrics and score.
    """
    try:
        # Basic text statistics
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        num_sentences = len(sentences)
        
        words = text.split()
        num_words = len(words)
        
        if num_words < 10:
            return {
                "status": "error",
                "error_message": "El texto es demasiado corto para analizar (mínimo 10 palabras)"
            }
        
        # Sentence statistics
        avg_words_per_sentence = num_words / max(num_sentences, 1)
        
        # Syllable count (simplified for Spanish)
        syllable_count = 0
        vowels = 'aeioáéíóúuy'
        for word in words:
            word_lower = word.lower().rstrip('.,!?;:')
            syllables = sum(1 for char in word_lower if char in vowels)
            # Adjust for consecutive vowels
            syllables = max(1, syllables)
            syllable_count += syllables
        
        avg_syllables_per_word = syllable_count / num_words if num_words > 0 else 0
        
        # Flesch-Kincaid Grade Level (adapted for Spanish)
        fkg_score = (0.39 * avg_words_per_sentence) + (11.8 * avg_syllables_per_word) - 15.59
        fkg_score = max(0, fkg_score)
        
        # Flesch Reading Ease (adapted for Spanish)
        fre_score = 206.835 - (1.3 * avg_words_per_sentence) - (60.1 * avg_syllables_per_word)
        fre_score = max(0, min(100, fre_score))
        
        # Determine readability level
        if fre_score >= 90:
            readability_level = "Muy Fácil - Infantil"
            readability_score = 95
        elif fre_score >= 80:
            readability_level = "Fácil"
            readability_score = 85
        elif fre_score >= 70:
            readability_level = "Moderado"
            readability_score = 75
        elif fre_score >= 60:
            readability_level = "Algo Difícil"
            readability_score = 65
        elif fre_score >= 50:
            readability_level = "Difícil"
            readability_score = 55
        elif fre_score >= 30:
            readability_level = "Muy Difícil"
            readability_score = 35
        else:
            readability_level = "Extremadamente Complejo"
            readability_score = 15
        
        return {
            "status": "success",
            "fre_score": round(fre_score, 2),
            "fkg_grade": round(fkg_score, 2),
            "readability_level": readability_level,
            "readability_score": readability_score,
            "avg_words_per_sentence": round(avg_words_per_sentence, 2),
            "avg_syllables_per_word": round(avg_syllables_per_word, 2),
            "num_sentences": num_sentences,
            "num_words": num_words,
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error al analizar legibilidad: {str(e)}"
        }

def evaluate_text_clarity(text: str) -> dict:
    """Evaluates text clarity based on sentence length, passive voice, and complexity.
    
    Args:
        text: The text to analyze.
        
    Returns:
        Dictionary with clarity metrics and score.
    """
    try:
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        words = text.split()
        num_words = len(words)
        
        if num_words < 10:
            return {
                "status": "error",
                "error_message": "El texto es demasiado corto para analizar"
            }
        
        # Analyze sentence lengths
        sentence_lengths = [len(s.split()) for s in sentences]
        avg_sentence_length = sum(sentence_lengths) / len(sentence_lengths) if sentences else 0
        
        # Count complex structures
        passive_voice_count = len(re.findall(r'\b(es|son|fue|fueron|sea|sean|sido|siendo)\s+\w+(?:ado|ada|idos|idas|able)\b', text, re.IGNORECASE))
        
        # Check for excessive pronouns and weak references
        weak_words = ['cosa', 'eso', 'esto', 'algo', 'alguien', 'etc', 'etc.']
        weak_word_count = sum(text.lower().count(w) for w in weak_words)
        
        # Calculate clarity score
        clarity_score = 100
        
        # Sentence length penalty (ideal: 15-20 words)
        if avg_sentence_length > 25:
            clarity_score -= 20
        elif avg_sentence_length > 20:
            clarity_score -= 10
        elif avg_sentence_length < 5:
            clarity_score -= 5
        
        # Passive voice penalty
        passive_ratio = passive_voice_count / max(len(sentences), 1)
        if passive_ratio > 0.3:
            clarity_score -= 15
        elif passive_ratio > 0.15:
            clarity_score -= 8
        
        # Weak word penalty
        weak_ratio = weak_word_count / max(num_words / 10, 1)
        if weak_ratio > 5:
            clarity_score -= 15
        elif weak_ratio > 2:
            clarity_score -= 8
        
        clarity_score = max(0, min(100, clarity_score))
        
        # Determine clarity level
        if clarity_score >= 85:
            clarity_level = "Muy Clara"
        elif clarity_score >= 70:
            clarity_level = "Clara"
        elif clarity_score >= 55:
            clarity_level = "Aceptable"
        elif clarity_score >= 40:
            clarity_level = "Poco Clara"
        else:
            clarity_level = "Confusa"
        
        return {
            "status": "success",
            "clarity_score": clarity_score,
            "clarity_level": clarity_level,
            "avg_sentence_length": round(avg_sentence_length, 2),
            "passive_voice_percentage": round(passive_ratio * 100, 1),
            "weak_word_count": weak_word_count,
            "recommendations": []
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error al evaluar claridad: {str(e)}"
        }

def evaluate_text_coherence(text: str) -> dict:
    """Evaluates text coherence based on paragraph structure and transitions.
    
    Args:
        text: The text to analyze.
        
    Returns:
        Dictionary with coherence metrics and score.
    """
    try:
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        
        if len(paragraphs) == 0:
            # If no double line breaks, use simple heuristic
            sentences = re.split(r'[.!?]+', text)
            sentences = [s.strip() for s in sentences if s.strip()]
            paragraphs = ['. '.join(sentences[i:i+3]) for i in range(0, len(sentences), 3)]
        
        num_paragraphs = len(paragraphs)
        
        # Count transitional words/phrases
        transitions = [
            'sin embargo', 'no obstante', 'por lo tanto', 'en conclusión',
            'además', 'asimismo', 'por otra parte', 'en primer lugar',
            'finalmente', 'en resumen', 'consecuentemente', 'por consiguiente'
        ]
        
        transition_count = sum(text.lower().count(t) for t in transitions)
        
        # Analyze paragraph lengths (should be reasonably balanced)
        paragraph_lengths = [len(p.split()) for p in paragraphs]
        avg_para_length = sum(paragraph_lengths) / len(paragraph_lengths) if paragraphs else 0
        para_length_variance = max(paragraph_lengths) - min(paragraph_lengths) if paragraph_lengths else 0
        
        # Calculate coherence score
        coherence_score = 100
        
        # Penalize very few paragraphs
        if num_paragraphs < 2:
            coherence_score -= 20
        
        # Penalize lack of transitions
        if transition_count == 0:
            coherence_score -= 15
        elif transition_count < 2:
            coherence_score -= 8
        
        # Penalize imbalanced paragraphs
        if para_length_variance > 300:
            coherence_score -= 10
        
        coherence_score = max(0, min(100, coherence_score))
        
        # Determine coherence level
        if coherence_score >= 85:
            coherence_level = "Muy Coherente"
        elif coherence_score >= 70:
            coherence_level = "Coherente"
        elif coherence_score >= 55:
            coherence_level = "Aceptable"
        elif coherence_score >= 40:
            coherence_level = "Poco Coherente"
        else:
            coherence_level = "Incoherente"
        
        return {
            "status": "success",
            "coherence_score": coherence_score,
            "coherence_level": coherence_level,
            "num_paragraphs": num_paragraphs,
            "avg_paragraph_length": round(avg_para_length, 1),
            "transition_phrases_count": transition_count,
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error al evaluar coherencia: {str(e)}"
        }

print("✅ Text quality analysis functions created")

# Quality agent with custom function tools
quality_agent = LlmAgent(
    name="quality_agent",
    model=Gemini(model="gemini-2.5-flash", retry_options=retry_config),
    instruction=(
        "Eres un evaluador de calidad de textos.\n\n"
        "1. Llama a analyze_text_readability(), evaluate_text_clarity() y evaluate_text_coherence()\n"
        "2. Calcula la puntuación general: (readability + clarity + coherence) / 3\n"
        "3. OBLIGATORIO: Devuelve SOLO una respuesta muy breve con:\n"
        "   - Puntuación total (0-100)\n"
        "   - Qué falla en el texto (máximo una línea)\n"
        "   - Recomendación clave (una frase)\n"
        "\n"
        "Formato ejemplo: 'Puntuación: 65/100. Problema: oraciones muy largas. Mejora: dividir en oraciones más cortas.'\n"
    ),
    tools=[analyze_text_readability, evaluate_text_clarity, evaluate_text_coherence],
)

print("✅ Quality agent created with text quality tools")
print("🔧 Available tools:")
print("  • analyze_text_readability - Evaluates text legibility")
print("  • evaluate_text_clarity - Evaluates clarity and precision")
print("  • evaluate_text_coherence - Evaluates structure and flow")

def _extract_response_text(result) -> str | None:
    """Extract actual response text from run_debug() result events."""
    if not isinstance(result, list):
        return None
    
    # Look through all events in reverse order
    for event in reversed(result):
        if hasattr(event, 'content') and event.content is not None:
            if hasattr(event.content, 'parts') and event.content.parts is not None:
                # Look for text parts (skip function_call and function_response)
                for part in event.content.parts:
                    if hasattr(part, 'text') and part.text:
                        return part.text
    
    return None

# Test the quality agent
if __name__ == "__main__":
    async def main():
        _ensure_api_key()
        print("\n" + "="*80)
        print("Testing quality_agent")
        print("="*80 + "\n")

        quality_runner = InMemoryRunner(
            agent=quality_agent,
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

        result = await quality_runner.run_debug(
            "Evalúa la calidad general del siguiente texto:\n\n"
            f"{sample_text}"
        )

        response_text = _extract_response_text(result)
        
        print("\n" + "="*80)
        if response_text:
            print(f"📊 RESPUESTA DEL AGENTE:\n\n{response_text}")
        else:
            print("⚠️ La respuesta no se pudo extraer.")
            print(f"\nTipo de resultado: {type(result).__name__}")
            if isinstance(result, list):
                print(f"Número de eventos: {len(result)}")
                for i, event in enumerate(result):
                    if hasattr(event, 'content'):
                        print(f"  Event {i}: content={'None' if event.content is None else 'Present'}")
        print("="*80)

    asyncio.run(main())
