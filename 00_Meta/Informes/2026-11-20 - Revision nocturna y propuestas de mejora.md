---
type: informe
status: pendiente-revision
origen: maquina
date: '2026-11-20'
---

# Revisión nocturna 2026-11-20

> [!resumen] En cristiano
> **Sigue urgente: el disco está al 98 % (14 GB libres) y `/var/log/syslog` ya pesa 96,5 GB; el temporizador `comandai-sync.timer` sigue activo** (es el nº 152 del informe del 18-nov, sin resolver). No se movió ningún archivo: la raíz ya estaba limpia. La revisión del 19-nov no se hizo (límite semanal de uso agotado). Hay 15 hallazgos de harness (nº 165-179), 7 propuestas (nº 180-186) y 5 apuestas (nº 187-191). Decisiones tuyas: parar el temporizador, hacer copia de `~/.claude` y aprobar los recortes de CLAUDE.md.

## 2. Raíz ordenada

Movimientos: **ninguno** (0 archivos). Sin mover: `Sin título.canvas` y `Sin título 1.canvas` (2 bytes, vacíos, tipo no clasificable) y `Compartido/` (carpeta del MCP `compartido`, no es un suelto). `git status --short`: 248 entradas, sin commit desde el 13-nov 20:30.

## 3. Estado del vault (solo propuestas)

| Prioridad | Hallazgo | Acción propuesta | Riesgo |
|---|---|---|---|
| Alta | 248 cambios sin commit, último commit hace 6 días (nº 179). | Commit manual o `vault-commit` en Go. | Bajo |
| Media | Ingecons Facturas: 3 repos en `~/Proyectos` (`ingecons`, `ingecons-facturas`, `ingecons-facturas-demo`) y sesiones 19 y 20-nov, pero sin ficha en `01_Projects/` (regla vault §0.8) (nº 177). | Crear ficha desde las sesiones. | Bajo |
| Media | Enlace roto: `00_Meta/Sesiones/2026-11-14 - Obsidian tema Rho Zero legible (cierre automatico).md` apunta a `...Obsidian - plugin Rho Network...`; la nota real lleva «:» (nº 178). | Corregir el enlace (nota `maquina`). | Bajo |
| Media | Estados sin lista cerrada en `01_Projects/`: `en-construccion`, `implementado-verificado`, `propuesto`, `propuesta`, `en-progreso`; `Yescapa Benimar 495 - ficha.md` sin `status`. | Aprobar la lista de §7 del CLAUDE.md. | Bajo |
| Baja | `00_Inbox/`: `2026-10-13_1223_preparacion-con-carlos.md` y `Plan futuro de aqui 3 años.md` sin clasificar. Huérfanas: 48 el 16-nov (no re-medido hoy). | Haytham clasifica. | — |

## 3B. Auditoría del harness

Medido hoy: `/` 98 % (14 GB libres); Zorin sano (47 %, 119 GB libres, 0 servicios fallidos, carga 0,13). Claude Code instalado 2.1.323. Skills: 65 invocaciones en 30 días (43 `diseno-central`); 66 de 74 activas sin uso (poda el **2026-12-04**, aún no toca). `sync-gemini --check`: al día. Hooks (`check-hooks`): 17 casos OK, 2-3 ms.

