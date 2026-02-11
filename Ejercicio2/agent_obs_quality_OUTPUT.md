✅ ADK components imported successfully.
✅ Gemini API key setup complete.
✅ Helper functions defined.
✅ Text quality analysis functions created
✅ Quality agent created with text quality tools
🔧 Available tools:
  • analyze_text_readability - Evaluates text legibility
  • evaluate_text_clarity - Evaluates clarity and precision
  • evaluate_text_coherence - Evaluates structure and flow

================================================================================
Testing quality_agent
================================================================================

📊 LoggingPlugin enabled for observability
📈 CountInvocationPlugin enabled for call tracking

 ### Created new session: debug_session_id

User > Evalúa la calidad general del siguiente texto:

En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion y que, ademas, se ve incrementada por la falta de concrecion en los planteamientos, se pretende abordar sin delimitar los conceptos principales ni establecer un marco claro, resulta inevitable que la comprension se diluya y que el lector, en un intento poco fructifero de encontrar un hilo conductor, termine por perderse en una sucesion de ideas vagamente conectadas.
[logging_plugin] 🚀 USER MESSAGE RECEIVED
[logging_plugin]    Invocation ID: e-6cc287df-8bd2-4ee3-86e5-ad61785ecea7
[logging_plugin]    Session ID: debug_session_id
[logging_plugin]    User ID: debug_user_id
[logging_plugin]    App Name: InMemoryRunner
[logging_plugin]    Root Agent: quality_agent
[logging_plugin]    User Content: text: 'Evalúa la calidad general del siguiente texto:

En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion y que, ademas, se ...'
[logging_plugin] 🏃 INVOCATION STARTING
[logging_plugin]    Invocation ID: e-6cc287df-8bd2-4ee3-86e5-ad61785ecea7
[logging_plugin]    Starting Agent: quality_agent
[logging_plugin] 🤖 AGENT STARTING
[logging_plugin]    Agent Name: quality_agent
[logging_plugin]    Invocation ID: e-6cc287df-8bd2-4ee3-86e5-ad61785ecea7
[count_invocation] [Plugin] Agent run count: 1
[logging_plugin] 🧠 LLM REQUEST
[logging_plugin]    Model: gemini-2.5-flash
[logging_plugin]    Agent: quality_agent
[logging_plugin]    System Instruction: 'Eres un evaluador de calidad de textos.

