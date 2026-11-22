---
type: informe
status: pendiente-revision
origen: maquina
date: '2026-11-14'
---

# Revisión nocturna 2026-11-14

> [!resumen] En cristiano
> Anoche solo había **1 cosa suelta** en la raíz y la moví a `00_Inbox/`. Queda un ZIP de 290 MB (Benimar) sin mover porque no encaja en las reglas: decide tú. El vault está sano (0 enlaces rotos según `vault-salud`), pero los dos `GEMINI.md` están desfasados y hay 156 cambios sin commit. Auditoría del harness: **10 hallazgos** (nº 58-67). Hay **20 propuestas** (nº 68-81) y **6 apuestas atrevidas** (nº 82-87). Tú marcas por número qué se aplica.

## 2. Raíz ordenada

| Origen | Destino | Deshacer |
|---|---|---|
| `Plan futuro de aqui 3 años.md` | `00_Inbox/Plan futuro de aqui 3 años.md` | `mv "00_Inbox/Plan futuro de aqui 3 años.md" .` |

Sin enlaces entrantes (grep) y sin choque de nombres. Es una nota personal (lista de metas): propuesta de destino final, `02_Areas/` o `00_Meta/`, la eliges tú. Sin commit.

**No movido:** `Benimar-20261113T154106Z-1-001.zip` (290 MB). Un .zip no está en la lista de la tarea. Está sin seguir en git; si alguien hace `git add -A`, subiría 290 MB al auto-push. Propuesta nº 67.

## 3. Estado del vault

| Prioridad | Ruta | Problema | Acción propuesta | Riesgo |
|---|---|---|---|---|
| Media | `01_Projects/*` | Estados fuera de la lista propuesta: `en-construccion` (Ultimo en Pie), `implementado-verificado` (Abisal Drill), `propuesto`, `borrador`, `cerrado` (Panel de Leads); `Yescapa Benimar 495 - ficha.md` sin `status` ni `origen` | Normalizar cuando apruebes la lista (CLAUDE.md vault §7); ficha Yescapa: añadir frontmatter | Bajo |
| Media | `00_Meta/GEMINI.md`, `~/.gemini/config/GEMINI.md` | Desfasados (`sync-gemini --check`) | Correr `sync-gemini` | Bajo |
| Baja | 49 huérfanas | Ver `Salud del vault.md` (plantillas, Retros, `Convencion Humano-Maquina`) | Índice aditivo (propuesto antes, nº 20) | Bajo |
| Baja | `01_Projects/Dashboard Command AI/Retro.md`, `Los Apuntes de Liyo/Retro.md` | Sin enlace desde su ficha | Enlazar desde la ficha | Bajo |

Sin duplicados nuevos ni enlaces rotos detectados (según `vault-salud`, 2026-11-13; no relanzado esta noche). `graphify update .` ejecutado.

## 3B. Auditoría del harness