| nº | tipo | hallazgo y evidencia | impacto | esfuerzo | recomendación |
|---|---|---|---|---|---|
| 165 | punto ciego | `df /` = 98 %; `syslog` 96.574 MB; `systemctl --user is-active comandai-sync.timer` = active. Empeora respecto al 18-nov (97 %, 92 GB). Refuerza nº 152-154. | Riesgo de que el equipo se quede sin disco hoy | S | Parar el timer y corregir IP (.100→.101) YA; ver nº 152. |
| 166 | punto ciego | `~/.claude` pesa 9,5 GB, sin git ni cron de copia; `_backups/` está en el mismo disco. Lo valioso (CLAUDE.md, rules, agents, bin, reference, settings) son pocos MB. | Evita perder todo el harness | M | Script Go: copia diaria de lo valioso (sin `projects/` ni secretos en claro) a Zorin. |
| 167 | recorte | `vault/CLAUDE.md` = 29.885 B (68 % de lo que carga el arranque, ~44 KB ≈ 12,6k tokens). El §0.10 (flujo de 6 documentos, ~4,5 KB) pasa a `reference/flujo-6-docs.md` con una línea. | ~1,3k tokens por sesión | M | Probar |
| 168 | recorte | §1 del vault CLAUDE.md (~6 KB, lista de proyectos) duplica `00_Meta/Estado de Proyectos`. Dejar puntero. | ~1,7k tokens | S | Aplicar |
| 169 | recorte | §3.1-3.3 y §5 del vault (graphify, tokens, convenciones visuales, ~5 KB) a `reference/`. | ~1,4k tokens | S | Aplicar |
| 170 | regla | Hooks sin regla escrita: `guard-ui-commit`, `guard-read-grande`, `verificar-cierre`; regla sin hook: `sistemas-resiliencia.md`. `rtk hook claude` en PreToolUse sin regla propia. | Menos sorpresas | S | Documentar en `rules/harness.md`. |
| 171 | script | `~/.claude/bash-commands.log` y `cost-tracker.log` 2,7 MB cada uno, sin rotación; `uso-mcp.jsonl` 3.420 líneas. | Disco/ruido | S | Go: rotar con gzip semanal (ya hay `logs-archivo/` del 13-nov manual). |
| 172 | regla | `settings.json`: `allow` vacío, 19 `deny`, 2 `ask`. Cada Bash nuevo pide permiso. | Menos prompts | S | `/fewer-permission-prompts` en sesión aparte (toca settings). |
| 173 | recorte | Agentes: 3 en haiku, 10 en sonnet. Candidatos a haiku: `investigador`, `scraper`, `neozeler-cfo`. Sin pruebas de calidad. | Menos coste por agente | S | Probar con 1 tarea cada uno. |
| 174 | punto ciego | `.credentials.json`: access token caducado hace 47 h (probablemente se renueva solo; **no verificado**). Solo se reporta la ruta. | Aviso antes del fallo | S | Comprobar a mano que `claude` sigue autenticado. |
| 175 | punto ciego | La revisión del 19-nov falló: `You've hit your weekly limit · resets 7am` (`list_task_runs`). Nada avisó. | Noches perdidas | S | Aviso en Panel si una tarea programada falla. |
| 176 | regla | Claude Code 2.1.323 instalada; hay 2.1.329 (19-nov): `/tasks` muestra programadas, parches de permisos 2.1.321/2.1.326 (fuente de tercero, sin confirmar en el changelog oficial). Refuerza nº 159. | Seguridad | S | Actualizar en sesión aparte. |

**Ahorro de tokens estimado**: nº 167+168+169 ≈ 4,4k tokens por sesión (~35 % del arranque, estimado a bytes÷3,5; no medido en sesión real).

**Candidatos a script/hook (Go)**: copia de `~/.claude` (166), rotador de logs (171), aviso de tarea programada fallida (175), `vault-commit` (179, refuerza nº 111), guardia de disco (nº 161).

| nº | tipo | hallazgo y evidencia | impacto | esfuerzo | recomendación |
|---|---|---|---|---|---|
| 177 | vault | Falta ficha de Ingecons Facturas (ver §3). | Documentación obligatoria | S | Crear ficha + README + `resumen.html` |
| 178 | vault | Enlace roto Rho Zero (ver §3). | Salud del vault | S | Corregir |
| 179 | automatización | 248 cambios sin commit. | Riesgo de perder trabajo; el auto-push no corre sin commit | S | Commit o `vault-commit` |

## 4. Propuestas de mejora

