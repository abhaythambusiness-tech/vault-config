---
type: referencia
status: activo
date: 2026-10-19
tags: [reto-30, imagenes, prompts]
proyecto: Reto 30
origen: mixto
---

# Prompts de imágenes de la app (generación externa)

> [!resumen]
> Nueve imágenes para la app de RETO 30. Se generan fuera (Midjourney, Ideogram, Flux, GPT-Image, Firefly…) y se dejan en `~/Proyectos/reto-30/public/images/` con el nombre indicado. Mientras no existan, la app usa ilustraciones SVG propias en `src/components/brand/Art.tsx`, así que **nada se rompe si faltan**. Cuando las tengas, pásame los archivos y las integro.

Sustituye a la tabla de [[3 - UI-UX Design]] §5, que era corta. Reglas de marca: negro mate `#0C0D0E`, carbón `#181A1D` y `#262A30`, lima `#CCFF00`. **Sin personas reconocibles, sin caras, sin texto, sin logotipos, sin marcas de agua.**

## Bloque de estilo (pégalo al principio de TODOS los prompts)

```
Style: premium dark sports-brand graphic, flat vector look with sharp angular geometry and chamfered (cut) corners, matte black background #0C0D0E, charcoal greys #181A1D and #262A30, single accent color electric lime #CCFF00 (no other hues), subtle thin lime edge-lighting, slight film grain, high contrast, clean negative space, aspirational and energetic, minimal, no text, no letters, no numbers, no logos, no watermark, no faces, no recognizable people.
```

## Negativo (para los modelos que lo admiten)

```
text, letters, numbers, logo, watermark, signature, face, realistic person, photo, gradient rainbow, pink, blue, purple, orange, 3d render plastic, cartoon, clutter, busy background, blurry, low contrast
```

## 1. Fondo de portada y acceso · `hero-desktop.webp` y `hero-mobile.webp`

- **Medidas**: 1920×1080 (escritorio) y 1080×1920 (móvil), opacas, WebP de menos de 150 kB. **Dónde**: portada, entrar y alta; el centro debe quedar limpio.
- Midjourney: `--ar 16:9` (escritorio) o `--ar 9:16` (móvil) `--style raw --s 200 --no text letters numbers face`.

### Escritorio
```
Premium dark sports-brand poster background for a fitness challenge app. Matte black base (#0C0D0E), charcoal greys (#181A1D, #262A30) and a single accent color, electric lime (#CCFF00); no other hues. Centerpiece: a huge angular lime lightning bolt, outlined in a crisp 3 px lime line with a faint translucent lime fill, tilted about 12 degrees, flanked by a thinner parallel echo outline of the same bolt. Behind it, a very large angular shield outline in dark charcoal line with chamfered corners, only partly visible, as a watermark. Diagonal speed lines in lime of varying thickness and opacity (5 to 15 percent) slicing from the upper left to the lower right, ending in sharp points, giving a sense of explosive forward motion. A soft radial lime glow behind the bolt, fading to pure black toward the edges; subtle film grain; faint scanline texture. Along the bottom edge, a long horizontal progress bar made of exactly 30 rectangular blocks with small gaps: the first 9 solid glowing lime, the remaining 21 dark charcoal. Wide landscape composition: the bolt and glow occupy the right third; the left two thirds and the whole center stay dark and calm, with generous empty space for a logo and two buttons. Flat vector style with sharp geometry and chamfered corners, high contrast, cinematic, aspirational, minimal, premium gym aesthetic. No text, no letters, no numbers, no logo, no watermark, no people, no faces, no photo, no 3D plastic look.
```

