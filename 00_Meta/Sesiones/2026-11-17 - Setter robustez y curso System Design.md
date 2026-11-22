---
title: Sesión - 2026-11-17 - Setter robustez y curso System Design
date: '2026-11-17'
type: meta/sesion
origen: mixto
proyecto: '[[Setter NeoZeler]]'
tags:
- sesion
---

# Sesión — 2026-11-17: Setter robustez y curso System Design

> [!resumen] En cristiano
> Se estudió el curso System Design y se aplicó al Setter: copia inactiva en n8n que no contesta dos veces, no se cuelga si OpenAI falla y no pierde mensajes. Se probó el camino normal y el fallo. TopLeads y NeoZeler HQ pasaron a archivo. Las reglas quedaron en el harness.

## Qué se hizo
- Nota `[[Curso System Design - Apuntes y aplicacion a NeoZeler]]` en `03_Resources` (§9 aplica al Setter, ARM y proyectos archivados).
- TopLeads y NeoZeler HQ movidos a `04_Archive/` con enlaces corregidos; `graphify update` y reindexado de `vault-search`.
- Setter: 5 puntos del curso contra el repo; copia `Setter (robustez)` (`4g1UmbgpLYpZC9IE`, inactiva) con dedupe, timeouts, reintentos y rama de fallo.
- Pruebas: ejecución 38540 (normal) y 38543 (OpenAI roto: `procesado` 1 → 0, `AvisoFallo`).
- `resumen.html` y ficha `[[Setter NeoZeler]]` actualizados; regla global `~/.claude/rules/sistemas-resiliencia.md` indexada en `CLAUDE.md` (Gemini sincronizado).

## Decisiones tomadas
- No mover `MarcarProcesado` al final (evita doble respuesta); se reabre solo si falla el agente.
- Copia sobre el Setter vivo, no import del JSON del repo (iba por detrás).

## Aprendizajes
- n8n: reintentos fijos (2-5, espera ≤5 s), `staticData` solo en producción; el reintento del subnodo OpenAI no actuó dentro del agente (sin confirmar).
- `test_workflow` pinnea credenciales/HTTP; las tablas de datos escriben de verdad.

## Pendiente
- Decidir sustitución del Setter vivo; borrar filas de prueba `34000000001` y `34000000002`.
