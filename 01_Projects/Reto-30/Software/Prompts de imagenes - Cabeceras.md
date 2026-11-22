---
type: referencia
status: activo
date: 2026-10-19
tags: [reto-30, imagenes, prompts]
proyecto: Reto 30
origen: mixto
---

# Prompts de cabeceras: tipo de ejercicio y nivel

> [!resumen]
> Diez cabeceras panorámicas para dar vida a la pantalla del día (siete tipos de reto) y a la elección de nivel (tres). Mismo estilo que el corredor del fondo y las insignias de [[Prompts de imagenes - App]]. Se generan fuera y se guardan en `~/Proyectos/reto-30/public/images/`; cuando estén, pásame los archivos y las integro.

## Cómo generarlas
- **Formato**: 21:9 (por ejemplo 2016×864 o 1792×768). Exporta a WebP de 1600 px de ancho y menos de 90 kB cada una.
- **Composición**: todo el interés visual en el 40 % derecho; el resto, negro limpio donde irá el título. Los bordes se funden con `#0C0D0E`.
- **Coherencia**: genera primero «entrenamiento» y úsala como imagen de referencia de estilo (Midjourney `--sref`, GPT-Image o Flux con referencia) para las demás; cambia solo la línea de escena.
- **Midjourney**: `--ar 21:9 --style raw --s 150 --no text letters numbers face frame`.
- **Revisión**: sin texto ni letras, sin caras, solo negro, carbón y lima; si el sujeto invade la izquierda, regenera.

## Por tipo de ejercicio · `header-<tipo>.webp`
### Entrenamiento · `header-entrenamiento.webp`
```
Wide cinematic banner header for a premium sports-training app, 21:9 aspect ratio. Composition: all the visual interest sits in the RIGHT 40 percent of the frame; the LEFT 55 percent is calm, empty, near-black space reserved for overlaid text, fading smoothly into matte black (#0C0D0E) at the left, top and bottom edges so the image blends into the page with no visible border. Subject: A faceless angular silhouette in a deep goblet squat holding a dumbbell at the chest, seen from the side, made of sharp lime light strokes, with a large faint outline of an angular shield and a lightning bolt behind it. Style: flat vector with sharp angular geometry and chamfered cuts, built only from electric lime (#CCFF00) light strokes and blades on matte black (#0C0D0E) with dark charcoal (#181A1D, #262A30) secondary shapes, a soft lime glow behind the subject fading to black, faint diagonal speed lines, very subtle film grain, high contrast, energetic, aspirational, motivating. Mood: strong, powerful, focused. Faceless: any human is a pure silhouette made of geometric light strokes with no face, no skin, no clothing detail, no logo. No text, no letters, no numbers, no watermark, no frame, no border.
```

### Movilidad · `header-movilidad.webp`
```
Wide cinematic banner header for a premium sports-training app, 21:9 aspect ratio. Composition: all the visual interest sits in the RIGHT 40 percent of the frame; the LEFT 55 percent is calm, empty, near-black space reserved for overlaid text, fading smoothly into matte black (#0C0D0E) at the left, top and bottom edges so the image blends into the page with no visible border. Subject: A faceless angular silhouette in a deep lunge with both arms stretched overhead, long flowing curved lime arcs tracing the path of the stretch around the body, elegant and fluid despite the angular style. Style: flat vector with sharp angular geometry and chamfered cuts, built only from electric lime (#CCFF00) light strokes and blades on matte black (#0C0D0E) with dark charcoal (#181A1D, #262A30) secondary shapes, a soft lime glow behind the subject fading to black, faint diagonal speed lines, very subtle film grain, high contrast, energetic, aspirational, motivating. Mood: flowing, free, light. Faceless: any human is a pure silhouette made of geometric light strokes with no face, no skin, no clothing detail, no logo. No text, no letters, no numbers, no watermark, no frame, no border.
```

