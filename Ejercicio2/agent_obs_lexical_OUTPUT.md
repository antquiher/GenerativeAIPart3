✅ ADK components imported successfully.
✅ Gemini API key setup complete.
✅ Helper functions defined.
✅ Lexical metrics function created
✅ Vocabulary richness evaluation function created
✅ Lexical quality agent created with custom function tools
🔧 Available tools:
  • get_lexical_metrics - Computes vocabulary richness metrics
  • evaluate_vocabulary_richness - Evaluates lexical diversity with score and recommendations

================================================================================
Testing lexical_quality_agent
================================================================================

📊 LoggingPlugin enabled for observability
📈 CountInvocationPlugin enabled for call tracking

 ### Created new session: debug_session_id

User > Analiza la riqueza lexica y calidad del siguiente texto:

En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion y que, ademas, se ve incrementada por la falta de concrecion en los planteamientos, se pretende abordar sin delimitar los conceptos principales ni establecer un marco claro, resulta inevitable que la comprension se diluya y que el lector, en un intento poco fructifero de encontrar un hilo conductor, termine por perderse en una sucesion de ideas vagamente conectadas.
[logging_plugin] 🚀 USER MESSAGE RECEIVED
[logging_plugin]    Invocation ID: e-4a9c3d20-c69e-4ca5-874d-e51268b80e38
[logging_plugin]    Session ID: debug_session_id
[logging_plugin]    User ID: debug_user_id
[logging_plugin]    App Name: InMemoryRunner
[logging_plugin]    Root Agent: lexical_quality_agent
[logging_plugin]    User Content: text: 'Analiza la riqueza lexica y calidad del siguiente texto:

