---
type: sesion
date: '2026-11-16'
proyecto: '[[01_Projects/MCP Diseno]]'
origen: maquina
sesion_id: 4925c572-29ab-4534-8b31-8132360f5632
tags:
  - sesion
  - cierre-automatico
---

> [!resumen] En cristiano
> Se llevó al USB portátil todo el harness nuevo y se comprobó, en un HOME temporal, que `usar.sh --sin-internet --perfil=3` instala el MCP `diseno` y el proyecto `mcp-diseno`. Funciona. Quedó sin probar que el MCP arranque de verdad ni abrir `claude` en ese HOME.

## Qué se hizo
- Actualización del USB (`Portable-NeoZeler`) con el harness completo.
- Simulación del perfil 3 («Claude solo, sin vault»): exit 0; el proyecto trae el binario `mcp-diseno` (ELF estático), `main.go`, `datos/catalogo.json`, README y `scripts/`; `.claude.json` apunta a `<HOME>/Proyectos/mcp-diseno/mcp-diseno` sin rutas `/home/haytham`; 16 MCP añadidos y verificación OK (claude, node, git, uv, rtk, hooks, statusline, token-optimizer, caveman, ponytail).

## Problemas y pendientes
- `cp -n` está obsoleto: cambiar a `--update=none` en `lib.sh`.
- No se arrancó `mcp-diseno` por MCP en el HOME simulado.
- El HOME temporal quedó en `/tmp/home-sim.TvYIvd`; un hook bloquea `rm -r`, se borra al reiniciar.

## Relacionado
- [[01_Projects/MCP Diseno]] · [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
