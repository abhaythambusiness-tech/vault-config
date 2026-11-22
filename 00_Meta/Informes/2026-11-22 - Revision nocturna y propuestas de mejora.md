---
type: informe
status: pendiente-revision
origen: maquina
date: '2026-11-22'
---

# Revisión nocturna 2026-11-22

> [!resumen] En cristiano
> **Buena noticia: el log gigante ya se rotó (syslog 1,4 MB), pero su copia vieja `syslog.1` sigue ocupando ~104 GB; borrarla (con tu permiso, sudo) libera casi un tercio del disco** (nº 220). El temporizador `comandai-sync` sigue fallando (~2.250 líneas de error en la última hora, nº 221). No se movió ningún archivo: la raíz ya estaba limpia. Hay 7 hallazgos de harness (nº 220-226), 10 propuestas (213-216, 227-233) y 6 apuestas atrevidas (217-219, 234-236). Nada se aplicó.

## 2. Raíz ordenada

Movimientos: **ninguno** (0 archivos). Sin mover: `Sin título.canvas` y `Sin título 1.canvas` (2 bytes, vacíos, no clasificables) y `Compartido/` (carpeta del MCP `compartido`). `git status --short`: 267 entradas; último commit 13-nov.

## 3. Estado del vault (solo propuestas)

| Prioridad | Hallazgo | Acción propuesta | Riesgo |
|---|---|---|---|
| Alta | 267 cambios sin commit; último commit 13-nov (refuerza nº 179/226). | Commit manual o `vault-commit` en Go. | Bajo |
| Media | Enlace roto aún sin corregir (4.ª noche, nº 178): `Sesiones/2026-11-14 - Obsidian tema Rho Zero legible (cierre automatico).md` → `[[2026-11-13 - Obsidian - plugin Rho Network y tema oscuro (sesión 8f81f004)]]` (la real lleva «:»). | Corregir el enlace (nota `maquina`). Con tu OK lo hago. | Bajo |
| Media | Estados fuera de lista en `01_Projects/`: `draft` 1, `borrador` 2, `en-construccion` 1, `implementado-verificado` 1, `propuesta` 1, `propuesto` 1 (7 notas). | Aprobar la lista cerrada de §7 del CLAUDE.md. | Bajo |
| Baja | `00_Inbox/`: `2026-10-13_1223_preparacion-con-carlos.md` y `Plan futuro de aqui 3 años.md` sin clasificar. | Haytham clasifica. | — |
| Baja | `Contexto NeoZeler` (10-nov) dice Zorin «.100»; el global dice .101 (nº 225). | Unificar IP. | Bajo |

No re-medí huérfanas ni enlaces rotos con `vault-salud` (último informe 16-nov).

## 3B. Auditoría del harness

Medido hoy: `/` 73 % (122 GB libres, 323 GB usados). `/var/log/syslog` 1,4 MB; `syslog.1` 105.988 MB; `syslog.2.gz` 83 MB, `.3.gz` 135 MB, `.4.gz` 59 MB. `journalctl --disk-usage` 3,9 GB. Claude Code instalado 2.1.323. `sync-gemini --check`: al día. Skills: 75 invocaciones/30 días, 43 de `diseno-central`; 70 de 81 activas sin uso; poda **2026-12-04** (aún no toca). Tareas programadas: `cierre-nocturno-sesiones` y esta, ambas activas y con última ejecución correcta. Zorin sano (CTO por SSH: disco 47 %, 0 servicios fallidos, 5 contenedores doory healthy, `syslog.1` de Zorin 65 MB).

