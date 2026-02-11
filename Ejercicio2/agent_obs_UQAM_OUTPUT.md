✅ ADK components imported successfully.
✅ Gemini API key setup complete.
✅ Helper functions defined.
✅ Text metrics function created
✅ Text quality evaluation function created
✅ Text quality agent created with custom function tools
🔧 Available tools:
  • get_text_metrics - Computes detailed readability metrics
  • evaluate_text_quality - Evaluates text quality with score and recommendations

================================================================================
Testing text_quality_agent
================================================================================

📊 LoggingPlugin enabled for observability
📈 CountInvocationPlugin enabled for call tracking

 ### Created new session: debug_session_id

User > Por favor, analiza la calidad y legibilidad del siguiente texto:

En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion y que, ademas, se ve incrementada por la falta de concrecion en los planteamientos, se pretende abordar sin delimitar los conceptos principales ni establecer un marco claro, resulta inevitable que la comprension se diluya y que el lector, en un intento poco fructifero de encontrar un hilo conductor, termine por perderse en una sucesion de ideas vagamente conectadas, donde cada afirmacion parece depender de otra que no se explica y donde la precision brilla por su ausencia.
[logging_plugin] 🚀 USER MESSAGE RECEIVED
[logging_plugin]    Invocation ID: e-61c28fe7-b790-428b-b0be-264eebf6b6da
[logging_plugin]    Session ID: debug_session_id
[logging_plugin]    User ID: debug_user_id
[logging_plugin]    App Name: InMemoryRunner
[logging_plugin]    Root Agent: text_quality_agent
[logging_plugin]    User Content: text: 'Por favor, analiza la calidad y legibilidad del siguiente texto:

En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion ...'
[logging_plugin] 🏃 INVOCATION STARTING
[logging_plugin]    Invocation ID: e-61c28fe7-b790-428b-b0be-264eebf6b6da
[logging_plugin]    Starting Agent: text_quality_agent
[logging_plugin] 🤖 AGENT STARTING
[logging_plugin]    Agent Name: text_quality_agent
[logging_plugin]    Invocation ID: e-61c28fe7-b790-428b-b0be-264eebf6b6da
[count_invocation] [Plugin] Agent run count: 1
[logging_plugin] 🧠 LLM REQUEST
[logging_plugin]    Model: gemini-2.5-flash-lite
[logging_plugin]    Agent: text_quality_agent
[logging_plugin]    System Instruction: 'Eres un asistente experto en analisis de calidad de textos en espanol.