| nº | Tipo | Hallazgo y evidencia | Impacto | Esfuerzo | Recomendación |
|---|---|---|---|---|---|
| 58 | recorte | Arranque seguro: global 10,7 KB + vault 27,7 KB + MEMORY 1,8 KB ≈ 40 KB. `rules/` suma 112 KB (`skills-frecuentes` 25 KB, `skills-seleccion-global` 23 KB, `web.md` 17 KB) pero **no medí cuáles se cargan** (dependen de `paths`). | Hasta ~12k tokens/sesión si se cargan las dos listas de skills; sin medir | S medir / M recortar | Medir antes con `token-optimizer:quick`; pasar a `reference/` lo que cargue sin necesidad |
| 59 | punto ciego | `sync-gemini --check` → 2 `GEMINI.md` desfasados | Gemini con reglas viejas | S | Correr `sync-gemini` y enganchar a pre-commit |
| 60 | punto ciego | Vault: 156 entradas sin commit; último commit 2026-11-13 20:30 | Pérdida si falla el disco | S | Script Go `vault-commit` (sin push) |
| 61 | punto ciego | `bash-commands.log` y `cost-tracker.log` (2,8 MB cada uno) sin escribirse desde 2026-11-13 00:48; ningún hook de `settings.json` los escribe | Telemetría de coste ciega; causa sin confirmar | S | Mirar quién los escribía (¿rotación o hook retirado?) |
| 62 | punto ciego | `uso.jsonl`: 46 invocaciones en 10 días, `diseno-central` 34; 55 de 58 skills sin uso | Poda de skills | S | Esperar al **2026-12-04** (30 días reales) como dice el CLAUDE global |
| 63 | regla | Hallazgos de informes previos ya aplicados: hooks Go con `timeout` en todos, hook `Stop` (`verificar-cierre`), `guard-destructive`, `guard-read-grande`, `check-hooks` OK 17 casos, modelo `sonnet`, `cleanupPeriodDays` 180 | Riesgo bajado | — | Ninguna; seguir |
| 64 | regla | `settings.json`: 0 `allow`, 19 `deny`, 2 `ask` (igual que nº 43) | Prompts repetidos; sin medir | S | Lanzar `fewer-permission-prompts` en sesión aparte |
| 65 | punto ciego | Disco local 83 % (80 GB libres); `projects/` 1,6 GB; `_backups/` 62 MB, sin copia automática de `~/.claude` | Riesgo creciente | S | Aviso de disco + copia semanal (Go) |
| 66 | punto ciego | Zorin sano: 7 días encendido, disco 44 %, n8n y 5 contenedores doory arriba; RAM libre baja (238 MB; sin mirar swap). `claude --version` falló allí (exit 127; sin Claude Code o Node, no confirmado) | Condiciona nº 84 | S | Comprobar antes de pensar en agentes en Zorin |
| 67 | punto ciego | ZIP de 290 MB suelto en raíz | Auto-push de 290 MB | S | Mover a `99_Assets/Documentos/` y añadir `*.zip` a `.gitignore`, o fuera del vault |

**Ahorro de tokens estimado:** no medible esta noche. Techo teórico del nº 58: ~12k tokens/sesión; la cifra de ~35-40k del CTO asume que todo `rules/` carga siempre (sin verificar).

**Candidatos a script/hook (Go):** `vault-commit` (nº 60), pre-commit con `sync-gemini --check` (nº 59), `aviso-disco-backup` (nº 65), `vault-oraculo` (nº 87).

Tareas programadas: `cierre-nocturno-sesiones` y esta, ambas con `lastRunAt` de hoy; sin fallos visibles (no abrí `list_task_runs`).

## 4. Propuestas de mejora

