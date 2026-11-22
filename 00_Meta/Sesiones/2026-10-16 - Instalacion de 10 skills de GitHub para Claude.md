---
type: sesion
date: '2026-10-16'
tags:
- skills
- claude-code
- herramientas
proyecto: Vault
origen: mixto
---

## Contexto
Haytham pasó una captura de aiagently con «10 repos de GitHub para Claude» y pidió instalarlos y documentarlos.

## Qué se hizo
- Instaladas globalmente (`npx skills add <repo> -g -y -a claude-code`, Node 22): `hallmark`, `impeccable`, `diagram-design`, `humanizer`, `last30days`, `scrapling-official`, `reverse-engineer-anything`, `ponytail` + `-review`, `-audit`, `-debt`, `-gain`, `-help`.
- `ui-ux-pro-max` ya estaba. No instaladas: Onyx (es un chat autoalojado, no una skill) y 3 skills internas del repo de REA (mantenimiento del repo).
- Documentado qué hace cada una, cuándo y cómo en `~/.claude/rules/skills-frecuentes.md`, con routing resumido en el `CLAUDE.md` global y del vault y en los tres `GEMINI.md`.

## Aprendizajes
- Las URLs de una captura pueden estar mal leídas: `moruto/rea` era en realidad `morluto/rea` y `nutope/hallmark` era `Nutlope/hallmark`. Verificar con `gh repo view` antes de dar un repo por inexistente.
- `reverse-engineer-anything` solo trae instrucciones: necesita registrar el MCP `rea-agents` (con aprobación de Haytham).
- `scrapling-official` necesita `venv` + `pip install "scrapling[all]"`; `last30days` necesita Python 3.12+ y su asistente guarda claves en `~/.config/last30days/.env`.
- `ponytail` no sustituye la regla de código completo y tipado del global §3.
- Varias solapan con skills previas (`pulse`, `content-humanizer`, `universal-scraping-architect`, `artifact-diagramming`); se dejan conviviendo.

## Cierre
- Scrapling: venv en `~/.local/share/scrapling-venv` (0.4.15), probado con fetch normal y `StealthyFetcher`. Sin librerías de sistema de Chromium (`playwright install-deps` pide `sudo`).
- REA: MCP `rea` registrado solo en Claude Code (copia `~/.claude.json.rea.backup`); `doctor` healthy. Motores Hopper/Ghidra/IDA/JADX sin instalar (opcionales). Requiere sesión nueva.

