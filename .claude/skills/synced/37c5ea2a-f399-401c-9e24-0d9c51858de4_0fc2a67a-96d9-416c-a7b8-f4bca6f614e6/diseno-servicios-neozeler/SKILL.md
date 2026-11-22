---
name: diseno-servicios-neozeler
description: >
  Diseña servicios de IA vendibles para NeoZeler y los documenta como par de notas Obsidian:
  ficha comercial + guía de montaje de la demo. Úsame SIEMPRE que el usuario quiera crear,
  definir, empaquetar o documentar un servicio, oferta o producto de su agencia de IA.
  Actívame con frases como: "crea un servicio de", "nuevo servicio para el nicho de",
  "quiero vender X a los distribuidores", "ficha de servicio", "cómo empaqueto esto como oferta",
  "qué le vendo a este nicho", "diseña la oferta", "convierte esta idea en servicio",
  "monta el catálogo de servicios", "cuánto cobro por esto", "ficha comercial + demo".
  También actívame cuando el usuario describa un dolor operativo de un nicho y quiera
  convertirlo en algo vendible, o cuando pida "un servicio más" para completar su portafolio,
  aunque no diga la palabra "servicio".
---

# Diseño de servicios NeoZeler

NeoZeler es una agencia unipersonal española de automatización con IA que vende a pymes con operativa compleja y administración artesanal. Esta skill convierte **un dolor operativo concreto de un nicho** en **un servicio vendible y montable**, documentado siempre como **dos notas Obsidian enlazadas entre sí**.

## Regla número uno

Un servicio no es una tecnología. Es **un dolor concreto de un nicho concreto, con un número delante y una demo que se puede enseñar en una reunión**.

Si no puedes rellenar esta frase, el servicio no está listo:

> "En [nicho], [persona] dedica [X horas/mes] a [tarea]. Esto lo hace solo, y eso son [€/año] recuperables."

## Flujo de trabajo

### Paso 0 — Recoger contexto del vault

Antes de escribir nada, busca y lee si están disponibles:
- La nota de nicho correspondiente (`Nicho - ...`) → de ahí salen los dolores, la jerga y las preguntas de cualificación. **No inventes dolores si la nota ya los tiene documentados.**
- `[[NeoZeler - MOC de Servicios]]` → para no duplicar un servicio existente y para asignar prioridad coherente.
- Fichas de servicio ya escritas → para mantener el mismo tono y el mismo nivel de detalle.

Si el nicho no tiene nota todavía, dilo y ofrece crearla primero: sin nota de nicho, la ficha de servicio se llena de tópicos.

### Paso 1 — Elegir y acotar el dolor

Un servicio = **un dolor**. Si la idea del usuario cubre tres dolores, divídela en tres servicios enlazados (así se venden en escalera: el primero abre la puerta y el segundo se vende solo). Ejemplo real del vault: el enriquecimiento de descripciones es un paso interno del Comercial Interno IA, pero se vende antes y aparte como `[[Servicio - Normalizador de Catálogo]]`.

Criterios para que un dolor merezca ser servicio:

| Criterio | Pregunta de control |
|----------|--------------------|
| Frecuencia | ¿Pasa todos los días o todas las semanas? |
| Medible | ¿El cliente puede darte un número de horas o documentos al mes? |
| Demostrable | ¿Se puede enseñar funcionando en 10 minutos con sus datos reales? |
| Sin IT interno | ¿Es algo que no van a "hacer en casa"? |
| Repetible | ¿Sirve para el siguiente cliente del mismo nicho cambiando solo los datos? |

Si falla "Demostrable" o "Repetible", es una consultoría a medida, no un servicio del catálogo. Dilo abiertamente.

### Paso 2 — Decidir el stack

Regla dura del portafolio: **la demo se monta con coste de infraestructura cero**. n8n autoalojado, PostgreSQL/pgvector o Qdrant autoalojado, WhatsApp Cloud API en tramo gratuito, Telegram o email para escalado a humano, y API de LLM que cuesta céntimos por conversación.

> [!warning] Nada de telefonía de pago en el portafolio
> Los agentes de voz (Twilio, Vapi, Retell) exigen coste obligatorio y **están fuera del catálogo de demos**. Si un cliente quiere voz, se cotiza aparte con los costes trasladados a él. La versión por chat da el 80% del valor con 0 €. Aplica el mismo criterio a cualquier pieza nueva que solo funcione con SaaS de pago: busca la alternativa autoalojada o marca esa pieza como "coste del cliente".

Ver `references/stack-neozeler.md` para las piezas ya validadas y sus alternativas.

