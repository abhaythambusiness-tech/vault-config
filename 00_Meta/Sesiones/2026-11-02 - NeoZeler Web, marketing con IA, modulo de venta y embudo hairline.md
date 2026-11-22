---
type: sesion
status: cerrada
fecha: '2026-11-02'
proyecto: NeoZeler Web
tags:
- diseño
- web
- hairline
origen: mixto
---

> [!resumen] En cristiano
> La web de NeoZeler ahora ofrece dos servicios nuevos, «Marketing con IA» y «Módulo de venta con IA», tanto para negocios como para lanzamientos. Hay una sección nueva con un embudo de venta dibujado en trazo fino (hairline): cuatro bandejas que bajan y se estrechan; al pasar el cursor, la bandeja sube y se iluminan los contactos que pasan a la siguiente. Falta pasar axe y Lighthouse.

## Qué se hizo
- Repo `~/Proyectos/neozeler-web/`: dos tarjetas nuevas en `negocios.tsx` (título pasa a «Nueve cosas») y en `lanzamientos.tsx`; dos iconos nuevos en `svg-data.json` (`icon-marketing`, `icon-modulo`).
- Sección nueva `sections/modulo-venta.tsx` (en el bloque oscuro, tras la diagonal B) con el embudo.
- Figura: `hairline/embudo.js` → `public/embudo-figura.html` (skill `hairline-create`), mostrada en un iframe del mismo origen (`components/embudo-figura.tsx`) que oculta los controles de la página de hairline.

## Aprendizajes
- Node del sistema es 18: ni Next 16 ni `look.mjs` de hairline arrancan. Se usó el Node 24 de `~/.cache/ms-playwright-go/1.57.0/node`; la revisión visual de hairline se hizo a mano.
- Hairline trae su propio motor JS: choca con «cero librería de animación» de DESIGN-IDENTITY §7; aceptado al ir aislado en un iframe. Decisión pendiente de Haytham.
- Los contactos del embudo son dibujo (10·6·4·2), no cifras reales.


## Ronda 2: embudo con anime.js
Haytham pidió probar GSAP o anime.js para un embudo más vistoso. Elegido anime.js v4 (pequeño, bueno con SVG; GSAP solo si hubiera scroll pesado). `embudo-animado.tsx` sustituye al iframe hairline. Aprendizaje: con anime.js dibujar cada punto en su sitio final y animar el desfase hasta ahí deja un SVG correcto sin JS ni movimiento. Identidad §7 actualizada (única librería de animación). Sin medir: Lighthouse, movimiento reducido en navegador real.
