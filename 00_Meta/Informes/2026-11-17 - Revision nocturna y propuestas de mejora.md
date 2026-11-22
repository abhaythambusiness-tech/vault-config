---
type: informe
status: pendiente-revision
origen: maquina
date: '2026-11-17'
---

# Revisión nocturna 2026-11-17

> [!resumen] En cristiano
> Hoy no había nada que mover de la raíz (0 archivos movidos). El disco bajó del 96 % al 91 %, pero el vault sigue sin commit desde el 13-nov (198 cambios) y no hay ningún cron/timer que lo haga. Hay 7 hallazgos de harness (nº 131-137), 8 propuestas (nº 138-145) y 6 apuestas atrevidas (nº 146-151). Te toca decidir: qué se limpia del disco (nº 131) y si pruebas el pack RGPD y el piloto de pago por cita (nº 138, 148).

## 2. Raíz ordenada

| Origen | Destino | Deshacer |
|---|---|---|
| (ninguno) | (ninguno) | — |

Sin mover, con motivo: `Sin título.canvas`, `Sin título 1.canvas` (2 bytes, vacíos, no clasificables; probablemente borrables) y `Compartido/` (carpeta del MCP `compartido`, con `Prueba-sync.md` y un log; no es un suelto). `git status --short`: 198 entradas, igual que antes.

## 3. Estado del vault (solo propuestas)

| Prioridad | Hallazgo | Acción propuesta | Riesgo |
|---|---|---|---|
| Alta | Último commit 2026-11-13 20:30; 198 cambios sin guardar; sin crontab ni timer de commit (solo `comandai-sync`, `ram-limpia`, `ordenar-descargas`, `ig-analytics-collector`). Refuerza nº 111. | Definir quién hace commit/push (script `vault-commit`, nº 60). | Bajo |
| Media | `01_Projects/`: estados mezclados (`propuesto`/`propuesta`, `borrador`/`draft`, `en-construccion`, `implementado-verificado`, `cerrado`); 17 `congelado`. 63 notas de primer nivel sin `origen`. | Aprobar la lista cerrada de estados (decisión abierta §7 del CLAUDE.md) y etiquetar con `etiquetar_origen.py` (simulacro). | Bajo |
| Media | `Enfoque web de la competencia.md` 177 KB (nota humana). | Dividir solo aditivo. | Medio |
| Baja | `00_Inbox/`: 2 notas sin clasificar. 1 enlace roto y 48 huérfanas (informe «Salud del vault» 2026-11-16). | Haytham clasifica; enlazar huérfanas desde MOCs. | — |

## 3B. Auditoría del harness

Medido hoy: arranque ≈ 40 KB (global 11,0 + vault 28,7 KB + MEMORY). `rules/` 132 KB en disco. Disco `/` 91 % (41 GB libres). Claude Code 2.1.323 (changelog ya en 2.1.326). `sync-gemini --check`: al día. Skills: 56 invocaciones en 30 días, 42 de `diseno-central`, 59 de 63 activas sin uso (poda: **2026-12-04**). Tareas programadas: las 2 activas, última ejecución 17-nov sin fallo visible (solo se leyó `list_scheduled_tasks`; `list_task_runs` de cierre-nocturno devolvió 16 ejecuciones, sin expandir).

| nº | tipo | hallazgo y evidencia | impacto | esfuerzo | recomendación |
|---|---|---|---|---|---|
| 131 | recorte | `~/.cache` 16 GB y `~/.npm` 13 GB (CTO, sin desglosar). Distintos de lo visto en nº 110. | ~29 GB (91 % → ~85 %) | S | Tras `du` por carpeta y con permiso: `npm cache clean --force`, limpiar pip/torch/huggingface si `vectordb-venv` los duplica. Se regeneran. |
| 132 | script | 3 transcripciones del vault de 51, 29 y 27 MB; `~/.claude/projects` 1,7 GB. | ~1 GB | S | Binario Go que comprima a `.zst` las de >14 días (alternativa a borrar, nº 112). Reversible. |
| 133 | punto ciego | `plugins/` 1,3 GB; ~250 skills y +60 MCP de plugins de cuenta (small-business, sales, finance…) en cada arranque. | 1 GB y lista de arranque más corta | S | Con permiso, desinstalar los que no se usaron en 30 días (MCPs usados: casi solo Browser, n8n, obsidian). |
| 134 | regla | `MEMORY.md`: 15 entradas, 4 marcadas «ya en CLAUDE.md». | ~1,5 KB/arranque | S | Mover esas 4 a `_archivo/`; tope de 12 entradas. |
| 135 | hook | Changelog 2.1.326: un hook con `"decision": "block"` ahora bloquea en más casos. Tenemos `guard-*`. | Evita bloqueos inesperados | S | Tras actualizar Claude Code, probar los guards en sandbox. |
| 136 | punto ciego | `cost-tracker.log` sin escribir desde 2026-11-13 00:48 (nº 89 sigue abierto). | Sin datos de coste | S | Revisar el hook. |
| 137 | punto ciego | Claude Code 2.1.323 vs 2.1.326: `/update-config` baja de ~93 k a ~13 k tokens; tareas programadas piden permiso por skills con `allowed-tools` salvo `Skill(nombre)` en `permissions.allow` ([changelog](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md), leído 17-nov, solo 100 K de 1,3 M caracteres). | Tokens; tareas sin atascos | S | Actualizar; refuerza nº 91. |

