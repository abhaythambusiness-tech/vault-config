---
title: "Sesión - 2026-11-09 - NeoFlow pitch según PDF, mapa de España y auditoría"
date: 2026-11-09
type: meta/sesion
origen: mixto
proyecto: "[[01_Projects/NeoFlow AI]]"
sesion_id: 9b5beccf-770e-42d3-86ba-c5bd41c857d6
tags:
  - sesion
  - neoflow
  - pitch
  - diseno
aliases: []
---

# Sesión — 2026-11-09: NeoFlow pitch según PDF, mapa de España y auditoría

> [!resumen] En cristiano
> Haytham pasó un PDF con cambios para la presentación de NeoFlow AI y pidió aplicarlos con el mismo diseño. La primera versión no le gustó: tenía que seguir el orden del PDF y llevar un mapa de España de verdad. Quedó en 14 diapositivas con mapa real, se revisó accesibilidad y velocidad en móvil, tablet y ordenador, y se subió el cambio a git.

## Contexto
Landing de pitch de `[[01_Projects/NeoFlow AI]]` (repo `~/Proyectos/neoflow-pitch/`), hecha el 2026-11-05 para Impulsa Startup. Entrada: `~/Descargas/Copia de Documento sin título.pdf`. Se invocó `diseno-central` antes de tocar la UI.

## Qué se hizo
- **Primera pasada:** 16 diapositivas nuevas (problema «agenda vacía», propuesta de valor, modelo de negocio, competencia, equipo, roadmap 2026). Haytham la rechazó: no seguía el PDF y faltaba el mapa.
- **Segunda pasada:** el pitch pasó a **14 diapositivas** siguiendo el orden del PDF (portada, problema con 5 causas, solución, propuesta de valor, mercado, modelo, diferenciación, equipo, roadmap, cierre).
- **Mapa real de España** con provincias, Canarias en recuadro y Málaga resaltada («906») con pulso animado; debajo «España: 22.771».
- Se quitaron la calculadora y las sinergias, que no estaban en el PDF (siguen en el historial de git).
- **Auditoría** a 375/768/1280 px: axe sin violaciones en las 14 diapositivas; Lighthouse accesibilidad, buenas prácticas y SEO a 100. Rendimiento: 87 (375), 79 (768), 99 (1280).
- Arreglos: contraste del mensaje del chat y de la ficha del lead, diapositivas con scroll enfocables por teclado, fuentes sin bloquear el render, diapositivas fuera de pantalla sin pintar, sin desenfoque ni partículas por debajo de 1100 px.
- Commit `da12dd7` en `neoflow-pitch` (README.md, app.js, index.html, style.css) y push a petición de Haytham.

## Decisiones tomadas
- El PDF manda sobre el diseño anterior: se priorizó su orden y se eliminó lo que no estaba.
- El roadmap se queda con las tres fases genéricas (piloto, Málaga, escala) hasta que Haytham dé hitos y fechas reales.

## Aprendizajes
- Aplicar «los cambios de un PDF» no es añadir diapositivas: la primera pasada falló por no respetar el orden ni pedir el mapa literal.
- Lighthouse se ejecutó una vez por ancho, sin mediana.

## Problemas y pendientes
- Rendimiento en tablet (79) por debajo de 90: queda trabajo del fondo animado en el hilo principal.
- Los PDF `NeoFlow-AI-Pitch.pdf` y `NeoFlow-AI-Dossier.pdf` se citan en la sesión sin confirmar que se regeneraran con las 14 diapositivas: comprobar.
- Datos de demo inventados siguen por sustituir (ficha del proyecto).

## Relacionado
- [[01_Projects/NeoFlow AI]] · [[01_Projects/NeoFlow AI - Guion del Pitch]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
