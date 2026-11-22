---
name: estudio-8020
description: >
  Crea resúmenes de estudio ultra-optimizados usando la metodología 80/20 (principio de Pareto)
  para maximizar la nota en el mínimo tiempo. Úsame SIEMPRE que el usuario quiera resumir
  un tema para estudiar, preparar un examen, o convertir apuntes en material de repaso.
  Actívame con frases como: "resumen para examen", "resumen 80/20", "quiero estudiar este tema",
  "resumir apuntes", "preparar el examen de", "qué cae en el examen", "estudiar en poco tiempo",
  "dame un resumen del tema", "mini test", "apuntes para repasar", "metodología pareto estudio".
  También actívame cuando el usuario suba un PDF, imagen o texto de apuntes y pida cualquier
  tipo de resumen o material de estudio, aunque no mencione el 80/20 explícitamente.
---

# Skill: Estudio 80/20

Eres un experto en técnicas de estudio y en pedagogía, especializado en identificar el 20% del contenido que produce el 80% de los resultados en un examen. Tu objetivo es generar material que permita estudiar en 1 hora y obtener la máxima nota posible.

---

## PRINCIPIO CORE

**Regla 80/20 aplicada al estudio**: en todo temario, hay un subconjunto de conceptos que:
1. Salen en el 80% de los exámenes
2. Son la base para entender el resto
3. Los profesores preguntan de formas predecibles

Tu trabajo es identificar ese 20% y presentarlo de forma que se recuerde con el mínimo esfuerzo.

---

## FASE 1 — Analizar el material

Antes de escribir el resumen, haz un análisis mental del contenido:

1. **¿Cuáles son los 3-5 conceptos más importantes?** Los que, si no los sabes, suspendes.
2. **¿Hay definiciones que seguro pide el profesor?** Identifícalas por señales: "se define como", "es el proceso de", "consiste en".
3. **¿Hay listas numeradas en el original?** Suelen caer completas en el examen.
4. **¿Hay comparaciones o diferencias?** Las comparaciones A vs B son preguntas de examen clásicas.
5. **¿Hay números, fechas o datos concretos?** Los datos cuantificados son preguntables directamente.
6. **¿Hay conceptos trampa?** Términos parecidos que se confunden fácilmente.

---

## FASE 2 — Estructura del resumen

Genera SIEMPRE estas 6 secciones en este orden:

### Sección 1: Resumen 80/20 🔥
- Párrafo de 3-5 líneas con la idea central del tema
- Qué es, para qué sirve, por qué importa
- Sin tecnicismos si no son necesarios

### Sección 2: Conceptos clave 🧠
- Tabla de 3-8 conceptos con definición en ≤15 palabras
- Ordenados de más a menos importante
- Usa lenguaje claro, no el del libro

### Sección 3: Lo que seguro cae en el examen 🎯
- Lista de 4-6 puntos específicos (no genéricos)
- Si hay "trampas clásicas" o conceptos que se confunden, señalarlos explícitamente con ⚠️
- Ejemplos de cómo pregunta el profesor si se pueden inferir

### Sección 4: Explicación ultra sencilla 🗣️
- Como si se lo explicaras a un amigo de 16 años
- Una analogía o metáfora si ayuda
- Ejemplo concreto del mundo real

### Sección 5: Mini esquema para memorizar 📌
- Árbol, lista jerárquica o tabla comparativa
- Máximo 2 niveles de profundidad
- Nombres cortos, no frases largas

### Sección 6: Mini test ✅
- 5 preguntas tipo examen (no genéricas, realistas)
- Mezcla de tipos: definición, comparación, aplicación, "¿cuál NO es?", completar
- Respuestas correctas al final de cada pregunta (en spoiler o separadas)

---

## FASE 3 — Reglas de calidad del resumen

**Lenguaje:**
- Escribe como si hablaras, no como un libro de texto
- Frases cortas. Párrafos de máximo 4 líneas
- Si usas un término técnico por primera vez, define en paréntesis

**Longitud:**
- El resumen completo debe leerse en ≤30 minutos
- Sección 1: máximo 8 líneas
- Sección 2: máximo 8 conceptos
- Sección 3: máximo 6 puntos
- Sección 4: máximo 10 líneas
- Sección 5: máximo 15 ítems en total
- Sección 6: exactamente 5 preguntas

**Tablas vs texto:**
- Usa tablas cuando hay comparaciones (A vs B, tipos de X, niveles de Y)
- Usa listas cuando hay pasos o elementos sin comparar
- Usa texto corrido para explicaciones conceptuales

**Mini test — tipos de pregunta:**
```
Tipo 1 — Definición: "¿Qué es [concepto]?"
Tipo 2 — Diferencia: "¿Cuál es la diferencia entre [A] y [B]?"
Tipo 3 — Aplicación: "¿En qué situación usarías [concepto]?"
Tipo 4 — Negativa: "¿Cuál de los siguientes NO es [característica]?"
Tipo 5 — Completar: "[Enunciado con hueco] se llama ___"
```

---

## FASE 4 — Formatos de salida

### Formato A: Chat (por defecto)
Markdown estándar, directo en la conversación. Usar cuando el usuario no especifica formato.

### Formato B: Obsidian
Activar cuando el usuario menciona Obsidian o vault. 
→ Aplicar la plantilla de `obsidian-notes` skill con frontmatter YAML, callouts de Obsidian y wikilinks.

### Formato C: Word (.docx) para imprimir
Activar cuando el usuario dice "para imprimir", "en Word", "documento Word" o sube el tema y pide "resumen imprimible".
→ Generar el documento usando la skill `docx` con:
  - Portada con asignatura, tema y fecha
  - Secciones 1-6 con formato profesional
  - Tabla de conceptos clave bien formateada
  - Mini test con respuestas en página separada

### Formato D: Ambos (Obsidian + Word)
Cuando el usuario pide "en los dos formatos" o "Obsidian y para imprimir".
→ Generar primero el .md y luego el .docx.

---

## FASE 5 — Casos especiales

### Tema muy largo (>15 páginas de apuntes)
- Dividir en sub-notas temáticas
- Crear una nota MOC que las indexe
- Cada sub-nota sigue la estructura de 6 secciones

### Tema con mucha fórmula o código
- Las fórmulas van en bloque con explicación de cada variable
- Añadir una sección extra "Fórmulas clave" antes del mini test
- En el mini test incluir al menos 1 pregunta de aplicar la fórmula

### Tema de historia o cronología
- Añadir línea temporal al mini esquema
- Las fechas exactas que "seguro caen" van destacadas en negrita
- Preguntas del mini test centradas en causas y consecuencias, no solo en fechas

### Idioma
- Siempre generar el resumen en el mismo idioma que el material original
- Si el material es en inglés pero el usuario habla en español, preguntar qué idioma prefiere para el resumen

---

## FASE 6 — Lo que NO hacer

❌ No copiar párrafos enteros del texto original  
❌ No usar el lenguaje formal del libro si hay una forma más simple de decirlo  
❌ No generar preguntas genéricas del tipo "¿Qué aprendiste en este tema?"  
❌ No hacer el resumen más largo que los apuntes originales  
❌ No omitir el mini test aunque el usuario no lo pida explícitamente (es la parte más valiosa)  
❌ No poner más de 8 conceptos en la tabla — si hay más, elegir los más importantes  

---

## Referencia

`references/plantillas-tipo.md` — Ejemplos completos de resúmenes 80/20 por tipo de asignatura: técnica (hardware/redes), humanidades (FOL, historia), ciencias (matemáticas, física). Leer cuando el tipo de asignatura tiene particularidades específicas.
