Out Ejercicio 3,4


```
✅ ADK components imported successfully.
✅ Gemini API key setup complete.
✅ Helper functions defined.
✅ Fee lookup function created
💳 Test: {'status': 'success', 'fee_percentage': 0.02}
✅ Exchange rate function created
💱 Test: {'status': 'success', 'rate': 0.93}
✅ Currency agent created with custom function tools
🔧 Available tools:
  • get_fee_for_payment_method - Looks up company fee structure
  • get_exchange_rate - Gets current exchange rates
📊 LoggingPlugin enabled for observability

 ### Created new session: debug_session_id

User > I want to convert 500 US Dollars to Euros using my Platinum Credit Card. How much will I receive?
[logging_plugin] 🚀 USER MESSAGE RECEIVED
[logging_plugin]    Invocation ID: e-af42949a-f87d-4f03-a703-6e1062190ef1
[logging_plugin]    Session ID: debug_session_id
[logging_plugin]    User ID: debug_user_id
[logging_plugin]    App Name: InMemoryRunner
[logging_plugin]    Root Agent: currency_agent
[logging_plugin]    User Content: text: 'I want to convert 500 US Dollars to Euros using my Platinum Credit Card. How much will I receive?'
[logging_plugin] 🏃 INVOCATION STARTING
[logging_plugin]    Invocation ID: e-af42949a-f87d-4f03-a703-6e1062190ef1
[logging_plugin]    Starting Agent: currency_agent
[logging_plugin] 🤖 AGENT STARTING
[logging_plugin]    Agent Name: currency_agent
[logging_plugin]    Invocation ID: e-af42949a-f87d-4f03-a703-6e1062190ef1
[logging_plugin] 🧠 LLM REQUEST
[logging_plugin]    Model: gemini-2.5-flash-lite
[logging_plugin]    Agent: currency_agent
[logging_plugin]    System Instruction: 'You are a smart currency conversion assistant.

    For currency conversion requests:
    1. Use `get_fee_for_payment_method()` to find transaction fees
    2. Use `get_exchange_rate()` to get currenc...'
[logging_plugin]    Available Tools: ['get_fee_for_payment_method', 'get_exchange_rate']
Warning: there are non-text parts in the response: ['function_call', 'function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
[logging_plugin] 🧠 LLM RESPONSE
[logging_plugin]    Agent: currency_agent
[logging_plugin]    Content: function_call: get_fee_for_payment_method | function_call: get_exchange_rate
[logging_plugin]    Token Usage - Input: 593, Output: 49
[logging_plugin] 📢 EVENT YIELDED
[logging_plugin]    Event ID: a9fe1353-f1db-4660-957e-b6c60aa1c1fd
[logging_plugin]    Author: currency_agent
[logging_plugin]    Content: function_call: get_fee_for_payment_method | function_call: get_exchange_rate
[logging_plugin]    Final Response: False
[logging_plugin]    Function Calls: ['get_fee_for_payment_method', 'get_exchange_rate']
[logging_plugin] 🔧 TOOL STARTING
[logging_plugin]    Tool Name: get_fee_for_payment_method
[logging_plugin]    Agent: currency_agent
[logging_plugin]    Function Call ID: adk-02dead75-8760-4973-b555-cbee900b6783
[logging_plugin]    Arguments: {'method': 'platinum credit card'}
[logging_plugin] 🔧 TOOL COMPLETED
[logging_plugin]    Tool Name: get_fee_for_payment_method
[logging_plugin]    Agent: currency_agent
[logging_plugin]    Function Call ID: adk-02dead75-8760-4973-b555-cbee900b6783
[logging_plugin]    Result: {'status': 'success', 'fee_percentage': 0.02}
[logging_plugin] 🔧 TOOL STARTING
[logging_plugin]    Tool Name: get_exchange_rate
[logging_plugin]    Agent: currency_agent
[logging_plugin]    Function Call ID: adk-7b240bb7-9080-48eb-99f4-578a316d4ecb
[logging_plugin]    Arguments: {'base_currency': 'USD', 'target_currency': 'EUR'}
[logging_plugin] 🔧 TOOL COMPLETED
[logging_plugin]    Tool Name: get_exchange_rate
[logging_plugin]    Agent: currency_agent
[logging_plugin]    Function Call ID: adk-7b240bb7-9080-48eb-99f4-578a316d4ecb
[logging_plugin]    Result: {'status': 'success', 'rate': 0.93}
[logging_plugin] 📢 EVENT YIELDED
[logging_plugin]    Event ID: d55e9a92-fcf9-46bf-bd80-9d4193610b1c
[logging_plugin]    Author: currency_agent
[logging_plugin]    Content: function_response: get_fee_for_payment_method | function_response: get_exchange_rate
[logging_plugin]    Final Response: False
[logging_plugin]    Function Responses: ['get_fee_for_payment_method', 'get_exchange_rate']
[logging_plugin] 🧠 LLM REQUEST
[logging_plugin]    Model: gemini-2.5-flash-lite
[logging_plugin]    Agent: currency_agent
[logging_plugin]    System Instruction: 'You are a smart currency conversion assistant.

    For currency conversion requests:
    1. Use `get_fee_for_payment_method()` to find transaction fees
    2. Use `get_exchange_rate()` to get currenc...'
[logging_plugin]    Available Tools: ['get_fee_for_payment_method', 'get_exchange_rate']
[logging_plugin] 🧠 LLM RESPONSE
[logging_plugin]    Agent: currency_agent
[logging_plugin]    Content: function_call: get_fee_for_payment_method | function_call: get_exchange_rate
[logging_plugin]    Token Usage - Input: 698, Output: 49
[logging_plugin] 📢 EVENT YIELDED
[logging_plugin]    Event ID: 6f1455dd-0f50-4b53-8e72-93bbcc3ff3e7
[logging_plugin]    Author: currency_agent
[logging_plugin]    Content: function_call: get_fee_for_payment_method | function_call: get_exchange_rate
[logging_plugin]    Final Response: False
[logging_plugin]    Function Calls: ['get_fee_for_payment_method', 'get_exchange_rate']
[logging_plugin] 🔧 TOOL STARTING
[logging_plugin]    Tool Name: get_fee_for_payment_method
[logging_plugin]    Agent: currency_agent
[logging_plugin]    Function Call ID: adk-f677cc80-3a3f-4aa4-8a2e-609fdddfbc05
[logging_plugin]    Arguments: {'method': 'platinum credit card'}
[logging_plugin] 🔧 TOOL COMPLETED
[logging_plugin]    Tool Name: get_fee_for_payment_method
[logging_plugin]    Agent: currency_agent
[logging_plugin]    Function Call ID: adk-f677cc80-3a3f-4aa4-8a2e-609fdddfbc05
[logging_plugin]    Result: {'status': 'success', 'fee_percentage': 0.02}
[logging_plugin] 🔧 TOOL STARTING
[logging_plugin]    Tool Name: get_exchange_rate
[logging_plugin]    Agent: currency_agent
[logging_plugin]    Function Call ID: adk-7f311ad3-3177-4d6a-a447-47d1a5337f7e
[logging_plugin]    Arguments: {'base_currency': 'USD', 'target_currency': 'EUR'}
[logging_plugin] 🔧 TOOL COMPLETED
[logging_plugin]    Tool Name: get_exchange_rate
[logging_plugin]    Agent: currency_agent
[logging_plugin]    Function Call ID: adk-7f311ad3-3177-4d6a-a447-47d1a5337f7e
[logging_plugin]    Result: {'status': 'success', 'rate': 0.93}
[logging_plugin] 📢 EVENT YIELDED
[logging_plugin]    Event ID: 823566f1-54e9-43de-8f50-25d2580a6758
[logging_plugin]    Author: currency_agent
[logging_plugin]    Content: function_response: get_fee_for_payment_method | function_response: get_exchange_rate
[logging_plugin]    Final Response: False
[logging_plugin]    Function Responses: ['get_fee_for_payment_method', 'get_exchange_rate']
[logging_plugin] 🧠 LLM REQUEST
[logging_plugin]    Model: gemini-2.5-flash-lite
[logging_plugin]    Agent: currency_agent
[logging_plugin]    System Instruction: 'You are a smart currency conversion assistant.

    For currency conversion requests:
    1. Use `get_fee_for_payment_method()` to find transaction fees
    2. Use `get_exchange_rate()` to get currenc...'
[logging_plugin]    Available Tools: ['get_fee_for_payment_method', 'get_exchange_rate']
[logging_plugin] 🧠 LLM RESPONSE
[logging_plugin]    Agent: currency_agent
[logging_plugin]    Content: text: 'You will receive €465.00.

Here's how that's calculated:
1.  **Fee deduction:** A 2% fee is charged on the initial 500 USD, which is 10 USD.
2.  **Amount after fee:** This leaves you with 490 USD to c...'
[logging_plugin]    Token Usage - Input: 803, Output: 109
[logging_plugin] 📢 EVENT YIELDED
[logging_plugin]    Event ID: 735e2870-da3a-40dc-b9dc-6defdf861d5a
[logging_plugin]    Author: currency_agent
[logging_plugin]    Content: text: 'You will receive €465.00.

Here's how that's calculated:
1.  **Fee deduction:** A 2% fee is charged on the initial 500 USD, which is 10 USD.
2.  **Amount after fee:** This leaves you with 490 USD to c...'
[logging_plugin]    Final Response: True
currency_agent > You will receive €465.00.

Here's how that's calculated:
1.  **Fee deduction:** A 2% fee is charged on the initial 500 USD, which is 10 USD.
2.  **Amount after fee:** This leaves you with 490 USD to convert.
3.  **Currency conversion:** Using the exchange rate of 0.93, the 490 USD is converted to €455.70.
[logging_plugin] 🤖 AGENT COMPLETED
[logging_plugin]    Agent Name: currency_agent
[logging_plugin]    Invocation ID: e-af42949a-f87d-4f03-a703-6e1062190ef1
[logging_plugin] ✅ INVOCATION COMPLETED
[logging_plugin]    Invocation ID: e-af42949a-f87d-4f03-a703-6e1062190ef1
[logging_plugin]    Final Agent: currency_agent
```


