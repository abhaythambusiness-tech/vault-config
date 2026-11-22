---
type: sesion
status: cerrada
date: '2026-10-28'
proyecto: '[[Ahorro de tokens en Claude Code]]'
origen: mixto
---

> [!resumen] En cristiano
> Se aplicó el informe de ahorro de tokens: se guardó como nota y sus reglas prácticas se añadieron a `~/.claude/rules/tokens.md` (limpiar entre tareas, no cambiar modelo a mitad, compactar con foco, instrucciones fijas cortas). La configuración ya estaba bien (sonnet + esfuerzo medio).

## Qué se hizo
- Nota fuente en `03_Resources/Ahorro de tokens en Claude Code.md` (copia; el original sigue en la raíz).
- Sección «Hábitos de ahorro» en `~/.claude/rules/tokens.md`; resumen replicado en los dos `GEMINI.md`.
- Medido: `CLAUDE.md` global 155 líneas (bien); el del vault pasó de 225 a 204 (duplicados de §3.3, §4.2 y §6 enviados a `tokens.md`; copia en `~/.claude/_backups/vault-CLAUDE-pre-recorte-20261028.md`).

## Aprendizajes
- Los archivos de instrucciones largos suben el coste y pueden bajar el acierto; solo lo que el agente no deduce del repo.
