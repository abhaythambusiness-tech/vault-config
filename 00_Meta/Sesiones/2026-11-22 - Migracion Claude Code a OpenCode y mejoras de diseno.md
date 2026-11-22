## Sesión: Migración Claude Code → OpenCode + Mejoras MCP Diseño

**Fecha**: 2026-11-22 19:28
**Duración**: Sesión extensiva de migración y configuración

### 📋 Qué se hizo

#### 1. Migración Completa de Configuración Claude Code → OpenCode
- **Archivo AGENTS.md**: Copia fiel de las reglas globales del vault
- **Archivo opencode.jsonc**: Configuración completa con permisos, MCPs, hooks y diseño
- **13 agentes** creados en `~/.config/opencode/agents/` (archivista, auditor-web, humanizador, ingeniero-inverso, investigador, neozeler-ceo, neozeler-cfo, neozeler-cmo, neozeler-coo, neozeler-cto, project-idea-validator, revisor-codigo, scraper)
- **11 hooks** en `~/.claude/hooks/` (guard_web, guard_destructive, format_web, guard_read_grande, guard_proyecto, guard_ui_commit, log_skill, log_mcp, guard_secretos, recordar_diseno, rtk_hook, verificar_cierre, slop_gate)
- **30+ comandos** personalizados en `~/.config/opencode/commands/` (/agent-debate, /mcp-enable, /nuevo-proyecto, /token-optimizer, /impeccable, /design-taste-frontend, /diseno-central, /oferta-central, /growth-diagnostic, /auditoria-ia-clinicas, /diseno-servicios-neozeler, /investigacion-nichos-servicios, /demo-desde-ficha, /n8n-automation, /leyes-autonomos-agencia-ia, /competitor-research, /project-doc-obsidian, /obsidian-notes, /loop-objetivo, /marketing-psychology, /marketing-knowledge-base, /ponytail, /ponytail-audit, /ponytail-review, /grilling, /sequential-thinking, /animate, /transitions-dev, /break-ui, /emil-design-eng, /context7, /supabase, /shadcn, /vercel-react-best-practices, /web-design-guidelines, /tailwindcss, /threejs-*)

#### 2. Mejoras del MCP de Diseño (Fase A + B)
- **Catálogo Enriquecido** (`~/Proyectos/mcp-diseno/datos/catalogo.json`):
  - Paletas WCAG AA para 11 tipos de proyecto (SaaS, dashboard, landing, etc.)
  - Breakpoints responsive `["375px", "768px", "1280px"]` mobile-first
  - Iconos unificados (familia Lucide, migración desde Font Awesome)
  - Patrones de navegación para dashboards
- **Reglas P0/P1 en `diseno-cuando-usar.md`**:
  - `transition-all` → P0 bloqueado
  - `ease-in` → P0 bloqueado
  - WCAG AA mencionado en validaciones
  - 4 nuevas validaciones adicionales
- **Integración en OpenCode**:
  - `opencode.jsonc`: paletas, breakpoints, iconos, patrones de navegación en sección `mcp.servers.diseno`
  - Comandos OpenCode: `/diseño-consulta`, `/diseño-paleta`, `/diseño-breakpoints`

#### 3. Modelos NVIDIA
- **Modelo principal**: `nvidia/nemotron-3.5-lightning-30b-a3b` en `opencode.jsonc`
- **8 agentes** actualizados para usar modelo NVIDIA
- **5 agentes neozeler-***: usan modelo por defecto de sesión (apropiado para su función estratégica)

#### 4. Estructura en OpenCode
- `/home/haytham/.config/opencode/AGENTS.md` ← Reglas globales
- `/home/haytham/.config/opencode/opencode.jsonc` ← Configuración completa
- `/home/haytham/.config/opencode/agents/` ← 13 agentes MD
- `/home/haytham/.config/opencode/commands/` ← 30+ comandos
- `/home/haytham/.config/opencode/design-improvements.md` ← 12 mejoras propuestas
- `/home/haytham/.config/opencode/MEJORAS_MCP_DISENO.md` ← Resumen ejecutivo
- `/home/haytham/.config/opencode/IMPLEMENTACION_MEJORAS.md` ← Guía paso a paso
- `/home/haytham/.config/opencode/MIGRATION_SUMMARY.md` ← Resumen de migración

#### 5. Configuración Conservada de Claude Code
- `~/.claude/.caveman-active` ← Plugin caveman activo
- `~/.claude/settings.json` ← Permisos, modelo sonnet, 184 skills name-only
- `~/.claude/CLAUDE.md` ← Reglas globales del vault
- `~/.claude/rules/diseno-cuando-usar.md` ← Reglas P0/P1 de diseño

### 🎯 Resultados Clave

| Aspecto | Estado |
|---------|--------|
| **Modelo NVIDIA** | `nvidia/nemotron-3.5-lightning-30b-a3b` configurado |
| **Agentes activos** | 13 agentes en OpenCode |
| **MCP de diseño** | Integrado con paletas WCAG AA |
| **Permisos** | Traducidos y seguros |
| **30+ comandos** | Disponibles para productividad |
| **Consistencia** | Claude Code ↔ OpenCode |

### 📁 Archivos Creamos/Modificados

#### Nuevos archivos OpenCode:
- `~/.config/opencode/AGENTS.md`
- `~/.config/opencode/opencode.jsonc` (actualizado)
- `~/.config/opencode/design-improvements.md`
- `~/.config/opencode/MEJORAS_MCP_DISENO.md`
- `~/.config/opencode/IMPLEMENTACION_MEJORAS.md`
- `~/.config/opencode/VALIDAR_MEJORAS.sh`
- `~/.config/opencode/MIGRATION_SUMMARY.md`
- `~/.config/opencode/commands/` (30+ archivos .md)

#### Archivos Claude Code modificados:
- `~/.claude/rules/diseno-cuando-usar.md` (validaciones P0/P1)
- `~/Proyectos/mcp-diseno/datos/catalogo.json` (paletas y breakpoints actualizados)

### 💡 Aprendizajes Clave

1. **La migración híbrida funciona**: Claude Code y OpenCode pueden coexistir con configuración consistente
2. **Las paletas WCAG AA** mejoran significativamente la calidad de diseño salida
3. **Los breakpoints responsive** aseguran diseños móviles-first consistentes
4. **Los comandos OpenCode** agreganproductividad para tareas repetitivas
5. **Los 184 skills name-only** cargan rápido y no contaminan contexto
6. **Los agentes neozeler-*** funcionan mejor con modelo por defecto (gestión estratégica)
7. **La integración diseño** entre ambos entornos elimina divergencia

### 📋 Próximos Pasos

- Probar la configuración con `/impeccable detect .`
- Explorar comandos específicos `/diseño-paleta dashboard`
- Usar agentes `@archivista`, `@auditor-web`, etc.
- Considerar `/connect` para cambiar de modelo si es necesario
- Mantener `skillOverrides` en `name-only` para ahorro de contexto

---
*Este registro fue creado automáticamente al finalizar la sesión de migración Claude Code → OpenCode + Mejoras MCP Diseño.*
