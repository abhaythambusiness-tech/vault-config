# Referencia: animaciones de dosduostudio.com (2026-11-17)
Fuente completa (tabla de 14 animaciones, intro, flotación): vault `03_Resources/Referencia - Animaciones GSAP de dosduostudio.md`. Analizada sobre `/js/site.js` minificado; GSAP 3.15.0 + ScrollTrigger, sin ScrollSmoother ni Flip, scroll nativo.

## Valores a copiar (traducir a `motion`; GSAP está fuera del stack)
- **Scrub**: `ease:"none"`, inercia `.4-.7`. `motion`: `useScroll({target,offset})` + `useTransform`.
- **Entrada única**: `once`, `y` 34-44 px, `duration` .9-1, `power3.out`/`expo.out` (≈ `[.16,1,.3,1]`), stagger .08-.1, disparo `top 72-84%`. `motion`: `whileInView` + `viewport={{once:true}}`.
- **Pop de items**: escala .85→1 + opacidad, `back.out(1.6)`, stagger .08, .8 s.
- **Transición entre secciones**: saliente → escala .93-.94, opacidad .35-.4 (`top bottom`→`top top`/`top 12-15%`); entrante .94/.4 → 1/1 en `top top`→`top+=innerHeight top`.
- **Pin largo** (≈2.4 pantallas): timeline con `scrub:.7`; en `motion`, `position:sticky` + `useScroll` sobre la sección alta.
- **Flotación**: tres tweens `y/rotation/x`, `sine.inOut`, yoyo infinito, duraciones aleatorias 1-3.8 s; parar con reduced-motion.
- **Vídeo**: `data-src` + `IntersectionObserver` (`rootMargin:"200px 0px"`), pausar fuera de vista.
- **Intro**: máx. un timeline, saltable con cualquier input.
- `invalidateOnRefresh` para medidas; `quickSetter` para lo que cambia cada frame.
