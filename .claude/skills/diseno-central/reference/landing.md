# Landing y páginas de conversión (landing-page-design, tastemaker, taste)

Una landing no es una home: **una oferta, una audiencia, una acción**. Todo lo demás se quita.

## Estructura de una acción (orden)
1 Nav mínima (logo + CTA; flotante translúcida con blur) · 2 Hero: promesa (6-12 palabras), sub (16-28), CTA único (+1 secundario), 1 prueba real, 1 visual · 3 Problema (corto) · 4 Solución mostrada (mockup o antes/después) · 5 Tagline reveal · 6 Cómo funciona (3 pasos) · 7 Beneficios (3-5, tamaños desiguales) · 8 Prueba social real · 9 FAQ (6-12) · 10 Inversión de riesgo · 11 CTA final idéntico al primero · 12 Footer legal. Sin dato real: marcador `{{testimonio}}`, nunca inventado.
Arco narrativo mínimo de 4 pasos: hook → problema → solución → cómo → prueba → cierre. Una ruptura intencional del ritmo.

## Lectura y jerarquía (detalle en `revision.md`)
- Landing = patrón **Z**: logo (1), CTA secundario arriba (2), valor al centro, pasos o iconos abajo (3), **CTA principal al final del recorrido (4)**. Repetir la Z por bloque si hay más de un argumento antes del CTA final.
- Contenido largo o de lectura = patrón **F**: lo importante en los dos primeros párrafos; cada título arranca con la palabra clave.
- Antes de entregar: **test del desenfoque** (blur 5-10 px). Debe destacar el CTA y el titular; si no, no entregar.

## Copy
- Titular atado a un hecho comprobable. Escribir 3 candidatos (mecanismo / resultado / tensión) y elegir. Fórmula: "{Resultado} sin {dolor}".
- CTA = verbo + qué ("Empezar prueba gratis"). Prohibido: revolucionar, potenciar, sin esfuerzo, de clase mundial, em dash.
- Estados vacío, error y carga con texto escrito. Mostrar, no contar.

## Hero
Sin badges ni rails; máx 1 chip de métrica **real**. Titular degradado de texto solo si la identidad lo pide (#FFF→#9B9B9B en oscuro), máx 680 px, `balance`. Hero usable sin JS. Etiqueta-izquierda/titular-derecha: evitar.

## Entrega
Skip link · 404 · legales · `og:image` · `<title>` y meta únicos · JSON-LD donde aplique · 390 px sin overflow · imágenes con `alt`/`width`/`height` · LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1 (detalle en `rules/web.md`).
