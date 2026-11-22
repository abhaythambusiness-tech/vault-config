# Plantilla — `Demo - Servicio - {Nombre}.md`

Manual de montaje. Se lee con n8n abierto en la otra pantalla.
Copia esta estructura tal cual, en este orden.

---

```markdown
---
title: "Demo - Servicio - {Nombre}"
date: {YYYY-MM-DD}
tags:
  - ia
  - automatizacion
  - neozeler
  - guia
type: guia
status: borrador | en-progreso | completo
related:
  - "[[NeoZeler - MOC de Servicios]]"
  - "[[Nicho - {Nicho}]]"
---

## 📋 Paso a paso para montar la demo

### Paso 1 — {Conseguir los datos}
Qué le pides al cliente exactamente y en qué formato. Sé concreto y poco exigente:
"un export del maestro de artículos, aunque sean 30.000 líneas" es mejor que
"acceso a la base de datos". Cuanto más fácil sea decir que sí, antes tienes la demo.

### Paso 2 — {La pieza central}
El corazón técnico del servicio, explicado en lenguaje llano pero preciso. Si hay un
concepto que hay que entender (búsqueda semántica, extracción estructurada, matching),
explícalo aquí en dos frases, sin jerga.

> [!important] El truco que multiplica la precisión
> El detalle no obvio que separa una demo que funciona de una que da vergüenza.
> Casi siempre es preprocesado de datos. Si ese truco puede venderse como servicio
> independiente, dilo y enlaza: "esto es, de hecho, [[Servicio - X]]: véndelo antes aparte".

### Paso 3 — {Montar el flujo}
El agente o workflow: qué herramientas tiene, con qué instrucciones. Incluye siempre
las prohibiciones explícitas del prompt (nunca inventar precios, fechas ni datos).

### Paso 4 — Reglas de seguridad
Tres o cuatro límites innegociables, en lista. **Se enseñan en la reunión antes de que
el cliente los pida** — es argumento de venta. Patrón base, adaptado al servicio:
- Nunca mezcla datos entre clientes.
- Nunca confirma nada que comprometa dinero sin validación humana.
- Ante queja o tema delicado, pasa a persona inmediatamente.

### Paso 5 — La demo
Cómo se enseña en la reunión. Regla constante: **con sus datos reales y sus casos reales**.
Pide al cliente que te dé 10 casos de verdad (los tiene en su WhatsApp o su bandeja de
entrada) y enseña el sistema resolviéndolos en directo.

### Paso 6 — La métrica que renueva el contrato
Qué contador se deja instalado desde el día uno y cómo se convierte en euros.
Formato: {cosas resueltas sin humano} × {minutos que costaba antes} = factura justificada.

## 💬 Cómo lo vendes

> [!tip] El gancho
> El párrafo literal que dices en la reunión o escribes en el primer mensaje.
> Estructura: dolor con el rol concreto → lo que pides (poco) → lo que enseñas (mucho) → plazo.

## ⚠️ Errores a evitar

Tres a cinco viñetas, cada una con el error y la corrección en la misma frase.
Prioriza los errores que ya te han costado tiempo o credibilidad. Los tres clásicos:
- Lanzarlo a clientes finales antes de rodarlo internamente.
- Dejar que el sistema afirme cosas que dependen de terceros.
- Montarlo sobre datos sucios: si los datos están mal, el sistema parece tonto.

---
## 🔗 Relacionado
- [[Servicio - {Nombre}|📄 Volver a la Ficha Comercial]]

- [[NeoZeler - MOC de Servicios]]
- [[Servicio - {relacionado}]]
- [[Nicho - {Nicho}]]
```

---

## Notas

- El número de pasos puede variar (4 a 7), pero **el penúltimo es siempre "La demo"
  y el último siempre "La métrica que renueva el contrato"**.
- Si un paso requiere más de un párrafo de detalle técnico, ese paso probablemente
  es un servicio aparte.
