```
✅ ADK components imported successfully.
✅ Helper functions defined.
✅ Fee lookup function created
💳 Test: {'status': 'success', 'fee_percentage': 0.02}
✅ Exchange rate function created
💱 Test: {'status': 'success', 'rate': 0.93}
✅ Currency agent created with custom function tools
🔧 Available tools:
  • get_fee_for_payment_method - Looks up company fee structure
  • get_exchange_rate - Gets current exchange rates
```

```
### Created new session: debug_session_id

User > I want to convert 500 US Dollars to Euros using my Platinum Credit Card. How much will I receive?

currency_agent > The final amount you will receive is 455.7 Euros.

Here's the breakdown:

1.  **Fee Calculation:** A fee of 2% will be charged on 500 USD.
    *   Fee percentage: 2%
    *   Fee amount: 10 USD
    *   Amount after fee: 500 USD - 10 USD = 490 USD

2.  **Currency Conversion:** The remaining 490 USD will be converted to EUR using the exchange rate of 0.93.
    *   Exchange rate: 1 USD = 0.93 EUR
    *   Converted amount: 490 USD * 0.93 = 455.7 EUR
```

Out Ejercicio 1,2
```
  ADK components imported successfully.
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

 ### Created new session: debug_session_id

User > I want to convert 500 US Dollars to Euros using my Platinum Credit Card. How much will I receive?
Warning: there are non-text parts in the response: ['function_call', 'function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
currency_agent > The final amount you will receive is 455.7 EUR.

Here's the breakdown:
1. Fee: A 2.0% fee is charged for using a platinum credit card. This amounts to 10.0 USD.
2. Amount after fee: 500 USD - 10.0 USD = 490.0 USD.
3. Conversion: 490.0 USD is converted to EUR at an exchange rate of 0.93.
4. Final amount: 490.0 USD * 0.93 = 455.7 EUR.
```


Variables entre OUTPUT 1 y 2: 

1. Notación de Moneda

Output 1: "455.7 Euros"
Output 2: "455.7 EUR"

2. Estructura de Puntos

Output 1: Dos puntos principales con sub-puntos anidados (viñetas con asteriscos)
Output 2: Cuatro puntos consecutivos sin anidación

3. Encabezados y Secciones

Output 1: Títulos en negrita como "Fee Calculation" y "Currency Conversion"
Output 2: Sin encabezados destacados, descripción directa en cada punto

4. Precisión de Números

Output 1: "2%", "10 USD"
Output 2: "2.0%", "10.0 USD" (con decimales explícitos)

5. Nivel de Detalle

Output 1: Más conciso, agrupa conceptos relacionados
Output 2: Más desglosado, cada paso es un punto separado (Fee → Amount after fee → Conversion → Final amount)

6. Descripciones

Output 1: Genérico ("A fee of 2% will be charged on 500 USD")
Output 2: Más contextual ("A 2.0% fee is charged for using a platinum credit card")

El Output 2 adopta un formato más formal y explícito, con mayor granularidad en los pasos y uso consistente de decimales, mientras que Output 1 es más resumido y utiliza formato anidado.