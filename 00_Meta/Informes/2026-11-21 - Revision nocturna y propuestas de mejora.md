---
type: informe
status: pendiente-revision
origen: maquina
date: '2026-11-21'
---

# Revisión nocturna 2026-11-21

> [!resumen] En cristiano
> **Urgente: `/var/log/syslog` pesa 106 GB y el temporizador `comandai-sync.timer` sigue fallando cada pocos segundos** (nº 192-193; refuerza 152 y 165). El disco bajó del 98 % al 74 % (alguien liberó espacio; no sé quién), pero sin tope de log vuelve a llenarse. No se movió ningún archivo: la raíz ya estaba limpia. Hay 8 hallazgos de harness (nº 192-199), 8 propuestas (nº 200-207) y 5 apuestas atrevidas (nº 208-212). Nada se aplicó.

## 2. Raíz ordenada

Movimientos: **ninguno** (0 archivos). Sin mover: `Sin título.canvas` y `Sin título 1.canvas` (2 bytes, vacíos, no clasificables) y `Compartido/` (carpeta del MCP `compartido`). `git status --short`: 259 entradas; último commit hace 7 días (`ec171be`).

## 3. Estado del vault (solo propuestas)

| Prioridad | Hallazgo | Acción propuesta | Riesgo |
|---|---|---|---|
| Alta | 259 cambios sin commit, último commit hace 7 días (refuerza nº 179). | Commit manual o `vault-commit` en Go. | Bajo |
| Media | Repos en `~/Proyectos` sin ninguna mención en `01_Projects/`, `02_Areas/` ni `04_Archive/`: `clinica-marbella-agente`, `hookdistill`, `foros-claude-code`, `estudio-mrr`, `agentes-ia-3d`, `ig-analytics` (tiene timer activo en systemd). `ingecons*` sigue sin ficha en `01_Projects/` (aunque se cita en 10 notas; nº 177). | Fichas o decidir archivar (regla vault §0.8). | Bajo |
| Media | Enlace roto sin corregir (nº 178): `Sesiones/2026-11-14 - Obsidian tema Rho Zero legible (cierre automatico).md` apunta a `...Obsidian - plugin Rho...`; la real lleva «:». | Corregir enlace (nota `maquina`). | Bajo |
| Media | Estados sin lista cerrada en `01_Projects/`: `propuesto`, `propuesta`, `implementado-verificado`, `en-construccion`, `draft`, `borrador` (contados hoy). | Aprobar la lista de §7 del CLAUDE.md. | Bajo |
| Baja | `00_Inbox/`: `2026-10-13_1223_preparacion-con-carlos.md` y `Plan futuro de aqui 3 años.md` sin clasificar. | Haytham clasifica. | — |

No re-medí huérfanas ni enlaces rotos con `vault-salud` (último informe 16-nov).

## 3B. Auditoría del harness

Medido hoy: `/` 74 % (119 GB libres); `syslog` 111.129.516.456 B (104 GB en disco), `syslog.1` 6,7 GB; Zorin sano (47 % disco, 0 servicios fallidos, según CTO por SSH). Claude Code instalado 2.1.323. `sync-gemini --check`: al día. Skills: 74 invocaciones en 30 días, 43 de `diseno-central`; poda **2026-12-04** (aún no toca). Tareas programadas: `cierre-nocturno-sesiones` y esta, ambas activas; la del 19-nov falló por límite semanal, la del 20-nov y esta fueron bien.