### Móvil
```
Premium dark sports-brand poster background for a fitness challenge app. Matte black base (#0C0D0E), charcoal greys (#181A1D, #262A30) and a single accent color, electric lime (#CCFF00); no other hues. Centerpiece: a huge angular lime lightning bolt, outlined in a crisp 3 px lime line with a faint translucent lime fill, tilted about 12 degrees, flanked by a thinner parallel echo outline of the same bolt. Behind it, a very large angular shield outline in dark charcoal line with chamfered corners, only partly visible, as a watermark. Diagonal speed lines in lime of varying thickness and opacity (5 to 15 percent) slicing from the upper left to the lower right, ending in sharp points, giving a sense of explosive forward motion. A soft radial lime glow behind the bolt, fading to pure black toward the edges; subtle film grain; faint scanline texture. Along the bottom edge, a long horizontal progress bar made of exactly 30 rectangular blocks with small gaps: the first 9 solid glowing lime, the remaining 21 dark charcoal. Vertical portrait composition: the bolt in the upper right two thirds of the frame, partly cropped by the edge; the center and lower-middle stay dark and calm, with generous empty space for a logo and two buttons; the 30-block bar at the very bottom. Flat vector style with sharp geometry and chamfered corners, high contrast, cinematic, aspirational, minimal, premium gym aesthetic. No text, no letters, no numbers, no logo, no watermark, no people, no faces, no photo, no 3D plastic look.
```

## 2. Estado vacío del día 1 · `empty-day1.webp`
- **Medidas**: 1024×1024, fondo `#0C0D0E` sólido. **Dónde**: panel del participante antes de empezar.
- **Prompt**:
```
[bloque de estilo] Centered icon illustration. A single empty angular shield outline in dark charcoal grey with a thin lime top edge, inside it a ring of 30 empty segment slots, and one small solid lime lightning bolt at the center. Plenty of empty black space around. Calm, expectant mood. Square composition.
```

## 3. Felicitación al completar un día · `celebration.webp`
- **Medidas**: 1024×1024, fondo `#0C0D0E` sólido. **Dónde**: pantalla de felicitación tras completar el día.
- **Prompt**:
```
[bloque de estilo] Centered burst illustration. A bright lime green lightning bolt breaking through the middle of a cracked dark charcoal angular shield, short sharp lime rays radiating outward, tiny angular shards flying away, strong sense of victory and energy. Matte black background. Square composition, symmetrical.
```

## 4. Insignias (cuatro piezas) · `badge-7.webp`, `badge-14.webp`, `badge-21.webp`, `badge-28.webp`

- **Medidas**: 1024×1024. **Dónde**: pantalla de insignias, panel y diploma.
- **Colección**: mismo escudo, mismo grosor de línea y mismo ángulo en las cuatro; cambian solo el símbolo central, los bloques iluminados de abajo (1 a 4, una por semana) y el adorno del borde, que crece con cada hito.
- **Método para que salgan iguales**: genera primero la del día 7. Súbela como imagen de referencia (Midjourney `--sref`, GPT-Image o Flux con referencia) y pide las otras tres cambiando solo el símbolo, los bloques y el adorno.
- **Fondo transparente**: la mayoría de modelos no dan alfa real. Los prompts piden fondo blanco liso; recórtalas después (remove.bg o Photopea) y guarda en WebP con alfa. GPT-Image e Ideogram sí admiten transparente: cambia «isolated on a flat pure white background» por «transparent background».
- **Parámetros orientativos**: Midjourney `--ar 1:1 --style raw --s 150 --no text letters numbers face`. Flux: guidance 3,5 a 4.