| nº | área | propuesta | beneficio | coste/riesgo | fuente | recomendación |
|---|---|---|---|---|---|---|
| 180 | Servicio | Ficha de oferta única «Mila para clínicas dentales» con `oferta-central` (precio, garantía, qué incluye). Comprobar antes si ya existe `Servicios/<Nombre> - Oferta.md` (no comprobado). | Precio y garantía por escrito | Obliga a decidir | CEO | aplicar |
| 181 | Captación | Caso «NeoZeler es cliente cero» con datos reales de Mila (citas, tiempos, coste, sin datos personales); solo borrador. | Prueba social sin cliente | Pocas conversaciones = cifras flojas | CEO | probar |
| 182 | Flujo vault | Cada lunes `nz ceo pulso` y máximo 3 decisiones anotadas en una sesión; 17 proyectos congelados con motivo. | Congelar con razón, no por olvido | Un ritual más | CEO | probar 4 semanas |
| 183 | Estructura | En `Contexto NeoZeler` marcar cada dato «firme» o «propuesta» con fecha (nota `mixto`, solo añadir). | Agentes leen datos fiables | Bajo | CEO | aplicar |
| 184 | Skills | `n8n-skills` (repo `czlonkowski/n8n-skills`, ~53,2K instalaciones según [claudemarketplaces](https://claudemarketplaces.com/skills/czlonkowski/n8n-skills)) y la oficial `n8n-io/skills` ([skills.sh](https://www.skills.sh/n8n-io/n8n/n8n%3Acreate-skill), 490 estrellas); las cifras no cuadran entre directorios. Solape: skill `n8n-automation`. Leer su SKILL.md antes de instalar (es texto que el agente obedece). | Mejor setter/workflows | Skill ajena | investigador | probar (solo leer) |
| 185 | Skills | Skill de SEO local (Google Business Profile, citas, NAP), ~1,8K instalaciones, [lista](https://claudeskills.info/best/seo-skills/); nombre de repo no confirmado. Solapa `searchfit-seo`. | Útil para clínicas | No verificada | investigador | descartar hasta ver el repo |
| 186 | Servicio | Piloto de «demo web personalizada por clínica» con aprobación humana antes de enviar. Precedentes anecdóticos: [pipeline n8n](https://dev.to/azeem_shafeeq/i-built-an-ai-agent-that-finds-clients-builds-their-website-emails-it-automatically-2jg6). Riesgos: correo no solicitado (LSSI/RGPD) y marca ajena. | Vender webs con demo | Legal | investigador | probar sin enviar |

## 4B. Apuestas atrevidas

Ronda de reto: CEO se auto-retó como CTO escéptico; CTO no retó las del CEO esta noche. Sin repetir apuestas de informes previos.

| nº | idea | por qué es atrevida | experimento ≤1 día | riesgo y reversión | coste | apuesta |
|---|---|---|---|---|---|---|
| 187 | **Agente de consulta para gestorías** (RAG: busca en documentos antes de responder y cita la fuente) | Contra el consejo de no empezar por un chatbot; RAG en 18 % de rivales, servicios profesionales × formación = 0 (estudio 10-nov) | 10 FAQs públicas de la AEAT + 20 preguntas; medir citas correctas | Respuesta fiscal errónea (legal); no sale del sandbox. Punto débil: qué pasa si el documento cambia | unos € (sin medir) | 3 · guardar |
| 188 | **Precio = % del coste de la recepcionista** + calculadora pública | 10 de 115 rivales publican precio | Hoja con datos falsos y 3 tamaños de clínica; ver si cae en 150-300 €/mes + setup | Precio que no cubre voz/WhatsApp; no publicarlo. Sueldo sin confirmar (INE) | 0 € | 2 · probar en sandbox |
| 189 | **Administradores de fincas**: incidencias por WhatsApp → parte de avería con prioridad | Nicho ausente del estudio | 20 incidencias inventadas; medir clasificación | Sin ninguna conversación real, solo mide nuestro guion | unos € (sin medir) | 4 · guardar hasta hablar con 5 |
| 190 | **Agente nocturno «poda de contexto»** (Go + haiku en Zorin): lee uso de skills y tamaño de rules, propone recortes en `00_Meta/Panel/maquina/`; nunca edita | Se vigila solo el harness | Ejecutarlo una vez a mano sobre copia de `~/.claude/rules` | Solo crea una nota; se borra | ~0,05 €/noche | 3 · probar en sandbox |
| 191 | **Hook que se corrige solo**: al corregir Haytham, apunta borrador en `COMMON_MISTAKES.md`; tercera reaparición se propone como regla dura | Cierra el bucle de errores | 20 correcciones simuladas en repo sandbox | Ruido; por defecto escribe en `.borrador`, `git checkout` revierte | ~0 € | 4 · probar en sandbox |

Precedentes (investigador, sin confirmar, blogs con resultados autodeclarados): [AutoDream](https://finisky.github.io/en/claude-code-auto-dream), [bucles que se auto-mejoran (Osmani)](https://addyosmani.com/blog/self-improving-agents/), [bucle de 12 h con cortacircuitos](https://dev.to/gentic_news/how-a-12-hour-autonomous-claude-code-loop-built-a-full-stack-dog-tracker-2c4), [autopilot que se para por coste](https://dev.to/bokuwalily/let-claude-code-improve-itself-unattended-an-autopilot-that-uses-cost-to-stop-runaways-5e76). Recomendación común: solo proyectos propios y sin push, correos ni edición de webs de noche.

## 5. Novedades de internet (20-nov)

- Claude Code (fuente de tercero [havoptic](https://www.havoptic.com/releases/claude-code/2026/11), consultada hoy; sin confirmar en el [changelog oficial](https://code.claude.com/docs/en/changelog)): 2.1.319 (6-nov) permisos y tareas MCP en segundo plano; 2.1.323 (12-nov) Code Mode experimental; 2.1.328 (18-nov) modo auto por defecto en sesiones interactivas; 2.1.329 (19-nov) `/tasks` muestra programadas.
- Listas para mirar: [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills), [anthropics/skills](https://github.com/anthropics/skills), [roundup Firecrawl 27-oct](https://firecrawl.dev/blog/best-claude-code-skills). Skills de Go y ventas: nada fiable. Obsidian (`julianobarbosa/claude-code-skills`, `zot24/skills`): baja prioridad, ya hay vault y MCP.
- Diseño 2026 (blogs de proveedores, opinión): tipografía protagonista y fuentes variables, scroll-driven animation ya estándar, 3D solo si aporta ([Webflow](https://webflow.com/blog/web-design-trends-2026), [Clay](https://clay.global/blog/web-design-guide/web-design-trends)). Sin herramienta nueva de diseño con evidencia.

## 6. Lo que NO se hizo / límites

- No se aplicó nada ni se movió ningún archivo. No se paró el timer ni se tocó `syslog`.
- Búsquedas en modo standard, resultados flojos; sin modo extended por el límite semanal de uso. skills.sh por tema: no consultado.
- Verifiqué yo: disco, tamaño de `syslog`, timer activo, runs programados, estados de `01_Projects`, ausencia de ficha de Ingecons. Cifras del CTO (tamaños de arranque, hooks, Zorin, token) y del investigador no re-medidas por mí. Token OAuth sin verificar.
- No re-medí huérfanas ni enlaces rotos con `vault-salud`; no comprobé si existe la ficha de oferta del nº 180. Rondas de reto CEO↔CTO incompletas.

## 7. Siguiente paso

Haytham marca por nº qué se aplica. **Primero 165 (disco, hoy).** Tocan settings, hooks, entorno o borran datos (sesión aparte con permiso): 165, 166, 167-169 (CLAUDE.md), 170, 171, 172, 173, 175, 176, 190, 191.

Límites activados: ninguno (≈25 llamadas, 3 agentes).

