---
title: "Sesión - 2026-11-11 - NeoFlow pitch: cambios del PDF"
date: 2026-11-11
type: meta/sesion
origen: maquina
proyecto: "[[01_Projects/NeoFlow AI]]"
sesion_id:
  - c06cd566-b095-4afa-a538-0abb71c35b7d
tags:
  - sesion
  - neoflow
  - cierre-automatico
aliases: []
---

# Sesión — 2026-11-11: NeoFlow pitch, cambios del PDF

> [!resumen] En cristiano
> Se aplicaron a la presentación NeoFlow los cambios de un PDF de Haytham: nueva portada, agenda vacía con iconos en vez de emojis, una diapositiva de datos con cifras y fuentes, y propuesta de valor. El cierre pasó a decir «Cada cliente, atendido.». Quedó subido a GitHub (commit `bf9edc3`). No se pasaron axe ni Lighthouse.

## Contexto
Proyecto [[01_Projects/NeoFlow AI]] (repo `~/Proyectos/neoflow-pitch/`), landing de 10 diapositivas para Impulsa Startup. El PDF `~/Descargas/cambios diapositivas.pdf` traía los cambios.

## Qué se hizo
- `index.html` y `style.css`: portada «Ningún cliente sin respuesta.» con la píldora «ficha por cliente»; agenda vacía con título «Hay demanda y sin respuesta = agenda vacía», 5 tarjetas con los textos del PDF y el dato del 79 % (Invoca, *Healthcare Broken Funnel Report 2026*); emojis sustituidos por iconos SVG.
- Diapositiva «fuera de horario» sustituida por dos tarjetas: 48,5 % (Foundever) y 17,8 % (SAS / Europa Press). El PDF no daba título, así que se puso uno propio.
- Cierre: «Cada lead, atendido.» → «Cada cliente, atendido.» (`index.html:283`).
- Revisado en navegador a 800 y 1280 px; commit `bf9edc3` subido a `origin/main`. Se dejaron fuera los PDFs y `pdf/`, que siguen sin seguimiento.

## Decisiones tomadas
- El texto de cara al cliente usa «cliente» y no «lead».

## Problemas abiertos
- Sin axe, Lighthouse ni scripts de revisión de diseño.
- El cambio de «cliente» en el cierre no se miró en el navegador.
- Las cifras del PDF vienen de terceros: conviene verificar las fuentes antes de presentarlas.
- Siguen sin sustituir los datos de demo inventados de la ficha del proyecto.

## Próximos pasos
- Pasar axe y Lighthouse a 375 y 1280 px; revisar la diapositiva de cierre; verificar las tres cifras y sus fuentes.

## Relacionado
- [[01_Projects/NeoFlow AI]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