### Día 7 · Resistencia
```
Heraldic sports achievement badge, front-on orthographic view, perfectly symmetrical, centered. Shape: an angular shield with a flat top edge, the two upper corners chamfered at 45 degrees, straight sides tapering to a sharp pointed bottom. Rim: thick polished dark gunmetal bevel (#2A2E35) with a crisp thin electric lime (#CCFF00) line running along the whole inner contour. Face: matte charcoal (#181A1D) with a fine diagonal brushed-metal grain and a faint lime rim-light coming from the upper left. Emblem: Three stacked horizontal zig-zag wave lines made of sharp angular segments, the top line longest and the bottom line shortest, conveying endurance. Solid lime (#CCFF00), embossed with a darker gunmetal edge, large and centered, about 45 percent of the shield height. Bottom of the face: a row of four small rectangular blocks, 1 of them solid lime and the rest dark charcoal. Tier: plain rim, no extra ornaments. Hard-edged flat vector look with a slight bevel and subtle inner shadow, sharp geometry, no soft curves, premium gym-brand collectible, high contrast, isolated on a flat pure white background, no ground shadow, no text, no letters, no numbers, no logo, no watermark, no faces.
```

### Día 14 · Fuerza
```
Heraldic sports achievement badge, front-on orthographic view, perfectly symmetrical, centered. Shape: an angular shield with a flat top edge, the two upper corners chamfered at 45 degrees, straight sides tapering to a sharp pointed bottom. Rim: thick polished dark gunmetal bevel (#2A2E35) with a crisp thin electric lime (#CCFF00) line running along the whole inner contour. Face: matte charcoal (#181A1D) with a fine diagonal brushed-metal grain and a faint lime rim-light coming from the upper left. Emblem: A side-view angular dumbbell: a straight bar with two stacked hexagonal weight plates at each end, perfectly horizontal, conveying strength. Solid lime (#CCFF00), embossed with a darker gunmetal edge, large and centered, about 45 percent of the shield height. Bottom of the face: a row of four small rectangular blocks, 2 of them solid lime and the rest dark charcoal. Tier: the rim gains four small lime studs, one on each upper corner and one on each lower side. Hard-edged flat vector look with a slight bevel and subtle inner shadow, sharp geometry, no soft curves, premium gym-brand collectible, high contrast, isolated on a flat pure white background, no ground shadow, no text, no letters, no numbers, no logo, no watermark, no faces.
```

### Día 21 · Constancia
```
Heraldic sports achievement badge, front-on orthographic view, perfectly symmetrical, centered. Shape: an angular shield with a flat top edge, the two upper corners chamfered at 45 degrees, straight sides tapering to a sharp pointed bottom. Rim: thick polished dark gunmetal bevel (#2A2E35) with a crisp thin electric lime (#CCFF00) line running along the whole inner contour. Face: matte charcoal (#181A1D) with a fine diagonal brushed-metal grain and a faint lime rim-light coming from the upper left. Emblem: A flame made of three sharp angular blades, a tall center blade and two shorter side blades, with a small dark diamond cutout at its core, conveying habit and consistency. Solid lime (#CCFF00), embossed with a darker gunmetal edge, large and centered, about 45 percent of the shield height. Bottom of the face: a row of four small rectangular blocks, 3 of them solid lime and the rest dark charcoal. Tier: the rim gains two short angular blade-wings extending sideways from the shield, in gunmetal with lime edges. Hard-edged flat vector look with a slight bevel and subtle inner shadow, sharp geometry, no soft curves, premium gym-brand collectible, high contrast, isolated on a flat pure white background, no ground shadow, no text, no letters, no numbers, no logo, no watermark, no faces.
```

### Día 28 · Gran reto final
```
Heraldic sports achievement badge, front-on orthographic view, perfectly symmetrical, centered. Shape: an angular shield with a flat top edge, the two upper corners chamfered at 45 degrees, straight sides tapering to a sharp pointed bottom. Rim: thick polished dark gunmetal bevel (#2A2E35) with a crisp thin electric lime (#CCFF00) line running along the whole inner contour. Face: matte charcoal (#181A1D) with a fine diagonal brushed-metal grain and a faint lime rim-light coming from the upper left. Emblem: An angular crown with five sharp spikes, the center spike tallest, on a flat base band with three small notches and a tiny lightning bolt cut out in the middle of the band, conveying the final challenge. Solid lime (#CCFF00), embossed with a darker gunmetal edge, large and centered, about 45 percent of the shield height. Bottom of the face: a row of four small rectangular blocks, 4 of them solid lime and the rest dark charcoal. Tier: full crest: the side blade-wings of the previous tier, a small angular peak above the top edge, and a faint lime glow behind the whole badge. Hard-edged flat vector look with a slight bevel and subtle inner shadow, sharp geometry, no soft curves, premium gym-brand collectible, high contrast, isolated on a flat pure white background, no ground shadow, no text, no letters, no numbers, no logo, no watermark, no faces.
```

