---
title: "Sesión - 2026-08-09 - skill-improver sobre skills de marketing"
date: 2026-08-09
type: meta/sesion
proyecto: "[[02_Areas/NeoZeler/NeoZeler - MOC|NeoZeler]]"
tags:
  - sesion
aliases: []
origen: mixto
---

# Sesión — 2026-08-09: skill-improver sobre skills de marketing

> [!abstract] Resumen
> Se instaló `trailofbits/skills` (auditado antes de instalar) y se corrió su skill `skill-improver` sobre las ~363 skills de marketing/GTM instaladas (gtm-*, coldiq-*, coldout-*, aimc*/aimcs-*, plugin marketing-skills), en 12 lotes paralelos en background + una pasada de mop-up automatizada para el problema sistémico de referencias rotas.

## Contexto
Continuación de la investigación `[[03_Resources/Investigaciones/claude-code-ecosystem-2026/2026-08-08_landscape|Ecosistema Claude Code 2026]]`. Su recomendación #3 era auditar/podar las ~400 skills instaladas antes de sumar más. Esta sesión ejecuta esa recomendación sobre el subconjunto de marketing/GTM.

## Qué se hizo
- Instalado marketplace `trailofbits/skills` + 4 plugins (`skill-improver`, `agentic-actions-auditor`, `supply-chain-risk-auditor`, `git-cleanup`), tras auditar el repo (URLs de API legítimas, `allowed-tools` bien acotado, sin patrones de exfiltración).
- Instalado también `plugin-dev@claude-plugins-official` (dependencia de `skill-improver` para el agente `skill-reviewer`).
- Confirmado que `kepano/obsidian-skills` y `coreyhaines31/marketingskills` ya estaban instalados vía el marketplace `claude-code-skills` (= `alirezarezvani/claude-skills`) — no se duplicaron.
- Lanzados 12 agentes en paralelo (background) sobre lotes de ~30 skills cada uno, aplicando la rúbrica de `skill-improver` (crítico: frontmatter/YAML/refs rotas; mayor: descripción sin "Use when...", voz incorrecta, >500 líneas sin `references/`; menor: estilo).
- Tras detectar un problema sistémico de referencias rotas en el pack `gtm-*`, se construyó un script Python de arreglo automático por coincidencia única de nombre de archivo (búsqueda de basename en todo el árbol `gtm-*`; solo reescribe si hay exactamente 1 candidato) en dos pasadas.

## Decisiones tomadas
- No instalar las ~26 skills de seguridad de bajo nivel de Trail of Bits (Rust/C/DWARF/YARA/smart contracts) — no encajan con el perfil del usuario (Obsidian/PARA + NeoZeler, no ingeniería de seguridad).
- Arreglos automáticos solo cuando el candidato es inequívoco (1 solo archivo con ese nombre en todo el árbol); referencias con 0 o 2+ candidatos se dejaron intactas y reportadas, para no fabricar contenido ni adivinar mal.

## Aprendizajes (para futuras sesiones)
- **El pack `gtm-*` (autor LeadMagic/gtm-skills) fue escrito para una jerarquía de carpetas por categoría** (`outbound/cold-email-strategy/...`, `skills/founder-led/...`, etc.) **que no coincide con la instalación real, plana** (`~/.claude/skills/gtm-*`). Esto rompe referencias cruzadas entre skills hermanas en gran escala (cientos de rutas). No es un bug puntual — es un desajuste estructural entre cómo el autor organiza el repo origen y cómo Claude Code instala skills sueltas. Si se instalan más colecciones grandes de terceros, vale la pena escanear este mismo patrón antes de asumir que las skills funcionan igual que en el repo origen.
- **14 skills `aimc-market-*` no tenían frontmatter YAML en absoluto** (ni `name` ni `description`) — invisibles para el enrutador de Claude Code, nadie las habría podido invocar nunca. Esto no se detecta navegando el listado de skills disponibles (que solo muestra las que sí tienen frontmatter válido); solo aparece auditando archivo por archivo.
- **~81 referencias rotas en `gtm-using-gtm-skills` son huérfanas de verdad** (apuntan a un índice maestro, perfiles de "expertos" y scripts de instalación que nunca se instalaron) — es contenido que el autor documentó pero nunca empaquetó, no arreglable por renombrado. Si se usa esta skill como guía del repo completo, tener en cuenta que buena parte de sus referencias no resuelven.
- El fix automático por "basename único en todo el árbol" fue seguro y rápido (326 referencias arregladas en 2 pasadas) precisamente porque el pack usa nombres de archivo muy específicos (autor-concepto.md) que rara vez colisionan — no generalizar esta técnica a colecciones con nombres de archivo genéricos (`overview.md`, `template.md`) sin antes comprobar la tasa de ambigüedad.
- Los subagentes de Task no pueden escribir archivos de "informe" en `~/.claude/jobs/*/tmp/reports/` (bloqueado por política del harness) — deben devolver hallazgos como texto en su resultado; el orquestador (sesión principal) es quien persiste si hace falta.