| nº | tipo | hallazgo y evidencia | impacto | esfuerzo | recomendación |
|---|---|---|---|---|---|
| 220 | punto ciego | `syslog.1` = 105.988 MB, ya rotado y sin escritura (`ls -la /var/log/syslog*`). Cierra parcialmente nº 192: falta el tope (`maxsize 1G`, `rotate 2` en `/etc/logrotate.d/rsyslog`) para que no vuelva a pasar. | ~104 GB libres (73 % → ~50 %) | S | `sudo rm /var/log/syslog.1` con permiso (irreversible; el contenido es el ruido de comandai-sync); añadir `maxsize`. |
| 221 | regla | `comandai-sync.timer` sigue `active`; 2.249 líneas en `journalctl --user -u comandai-sync.service --since "1 hour ago"` (nº 193/152). Causa sin leer (`sync-panel.sh`, IP .100 vs .101). | Origen del log de 104 GB | S | `systemctl --user disable --now comandai-sync.timer` o `OnUnitInactiveSec=5min`; corregir IP. |
| 222 | recorte | journald 3,9 GB sin límite (nº 194). | Disco | S | `SystemMaxUse=500M` (sudo). |
| 223 | recorte | Arranque: `~/.claude/CLAUDE.md` 11,5 KB + vault `CLAUDE.md` 31,1 KB; `rules/` 186 KB: `skills-frecuentes.md` 25,3 (histórica), `skills-seleccion-global.md` 24,5, `diseno.md` 24,5, `web.md` 19,8. **No medí** cuáles cargan siempre y cuáles por `paths`. | Hasta ~7-12k tokens/sesión (bytes÷3,5, no medido en sesión) | S-M | Mirar `paths:`; mover la histórica a `reference/`; pasar a `reference/` la §0.10 y la lista de proyectos del CLAUDE.md del vault (refuerza 167-169, 195). |
| 224 | punto ciego | Instalada 2.1.323; última 2.1.330 (20-nov, changelog oficial). Cambios que tocan hooks: `rm` sobre raíz/home pide permiso, modo auto ignora reglas amplias tipo `Bash(pnpm dlx *)` (2.1.328), error de hook MCP solo bloquea con `"onFailure": "block"`, hooks prompt aceptan `model: haiku` (2.1.330). | Hooks propios podrían dejar de bloquear | S | Actualizar y revisar los hooks PreToolUse en sesión aparte (refuerza 196, 206). |
| 225 | regla | Dos fuentes dicen IP distinta de Zorin (.100 en `Contexto NeoZeler`, .101 en el global). | Scripts fallan (nº 221) | S | Unificar. |
| 226 | automatización | 267 cambios sin commit, último commit hace 9 días; sin aviso si falla una tarea programada (refuerza 175, 179, 199). | Trabajo sin respaldo | S | `vault-commit` en Go + aviso en Panel. |

**Ahorro de tokens estimado**: 223 ≈ 7-12k tokens por sesión (sin medir en sesión real); 220 libera disco, no tokens.

**Candidatos a script/hook (Go)**: guarda de disco/logs (nº 212 previo), `vault-commit` (226), `nz vault-cambios` (229), medidor de coste por skill (230), medidor de contexto `nz ctx` (211 previo).

## 4. Propuestas de mejora

