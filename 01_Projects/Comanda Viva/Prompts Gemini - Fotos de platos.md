---
type: guia
proyecto: "Comanda Viva"
status: activa
date: 2026-11-04
origen: mixto
---

# Prompts Gemini — fotos de platos

> [!resumen] En cristiano
> Textos para pegar en Gemini y obtener una foto por plato con el mismo estilo. Se pega siempre el **bloque de estilo** entero y detrás la línea del plato. Cuando tengas las fotos reales de la clienta, esas mandan y estas sobran. Las imágenes se pasan a WebP de 800×800 y ≤ 80 kB. Fondo liso crema (el pastel anterior se descarta con la dirección sobria).

## Bloque de estilo (pegar entero, sin retocar)
```
Overhead 90-degree food photograph of a single plated breakfast dish on a handmade ceramic plate,
soft natural window light from the left, gentle realistic shadow, appetizing true-to-life colours,
plain warm off-white paper background (#F6F2EA), centred composition with generous margin,
square 1:1 format, no hands, no cutlery clutter, no text, no logos, no watermark,
not illustrated, not 3D-rendered, looks like a real photo taken in a small Spanish café.
```

## Una línea por plato (se añade después del bloque)
| Plato | Línea para Gemini |
|---|---|
| Tostada con tomate | `Dish: one thick slice of toasted country bread with grated tomato and a thin drizzle of olive oil.` |
| Tostada con jamón | `Dish: one thick slice of toasted country bread with grated tomato and thin slices of Spanish serrano ham.` |
| Tostada de aguacate y huevo | `Dish: toasted bread with sliced avocado and one fried egg with a runny yolk on top.` |
| Huevos revueltos | `Dish: soft scrambled eggs on a plate with one small slice of toast on the side.` |
| Café con leche | `Dish: a white ceramic cup of café con leche on a saucer, seen from above, light foam, no latte art.` |
| Zumo de naranja | `Dish: a clear glass of fresh orange juice seen from above, with half an orange beside it.` |

## Pasos
1. Pega bloque + línea en Gemini, una imagen por plato.
2. Descarta las que tengan texto, manos o platos distintos al de la carta real.
3. Guárdalas en `~/Proyectos/comanda-viva/public/platos/<slug>.webp` (800×800, ≤ 80 kB) y avísame: las enlazo al menú.
4. Honestidad: son imágenes generadas, no del local. Cambiarlas por fotos reales en cuanto existan.

## Relacionado
[[3 - UI-UX Design]] · [[6 - Plan de Implementacion]] (T-21)
