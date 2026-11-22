---
title: "Sesión - 2026-11-05 - NeoFlow AI pitch, guion, PDF y USB"
date: 2026-11-05
type: meta/sesion
origen: mixto
proyecto: "[[01_Projects/NeoFlow AI]]"
sesion_id:
  - 16f03686-5efe-4c1a-87e1-97bbd49d378a
  - 5ad4f7b1-e4a0-452d-9301-da0420261887
  - 1b5ae289-2616-409c-9ec8-c8e2df5a4a00
tags:
  - sesion
  - neoflow
aliases: []
---

# Sesión — 2026-11-05: NeoFlow AI, de la landing al dossier

> [!resumen] En cristiano
> Tres sesiones encadenadas (cada una continúa la anterior porque se agotó el contexto). Se hizo la presentación de NeoFlow AI para Impulsa Startup: una web de diapositivas que se recorre como un lienzo grande, su guion para decir en voz alta, una carpeta para llevar en USB y un PDF. Mañana se presenta la idea con el PDF; la demo con la presentación llegará otro día.

Complementa a [[2026-11-05 - Landing pitch NeoFlow AI]] (que cubre solo el arreglo del fondo SVG). Ficha: [[01_Projects/NeoFlow AI]]. Guion: [[01_Projects/NeoFlow AI - Guion del Pitch]].

## Qué se hizo
- **Landing de 10 diapositivas** en `~/Proyectos/neoflow-pitch/`, a partir de PDFs de pitch de referencia que pasó Haytham. Verificada a 320, 375, 768 y 1280 px. Axe: 0 violaciones. Lighthouse móvil: rendimiento 87, accesibilidad 100, buenas prácticas 96, SEO 100.
- **Más impacto**: letras grandes, diapositivas más llenas y fondo SVG animado (rejilla de puntos, brillos, flujos hacia un nodo central, anillos y partículas). Al principio no se veía: el `body` tenía fondo propio y lo tapaba.
- **Navegación tipo lienzo**: en vez de bajar siempre, la cámara se mueve en horizontal, vertical y diagonal con zoom-out a mitad de viaje.
- **Diapositiva nueva (la 2)**, pedida por Haytham: «Escriben de noche. Nadie contesta.» Una barra de 24 horas con horario de ejemplo 9–20 h y dos datos de un informe sobre embudos sanitarios (25 % y 79 %). La landing pasó a 11 diapositivas.
- **Guion del pitch** en el vault (unos 6 minutos), con aviso de qué datos son de ejemplo. Se quitó la palabra «Gracias» del cierre; ahora cierra con «Cada lead, atendido.».
- **Carpeta portable** para USB con LÉEME y tipografías en local (funciona sin internet).
- **PDF**: primero de 11 páginas parecido a la presentación; Haytham pidió que no se pareciera tanto. Versión final `NeoFlow-AI-Dossier.pdf` (6 páginas, solo la idea, sin demo), copiada al USB y a `99_Assets/Documentos/`.
- **Git**: commit en el repo del pitch, repo **privado** en GitHub `abhaythambusiness-tech/neoflow-pitch` (datos de demo inventados) y commit del vault `6172a46`.

## Decisiones tomadas
- El PDF sirve para presentar la **idea**; la landing se reserva para la **demo**.
- Repo privado hasta sustituir los datos inventados.

## Aprendizajes
- Vercel bloqueó el despliegue automático porque los commits llevaban el email `southway665@gmail.com`, no asociado a la cuenta de GitHub. Se arregló con el email correcto; el repo no tenía identidad git y se fijó solo en local.
- Fondo solo en `html`; un `body` con fondo tapa hijos `position:fixed` con `z-index:-1`.

## Problemas
- El commit del vault `6172a46` entró con 745 archivos y borrados de notas (INGECONS, Clínica Marbella Estética y otras). Conviene revisar que fuera intencionado.

## Próximos pasos
- Sustituir los datos de demo inventados por reales.
- Commit pendiente del cambio de `index.html` (quitar «Gracias») y de la diapositiva 2, si no se hizo ya.
- Revisar el contraste y `aria-prohibited-attr` que axe dejó como «incomplete».

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
