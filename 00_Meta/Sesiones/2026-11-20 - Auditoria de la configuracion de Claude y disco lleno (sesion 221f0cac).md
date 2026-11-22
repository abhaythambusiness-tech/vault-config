---
title: Auditoría de la configuración de Claude y disco lleno
date: '2026-11-20'
type: meta/sesion
origen: maquina
proyecto: ''
sesion_id: 221f0cac-092f-4f3a-8f14-527456393cb0
tags:
- sesion
- configuracion
- mcp
- disco
---

> [!resumen] En cristiano
> Se auditó `~/.claude`. Al principio el disco estaba al 100 % y 11 MCP (enchufes a herramientas) no arrancaban. Tras limpiar caché, se aplicaron 5 arreglos más uno extra y se quitaron MCP duplicados.

## Qué se hizo
- Disco: limpiados `~/.npm` y `~/.cache`; quedaron ~118 GB libres. Lo que más pesa es Steam (89 GB, CS2 69 GB); decisión de desinstalar, de Haytham.
- Copia previa en `~/.claude/_backups/auditoria-20261120/`.
- Arreglos: caveman de `ultracave` a `caveman`; `rea` desactivado del todo (config guardada en `_disabledMcpServers`); `diseno-central` descrito solo como referencia; 4 hooks de edición agrupados en un bloque; `CLAUDE.md` resumido y al día.
- `npx` corrupto en `~/.npm/_npx` (`ENOTEMPTY`) rompía `memory`, `sequential-thinking`, `shadcn-ui`; el `.mcp.json` del vault los lanzaba con Node 18 → se les antepuso Node 22 (el USB sigue valiendo).
- MCP duplicados quitados entre `~/.claude.json` y `.mcp.json` del vault: global = context7, sequential-thinking, memory, obsidian-vault; vault = graphify, vault-search, mcp-dropshipping, mcp-marketing, roblox-studio, supabase.

## Aprendizajes
- Con el disco lleno, no tocar `settings.json`: puede quedar cortado.
- Una sesión abierta antes de los arreglos sigue viendo los MCP caídos; reiniciar.

## Pendientes
- Opcional: desinstalar CS2 desde Steam.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

