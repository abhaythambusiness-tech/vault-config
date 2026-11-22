---
date: '2026-10-22'
type: sesion
proyecto: '[[01_Projects/Laya Leads]]'
tags:
- scraping
- laya
- neozeler
origen: mixto
---

> [!resumen] En cristiano
> Construimos en el servidor un programa que lista negocios de Málaga con web, saca su correo y puntúa si la web se puede modernizar. Probamos a que Laya clasificara y no pasó la prueba, así que se usan reglas. Salieron 866 webs leídas, 602 con correo y 98 candidatas a modernizar.

## Qué se hizo
- Referencias pasadas por Haytham (jevrake, jev-scrape-lab, jev-ultrafast, JevBrowser, awesome-jev): son de Jev; aportaron el patrón de preguntas tipadas con umbral de confianza.
- Lista de empresas desde OpenStreetMap (Overpass): 2.265 elementos con web, 1.010 válidos tras filtrar.
- Rastreo educado (robots.txt, 1 s, User-Agent propio), extracción y puntuación por reglas. Proyecto `~/Proyectos/laya-leads/` (git local, commit `9d3ed44`).
- Prueba de Laya con criterio fijado antes de medir: NO PASA (ver ficha).

## Aprendizajes
- **Regla de Haytham**: si enseña material de Jev, se interpreta que se usa Laya (memoria `feedback-jev-es-laya`).
- Overpass: sin User-Agent responde 406; el servidor principal se satura (502); el espejo `overpass.kumi.systems` respondió en ~1,5 min.
- `selectolax` ya no trae el motor antiguo: usar `selectolax.lexbor`.
- Con 10 empresas Laya parecía fallar en todo; con 100 acertó el sector (66 %) pero no la web anticuada. Medir con muestras grandes antes de concluir.
- Laya tarda 3-7 s por empresa en la CPU del servidor y su checkpoint avisa de confianza no calibrada.
- Lanzar tandas largas con `(nohup … &)`; `read-command` rechaza `;`, pipes y paréntesis.

