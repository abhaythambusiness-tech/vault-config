---
type: proyecto
status: congelado
date: '2026-10-30'
repo: ~/Proyectos/lancet-antigravity-web
origen: https://github.com/melianeliezer05-a11y/Lancet-antigravity-web
---

> [!resumen] En cristiano
> Web de NM Electroclima (electricista y climatización de Néstor Melián, Andalucía), rediseñada entera el 2026-10-30 con un estilo de «plano técnico». Mantiene el aviso urgente, los trabajos y las opiniones. Falta subir fotos reales y proteger mejor el panel interno.

## Qué es
Landing pública (`/`) y panel interno (`/admin`) en React + Vite + Supabase. Código en `~/Proyectos/lancet-antigravity-web/` (clon del repo de origen, sin commit ni push todavía).

## Diseño (decidido con Haytham)
- Dirección: plano técnico (papel hueso, azul tinta, naranja del rayo del logo, Archivo + IBM Plex Mono).
- Imágenes: SVG ilustrados propios (no había fotos reales).
- Se descartó todo el diseño anterior (fondo oscuro cian, splash, emojis).

## Pendiente
- Clave de `/admin` visible en el JS del cliente: migrar a Supabase Auth + RLS.
- Clave anónima de Supabase escrita en `src/supabaseClient.js`: pasar a variables `VITE_*`.
- Confirmar con el cliente los textos «Presupuesto claro y antes de empezar» y «Toda Andalucía».
- Subir fotos reales de trabajos desde `/admin`.

Detalle técnico: README del repo.

