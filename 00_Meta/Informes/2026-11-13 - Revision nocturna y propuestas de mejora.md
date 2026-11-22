---
type: informe
status: pendiente-revision
origen: maquina
date: '2026-11-13'
---

# Revisión nocturna 2026-11-13

> [!resumen] En cristiano
> La raíz del vault ya estaba limpia (0 archivos movidos). Hay 9 hallazgos del harness (la «caja de herramientas» de Claude Code, nº 35-43), con 3 puntos ciegos: el vault no se sube a GitHub desde hace 30 h, el registro de uso de skills solo cubre 9 días y las plantillas crean enlaces rotos. Además 9 propuestas de mejora (44-52) y 5 apuestas atrevidas (53-57). Te toca marcar por número cuáles se aplican. Las fuentes de internet salieron flojas: tómalas como pistas, no como hechos.

## 2. Raíz ordenada

Sin movimientos esta noche. En la raíz solo están los archivos permitidos (CLAUDE.md, GEMINI.md, .mcp.json, .gitignore, .claudeignore, .graphifyignore, .diagram-design y carpetas PARA/sistema). Los 4 `.glb` y la carpeta de código `ssh@192.168.0.100mp-crm-test` se movieron anoche (ver [[2026-11-12 - Revision nocturna y propuestas de mejora]]); en `git status` salen como borrados de la raíz porque aún no hay commit. Nada se dejó sin mover.

## 3. Estado del vault

Datos de `vault-salud` (610 notas): 41 enlaces rotos y 48 huérfanas. [[Salud del vault]].

| Prioridad | Ruta | Problema | Acción propuesta | Riesgo |
|---|---|---|---|---|
| Alta | `00_Meta/Plantillas/Plantilla - Cliente / Proyecto / Servicio IA / Caso de Éxito` | Enlazan a MOCs que no existen («NeoZeler - MOC de Clientes», «MOC de Nichos», «MOC de Servicios», «Plantillas de Cold Email por Nicho», «Sistema de Contenido LinkedIn»). Cada nota nueva hereda enlaces rotos | Repuntar a los MOC reales o quitar la línea | Bajo |
| Media | `00_Meta/Sesiones/2026-08-19…` y `2026-08-25…` | ~30 enlaces rotos a notas de agosto que ya no existen | Dejar (histórico humano); excluir de `vault-salud` | Ninguno |
| Media | `CLAUDE.md` del vault §1 y §7 | Sigue listando `Neozeler CRM` como vigente; la memoria dice «CRM: ninguno vigente» (2026-11-12). Última actualización escrita: 2026-10-22 | Decidir y corregir (nota humana: lo hace Haytham) | Datos viejos en cada sesión |
| Baja | 48 huérfanas | Sin enlace entrante | Índice aditivo (ya propuesto, nº 20) | Bajo |

No medido esta noche: duplicados, notas largas, sesiones sin enlazar a su proyecto, estados viejos de proyectos (la tabla auto de estados existe en `00_Meta/Estado de Proyectos (auto).md`).

## 3B. Auditoría del harness

| nº | Tipo | Hallazgo y evidencia | Impacto | Esfuerzo | Recomendación |
|---|---|---|---|---|---|
| 35 | punto ciego | El vault no se sube a GitHub: último commit 2026-11-11 22:32 (hace 30 h), 92 entradas sin commitear, ningún proceso de sincronización activo (`pgrep`). El CLAUDE.md dice «auto-push» | Riesgo: perder 2 días de trabajo si falla el disco (82 % usado, 84 GB libres) | S | Revisar si el auto-push murió; hook/script Go que avise si pasan >24 h sin commit |
| 36 | punto ciego | `~/.claude/uso-skills/uso.jsonl` tiene 40 líneas y empieza el 2026-11-04 (9 días, no 30). Incluye una entrada de prueba (`test`). El informe «46 de 49 skills sin uso» es poco fiable | Evita archivar skills útiles | S | Esperar al 2026-12-04 (poda ya prevista) y comprobar que `log-skill` registra siempre |
| 37 | recorte | Arranque: `~/.claude/CLAUDE.md` 10,5 KB + `CLAUDE.md` del vault 27,7 KB + MEMORY 1,7 KB ≈ 40 KB (~10 000 tokens por sesión). El del vault trae listas largas de proyectos (§1) y §0.8-0.10 | ~4 000 tokens por sesión (estimado, sin medir) | M | Pasar §1 (lista de proyectos) y detalle de §0.8-0.10 a `reference/` o a `Estado de Proyectos`, dejar enlace |
| 38 | recorte | `enabledPlugins`: 9 activos de 121 instalados; la lista de skills inyectada trae cientos ajenas (`small-business`, `sales`, `finance`, `fastly`, `buildkite`, `qt`, `searchfit`). Además ~60 MCPs pendientes de autorizar | Tokens de arranque: sin medir | S | Desactivar por perfil los plugins sin uso; `token-optimizer:quick` para cifrar |
| 39 | automatización | `bash-commands.log` 2,7 MB, `cost-tracker.log` 2,8 MB, `projects/` 1,5 GB (`cleanupPeriodDays` ya a 180) | Espacio y lecturas lentas | S | Rotar los dos logs (script Go) |
| 40 | punto ciego | Las copias de `~/.claude` son manuales (70 entradas en `_backups/`, ninguna automática). `reference/` guarda `.env` con `chmod 600` (correcto) | Perder reglas/hooks/skills | M | Backup semanal cifrado a Zorin (Go) |
| 41 | regla | Plantillas con enlaces rotos (ver sección 3) | Enlaces rotos nuevos cada nota | S | Corregir plantillas |
| 42 | regla | Contradicción CRM entre `CLAUDE.md` del vault y la memoria | Agentes con datos viejos | S | Decisión de Haytham |
| 43 | hook | `settings.json` tiene 0 reglas `allow` y 19 `deny`: puede generar avisos repetidos | Tiempo; sin medir | S | Ejecutar `fewer-permission-prompts` sobre transcripciones |

