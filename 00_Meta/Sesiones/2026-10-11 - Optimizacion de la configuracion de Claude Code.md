---
type: sesion
date: '2026-10-11'
proyecto: '[[CLAUDE]]'
tags:
- sesion
- claude-code
- configuracion
- tokens
- skills
origen: mixto
---


# Sesión — 2026-10-11: Optimización de la configuración de Claude Code

> [!abstract] Resumen
> Se midió el uso real de skills, agentes y plugins, y con esos datos se redujo el contexto fijo de ~86 KB a ~15 KB de CLAUDE.md, se movieron 314 skills GTM a un perfil on/off y se desactivaron 34 plugins y 7 agentes sin uso.

## Contexto
Haytham quería recortar skills y agentes que no usa y partir un CLAUDE.md demasiado largo (global 40 KB + vault 46 KB, con mucho contenido duplicado) en archivos metódicos. Toca `~/.claude/` (global) y [[CLAUDE]] del vault. Borrador completo en `docs/borrador-config/`.

## Qué se hizo
- Auditoría de uso sobre 188 transcripts (`~/.claude/projects/*/*.jsonl`): 27 skills distintas usadas de ~900, `general-purpose` 212 invocaciones de agente, ningún agente propio usado.
- Copia de seguridad en `~/.claude/backups/2026-10-11-optimizacion/` (CLAUDE.md global, del vault y `settings.json`).
- 314 skills (`gtm-`, `coldiq-`, `coldout-`, `aimc-`, `aimcs-`) movidas a `~/.claude/skills-gtm/` con `toggle.sh on|off|status`.
- CLAUDE.md global 40 KB → 7,7 KB y del vault 46 KB → 7,1 KB; el resto vive en `~/.claude/rules/` (`diseno`, `stack-web`, `dashboards-saas`, `tokens`, `librerias`, `agentes-frecuentes`, `skills-frecuentes`).
- 33 plugins desactivados en `settings.json` (71 → 38 activos con el duplicado de `token-optimizer`); 7 agentes propios archivados en `~/.claude/agents-archivo/` (queda `project-idea-validator`).

## Decisiones tomadas
- Desactivar plugins (`false`), no desinstalar ni borrar: es reversible y se reactivan por proyecto.
- Skills GTM como perfil apagado por defecto en vez de borrarlas: son la base de NeoZeler aunque apenas aparezcan en los transcripts.
- La tabla de routing de diseño (Canva, Bloom, Figma, shadcn) se queda en el CLAUDE.md global, siempre cargada.
- `token-optimizer`: se conserva la v5.11.81 (`alexgreensh-token-optimizer`) y se desactiva la v5.4.3.
- Se conserva `project-idea-validator` porque el CLAUDE.md lo exige como paso previo a construir.

## Aprendizajes (para futuras sesiones)
- Una regla con `paths:` solo se carga al tocar archivos que coincidan; las peticiones de diseño que no tocan archivos ("hazme un banner") no la activarían. Por eso el routing de diseño no puede vivir solo en `rules/diseno.md`.
- Las descripciones de las skills cuestan contexto en cada turno aunque no se usen: apagar plugins enteros rinde más que editar el CLAUDE.md.
- `ecc` se mantiene activo porque trae el hook GateGuard, aunque sus agentes casi no se usen.
- GateGuard deniega la primera escritura de cada archivo nuevo, también en el fallback de `Write`: declarar y reintentar.
- Los cambios de plugins, skills y rules solo se ven en una sesión nueva.

## Próximos pasos
- Abrir sesión nueva y ejecutar `/memory` y `/context`: confirmar que `rules/` se carga a nivel de usuario (sin verificar con `paths:`) y medir el ahorro real.
- Si el MCP de `token-optimizer` sigue sin conectar (`CONNECTION_CLOSED`), ejecutar `install_doctor`.
- Revisar y commitear `.claude/COMMON_MISTAKES.md` y `CLAUDE.md` del vault, que quedan modificados sin commit.
- Repetir la auditoría de uso en unas semanas y retirar lo que siga a 0.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[CLAUDE]]