1. Llama a analyze_text_readability(), evaluate_text_clarity() y evaluate_text_coherence()
2. Calcula la puntuación general: (readability + clarity + coherence...'
[logging_plugin]    Available Tools: ['analyze_text_readability', 'evaluate_text_clarity', 'evaluate_text_coherence']
[count_invocation] [Plugin] LLM request count: 1
Warning: there are non-text parts in the response: ['function_call', 'function_call', 'function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
[logging_plugin] 🧠 LLM RESPONSE
[logging_plugin]    Agent: quality_agent
[logging_plugin]    Content: function_call: analyze_text_readability | function_call: evaluate_text_clarity | function_call: evaluate_text_coherence
[logging_plugin]    Token Usage - Input: 517, Output: 363
[count_invocation] [Plugin] LLM response received: function_call: analyze_text_readability
[logging_plugin] 📢 EVENT YIELDED
[logging_plugin]    Event ID: cea586c7-5b04-480b-91b4-2e07dcea1026
[logging_plugin]    Author: quality_agent
[logging_plugin]    Content: function_call: analyze_text_readability | function_call: evaluate_text_clarity | function_call: evaluate_text_coherence
[logging_plugin]    Final Response: False
[logging_plugin]    Function Calls: ['analyze_text_readability', 'evaluate_text_clarity', 'evaluate_text_coherence']
[logging_plugin] 🔧 TOOL STARTING
[logging_plugin]    Tool Name: analyze_text_readability
[logging_plugin]    Agent: quality_agent
[logging_plugin]    Function Call ID: adk-bff04549-b22a-49b2-81f0-70c4d054700c
[logging_plugin]    Arguments: {'text': 'En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion y que, ademas, se ve incrementada por la falta de concrecion en los planteamientos, se pretende abordar sin delimitar los conceptos principales ni establece...}
[count_invocation] [Plugin] Tool count: 1
[count_invocation] 🔧 TOOL STARTING
[count_invocation]    Tool Name: analyze_text_readability
[count_invocation]    Agent: quality_agent
[count_invocation]    Function Call ID: adk-bff04549-b22a-49b2-81f0-70c4d054700c
[count_invocation]    Arguments: {'text': 'En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion y que, ademas, se ve incrementada por la falta de concrecion en los planteamientos, se pretende abordar sin delimitar los conceptos principales ni establece...}

[logging_plugin] 🔧 TOOL COMPLETED
[logging_plugin]    Tool Name: analyze_text_readability
[logging_plugin]    Agent: quality_agent
[logging_plugin]    Function Call ID: adk-bff04549-b22a-49b2-81f0-70c4d054700c
[logging_plugin]    Result: {'status': 'success', 'fre_score': 0, 'fkg_grade': 42.8, 'readability_level': 'Extremadamente Complejo', 'readability_score': 15, 'avg_words_per_sentence': 81.0, 'avg_syllables_per_word': 2.27, 'num_sentences': 1, 'num_words': 81}
[count_invocation] 🔧 TOOL COMPLETED
[count_invocation]    Tool Name: analyze_text_readability
[count_invocation]    Agent: quality_agent
[count_invocation]    Function Call ID: adk-bff04549-b22a-49b2-81f0-70c4d054700c
[count_invocation]    Result: {'status': 'success', 'fre_score': 0, 'fkg_grade': 42.8, 'readability_level': 'Extremadamente Complejo', 'readability_score': 15, 'avg_words_per_sentence': 81.0, 'avg_syllables_per_word': 2.27, 'num_sentences': 1, 'num_words': 81}
----------

[logging_plugin] 🔧 TOOL STARTING
[logging_plugin]    Tool Name: evaluate_text_clarity
[logging_plugin]    Agent: quality_agent
[logging_plugin]    Function Call ID: adk-81c4a814-377a-4c3c-b70a-075c48cf3fa1
[logging_plugin]    Arguments: {'text': 'En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion y que, ademas, se ve incrementada por la falta de concrecion en los planteamientos, se pretende abordar sin delimitar los conceptos principales ni establece...}
[count_invocation] [Plugin] Tool count: 2
[count_invocation] 🔧 TOOL STARTING
[count_invocation]    Tool Name: evaluate_text_clarity
[count_invocation]    Agent: quality_agent
[count_invocation]    Function Call ID: adk-81c4a814-377a-4c3c-b70a-075c48cf3fa1
[count_invocation]    Arguments: {'text': 'En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion y que, ademas, se ve incrementada por la falta de concrecion en los planteamientos, se pretende abordar sin delimitar los conceptos principales ni establece...}

[logging_plugin] 🔧 TOOL COMPLETED
[logging_plugin]    Tool Name: evaluate_text_clarity
[logging_plugin]    Agent: quality_agent
[logging_plugin]    Function Call ID: adk-81c4a814-377a-4c3c-b70a-075c48cf3fa1
[logging_plugin]    Result: {'status': 'success', 'clarity_score': 80, 'clarity_level': 'Clara', 'avg_sentence_length': 81.0, 'passive_voice_percentage': 0.0, 'weak_word_count': 0, 'recommendations': []}
[count_invocation] 🔧 TOOL COMPLETED
[count_invocation]    Tool Name: evaluate_text_clarity
[count_invocation]    Agent: quality_agent
[count_invocation]    Function Call ID: adk-81c4a814-377a-4c3c-b70a-075c48cf3fa1
[count_invocation]    Result: {'status': 'success', 'clarity_score': 80, 'clarity_level': 'Clara', 'avg_sentence_length': 81.0, 'passive_voice_percentage': 0.0, 'weak_word_count': 0, 'recommendations': []}
----------

[logging_plugin] 🔧 TOOL STARTING
[logging_plugin]    Tool Name: evaluate_text_coherence
[logging_plugin]    Agent: quality_agent
[logging_plugin]    Function Call ID: adk-333fd5ed-8099-4413-a821-8c1fc4f2467b
[logging_plugin]    Arguments: {'text': 'En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion y que, ademas, se ve incrementada por la falta de concrecion en los planteamientos, se pretende abordar sin delimitar los conceptos principales ni establece...}
[count_invocation] [Plugin] Tool count: 3
[count_invocation] 🔧 TOOL STARTING
[count_invocation]    Tool Name: evaluate_text_coherence
[count_invocation]    Agent: quality_agent
[count_invocation]    Function Call ID: adk-333fd5ed-8099-4413-a821-8c1fc4f2467b
[count_invocation]    Arguments: {'text': 'En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion y que, ademas, se ve incrementada por la falta de concrecion en los planteamientos, se pretende abordar sin delimitar los conceptos principales ni establece...}

[logging_plugin] 🔧 TOOL COMPLETED
[logging_plugin]    Tool Name: evaluate_text_coherence
[logging_plugin]    Agent: quality_agent
[logging_plugin]    Function Call ID: adk-333fd5ed-8099-4413-a821-8c1fc4f2467b
[logging_plugin]    Result: {'status': 'success', 'coherence_score': 65, 'coherence_level': 'Aceptable', 'num_paragraphs': 1, 'avg_paragraph_length': 81.0, 'transition_phrases_count': 0}
[count_invocation] 🔧 TOOL COMPLETED
[count_invocation]    Tool Name: evaluate_text_coherence
[count_invocation]    Agent: quality_agent
[count_invocation]    Function Call ID: adk-333fd5ed-8099-4413-a821-8c1fc4f2467b
[count_invocation]    Result: {'status': 'success', 'coherence_score': 65, 'coherence_level': 'Aceptable', 'num_paragraphs': 1, 'avg_paragraph_length': 81.0, 'transition_phrases_count': 0}
----------

[logging_plugin] 📢 EVENT YIELDED
[logging_plugin]    Event ID: bac8e6f1-f6f2-447d-9539-27ebaeb0b267
[logging_plugin]    Author: quality_agent
[logging_plugin]    Content: function_response: analyze_text_readability | function_response: evaluate_text_clarity | function_response: evaluate_text_coherence
[logging_plugin]    Final Response: False
[logging_plugin]    Function Responses: ['analyze_text_readability', 'evaluate_text_clarity', 'evaluate_text_coherence']
[logging_plugin] 🧠 LLM REQUEST
[logging_plugin]    Model: gemini-2.5-flash
[logging_plugin]    Agent: quality_agent
[logging_plugin]    System Instruction: 'Eres un evaluador de calidad de textos.

1. Llama a analyze_text_readability(), evaluate_text_clarity() y evaluate_text_coherence()
2. Calcula la puntuación general: (readability + clarity + coherence...'
[logging_plugin]    Available Tools: ['analyze_text_readability', 'evaluate_text_clarity', 'evaluate_text_coherence']
[count_invocation] [Plugin] LLM request count: 2
[logging_plugin] 🧠 LLM RESPONSE
[logging_plugin]    Agent: quality_agent
[logging_plugin]    Content: text: 'Puntuación: 53/100. Problema: Oración excesivamente larga y compleja que dificulta la comprensión. Mejora: Divide la oración en varias más cortas y claras.'
[logging_plugin]    Token Usage - Input: 1127, Output: 42
[count_invocation] [Plugin] LLM response received: 
[logging_plugin] 📢 EVENT YIELDED
[logging_plugin]    Event ID: c440f4d0-5cfc-4abb-8ca8-3e67ea135b4f
[logging_plugin]    Author: quality_agent
[logging_plugin]    Content: text: 'Puntuación: 53/100. Problema: Oración excesivamente larga y compleja que dificulta la comprensión. Mejora: Divide la oración en varias más cortas y claras.'
[logging_plugin]    Final Response: True
quality_agent > Puntuación: 53/100. Problema: Oración excesivamente larga y compleja que dificulta la comprensión. Mejora: Divide la oración en varias más cortas y claras.
[logging_plugin] 🤖 AGENT COMPLETED
[logging_plugin]    Agent Name: quality_agent
[logging_plugin]    Invocation ID: e-6cc287df-8bd2-4ee3-86e5-ad61785ecea7
[logging_plugin] ✅ INVOCATION COMPLETED
[logging_plugin]    Invocation ID: e-6cc287df-8bd2-4ee3-86e5-ad61785ecea7
[logging_plugin]    Final Agent: quality_agent

================================================================================
📊 RESPUESTA DEL AGENTE:

Puntuación: 53/100. Problema: Oración excesivamente larga y compleja que dificulta la comprensión. Mejora: Divide la oración en varias más cortas y claras.
================================================================================





================================================================================================================================================================

1.- Texto es técnico pero claro, con buena puntuación y estructura, para probar una evaluación de calidad alta

User > Por favor, analiza la calidad y legibilidad del siguiente texto:

El caso que se nos plantea tiene como base diferentes problemas de gran envergadura de manera individual, pero en su conjunto es problema de índole mayor. Según datos del PMI, los proyectos de desarrollo de software en formato waterfall presentan altos porcentajes de retrasos, sobrecostes y retrabajos, mientras que los enfoques ágiles reducen parcialmente estos riesgos. En el proyecto MedSys Online ya se han materializado varios de estos factores de riesgo.

📊 RESPUESTA DEL AGENTE:

Puntuación: 63/100. Problema: Oraciones muy largas. Mejora: Dividir oraciones en fragmentos más cortos y usar más transiciones.

================================================================================================================================================================

2.- Texto literario con oraciones largas y uso de voz pasiva, para probar una evaluación de calidad media

User > Por favor, analiza la calidad y legibilidad del siguiente texto:

En la penumbra de la habitación, donde las sombras danzaban al ritmo de la brisa nocturna, se encontraba un anciano de mirada profunda y voz pausada, quien relataba historias de tiempos pasados con una melancolía que parecía envolver cada palabra en un manto de nostalgia, mientras el fuego crepitaba suavemente en la chimenea, creando un ambiente propicio para la introspección y el recuerdo.

📊 RESPUESTA DEL AGENTE:

Puntuación: 53/100. Problema: Oración extremadamente larga que dificulta la lectura. Mejora: Dividir la oración en frases más cortas para aumentar la legibilidad.


================================================================================================================================================================

3.- Texto es historico con oraciones muy largas, uso excesivo de voz pasiva y vocabulario complejo, para probar una evaluación de calidad baja

User > Por favor, analiza la calidad y legibilidad del siguiente texto:

Durante el periodo comprendido entre los siglos XVI y XVIII, se llevaron a  cabo una serie de eventos que, aunque aparentemente desconectados, contribuyeron a moldear el curso de la historia de manera significativa, siendo la Revolución Industrial uno de los hitos más destacados, ya que no solo transformó las estructuras económicas y sociales, sino que también dio lugar a un cambio paradigmático en la forma en que las personas vivían y trabajaban, marcando el inicio de una era caracterizada por avances tecnológicos sin precedentes y por una creciente interconexión global.

📊 RESPUESTA DEL AGENTE:

Puntuación: 53/100. Problema: El texto es una única oración extremadamente larga. Mejora: Dividir la oración en varias más cortas para facilitar la comprensión.