### Negativo (todas)
```
text, letters, numbers, logo, watermark, signature, face, person, photo, realistic metal render, 3d plastic, cartoon, soft rounded shapes, extra colors (pink, blue, purple, orange, red), cluttered background, blurry, low contrast, drop shadow
```

## 5. Marco del diploma · `diploma-frame.webp`
- **Medidas**: 2480×1754 (A4 apaisado a 300 ppp), fondo `#0C0D0E`. **Dónde**: fondo de `/diploma` y de la versión para imprimir. El centro debe quedar vacío para poner el nombre.
- **Prompt**:
```
[bloque de estilo] Premium certificate frame, landscape A4. A thin double border in lime green with chamfered cut corners on matte black, small angular ornaments at the four corners, a subtle faint shield watermark in the exact center in very dark grey, and along the bottom edge a long bar made of 30 solid lime blocks. Large empty central area reserved for text. Elegant, ceremonial, minimal.
```

## 6. Vacíos de admin y gerencia · `empty-admin.webp`
- **Medidas**: 768×768, fondo `#0C0D0E`. **Dónde**: listas sin datos en administración y gerencia.
- **Prompt**:
```
[bloque de estilo] Minimal line icon illustration of an empty clipboard with a bold lime green check mark floating above it, dark grey outline, generous empty space, flat vector, square composition.
```

## 7. Comodín · `wildcard.webp`
- **Medidas**: 512×512, **fondo transparente**. **Dónde**: contador de comodines y aviso «se ha gastado un comodín».
- **Prompt**:
```
[bloque de estilo] Small angular dark charcoal shield with a bright lime green lightning bolt in the center and a thin lime top edge, flat vector, centered, transparent background, no text. Must stay readable at 48 px.
```

## 8. Ranking vacío · `empty-ranking.webp`
- **Medidas**: 1024×768, fondo `#0C0D0E`. **Dónde**: ranking cuando todavía no hay nadie.
- **Prompt**:
```
[bloque de estilo] Vector podium with three empty angular steps in dark charcoal grey, the tallest center step outlined with a thin lime line, a faint lime glow above the first place, no people, no trophies, no text. Centered, plenty of black space.
```

## 9. Pareja del plan Dúo · `duo.webp`
- **Medidas**: 1024×768, fondo `#0C0D0E`. **Dónde**: pestaña Pareja, antes de que se una la otra persona.
- **Prompt**:
```
[bloque de estilo] Two angular dark charcoal shields side by side, each with a thin lime edge, sharing a single large lime green lightning bolt placed between them that overlaps both, flat vector, symmetrical, no faces, no text. Centered with generous empty space.
```

## Revisión antes de entregar
- Sin texto ni letras en ninguna imagen (los modelos las inventan: si salen, regenera).
- Solo negro, carbón y lima. Si aparece otro color, regenera o corrígelo.
- Las transparentes (4, 7) deben tener alfa real: ábrelas sobre un fondo de otro color para comprobarlo.
- Peso: cada imagen por debajo de 150 kB (WebP, calidad 80). El presupuesto de JS de la app no cuenta imágenes, pero sí el tiempo de carga en móvil.
- Nombres exactos de la lista: así las integro sin cambiar nada más.

Ver también [[Prompts de imagenes - Cabeceras]]: cabeceras por tipo de ejercicio y por nivel.
