---
title: "Sesión - 2026-11-04 - Skills de YouTube, limpieza de skills y MCPs"
date: 2026-11-04
type: meta/sesion
origen: mixto
proyecto: ""
sesion_id:
  - 4dce9f31-d5a3-4ad0-8300-700c3496f44d
  - 178671e5-e6c4-4f1b-981d-bfe51323cf31
tags:
  - sesion
  - skills
  - configuracion
aliases: []
---

# Sesión — 2026-11-04: skills de vídeos, limpieza global y MCPs

> [!resumen] En cristiano
> Haytham pasó varios vídeos de YouTube sobre diseño con IA y pidió instalar las skills que mencionan. Resultó que ya estaban instaladas. De ahí salió una limpieza grande: de 255 skills activas se pasó a 149 y cada una quedó con su «cuándo usarla» en las reglas. Después se aplicó el consejo de simplificar la configuración y se hizo lo mismo con los MCP. No se borró nada; todo se puede recuperar.

`4dce9f31` es la primera mitad de la misma conversación (se interrumpió al revisar 331 skills descargadas); `178671e5` la continúa tras agotar el contexto.

## Qué se hizo
- Vídeos vistos con `/watch`: «Llevo 947 días usando IA en Diseño UX/UI» (Antonio Díaz Cueto), otros cinco sobre diseño con IA y «Insane Claude Design Skills» (AI LABS).
- Las 7 colecciones del vídeo (Emil Kowalski, garden-skills, elayadesign, MengTo, jakubkrehel, tastemaker, Owl-Listener) ya estaban en `~/.claude/skills/`, idénticas a GitHub: no se instaló ni sobrescribió nada.
- Limpieza por secciones: quedan 76 skills de diseño, una por sección (253 archivadas). Luego limpieza global: 255 → 149 activas, perfil GTM 314 → 214.
- Reglas: `~/.claude/rules/skills-diseno-seleccion.md` (76) y `skills-seleccion-global.md` (73 + 214 GTM), cada skill con su línea «cuándo usarla». `CLAUDE.md` global, del vault y los dos `GEMINI.md` actualizados.
- Tras una opinión «objetiva» de la configuración: plugins sin uso desactivados, reglas «graphify» y «skills primero» pasadas a «solo si ayuda», una única fuente de verdad (los `GEMINI.md` se generan con `sync-gemini.py`).
- MCPs: `doory` y `shopify-storefront` desactivados (a `_disabledMcpServers`), `rules/mcps-seleccion.md` con cada MCP y su «cuándo», hook `log-mcp.py` que mide su uso; informe de uso fijado para el 2026-12-04.

## Decisiones
- Filtro de limpieza: pasa si encaja con el trabajo real (NeoZeler, vault, web/UI, Supabase/Next, n8n, trading, scraping, marketing), no la cubre otra mejor y no es de otro mundo.
- Archivar con `mv`, nunca borrar. Recuperar: `mv ~/.claude/skills-archivo/<nombre> ~/.claude/skills/`.
- Los MCP duplicados entre usuario y `.mcp.json` del vault se dejan así, para que el USB siga funcionando.

## Problemas
- Al listar la configuración se vio en pantalla el token del MCP `doory`. Se sacó de `settings.json` (se sube al repo) a `~/.claude/reference/mcp-desactivados-secretos.json` con `chmod 600`. No se copia aquí. **Conviene rotarlo** si ese servidor importa.
- El vídeo de AI LABS no tenía subtítulos en inglés; la lectura se hizo con subtítulos automáticos y descripción.

## Archivos afectados
`~/.claude/CLAUDE.md`, `~/.claude/rules/` (cuatro archivos), `~/.claude/settings.json`, `~/.claude/hooks/log-mcp.py`, `~/Documentos/vault/CLAUDE.md`, `00_Meta/GEMINI.md`, copias en `~/.claude/_backups/plugins-20261104/`.

## Mejoras propuestas
- Revisar el informe de uso del 2026-12-04 y archivar lo que siga sin usarse.
- Quitar a mano en los ajustes de claude.ai los conectores de cuenta que no se usan (la herramienta no puede).

## Pendientes
- Nada de esto estaba commiteado al terminar.
- Si algo falla tras la limpieza, restaurar desde `_backups/plugins-20261104/`.

## Relacionado
- [[2026-11-04 - Rediseno del sistema de UI (diseno-central)]] · [[2026-11-04 - Auditoría de Token Optimizer y hooks de ahorro (sesiones a3965f27 y 31764197)]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