| nº | tipo | hallazgo y evidencia | impacto | esfuerzo | recomendación |
|---|---|---|---|---|---|
| 192 | punto ciego | `/etc/logrotate.d/rsyslog`: `weekly`, `rotate 4`, sin `maxsize` (CTO). `syslog` = 104 GB; el CTO estima ~17 GB/día (extrapolado de la cola; **no verificado**). En la cola hay ráfagas de `gnome-shell`, steam y Discord además de comandai-sync: causa mixta, sin probar. | Disco lleno en días | S | `maxsize 1G`, `rotate 2` (sudo, con permiso). Vaciar el log solo tras parar `rsyslog` (un `rm` con el fichero abierto no libera espacio). Antes, `awk '{print $3}'` sobre el log para ver quién escribe. |
| 193 | regla | `comandai-sync.timer` activo, `OnUnitInactiveSec=10s`, falla con `rsync error 255` contra Zorin (Zorin está sano; el fallo es de este lado, causa sin leer en `sync-panel.sh`). Seguía fallando a las 04:08. | Ruido de ~5.000 líneas por cada 40 MB | S | `systemctl --user disable --now comandai-sync.timer` o `OnUnitInactiveSec=5min` + `StartLimitBurst`; corregir IP .100→.101 (nº 152). |
| 194 | recorte | `journalctl --disk-usage` = 3,9 GB, sin límite (CTO). | Disco | S | `SystemMaxUse=500M` en `journald.conf` (sudo). |
| 195 | recorte | `rules/skills-frecuentes.md` (25,3 KB) es «histórico» según el CLAUDE.md global; la vigente es `skills-seleccion-global.md` (23,7 KB). `rules/` suma 177 KB. **No verificado** qué `rules/` cargan siempre y cuáles solo por `paths`. | Hasta ~7k tokens/sesión | S-M | Mirar `paths:` de cada una; mover la histórica a `reference/` con puntero. Refuerza 167-169 (el CLAUDE.md del vault sigue en 30,7 KB). |
| 196 | regla | Changelog oficial 2.1.326-330 (16-20 nov): permisos Bash más estrictos, `rm` sobre raíz/home/carpeta de trabajo pide aprobación, `git` que descarta cambios puede bloquearse; en Code Mode un error de PreToolUse ya no bloquea salvo `"onFailure": "block"`; hooks de tipo prompt aceptan alias de modelo (`haiku`). Versiones 7-15 nov no leídas. Instalada: 2.1.323. | Hooks propios podrían dejar de bloquear o empezar a pedir permiso | S | Revisar los 10 hooks PreToolUse y actualizar en sesión aparte (refuerza 159/176). |
| 197 | punto ciego | Un hook externo (`rtk hook claude`) reescribe las llamadas Bash; hoy 2 llamadas mías se bloquearon en modo auto («a hook changed this call's input»). Modo auto no puede revisar entradas modificadas. | Fricción en tareas automáticas | S | Medir cuántos bloqueos genera y decidir si compensa. |
| 198 | recorte | `~/.claude` = 9,5 GB: `vectordb-venv` 5,9 GB, `projects` 1,9 GB, `plugins` 1,3 GB, `_backup-usar-20261103-200349` 69 MB, `skills-archivo` 169 MB. Sin git ni copia (nº 166). | Disco | S | Script Go: podar `projects/` a 30 días; borrar `_backup-usar-*` solo con permiso. |
| 199 | automatización | 259 cambios sin commit y auto-push que no corre sin commit (refuerza 179); sin aviso si una tarea programada falla (refuerza 175). | Trabajo sin respaldo | S | `vault-commit` en Go + aviso en Panel. |

**Ahorro de tokens estimado**: 195 (+167-169 aún sin aplicar) ≈ 7k + 4,4k tokens por sesión (bytes÷3,5; no medido en sesión real). Este informe mismo: arranque cargó contexto ~15 % de 1M.

**Candidatos a script/hook (Go)**: guarda de disco/logs (nº 212), rotador de logs (171), `vault-commit` (199), copia de `~/.claude` (166), poda de `projects/` (198), medidor de presupuesto de contexto (nº 211).

## 4. Propuestas de mejora

| nº | área | propuesta | beneficio | coste/riesgo | fuente | recomendación |
|---|---|---|---|---|---|---|
| 200 | Oferta | Piloto de pago de 30 días (~290 €, descontable del setup) en vez de «auditoría gratis + setup a 0 €». El precio es hipótesis del CEO, sin fuente. Enseñarlo a 3 clínicas conocidas. | Filtra curiosos | Menos respuestas al inicio | CEO | probar |
| 201 | Producto | Campaña única «reactivar pacientes dormidos» (>12 meses sin cita) sobre Mila, precio fijo. | Subida de precio a clientes | RGPD con datos de salud y plantillas de Meta sin verificar; consultar al gestor | CEO | probar (solo preguntar a una clínica) |
| 202 | Captación | Canal de socios (distribuidores de material, protésicos, gestorías dentales) con comisión del primer año; listar 10 en Málaga, hablar con 2. | Llegar a muchas clínicas con confianza | Depender de terceros | CEO | probar |
| 203 | Operaciones | Cronometrar la implantación del cliente cero (8 fases, horas) y sacar runbook con `demo-desde-ficha`. Falta el dato de «capacidad semanal real» (Contexto §6). | Fijar precio y cupo | Horas aproximadas | CEO | aplicar |
| 204 | Skills | `golang-how-to` (repo `samber/cc-skills-golang`), ~37,8K instalaciones en [skills.sh](https://skills.sh/samber/cc-skills-golang) (tercero: 30.887 al 5-ago, [skillselion](https://skillselion.com/skills/samber/cc-skills-golang/golang-how-to)); sub-skills de estilo, errores, tests. Encaja con la regla «scripts en Go». Leer su SKILL.md antes de instalar. | Mejor Go | Skill = texto que el agente obedece | investigador | probar |
| 205 | Skills | `cold-email` de `alirezarezvani/claude-skills` (588 instalaciones, [skills.sh](https://skills.sh/alirezarezvani/claude-skills/cold-email)) o de `coreyhaines31/marketingskills` (36K según [directorio tercero](https://claudemarketplaces.com/skills/coreyhaines31/marketingskills/cold-email), sin confirmar). Solapa el perfil GTM. | Posible mejora de copy | Duplica | investigador | descartar salvo prueba comparada |
| 206 | Harness | Hooks de tipo prompt con `"model": "haiku"` (2.1.330) para guards baratos. | Menos coste | Depende de actualizar | changelog oficial | probar tras actualizar |
| 207 | Estructura | Patrón «3 correcciones de la misma regla = hook» ya está en el global §4; precedente: [pro-workflow](https://www.mintlify.com/rohitg00/pro-workflow/concepts/self-correction-loop) (fecha sin confirmar). Sin acción nueva; solo confirma el enfoque. | — | — | investigador | descartar |

## 4B. Apuestas atrevidas

Ronda de reto: el CEO rompió sus propias apuestas; el CTO no retó las del CEO (limitado por cortacircuitos de agentes). Sin repetir 187-191.

| nº | idea | por qué es atrevida | experimento ≤1 día | riesgo y reversión | coste | apuesta |
|---|---|---|---|---|---|---|
| 208 | **Mila Lite**: Mila como plantilla clonable que el cliente se instala solo, cuota baja | Rompe el modelo de ~1.000 € de setup y abre soporte masivo | Clonar el workflow en n8n para un negocio ficticio y cronometrar hasta la primera respuesta correcta | Meta bloquea números nuevos o el soporte se come el margen; borrar el workflow | 0-5 € | 3 · probar en sandbox |
| 209 | **Clínica en 3D** con Mila de recepcionista como demo | El 3D rara vez aporta ([Webflow](https://webflow.com/blog/web-design-trends-2026), no reabierto) y pesa en móvil | Escena React Three Fiber + chat falso; medir peso, FPS móvil y reacción de 3 personas | Lento en móviles baratos; borrar carpeta. El CEO: un dueño compra citas, no gráficos | 0 € | 2 · guardar |
| 210 | **«Radar de tu zona»** (Spyder) como informe de 1 página con nota 0-100 de rivales | Convierte herramienta interna en producto | Radar «clínica dental + Málaga» y maquetar; faltan claves Firecrawl/Groq (nota parcial) | Nota arbitraria; scraping vs. términos de uso; no enviar nada. Casi igual que 106 | unos € (sin medir) | 3 · probar en sandbox |
| 211 | **Presupuesto de contexto con alarma**: binario Go `nz ctx` que cuenta bytes del arranque (CLAUDE.md global, vault, `rules/` sin `paths`) y avisa si pasa de ~35 KB; solo avisa, no bloquea | Convierte el recorte en un límite fijo, no en limpiezas puntuales | Copiar `~/.claude` a un temporal, mover `skills-frecuentes.md` y §0.10, comparar con `/context` | Perder una regla usada; revierte la copia (no hay git en `~/.claude`, nº 166). Ahorro 12-15k tokens/sesión, no verificado | 0 € | 4 · probar en sandbox |
| 212 | **Guarda de disco y logs en Zorin**: timer Go cada hora que lee `df`, `/var/log` y servicios fallidos por SSH de solo lectura; avisa por Panel/ntfy sobre 85 % o +5 GB/día | El disco llegó al 98 % el 20-nov y nadie avisó | Ejecutar en seco 24 h y comparar con el crecimiento real de `syslog` | Falsos avisos; `systemctl --user disable` del timer | 0 € | 5 · probar en sandbox |

Precedentes (todo contenido de terceros, fechas sin confirmar): [cc-self-audit.sh](https://dev.to/bokuwalily/how-claude-code-detects-its-own-weekly-rot-and-repairs-itself-4akb) (semanal, archiva sin borrar, no nocturno); [Claude Reflect](https://smithery.ai/skills/BayramAnnakov/claude-reflect). Agente nocturno puro de poda: **sin confirmar**.

## 5. Novedades de internet (21-nov)

- Claude Code, [changelog oficial](https://code.claude.com/docs/en/changelog) (leído hoy, solo 2.1.326-330): ver nº 196 y 206. `/update-config` baja de ~93k a ~13k tokens (2.1.326); `/loop` y tareas recurrentes duran 30 días (2.1.330); 2.1.329: la mayoría de tareas guardadas hay que reprogramarlas (revisar que las nuestras siguen; hoy corren).
- [skills.sh](https://skills.sh): top find-skills 4,5M, agent-browser 1,6M, grill-me 1,6M, frontend-design 1,1M, web-design-guidelines 887K, ui-ux-pro-max 463K (las dos últimas ya instaladas). Sin novedades de Obsidian, SEO, n8n ni ventas.
- Listas: [awesome-claude-skills (Composio)](https://github.com/ComposioHQ/awesome-claude-skills), [travisvn](https://github.com/travisvn/awesome-claude-skills); contenido por tema no revisado.
- Precios de mercado (blogs de proveedor, poco fiables): [Upliora](https://www.upliora.es/blog/ia-para-administradores-fincas-comunidades-propietarios-espana-2026) 4.000-9.000 € de proyecto para administración de fincas; [Famulor](https://www.famulor.io/es/industries/property-management) voz desde 130 €/mes. Ninguna agencia española con precio público para gestorías/fincas encontrada.

## 6. Lo que NO se hizo / límites

- No se aplicó nada ni se movió ningún archivo; no se tocó syslog, timers, settings, hooks ni skills. Tampoco se aplicó la sugerencia de hook de «Haytham corrige algo»: no hubo corrección humana, así que no se editó `COMMON_MISTAKES.md`.
- Investigación en modo estándar; changelog 7-15 nov y listas awesome por tema sin leer. CMO y CFO no se lanzaron (límite de agentes).
- Verifiqué yo: disco, tamaño de `syslog`, timer activo, runs programados, estados de `01_Projects`, ausencia de ficha de Ingecons. Cifras del CTO (rotación, journal, Zorin, 17 GB/día) y del investigador no re-medidas. No comprobé el token OAuth (nº 174) ni huérfanas.

## 7. Siguiente paso

Haytham marca por nº qué se aplica. **Primero 193 y 192 (log y timer).** Tocan settings, hooks, sudo o borran datos (sesión aparte con permiso): 192, 193, 194, 195, 196, 197, 198, 206, 211, 212.

Límites activados: ninguno (≈20 llamadas, 3 agentes).