## Balance final
- ~363 skills auditadas (315 sueltas + 48 del plugin marketing-skills).
- Frontmatter/YAML crítico arreglado: 14 skills `aimc-market-*` (sin frontmatter) + ~6 con YAML inválido (`coldiq-design-director`, `coldiq-design-stack`, `gtm-citation-harvesting`, etc.).
- Descripciones sin "Use when..." arregladas: ~10 (aimcs-*).
- Referencias rotas arregladas: ~200 por los agentes de lote (recorte quirúrgico o repunteo manual) + 326 por el script automático de basename único = más de 500 referencias corregidas en total.
- Huérfanas reales sin arreglar (archivo nunca existió): ~247, concentradas en `gtm-using-gtm-skills` (81) y una larga cola de 1-11 por skill en el resto del pack `gtm-*` — contenido nunca escrito por el autor original, no un bug de instalación.
- 1 skill vacía detectada (`coldiq-clay`, solo `.DS_Store`, sin `SKILL.md`) — reportada, no arreglada (no se puede fabricar contenido).

## Próximos pasos
- Decidir si vale la pena escribir el contenido faltante de las ~247 referencias huérfanas (mayormente en `gtm-*`) o dejarlas así — son enlaces muertos dentro de las skills, no rompen su funcionamiento básico.
- `coldiq-clay` — **hecho**: carpeta vacía eliminada (2026-08-09).

## Adenda — 2026-08-09: segunda pasada sobre el resto de skills sueltas
Tras cerrar la pasada de marketing, se corrió `skill-improver` sobre las **143 skills sueltas restantes** en `~/.claude/skills/` (no-marketing), en 5 lotes paralelos. Se decidió NO extender esta pasada a las ~1563 skills que viven dentro de plugins de terceros (ecc, engineering-skills, c-level-agents, etc.) — coste/escala desproporcionados, queda pendiente como decisión aparte si se quiere abordar.

**Resultado:**
- ~63 descripciones reescritas al patrón "Use when..."
- 3 frontmatter/YAML rotos arreglados: `antigravity-design-expert` (delimitador YAML mal formado), `brooks-test` (description truncada a mitad de frase), `copywriting-psychologist` (description era el placeholder sin rellenar)
- 2 correcciones de voz (2ª persona → imperativo/3ª persona)
- 7 problemas estructurales reportados sin arreglar (decisión del usuario pendiente, no se fabricó contenido):
  - `learned` — carpeta vacía sin SKILL.md
  - `linear-claude-skill` — 9 archivos (scripts/docs) referenciados que nunca se instalaron
  - `monopoly/patterns` — subskill huérfana, su skill padre `monopoly` no existe
  - `brooks-test` — depende de una carpeta `_shared/` del repo origen (`brooks-lint`) que no se instaló
  - `crossframe-casebook` — depende de un suite (`crossframe`/`crossframe-suite`) que no se instaló
  - `business-analyst`, `data-storytelling`, `debugger`, `haskell-pro`, `recsys-pipeline-architect`, `statsmodels` — referencian archivos individuales (`resources/implementation-playbook.md`, `references/interfaces.md`, etc.) que nunca se copiaron con la skill
- 6 skills >500 líneas sin fragmentar, reportadas: `advogado-criminal`, `agent-evaluation`, `agent-memory-systems`, `hyperframes-producer`, `sexual-health-analyzer`, `shopify-apps`, `convex`

**Aprendizaje nuevo**: el patrón de "referencia a un archivo compañero que nunca se instaló" no es exclusivo del pack `gtm-*` — aparece disperso en skills de autores distintos (`brooks-test`, `crossframe-casebook`, `linear-claude-skill`). Parece ser un problema genérico de cómo estas colecciones empaquetan/instalan skills que dependen de carpetas hermanas o compañeras, no algo propio de un solo autor.

**Balance combinado de ambas pasadas**: ~500 skills auditadas, cientos de referencias/descripciones/frontmatter arregladas, ~13 problemas estructurales identificados y documentados para decisión manual futura.

## Relacionado
- [[03_Resources/Investigaciones/claude-code-ecosystem-2026/2026-08-08_landscape|Ecosistema Claude Code 2026]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