### Paso 3 — Poner precio y prioridad

Ver `references/precios-y-prioridad.md`. Resumen: montaje entre 1.500 y 8.000 € según dificultad, más mantenimiento mensual del 5-10% del montaje. **Siempre hay cuota mensual**: sin recurrencia esto es una agencia de proyectos, no un negocio.

### Paso 4 — Escribir las dos notas

Siempre dos archivos, nunca uno solo:

1. **`Servicio - {Nombre}.md`** — la ficha comercial. Para leer antes de una reunión. Responde *qué es, a quién, qué problema resuelve y cuánto cuesta*.
2. **`Demo - Servicio - {Nombre}.md`** — el manual de montaje. Para leer con n8n abierto. Responde *cómo se construye, cómo se enseña y qué no hay que hacer*.

Las plantillas exactas, con todas las secciones y su orden, están en:
- `references/plantilla-ficha.md`
- `references/plantilla-demo.md`

Léelas antes de escribir. No improvises la estructura: el valor del vault está en que todas las fichas se lean igual.

### Paso 5 — Cerrar los enlaces

Cada nota nueva debe quedar conectada en las dos direcciones:
- La ficha enlaza a la demo y la demo enlaza a la ficha (con alias: `[[Demo - Servicio - X|🔗 Ver montaje de la Demo]]`).
- Ambas enlazan al `[[NeoZeler - MOC de Servicios]]` y a la nota de nicho.
- Si el servicio se apoya en otro o lo alimenta, enlázalos entre sí.
- Al terminar, recuerda al usuario que añada la línea correspondiente al MOC de Servicios (y ofrécete a escribirla).

## Reglas de escritura

Estas notas las lee el usuario en frío antes de una reunión. El tono importa tanto como el contenido.

- **En cristiano.** Nada de "optimización de procesos mediante inteligencia artificial". Se escribe "alguien teclea ochenta albaranes al día a mano".
- **Segunda persona y tono directo.** La ficha le habla al usuario ("dame su catálogo y en una semana le enseñas..."), no a un cliente anónimo.
- **La jerga del nicho, explicada.** La sección de conceptos existe para que el usuario entre a la reunión sabiendo qué es un CMR o una tarifa de cliente. Sin eso, el cliente nota que no eres de su mundo y se acabó la venta.
- **Números concretos, no adjetivos.** "3-5 días" en vez de "lento". "12 h/semana" en vez de "mucho tiempo".
- **Callouts con moderación**: 3-4 por nota como máximo.
- **Honestidad sobre las limitaciones.** Si algo del servicio es frágil, caro o difícil de vender, se escribe. Una ficha optimista es una ficha inútil en una reunión.
- Frontmatter Obsidian completo según `[[obsidian-notes]]`: `title`, `date`, `tags` (`ia`, `automatizacion`, `neozeler` + tipo), `type: guia`, `status`, `related`.

## Errores frecuentes al diseñar el servicio

- **Vender la tecnología en vez del ahorro.** Nadie compra "un agente RAG sobre pgvector". Compran "tu comercial deja de contestar el teléfono y vuelve a vender".
- **Un servicio que hace de todo.** Imposible de demostrar en 10 minutos e imposible de presupuestar. Divide.
- **Prometer decisiones autónomas.** Todo lo que toque dinero, precio o compromiso con un cliente final pasa por validación humana. Esto además **se enseña en la reunión antes de que te lo pregunten**: es argumento de venta, no limitación.
- **Depender de datos limpios que el cliente no tiene.** Si el proceso necesita catálogo normalizado, historial estructurado o un ERP con API, eso es una fase previa facturable, no un supuesto.
- **Olvidar la métrica de renovación.** Todo servicio necesita un contador que justifique la cuota mensual cada mes. Si no se te ocurre cuál, el servicio no sostiene recurrencia.

## Salida esperada

Dos archivos `.md` listos para arrastrar al vault, con el nombre exacto `Servicio - {Nombre}.md` y `Demo - Servicio - {Nombre}.md`, más una línea de resumen para pegar en el MOC de Servicios.

## Archivos de referencia

- `references/plantilla-ficha.md` — estructura completa de la ficha comercial. Leer siempre antes de escribir.
- `references/plantilla-demo.md` — estructura completa de la nota de montaje. Leer siempre antes de escribir.
- `references/precios-y-prioridad.md` — horquillas de precio, criterios de dificultad y cómo asignar prioridad en el portafolio.
- `references/stack-neozeler.md` — piezas técnicas validadas, coste y criterio de "todo autoalojado".
