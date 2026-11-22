---
title: "Sesión - 2026-11-22 - OpenCode con configuracion de Claude Code"
date: 2026-11-22
type: meta/sesion
origen: mixto
proyecto: ""
tags:
  - sesion
  - opencode
  - configuracion
aliases: []
---

# Sesión — 2026-11-22: OpenCode con la configuración de Claude Code

> [!resumen] En cristiano
> Se ha montado OpenCode (otro programa de IA para programar) para que funcione exactamente como Claude Code: mismas reglas, mismos 13 agentes, mismos 20 enchufes de herramientas y los mismos vigilantes que bloquean secretos y comandos peligrosos. No se ha tocado nada de `~/.claude/`: OpenCode lee de ahí. Lo único que cambia es el modelo, que aquí se elige en cada sesión.

## Contexto

Haytham usa Claude Code a diario y quería el mismo entorno en OpenCode (versión 2.3.2, app de escritorio en Linux). La duda era si había que copiar todo o si OpenCode podía leer la configuración original.

## Qué se hizo

- Se comprobó que OpenCode ya lee `~/.claude/CLAUDE.md` (declarado en `instructions`), las skills de `~/.claude/skills/` (incluidas `synced/` y `skills-gtm` cuando se activan) y el `CLAUDE.md` del vault.
- Se creó `~/.config/opencode/opencode.jsonc`: permisos (secretos, `.env`, `node_modules`, `git push --force`, `terraform`), los 14 MCP globales, `formatter: true`, compactación automática y el plugin de hooks.
- Se creó `~/.config/opencode/AGENTS.md` como capa corta: solo lo que cambia respecto a Claude, sin duplicar el `CLAUDE.md`.
- Se tradujeron los 13 agentes a `~/.config/opencode/agents/*.md`: mismo cuerpo, `mode: subagent`, `tools` → `permissions`, sin `model`.
- Se creó el config del vault `~/Documentos/vault/.opencode/opencode.jsonc` con los 6 MCP portables (`{env:HOME}`), sin tocar `.mcp.json`.
- Se escribió el plugin `plugins/claude-hooks` que reconstruye el JSON de Claude y ejecuta los binarios Go de `~/.claude/bin/`.
- Verificado: 20 MCP conectados, 13 agentes cargados, `rm -rf` bloqueado y una clave de AWS fingida bloqueada al escribir.

## Decisiones tomadas

- **No copiar**: skills, reglas y `CLAUDE.md` se leen desde `~/.claude/` para no tener dos fuentes de verdad.
- **No fijar modelo**: no hay proveedor Anthropic conectado; los agentes heredan el modelo de la sesión.
- **Hooks como plugin**: así las reglas siguen viviendo solo en los binarios Go, no duplicadas.
- **`settings.json` viejo de `~/.config/opencode/`**: se deja intacto porque OpenCode no lo lee.

## Aprendizajes (para futuras sesiones)

- Los agentes Markdown de OpenCode necesitan YAML válido; un `description` largo con `:` sin comillas rompe el archivo y el log dice `agent file skipped ... reason=markdown`. Con `json.dumps` para entrecomillar, resuelto.
- OpenCode agrupa `edit`/`write`/`patch` en una sola acción: no se puede permitir escribir y prohibir editar en el mismo agente.
- El plugin corre en el servidor de OpenCode (Bun): `Bun.spawnSync` es la vía para llamar a binarios externos con stdin.
- `opencode mcp list` tarda unos segundos con `vault-search` (índice vectorial); hay que esperar antes de darlo por caído.

## Próximos pasos

- Usar OpenCode unos días y anotar lo que chirríe (hooks, permisos, agentes).
- Si se añade un agente o MCP nuevo en Claude, replicarlo a mano en `~/.config/opencode/`.
- Recordar `~/.claude/bin/informe-uso-skills 30` el 2026-12-04, ahora que hay dos programas usando las mismas skills.

## Relacionado

- [[03_Resources/OpenCode - Configuracion portada desde Claude Code]]
- [[03_Resources/Sistema Claude Code - Configuracion Completa]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