| nº | Área | Propuesta | Beneficio | Coste/riesgo | Fuente | Recomendación |
|---|---|---|---|---|---|---|
| 68 | Servicio | «Auditoría IA de 1 hora» a precio fijo, informe de 1 página; piloto con 2 clientes web | Entrada barata, filtra curiosos | Trabajo gratis si precio 0 | CEO | probar |
| 69 | Servicio | Mantenimiento mensual con extra de IA en webs entregadas (chat FAQ, reseñas, resumen) | Ingreso recurrente | Soporte se come horas | CEO | aplicar en 1 cliente |
| 70 | Captación | Casos de éxito mínimos (antes/después + frase) con permiso por escrito | NeoFlow AI hoy sin pruebas | Ninguno serio | CEO | aplicar |
| 71 | Recorte | Mover las dos listas de skills a `reference/` si cargan al arrancar | ~12k tokens/sesión (sin medir) | Perder una regla | CTO | probar (tras nº 58) |
| 72 | Recorte | Dejar 2 líneas en §0.8-0.10 del CLAUDE del vault y detalle en `[[00 - Flujo de Software]]` | ~8k tokens (estimado) | Perder regla dura; revisar diff | CTO | probar |
| 73 | Script | `vault-commit` en Go: agrupa por carpeta, pasa `guard-secretos`, commit sin push | Historial limpio | Bajo | CTO | aplicar |
| 74 | Hook | `sync-gemini --check` en pre-commit | Fin del desfase | Bajo | CTO | aplicar |
| 75 | Config | Probar `permissions.blockWritesOutsideWorkingDirectories` (v2.1.314, 30-oct). Versión local 2.1.323 | Encaja con «no destruir sin comprobar» | Bloquear escrituras legítimas a `~/.claude` | [claude-world](https://claude-world.com/articles/claude-code-november-2026-whats-new/) (tercero; no abrí el changelog) | probar |
| 76 | Config | El modo rápido de Opus 4.8 desaparece el 2026-11-30: revisar si se usa | Evitar sorpresa | Ninguno | misma fuente, sin confirmar | revisar |
| 77 | Skills | `samber/cc-skills-golang` (~45 skills de Go) | Encaja con regla «scripts en Go» | Skill ajena: leer SKILL.md antes | [GitHub](https://github.com/samber/cc-skills-golang) (14-nov); instalaciones sin verificar | probar |
| 78 | Skills | `grill-me` (mattpocock/skills, 1,5M inst.) y `emil-design-eng` (446K) de skills.sh | Interroga antes de construir (PRD); pulido de animación | Solapa con `brainstorming`, `impeccable`; leer antes | [skills.sh](https://skills.sh) (14-nov) | probar tras leer |
| 79 | Skills | `coreyhaines31/marketingskills` (SEO + cold email) frente al perfil GTM | Comparar | Duplicar | [dev-gtm](https://github.com/infrasity-labs/dev-gtm-claude-skills), búsqueda 14-nov | descartar salvo hueco real |
| 80 | Memoria | Ver si `/memory` ofrece «Auto Dream» (poda y fusiona memoria) | Memoria limpia sola | Reglas de activación contradictorias; sin doc oficial | [claudefa.st](https://claudefa.st/blog/guide/mechanics/auto-dream) (2026) | probar mirando el interruptor |
| 81 | Diseño | Contratendencia a probar: ilustración a mano e imperfecciones frente a lo «pulido de IA»; web legible por agentes (datos estructurados) | Diferencial | Fuentes de marketing, flojas | [line25](https://line25.com/articles/web-design-trends-2026/) | probar en 1 web |

`web-design-guidelines` ya la tenemos instalada.

## 4B. Apuestas atrevidas

La ronda CEO vs CTO (que se retaran entre sí) **no se hizo** (límite de agentes); cada apuesta sale de un agente solo y los riesgos son los suyos.

| nº | Idea | Por qué es atrevida | Experimento ≤1 día | Riesgo y reversión | Coste | Apuesta |
|---|---|---|---|---|---|---|
| 82 | Clínicas dentales: NeoFlow AI sin cuota, **pago por cita confirmada** | Pasa el riesgo al proveedor | Hoja con 3 escenarios (5/15/30 citas) y datos falsos; no contactar a nadie | Citas que no llegan, disputas. Si margen medio < 0, se descarta; real: 1 piloto 30 días | 0 €, ~4 h | 4 · probar en sandbox |
| 83 | Convertir una web de cliente en **pack con plantilla**, instalación en 1 día | De agencia a medida a producto | Clonar Barber-DF en carpeta aparte, cambiar marca y textos, cronometrar (si > 4 h no escala) | Cada cliente pide «algo distinto»; se borra la carpeta | 0 €, 1 día | 3 · probar en sandbox |
| 84 | **Agente semanal por suscripción** que Haytham supervisa 30 min/semana | Cambia el trabajo de construir a vigilar | `claude -p` en Zorin sobre buzón ficticio 1 día; contar fallos y coste (ver nº 66: Zorin quizá sin Claude Code) | Errores con datos del cliente; apagar el servicio | ~5-10 € (sin medir), 6 h | 5 · probar en sandbox |
| 85 | **Arranque mínimo**: CLAUDE global ~5 KB y un hook `UserPromptSubmit` en Go que inyecta reglas por palabra clave | De «todo cargado» a «bajo demanda» | Copia de `~/.claude` en un `CLAUDE_CONFIG_DIR` de pruebas, 10 tareas reales con cada versión | Una regla no se inyecta; reglas duras §0 siempre cargadas; volver al directorio original | bajo; ahorro posible 25-30k tokens (estimado) | 4 · probar en sandbox |
| 86 | **Lista blanca de skills**: solo las usadas en 30 días + `diseno-central`, comando para reactivar | Apaga 55 skills de golpe | Archivar en sandbox y lanzar 5 tareas típicas | Falta una skill rara; `mv` de vuelta. Esperar a 2026-12-04 | 0 € | 3 · guardar |
| 87 | **Oráculo de verdad del vault**: binario Go nocturno que compara `Estado de Proyectos` con `git log` de `~/Proyectos` y escribe solo diferencias en nota `origen: maquina` | El vault se audita solo | Solo lectura sobre 5 proyectos y comprobar a mano | Ruido; máx. 10 líneas; borrar la nota | 0 tokens si es determinista | 5 · probar en sandbox |

Parecidas a ideas previas: 84 y 54, 86 y 44. Se mantienen porque traen un dato nuevo (84: Zorin sin confirmar; 86: telemetría real).

## 5. Novedades de internet (14-nov)

- Agente nocturno con tope y botón de pausa (archivo `PAUSE`, máx. 3 PRs/noche): [dev.to](https://dev.to/jenatechio/i-gave-an-ai-agent-nightly-merge-rights-to-every-repo-i-own-with-a-budget-and-a-kill-switch-5b6k). Primera noche 4 errores; los topes se reiniciaban tras un fallo. Anécdota única. Esta tarea ya tiene cortacircuitos; falta un `PAUSE` explícito.
- Auto-mejora de skills: [hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution). Riesgo documentado: el agente que ve la puntuación la trampea → evals ocultos ([tessl](https://tessl.io/registry/skills/github/muratcankoylan/Agent-Skills-for-Context-Engineering/self-improvement-loops)).
- skills.sh, ranking (14-nov): find-skills 4,4M, hyperframes 1,5M, grill-me 1,5M, agent-browser 1,5M, frontend-design 1,1M, web-design-guidelines 860K. Las búsquedas por tema no cargaron.
- Precio por resultado: solo fuentes de vendedores ([monetizely](https://www.getmonetizely.com/articles/why-are-outcome-based-ai-agent-pricing-models-gaining-traction), [ciela](https://ciela.ai/blogs/what-to-charge-for-ai-automation-services), 27-mar-2026): sin confirmar. 
- Webs personalizadas por prospecto: [SEATEXT](https://seatext.com/seatext-ai-personalization), [Architect](https://tryarchitect.com/abm); cifras de vendedor, sin confirmar.
- `ultrathink` = esfuerzo xhigh (v2.1.311, 26-oct), según el mismo tercero.
- Contradicciones: fecha de v2.1.318, estrellas de las listas awesome, reglas de Auto Dream.

## 6. Lo que NO se hizo / límites

- Ronda CEO vs CTO y agentes CFO/COO/CMO: no lanzados (3 agentes en total).
- No abrí el changelog oficial de Claude Code ni contrasté tres fuentes; no probé ninguna skill ni leí su SKILL.md.
- No relancé `vault-salud`; no medí qué reglas se cargan al arrancar; no leí `Contexto NeoZeler` ni la memoria a fondo.
- No toqué settings, hooks, skills, MCPs ni plugins. Sin commit ni push.
- CEO y CTO respondieron sin leer el vault esta noche; sus cifras son hipótesis.

## 7. Siguiente paso

**Haytham marca por número qué se aplica.** Las que tocan `settings.json`, hooks, skills o reglas y esta tarea no puede aplicar: 58, 59, 61, 64, 71, 72, 74, 75, 77, 78, 85, 86. Hacerlas en sesión aparte con tu permiso. Las demás (68-70, 82-84) son decisiones de negocio.

Límites activados: ninguno (≈35 llamadas, 4 agentes). Hallazgos de harness: 10.
