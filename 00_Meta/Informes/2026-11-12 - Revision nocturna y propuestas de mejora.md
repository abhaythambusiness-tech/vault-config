---
type: informe
status: pendiente-revision
origen: maquina
date: '2026-11-12'
---

# Revisión nocturna y propuestas de mejora (2026-11-12)

> [!resumen] En cristiano
> Se ordenó la raíz del vault: 4 modelos 3D fueron a `99_Assets/3d/` y una carpeta de código suelta fue a `~/Proyectos/archive/`. No se borró nada. El vault está sano (593 notas), pero hay 66 enlaces rotos, 44 notas huérfanas y estados de proyecto escritos de varias formas. Seis agentes investigaron mejoras; casi todas las fuentes son blogs de proveedores, así que las cifras orientan, no prueban. A ti te tocan estas decisiones: qué CRM es el vigente (#4), si se fija un nicho y se congelan proyectos (#23-#24) y qué ajustes de Claude Code se activan (#1-#6). Marca por número.

## 1. Raíz ordenada

| Origen | Destino | Deshacer |
|---|---|---|
| `beacon.glb` | `99_Assets/3d/beacon.glb` | `mv 99_Assets/3d/beacon.glb .` |
| `brain_orb.glb` | `99_Assets/3d/brain_orb.glb` | `mv 99_Assets/3d/brain_orb.glb .` |
| `crystal-core.glb` | `99_Assets/3d/crystal-core.glb` | `mv 99_Assets/3d/crystal-core.glb .` |
| `satellite_dish_drone.glb` | `99_Assets/3d/satellite_dish_drone.glb` | `mv 99_Assets/3d/satellite_dish_drone.glb .` |
| `ssh@192.168.0.100mp-crm-test/` (código TypeScript, tests y n8n) | `~/Proyectos/archive/ssh-192.168.0.100mp-crm-test-20261112/` | `mv ~/Proyectos/archive/ssh-192.168.0.100mp-crm-test-20261112 ./"ssh@192.168.0.100mp-crm-test"` (desde la raíz del vault) |

- Ningún `.md` enlazaba los .glb. Tres notas (`Estructura del Vault`, dos sesiones) citan el nombre de la carpeta solo como texto, así que no se rompe ningún enlace.
- Sin commit. `git status` muestra los .glb como nuevos en `99_Assets/3d/` y los archivos de la carpeta como borrados de la raíz.
- Nada quedó sin mover. `.capturas/` es carpeta de sistema permitida y se dejó.

## 2. Estado del vault (solo propuestas, nada aplicado)

Alta prioridad:
- **Estados de proyecto sin norma.** Conviven `en-progreso` y `en_progreso`, entre otros (9 estados distintos según `nz ceo pulso`). Acción: fijar lista cerrada (decisión abierta de `CLAUDE.md` §7). Riesgo bajo.
- **`00_Meta/Estado de Proyectos.md`** está fechado 2026-10-26. Acción: regenerarlo desde el frontmatter. Riesgo bajo.
- **`Taller-Bravo`** figura como completado, pero el `CLAUDE.md` lo tiene como decisión abierta. Acción: decidir (archivar, documentar o dejar). Solo Haytham.
- **Dos CRM a la vez.** La memoria dice que `minicrm-go` sustituye a Neozeler CRM; `Contexto NeoZeler` y `Estado de Proyectos` aún dan Neozeler CRM como vigente. Acción: confirmar y corregir. Solo Haytham.

Media:
- **66 enlaces rotos.** La mayoría son marcadores `{{nombre}}` de plantillas (no son errores) y enlaces en sesiones de agosto y `04_Archive/Vault OS`. Reales: `00_Meta/Dashboard.md` tiene 6 enlaces con `\` pegado al nombre (`INGECONS\`, `Cauce - Master Command Center\`, `Dropshipping - MOC\`, `NeoZeler - MOC\`, `03_Resources/README\`, `04_Archive/README\`). Acción: quitar la barra. Riesgo muy bajo.
- **44 huérfanas.** 18 son `04_Archive/Memecoin-LSTM`; el resto son prompts 3D de Abisal Drill, retros (`Los Apuntes de Liyo`, `Dashboard Command AI`), `03_Resources/` sueltas y `00_Meta/cosas que hacer.md`. Acción: índice aditivo en `04_Archive/README.md` y en los MOCs. Riesgo bajo.
- **Sin frontmatter:** `00_Meta/API.md`, `00_Meta/GEMINI.md`, `04_Archive/Memecoin-LSTM/GEMINI.md` (`CLAUDE.md` y `GEMINI.md` de la raíz son excepciones). **Sin `type`:** 14 notas (lista: Panel/humano/tareas, 2 sesiones, 6 de Memecoin-LSTM, Crypto-Copy-Bot spec, INGECONS guion, Reto-30 idea original, 3 de 03_Resources). **Sin `origen`:** 11. Acción: etiquetar con `etiquetar_origen.py` en simulacro. Riesgo bajo.

Baja:
- **Duplicados:** `Retro.md` (Liyo y Dashboard Command AI) y `Guia - Skills y reglas por fase.md` (5 proyectos) se repiten por diseño; `Dashboard.md` y `README.md` tienen homónimos en otras carpetas. Solo vigilar con wikilinks por ruta.
- **Notas largas (>500 líneas):** `Enfoque web de la competencia.md` (1.050), y los `5 - Backend Schema.md` de Reto-30, Comanda Viva y TopLeads (esperable en esquemas). Dividir solo la primera.
- **Panel:** `00_Meta/Panel/humano/tareas.md` pesa 23 bytes; casi no se usa.
- **Sesiones:** 170 notas; hubo 4 el 11-nov. Todas las de noviembre llevan `proyecto`.

## 3. Propuestas de mejora

Fiabilidad: las filas 1-5 salen del changelog oficial; el resto, de blogs o agregadores. Sin cifras de resultado independientes.

| Nº | Área | Propuesta | Beneficio | Coste/riesgo | Fuente | Recomendación |
|---|---|---|---|---|---|---|
| 1 | Claude Code | `permissions.blockWritesOutsideWorkingDirectories`: Write/Edit no escriben fuera de las carpetas de trabajo | Un agente no toca `~/.claude` ni `.ssh` por error | Una línea; puede bloquear ediciones legítimas entre repos (se arregla con `--add-dir`) | [Changelog oficial](https://code.claude.com/docs/en/changelog) v2.1.314, 2026-10-30 | Probar una semana |
| 2 | Claude Code | `permissions.denyInsteadOfPrompting` solo para subagentes y ejecuciones sin supervisión | Subagentes no se quedan parados esperando un sí | Si falta una regla `allow`, la tarea falla sin avisar; antes afinar con `/fewer-permission-prompts` | Changelog v2.1.319, 2026-11-06 | Probar |
| 3 | Tokens | `CLAUDE_CODE_SUBAGENT_EFFORT=low` en `env` | Ahorro directo en subagentes | Un subagente de arquitectura razona menos (se puede subir por agente) | Changelog v2.1.316, 2026-10-31 | Aplicar |
| 4 | Claude Code | Hooks con `onFailure: "block"` en `guard-destructive` y `guard_proyecto` | Hoy, si el script se rompe, no protege | Un bug bloquea todo; no confirmado que valga para hooks de comando (solo Agent SDK) | Changelog v2.1.317, 2026-11-03 | Probar tras tests de `hooks/tests/` |
| 5 | Claude Code | Actualizar Claude Code (arreglos de seguridad de permisos en v2.1.321, 2026-11-09) y probar `/skill-doctor` (mide skills sin uso y su coste de contexto) | Recorte de contexto con 149 skills activas; encaja con la revisión del 4-dic | Versiones citadas vía agregador [havoptic](https://www.havoptic.com/releases/claude-code/2026/11), sin confirmar en la oficial | [implicator.ai](https://www.implicator.ai/anthropic-claude-code-skill-doctor-context-audit/) | Aplicar |
| 6 | Claude Code | Aviso: Opus 4.8 modo rápido se retira el 2026-11-30; skills en `.claude/skills` dentro de `~/.claude/plugins` ya no cargan (v2.1.321) | Evitar sorpresas | Ninguno | Changelog v2.1.316 / v2.1.321 | Revisar |
| 7 | Tokens | Menos MCP y más CLI; medir con `token-optimizer` (candidatos: Figma, Bloom) | Sesiones más baratas | Cifras de ahorro de vendedores (hay un test de junio casi en empate) | [Checkly](https://www.checklyhq.com/blog/mcp-vs-cli-token-efficiency/), [DEV](https://dev.to/pickuma/cli-vs-mcp-which-tool-interface-actually-works-for-ai-coding-agents-1894) | Probar midiendo |
| 8 | Skills | `n8n-io/skills` (oficial) o `czlonkowski/n8n-skills`: elegir una línea y compararla con las 4 skills n8n actuales | Fuente oficial para flujos de clientes | Solape; repos sin verificar | [vibeindex](https://vibeindex.ai/plugins/n8n-io/skills/n8n-skills) (2026-07-26, agregador) | Probar en carpeta aparte |
| 9 | Skills | `design-extract`: saca tokens de diseño de una web vieja de pyme | Útil para `local-business-rebuild` | Estrellas no verificadas | [awesome-claude-design-skills](https://github.com/zhuyansen/awesome-claude-design-skills) (10-nov) | Probar |
| 10 | Skills | `grill-me`, `shadcn/improve`, `stitch-skills`, `logo-design-skill` | Preguntas que afinan planes, revisión de código shadcn, logos de cliente | `grill-me` puede duplicar `agent-debate`/`before-you-build` | [claudemarketplaces](https://claudemarketplaces.com/) (12-nov) | Probar solo `logo-design-skill` y `shadcn/improve` |
| 11 | Skills | `unslop`, `obsidian-second-brain`, `ECC`, `awesome-design-md`: descartar | Evita duplicar o chocar con la regla humano/máquina | — | Investigador y CTO | Descartar |
| 12 | Skills | Leer `awesome-claude-code` una vez al mes en la revisión del 4-dic, sin instalar a ciegas | Mantener el radar | Instalar desde listas abiertas es el riesgo | [ClaudeFast](https://claudefa.st/blog/tools/resources/awesome-claude-code) | Aplicar como lectura |
| 13 | Diseño | Fuentes variables (un archivo WOFF2) como norma técnica; serifas expresivas y texto animado solo si lo permite la identidad aprobada | Menos peso de carga | Opinión de blogs comerciales | [Made Good Designs](https://madegooddesigns.com/web-typography-trends-2026/), [Creative Bloq](https://www.creativebloq.com/design/fonts-typography/breaking-rules-and-bringing-joy-top-typography-trends-for-2026) | Aplicar la parte técnica |
| 14 | Diseño | Claude Design (`/design`, vista previa, abril-agosto 2026) | Explorar ideas rápido | Exige sesión claude.ai; se solapa con hallmark | [blakecrosley](https://blakecrosley.com/blog/claude-code-design-skill) (25-ago) | Probar solo para explorar |
| 15 | Diseño | Sistemas de componentes nuevos | — | Sin evidencia fiable de algo que supere shadcn, 21st o magicui | — | Descartar |
| 16 | Operaciones | Lista cerrada de `status` y tabla de estado generada desde el frontmatter | Un solo estado por proyecto | Tocar notas humanas solo de forma aditiva | `nz ceo pulso` 2026-11-12; `CLAUDE.md` §7 | Aplicar |
| 17 | Operaciones | Elegir CRM vigente (minicrm-go vs Neozeler CRM) y corregir Contexto, Estado y Estructura | Evita agentes con datos viejos | Decisión tuya | Memoria 2026-11-07 | Decidir |
| 18 | Operaciones | Ritual del lunes (15 min): nota `origen: maquina` con pulso, parados y decisiones pendientes | Todo en una nota | Bajo; probar 4 semanas | `nz coo`, `small-business:monday-brief` | Aplicar |
| 19 | Operaciones | Script semanal de enlaces rotos y duplicados (solo informe) | La tarea ya se repite (§0.12) | Bajo | Auditoría de esta noche | Aplicar |
| 20 | Operaciones | Índice aditivo de huérfanas en `04_Archive/README.md` | Dejan de estar huérfanas sin mover nada | Bajo | Auditoría | Aplicar |
| 21 | Operaciones | Medir horas por tarea 4 semanas y usar `nz coo checklist` | Hoy no hay capacidad semanal real | Exige disciplina | Contexto NeoZeler §6 | Aplicar |
| 22 | Operaciones | Bases nativas de Obsidian (1.15) para una vista nueva; compartir con Sam solo una carpeta, no el vault | Sin plugin extra; Sam ve lo suyo sin ver `API.md` | Dos sistemas con Dataview | [Changelog Obsidian](https://obsidian.md/changelog) 1.15 (2026-11-02) | Probar una vista |
| 23 | Estrategia | Elegir 1 nicho + 1 oferta y congelar el resto. Propuesta del CEO: mantener NeoFlow AI (núcleo), NeoZeler Web, Mini CRM Go, INGECONS; congelar NeoZeler HQ y TopLeads; pausar Comanda Viva y Grid64; sacar Reto 30, trading y Roblox de NeoZeler | Foco: hoy hay 17 proyectos en-progreso | Demanda sin validar; ninguna cifra es independiente | Contexto NeoZeler; `nz ceo pulso` | Decidir |
| 24 | Estrategia | Antes de construir, 10 conversaciones con dentales o inmobiliarias | Validar demanda barato | Tiempo | Informe CEO | Aplicar |
| 25 | Servicios | Recepcionista de voz + recordatorios WhatsApp para clínicas dentales; inmobiliario × voz y gestorías con RAG como a probar | Voz es solo 26 % de rivales (estudio propio); hueco ≠ demanda | Rivales grandes (Vodafone, CloudTalk) | [Automatizator](https://automatizator.es/), [CloudTalk](https://www.cloudtalk.io/es/agentes-de-voz-con-ia-para-pymes/) | Probar con 1 piloto de pago |
| 26 | Precios | Subir el setup de la línea general de 1.000-1.100 € a 1.500-2.500 € y publicar precio (solo 10 de 115 rivales lo hacen) | Mercado ES cobra 1.500-12.000 € | Menos cierres posibles | [Upliora](https://www.upliora.es/blog/cuanto-cuesta-implementar-ia-pyme-espana-por-tipo-proyecto-2026), [Flowmatic](https://flowmatic.es/automatizacion/cuanto-cuesta-automatizar/) | Probar con 3-5 propuestas |
| 27 | Precios | Mensualidad obligatoria mínima (150-300 €/mes) con tope de IA y WhatsApp; exceso facturado | Ingreso recurrente: 5 clientes × 200 € = 1.000 €/mes | Definir bien el tope | [Forge](https://forge.so/articles/ai-automation-agency-pricing), [Codewave](https://codewave.com/feeds/blog/ai-automation-agency-pricing) | Aplicar |
| 28 | Costes | Pasar WhatsApp y minutos de voz al cliente (coste + margen o su cuenta); control de IA con caché, modelo barato y tope por cliente | Un cliente de mucho volumen no se come el margen | Parece letra pequeña si no se explica | [Quickreply](https://www.quickreply.ai/whatsapp-automation/whatsapp-business-api-pricing), [Dupple](https://dupple.com/learn/how-to-reduce-llm-api-costs) | Aplicar |
| 29 | Costes | n8n autoalojado en Zorin para clientes pequeños | Ahorra 20-50 €/mes por cliente | Punto único de fallo; revisar licencia Community | [Dupple](https://dupple.com/learn/n8n-pricing) | Probar tras revisar licencia |
| 30 | Captación | Kit Digital como agente digitalizador (bonos con IA) | La pyme paga menos | Sin convocatoria nueva confirmada en fuente oficial (la 5.ª cerró el 30-jun-2025); importes que se contradicen | [TeamSystem](https://teamsystem.es/magazine/kit-digital-2026/), [España Digital](https://espanadigital.gob.es/lineas-de-actuacion/programa-kit-digital) | Probar, verificando antes en Red.es y BOE |
| 31 | Captación | Auditoría gratis con entregable fijo de 1 página en 48 h y tope mensual; añadir módulo GEO local ("que la IA te recomiende") | Menos fricción de entrada | Sin datos de conversión; no copiar cifras de competidores | [Ciela](https://ciela.ai/blogs/how-to-get-ai-agency-clients-with-a-free-audit) (29-abr-2026) | Aplicar |
| 32 | Captación | Cold email y LinkedIn en España | Canal barato | Duda legal real: LSSI art. 21 exige consentimiento o relación previa; multa leve citada 600 € | [Legiscope](https://www.legiscope.com/blog/lssi-ce-ley-servicios-informacion.html), [Fieldfisher](https://www.fieldfisher.com/es-es/locations/spain/insights/bases-datos-empresariales) | Consultar con el gestor antes |
| 33 | Producto | Bots de WhatsApp solo para tareas concretas (citas, reservas, seguimiento), nunca "asistente general" | Meta prohíbe desde 2026-01-15 chatbots de IA de propósito general en la API | Estado actual de la política sin confirmar | [respond.io](https://respond.io/es/blog/whatsapp-general-purpose-chatbots-ban) | Aplicar como precaución |
| 34 | Servicios | Cobro por resultado (base fija + variable por cita) | Alinea con el cobro por % | Disputas de atribución y caja irregular | [Lotus Libre](https://lotuslibre.com/blog/outcome-based-ai-pricing/) | Descartar por ahora |

## 4. Novedades relevantes de internet

- Claude Code v2.1.314-v2.1.321 (30-oct a 9-nov): bloqueo de escrituras fuera de carpetas, `denyInsteadOfPrompting`, esfuerzo de subagentes, compactación en reposo, arreglos de seguridad. Fuente principal: [changelog oficial](https://code.claude.com/docs/en/changelog); el agregador [havoptic](https://www.havoptic.com/releases/claude-code/2026/11) da versiones y fechas, sin confirmar contra la oficial.
- Obsidian 1.15 (2026-11-02) y 1.15.1 (2026-11-03): reordenación de filtros en Bases; los vaults compartidos no sincronizan ajustes por defecto. [Changelog](https://obsidian.md/changelog).
- Skills que suben: `grill-me`, `shadcn/improve`, `design-extract`, `logo-design-skill`. Las estrellas son mala señal: un análisis dice que un marketplace de un solo plugin hereda 380.416 estrellas de otro proyecto ([claudemarketplaces](https://www.claudemarketplaces.com/blog/claude-code-plugin-ecosystem-data-2026)). Hay quejas de que las skills gastan decenas de miles de tokens al inicio ([aiweekly](https://aiweekly.co/alerts/claude-code-skills-waste-23k-tokens-per-session), cifra de una sola auditoría).
- WhatsApp: mensajes de servicio de pago desde 2026-10-01 y respuestas de IA de Meta desde 2026-08-01 salen de una sola fuente secundaria ([Wati](https://www.wati.io/en/blog/whatsapp-business-api-pricing-changes-2026-what-meta-s-two-new-fees-actually-cost-you/)): sin confirmar.

## 5. Lo que NO se hizo / límites

- No se borró, renombró ni reorganizó nada salvo los 5 movimientos de §1. No se hizo commit ni push. No se tocaron settings, hooks, skills, MCPs ni plugins.
- Los hallazgos de §2 son solo propuesta: nada se etiquetó, enlazó ni corrigió.
- Fuentes: casi todo son blogs de proveedores, sin estudios independientes. Fechas exactas de muchas webs sin confirmar. No se abrieron BOE, Red.es ni las páginas oficiales de n8n, Meta o Anthropic. No se verificaron estrellas en GitHub.
- El agente COO no tuvo buscador web (solo `curl`): las prácticas de equipos pequeños con Obsidian en 2026 quedan sin verificar. El CTO leyó solo 100.000 de 1,2 millones de caracteres del changelog oficial.
- El CEO no leyó `Estado de Proyectos.md`; el COO sí lo vio (fechado 2026-10-26).
- Los precios en dólares de las guías no sirven como precio para pymes españolas sin calibrar. Consejo fiscal o de ayudas: consultar al gestor.

## 6. Siguiente paso

Haytham marca por nº qué se aplica (por ejemplo: «1, 3, 5, 16, 17, 20»). Los nº 17, 23, 30 y 32 son decisiones tuyas antes de tocar nada.

