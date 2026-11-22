---
type: informe
status: pendiente-revision
origen: maquina
date: '2026-11-15'
---

# Revisión nocturna 2026-11-15

> [!resumen] En cristiano
> No hubo nada que mover de la raíz (0 archivos movidos). Quedan 3 cosas sueltas que la tarea no puede clasificar; la más urgente es un ZIP de 290 MB que el auto-push del vault intentaría subir a GitHub. Hay 8 hallazgos de harness (nº 88-95), 9 propuestas (nº 96-104) y 5 apuestas atrevidas (nº 105-109). Te toca decidir: qué hacer con el ZIP, si se ajustan los permisos de las tareas nocturnas (nº 91) y qué proyectos congelados tienen puerta de reactivación (nº 101).

## 2. Raíz ordenada

| Origen | Destino | Deshacer |
|---|---|---|
| (ninguno) | (ninguno) | — |

Sin mover, con motivo:
- `Benimar-20261113T154106Z-1-001.zip` (290 MB): un `.zip` no está en las reglas de la Fase 0. Sigue **sin ignorar** en `.gitignore` y el vault tiene 161 entradas sin commit. Ver nº 88.
- `Sin título.canvas` y `Sin título 1.canvas` (2 bytes, vacíos): no son clasificables por regla. Probablemente se pueden borrar; lo decide Haytham.
- `git status --short` no cambia por esta fase (no se movió nada).

## 3. Estado del vault (solo propuestas, nada aplicado)

| Prioridad | Hallazgo | Acción propuesta | Riesgo |
|---|---|---|---|
| Alta | Estados mezclados en `01_Projects`: `aprobado` 69 / `aprobada` 17; `activo` 65 / `en-progreso` 9; 20 `por-validar`. | Fijar la lista cerrada de estados (pendiente en CLAUDE §7) y normalizar con `vault-salud`. | Bajo |
| Alta | 72 destinos de enlace rotos distintos. Los reales: `goat-trading` (10), `Vault OS` (6), `Dashboard Command AI` (5), `AVAX-RL-Bot` (6), `crypto-copy-bot-spec`, `00_Roadmap Maestro…` (todos proyectos archivados). Los `{{nombre}}` son plantillas: falsos positivos. | Enlazar a su ficha en `04_Archive/` o quitar el enlace. | Bajo |
| Media | 14 notas sin `origen:` en 00_Meta/01/02/03. | `etiquetar_origen.py` (simulacro primero). | Bajo |
| Media | 49 notas sin enlace entrante (p. ej. `Registro de Oportunidades`, `Plan de Componentes UX v2`, `Experimento oro (PAXG)`, plantillas). Muchas son plantillas (esperable). | Enlazar las no-plantilla desde su MOC. | Bajo |
| Media | `02_Areas/NeoZeler/Estrategia/Enfoque web…` pesa 177 KB; `Reto-30/Software/5 - Backend Schema` 56 KB; `Comanda Viva/5 - Backend` 48 KB. | Dividir el de 177 KB por secciones; los demás leer con `offset`. | Medio (nota humana: solo aditivo) |
| Baja | `00_Inbox/` con 2 notas (`preparacion-con-carlos`, `Plan futuro de aqui 3 años`). | Haytham las clasifica. | — |
| Baja | 193 sesiones en `00_Meta/Sesiones/`; la última, `2026-11-15 - Cierre nocturno`. Sin medir cuántas no enlazan a su proyecto. | Medir con script. | — |

## 3B. Auditoría del harness

Medido: arranque ≈ 40 KB (global 10,7 + vault 27,7 + MEMORY 1,8); `rules/` 111 KB (no se mide cuáles cargan). Disco 81 % (89 GB libres). Zorin: encendido 9 días, disco 44 %, RAM libre 189 MB (2,3 GB disponibles), **sin `claude` instalado**. `settings.json`: 0 allow, 19 deny, 2 ask; solo 9 plugins activos. `claude` 2.1.323.