Ya bien (no tocar): `check-hooks` 17 casos OK, `sync-gemini --check` al día, hook Stop, `CLAUDE_CODE_SUBAGENT_EFFORT` y `cleanupPeriodDays` ya aplicados desde anoche; ambas tareas programadas corrieron esta noche (01:02 y 03:07).

**Ahorro de tokens estimado:** ~4 000 tokens/sesión por el nº 37 más una cifra sin medir por el nº 38.
**Candidatos a script/hook (Go):** aviso de vault sin commit >24 h (35), rotar logs (39), backup semanal de `~/.claude` (40), validador de `log-skill` (36).
Propuestas 36, 38, 43 tocan settings/hooks/plugins: no las puede aplicar esta tarea.

## 4. Propuestas de mejora (series continua; ayer llegó al 34)

| nº | Área | Propuesta | Beneficio | Coste/riesgo | Fuente | Recomendación |
|---|---|---|---|---|---|---|
| 44 | Skills | Pocas skills: con ~20 parecidas Claude elige mal, con 12 acierta; hoy hay 49 | Menos errores y tokens | Archivar mal | [LangChain](https://langchain.com/blog/evaluating-skills) (sin fecha) | Probar tras la poda del 2026-12-04 |
| 45 | Skills | Evals con skill-creator (con y sin skill) | Decidir con datos | Evals mal hechas | [Anthropic](https://claude.com/resources/articles/improving-skill-creator-test-measure-and-refine-agent-skills), 2026-03-03 | Probar |
| 46 | Tareas nocturnas | `claude -p` con `--allowedTools` explícito y fallo si sale distinto de 0 | Tareas más seguras | Sin verificar cómo corre hoy la tarea | [MindStudio](https://mindstudio.ai/blog/claude-code-headless-mode-autonomous-agents) (sin fecha) | Probar |
| 47 | Tareas | Routines en la nube (antes /schedule) | No depende del PC | No ven el vault local ni Zorin; plan sin comprobar | [MindStudio](https://www.mindstudio.ai/blog/claude-code-routines-scheduled-cloud-tasks) | Descartar para el vault; guardar |
| 48 | Plugins | Marketplace oficial (315 plugins, act. 2026-10-27): mirar solo lo que no tengamos | Radar | Instalar a ciegas | [claudemarketplaces](https://claudemarketplaces.com/plugins/anthropics-claude-plugins-official) | Guardar |
| 49 | Servicios | Gestorías (leer facturas, conciliar) y talleres (presupuestos, avisos de revisión) como nichos nuevos | Nichos no atacados | Demanda sin confirmar (fuente: blog comercial) | [Upliora](https://www.upliora.es/blog/ia-por-sectores-empresas-espana-guia-gremios-2026) | Probar con 3 conversaciones |
| 50 | Servicios | Rescate de leads dormidos (reactivar contactos viejos del cliente) | Servicio corto, se enseña con sus datos | Sin fuente propia | CEO | Probar |
| 51 | Captación | Alianza por comisión con gestores/asesores locales | Canal casi gratis | Sin dato de mercado | CEO | Aplicar |
| 52 | Diseño | Tipografía enorme, fuentes variables, movimiento con función, 3D solo en portada; Spline y Unicorn Studio a probar; contratendencia «no parecer hecho por IA» | Refuerza la regla de identidad | Fuentes: blogs de vendedores | [Lovable](https://lovable.dev/es/guides/website-design-trends-2026), [Elementor](https://elementor.com/blog/web-design-trends-to-expect-in-2026/) | Aplicar lo ya compatible; Spline/Unicorn: probar |

## 4B. Apuestas atrevidas

| nº | Idea | Por qué es atrevida | Experimento ≤1 día | Riesgo y reversión | Coste | Apuesta |
|---|---|---|---|---|---|---|
| 53 | Cada noche Zorin prueba cada skill con 3 casos y propone archivar las que fallan | Hoy ninguna skill tiene test | skill-creator, evals de 3 skills (diseno-central y 2 sin uso), con y sin skill | Evals mal escritas dan falsos «inútil»; solo informe, borrar carpeta | ~2-5 € (sin medir) | 2 · Probar en sandbox |
| 54 | Claude Code manda tareas largas a Zorin con `claude -p` y recoge el resultado de mañana | El agente trabaja solo de noche | Resumir logs en una carpeta vacía de Zorin, solo lectura, límite de turnos | Permisos amplios tocan datos reales; usuario sin escritura fuera de la carpeta, copia previa, nunca saltarse permisos | ~1-3 €/noche (sin medir) | 4 · Probar en sandbox |
| 55 | Demo hecha por IA para cada prospecto (lee su web y monta una mini-demo con su marca) antes de escribir | Se regala trabajo antes de que respondan; ya existe `demo-desde-ficha` | 10 demos para 10 clínicas dentales de Málaga con n8n + Laya Leads; probar con demo y sin demo | Puede parecer spam; no enviar sin permiso de Haytham (LSSI/RGPD); parar y no seguir | Pocos € + tiempo | 3 · Probar en sandbox |
| 56 | Vender Laya Leads como informe mensual («negocios de Málaga sin web/reservas/WhatsApp») a freelancers y agencias web | Convierte la herramienta interna en ingreso sin construir TopLeads | Informe de 30 leads, enseñarlo a 5 freelancers y preguntar precio | Datos personales y correos en frío; consultar al gestor; retirar el informe | Solo tiempo | 2 · Guardar hasta paso legal |
| 57 | Un agente nocturno escribe lecciones (errores que reaparecen) y otro las lee y abre un borrador de cambio, tipo «mejora de sí mismo» | Memoria que se cura sola sin que Haytham mire | Sobre una copia de `.claude/COMMON_MISTAKES.md` en Zorin, 1 ciclo | 24 agentes siguieron haciendo commits tras la orden de parar en un relato; exige tope de coste, archivos prohibidos e interruptor | Sin medir | 3 · Guardar |

Precedente para 57: [Addy Osmani](https://addyosmani.com/blog/self-improving-agents/) (sin fecha); para 55: [Ciela](https://ciela.ai/blogs/reverse-demo-method-ai-agencies) (2025-11-06), cifras de vendedor, no fiables. Ninguna apuesta repite las de informes anteriores.

## 5. Novedades de internet

- Plugin Ralph Wiggum (repite una tarea hasta pasar tests; bucles nocturnos): [blog](https://thebiggish.pages.dev/news/ralph-wiggum-autonomous-coding-loops-overnight-development-costs-12-delivers-47-commits), sin fecha. A probar con cuidado.
- `claude-overnight` (agentes en paralelo con worktrees): [Socket](https://socket.dev/npm/package/claude-overnight). Sin reseñas; a probar.
- Memoria: `consolidation-memory` ([PyPI](https://pypi.org/project/consolidation-memory/0.9.0/)) y Myelin, Apache-2.0 ([2026-03-12](https://shsolomo.github.io/ai/agents/2026/03/12/Myelin-Brain-Inspired-Knowledge-Graph-For-AI-Agent-Memory.html)). LedgerMind: licencia no comercial, no aplicable.
- `--safe-mode` (CC 2.1.169, junio): arranca sin plugins ni hooks; útil para depurar.
- Adopción de IA en pymes españolas, cifras muy dispares (4,1 % a 31 %): [Emprendedores](https://emprendedores.es/gestion/holded-informe-emprende-2026/), [Ecosistema Startup](https://ecosistemastartup.com/pymes-espanolas-el-41-usa-ia-el-doble-que-en-2024/).

## 6. Lo que NO se hizo / límites

- Los agentes hicieron 3-6 búsquedas cada uno, sin abrir páginas; casi todo son blogs de vendedores sin fecha. No hay novedades fechadas de noviembre 2026.
- No hubo ronda de reto CEO↔CTO (los dos corrieron en paralelo, no se cruzaron). No se lanzaron CMO ni CFO.
- Un hand-back del CTO disparó el filtro de «instrucciones» por mencionar `--dangerously-skip-permissions`; era una advertencia («nunca»), sin acción.
- No medidos: duplicados, notas largas, sesiones sin enlazar, versión más reciente de Claude Code, `settings.local.json`, tokens reales de arranque (cifras estimadas).
- No se tocó settings, hooks, skills, MCP ni plugins; sin commit.

## 7. Siguiente paso

Haytham marca por nº qué se aplica. Tocan settings/hooks/plugins (sesión aparte con permiso): 36, 38, 43, 46. Scripts en Go nuevos: 35, 39, 40. Urgente de verdad: nº 35 (vault sin subir hace 30 h).

Límites activados: ninguno.

