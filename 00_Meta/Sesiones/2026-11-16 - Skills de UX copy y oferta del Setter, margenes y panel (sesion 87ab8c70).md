---
type: sesion
date: '2026-11-16'
proyecto: '[[01_Projects/Setter NeoZeler]]'
origen: maquina
sesion_id: 87ab8c70-7372-4182-89f3-8f1cd966e9e4
tags:
  - sesion
  - cierre-automatico
---

> [!resumen] En cristiano
> Haytham pidió skills de marketing para diseño de producto. Se añadió una guía de textos de interfaz (UX copy) a `diseno-central` y se mejoró `oferta-central` con ficha y precios. Se actualizó la oferta del Setter con paquetes, extras y márgenes. También se rehízo el panel `resumen.html`, más claro y con gráficos. Cierre automático nocturno; complementa [[2026-11-15 - Oferta central y ficha de servicio del Setter]].

## Qué se hizo
- Búsqueda de skills de marketing para diseño de producto y decisión de cuáles encadenar.
- `diseno-central`: nueva `reference/ux-copy.md`. `oferta-central`: `fases.md`, `ficha-oferta.md` y `pricing.md` revisados; `CLAUDE.md` global actualizado.
- Pregunta clave: ¿el Setter actual es un buen MVP para salir al mercado? Respuesta: sí, con huecos: falta el contrato de encargado de tratamiento (RGPD) antes de guardar conversaciones reales, y hay un cliente por instalación (workflows con IDs y tablas fijos: hay que clonar y parametrizar por cliente).
- Se aplicó a la tabla de paquetes §4 de [[02_Areas/NeoZeler/Servicios/Setter WhatsApp (Mila) - Oferta]]: notas de voz, datos de leads en tablas n8n y extra de CRM de 390 €; se añadió un apartado de márgenes.
- `resumen.html` del Setter rehecho: menos texto, menos pestañas (agrupadas), gráficos en los datos y menos negro.
- Nueva regla `~/.claude/rules/oferta.md` (se carga sola al tocar servicios, ofertas, pricing, propuestas o PRD) e índice en el global §5.

## Decisiones tomadas
- Nada de Google Sheets: los datos van en las tablas de n8n.
- El agente de producto («Mila», pero podrá ser «Sofia» u otro nombre en otro VPS) es una plantilla clonable: la paquetización debe valer para varios clientes y negocios.
- La skill nueva se activa sola mediante regla por rutas.

## Problemas
- Sin capturas 375/1280 px del `resumen.html` (pendiente en `.capturas/` del repo).

## Próximos pasos
- Contrato de encargado de tratamiento (RGPD) antes de datos reales.
- Parametrizar el clonado por cliente (número, horario, prompt).
- Hacer las capturas responsive del `resumen.html`.

## Relacionado
- [[01_Projects/Setter NeoZeler]] · [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
