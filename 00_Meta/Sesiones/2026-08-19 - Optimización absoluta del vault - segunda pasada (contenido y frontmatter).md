---
title: Sesión - 2026-08-19 - Optimización absoluta del vault, segunda pasada (contenido
  y frontmatter)
date: '2026-08-19'
type: meta/sesion
proyecto: '[[02_Areas/NeoZeler/NeoZeler - MOC|NeoZeler]]'
tags:
- sesion
- mantenimiento
aliases: []
origen: mixto
---

> [!abstract] Resumen
> Segunda pasada de la "optimización absoluta del vault" (continúa [[00_Meta/Sesiones/2026-08-19 - Optimización absoluta del vault (enlaces, frontmatter, huérfanas)|la auditoría inicial]]): se escribió el contenido que faltaba (9 fichas de servicio + 2 notas de estrategia, cerrando ~11 enlaces rotos) y se estandarizó el frontmatter de las 10 notas del vault que no tenían.

## Qué se hizo

**Contenido nuevo:**
- Diseño-servicios-neozeler — metodología de diseño de servicios de NeoZeler.
- NeoZeler - Competencia — mapa razonado de 5 tipos de competidor (sin cifras de mercado inventadas, marcado explícitamente como hipótesis a validar).
- 9 fichas de servicio en `Servicios/Fichas/Instalación y mantenimiento/` y `Servicios/Fichas/Distribución industrial/`, construidas a partir de las filas correspondientes de NeoZeler - Modelo de Precios.

**Frontmatter estandarizado (10 notas):**
- `2026-08-08_landscape.md` y `plan.md` en `Investigaciones/claude-code-ecosystem-2026/`: ya tenían frontmatter pero con claves en español no convencionales (`tipo`, `fecha`, `estado`) — renombradas a `type`/`date`/`status` (convención del resto del vault), conservando `tema`/`fecha_inicio` como campos adicionales.
- 6 notas sin frontmatter en absoluto (`refresh_targets.md` + 4 de `sources/`, el duplicado archivado de transcripciones, y la compilación de 32 transcripciones de Dropshipping): se les añadió `type: investigacion` o `type: fuente-cruda` (tipo nuevo, no existía en el vault — para dumps de fuente cruda no editorializados, distinto de `type: nota`), `date`, `status`.

## Hallazgo importante — no resuelto, pendiente de decisión

Al enlazar las 9 fichas nuevas desde NeoZeler - MOC de Servicios se descubrió que ese mismo documento declara, en una nota de 2026-08-07, que los nichos **"Instalación y Mantenimiento"** y **"Distribución Industrial"** quedaron retirados, sustituidos por Nicho - Talleres y garajes e Nicho - Instalación de placas solares. Pero NeoZeler - Modelo de Precios (fechado 2026-08-05, antes de ese reseteo) sigue listando 9 servicios bajo esos dos nichos retirados — que son precisamente los que esta sesión ha escrito. Se ha documentado la inconsistencia con una advertencia explícita en el MOC de Servicios, **sin decidir la reconciliación** (¿remapear a los nichos vigentes o revivir los nichos retirados?) — es una decisión de estrategia de negocio, no de higiene de datos.

## Decisiones tomadas
- No se inventaron cifras de mercado en la nota de Competencia — se marcó explícitamente como mapa razonado, no estudio de mercado.
- `type: fuente-cruda` se creó como tipo nuevo (no existía) para no forzar `type: nota` sobre dumps de fuente sin editorializar — más honesto que fingir que son notas de síntesis.
- No se tocó el contenido real de la compilación de 32 transcripciones (25k+ tokens) — solo se le antepuso el frontmatter vía edición de texto, sin releer/reescribir el cuerpo completo.

## Aprendizajes (para futuras sesiones)
- `list_notes` reporta `type: null` tanto para notas sin frontmatter como para notas cuyo frontmatter usa una clave distinta a `type` (ej. `tipo`) — no asumir que "sin type" significa "sin frontmatter" sin leer el archivo primero.
- Antes de enlazar contenido nuevo desde un MOC, leer el MOC completo primero: contenía una decisión estratégica (reseteo de nichos) que cambiaba el contexto de la tarea a mitad de ejecución.

## Relacionado
- [[00_Meta/Sesiones/2026-08-19 - Optimización absoluta del vault (enlaces, frontmatter, huérfanas)]]
- [[00_Meta/Registro de Sesiones]]
- NeoZeler - MOC de Servicios
- NeoZeler - Modelo de Precios

