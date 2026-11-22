---
type: informe
status: pendiente-revision
origen: maquina
date: '2026-11-16'
---

# Revisión nocturna 2026-11-16

> [!resumen] En cristiano
> Hoy no había nada que mover de la raíz (0 archivos movidos). Lo más urgente: el disco está al **96 %** (20 GB libres; hace un día estaba al 81 %) y el vault lleva desde el 13-nov sin commit (181 cambios). Hay 8 hallazgos de harness (nº 110-117), 7 propuestas (nº 118-124) y 6 apuestas atrevidas (nº 125-130). Te toca decidir: qué se limpia del disco (nº 110) y si se prueba el piloto de setter/reactivación (nº 118-119).

## 2. Raíz ordenada

| Origen | Destino | Deshacer |
|---|---|---|
| (ninguno) | (ninguno) | — |

Sin mover, con motivo:
- `Sin título.canvas` y `Sin título 1.canvas` (2 bytes, vacíos): no clasificables por regla. Probablemente borrables; decide Haytham.
- El ZIP de 290 MB que avisó el informe de ayer ya está en `99_Assets/Documentos/` (alguien lo movió; `.gitignore` ya trae `*.zip`).
- `docs/` ya no existe en la raíz y los `.glb` sueltos tampoco (en `99_Assets/3d/` hay `.glb`, `.obj`, `.mtl`). Git los marca borrados/sin commit: esta tarea no los movió (nº 117).
- `git status --short`: 181 entradas, igual que antes de esta fase.

## 3. Estado del vault (solo propuestas)

| Prioridad | Hallazgo | Acción propuesta | Riesgo |
|---|---|---|---|
| Alta | Vault sin commit desde 2026-11-13 20:30 (181 cambios sin guardar). | Revisar por qué no se confirma (nº 111). | Bajo |
| Media | `02_Areas/NeoZeler/Estrategia/Enfoque web de la competencia.md` pesa 177 KB (único >60 KB). | Dividir por secciones, solo aditivo (es nota humana). | Medio |
| Media | `00_Inbox/` con 2 notas: `2026-10-13_1223_preparacion-con-carlos`, `Plan futuro de aqui 3 años`. | Haytham las clasifica. | — |
| Baja | 208 archivos en `00_Meta/Sesiones/`; sin medir cuántos no enlazan a su proyecto. | Medir con script. | — |
| — | Enlaces rotos, huérfanas, duplicados, estados mezclados: **no re-medidos** esta noche (ver informe 2026-11-15, 72 destinos rotos y estados mezclados siguen sin decidir). | — | — |

## 3B. Auditoría del harness

Medido: arranque ≈ 41 KB (global 11,2 + vault 27,8 + MEMORY 1,9). `rules/` 119-152 KB en disco (carga por `paths`, no medido). `claude` 2.1.323. `sync-gemini --check`: **al día** (nº 90 resuelto). Skills: 50 usos en 30 días, 38 `diseno-central`, 60 de 63 activas sin uso (poda: **2026-12-04**).

| nº | tipo | hallazgo y evidencia | impacto | esfuerzo | recomendación |
|---|---|---|---|---|---|
| 110 | punto ciego | Disco `/` al 96 % (425/468 GB). `~/Descargas` 46 GB (`Comprimidos` 21, `Per3sona3Relo3ad` 18, 3 copias de Isaac 4,8), `.cache/uv` 9,8 + `.local/share/uv` 7, Papelera 5, `.cache/pip` 3,4, playwright 2,2, puppeteer 1,3; `~/.var` 105 GB, `~/Games` 40, `.wine` 27, `.config` 15 (sin desglosar). | Riesgo de que fallen builds, auto-push y tareas | S | Con permiso: vaciar Papelera (5 GB), `uv cache clean` + `pip cache purge` (~13 GB, se regeneran), quitar 2 copias de Isaac (3,2 GB). Los juegos (39 GB) los decide Haytham. Script Go `nz cto disco` con aviso al 90 %. |
| 111 | punto ciego | Último commit del vault 13-nov; 181 cambios sin commit; el auto-push no está guardando (causa sin confirmar). | Pérdida de cambios si falla el disco | S | Revisar el mecanismo de auto-commit; script `vault-commit` (ya propuesto, nº 60). |
| 112 | automatización | `~/.claude/projects` 1,6 GB, 13 carpetas de transcripciones sin límite. | Disco | S | Job semanal en Go que borra >45 días con `--dry-run` por defecto y tras comprobar que el cierre nocturno ya extrajo lo útil. Destructivo: pedir permiso. |
| 113 | recorte | `~/.claude/vectordb-venv` 5,9 GB para ~178 notas (probablemente torch/CUDA; contenido no verificado). | 5 GB de disco | M | Probar en sandbox ONNX pequeño o índice en Go+SQLite; comparar 20 consultas reales. |
| 114 | hook | Arranque 41 KB sin candado: si cambia un `paths` de `rules/` el coste sube sin aviso. | Tokens | S | Binario Go `guard-arranque` que falle si pasa de 45 KB; correr en cierre nocturno. |
| 115 | punto ciego | Tokens pegados en el chat quedan en claro en `~/.claude/projects/*.jsonl` y `uso-*.jsonl`; permisos de esa carpeta sin verificar. | Riesgo de credenciales | S | Escáner Go semanal de patrones de clave (solo rutas, nunca valores) + `chmod 700`. |
| 116 | recorte | 17 hooks Go de 2,3-7 MB (`check-mcps` 7,1 MB), un proceso por evento. | Disco y arranques | M | Un solo binario `hook` con subcomandos; migrar uno a uno. |
| 117 | punto ciego | `docs/` (con `borrador-config/`) y `.glb` de la raíz figuran borrados en git; origen sin confirmar. | Pérdida si no estaban copiados | S | Confirmar que `docs/` tiene copia (git la conserva: `git restore docs`). No se tocó. |