En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion y que, a...'
[logging_plugin] 🏃 INVOCATION STARTING
[logging_plugin]    Invocation ID: e-4a9c3d20-c69e-4ca5-874d-e51268b80e38
[logging_plugin]    Starting Agent: lexical_quality_agent
[logging_plugin] 🤖 AGENT STARTING
[logging_plugin]    Agent Name: lexical_quality_agent
[logging_plugin]    Invocation ID: e-4a9c3d20-c69e-4ca5-874d-e51268b80e38
[count_invocation] [Plugin] Agent run count: 1
[logging_plugin] 🧠 LLM REQUEST
[logging_plugin]    Model: gemini-2.5-flash-lite
[logging_plugin]    Agent: lexical_quality_agent
[logging_plugin]    System Instruction: 'Eres un asistente de analisis de riqueza lexica.
Usa get_lexical_metrics() y evaluate_vocabulary_richness() para analizar el texto.
Devuelve solo un resumen conciso con la evaluacion y score de calida...'
[logging_plugin]    Available Tools: ['get_lexical_metrics', 'evaluate_vocabulary_richness']
[count_invocation] [Plugin] LLM request count: 1
Warning: there are non-text parts in the response: ['function_call', 'function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
[logging_plugin] 🧠 LLM RESPONSE
[logging_plugin]    Agent: lexical_quality_agent
[logging_plugin]    Content: function_call: evaluate_vocabulary_richness | function_call: get_lexical_metrics
[logging_plugin]    Token Usage - Input: 311, Output: 242
[count_invocation] [Plugin] LLM response received: function_call: evaluate_vocabulary_richness
[logging_plugin] 📢 EVENT YIELDED
[logging_plugin]    Event ID: b0c4f44c-cc55-40c3-aa2f-a40f7d2cf3b8
[logging_plugin]    Author: lexical_quality_agent
[logging_plugin]    Content: function_call: evaluate_vocabulary_richness | function_call: get_lexical_metrics
[logging_plugin]    Final Response: False
[logging_plugin]    Function Calls: ['evaluate_vocabulary_richness', 'get_lexical_metrics']
[logging_plugin] 🔧 TOOL STARTING
[logging_plugin]    Tool Name: evaluate_vocabulary_richness
[logging_plugin]    Agent: lexical_quality_agent
[logging_plugin]    Function Call ID: adk-fafcfc68-4b8e-40bd-b59a-37accd91e570
[logging_plugin]    Arguments: {'text': 'En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion y que, ademas, se ve incrementada por la falta de concrecion en los planteamientos, se pretende abordar sin delimitar los conceptos principales ni establece...}
[count_invocation] [Plugin] Tool count: 1
[count_invocation] 🔧 TOOL STARTING
[count_invocation]    Tool Name: evaluate_vocabulary_richness
[count_invocation]    Agent: lexical_quality_agent
[count_invocation]    Function Call ID: adk-fafcfc68-4b8e-40bd-b59a-37accd91e570
[count_invocation]    Arguments: {'text': 'En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion y que, ademas, se ve incrementada por la falta de concrecion en los planteamientos, se pretende abordar sin delimitar los conceptos principales ni establece...}

[logging_plugin] 🔧 TOOL COMPLETED
[logging_plugin]    Tool Name: evaluate_vocabulary_richness
[logging_plugin]    Agent: lexical_quality_agent
[logging_plugin]    Function Call ID: adk-fafcfc68-4b8e-40bd-b59a-37accd91e570
[logging_plugin]    Result: {'status': 'success', 'quality_score': 82.0, 'quality_level': 'Bueno', 'recommendations': ['Excelente riqueza lexica y diversidad de vocabulario.']}
[count_invocation] 🔧 TOOL COMPLETED
[count_invocation]    Tool Name: evaluate_vocabulary_richness
[count_invocation]    Agent: lexical_quality_agent
[count_invocation]    Function Call ID: adk-fafcfc68-4b8e-40bd-b59a-37accd91e570
[count_invocation]    Result: {'status': 'success', 'quality_score': 82.0, 'quality_level': 'Bueno', 'recommendations': ['Excelente riqueza lexica y diversidad de vocabulario.']}
----------

[logging_plugin] 🔧 TOOL STARTING
[logging_plugin]    Tool Name: get_lexical_metrics
[logging_plugin]    Agent: lexical_quality_agent
[logging_plugin]    Function Call ID: adk-70096380-83c5-4a54-a30b-d676759f7dd8
[logging_plugin]    Arguments: {'text': 'En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion y que, ademas, se ve incrementada por la falta de concrecion en los planteamientos, se pretende abordar sin delimitar los conceptos principales ni establece...}
[count_invocation] [Plugin] Tool count: 2
[count_invocation] 🔧 TOOL STARTING
[count_invocation]    Tool Name: get_lexical_metrics
[count_invocation]    Agent: lexical_quality_agent
[count_invocation]    Function Call ID: adk-70096380-83c5-4a54-a30b-d676759f7dd8
[count_invocation]    Arguments: {'text': 'En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion y que, ademas, se ve incrementada por la falta de concrecion en los planteamientos, se pretende abordar sin delimitar los conceptos principales ni establece...}

[logging_plugin] 🔧 TOOL COMPLETED
[logging_plugin]    Tool Name: get_lexical_metrics
[logging_plugin]    Agent: lexical_quality_agent
[logging_plugin]    Function Call ID: adk-70096380-83c5-4a54-a30b-d676759f7dd8
[logging_plugin]    Result: {'status': 'success', 'num_words': 81, 'num_unique_words': 55, 'ttr': 0.679, 'rttr': 6.11, 'hapax_count': 46, 'hapax_ratio': 83.64, 'avg_word_length': 5.11, 'avg_syllables_per_word': 2.09, 'content_density': 49.38, 'lexical_diversity': 67.07}
[count_invocation] 🔧 TOOL COMPLETED
[count_invocation]    Tool Name: get_lexical_metrics
[count_invocation]    Agent: lexical_quality_agent
[count_invocation]    Function Call ID: adk-70096380-83c5-4a54-a30b-d676759f7dd8
[count_invocation]    Result: {'status': 'success', 'num_words': 81, 'num_unique_words': 55, 'ttr': 0.679, 'rttr': 6.11, 'hapax_count': 46, 'hapax_ratio': 83.64, 'avg_word_length': 5.11, 'avg_syllables_per_word': 2.09, 'content_density': 49.38, 'lexical_diversity': 67.07}
----------

[logging_plugin] 📢 EVENT YIELDED
[logging_plugin]    Event ID: 8c54eee2-cdce-491d-a622-d8490178502c
[logging_plugin]    Author: lexical_quality_agent
[logging_plugin]    Content: function_response: evaluate_vocabulary_richness | function_response: get_lexical_metrics
[logging_plugin]    Final Response: False
[logging_plugin]    Function Responses: ['evaluate_vocabulary_richness', 'get_lexical_metrics']
[logging_plugin] 🧠 LLM REQUEST
[logging_plugin]    Model: gemini-2.5-flash-lite
[logging_plugin]    Agent: lexical_quality_agent
[logging_plugin]    System Instruction: 'Eres un asistente de analisis de riqueza lexica.
Usa get_lexical_metrics() y evaluate_vocabulary_richness() para analizar el texto.
Devuelve solo un resumen conciso con la evaluacion y score de calida...'
[logging_plugin]    Available Tools: ['get_lexical_metrics', 'evaluate_vocabulary_richness']
[count_invocation] [Plugin] LLM request count: 2
[logging_plugin] 🧠 LLM RESPONSE
[logging_plugin]    Agent: lexical_quality_agent
[logging_plugin]    Content: text: 'El texto presenta una riqueza léxica y diversidad de vocabulario de nivel "Bueno", con una puntuación de 82. Se recomienda continuar con un lenguaje tan rico. Las métricas detallan una diversidad léxi...'
[logging_plugin]    Token Usage - Input: 738, Output: 70
[count_invocation] [Plugin] LLM response received: text: 'El texto presenta una riqueza léxica y diversidad de vocabulario de nivel "Bueno", con una puntuación de 82. Se recomienda continuar con un lenguaje tan rico. Las métricas detallan una diversidad léxi...'
[logging_plugin] 📢 EVENT YIELDED
[logging_plugin]    Event ID: 96454490-4a00-4afc-9172-4375eeea94ab
[logging_plugin]    Author: lexical_quality_agent
[logging_plugin]    Content: text: 'El texto presenta una riqueza léxica y diversidad de vocabulario de nivel "Bueno", con una puntuación de 82. Se recomienda continuar con un lenguaje tan rico. Las métricas detallan una diversidad léxi...'
[logging_plugin]    Final Response: True
lexical_quality_agent > El texto presenta una riqueza léxica y diversidad de vocabulario de nivel "Bueno", con una puntuación de 82. Se recomienda continuar con un lenguaje tan rico. Las métricas detallan una diversidad léxica (TTR) de 0.679 y una densidad de contenido del 49.38%.
[logging_plugin] 🤖 AGENT COMPLETED
[logging_plugin]    Agent Name: lexical_quality_agent
[logging_plugin]    Invocation ID: e-4a9c3d20-c69e-4ca5-874d-e51268b80e38
[logging_plugin] ✅ INVOCATION COMPLETED
[logging_plugin]    Invocation ID: e-4a9c3d20-c69e-4ca5-874d-e51268b80e38
[logging_plugin]    Final Agent: lexical_quality_agent

📊 Resultado:
El texto presenta una riqueza léxica y diversidad de vocabulario de nivel "Bueno", con una puntuación de 82. Se recomienda continuar con un lenguaje tan rico. Las métricas detallan una diversidad léxica (TTR) de 0.679 y una densidad de contenido del 49.38%.





================================================================================================================================================================

1.- Texto es técnico pero claro, con buena puntuación y estructura, para probar una evaluación de calidad alta

User > Por favor, analiza la calidad y legibilidad del siguiente texto:

El caso que se nos plantea tiene como base diferentes problemas de gran envergadura de manera individual, pero en su conjunto es problema de índole mayor. Según datos del PMI, los proyectos de desarrollo de software en formato waterfall presentan altos porcentajes de retrasos, sobrecostes y retrabajos, mientras que los enfoques ágiles reducen parcialmente estos riesgos. En el proyecto MedSys Online ya se han materializado varios de estos factores de riesgo.

📊 Resultado:
La riqueza léxica del texto es excelente, con un `quality_score` de 96. El texto demuestra una notable diversidad de vocabulario y utiliza un lenguaje preciso para describir la problemática. Las métricas adicionales como `lexical_diversity` (77.87) y `hapax_ratio` (87.72) respaldan esta alta calidad.


================================================================================================================================================================

2.- Texto literario con oraciones largas y uso de voz pasiva, para probar una evaluación de calidad media

User > Por favor, analiza la calidad y legibilidad del siguiente texto:

En la penumbra de la habitación, donde las sombras danzaban al ritmo de la brisa nocturna, se encontraba un anciano de mirada profunda y voz pausada, quien relataba historias de tiempos pasados con una melancolía que parecía envolver cada palabra en un manto de nostalgia, mientras el fuego crepitaba suavemente en la chimenea, creando un ambiente propicio para la introspección y el recuerdo.

📊 Resultado:
El texto presenta una **excelente riqueza léxica y diversidad de vocabulario**, con un **puntaje de calidad de 93**. Se destaca por el uso de palabras variadas y apropiadas para la atmósfera descrita, logrando una alta densidad de contenido y una notable proporción de palabras únicas.


================================================================================================================================================================

3.- Texto es historico con oraciones muy largas, uso excesivo de voz pasiva y vocabulario complejo, para probar una evaluación de calidad baja

User > Por favor, analiza la calidad y legibilidad del siguiente texto:

Durante el periodo comprendido entre los siglos XVI y XVIII, se llevaron a  cabo una serie de eventos que, aunque aparentemente desconectados, contribuyeron a moldear el curso de la historia de manera significativa, siendo la Revolución Industrial uno de los hitos más destacados, ya que no solo transformó las estructuras económicas y sociales, sino que también dio lugar a un cambio paradigmático en la forma en que las personas vivían y trabajaban, marcando el inicio de una era caracterizada por avances tecnológicos sin precedentes y por una creciente interconexión global.

📊 Resultado:
El texto presenta una riqueza léxica y diversidad de vocabulario "Excelente", con un score de calidad de 93. Los metrics indican un buen uso del lenguaje, con una diversidad léxica de 72.04 y un ratio de palabras únicas (TTR) de 0.756. Se destaca la utilización de un vocabulario variado y preciso para describir los eventos históricos y sus implicaciones.