Para analizar textos:
1. Usa get_text_metrics() para obtener metricas detalladas de legibilidad
2. Usa evaluate_text_quality() p...'
[logging_plugin]    Available Tools: ['get_text_metrics', 'evaluate_text_quality']
[count_invocation] [Plugin] LLM request count: 1
Warning: there are non-text parts in the response: ['function_call', 'function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
[logging_plugin] 🧠 LLM RESPONSE
[logging_plugin]    Agent: text_quality_agent
[logging_plugin]    Content: function_call: get_text_metrics | function_call: evaluate_text_quality
[logging_plugin]    Token Usage - Input: 386, Output: 284
[count_invocation] [Plugin] LLM response received: function_call: get_text_metrics
[logging_plugin] 📢 EVENT YIELDED
[logging_plugin]    Event ID: 985c0e16-848c-4fd8-9cdb-2e9558f7c595
[logging_plugin]    Author: text_quality_agent
[logging_plugin]    Content: function_call: get_text_metrics | function_call: evaluate_text_quality
[logging_plugin]    Final Response: False
[logging_plugin]    Function Calls: ['get_text_metrics', 'evaluate_text_quality']
[logging_plugin] 🔧 TOOL STARTING
[logging_plugin]    Tool Name: get_text_metrics
[logging_plugin]    Agent: text_quality_agent
[logging_plugin]    Function Call ID: adk-14840f53-1cef-44ce-91b2-84432134e43b
[logging_plugin]    Arguments: {'text': 'En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion y que, ademas, se ve incrementada por la falta de concrecion en los planteamientos, se pretende abordar sin delimitar los conceptos principales ni establece...}
[count_invocation] [Plugin] Tool count: 1
[count_invocation] 🔧 TOOL STARTING
[count_invocation]    Tool Name: get_text_metrics
[count_invocation]    Agent: text_quality_agent
[count_invocation]    Function Call ID: adk-14840f53-1cef-44ce-91b2-84432134e43b
[count_invocation]    Arguments: {'text': 'En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion y que, ademas, se ve incrementada por la falta de concrecion en los planteamientos, se pretende abordar sin delimitar los conceptos principales ni establece...}

[logging_plugin] 🔧 TOOL COMPLETED
[logging_plugin]    Tool Name: get_text_metrics
[logging_plugin]    Agent: text_quality_agent
[logging_plugin]    Function Call ID: adk-14840f53-1cef-44ce-91b2-84432134e43b
[logging_plugin]    Result: {'status': 'success', 'num_sentences': 1, 'num_words': 100, 'num_syllables': 206, 'lmo': 100.0, 'std_sentence_len': 0.0, 'cv_sentence_len': 0.0, 'z_normality': 16.0, 'flesch_szigriszt': -23.0, 'passive_ratio': 0.0}
[count_invocation] 🔧 TOOL COMPLETED
[count_invocation]    Tool Name: get_text_metrics
[count_invocation]    Agent: text_quality_agent
[count_invocation]    Function Call ID: adk-14840f53-1cef-44ce-91b2-84432134e43b
[count_invocation]    Result: {'status': 'success', 'num_sentences': 1, 'num_words': 100, 'num_syllables': 206, 'lmo': 100.0, 'std_sentence_len': 0.0, 'cv_sentence_len': 0.0, 'z_normality': 16.0, 'flesch_szigriszt': -23.0, 'passive_ratio': 0.0}
----------

[logging_plugin] 🔧 TOOL STARTING
[logging_plugin]    Tool Name: evaluate_text_quality
[logging_plugin]    Agent: text_quality_agent
[logging_plugin]    Function Call ID: adk-6da64dbb-071e-47c2-9822-154ad9f3e95d
[logging_plugin]    Arguments: {'text': 'En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion y que, ademas, se ve incrementada por la falta de concrecion en los planteamientos, se pretende abordar sin delimitar los conceptos principales ni establece...}
[count_invocation] [Plugin] Tool count: 2
[count_invocation] 🔧 TOOL STARTING
[count_invocation]    Tool Name: evaluate_text_quality
[count_invocation]    Agent: text_quality_agent
[count_invocation]    Function Call ID: adk-6da64dbb-071e-47c2-9822-154ad9f3e95d
[count_invocation]    Arguments: {'text': 'En la medida en que la complejidad inherente a la problematica, que ya de por si se manifiesta en multiples niveles de interpretacion y que, ademas, se ve incrementada por la falta de concrecion en los planteamientos, se pretende abordar sin delimitar los conceptos principales ni establece...}

[logging_plugin] 🔧 TOOL COMPLETED
[logging_plugin]    Tool Name: evaluate_text_quality
[logging_plugin]    Agent: text_quality_agent
[logging_plugin]    Function Call ID: adk-6da64dbb-071e-47c2-9822-154ad9f3e95d
[logging_plugin]    Result: {'status': 'success', 'quality_score': 45.0, 'quality_level': 'Mejorable', 'recommendations': ['El texto es muy dificil de leer. Usa oraciones mas cortas y palabras simples.', 'Oraciones demasiado largas (promedio: 100.0 palabras). Divide algunas oraciones.', 'Varia la longitud de las oraciones para...}
[count_invocation] 🔧 TOOL COMPLETED
[count_invocation]    Tool Name: evaluate_text_quality
[count_invocation]    Agent: text_quality_agent
[count_invocation]    Function Call ID: adk-6da64dbb-071e-47c2-9822-154ad9f3e95d
[count_invocation]    Result: {'status': 'success', 'quality_score': 45.0, 'quality_level': 'Mejorable', 'recommendations': ['El texto es muy dificil de leer. Usa oraciones mas cortas y palabras simples.', 'Oraciones demasiado largas (promedio: 100.0 palabras). Divide algunas oraciones.', 'Varia la longitud de las oraciones para...}
----------

[logging_plugin] 📢 EVENT YIELDED
[logging_plugin]    Event ID: 7ab04ece-b76c-495d-ad60-fb3d735e46a2
[logging_plugin]    Author: text_quality_agent
[logging_plugin]    Content: function_response: get_text_metrics | function_response: evaluate_text_quality
[logging_plugin]    Final Response: False
[logging_plugin]    Function Responses: ['get_text_metrics', 'evaluate_text_quality']
[logging_plugin] 🧠 LLM REQUEST
[logging_plugin]    Model: gemini-2.5-flash-lite
[logging_plugin]    Agent: text_quality_agent
[logging_plugin]    System Instruction: 'Eres un asistente experto en analisis de calidad de textos en espanol.

Para analizar textos:
1. Usa get_text_metrics() para obtener metricas detalladas de legibilidad
2. Usa evaluate_text_quality() p...'
[logging_plugin]    Available Tools: ['get_text_metrics', 'evaluate_text_quality']
[count_invocation] [Plugin] LLM request count: 2
[logging_plugin] 🧠 LLM RESPONSE
[logging_plugin]    Agent: text_quality_agent
[logging_plugin]    Content: text: 'El texto proporcionado tiene una calidad "Mejorable" con una puntuación de 45. Se recomienda simplificar el lenguaje y acortar las oraciones para facilitar la lectura. Actualmente, el promedio de pala...'
[logging_plugin]    Token Usage - Input: 872, Output: 87
[count_invocation] [Plugin] LLM response received: text: 'El texto proporcionado tiene una calidad "Mejorable" con una puntuación de 45. Se recomienda simplificar el lenguaje y acortar las oraciones para facilitar la lectura. Actualmente, el promedio de pala...'
[logging_plugin] 📢 EVENT YIELDED
[logging_plugin]    Event ID: 6a951772-935c-41c6-9092-2d3d0ef6fe38
[logging_plugin]    Author: text_quality_agent
[logging_plugin]    Content: text: 'El texto proporcionado tiene una calidad "Mejorable" con una puntuación de 45. Se recomienda simplificar el lenguaje y acortar las oraciones para facilitar la lectura. Actualmente, el promedio de pala...'
[logging_plugin]    Final Response: True
text_quality_agent > El texto proporcionado tiene una calidad "Mejorable" con una puntuación de 45. Se recomienda simplificar el lenguaje y acortar las oraciones para facilitar la lectura. Actualmente, el promedio de palabras por oración es de 100.0, lo cual dificulta la comprensión. Sería beneficioso dividir las oraciones largas y variar su longitud para mejorar el ritmo y la fluidez del texto.
[logging_plugin] 🤖 AGENT COMPLETED
[logging_plugin]    Agent Name: text_quality_agent
[logging_plugin]    Invocation ID: e-61c28fe7-b790-428b-b0be-264eebf6b6da
[logging_plugin] ✅ INVOCATION COMPLETED
[logging_plugin]    Invocation ID: e-61c28fe7-b790-428b-b0be-264eebf6b6da
[logging_plugin]    Final Agent: text_quality_agent
✅ Respuesta de Gemini:
El texto proporcionado tiene una calidad "Mejorable" con una puntuación de 45. Se recomienda simplificar el lenguaje y acortar las oraciones para facilitar la lectura. Actualmente, el promedio de palabras por oración es de 100.0, lo cual dificulta la comprensión. Sería beneficioso dividir las oraciones largas y variar su longitud para mejorar el ritmo y la fluidez del texto.



================================================================================================================================================================

1.- Texto es técnico pero claro, con buena puntuación y estructura, para probar una evaluación de calidad alta

User > Por favor, analiza la calidad y legibilidad del siguiente texto:

El caso que se nos plantea tiene como base diferentes problemas de gran envergadura de manera individual, pero en su conjunto es problema de índole mayor. Según datos del PMI, los proyectos de desarrollo de software en formato waterfall presentan altos porcentajes de retrasos, sobrecostes y retrabajos, mientras que los enfoques ágiles reducen parcialmente estos riesgos. En el proyecto MedSys Online ya se han materializado varios de estos factores de riesgo.

✅ Respuesta de Gemini:
El texto proporcionado tiene una calidad **Excelente** con una puntuación de **85**.

**Métricas de Legibilidad:**

*   **Número de palabras:** 71
*   **Número de oraciones:** 3
*   **Longitud media de oración (palabras):** 23.67
*   **Número de sílabas:** 151
*   **Índice Flesch-Szigriszt:** 50.32

**Recomendaciones:**
*   Excelente legibilidad del texto.

¡Felicidades, el texto es de alta calidad!

================================================================================================================================================================

2.- Texto literario con oraciones largas y uso de voz pasiva, para probar una evaluación de calidad media

User > Por favor, analiza la calidad y legibilidad del siguiente texto:

En la penumbra de la habitación, donde las sombras danzaban al ritmo de la brisa nocturna, se encontraba un anciano de mirada profunda y voz pausada, quien relataba historias de tiempos pasados con una melancolía que parecía envolver cada palabra en un manto de nostalgia, mientras el fuego crepitaba suavemente en la chimenea, creando un ambiente propicio para la introspección y el recuerdo.

✅ Respuesta de Gemini:
El texto proporcionado tiene una calidad "Mejorable" con una puntuación de 45.

**Métricas de legibilidad:**
*   **Número de palabras:** 63
*   **Número de oraciones:** 1
*   **Número de sílabas:** 130
*   **Longitud media de oración:** 63.0 palabras
*   **Índice Flesch-Szigriszt:** 14.33

**Recomendaciones:**
*   El texto es muy difícil de leer. Se sugiere usar oraciones más cortas y palabras más simples.
*   Las oraciones son demasiado largas (promedio: 63.0 palabras). Considera dividir algunas oraciones para mejorar la fluidez.
*   Varía la longitud de las oraciones para mejorar el ritmo general del texto.


================================================================================================================================================================

3.- Texto es historico con oraciones muy largas, uso excesivo de voz pasiva y vocabulario complejo, para probar una evaluación de calidad baja

User > Por favor, analiza la calidad y legibilidad del siguiente texto:

Durante el periodo comprendido entre los siglos XVI y XVIII, se llevaron a  cabo una serie de eventos que, aunque aparentemente desconectados, contribuyeron a moldear el curso de la historia de manera significativa, siendo la Revolución Industrial uno de los hitos más destacados, ya que no solo transformó las estructuras económicas y sociales, sino que también dio lugar a un cambio paradigmático en la forma en que las personas vivían y trabajaban, marcando el inicio de una era caracterizada por avances tecnológicos sin precedentes y por una creciente interconexión global.

✅ Respuesta de Gemini:
El texto proporcionado es de calidad "Mejorable" con una puntuación de 45. Se recomienda acortar las oraciones y utilizar palabras más sencillas para facilitar la lectura. La oración actual tiene un promedio de 90 palabras, por lo que se sugiere dividirla para mejorar el ritmo y la comprensión.