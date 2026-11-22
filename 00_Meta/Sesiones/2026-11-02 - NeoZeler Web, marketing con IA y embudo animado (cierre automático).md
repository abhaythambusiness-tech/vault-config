---
title: "Sesión - 2026-11-02 - NeoZeler Web, marketing con IA y embudo animado (cierre automático)"
date: 2026-11-02
type: meta/sesion
proyecto: "[[NeoZeler Web]]"
sesion_id: 41fb6399-6da0-4798-b3a4-9d6dfe3d656a
tags:
  - sesion
  - cierre-nocturno
aliases: []
origen: mixto
---

# Sesión — 2026-11-02: NeoZeler Web, marketing con IA y embudo animado (cierre automático)

> [!resumen] En cristiano
> A la web de NeoZeler se le añadió marketing con IA y un módulo de venta. El embudo no convencía, así que se rehízo animado con anime.js v4. La sesión ya dejó su nota; esta la enlaza.

> Cierre automático (tarea nocturna) a partir del historial de la sesión `41fb6399`; es un resumen fiel pero breve, el detalle está en la conversación original.

## Qué se hizo
- Nuevas secciones (`negocios.tsx`, `lanzamientos.tsx`, `modulo-venta.tsx`) y figura hairline del embudo.
- Embudo animado con anime.js v4: 18 personas entran, unas caen en cada puerta y quedan 3 brillando; se mueve una vez al entrar en pantalla con botón «Ver otra vez»; con `prefers-reduced-motion` y sin JavaScript se ve ya resuelto.
- Excepción a la regla «cero librería de animación», anotada en `DESIGN-IDENTITY.md` §7, UI-UX del vault, README y ficha.

## Decisiones tomadas
- anime.js como única librería de animación (GSAP pesa más y no hace falta).

## Archivos y proyectos afectados
- `~/Proyectos/neozeler-web/src/components/embudo-animado.tsx`
- `01_Projects/NeoZeler Web.md`

## Problemas
- Movimiento reducido no probado en el navegador.

## Mejoras propuestas
- Ninguna registrada.

## Pendientes y próximos pasos
- Medir Lighthouse y 375/768 px con el embudo nuevo.

## Relacionado
- [[2026-11-02 - NeoZeler Web, marketing con IA, modulo de venta y embudo hairline]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
