---
type: sesion
date: 2026-11-17
proyecto: "[[01_Projects/MCP Compartido]]"
origen: mixto
---

> [!resumen] En cristiano
> Se creó un MCP en Go que deja a dos Claude Code compartir una carpeta de notas. La copia entre equipos la hace Syncthing con Zorin en medio. Falta emparejar los equipos y registrar el MCP.

## Aprendizajes
- Zorin ya tenía Syncthing instalado pero parado, y Tailscale Funnel activo: un futuro modo HTTP del MCP nunca debe colgar de Funnel.
- Syncthing resuelve la sincronización; el valor del MCP es escribir sin pisar (`hash_base`) y avisar de cambios y conflictos.
- Un registro de cambios por autor evita que Syncthing genere conflictos en el propio registro.
- `guard-destructive` bloquea `rm -r` fuera de `/tmp`: en pruebas usar el scratchpad.
