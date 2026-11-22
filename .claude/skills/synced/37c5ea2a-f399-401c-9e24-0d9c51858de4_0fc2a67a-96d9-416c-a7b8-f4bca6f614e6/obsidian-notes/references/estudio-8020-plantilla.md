# Plantilla: Nota de Estudio 80/20 para Obsidian

Usa esta plantilla cuando el tipo de nota sea `estudio`. Está optimizada para retención máxima en el menor tiempo posible.

---

## Estructura completa

```markdown
---
title: "{{Asignatura}} - {{Tema}} (Resumen 80/20)"
date: YYYY-MM-DD
tags:
  - estudio
  - {{asignatura-en-minúsculas}}
  - examen
  - 80/20
type: estudio
status: completo
related:
  - "[[{{Asignatura}} - Índice]]"
---

## 🔥 Resumen 80/20

> [!important] Lo más importante
> El concepto central de este tema en 2-3 líneas.

Párrafo breve con la idea principal. Qué es, para qué sirve, por qué importa.

---

## 🧠 Conceptos clave

| Concepto | Definición simple |
|---------|-----------------|
| [[Concepto A]] | Definición en menos de 15 palabras |
| [[Concepto B]] | Definición en menos de 15 palabras |
| [[Concepto C]] | Definición en menos de 15 palabras |

---

## 🎯 Lo que seguro cae en el examen

> [!warning] Puntos críticos
> - Punto 1 que suele preguntar el profesor
> - Punto 2
> - Comparación o diferencia clave

> [!tip] Truco para recordar
> Mnemotécnico o forma de no confundirse con X.

---

## 🗣️ Explicación ultra sencilla

Como si se lo explicaras a un amigo que no sabe nada del tema:
[Párrafo en lenguaje coloquial]

Analogía o ejemplo del mundo real:
[Ejemplo concreto]

---

## 📌 Mini esquema

```
CONCEPTO PRINCIPAL
├── Subtema A
│   ├── Detalle 1
│   └── Detalle 2
└── Subtema B
    ├── Detalle 3
    └── Detalle 4
```

---

## ✅ Mini test (autoevaluación)

> [!question] Pregunta 1
> ¿Qué es {{concepto}}?
> > **Respuesta:** {{respuesta breve}}

> [!question] Pregunta 2
> ¿Cuál es la diferencia entre {{A}} y {{B}}?
> > **Respuesta:** {{diferencia clave}}

> [!question] Pregunta 3
> {{Pregunta típica de examen}}
> > **Respuesta:** {{respuesta}}

> [!question] Pregunta 4
> {{Pregunta de aplicación práctica}}
> > **Respuesta:** {{respuesta}}

> [!question] Pregunta 5
> {{Pregunta trampa habitual}}
> > **Respuesta:** {{respuesta}}

---

## 🔗 Relacionado
- [[{{Asignatura}} - Índice]]
- [[{{Tema anterior}}]]
- [[{{Tema siguiente}}]]
```

---

## Reglas específicas para notas de estudio

1. **Cada concepto = su propio wikilink**. Si aparece "Memoria Caché" en una nota de procesadores, debe ser `[[Memoria Caché]]`, no texto plano. Aunque la nota no exista todavía.

2. **Las preguntas del mini test deben ser reales**. No inventes preguntas genéricas. Usa las que suelen poner los profesores, las comparaciones más confusas, y los conceptos trampa.

3. **Nunca copies definiciones textuales del libro**. Reformula siempre. El objetivo es que el estudiante entienda, no que memorice el texto exacto.

4. **El mini esquema es obligatorio** para temas con más de 3 conceptos. Ayuda a ver la estructura de golpe.

5. **Status = completo** solo cuando tiene los 5 apartados llenos. Si falta el mini test o el esquema, usar `en-progreso`.
