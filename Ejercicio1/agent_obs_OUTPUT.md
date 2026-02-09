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
Resultado diferente: Output 1 vs Output 3-4 en estructura y formato
Justificación técnica:
Los modelos transformers generativos como Gemini utilizan:

Sampling estocástico: Seleccionan tokens probabilísticamente en cada pass
Diferentes random seeds por sesión: Incluso con temperatura constante
Token usage variable: Output 1 (0 tokens mencionados) vs Output 3-4 (Input: 803, Output: 109)

Esto explica por qué 490 × 0.93 se presenta como:

Output 1: "455.7 Euros" (formato simplificado)
Output 3-4: "€455.70" (formato con símbolo y precisión)

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
Output 3-4: Formato lineal (1, 2, 3)
Output 3-4: Usa símbolo € vs texto "Euros"

Justificación del cambio:

El modelo tiene temperatura variable implícita entre sesiones
El token 109 en Output 3-4 es notablemente mayor que Output 1, indicando más "creatividad"
El símbolo € vs "Euros" sugiere diferentes prompt templates aplicados internamente por Gemini

4. Implicaciones Prácticas
Problemas reales que demuestra el Exercise:

Sin LoggingPlugin (Output 1-2):

"Warning: there are non-text parts in the response" → No sabes qué pasó
Solo ves resultado final, no los pasos intermedios
Los 2 reintentos son invisibles

 Con LoggingPlugin (Output 3-4):

Ves que hubo 2 ciclos: evento "function_call" → evento "function_response"
Sabes exactamente cuántos tokens se gastaron (optimización de costos)
Puedes medir latencia: tiempo entre "🧠 LLM REQUEST" y "🧠 LLM RESPONSE"



Apartado 5,6
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
📈 CountInvocationPlugin enabled for call tracking

 ### Created new session: debug_session_id

User > I want to convert 500 US Dollars to Euros using my Platinum Credit Card. How much will I receive?
[logging_plugin] 🚀 USER MESSAGE RECEIVED
[logging_plugin]    Invocation ID: e-a07dd59d-8ffe-4838-b006-4f9fd4add9b0
[logging_plugin]    Session ID: debug_session_id
[logging_plugin]    User ID: debug_user_id
[logging_plugin]    App Name: InMemoryRunner
[logging_plugin]    Root Agent: currency_agent
[logging_plugin]    User Content: text: 'I want to convert 500 US Dollars to Euros using my Platinum Credit Card. How much will I receive?'
[logging_plugin] 🏃 INVOCATION STARTING
[logging_plugin]    Invocation ID: e-a07dd59d-8ffe-4838-b006-4f9fd4add9b0
[logging_plugin]    Starting Agent: currency_agent
[logging_plugin] 🤖 AGENT STARTING
[logging_plugin]    Agent Name: currency_agent
[logging_plugin]    Invocation ID: e-a07dd59d-8ffe-4838-b006-4f9fd4add9b0
[count_invocation] [Plugin] Agent run count: 1
[logging_plugin] 🧠 LLM REQUEST
[logging_plugin]    Model: gemini-2.5-flash-lite
[logging_plugin]    Agent: currency_agent
[logging_plugin]    System Instruction: 'You are a smart currency conversion assistant.

    For currency conversion requests:
    1. Use `get_fee_for_payment_method()` to find transaction fees
    2. Use `get_exchange_rate()` to get currenc...'
