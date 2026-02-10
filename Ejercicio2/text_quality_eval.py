"""
Text Quality Evaluator - Analyzes text quality based on readability, clarity, and coherence
"""
import re
from dataclasses import dataclass

@dataclass
class QualityScore:
    readability: float
    clarity: float
    coherence: float
    overall: float
    level: str

def analyze_readability(text: str) -> dict:
    """Analyzes text readability using Flesch metrics adapted for Spanish."""
    try:
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        num_sentences = len(sentences)
        
        words = text.split()
        num_words = len(words)
        
        if num_words < 10:
            return {"status": "error", "error": "Text too short"}
        
        avg_words_per_sentence = num_words / max(num_sentences, 1)
        
        # Syllable count
        syllable_count = 0
        vowels = 'aeioáéíóúuy'
        for word in words:
            word_clean = word.lower().rstrip('.,!?;:')
            syllables = sum(1 for char in word_clean if char in vowels)
            syllable_count += max(1, syllables)
        
        avg_syllables = syllable_count / num_words
        
        # Flesch Reading Ease (Spanish)
        fre = 206.835 - (1.3 * avg_words_per_sentence) - (60.1 * avg_syllables)
        fre = max(0, min(100, fre))
        
        if fre >= 80:
            level = "Easy to read"
            score = 90
        elif fre >= 60:
            level = "Moderate"
            score = 70
        elif fre >= 40:
            level = "Difficult"
            score = 50
        else:
            level = "Very difficult"
            score = 20
        
        return {
            "status": "success",
            "fre_score": round(fre, 1),
            "score": score,
            "level": level,
            "avg_words_per_sentence": round(avg_words_per_sentence, 1),
            "num_sentences": num_sentences
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}

def analyze_clarity(text: str) -> dict:
    """Analyzes text clarity."""
    try:
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        words = text.split()
        num_words = len(words)
        
        if num_words < 10:
            return {"status": "error", "error": "Text too short"}
        
        # Average sentence length
        avg_sent_len = sum(len(s.split()) for s in sentences) / len(sentences) if sentences else 0
        
        # Passive voice detection
        passive_count = len(re.findall(r'\b(es|son|fue|fueron)\s+\w+(ado|ada|ados|adas)\b', text, re.IGNORECASE))
        passive_ratio = passive_count / max(len(sentences), 1)
        
        # Weak words count
        weak_words = ['cosa', 'eso', 'esto', 'algo']
        weak_count = sum(text.lower().count(w) for w in weak_words)
        
        score = 100
        if avg_sent_len > 25:
            score -= 20
        elif avg_sent_len > 20:
            score -= 10
        
        if passive_ratio > 0.3:
            score -= 15
        elif passive_ratio > 0.15:
            score -= 8
        
        if weak_count > 5:
            score -= 15
        elif weak_count > 2:
            score -= 8
        
        score = max(0, min(100, score))
        
        if score >= 80:
            level = "Very clear"
        elif score >= 60:
            level = "Clear"
        elif score >= 40:
            level = "Acceptable"
        else:
            level = "Unclear"
        
        return {
            "status": "success",
            "score": score,
            "level": level,
            "avg_sentence_length": round(avg_sent_len, 1),
            "passive_ratio": round(passive_ratio * 100, 1)
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}

def analyze_coherence(text: str) -> dict:
    """Analyzes text coherence."""
    try:
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        
        if not paragraphs:
            sentences = re.split(r'[.!?]+', text)
            sentences = [s.strip() for s in sentences if s.strip()]
            paragraphs = ['. '.join(sentences[i:i+3]) for i in range(0, len(sentences), 3)]
        
        # Transition words
        transitions = ['sin embargo', 'por lo tanto', 'en conclusión', 'además', 'asimismo']
        trans_count = sum(text.lower().count(t) for t in transitions)
        
        score = 100
        
        if len(paragraphs) < 2:
            score -= 20
        
        if trans_count == 0:
            score -= 15
        elif trans_count < 2:
            score -= 8
        
        score = max(0, min(100, score))
        
        if score >= 80:
            level = "Very coherent"
        elif score >= 60:
            level = "Coherent"
        elif score >= 40:
            level = "Acceptable"
        else:
            level = "Incoherent"
        
        return {
            "status": "success",
            "score": score,
            "level": level,
            "num_paragraphs": len(paragraphs),
            "transition_count": trans_count
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}

def evaluate_text(text: str) -> dict:
    """Comprehensive text quality evaluation."""
    readability = analyze_readability(text)
    clarity = analyze_clarity(text)
    coherence = analyze_coherence(text)
    
    # Calculate overall score
    if all(r["status"] == "success" for r in [readability, clarity, coherence]):
        overall = (readability["score"] + clarity["score"] + coherence["score"]) / 3
        
        if overall >= 80:
            level = "Excellent"
        elif overall >= 65:
            level = "Good"
        elif overall >= 50:
            level = "Fair"
        else:
            level = "Poor"
    else:
        overall = 0
        level = "Error"
    
    return {
        "overall_score": round(overall, 1),
        "overall_level": level,
        "readability": readability,
        "clarity": clarity,
        "coherence": coherence
    }

if __name__ == "__main__":
    # Test text
    sample_text = (
        "En la medida en que la complejidad inherente a la problematica, que ya de por si "
        "se manifiesta en multiples niveles de interpretacion y que, ademas, se ve incrementada "
        "por la falta de concrecion en los planteamientos, se pretende abordar sin delimitar "
        "los conceptos principales ni establecer un marco claro, resulta inevitable que la "
        "comprension se diluya y que el lector, en un intento poco fructifero de encontrar un "
        "hilo conductor, termine por perderse en una sucesion de ideas vagamente conectadas."
    )
    
    print("\n" + "="*70)
    print("TEXT QUALITY EVALUATION")
    print("="*70 + "\n")
    
    result = evaluate_text(sample_text)
    
    print(f"📊 OVERALL QUALITY: {result['overall_score']}/100 ({result['overall_level']})\n")
    
    print(f"📖 Readability: {result['readability']['score']}/100 - {result['readability']['level']}")
    if result['readability']['status'] == 'success':
        print(f"   → FRE Score: {result['readability']['fre_score']}")
        print(f"   → Avg words/sentence: {result['readability']['avg_words_per_sentence']}")
    
    print(f"\n💡 Clarity: {result['clarity']['score']}/100 - {result['clarity']['level']}")
    if result['clarity']['status'] == 'success':
        print(f"   → Avg sentence length: {result['clarity']['avg_sentence_length']} words")
        print(f"   → Passive voice: {result['clarity']['passive_ratio']}%")
    
    print(f"\n🔗 Coherence: {result['coherence']['score']}/100 - {result['coherence']['level']}")
    if result['coherence']['status'] == 'success':
        print(f"   → Paragraphs: {result['coherence']['num_paragraphs']}")
        print(f"   → Transition phrases: {result['coherence']['transition_count']}")
    
    print("\n" + "="*70 + "\n")
