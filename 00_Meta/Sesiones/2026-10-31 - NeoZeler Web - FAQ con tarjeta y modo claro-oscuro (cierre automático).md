---
title: "Sesión - 2026-10-31 - NeoZeler Web - FAQ con tarjeta y modo claro-oscuro (cierre automático)"
date: 2026-10-31
type: meta/sesion
proyecto: "[[NeoZeler Web]]"
sesion_id: 23f82061-f5b2-43a3-bddb-3fcdf1b7de35
tags:
  - sesion
  - cierre-nocturno
aliases: []
origen: mixto
---

# Sesión — 2026-10-31: NeoZeler Web: FAQ con tarjeta y modo claro/oscuro (cierre automático)

> [!resumen] En cristiano
> Un hueco vacío de la web pedía un dibujo; Haytham rechazó varios y se acabó cambiando el enfoque (tarjeta de contacto en la FAQ). También se quitó el selector «mundo papel/croma» y se dejó solo modo claro u oscuro. La sesión ya dejó su propia nota; esta la enlaza.

> Cierre automático (tarea nocturna) a partir del historial de la sesión `23f82061`; es un resumen fiel pero breve, el detalle está en la conversación original.

## Qué se hizo
- Rechazados tres dibujos SVG sin preguntar antes; se cambió de enfoque.
- Se eliminó el selector de «mundos» y se dejó el botón de modo claro/oscuro.
- Commit en `neozeler-web` con las preguntas frecuentes (tarjeta de contacto) y el botón.
- 4 errores nuevos (#71-#74) en `.claude/COMMON_MISTAKES.md`; sección «Tailwind 4 / Next 16» en `librerias.md`; regla de memoria sobre adornos visuales.

## Decisiones tomadas
- Tras un rechazo visual, ofrecer 2-3 enfoques distintos y preguntar.

## Archivos y proyectos afectados
- `faq-lista.tsx`, `faq.tsx`, `world-switch.tsx`, `(legal)/cookies/page.tsx`

## Problemas
- Build vieja en el puerto 3000; `pkill -f` mató su propia shell; Node 18 con Next 16.

## Mejoras propuestas
- Ninguna registrada.

## Pendientes y próximos pasos
- Puerto 3000 sin supervisión.
- Revisar la tarjeta a 375 y 768 px; axe y Lighthouse.
- Retro del proyecto.

## Relacionado
- [[2026-10-31 - NeoZeler Web FAQ tarjeta y modo claro-oscuro]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
