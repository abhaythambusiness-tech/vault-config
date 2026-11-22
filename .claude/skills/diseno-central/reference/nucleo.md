# Núcleo de diseño: valores exactos (fusión de impeccable, taste, hallmark, Jakub, garden, landing, tastemaker)

Si el proyecto tiene `DESIGN-IDENTITY.md` aprobado, **manda sobre todo lo de abajo**. Esto es el suelo de calidad, no una estética.

## Modo (impeccable)
Fijar uno antes de diseñar: **Operate** (apps, dashboards: precisión y familiaridad, motion 150-250 ms) · **Read** (contenido largo) · **Persuade** (landing, marketing: punto de vista y un momento autoral) · **Experience** (portfolio, narrativa). El brief gana al gusto propio.

## Diales (garden), 1-10: variance / motion / density / assets / brand
SaaS 6/5/4/6/5 · estudio o portfolio 8/7/3/8/4 · dashboard 4/3/8/3/7. La accesibilidad manda sobre cualquier dial. Declararlos en una línea.

## Tipografía
- Máx 2 familias (3 solo con una "outlier" en ≤2 sitios). Pesos ≥400 bajo 18 px. Fuentes **autoalojadas WOFF2** (sin CDN).
- Cuerpo ≥16 px (input 16 px en móvil), interlineado 1.5-1.65, medida 60-75ch (`max-width:62ch` en marketing). Caption 13/1.4.
- Escala marketing (taste): 2-3 tamaños muy separados, máx 5. small 13-14 · body 17-19 · lead 20-26 · head 32-64 · display `clamp(3rem,1rem+9vw,9rem)` ≥4x cuerpo (mín 2.5x). Display interlineado 0.85-1.05, tracking -0.02/-0.05em; ≥24 px tracking -0.01/-0.02em; mayúsculas ≤14 px +0.05em.
- Escala app (impeccable/Jakub): una familia, razón 1.125-1.2: body 16/1.5/400 · heading 18/1.3/600 · title 24/1.2/600 · display 36/1.1/600.
- Titulares ≤2 líneas en cualquier ancho (~32 caracteres), `text-wrap: balance`; párrafos `pretty`. Un `h1`; hero ≤7 palabras / ≤50 car.; sublínea ≤22 palabras.
- `font-variant-numeric: tabular-nums` en cifras; `…` y `–` correctos; nbsp en unidades.
- Reflejo de IA a evitar sin motivo: Fraunces, Playfair, Cormorant, Lora, Syne, Space Grotesk/Mono, IBM Plex, DM Sans, Inter/Roboto/Poppins. Inter/Geist son válidas en UI densa de app.

## Color (OKLCH para generar; los hex de marca de NeoZeler se conservan como tokens)
- Suelo 70-90 %, tinta, **un acento (máx 2) <5 % del viewport**, croma .12-.22. Sin `#000`/`#fff`.
- Claro: papel `L 96-98 %` croma .005-.015, tinta `L 16-22 %`. Oscuro: base `L 12-16 %`, texto `92-96 %`, elevación = más claro (+3 %/nivel), acento -.02..-.04 croma y +5-10 % luz, peso -50. Neutros con croma ≥.005 hacia el tono ancla.
- Roles: canvas, texto, acción, foco, semánticos, datos. Primitivos por tono → semánticos por rol → componentes solo semánticos. Estado ≥15° de hue del acento. 1 color = 1 significado; nunca color como único código.
- Contraste: texto 4.5:1, grande/UI/foco 3:1 (APCA: cuerpo Lc75, label 60, grande 45). Sobre color, el secundario es del tono (no gris). Arreglar con luminosidad. Texto bajo ~55 % de opacidad a <14 px sobre oscuro = fallo.
- Gradientes `in oklab`; nunca morado→azul ni 3 paradas. Ningún color ni `font-family` literal fuera de `:root`.
- Medir: `python3 -I scripts/check_contrast.py "#fff" "#777"`.

