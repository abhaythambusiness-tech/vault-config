---
type: retro
proyecto: "Los Apuntes de Liyo"
tipo: micro-saas
status: pendiente
retoques:
revisada: false
date: 2026-10-28
origen: mixto
---

> [!resumen] En cristiano
> La retro es el "qué aprendimos" del proyecto. Esta es la del piloto y **sigue pendiente**: falta la cifra de retoques, que solo Haytham puede confirmar, y el proyecto aún no está desplegado.
> Lo que sí consta: la primera versión del diseño salió "cutre" y hubo que rehacer el front el 2026-10-28.
> El tipo `micro-saas` es provisional hasta que Haytham lo confirme.

# Retro de Proyecto

## Retoques
- Cifra y qué se corrigió: pendiente de confirmar con Haytham. Hecho constatado: rediseño completo del front el 2026-10-28 («muy cutre»: entrada pequeña y vacía, módulos y chat en pestañas).

## Nivel frente a referencias
- Pendiente de confirmar con Haytham: el rediseño no se ha comparado aún con Linear, Readwise Reader ni la biblioteca de noche de la ficha.

## Skills previstas vs usadas
- Previstas en la ficha: `hallmark`, `impeccable`, `accessible-animation`, `accesslint-audit`, `pre-ship-gate`, `ponytail-review`. Uso real: pendiente de confirmar con Haytham (la ficha se escribió a posteriori).

## Librerías
- Previstas y usadas: Bun + TypeScript, `bun:sqlite` (FTS5), `unpdf`, Groq con `fetch`; en `package.json` solo `unpdf` como dependencia. Sin trampas anotadas aún.

## Lecciones
| Síntoma | Causa | Regla | dominio | documento-destino |
|---|---|---|---|---|
| Diseños anteriores y la v1 de Liyo salieron "cutres" | No se investigaron referencias de nivel alto ni se miró el resultado antes de entregar | Fijar 2-3 referencias en la ficha y compararlas al cerrar; ver la pantalla en navegador antes de darla por buena | diseno | UI-UX |
| Librerías elegidas sin investigar | Se tomó la primera opción o la de memoria; `pdf-parse` quedó sin verificar | Comparar al menos dos candidatas con versión, licencia y mantenimiento en la ficha antes del TRD | librerias | TRD |
| Entregas del mínimo que funciona | Se paró al cumplir lo básico, sin pulido | Reservar fase de pulido con `impeccable` antes de entregar | diseno | Plan |
| Skills sin aprovechar a fondo | No se nombraban por fase | Listar skill por fase en la ficha y revisarla en la retro | skills | Plan |
