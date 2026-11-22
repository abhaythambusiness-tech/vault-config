---
title: 'Reto 30: camino vertical estilo Duolingo'
date: '2026-11-20'
type: meta/sesion
origen: maquina
proyecto: '[[01_Projects/Reto-30]]'
sesion_id: b6180faf-eb82-4f30-850c-6de76c5e0be2
tags:
- sesion
- reto-30
- ui
---

> [!resumen] En cristiano
> Haytham pidió que la pantalla de inicio de Reto 30 muestre los días como círculos en un camino vertical, como Duolingo. Era viable (solo cambia la pantalla) y quedó hecho en local, sin commit.

## Qué se hizo
- Estudio de viabilidad: 1-2 días, sin tocar la base de datos; los 30 días, el extra cada 3 días y las rutas `/reto/[dia]` ya existían.
- Implementado en el panel: **camino vertical** con reveal por semanas (semana en curso + 2 días apagados de la siguiente), **insignias** junto a los días 7, 14, 21 y 28, **comodín** junto al día que lo da (cada 7 días en Básico/Medio, cada 10 en Avanzado), reto extra opcional.
- Se quitó el mapa serpenteante de abajo y se borró `RoadMap.tsx` (nada lo usaba). Revisado en 375 px; `tsc` limpio salvo caché `.next/dev/types`.
- Última petición («mejora un poco el roadmap») se interrumpió.

## Pendientes
- Probar con cuenta real, limpiar `.next/dev/types`, **commit** (no hecho).
- Retoque pendiente del camino.

## Relacionado
- [[01_Projects/Reto-30]] · [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