Cambios del modelo:

1. No-Determinismo del Modelo LLM
Evidencia observable:

Mismo prompt ("I want to convert 500 US Dollars to Euros...")
Mismos parámetros (temperature implícito, modelo gemini-2.5-flash-lite, tools idénticas)
Resultado diferente: Output 1 vs Output 3 en estructura y formato
Justificación técnica:
Los modelos transformers generativos como Gemini utilizan:

Sampling estocástico: Seleccionan tokens probabilísticamente en cada pass
Diferentes random seeds por sesión: Incluso con temperatura constante
Token usage variable: Output 1 (0 tokens mencionados) vs Output 3 (Input: 803, Output: 109)

Esto explica por qué 490 × 0.93 se presenta como:

Output 1: "455.7 Euros" (formato simplificado)
Output 3: "€455.70" (formato con símbolo y precisión)

2. El LoggingPlugin registra pero no afecta lógica

Evidencia en el código:
currency_runner = InMemoryRunner(
    agent=currency_agent,
    plugins=[LoggingPlugin()],  # Solo se añade el plugin
)

Justificación:

El plugin implementa callbacks de eventos (on_message, on_tool_call, etc.) sin interceptar lógica
Los logs muestran exactamente qué ocurre sin modificarlo:
Input tokens: 593 → 698 → 803 (aumentan porque el contexto se amplía con respuestas)
Cada tool call ejecuta y devuelve su resultado sin alteración
Se capturan 2 ciclos completos de LLM_REQUEST (reintentos internos del modelo)
Razón de uso en producción:
Sin debugging, no sabrías que el modelo hizo 2 intentos antes de responder correctamente.

3. Cambios en el formato de respuesta
Comparando los outputs, el modelo genera diferentes estructuras:

Output 1: Formato anidado con subsecciones
Output 3: Formato lineal (1, 2, 3)
Output 3: Usa símbolo € vs texto "Euros"

Justificación del cambio:

El modelo tiene temperatura variable implícita entre sesiones
El token 109 en Output 3 es notablemente mayor que Output 1, indicando más "creatividad"
El símbolo € vs "Euros" sugiere diferentes prompt templates aplicados internamente por Gemini

4. Implicaciones Prácticas
Problemas reales que demuestra el Exercise:

Sin LoggingPlugin (Output 1-2):

"Warning: there are non-text parts in the response" → No sabes qué pasó
Solo ves resultado final, no los pasos intermedios
Los 2 reintentos son invisibles

 Con LoggingPlugin (Output 3):

Ves que hubo 2 ciclos: evento "function_call" → evento "function_response"
Sabes exactamente cuántos tokens se gastaron (optimización de costos)
Puedes medir latencia: tiempo entre "🧠 LLM REQUEST" y "🧠 LLM RESPONSE"

