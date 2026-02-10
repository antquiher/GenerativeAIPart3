import re
import math
from dataclasses import dataclass
from typing import List
from collections import Counter

# -------------------------
# Utilidades básicas
# -------------------------

VOWELS = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"

FUNCTION_WORDS = {
    "el", "la", "los", "las", "un", "una", "unos", "unas",
    "de", "del", "a", "al", "en", "con", "por", "para", "sin", "sobre",
    "y", "e", "o", "u", "pero", "sino", "ni", "que", "si",
    "me", "te", "se", "le", "lo", "nos", "os", "les", "mi", "tu", "su",
    "este", "ese", "aquel", "esta", "esa", "aquella",
    "muy", "más", "menos", "tan", "tanto", "también", "tampoco",
    "no", "sí", "como", "cuando", "donde", "cual", "quien"
}


def tokenize_words(text: str) -> List[str]:
    """Extrae palabras (tokens alfabéticos) de un texto."""
    return re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+", text)


def count_syllables_es(word: str) -> int:
    """Conteo aproximado de sílabas en español."""
    word = word.lower()
    word = re.sub(r"y$", "i", word)
    groups = re.findall(f"[{VOWELS}]+", word)
    syllables = len(groups)
    return max(1, syllables)


# -------------------------
# Métricas léxicas
# -------------------------

@dataclass
class LexicalMetrics:
    num_words: int              # Total de palabras
    num_unique_words: int       # Palabras únicas
    ttr: float                  # Type-Token Ratio: unique/total
    rttr: float                 # Root TTR: unique/sqrt(total)
    hapax_count: int            # Palabras que aparecen solo una vez
    hapax_ratio: float          # Ratio de hapax legomena
    avg_word_length: float      # Longitud promedio de palabra (caracteres)
    avg_syllables_per_word: float  # Promedio de sílabas por palabra
    content_density: float      # % de palabras de contenido (no funcionales)
    lexical_diversity: float    # Índice de diversidad (0-100)


def compute_lexical_metrics(text: str) -> LexicalMetrics:
    """Calcula métricas de riqueza léxica y diversidad de vocabulario."""
    words_raw = tokenize_words(text)
    
    if not words_raw:
        raise ValueError("El texto está vacío o no contiene palabras reconocibles.")
    
    # Normalizar a minúsculas para análisis
    words = [w.lower() for w in words_raw]
    num_words = len(words)
    
    # Palabras únicas
    word_counts = Counter(words)
    num_unique_words = len(word_counts)
    
    # Type-Token Ratio (TTR)
    ttr = num_unique_words / num_words if num_words > 0 else 0.0
    
    # Root TTR (más estable para textos de diferente longitud)
    rttr = num_unique_words / math.sqrt(num_words) if num_words > 0 else 0.0
    
    # Hapax Legomena (palabras que aparecen solo una vez)
    hapax_count = sum(1 for count in word_counts.values() if count == 1)
    hapax_ratio = (hapax_count / num_unique_words * 100) if num_unique_words > 0 else 0.0
    
    # Longitud promedio de palabra
    avg_word_length = sum(len(w) for w in words) / num_words
    
    # Promedio de sílabas por palabra
    total_syllables = sum(count_syllables_es(w) for w in words)
    avg_syllables = total_syllables / num_words
    
    # Densidad de contenido (palabras no funcionales)
    content_words = [w for w in words if w not in FUNCTION_WORDS]
    content_density = (len(content_words) / num_words * 100) if num_words > 0 else 0.0
    
    # Índice de diversidad léxica (0-100)
    # Combinación de TTR, hapax ratio y content density
    diversity_score = (
        ttr * 40 +  # TTR normalizado a 40 puntos
        (hapax_ratio / 100) * 30 +  # Hapax ratio a 30 puntos
        (content_density / 100) * 30  # Content density a 30 puntos
    )
    
    return LexicalMetrics(
        num_words=num_words,
        num_unique_words=num_unique_words,
        ttr=ttr,
        rttr=rttr,
        hapax_count=hapax_count,
        hapax_ratio=hapax_ratio,
        avg_word_length=avg_word_length,
        avg_syllables_per_word=avg_syllables,
        content_density=content_density,
        lexical_diversity=diversity_score,
    )


# -------------------------
# Ejemplo de uso
# -------------------------

if __name__ == "__main__":
    sample_text = """
    En la medida en que la complejidad inherente a la problemática, que ya de por sí 
    se manifiesta en múltiples niveles de interpretación y que, además, se ve incrementada 
    por la falta de concreción en los planteamientos, se pretende abordar sin delimitar 
    los conceptos principales ni establecer un marco claro, resulta inevitable que la 
    comprensión se diluya.
    """
    
    metrics = compute_lexical_metrics(sample_text)
    
    print("=== MÉTRICAS LÉXICAS ===")
    print(f"Total palabras: {metrics.num_words}")
    print(f"Palabras únicas: {metrics.num_unique_words}")
    print(f"Type-Token Ratio (TTR): {metrics.ttr:.3f}")
    print(f"Root TTR: {metrics.rttr:.2f}")
    print(f"Hapax legomena: {metrics.hapax_count} ({metrics.hapax_ratio:.1f}%)")
    print(f"Longitud promedio palabra: {metrics.avg_word_length:.2f} caracteres")
    print(f"Sílabas por palabra: {metrics.avg_syllables_per_word:.2f}")
    print(f"Densidad de contenido: {metrics.content_density:.1f}%")
    print(f"Diversidad léxica: {metrics.lexical_diversity:.1f}/100")