| nº | tipo | hallazgo y evidencia | impacto | esfuerzo | recomendación |
|---|---|---|---|---|---|
| 88 | punto ciego | ZIP de 290 MB en la raíz, no ignorado; sigue desde el 14-nov (repite nº 67). | Auto-push de 290 MB / repo hinchado | S | Mover a `99_Assets/Documentos/` o fuera del vault y añadir `*.zip` a `.gitignore`. Haytham decide. |
| 89 | punto ciego | `bash-commands.log` y `cost-tracker.log` (2,8 MB c/u) siguen sin escribirse desde 2026-11-13 (repite nº 61). Causa sin confirmar. | Telemetría de coste ciega | S | Revisar qué hook los escribía. |
| 90 | punto ciego | `sync-gemini --check` → DESFASADOS: `~/.gemini/config/GEMINI.md` y `00_Meta/GEMINI.md` (repite nº 59/74). | Gemini con reglas viejas | S | Correr `sync-gemini`; hook pre-commit. |
| 91 | regla/config | Claude Code 2.1.319: `permissions.denyInsteadOfPrompting`; 2.1.325: las tareas programadas piden permiso antes de skills con hooks salvo `Skill(nombre)` en allow. Fuente: [changelog](https://code.claude.com/docs/en/changelog) (leído 15-nov). | Una tarea nocturna puede quedarse colgada | S | Probar en sesión aparte (toca `settings.json`). |
| 92 | recorte | Variable `CLAUDE_CODE_DISABLE_AGENT_PROGRESS_SUMMARIES=1` (2.1.323) ahorra tokens en subagentes; `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` evita ventana de 1M asumida. Ahorro sin medir. | Tokens | S | Probar (toca `settings.json`). |
| 93 | recorte | Esta sesión lista ~250 skills y +40 MCP sin autorizar de plugins de cuenta (`small-business`, `sales`, `finance`, `fastly`, `buildkite`, `qt`…), pero `enabledPlugins` solo tiene 9. Vienen de la cuenta de claude.ai, no de `settings.json`. Tokens sin medir. | Contexto de arranque | S | Apagarlos en los ajustes de la cuenta; medir con `token-optimizer:quick` antes/después. |
| 94 | punto ciego | Zorin no tiene `claude` (exit 127) ni Node en PATH visible; bloquea apuestas que ejecuten agentes allí. | Riesgo de plan | S | Decidir si se instala (sesión aparte). |
| 95 | punto ciego | Ya aplicado, no repetir: todos los agentes tienen `model:` (comprobado), `cleanupPeriodDays: 180`, hooks con timeout. Poda de skills: esperar al **2026-12-04** (46 usos de skills registrados; `diseno-central` domina). | — | — | — |

**Ahorro de tokens estimado**: sin medir (nº 92, 93, 103). Solo cifras reales: arranque 40 KB.

**Candidatos a script/hook (Go)**: `vault-commit` (nº 60, ya propuesto); `PreCompact` con las «Compact Instructions» (nº 103); rotación semanal de `uso-mcp.jsonl` (168 KB; nº 104).

## 4. Propuestas de mejora

| nº | área | propuesta | beneficio | coste/riesgo | fuente | recomendación |
|---|---|---|---|---|---|---|
| 96 | Skills | `czlonkowski/n8n-skills` (14 skills de n8n, MIT, ~6,6k estrellas) | Mejores flujos n8n | Skill ajena: leer SKILL.md; fecha de último commit sin confirmar | [GitHub](https://github.com/czlonkowski/n8n-skills) (15-nov) | probar |
| 97 | Skills | `kepano/obsidian-skills` | — | **Duplicado**: ya tenemos obsidian-markdown, obsidian-bases, json-canvas y obsidian-cli | [GitHub](https://github.com/kepano/obsidian-skills) | descartar |
| 98 | Skills | `website-builder` (flowkit-labs, skills.sh) | Webs | Solapa con `diseno-central`; cifras de instalaciones poco fiables | [skills.sh](https://skills.sh) (15-nov) | descartar salvo hueco real |
| 99 | Comercial | Nota `02_Areas/NeoZeler/Comercial/Embudo.md` con tabla (lead, tier, etapa, próxima acción, fecha) a mano | Los leads de Laya Leads se trabajan sin CRM | 30 min; se borra la nota | CEO | aplicar |
| 100 | Flujo | Plantilla «un cliente = una carpeta» (Brief, Entregable, Resultado, Permiso de caso de éxito) en `00_Meta/Plantillas` | El caso de éxito sale al cerrar | 1 h | CEO | aplicar |
| 101 | Flujo | Cada proyecto congelado lleva «se reactiva si: X»; sin esa línea pasa a `abandonado` | 17 congelados dispersan | Decide Haytham | CEO | aplicar |
| 102 | Flujo | Hueco fijo semanal de captación (90 min, lunes) | Constancia | 90 min/semana; horas reales sin confirmar | CEO | probar |
| 103 | Hook | Mover «Compact Instructions» a un hook `PreCompact` en Go | Unos cientos de tokens por turno | Toca CLAUDE/hooks | CTO | probar |
| 104 | Script | Rotar `uso-mcp.jsonl` y resumir por semana en `informe-uso-skills` | Decidir MCP a apagar con datos | Bajo | CTO | aplicar |

## 4B. Apuestas atrevidas

| nº | idea | por qué es atrevida | experimento ≤1 día | riesgo y reversión | coste | apuesta |
|---|---|---|---|---|---|---|
| 105 | **Demo personalizada por prospecto**: la IA monta una mini-web con su logo y textos más un chat FAQ, y se le enseña antes de vender | Se trabaja gratis antes de vender | 3 empresas del CSV de Laya Leads, demos en carpeta local, cronometrar (>20 min cada una = no escala). Nada se envía. | Parecer spam / marca ajena: antes de usarla real, revisar `leyes-autonomos-agencia-ia`; se borra la carpeta. Eficacia en frío: **sin evidencia** (investigador no halló). | Sin medir | 4 · probar en sandbox |
| 106 | **«Auditor de clínicas» como producto**: la skill `auditoria-ia-clinicas` genera un informe por URL; se vende (29-49 €) o se regala de gancho | De servicio a producto con coste casi cero | 5 URLs públicas de clínicas, comparar con juicio humano; >2 flojos = descartar | Informes genéricos; solo lectura. Skill no ejecutada aún. | Sin medir | 3 · probar |
| 107 | **Precio híbrido por conversación resuelta** en agentes de WhatsApp (fijo bajo + variable) | Obliga a medir resultados desde el día 1. Precedente: Salesforce Breeze 0,50 USD/conversación; en general ~95 % usa híbrido ([monetizely](https://www.getmonetizely.com/articles/what-should-companies-charge-for-an-ai-agent-s-work), cifra de vendor sin verificar) | Hoja con 500/1.500/4.000 conversaciones/mes y coste real de tokens y n8n | Ingresos impredecibles; sin gasto si sale negativo. Definir «resuelta» antes de cobrar. | 0 €, ~3 h | 3 · probar |
| 108 | **Banco de pruebas con tus propias sesiones**: 20 prompts reales de los transcripts contra dos configuraciones del harness (actual vs mínima) | Hoy el harness se decide por intuición | Binario Go extrae prompts; `claude -p` con `CLAUDE_CONFIG_DIR` de copia y worktrees desechables; puntuar con criterios ocultos al agente | Juez que se equivoca o tareas que tocan archivos reales; se borra la carpeta. Aprovecha nº 85/86 del informe anterior. | Sin medir (consumo de suscripción) | 3 · probar |
| 109 | **Zorin como CI**: tras cada commit en `~/Proyectos`, build + axe/Lighthouse en Zorin y resultado a una nota | Verificar deja de ser manual | Hook `post-commit` en Go con `ssh` a Zorin, 1 repo, con timeout; `git clone` limpio sin `.env` | Zorin saturado (RAM libre 189 MB); se quita el hook. Ojo nº 94. | 0 € | 2 · guardar |

Retos entre CEO y CTO (ronda de «romper la idea»): **no se hizo** (ver límites). Autocrítica mía: 105 y 107 se apoyan en cifras de vendedores; 108 es fácil de engañarse al puntuar.

## 5. Novedades de internet (15-nov)

- Claude Code 2.1.319-2.1.325 (6-13 nov): `denyInsteadOfPrompting`, permisos de tareas programadas, variables de ahorro de tokens, `/context` más ligero, se elimina `subagentStatusLine`. [Changelog oficial](https://code.claude.com/docs/en/changelog).
- Vaults que se curan solos (proyectos personales, sin métricas de agencia): [obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain); [Vault Health Check de solo lectura](https://forum.obsidian.md/t/vault-health-check-a-read-only-claude-code-routine-that-audits-your-vault-free-mit/117831) (ya hacemos lo mismo con esta tarea); un autor reporta ~0,04 USD/noche ([dev.to](https://dev.to/bokuwalily/turning-conversation-logs-into-obsidian-long-term-memory-a-pipeline-that-distills-them-every-night-18c2), sin verificar).
- Agentes de noche: [Automaton](https://automatonagency.com/work/autonomous-session-infrastructure) (interno, sin métricas de cliente); Routines en la nube de Anthropic ([guía](https://www.mindstudio.ai/blog/claude-code-routines-scheduled-agents)).
- Diseño web 2026: tipografía grande/experimental, 3D con propósito, Figma Motion; fuentes de marketing, fechas sin verificar ([index.dev](https://www.index.dev/blog/web-design-trends)). Ya cubierto por `threejs-*` y `web-animation-skills`.
- skills.sh: las búsquedas por tema cargan vacías en lectura; las cifras de /trending parecen infladas. Candidatas solo con aviso: leer SKILL.md antes de instalar (una skill es texto que el agente obedece).
- Webs de precio fijo: la trampa son las «revisiones ilimitadas» ([DesignRush](https://news.designrush.com/small-budget-website-projects)).

## 6. Lo que NO se hizo / límites

- No se movió nada (no había sueltos clasificables) ni se aplicó ninguna propuesta.
- Ronda de reto CEO↔CTO de la Fase 2B omitida por coste; los agentes trabajaron en paralelo sin cruzarse.
- Sin búsqueda web propia del CTO ni del CEO; el CEO no leyó `Contexto NeoZeler`.
- No se midió qué `rules/` cargan al arrancar ni el ahorro real de tokens.
- skills.sh por tema, ventas/diseño/Go nuevos y casos reales de agencias con resultados: sin evidencia.
- `graphify update .` y registro de sesión: ver nota de sesión (si falla, se anota allí).

## 7. Siguiente paso

Haytham marca por nº qué se aplica. Tocan `settings.json`/hooks/skills (esta tarea no puede aplicarlos; sesión aparte con permiso): 88 (`.gitignore`), 91, 92, 93, 96 (instalar skill), 103, 104.

Límites activados: ronda de reto CEO↔CTO omitida; ninguno de tiempo ni de llamadas.

