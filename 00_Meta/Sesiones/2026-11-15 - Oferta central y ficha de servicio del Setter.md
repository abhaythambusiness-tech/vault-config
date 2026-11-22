---
type: sesion
status: completado
origen: mixto
date: '2026-11-15'
proyecto: '[[01_Projects/Setter NeoZeler]]'
tags:
- sesion
- oferta
- setter
- diseno
---

> [!resumen] En cristiano
> Se creó la skill `oferta-central` (de idea a oferta con paquetes y precio) y se añadió referencia de textos de interfaz a `diseno-central`. Se probó con el Setter de WhatsApp y se rehízo su `resumen.html` como **ficha de servicio** con pestañas (producto, paquetes, funcionamiento, costes, tiempos, mercado, estado), pensada para repetirse con cada servicio.

## Qué se hizo
- `~/.claude/skills/oferta-central/` (8 fases con puertas) y routing en el `CLAUDE.md` global; `diseno-central/reference/ux-copy.md`.
- Oferta del Setter: [[02_Areas/NeoZeler/Servicios/Setter WhatsApp (Mila) - Oferta]] (§11: tokens y VPS incluidos, audios/seguimiento por construir, CRM del cliente 390 € + 29 €/mes, CRM propio no se vende; sin Google Sheets, datos en tablas de n8n).
- `~/Proyectos/setter-neozeler/resumen.html` reescrito: 8 pestañas, bloque `SVC` reutilizable, persona configurable. Verificado a 375/1280, claro y oscuro, sin errores de consola ni scroll horizontal; capturas en `.capturas/`.

## Aprendizajes
- Un servicio = una persona con nombre por instalación; el resumen no debe fijar «Mila».
- Convención: toda ficha de servicio muestra producto, paquetes, funcionamiento, costes, tiempos, mercado y estado, marcando medido vs estimado.
- Pendiente: aprobar cambios de la tabla §4 de la oferta; `oferta-central` aún no comprueba si ya existe una ficha de oferta.


## Cierre
- Ficha rediseñada: tema claro, 5 pestañas, gráficos (Chart.js); copia alojada en https://claude.ai/artifact/WwJotVrmiQT4sAHLEoiRnd (privada).
- Regla nueva `~/.claude/rules/oferta.md` (por `paths`): invoca `oferta-central` al tocar servicios, ofertas, pricing, propuestas o PRD; indexada en CLAUDE.md global §5.
- Pendiente: capturas 375/1280 en `.capturas/` del repo; `oferta-central` sin comprobación previa de oferta existente (la regla lo cubre).
