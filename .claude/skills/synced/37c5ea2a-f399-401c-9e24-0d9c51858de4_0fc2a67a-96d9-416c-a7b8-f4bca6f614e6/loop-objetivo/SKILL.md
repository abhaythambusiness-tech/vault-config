---
name: loop-objetivo
description: Bucle de auto-verificación antes de entregar cualquier respuesta con entregable concreto. Úsame SIEMPRE que el usuario pida que se haga algo y no solo una charla — cualquier tarea con un entregable concreto: redacción de textos, emails, documentos o posts; análisis de datos, mercado o competencia; código, scripts o debugging; planificación y estrategia; resúmenes; automatizaciones y workflows; creación o mejora de prompts; propuestas, informes y presentaciones. Actívame aunque la petición sea informal ("hazme un...", "prepara...", "escríbeme...", "monta...", "revisa y arregla..."). El agente extrae el objetivo real, genera, audita su propio output contra una checklist de criterios y regenera si no encaja — el usuario solo ve el resultado final, nunca las iteraciones. NO me actives para: saludos, conversación casual, preguntas factuales de una línea, o aclaraciones rápidas sin entregable.
---

# Loop-Objetivo: Auto-verificación antes de entregar

Antes de entregar cualquier respuesta con entregable, compara tu output contra el objetivo real del usuario y regenera si no encaja. El usuario solo ve el resultado final.

## Fase 1 — Extraer el objetivo

Lee el prompt del usuario y destila:

- **Objetivo real** (no el literal): qué quiere conseguir con esto, no solo qué ha escrito.
- **Formato del entregable**: tipo, estructura, longitud aproximada, idioma, destino de uso.
- **Criterios de éxito**: qué haría que el usuario dijera "esto es exactamente lo que necesitaba".
- **Restricciones explícitas e implícitas**: límites de longitud, tono, tecnologías, presupuesto, audiencia.
- **Qué NO se pide**: para no inflar el entregable con cosas que nadie quiere.

Escribe esto como una **checklist interna de 3-6 criterios verificables**. Verificable significa que puedes responder sí/no mirando el output, sin opinar.

**Ambigüedad**: si hay una ambigüedad que cambiaría materialmente el resultado, haz **UNA sola pregunta** antes de empezar. Si no la hay, asume lo más razonable y declara la asunción en una línea al final de la respuesta. Nunca hagas rondas de preguntas.

### Ejemplo de checklist bien construida

Petición: "Prepárame una propuesta de precios para el cliente X con tres escenarios."

- [ ] Incluye exactamente los 3 escenarios de precio pedidos (básico, medio, premium)
- [ ] Cada escenario tiene precio concreto, qué incluye y qué no
- [ ] Formato: documento listo para enviar al cliente, no notas internas
- [ ] Tono comercial pero sin humo — cada afirmación de valor tiene respaldo
- [ ] Cabe en 1-2 páginas; el cliente lo lee en 3 minutos

### Ejemplo de checklist mal construida

- [ ] Que esté bien
- [ ] Que sea profesional
- [ ] Que al cliente le guste
- [ ] Que sea completo

Criterios vagos = auditoría imposible. Si no puedes verificar un criterio mirando el output, reescríbelo hasta que puedas.

## Fase 2 — Generar

Produce el output completo contra esa checklist. No a medias, no un borrador: la versión que entregarías.

## Fase 3 — Auditoría contra objetivo

Revisa el output **criterio por criterio** con veredicto: **CUMPLE / PARCIAL / FALLA**.

Busca activamente los fallos típicos:

- Responder a una versión más fácil de la pregunta que la que se hizo
- Relleno genérico que podría estar en cualquier respuesta sobre el tema
- Formato equivocado (pidieron tabla y hay prosa; pidieron email y hay informe)
- Ignorar una restricción explícita o implícita
- Longitud desajustada (el doble o la mitad de lo útil)
- Afirmaciones sin respaldo, números inventados, promesas vacías
- Tono que no encaja con el uso final del entregable

**Sé adversarial, no complaciente.** Si todo sale CUMPLE en la primera pasada, la auditoría se ha hecho mal: vuelve y busca el punto más débil del output. Siempre hay uno.

## Fase 4 — Decisión

- **Todos CUMPLEN** → entregar.
- **Algún PARCIAL o FALLA** → regenerar corrigiendo específicamente eso. No reescribas desde cero lo que ya funcionaba: cirugía, no demolición. Vuelve a Fase 3.
- **Máximo 3 iteraciones.** Si tras la tercera sigue habiendo un criterio sin cumplir, entrega la mejor versión y di en una línea qué quedó corto y por qué.

## Reglas de salida (críticas)

- **No mostrar** la checklist, la auditoría, los veredictos ni las iteraciones.
- **No narrar** el proceso: nada de "he revisado y...", "iteración 2:", "tras verificar...".
- La respuesta debe verse como si hubiera salido bien a la primera.
- **Excepción**: si el usuario escribe "muestra el loop", expón la checklist y los veredictos de la última auditoría.

## Nota de calibración

Para peticiones triviales (un email de dos líneas, un rename, una lista rápida), una sola pasada de auditoría mental basta — no montes checklist formal. El bucle completo es para entregables de peso: documentos, análisis, código, propuestas, sistemas. El objetivo es calidad, no gastar tokens en ceremonia. Si dudas de si algo es "de peso": ¿el usuario va a usar esto delante de otra persona o va a construir sobre ello? Entonces es de peso.
