# GEMINI.md — global (optimizado 2026-11-22)

## 0. Reglas duras

1. **Ningún secreto real en el repo** → `~/.claude/reference/` chmod 600
2. **No destruir sin comprobar** → `git status` antes
3. **Aditivo; destructivo con permiso** → preguntar
4. **Avisar riesgos reales** → datos, credenciales, coste
5. **No duplicar** → probar si existe
6. **MCP/skill → primero** → mejor que Read/Grep si da resultado
7. **graphify** → solo para arquitectura/dependencias
8. **GateGuard inactivo** desde 2026-10-25
9. **Humano/máquina** → notas con `origen:` (regla `humano-maquina.md`)

## 1. Estilo

- **Español**, máximo 8 líneas. Conclusión → acción
- Sin emojis, sin resumen no pedido
- **Lenguaje sencillo siempre** → principio + conclusión + detalle

## 2. Routing esencial

| Necesito | Usar |
|---|---|
| API/ Librería | `context7` |
| Refactor/arquitectura | `sequential-thinking` o `/agent-debate` |
| Idea/nuevo proyecto | `buscador-oportunidades` → `nuevo-proyecto` |
| Producto/servicio | `oferta-central` (8 fases) |
| Validar idea | `before-you-build` + `project-idea-validator` |
| Archivo grande | `token-optimizer:quick` |
| GTM/cold email | Toggle GTM → sesión nueva |
| Proyecto lejano | MCP `zorin-ssh` |
| UI/componente | **Capa 0 primero**: `impeccable init` → luego: `design-taste-frontend` / `emil-design-eng` / `impeccable` |

## 3. Enlaces clave

- **Skills frecuentes**: `rules/skills-frecuentes.md`
- **Routing skills**: `reference/routing-skills-y-gtm.md`
- **Tokens**: `rules/tokens.md`
- **Plugins útiles**: `caveman`, `ponytail`, `token-optimizer`, `web-animation-skills`

## 4. Agentes del vault

`archivista`, `auditor-web`, `humanizador`, `ingeniero-inverso`, `investigador`, `neozeler-ceo`, `neozeler-cfo`, `neozeler-cmo`, `neozeler-cto`, `neozeler-coo`, `scraper`, `proyecto-idea-validator`

## 5. MCPs del vault

- `graphify` → knowledge graph
- `vault-search` → búsqueda semántica
- `mcp-dropshipping`, `mcp-marketing` → GTM
- `roblox-studio`, `supabase` → cuando los necesites

**Toggle MCPs**: `/mcp enable/disable <name>`