| nº | área | propuesta | beneficio | coste/riesgo | fuente | recomendación |
|---|---|---|---|---|---|---|
| 213 | Servicio | **Mila Voz**: atiende y agenda llamadas perdidas en clínicas. | Ataca el hueco de voz (26 % de ocupación entre rivales según estudio del vault 10-nov, orientativo) | RGPD y consentimiento al grabar; coste de minutos sin medir | CEO | probar |
| 214 | Captación | Informe «teléfono sin respuesta»: llamar a 10 clínicas tier A en horario de comida y anotar si contestan; enviar el dato solo a cada clínica. | Abre conversación con dato propio | Parece intrusivo; llamar es acción externa, necesita permiso | CEO | probar con 10 llamadas |
| 215 | Precio | Cuota baja + 15-25 € por cita confirmada (hipótesis, sin confirmar), dentro del piloto 200. | Riesgo cero para el cliente | Discutir qué es «cita real»; margen incierto | CEO | probar |
| 216 | Operación | Formulario Tally único de accesos previos (WhatsApp Business, agenda, Google Business). | Evita semanas esperando claves | Ninguno relevante | CEO | aplicar |
| 227 | Recorte | `rules/` por `paths` con índice de 1 KB (ver 223). | Alto en tokens | M; medir primero | CTO | probar |
| 228 | Estructura | Pasar tareas programadas a 30 días y comprobar que siguen (2.1.329: muchas guardadas hay que reprogramarlas; hoy corren). | Evita que mueran | S | changelog oficial | aplicar |
| 229 | Script (Go) | `nz vault-cambios`: resumen por carpeta de cambios sin commit, humano/máquina y posibles secretos antes del auto-push. Solo informa. | Evita fugas | S | CTO | probar |
| 230 | Hook | `PostToolUse` que registra el coste real de cada skill, para decidir la poda del 4-dic con datos. Añadir el perfil GTM (214 skills) al informe de uso. | Poda informada | S-M | CTO | probar |
| 231 | Skills | `czlonkowski/n8n-skills` (25,1K instalaciones en 7 skills, [skills.sh](https://www.skills.sh/czlonkowski/n8n-skills)). Solapa el MCP oficial de n8n. Leer SKILL.md antes. | Posible mejor n8n | Duplica; skill = texto que el agente obedece | investigador | descartar salvo prueba |
| 232 | Skills | `bitbonsai/mcpvault/obsidian` (1,6K, [skills.sh](https://www.skills.sh/bitbonsai/mcpvault/obsidian)). Solapa nuestro MCP `obsidian-vault`. | — | Duplica | investigador | descartar |
| 233 | Skills | `grill-me` (mattpocock/skills, 1,6M instalaciones, skills.sh): te interroga sobre un plan; solapa `superpowers:brainstorming`. | — | Duplica | investigador | descartar |

## 4B. Apuestas atrevidas

Ronda de reto: cada agente atacó sus propias ideas (línea «ataque»); no hubo cruce CEO↔CTO por el tope de agentes. Sin repetir 187-191 ni 208-212.

| nº | idea | por qué es atrevida | experimento ≤1 día | riesgo y reversión | coste | apuesta |
|---|---|---|---|---|---|---|
| 217 | **Demo web personalizada por clínica**: tomar la web real de un lead de Laya Leads, generar en minutos un rediseño con Mila integrada y mandar el enlace. | Vende con una demo propia por prospecto. Ataque: el rediseño sale genérico y lo que vende es Mila, no la web. | 3 leads tier A, en local, sin enviar nada. | Marca ajena sin permiso; borrar la carpeta. | sin medir | 4 · probar en sandbox |
| 218 | **Notas del vault que se actualizan solas**: binario Go que lee sesiones y Mini CRM y escribe borradores `origen: maquina` en carpeta aparte. | Cambia el vault de archivo a panel vivo. Ataque: duplica `nz ceo pulso` y `vault-salud`; nadie lee los borradores. | Regenerar solo el bloque de pulso de Estado de Proyectos en sandbox. | Ruido; se revierte con git. | sin medir | 3 · guardar |
| 219 | **Nicho gestorías/asesorías × voz con precio por resultado**. | 0 rivales según el estudio, lo que no prueba demanda. Ataque: compran por relación personal. | Contar en Laya Leads gestorías de Málaga con teléfono y sin reserva online; guion de 1 página. | Nicho sin presupuesto; se descarta sin coste. | sin medir | 3 · probar en sandbox |
| 234 | **Vigía nocturno en Zorin**: cron que lanza `claude -p` de solo lectura y deja un parte en `00_Meta/Panel/maquina/`. | Agente que trabaja de noche sin ti. Ataque: bucle que gasta tokens sin aviso. | Una noche en carpeta sandbox, lista fija de comandos y tope 50k tokens. | Ejecuta algo destructivo; desactivar el timer. | céntimos/noche (sin medir) | 3 · probar en sandbox |
| 235 | **Memoria que se cura sola**: job semanal que propone fusionar/borrar memorias como diff, nunca aplica solo. | Memoria viva. Ataque: fusiona dos memorias y pierde el «porqué». | Copia de la memoria en scratchpad y revisar el diff a mano. | Borrar una lección no obvia; restaurar copia. | ~0 | 4 · probar en sandbox |
| 236 | **Evaluación automática de skills**: 10 prompts fijos por skill, con y sin ella, juzgados con rúbrica. | Poda por calidad medida. Ataque: el juez es el mismo modelo; 10 muestras son ruido. | 3 skills (`diseno-central`, `ponytail`, `nuevo-proyecto`), ~30 ejecuciones. | Conclusiones falsas; borrar resultados. | 2-5 € (estimación CTO) | 3 · guardar |

Precedentes (todo contenido de terceros): no hallé agente nocturno que cure su propia configuración documentado. Piezas sueltas: [Auto Dream](https://www.mindstudio.ai/blog/what-is-claude-code-autodream-memory-consolidation-3) (blog, sin confirmar), [`/doctor prompt-audit`](https://flaviocopes.com/claude-code-prompt-audit.md), [claude-memory-curator](https://raw.githubusercontent.com/stark-ai-de/agent-skills/main/skills/claude-operations/claude-memory-curator/SKILL.md), [diagnóstico con Claude sin interfaz](https://nikiforovall.blog/ai/2026/08/23/headless-claude-code-in-agent-instructions-diagnoser.html) (23-ago-2026). Demos por prospecto: [Seatext](https://seatext.com/seatext-ai-personalization), [Supademo](https://supademo.com/blog/personalized-outbound-demos-at-scale) (cifras del propio vendedor; un aviso de IndieHackers dice que puede parecer invasivo).

## 5. Novedades de internet (22-nov)

- Claude Code: la última versión es la **2.1.330** (20-nov), no existe 2.1.331 ([changelog](https://code.claude.com/docs/en/changelog); solo leído el principio). `/loop` y tareas recurrentes duran 30 días (las creadas antes siguen en 7); `/update-config` ~13k tokens en vez de 93k; subagentes con notas cortas; mejor caché con MCP en Code Mode.
- [skills.sh](https://skills.sh) (solo pestaña All Time, sin descripciones; cifras cambian por captura): hyperframes (1,6M, vídeo), agent-browser (1,6M, solapa scrapling), design-mobile-apps (1,6M), reddit-automation (1,5M), SEO `calm-north/seojuice-skills/audit` (6,2K; un escaneo Socket avisó riesgo medio en una de las skills SEO), ventas `louisblythe/sales-skills` (51,7K en 122 skills; solapa perfil GTM). Go: `samber/cc-skills-golang` (ya propuesta en 204).
- Diseño 2026: tipografía grande expresiva, fuentes variables, texto en movimiento, 3D solo si resuelve algo ([Webflow](https://webflow.com/blog/web-design-trends-2026), [Clay](https://clay.global/blog/web-design-guide/web-design-trends); genéricos, sin fecha de noviembre).
- Clínicas dentales: recordatorios WhatsApp a 24 h y 2 h con enlace de confirmar, y recall; dicen bajar los impagos de cita del 15-25 % al 5-8 % (cifras de vendedores, sin confirmar): [ChatDaddy](https://chatdaddy.tech/blog/whatsapp-for-dentists), [dev.to](https://dev.to/scalelogix_ai/ai-automation-for-dental-practices-what-actually-works-in-2026-5ekc).

## 6. Lo que NO se hizo / límites

- No se aplicó nada ni se movió ningún archivo; no se tocó syslog, timers, settings, hooks ni skills; no se corrigió el enlace roto (nota `maquina`, pendiente de tu OK).
- Investigación en modo estándar, 11 búsquedas; changelog solo el principio; pestaña skills.sh de 24 h no cargó. CMO y CFO no se lanzaron (tope de agentes: 3 usados).
- Verifiqué yo: disco, tamaños de `syslog*`, timer activo, estados de `01_Projects`, tamaños de reglas, uso de skills, tareas programadas. Cifras de Zorin (CTO por SSH) y del investigador/CEO no re-medidas. Dos llamadas Bash fueron bloqueadas por el clasificador del modo auto porque el hook `rtk` reescribe las entradas (nº 197 del informe anterior); una se repitió con éxito. No comprobé token OAuth ni huérfanas. Permisos de `~/.claude/reference/` revisados solo por modo (600 en los `.env`/json; carpeta `memecoin-bak-secretos` 700), sin leer valores.

## 7. Siguiente paso

Haytham marca por nº qué se aplica. **Primero 220 y 221** (liberar 104 GB y parar el log). Tocan sudo, settings, hooks o borran datos (sesión aparte con permiso): 220, 221, 222, 223, 224, 227, 228, 230, 234, 235.

Límites activados: ninguno (≈19 llamadas, 3 agentes).