[logging_plugin]    Available Tools: ['get_fee_for_payment_method', 'get_exchange_rate']
[count_invocation] [Plugin] LLM request count: 1
Warning: there are non-text parts in the response: ['function_call', 'function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
[logging_plugin] 🧠 LLM RESPONSE
[logging_plugin]    Agent: currency_agent
[logging_plugin]    Content: function_call: get_fee_for_payment_method | function_call: get_exchange_rate
[logging_plugin]    Token Usage - Input: 593, Output: 49
[count_invocation] [Plugin] LLM response received: function_call: get_fee_for_payment_method
[logging_plugin] 📢 EVENT YIELDED
[logging_plugin]    Event ID: 9461810a-312f-4fb4-8dc9-863543329309
[logging_plugin]    Author: currency_agent
[logging_plugin]    Content: function_call: get_fee_for_payment_method | function_call: get_exchange_rate
[logging_plugin]    Final Response: False
[logging_plugin]    Function Calls: ['get_fee_for_payment_method', 'get_exchange_rate']
[logging_plugin] 🔧 TOOL STARTING
[logging_plugin]    Tool Name: get_fee_for_payment_method
[logging_plugin]    Agent: currency_agent
[logging_plugin]    Function Call ID: adk-e98305d2-4b11-49fe-a3c6-4f0f4c8886ca
[logging_plugin]    Arguments: {'method': 'platinum credit card'}
[count_invocation] [Plugin] Tool count: 1
[count_invocation] 🔧 TOOL STARTING
[count_invocation]    Tool Name: get_fee_for_payment_method
[count_invocation]    Agent: currency_agent
[count_invocation]    Function Call ID: adk-e98305d2-4b11-49fe-a3c6-4f0f4c8886ca
[count_invocation]    Arguments: {'method': 'platinum credit card'}

[logging_plugin] 🔧 TOOL COMPLETED
[logging_plugin]    Tool Name: get_fee_for_payment_method
[logging_plugin]    Agent: currency_agent
[logging_plugin]    Function Call ID: adk-e98305d2-4b11-49fe-a3c6-4f0f4c8886ca
[logging_plugin]    Result: {'status': 'success', 'fee_percentage': 0.02}
[count_invocation] 🔧 TOOL COMPLETED
[count_invocation]    Tool Name: get_fee_for_payment_method
[count_invocation]    Agent: currency_agent
[count_invocation]    Function Call ID: adk-e98305d2-4b11-49fe-a3c6-4f0f4c8886ca
[count_invocation]    Result: {'status': 'success', 'fee_percentage': 0.02}
----------

[logging_plugin] 🔧 TOOL STARTING
[logging_plugin]    Tool Name: get_exchange_rate
[logging_plugin]    Agent: currency_agent
[logging_plugin]    Function Call ID: adk-2f42e62b-1762-4f78-9949-65be385a516d
[logging_plugin]    Arguments: {'target_currency': 'EUR', 'base_currency': 'USD'}
[count_invocation] [Plugin] Tool count: 2
[count_invocation] 🔧 TOOL STARTING
[count_invocation]    Tool Name: get_exchange_rate
[count_invocation]    Agent: currency_agent
[count_invocation]    Function Call ID: adk-2f42e62b-1762-4f78-9949-65be385a516d
[count_invocation]    Arguments: {'target_currency': 'EUR', 'base_currency': 'USD'}

[logging_plugin] 🔧 TOOL COMPLETED
[logging_plugin]    Tool Name: get_exchange_rate
[logging_plugin]    Agent: currency_agent
[logging_plugin]    Function Call ID: adk-2f42e62b-1762-4f78-9949-65be385a516d
[logging_plugin]    Result: {'status': 'success', 'rate': 0.93}
[count_invocation] 🔧 TOOL COMPLETED
[count_invocation]    Tool Name: get_exchange_rate
[count_invocation]    Agent: currency_agent
[count_invocation]    Function Call ID: adk-2f42e62b-1762-4f78-9949-65be385a516d
[count_invocation]    Result: {'status': 'success', 'rate': 0.93}
----------

[logging_plugin] 📢 EVENT YIELDED
[logging_plugin]    Event ID: 44e3d051-c3d8-43d1-9eea-283bc59bda35
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
[count_invocation] [Plugin] LLM request count: 2
[logging_plugin] 🧠 LLM RESPONSE
[logging_plugin]    Agent: currency_agent
[logging_plugin]    Content: text: 'With your Platinum Credit Card, the conversion of 500 USD to EUR involves a fee and uses an exchange rate.

The transaction fee is 2.00% of 500 USD, which is 10.00 USD.
After deducting the fee, you ha...'
[logging_plugin]    Token Usage - Input: 698, Output: 119
[count_invocation] [Plugin] LLM response received: text: 'With your Platinum Credit Card, the conversion of 500 USD to EUR involves a fee and uses an exchange rate.

The transaction fee is 2.00% of 500 USD, which is 10.00 USD.
After deducting the fee, you ha...'
[logging_plugin] 📢 EVENT YIELDED
[logging_plugin]    Event ID: 36c81e79-655c-4fdd-b560-7e9842125cbc
[logging_plugin]    Author: currency_agent
[logging_plugin]    Content: text: 'With your Platinum Credit Card, the conversion of 500 USD to EUR involves a fee and uses an exchange rate.

The transaction fee is 2.00% of 500 USD, which is 10.00 USD.
After deducting the fee, you ha...'
[logging_plugin]    Final Response: True
currency_agent > With your Platinum Credit Card, the conversion of 500 USD to EUR involves a fee and uses an exchange rate.

The transaction fee is 2.00% of 500 USD, which is 10.00 USD.
After deducting the fee, you have 490.00 USD remaining.
The exchange rate from USD to EUR is 0.93.
So, the final amount you will receive is 455.70 EUR (490.00 USD * 0.93).
[logging_plugin] 🤖 AGENT COMPLETED
[logging_plugin]    Agent Name: currency_agent
[logging_plugin]    Invocation ID: e-a07dd59d-8ffe-4838-b006-4f9fd4add9b0
[logging_plugin] ✅ INVOCATION COMPLETED
[logging_plugin]    Invocation ID: e-a07dd59d-8ffe-4838-b006-4f9fd4add9b0
[logging_plugin]    Final Agent: currency_agent
```


## Cambios al Añadir CountInvocationPlugin

### 1. Incremento en Logs sin Cambio Funcional
Evidencia observable:
- Mismo prompt y configuración que Output 3-4 (solo LoggingPlugin)
- Output 5-6 añade `CountInvocationPlugin()` al array de plugins
- **Resultado**: Logs adicionales sin alteración de la respuesta final

```python
currency_runner = InMemoryRunner(
    agent=currency_agent,
    plugins=[LoggingPlugin(), CountInvocationPlugin()],  # Ambos plugins
)
```

### 2. Métricas Adicionales de Conteo
Nuevas líneas de log que aparecen:

**Contadores de Agent:**
```
[count_invocation] [Plugin] Agent run count: 1
```

**Contadores de LLM:**
```
[count_invocation] [Plugin] LLM request count: 1
[count_invocation] [Plugin] LLM request count: 2
```

**Contadores de Tools:**
```
[count_invocation] [Plugin] Tool count: 1  # get_fee_for_payment_method
[count_invocation] [Plugin] Tool count: 2  # get_exchange_rate
```

**Duplicación de Logs de Herramientas:**
- Cada `🔧 TOOL STARTING` y `🔧 TOOL COMPLETED` aparece duplicado
- LoggingPlugin registra el evento completo
- CountInvocationPlugin registra el contador + detalles (con separador `----------`)

### 3. Cambio en el Formato de Respuesta del Agente
**Output 3-4 (solo LoggingPlugin):**
```
You will receive €465.00.

Here's how that's calculated:
1. **Fee deduction:** A 2% fee is charged on the initial 500 USD, which is 10 USD.
2. **Amount after fee:** This leaves you with 490 USD to convert.
3. **Currency conversion:** Using the exchange rate of 0.93, the 490 USD is converted to €455.70.
```

**Output 5-6 (LoggingPlugin + CountInvocationPlugin):**
```
With your Platinum Credit Card, the conversion of 500 USD to EUR involves a fee and uses an exchange rate.

The transaction fee is 2.00% of 500 USD, which is 10.00 USD.
After deducting the fee, you have 490.00 USD remaining.
The exchange rate from USD to EUR is 0.93.
So, the final amount you will receive is 455.70 EUR (490.00 USD * 0.93).
```

**Diferencias:**
| Aspecto | Output 3-4 | Output 5-6 |
|---------|----------|------------|
| Estructura | Lista numerada (1, 2, 3) | Párrafos secuenciales sin numeración |
| Mención inicial | "€465.00" (incorrecto) | "455.70 EUR" (correcto al final) |
| Contexto | Más directo y esquemático | Más narrativo y contextual |
| Decimales | Mixto en el texto | Consistente "2.00%", "10.00 USD", "490.00 USD" |
| Fórmula final | No mostrada explícitamente | "490.00 USD * 0.93" explícita |

### 4. Justificación del Cambio de Formato
**Razón Principal: No-Determinismo del LLM**
- Aunque no cambie la lógica, el modelo genera diferente respuesta textual
- **Token usage idéntico en primer request**: 593 → 49 (ambos outputs)
- **Token usage diferente en segundo request**: 
  - Output 3-4: Input 698, Output 109
  - Output 5-6: Input 698, Output **119** (10 tokens más)

**Comportamiento Observado:**
- Solo hubo 1 ciclo de LLM REQUEST en Output 5-6 (vs 2 ciclos en Output 3-4)
- CountInvocationPlugin NO causa el cambio, solo cuenta eventos existentes
- La variabilidad proviene del sampling estocástico del modelo Gemini

### 5. Ventajas de CountInvocationPlugin en Producción

**Métricas Simplificadas:**
-  **Conteo inmediato**: Saber cuántas llamadas LLM sin parsear logs complejos
-  **Tracking de costos**: Tool count permite estimar latencia y uso de API
-  **Debugging rápido**: "Agent run count: 1" confirma ejecución única

**Complementariedad con LoggingPlugin:**
```
[logging_plugin] → Logs detallados (IDs, contenido, tokens)
[count_invocation] → Contadores acumulativos (métricas agregadas)
```

**Caso de Uso Real:**
En una sesión con múltiples interacciones:
- LoggingPlugin: Muestra cada evento individual
- CountInvocationPlugin: Resume totales (ej: "50 LLM requests en esta sesión")

---

## Conclusiones Generales

### 1. **No-Determinismo del Modelo LLM**
Evidencia observable:
- Mismo prompt ("I want to convert 500 US Dollars to Euros...")
- Mismos parámetros (temperature implícito, modelo gemini-2.5-flash-lite, tools idénticas)
- **Resultado diferente**: Output 1 vs Output 3-4 vs Output 5-6 en estructura y formato

Justificación técnica:
Los modelos transformers generativos como Gemini utilizan:
- **Sampling estocástico**: Seleccionan tokens probabilísticamente en cada pass
- **Diferentes random seeds por sesión**: Incluso con temperatura constante
- **Token usage variable**: Output 3-4 (109 tokens) vs Output 5-6 (119 tokens)

Esto explica por qué 490 × 0.93 se presenta como:
- Output 1: "455.7 Euros" (formato simplificado)
- Output 3-4: "€465.00" inicial → "€455.70" final (inconsistencia)
- Output 5-6: "455.70 EUR" con fórmula explícita (más claro)

### 2. **Los Plugins son Observables, No Invasivos**
Evidencia en el código:
```python
currency_runner = InMemoryRunner(
    agent=currency_agent,
    plugins=[LoggingPlugin(), CountInvocationPlugin()],
)
```

Justificación:
- Los plugins implementan callbacks de eventos (on_message, on_tool_call, etc.) **sin interceptar lógica**
- Los logs muestran **exactamente qué ocurre** sin modificarlo:
  - Input tokens: 593 → 698 (aumentan porque el contexto se amplía con respuestas)
  - Cada tool call ejecuta y devuelve su resultado sin alteración
  - CountInvocationPlugin solo incrementa contadores sin afectar flujo

Razón de uso en producción:
- **LoggingPlugin**: Debugging detallado (ver cada paso del agente)
- **CountInvocationPlugin**: Métricas agregadas (costos, performance, auditoría)

### 3. **Variabilidad en Formato de Respuesta**
Comparando los tres outputs principales:

| Aspecto | Output 1 | Output 3-4 | Output 5-6 |
|---------|----------|----------|------------|
| Montante final | "455.7 Euros" | "€465.00" → "€455.70" | "455.70 EUR" |
| Estructura | 2 puntos anidados | 3 puntos numerados | Párrafos narrativos |
| Precisión | Sin decimales | Decimales mixtos | Decimales consistentes |
| Contexto | Genérico | Menciona "platinum credit card" | Más descriptivo |
| LLM Requests | No visible | 3 requests (2 reintentos) | 2 requests (1 reintento) |

Justificación del cambio:
- El modelo tiene **temperatura variable implícita** entre sesiones
- Diferentes token outputs (49 → 109 → 119) indican mayor "creatividad"
- El número de reintentos también varía (modelo decide cuándo responder)

### 4. **Implicaciones Prácticas**

Problemas reales que demuestran los ejercicios:

 **Sin Plugins** (Output 1-2):
- "Warning: there are non-text parts in the response" → No sabes qué pasó
- Solo ves resultado final, no los pasos intermedios
- Los reintentos del modelo son invisibles
- No hay métricas de costos o performance

 **Con LoggingPlugin** (Output 3-4):
- Ves los 3 ciclos: evento "function_call" → "function_response" → "text"
- Sabes exactamente cuántos tokens se gastaron (optimización de costos)
- Puedes medir latencia: tiempo entre "🧠 LLM REQUEST" y "🧠 LLM RESPONSE"
- Detectas inconsistencias (€465.00 vs €455.70)

 **Con LoggingPlugin + CountInvocationPlugin** (Output 5-6):
- Todo lo anterior +
- Contadores simples: "Agent run count: 1", "LLM request count: 2"
- Tracking de tools: "Tool count: 1" → "Tool count: 2"
- Métricas agregadas para dashboards de monitoreo

**Por qué es crítico en producción:**
- **Costos**: Sin logging, no sabías que se hacían múltiples requests al modelo (n× costo)
- **Confiabilidad**: Necesitas validar que "€455.70" es correcto (490 × 0.93 = 455.7 ✓)
- **SLAs**: Detectar qué sesiones son lentas (múltiples reintentos no son ideales)
- **Debugging**: CountInvocationPlugin permite alertas si "LLM request count" > threshold
- **Auditoría**: Los logs completos permiten reproducir problemas en desarrollo