Siguen abiertos de ayer (no se repiten): nº 89 (logs de coste sin escribirse desde el 13-nov), 91-93 (permisos de tareas programadas, variables de ahorro, plugins de cuenta). El investigador confirma en el [changelog oficial](https://code.claude.com/docs/en/changelog) (2.1.325, leído 16-nov) que las tareas programadas piden permiso antes de skills con `allowed-tools`/hooks salvo `Skill(nombre)` en `permissions.allow`: refuerza nº 91.

**Ahorro de tokens estimado**: sin medir. Cifra real: arranque 41 KB. El CTO estima ~6 KB/turno en la apuesta nº 128 (sin medir).

**Candidatos a script/hook (Go)**: `nz cto disco` (110), `vault-commit` (111), job de poda de transcripciones (112), `guard-arranque` (114), escáner de secretos en transcripciones (115), binario único `hook` (116).

## 4. Propuestas de mejora

| nº | área | propuesta | beneficio | coste/riesgo | fuente | recomendación |
|---|---|---|---|---|---|---|
| 118 | Servicio | Setter-como-servicio con prueba de 14 días: Mila en el WhatsApp de 1 clínica o inmobiliaria | Ya está construido; el cliente lo prueba él mismo | Coste de WhatsApp/IA en la prueba; política de Meta sobre bots sin confirmar | CEO | probar |
| 119 | Servicio | Reactivación de clientes dormidos (lista antigua de contactos de la pyme), vendida por citas recuperadas | Fácil de entender y medir | RGPD/consentimiento (consultar gestor); tasa de respuesta sin medir | CEO | probar (piloto) |
| 120 | Producto | Licencia de Laya Leads a otras agencias | — | Desvía el foco; TopLeads ya cubre la idea sin demanda validada | CEO | descartar ahora; vender a mano 2-3 listas (100-200 €, cifra sin medir) para medir interés |
| 121 | Servicio | «Cerebro de la empresa» (RAG tipo vault para manuales/FAQs de pymes) como ejemplo propio | Hueco del estudio (RAG solo 18 % de rivales) | Venta lenta; datos sensibles | CEO | probar solo con caso propio |
| 122 | Skills | `emil-design-eng` (emilkowalski/skills, 452 K instalaciones) | Diseño de interacción | Solapa con `impeccable`/`diseno-central`. `web-design-guidelines` **ya la tenemos** (duplicado: descartar) | [skills.sh](https://skills.sh) (16-nov) | probar tras leer su SKILL.md |
| 123 | Skills | `improve-codebase-architecture` (mattpocock/skills), skills de Go (lista [BehiSecc](https://github.com/BehiSecc/awesome-claude-skills)), `cold-email` (coreyhaines31/marketingskills) | Revisión en Go; cold email | Una skill es texto que el agente obedece: leer SKILL.md; cifras de instalaciones de agregadores se contradicen; solapa con perfil GTM | skills.sh, claudemarket.ai (16-nov) | probar uno por vez |
| 124 | Flujo | Patrón de agente nocturno que abre PR (autoimprove, night-shift) y una persona fusiona; nunca push directo (el vault hace auto-push) | Mejora sin riesgo | No se sabe cuánta gente los usa | [Addy Osmani](https://addyosmani.com/blog/self-improving-agents/) (16-nov) | probar en repo de prueba |

## 4B. Apuestas atrevidas

| nº | idea | por qué es atrevida | experimento ≤1 día | riesgo y reversión | coste | apuesta |
|---|---|---|---|---|---|---|
| 125 | **Pago solo por cita agendada, sin setup** | Cambia 1.000+ € de setup por riesgo propio | Escribir la oferta en una página y enseñarla a 5 clínicas conocidas | Citas falsas o canceladas; mínimo 10 citas/mes y cláusula de cancelación. Sin precedente hallado en España | sin medir | 4 · probar |
| 126 | **Publicar el coste real de Mila** (datos de `resumen.html`) como marketing | Solo 10 de 115 rivales publican precio | Un post en LinkedIn con los números reales | Que copien o parezca barato; se borra el post | 0 € | 2 · probar |
| 127 | **Llamar con voz de IA propia** a 10 negocios («soy una IA») | Hueco de voz (26 % de rivales) y la demo es la prueba | 3 llamadas a conocidos con permiso | LSSI/consentimiento y mala imagen | sin medir | 5 · guardar (solo con permiso explícito) |
| 128 | **Contexto bajo demanda**: CLAUDE.md del vault (28 KB) en núcleo de 4 KB + hook `UserPromptSubmit` en Go que inyecta solo la sección pertinente | Toca la capa base de todos los agentes | Copia del vault en sandbox, 20 peticiones reales, medir tokens y reglas respetadas | Perder una regla dura sin aviso; volver al original (copia en `_backups`) | 0 €; ~6 KB/turno sin medir | 3 · probar en sandbox |
| 129 | **Mila se evalúa sola**: job nocturno puntúa cada conversación y prueba cambios de prompt en sombra | Usa producción como banco de pruebas | 30 conversaciones exportadas y anonimizadas, puntuadas con gpt-4.1-mini | Fuga de datos personales (RGPD); anonimizar antes de que salga nada, no guardar texto; apagar cron | ~1-3 €/mes | 4 · probar en sandbox |
| 130 | **Backup con restauración probada** semanal (restic en Zorin de `~/.claude` y vault) | Un backup que nunca se restauró no es backup | Una restauración pequeña midiendo RAM en Zorin | Zorin con poca RAM; parar el cron | 0 € | 2 · probar |

Reto realizado: el CEO y el CTO rompieron las apuestas de ayer (no se cruzaron entre sí en esta ronda). Resumen:
- **Demo por prospecto (nº 105)**: el coste escala con 291 leads, mide curiosidad y no demanda, y puede tocar RGPD. Mejor generarla solo tras respuesta del prospecto.
- **Auditor de clínicas 29-49 € (nº 106)**: no paga el soporte, atrae al comprador barato y compite con la auditoría gratuita; mejor como gancho gratis a cambio de reunión.
- **Zorin como CI (nº 109)**: poca RAM (riesgo de tumbar Laya Trader y el CRM), 181 cambios sin commit lanzarían ejecuciones sobre notas, y exige credenciales de GitHub en un servidor doméstico. Alternativa: `pre-push` local.
- **Banco de pruebas del harness (nº 108)**: 50 usos/mes, 38 de una sola skill = muestra mínima; sin criterio de «mejor» se mide ruido. Versión viable: medir solo tokens de arranque.

## 5. Novedades de internet (16-nov)

- Claude Code 2.1.325 (13-nov) es la última entrada del [changelog](https://code.claude.com/docs/en/changelog): tareas programadas con permiso de skills, `sandbox.autoAllowBashIfSandboxed`, arreglos de reglas deny/ask (`Read(./.env)` tras un `cd`, hueco en comandos compuestos). Solo se leyó el 8 % de la página; cambios de hooks sin confirmar.
- Skills: ranking de [skills.sh](https://skills.sh): frontend-design, ui-taste, web-design-guidelines, emil-design-eng; mattpocock/skills. No aparecen skills de SEO, n8n ni Obsidian nuevas.
- Bucles de mejora con evaluación: GEPA, Hermes self-evolution, [Fireworks](https://fireworks.ai/blog/self-improving-agent) (cifra de proveedor). Piden tareas de prueba y métrica; no montar de noche sin revisión humana.
- Demos por prospecto: [Ciela AI](https://ciela.ai/blogs/personalized-demo-at-scale-for-agencies) (vendedor, 12-ene); sin caso independiente; la mejora de conversión del vendedor no está confirmada.
- Precio de agentes en España: [javadex.es](https://www.javadex.es/blog/agentes-ia-atencion-cliente-pymes-espana-precios-2026): 5.000-12.000 € de implantación + 50-300 €/mes (blog comercial). Sin precedente de pago por cita. La tarifa de WhatsApp API cambió (mensajes de servicio gratis hasta 30-sep-2026): verificar la actual en Meta.
- Diseño 2026: 3D con propósito, titulares enormes, fuentes variables, scrollytelling con opción de pausa ([Figma](https://www.figma.com/resource-library/web-design-trends/)). Fuentes de marketing; sin datos de librerías concretas.

## 6. Lo que NO se hizo / límites

- No se movió nada ni se aplicó ninguna propuesta.
- No se re-midieron enlaces rotos, huérfanas ni duplicados del vault (solo hallazgos del día).
- No se desglosó `.config` (15 GB) ni `~/.var` (105 GB); no se verificó el contenido de `vectordb-venv` ni los permisos de `~/.claude/projects`.
- Investigación web de una fuente por punto, sin leer ningún SKILL.md; no se consultó `list_task_runs`.
- La ronda de reto fue contra apuestas previas, no CEO↔CTO entre sí.
- Numeración: el CTO usó 60-65 en su informe; aquí están renumeradas a 110-116.

## 7. Siguiente paso

Haytham marca por nº qué se aplica. Tocan `settings.json`, hooks, skills o borran datos (esta tarea no puede aplicarlos; sesión aparte con permiso): 110, 111, 112, 113, 114, 115, 116, 122-124, 128.

Límites activados: ninguno (≈25 llamadas, 3 agentes).

