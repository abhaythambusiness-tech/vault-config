# Movimiento (fusión de Emil Kowalski, animate, taste, hallmark, Meng To)

## Puerta: ¿animar?
Frecuencia alta (teclado, acciones repetidas cientos de veces/día) → **no animar**. Animar solo si comunica estado, guía la atención o da continuidad. Una animación que no pasa esto se borra. Un solo momento "autoral" por pantalla (500-800 ms); el resto es feedback.

## Tokens
- Curvas: `--ease-out: cubic-bezier(.22,1,.36,1)` · `--ease-expo: (.16,1,.3,1)` (≥800 ms) · `--ease-in-out: (.76,0,.24,1)` · `--ease-drawer: (.32,.72,0,1)` · salida `(.55,.055,.675,.19)`. Nunca `ease`, `ease-in`, bounce, `scale(0)` ni `transition: all`. Definir **una curva propia del proyecto** y reutilizarla.
- Tiempos: press 100-160 · hover 150-180 · UI 240 · overlay 300-500 · reveal 600-800 · apertura 1200 máx. Salida = 75 % de la entrada.
- Solo `transform` y `opacity` (+ `clip-path`, `filter: blur` ≤4 px). Acordeón: `grid-template-rows 0fr→1fr`. Contenido visible por defecto (sin JS el hero se lee).

## Vocabulario: situación → duración / curva / propiedad
| Situación | Duración | Curva | Propiedad |
|---|---|---|---|
| Press botón | 160 ms | ease-out fuerte | scale .97 |
| Hover fila/color | 100-150 | ease | background/opacity |
| Tooltip | 125 (0 si vecino abierto) | ease-out | opacity + scale .97 |
| Popover/menú | 200 | ease-out fuerte | opacity + scale .95, origin en el trigger |
| Modal | 250 | ease-out | opacity + scale .96 + backdrop |
| Drawer | 500 | (.32,.72,0,1) | translateY(100%) |
| Toast | 400 | ease | opacity + translateY, `@starting-style` |
| Acordeón | 200 | ease-out | height/rows + opacity |
| Stagger de entrada | 300, +50-60 ms/ítem (tope 500) | ease-out | opacity + y 8-12 (+blur 4) |
| Salida | 150 | ease-out | opacity + y -12 + blur 4 |
| Cambio de icono | 300 | spring bounce 0 | scale .25→1, blur 4→0, opacity |
| Hold-confirm | 2 s pulsar / 200 ms soltar | linear / ease-out | clip-path inset |
| Indicador de tabs | 250 | in-out fuerte | clip-path (copia del activo) |
| Reveal al scroll | 600-800 ms, una vez | in-out fuerte | clip-path `inset(0 0 100% 0)→0` o y 16-32 px |
| Drag settle | 500 | spring bounce .2 | transform |

Springs: `{duration:.4, bounce:0}` por defecto. Stagger CSS: `calc(var(--i)*60ms)`. Primer render: `initial={false}`. Al cambiar de tema, suprimir transiciones. Interrumpible: las transiciones CSS se pueden revertir; los keyframes no para cosas interactivas.

## Reduced-motion
Menos, no cero: sin scrub, parallax, ni scroll suave; crossfade de 150 ms; foco instantáneo; estado final visible. Skill de apoyo: `web-animation-skills:accessible-animation`.

## Scroll-storytelling (solo Persuade/Experience)
1. Declarar antes de código: tesis, foco del hero, tipo, paleta, narrativa de movimiento, motor de scroll.
2. **Un** motor: Lenis (`lenis.on('scroll', ScrollTrigger.update)`) + GSAP ScrollTrigger; `ScrollTrigger.refresh()` tras cargar fuentes; destruir al desmontar.
3. Intro del hero: timeline de máx 4 beats (nav → titular palabra a palabra, stagger ~.06 → sub + CTA → visual); el CTA es usable ya. Titular dividido por palabras conserva el nombre accesible (`aria-label`).
4. `scrub` para ensamblado del hero, contadores y trazos SVG; `pin` en 1-2 secciones máx; parallax sutil (<8 %). Tagline reveal: palabras de 25-35 % a 100 % de opacidad al cruzar la línea de disparo. Wipe antes/después con `clip-path: inset()` (rango 15-85 %).
5. Un momento firma; no apilar marquees + pins; nada de blobs ni glass en todo.
6. Three.js solo si es el producto: DPR con tope, pausa fuera de pantalla, `dispose`, póster y pérdida de contexto.
7. Árbol de librería (una por proyecto): `motion` (React, layout/gestos) · GSAP+ScrollTrigger (scroll/pin) · Anime.js v4 (`animate`, `createTimeline`; secuencias sin scroll) · CSS puro si basta.
8. Valores de scrub, entradas y transiciones entre secciones de una web de referencia (dosduostudio.com): `reference/referencia-dosduo-gsap.md`.

## Micro-interacciones de app (donde más rinde)
Feedback de envío de formulario, flotación al hover, botón con press, conmutadores, listas que entran/salen, toasts. Pocas, rápidas (150-250 ms), todas con la misma curva.