### Actividad física · `header-actividad.webp`
```
Wide cinematic banner header for a premium sports-training app, 21:9 aspect ratio. Composition: all the visual interest sits in the RIGHT 40 percent of the frame; the LEFT 55 percent is calm, empty, near-black space reserved for overlaid text, fading smoothly into matte black (#0C0D0E) at the left, top and bottom edges so the image blends into the page with no visible border. Subject: A faceless angular silhouette leaping in mid-air with arms raised and one knee up, caught at the peak of a jump, a few dust-like lime sparks below the feet, a thin horizon line near the bottom. Style: flat vector with sharp angular geometry and chamfered cuts, built only from electric lime (#CCFF00) light strokes and blades on matte black (#0C0D0E) with dark charcoal (#181A1D, #262A30) secondary shapes, a soft lime glow behind the subject fading to black, faint diagonal speed lines, very subtle film grain, high contrast, energetic, aspirational, motivating. Mood: explosive, joyful, dynamic. Faceless: any human is a pure silhouette made of geometric light strokes with no face, no skin, no clothing detail, no logo. No text, no letters, no numbers, no watermark, no frame, no border.
```

### Recuperación · `header-recuperacion.webp`
```
Wide cinematic banner header for a premium sports-training app, 21:9 aspect ratio. Composition: all the visual interest sits in the RIGHT 40 percent of the frame; the LEFT 55 percent is calm, empty, near-black space reserved for overlaid text, fading smoothly into matte black (#0C0D0E) at the left, top and bottom edges so the image blends into the page with no visible border. Subject: A faceless angular silhouette seated calmly in a cross-legged stretch with the torso leaning forward, surrounded by thin concentric lime rings like slow breathing waves, very gentle glow. Style: flat vector with sharp angular geometry and chamfered cuts, built only from electric lime (#CCFF00) light strokes and blades on matte black (#0C0D0E) with dark charcoal (#181A1D, #262A30) secondary shapes, a soft lime glow behind the subject fading to black, faint diagonal speed lines, very subtle film grain, high contrast, energetic, aspirational, motivating. Mood: calm, restorative, quiet. Lower the intensity: fewer speed lines, softer and dimmer lime glow. Faceless: any human is a pure silhouette made of geometric light strokes with no face, no skin, no clothing detail, no logo. No text, no letters, no numbers, no watermark, no frame, no border.
```

### Alimentación · `header-alimentacion.webp`
```
Wide cinematic banner header for a premium sports-training app, 21:9 aspect ratio. Composition: all the visual interest sits in the RIGHT 40 percent of the frame; the LEFT 55 percent is calm, empty, near-black space reserved for overlaid text, fading smoothly into matte black (#0C0D0E) at the left, top and bottom edges so the image blends into the page with no visible border. Subject: A top-down angular bowl filled with stylized geometric food shapes (leaf blades, round vegetable discs, an egg half) drawn as flat lime and charcoal polygons, with an angular fork and spoon beside it. Style: flat vector with sharp angular geometry and chamfered cuts, built only from electric lime (#CCFF00) light strokes and blades on matte black (#0C0D0E) with dark charcoal (#181A1D, #262A30) secondary shapes, a soft lime glow behind the subject fading to black, faint diagonal speed lines, very subtle film grain, high contrast, energetic, aspirational, motivating. Mood: fresh, healthy, appetizing. No realistic food, no photo. Faceless: any human is a pure silhouette made of geometric light strokes with no face, no skin, no clothing detail, no logo. No text, no letters, no numbers, no watermark, no frame, no border.
```

### Hidratación · `header-hidratacion.webp`
```
Wide cinematic banner header for a premium sports-training app, 21:9 aspect ratio. Composition: all the visual interest sits in the RIGHT 40 percent of the frame; the LEFT 55 percent is calm, empty, near-black space reserved for overlaid text, fading smoothly into matte black (#0C0D0E) at the left, top and bottom edges so the image blends into the page with no visible border. Subject: An angular sports water bottle standing upright, half full, with clean lime wave lines inside and a few sharp lime water drops flying around it, a faint circular ripple at its base. Style: flat vector with sharp angular geometry and chamfered cuts, built only from electric lime (#CCFF00) light strokes and blades on matte black (#0C0D0E) with dark charcoal (#181A1D, #262A30) secondary shapes, a soft lime glow behind the subject fading to black, faint diagonal speed lines, very subtle film grain, high contrast, energetic, aspirational, motivating. Mood: fresh, clean, energizing. Faceless: any human is a pure silhouette made of geometric light strokes with no face, no skin, no clothing detail, no logo. No text, no letters, no numbers, no watermark, no frame, no border.
```

