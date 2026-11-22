# Técnicas de Prompting — Referencia Completa

---

## 1. Zero-shot
**Qué es:** Dar la instrucción directamente sin ejemplos.  
**Cuándo:** Tareas simples, modelos grandes, cuando el formato es obvio.  
**Ejemplo:**
```
Resume el siguiente texto en 3 puntos clave.

[TEXTO]
```

---

## 2. Few-shot
**Qué es:** Incluir 2-5 ejemplos de input→output antes de la tarea real.  
**Cuándo:** El formato o estilo de salida es crítico. El modelo tiende a desviarse sin ejemplos.  
**Ejemplo:**
```
Clasifica el sentimiento del comentario.

Comentario: "Me encantó el producto, llegó rápido."
Sentimiento: Positivo

Comentario: "Tardó mucho y venía roto."
Sentimiento: Negativo

Comentario: "Está bien, nada especial."
Sentimiento: Neutral

Comentario: "[NUEVO COMENTARIO]"
Sentimiento:
```
**Tip:** Los ejemplos deben cubrir los casos borde más importantes.

---

## 3. Chain of Thought (CoT)
**Qué es:** Pedir al modelo que razone paso a paso antes de dar la respuesta final.  
**Cuándo:** Matemáticas, lógica, análisis complejos, diagnósticos.  
**Versión simple:** Añadir al final del prompt: *"Piensa paso a paso."*  
**Versión explícita:**
```
Responde el siguiente problema. Muestra tu razonamiento paso a paso
antes de dar la respuesta final.

Problema: [...]
```
**Versión con ejemplo (CoT few-shot):**
```
P: Si tengo 3 cajas con 8 manzanas cada una y regalo 5, ¿cuántas me quedan?
R: Primero calculo el total: 3 × 8 = 24. Luego resto las regaladas: 24 − 5 = 19. Quedan 19 manzanas.

P: [NUEVO PROBLEMA]
R:
```

---

## 4. Role Prompting
**Qué es:** Asignar al modelo un rol, identidad o expertise.  
**Cuándo:** El tono, nivel técnico o perspectiva del output importan.  
**Ejemplo:**
```
Eres un abogado especialista en derecho laboral español con 20 años de experiencia.
Responde de forma clara y sin jerga innecesaria para alguien sin formación jurídica.

Pregunta: [...]
```
**Tip:** Combina rol + audiencia ("explícalo como si fuera para...") para máximo efecto.

---

## 5. Output Constraints
**Qué es:** Especificar con precisión el formato, longitud y estructura de la respuesta.  
**Cuándo:** Siempre que el output vaya a ser procesado (JSON), mostrado en UI, o deba tener una forma concreta.  
**Ejemplo:**
```
Extrae la información del siguiente texto y devuélvela ÚNICAMENTE en este formato JSON:
{
  "nombre": "",
  "email": "",
  "empresa": "",
  "cargo": ""
}
No incluyas explicaciones ni texto adicional.

Texto: [...]
```

---

## 6. Self-Consistency
**Qué es:** Pedir múltiples respuestas independientes y quedarse con la más frecuente o razonada.  
**Cuándo:** Decisiones críticas, respuestas donde la fiabilidad importa más que la velocidad.  
**Implementación en prompt:**
```
Resuelve este problema de 3 formas diferentes y de forma independiente.
Luego indica cuál es la respuesta más consistente entre las tres y por qué.

Problema: [...]
```

---

## 7. Step-back Prompting
**Qué es:** Antes de responder la pregunta concreta, pedir al modelo que identifique el principio o concepto general detrás.  
**Cuándo:** Preguntas abstractas, problemas complejos donde el modelo tiende a ir directo sin pensar.  
**Ejemplo:**
```
Antes de responder, identifica qué principio general o concepto subyace a esta pregunta.
Luego aplícalo para responder.

Pregunta: [...]
```

---

## 8. ReAct (Reason + Act)
**Qué es:** El modelo alterna entre razonar (Thought), decidir una acción (Action) y observar resultados (Observation).  
**Cuándo:** Agentes con herramientas (tool use), tareas de múltiples pasos con feedback externo.  
**Estructura:**
```
Thought: [qué necesito saber o hacer]
Action: [herramienta o paso a ejecutar]
Observation: [resultado de la acción]
Thought: [siguiente razonamiento]
...
Final Answer: [respuesta final]
```
**Tip:** Muy usado en agentes LangChain, agentes de Claude con tools, y flujos de automatización.

---

## 9. Meta-prompting
**Qué es:** Pedirle al modelo que genere o mejore un prompt.  
**Cuándo:** No sabes bien cómo formular lo que quieres, o quieres explorar variantes.  
**Ejemplo:**
```
Escribe un prompt detallado que le pida a un LLM que [descripción de la tarea].
El prompt debe incluir rol, instrucciones claras, formato de salida y al menos un ejemplo.
```

---

## 10. Delimiters y estructura
**Qué es:** Usar separadores visuales (```, ###, XML tags, ---) para separar instrucciones de datos.  
**Cuándo:** Siempre que el prompt mezcle instrucciones con datos variables.  
**Ejemplo:**
```
Resume el siguiente artículo en 3 puntos. Sé objetivo y conciso.

### ARTÍCULO ###
[contenido del artículo aquí]
### FIN ###
```
**Tip:** Los delimiters evitan que el modelo confunda los datos con las instrucciones.

---

## Combinaciones recomendadas

| Caso de uso | Técnicas combinadas |
|---|---|
| Análisis de documentos largo | Role + CoT + Output constraints |
| Extracción de datos estructurados | Output constraints + Few-shot + Delimiters |
| Agente con herramientas | ReAct + Role + System prompt completo |
| Clasificación / tagging | Few-shot + Output constraints |
| Razonamiento complejo | CoT + Self-consistency |
| Generación creativa con estilo | Role + Few-shot |
