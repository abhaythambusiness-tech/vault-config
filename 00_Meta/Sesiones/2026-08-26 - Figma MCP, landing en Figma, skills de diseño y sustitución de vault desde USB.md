---
title: Sesión - 2026-08-26 - Figma MCP, landing en Figma, skills de diseño y sustitución
  de vault desde USB
date: '2026-08-26'
type: meta/sesion
proyecto: 02_Areas/NeoZeler
tags:
- sesion
aliases: []
origen: mixto
---


# Sesión — 2026-08-26: Figma MCP, landing en Figma, skills de diseño y sustitución de vault desde USB

> [!abstract] Resumen
> Se autenticó y usó el MCP de Figma para construir una landing de ejemplo, se instalaron/inventariaron skills de diseño (motion-design-skills, taste, genjutsu), se limpió una instalación duplicada de una skill dentro del vault, y se sustituyó el contenido del vault por una copia del USB tras detectar y confirmar explícitamente que revertía un pivote estratégico de nichos de NeoZeler.

## Contexto
Sesión de mantenimiento de entorno + trabajo de diseño. Toca `[[02_Areas/NeoZeler/NeoZeler - MOC|NeoZeler - MOC]]` (nichos/servicios) y la configuración global de Claude Code (`~/.claude/`).

## Qué se hizo
- Autenticado el conector `claude.ai Figma` (MCP) vía `/mcp`.
- Confirmado que `vault-search` ya estaba correctamente configurado en `.mcp.json` (nada que hacer).
- Construida una landing "Sistema Completo de Finanzas Personales" completa en un archivo Figma nuevo (Hero + Features 3-col + Closing CTA), usando `use_figma` con auto-layout, sin design system previo (archivo en blanco).
- Instalada la marketplace + plugin `iart-ai/motion-design-skills` (9 skills de motion design).
- Clonado `rohitg00/awesome-claude-design` a `~/Proyectos/` como referencia (no es un plugin instalable, son prompts DESIGN.md).
- Detectada y corregida una instalación duplicada: `npx skills add ... web-design-guidelines` instaló la skill dentro del propio vault (`.agents/`, `.claude/skills/` symlink, `skills-lock.json`), que el auto-sync ya había commiteado/pusheado antes de poder moverla. Se borró, commiteó y pusheó la limpieza.
- Sustituido el contenido de Obsidian del vault actual por la copia `Haytham-Vault-main` del USB (`NeoUSB`), excluyendo toda config de Claude Code (`.claude/`, `.mcp.json`, `CLAUDE.md`, `docs/`, `.token-optimizer/`, `.git/`). Commit `a699276`.
- Creada la nota `[[03_Resources/Web Interface Guidelines]]` (checklist de UI/UX pedida por el usuario).

## Decisiones tomadas
- La copia del USB (`Haytham-Vault-main`) **sustituye** al vault actual pese a ser una versión anterior a un pivote estratégico reciente de NeoZeler (menos nichos: se perdieron Transporte y logística, Talleres y garajes, Instalación de placas solares, Barberías y peluquerías, y sus demos/fichas asociadas). Confirmado explícitamente dos veces por el usuario tras advertir la pérdida.
- La skill `web-design-guidelines` vive solo en `~/.claude/skills/` (global), no dentro del vault — evitar reinstalarla vía `npx skills add` sin el flag/ruta que apunte fuera del repo.

## Aprendizajes (para futuras sesiones)
> Solo lo no obvio: por qué se eligió X y no Y, qué falló y por qué, qué convención quedó fijada.
- El auto-sync del vault (cron "Auto-sync: ...") puede commitear y pushear cambios **entre turnos de la conversación**, antes de que dé tiempo a limpiar un error propio (pasó con la skill duplicada). Antes de "mover" algo mal colocado en el vault, asumir que puede que ya esté en el remoto y verificar `git log` en vez de solo `git status`.
- `npx skills add <repo> --skill <nombre>` no comprueba si la skill ya existe globalmente en `~/.claude/skills/` — puede duplicarla dentro del directorio de trabajo actual (aquí, el vault con auto-push). Comparar antes con `diff` contra `~/.claude/skills/<nombre>` en vez de asumir que es nueva.
- Al pedir "instala X skill" con nombres coloquiales ("awesome design", "motion design", "design dna"), no todos existen como marketplace instalable — algunas son colecciones de prompts (`DESIGN.md`) para copiar/pegar, no plugins. Verificar con `WebSearch` + inspección del `.claude-plugin/marketplace.json` antes de instalar a ciegas.
- Antes de una sustitución masiva de contenido (vault desde USB), un `rsync -avn --delete` (dry-run) con `--exclude` explícito de rutas de config es el patrón seguro: muestra exactamente qué se borraría sin tocar nada, y permite detectar que una "copia nueva" en realidad era un snapshot de Syncthing más antiguo que el vault activo (mismo `.stfolder`/`.sync`, mismas notas, fecha de mod. anterior).
- Cuando el usuario insiste tras una advertencia de pérdida de datos real, seguir insistiendo con más preguntas es contraproducente — una confirmación explícita y directa (no vía `AskUserQuestion`) tras dos advertencias claras es suficiente para proceder, siempre que el estado previo esté limpio en git (recuperable).
- Figma MCP: `create_new_file` requiere resolver `planKey` vía `whoami` primero; en un archivo en blanco sin design system, el workflow de `figma-generate-design` se reduce a construir manualmente con `figma-use` (auto-layout, sin `search_design_system`) — los pasos de descubrimiento de componentes son N/A cuando no hay librería.
- `figma.createAutoLayout()` sin fills explícito puede heredar un fondo blanco por defecto que tapa contenido hermano (bug sutil, solo visible en `screenshot()`, no en el código).

## Próximos pasos
- Decidir si se completa el "gate de diseño §4.1" que la nota `Web Interface Guidelines` referencia — no existe todavía en `CLAUDE.md` (queda pendiente, no se tocó sin permiso explícito).
- Revisar si `00_Meta/Scripts/vault-sync.sh` (borrado por la sustitución del USB) hacía falta o ya estaba obsoleto.
- Pendiente de siempre: decidir qué hacer con `taller-bravo/` (archivar / documentar / eliminar).

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[03_Resources/Web Interface Guidelines]]
- [[02_Areas/NeoZeler/NeoZeler - MOC|NeoZeler - MOC]]