## Espacio, capas y radios
- Escala 4 (2, 4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96, 128, 144 px), `gap` en vez de márgenes. Más aire sobre el título que debajo. Gap entre grupos ≥2x el interno. Entre botones 12 px.
- Secciones landing: 64 / 96 (núcleo) / 128 (hero, demo). Padding interior ≤ exterior; tarjeta ≥24 px.
- **Elevación: declarar una** (borde O sombra; ambos = tarjeta fantasma). Sombra de 3 capas: `0 0 0 1px oklch(0 0 0/.06), 0 1px 2px -1px oklch(0 0 0/.06), 0 2px 4px oklch(0 0 0/.04)` + `border:1px solid transparent`; oscuro `0 0 0 1px oklch(1 0 0/.08)`. Imagen: outline `1px` offset -1px `oklch(0 0 0/.1)` (nunca tintado).
- Radios: tarjeta 12-16 px; píldora solo en controles pequeños; **anidado: interior = exterior − gap** (radio ext = int + padding). Icono-botón: -2 px de padding en el lado del icono.
- z-index 1 / 10 / 100 / 200 / 400 / 500 / 600.

## Estados y controles
- 8 estados: default, hover (solo `@media (hover:hover)`), `:focus-visible` (2 px, offset 2 px, 3:1), active (`scale(.97-.98)`), disabled (.5), loading (skeleton, no spinner), error (inline), success. Vacío compuesto, nunca pantalla en blanco.
- Diana 44 px (24 mínimo AA; 40 en escritorio; usar pseudo-elemento). Una acción primaria por vista (>3 secundarias → menú). Validar al enviar/blur, no al teclear; `aria-invalid` + `aria-describedby`; foco al primer inválido; submit sin `disabled`.
- Nativo antes que ARIA. `<dialog showModal>` y devolver foco. Toast ≥5 s con pausa en hover. Modal = último recurso.
- Nunca `user-scalable=no`; capas decorativas con `pointer-events:none`; `::selection`, caret y scrollbar tematizados.

## Móvil y layout
`html,body{overflow-x:clip}` (no hidden) · `minmax(0,1fr)` + `min-width:0` · `overflow-wrap:anywhere` · `dvh`, nunca `100vw`/`100vh` · CTAs `nowrap` (acortar la etiqueta antes) · propiedades lógicas · `@container` · `scroll-padding-block-start` = header · `repeat(auto-fit,minmax(280px,1fr))` · `clamp(1rem,.9rem+.5vw,1.125rem)` · tabla → tarjetas en móvil · `srcset`/`<picture>`, lazy solo bajo el pliegue · breakpoints en `rem`. Probar 375 / 768 / 1280 y además 320 sin scroll horizontal y 200 % zoom.

## Pantallas de app y dashboards (taste, 23 productos)
Sidebar 210-292 px (230) · fila 32-34 px · iconos 16 px trazo 1.5 · activo = píldora gris r8 · top bar 44-51 o 64 px · gutter único 24-36 px · h1 24 px/600-700, un sustantivo. KPI 24-30 px (cifra respuesta 30-36, ≥1.3x), etiqueta 14 px gris, sin icono-círculo ni sparkline, delta 10-15 px, color = bueno/malo. Tablas: filas 36-53 px, cabecera 12 px sin fondo, cifras a la derecha `tabular-nums`, sin cebra. Píldoras 20 px. Gráficos: 1 serie, 3-5 gridlines 1 px `#e5e5e5`, línea 2 px recta, barras cuadradas, 4-7 ticks 12 px, anotar eventos. Oscuro tipo Linear: bg `#08090A`, S1 `#16171C`, S2 `#1E1F25`, hairline `rgba(255,255,255,.06)`, texto `#F7F8F8`/`#9CA3AF`, radios 6/12/16.

## Jerarquía (3 reglas)
Un punto de entrada visual · peso ≥1.5x entre niveles · un solo énfasis por zona. Fallos: varios primarios, aplanamiento, CTA enterrado. Pruebas: **entornar los ojos** (¿qué se ve primero?) y **borrado** (¿qué se puede quitar sin perder?).

## Iconos y assets
Una librería (Lucide por defecto; Phosphor/Solar válidas; nunca Material). Outline por defecto, fill en activo; trazo 1.5 px (peso 400) / 2 (500-600) / 2.5 (700); `currentColor`. Logo real obligatorio; si falta, preguntar. Cero métricas, testimonios, logos ni caras inventados; sin chrome falso (barras de navegador, marcos de móvil).

## Resolución de choques (decisiones fijas)
Identidad aprobada > brief > esta tabla > gusto. Decidir solo; preguntar únicamente si falta identidad o una imagen. Parallax ≤8 % solo con dinamismo ≥2; cursor propio solo con dinamismo 3 y `(hover:hover) and (pointer:fine)`. Tipo marketing: taste; app/lectura: impeccable. Motion: tokens de `movimiento.md`. Dashboards: sección de arriba.
