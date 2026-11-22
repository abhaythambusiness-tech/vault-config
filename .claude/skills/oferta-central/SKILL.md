---
name: oferta-central
description: Usar SIEMPRE que Haytham quiera crear, validar, empaquetar o poner precio a un servicio o producto (oferta, paquetes, pricing, propuesta de valor, garantía, mensaje de venta, "cómo lo vendo", "cuánto cobro", "qué incluye", "paquetízalo"). Director de la cadena producto y mercado: orquesta before-you-build, buscador-oportunidades, growth-diagnostic-consultant, product-management, marketing-psychology, marketing-knowledge-base y brand-style en 8 fases con puertas. Sale con una Ficha de Oferta lista para landing, propuesta y spec. No construye ni maqueta (eso es nuevo-proyecto y diseno-central).
---

# oferta-central

Un solo sitio para pasar de idea a **oferta vendible**: qué vendo, a quién, por qué me compra, qué incluye, cuánto cuesta y cómo lo digo. Lenguaje sencillo (global §1): conclusión primero, términos traducidos, recuadro «En cristiano» en lo que se guarde.

Regla madre: **sin número no hay valor** y **sin señal de demanda no hay oferta**. Si falta un dato, una pregunta; no inventar cifras ni testimonios.

## Paso 0: tamaño y punto de entrada (una línea)

«Entrada: X · Tipo: Y». Duda entre dos: la mayor.

| Entrada | Qué hay | Empezar en |
|---|---|---|
| **Sin idea** | «No sé qué vender» | Fase 1 |
| **Idea cruda** | Servicio/producto en la cabeza | Fase 2 |
| **Oferta existente** | Ya se vende; mejorar paquetes o precio | Fase 4 o 5 |
| **Cliente concreto** | Presupuesto para un negocio | Fase 5 (diagnóstico) y 8 |

Tipo: `servicio-NeoZeler` · `micro-saas` · `saas` · `startup` · `web-cliente` (vías en `[[01 - Tipos de producto (Micro SaaS, SaaS, Startup)]]`).

## Skills: solo estas

| Fase | Skill / agente |
|---|---|
| Cazar y generar ideas | `buscador-oportunidades` (modos A cazar, B desde cero, C funciones, D a la calle) |
| Validar | `before-you-build`; duro y con competencia: agente `project-idea-validator`; mercado: `last30days`, agente `investigador` |
| Valor, pricing, cierre | `growth-diagnostic-consultant` (regla 5-20 % del impacto, setup/mensual/híbrido) |
| Producto y alcance | `product-management:product-brainstorming`, `product-management:write-spec` |
| Persuasión y mensaje | `marketing-psychology`, `anthropic-skills:marketing-knowledge-base` |
| Voz y marca | `small-business:brand-style`; identidad visual: `diseno-central` |
| Texto de venta | `humanizer` (no en legal); microcopy: `diseno-central/reference/ux-copy.md` |
| Servicios NeoZeler ya hechos | `anthropic-skills:diseno-servicios-neozeler`, `anthropic-skills:estudio-8020` |

Detalle de cada fase, plantillas y fórmulas: `reference/fases.md`, `reference/pricing.md`, `reference/ficha-oferta.md`.

## Fases (puerta = no se pasa sin cumplirla)

**1. Oportunidad.** Problema real con dinero y poca competencia. `buscador-oportunidades`.
*Puerta*: un problema con quién lo sufre, cuánto le cuesta y de dónde sale la evidencia.

**2. Validación.** `before-you-build`: comprador, flujo actual, canal, motivo para cambiarse. Producto propio: señal de demanda antes de construir (entrevistas, lista de espera, prueba de pago). Duro: `project-idea-validator`.
*Puerta*: veredicto **sí / ajustar / no** con la prueba que lo sostiene. «No» = parar y archivar, no seguir.

**3. Promesa y oferta.** Una frase: «Ayudo a [quién] a [resultado medible] en [plazo] sin [mayor miedo]». Entregables concretos, plazo, garantía, qué NO incluye. Tres opciones de promesa, elegir una.
*Puerta*: promesa en una frase con resultado medible y plazo.

**4. Paquetes.** Tres niveles (entrada / recomendado / completo) con el recomendado marcado y el de entrada como señuelo honesto, no engañoso. Alcance cerrado por paquete, límites, extras con precio, qué pasa fuera de alcance. Servicio: setup + mantenimiento. Producto: planes y qué cambia entre ellos.
*Puerta*: tabla de paquetes donde cada diferencia se explica en una línea.

**5. Pricing.** `growth-diagnostic-consultant`: cuantificar el impacto en dinero del cliente (€/mes ganados o perdidos), cobrar 5-20 % según tamaño, urgencia y confianza; contrastar con coste propio (horas, tokens, herramientas; `neozeler-cfo`) y con la competencia. Producto: ancla, mensual vs anual, créditos/uso, prueba gratis o no. Antes de cobrar producto: `[[Checklist pre-cobro (micro SaaS)]]`.
*Puerta*: precio con margen mínimo calculado y justificado en valor, no en horas. Margen < objetivo = rehacer paquete, no regalar.

**6. Mensaje y persuasión.** `marketing-psychology`: ancla de precio, prueba social **real**, riesgo invertido (garantía), encuadre de pérdida/ganancia; cada táctica con el chequeo «¿es honesta?». `marketing-knowledge-base` para canal, ángulo y objeciones. Respuesta a las 5 objeciones típicas (precio, tiempo, confianza, «lo hago yo», «ahora no»).
*Puerta*: mensaje central, 3 beneficios con prueba, 5 objeciones con respuesta, sin claims sin respaldo.

**7. Voz y spec.** `small-business:brand-style` (tono, vocabulario, lo que nunca se dice). Si es producto: `product-management:write-spec` con la oferta como entrada (alcance del paquete = alcance del PRD); enlazar al flujo de 6 documentos (`nuevo-proyecto`, vault §0.10).
*Puerta*: guía de voz en 5 líneas y, si hay producto, spec o PRD enlazado.

**8. Ficha de Oferta.** Un documento final con todo lo anterior (plantilla en `reference/ficha-oferta.md`) en `02_Areas/NeoZeler/Servicios/<Nombre> - Oferta.md` (servicio) o `01_Projects/<Nombre>/` (producto), `origen: mixto`, con «En cristiano» arriba. De aquí salen: landing (`diseno-central` modo Persuade, texto vía este documento), propuesta (`[[Plantilla - Propuesta]]`) y secuencias (`marketing:email-sequence`).
*Hecho cuando*: ficha guardada, enlazada al proyecto y declarados fases saltadas y datos sin confirmar.

## Reglas

- Cifras, testimonios, casos y competencia: solo con fuente. Sin dato: «sin confirmar» y fecha de qué falta.
- No vender «IA» ni herramientas: vender el dinero que se pierde hoy o el tiempo que se libera.
- Precio por valor, nunca tarifa plana por horas (vault §2).
- Nada se envía, publica ni cobra sin permiso de Haytham; todo es borrador.
- Si choca con identidad aprobada, manda la identidad; con `nuevo-proyecto`, esta skill va **antes** de abrir proyecto.
- Declarar al cerrar: entrada, tipo, fases hechas, skills usadas, veredicto de validación, precio y margen, qué queda sin confirmar.