### Reto especial · `header-especial.webp`
```
Wide cinematic banner header for a premium sports-training app, 21:9 aspect ratio. Composition: all the visual interest sits in the RIGHT 40 percent of the frame; the LEFT 55 percent is calm, empty, near-black space reserved for overlaid text, fading smoothly into matte black (#0C0D0E) at the left, top and bottom edges so the image blends into the page with no visible border. Subject: A huge angular lightning bolt splitting a cracked charcoal shield, radiating sharp lime rays and falling shards, a small angular crown hovering above the bolt, grand and celebratory. Style: flat vector with sharp angular geometry and chamfered cuts, built only from electric lime (#CCFF00) light strokes and blades on matte black (#0C0D0E) with dark charcoal (#181A1D, #262A30) secondary shapes, a soft lime glow behind the subject fading to black, faint diagonal speed lines, very subtle film grain, high contrast, energetic, aspirational, motivating. Mood: epic, victorious, rare. Stronger glow and more rays than the other banners. Faceless: any human is a pure silhouette made of geometric light strokes with no face, no skin, no clothing detail, no logo. No text, no letters, no numbers, no watermark, no frame, no border.
```

## Por nivel · `level-<nivel>.webp`
Enfoque 3 (2026-10-19): misma silueta de trazos lima que el banner del corredor (úsalo como imagen de referencia), una sola figura y un brillo. El nivel se nota en la postura y la intensidad: caminar, correr, esprintar.

### Básico · `level-basico.webp`
```
Wide banner for a sports app, 21:9 aspect ratio, in the exact same style as the reference image: a single faceless athlete silhouette built from sharp angular lime (#CCFF00) light strokes and blades on matte black (#0C0D0E), with a soft lime glow behind it and a faint thin outline of an angular shield in the background. The athlete is placed in the right third of the frame; the rest is clean empty black, fading to black at the edges with no visible border. Pose: a relaxed brisk walk, upright posture, one arm swinging gently, calm steady stride. Few strokes, very little speed lines, soft low glow. Mood: easy, friendly, just starting. Flat vector, high contrast, very subtle film grain, no face, no skin, no text, no letters, no numbers, no logo, no watermark, no frame.
```

### Medio · `level-medio.webp`
```
Wide banner for a sports app, 21:9 aspect ratio, in the exact same style as the reference image: a single faceless athlete silhouette built from sharp angular lime (#CCFF00) light strokes and blades on matte black (#0C0D0E), with a soft lime glow behind it and a faint thin outline of an angular shield in the background. The athlete is placed in the right third of the frame; the rest is clean empty black, fading to black at the edges with no visible border. Pose: a steady rhythmic run, torso leaning slightly forward, arms bent and driving. A few speed lines behind it, medium glow. Mood: focused, in the flow, getting stronger. Flat vector, high contrast, very subtle film grain, no face, no skin, no text, no letters, no numbers, no logo, no watermark, no frame.
```

### Avanzado · `level-avanzado.webp`
```
Wide banner for a sports app, 21:9 aspect ratio, in the exact same style as the reference image: a single faceless athlete silhouette built from sharp angular lime (#CCFF00) light strokes and blades on matte black (#0C0D0E), with a soft lime glow behind it and a faint thin outline of an angular shield in the background. The athlete is placed in the right third of the frame; the rest is clean empty black, fading to black at the edges with no visible border. Pose: an explosive sprint, body leaning far forward, one knee driving high, arms powerful. Dense sharp strokes with small shards trailing behind, long speed lines, strong bright glow. Mood: intense, fast, elite. Flat vector, high contrast, very subtle film grain, no face, no skin, no text, no letters, no numbers, no logo, no watermark, no frame.
```

## Negativo (todas)
```
text, letters, numbers, logo, watermark, signature, frame, border, face, realistic person, photo, realistic food, 3d render, cartoon, soft rounded shapes, extra colors (pink, blue, purple, orange, red), cluttered background, busy centered subject, blurry, low contrast
```