Modelos por agente: ya bien (13/13 con `model:`, 10 sonnet, 3 haiku); sin propuesta. Permisos de `~/.claude/reference/`: archivos `.env` en `600` (solo rutas verificadas; `projects/` es `755` dentro de `~/.claude` `700`).

**Ahorro de tokens estimado**: sin medir salvo lo dicho (~1,5 KB/arranque con nº 134; la lista de skills/MCP de plugins, nº 133, no se pudo medir en tokens).

**Candidatos a script/hook (Go)**: compresor de transcripciones (132), `vault-commit` (111), `nz cto disco` con aviso (110), `guard-arranque` (114).

## 4. Propuestas de mejora

| nº | área | propuesta | beneficio | coste/riesgo | fuente | recomendación |
|---|---|---|---|---|---|---|
| 138 | Servicio | Pack de cumplimiento del bot (aviso «hablas con una IA», consentimiento, registro de tratamientos) por 150-300 € para clínicas | Sube el ticket; quita una objeción | Es asesoría legal: solo plantilla sin abogado; cifras legales sin confirmar | CEO | probar |
| 139 | Captación | 1 charla de 30 min en un colegio profesional o cámara local («3 fugas de citas que no ves») | Audiencia cualificada sin cold email | Puede dar 0 leads | CEO | probar |
| 140 | Precio | Prepago anual (10 meses por 12) con garantía de 30 días | Caja por adelantado | Reembolsos si Mila falla | CEO | aplicar con el 1.er cliente de pago |
| 141 | Nicho | Contar en Laya Leads (1.900 leads) cuántos fisios/podólogos/estética tienen WhatsApp sin reserva online | Coste 0 € | Dispersa foco (nº 23): solo contar, no vender | CEO | probar el recuento |
| 142 | Skills | `agent-browser` (vercel-labs, 17,8 K, trending) y `seo-audit` de coreyhaines31/marketingskills (mismo repo que `cold-email`, nº 123) | Navegar/SEO | Una skill es texto que el agente obedece: leer SKILL.md. Instalaciones de SEO sin confirmar | [skills.sh](https://skills.sh) 17-nov | probar uno |
| 143 | Skills | Diseño: `frontend-design` (anthropics/skills, 1,1 M), `ui-taste` (1,1 M), `high-end-visual-design`, `minimalist-ui` (mismo repo que `design-taste-frontend`) | Poca novedad | Solapan con `diseno-central`, `design-taste-frontend`; `ui-taste`, `design-mobile-apps`, `ios-design` sin evaluar | skills.sh 17-nov | descartar (duplicados) salvo `ui-taste` tras leerla |
| 144 | Skills | Go: `golang-patterns`/`golang-testing` (everything-claude-code) y `johnqtcg/awesome-skills` | Encajan con la regla de Go | Instalaciones casi 0: poco probadas | skills.sh 17-nov | descartar por ahora |
| 145 | Flujo | Agente nocturno que abre PR y una persona fusiona (ya nº 124); aviso: estudio de ~110.000 PR halla más cambios posteriores y menos código que sobrevive | Cautela con datos | Nunca push directo | [alphaxiv](https://www.alphaxiv.org/abs/2604.00917.md), [Greptile](https://greptile.com/blog/rise-of-the-overnight-agents) | probar solo con revisión humana |

Skills de n8n, Obsidian, SEO y ventas por tema: las búsquedas de skills.sh cargaron vacías; no se afirma nada.

## 4B. Apuestas atrevidas

Ronda de reto (una): el CEO rompió las del CTO y el CTO las del CEO.

| nº | idea | por qué es atrevida | experimento ≤1 día | riesgo y reversión | coste | apuesta |
|---|---|---|---|---|---|---|
| 146 | **Memoria que se cura sola** (CTO): Go en Zorin comprueba que rutas/flags citados en `memory/*.md` aún existen; informe «memoria rancia» | Hoy la memoria solo crece | 40 líneas de Go sobre las 18 memorias | Reto CEO: **aguanta con cambio** — solo rutas absolutas entre comillas de código y solo las que antes existían, o habrá falsos positivos. Solo informa | 0 tokens | 2 · probar en sandbox |
| 147 | **Copias con versiones en Zorin** (CTO): rsync del vault y `~/.claude` sin `projects/`/`plugins/`, aviso a n8n | Pasa de copia manual a automática | rsync a carpeta de prueba, restaurar un archivo | Reto CEO: **aguanta con cambio** — rsync simple copia también borrados/corrupción: usar `--link-dest` con 7 copias rotativas o restic y avisar al 80 %. Zorin 44 % de disco, RAM sin medir | 0 | 3 · probar en sandbox |
| 148 | **Auto-poda por uso real** (CTO): job que propone apagar skills/hooks/MCP sin uso | El sistema se recorta solo | Tabla Markdown desde `uso.jsonl` | Reto CEO: **se rompe** con 56 invocaciones/30 días (42 de una skill): «sin uso» = «no lo usé este mes». Cambio: solo con ≥90 días de datos, nunca apagar hooks de seguridad. La poda de 2026-12-04 ya cubre lo útil | sin medir | 2 · guardar hasta tener 90 días |
| 149 | **Mila solo de noche y fines de semana** (CEO): producto estrecho (20:00-09:00 y festivos) | Renuncia al «recepcionista completo» | 30 conversaciones sintéticas | Reto CTO: **aguanta con cambio** — lo sintético no prueba demanda; probar con 30 chats reales anonimizados; regla fija de urgencias (teléfono de guardia + aviso humano) | sin medir | 2 · probar en sandbox |
| 150 | **Recotizar INGECONS al doble por valor** (CEO) | Único cliente con propuesta viva | Borradores A/B sin enviar | Reto CTO: **aguanta con cambio** — A = doble con ROI visible; B = precio actual + extra de mantenimiento; decide Haytham/Sam. Si se envía, no hay vuelta | hasta ~2.400 € + 180-240 €/mes en juego | 4 · probar solo como borrador |
| 151 | **Mila en marca blanca para agencias web** (CEO), reparto 70/30 | Nos vuelve proveedor | Clonar instancia, medir montaje | Reto CTO: **se rompe** — N instancias a mano, riesgo de baneo (API no oficial) y RGPD sin contrato de encargado. Cambio: un n8n multi-tenant, API oficial de WhatsApp, piloto con 1 agencia | sin medir | 3 · guardar |

Precedentes (investigador): pago por resultado lo usa solo el 3,8 % de 80 empresas de agentes (Orb, vía blog; otro blog proyecta 61 % a fin de 2026, sin confirmar); [Aloware](https://aloware.com/ai-voice-agent/outcome-based-pricing) lista 8-40 USD por cita; todo de vendedores. Memoria: «Dreaming» para Managed Agents (anunciado 06-may-2026, [MindStudio](https://www.mindstudio.ai/blog/what-is-claude-dreaming-anthropic-agent-memory)); «Auto Dream» en Claude Code no es oficial ([Tessl](https://tessl.io/blog/anthropic-tests-auto-dream-to-clean-up-claudes-memory/)). Auto-mejora con evaluación: [EvoSkill](https://github.com/geffzhang/EvoSkill) y GEPA/DSPy en Hermes (resultados de los propios autores).

## 5. Novedades de internet (17-nov)

- Claude Code 2.1.325-2.1.326 ([changelog](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md)): `/update-config` ~13 k tokens (antes ~93 k); hooks `block` más estrictos; reanudar con poca memoria sin perder historial; tareas programadas piden permiso por skills con `allowed-tools`/hooks salvo `Skill(nombre)` en `permissions.allow`; autocompactación en modo plan con el modelo activo (puede costar más).
- CLAUDE.md corto: guías de terceros dicen <200 líneas (otra <150), enlaces `@` y solo reglas siempre válidas ([dev.to](https://dev.to/nishilbhave/claudemd-best-practices-the-complete-2026-guide-435j), fecha sin confirmar; no se halló página oficial). El nuestro (11 + 28,7 KB) es bastante más largo: ver nº 128 de ayer.
- skills.sh «todo el tiempo»: design-mobile-apps 1,5 M, frontend-design 1,1 M, ui-taste 1,1 M; trending: hyperframes (HeyGen), remotion-best-practices, agent-browser. Listas: ComposioHQ/awesome-claude-skills, hesreallyhim/awesome-claude-code.
- Diseño 2026: tipografías variables (Fraunces, Cabinet Grotesk, Clash Display), texto cinético, 3D con Spline/Unicorn Studio, respetar `prefers-reduced-motion` ([Lovable](https://lovable.dev/guides/website-design-trends-2026), [Line25](https://line25.com/articles/web-design-trends-2026/); blogs de opinión; cifras sin fuente primaria).

## 6. Lo que NO se hizo / límites

- Nada movido ni aplicado. No se re-midieron enlaces rotos/huérfanas (se usa el informe «Salud del vault» del 16-nov).
- Cifras del CTO (`~/.cache`, `~/.npm`, `plugins/`, transcripciones) no re-verificadas por mí; sin desglosar `.config` ni `~/.var`.
- Changelog leído solo en parte (100 K de 1,3 M caracteres). Búsquedas por tema en skills.sh vacías.
- `list_task_runs` no expandido; no se midió RAM de Zorin.
- Numeración: continúa desde 131 (CEO y CTO usaron 131-137 en paralelo; renumerado aquí).

## 7. Siguiente paso

Haytham marca por nº qué se aplica. Tocan `settings.json`, hooks, skills, plugins o borran datos (sesión aparte con permiso): 131, 132, 133, 134, 135, 136, 137, 142, 146-148.

Límites activados: ninguno (≈20 llamadas, 5 agentes).

