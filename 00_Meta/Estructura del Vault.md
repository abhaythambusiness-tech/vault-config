---
type: meta
status: activo
date: 2026-11-06
origen: mixto
tags: [meta, estructura, mapa]
---

# Estructura del Vault

> [!resumen] En cristiano
> El vault es una casa con **cinco habitaciones numeradas** (método PARA): `00` es el cuarto de máquinas (plantillas, sesiones, paneles), `01` lo que estás construyendo ahora, `02` lo que mantienes siempre, `03` lo que consultas y `04` el trastero. `99_Assets` guarda los archivos pesados (imágenes, PDFs, modelos). Lo demás (carpetas con punto, `docs/`, `graphify-out/`) es maquinaria de las herramientas: no se toca.
> Foto del 2026-11-06. Si cambia la estructura, actualizar esta nota (regla §0.5 del `CLAUDE.md`).

Ruta física: `/home/haytham/Documentos/vault/` (repo git con auto-push a `Haytham-Vault`). No es repo de código: el código vive en `~/Proyectos/<nombre>/`.

---

## 1. Vista de pájaro

```
vault/
├── 00_Inbox/          entrada sin clasificar            (1 archivo)
├── 00_Meta/           sistema del vault                 (179)
├── 01_Projects/       proyectos activos                 (247)
├── 02_Areas/          responsabilidades continuas       (43)
├── 03_Resources/      referencia reutilizable           (45)
├── 04_Archive/        descartado / histórico            (36)
├── 99_Assets/         binarios                          (154)
├── docs/              meta de Claude Code               (11)
├── graphify-out/      grafo regenerable (ignorar)
├── .agents/ .claude/  configuración de agentes          (13 / 7)
├── .obsidian/         ajustes de Obsidian
├── .token-optimizer/  métricas de tokens
└── (raíz)             CLAUDE.md, GEMINI.md, .mcp.json + archivos sueltos (ver §9)
```

Reglas de oro: no reorganizar PARA ni `99_Assets/`, `docs/`, `graphify-out/`, `taller-bravo/` sin petición explícita (`CLAUDE.md` §0.2). Crear notas dentro: sí.

---

## 2. `00_Inbox/` — entrada

Cosas por clasificar. Se vacía hacia `01`–`04` o `99_Assets/`.

| Elemento | Qué es |
|---|---|
| `2026-10-13_1223_preparacion-con-carlos.md` | Preparación de reunión |

---

## 3. `00_Meta/` — sistema del vault (179 archivos)

| Ruta | Contenido |
|---|---|
| `Dashboard.md`, `Dashboard - Proyectos de Software.md` | Paneles Dataview |
| `Estado de Proyectos.md` | Estado de cada proyecto (leer al trabajar en uno) |
| `Registro de Sesiones.md` | Índice del registro de sesiones |
| `Proyectos Pendientes a Futuro.md`, `cosas que hacer.md` | Pendientes |
| `Convencion Humano-Maquina.md` | Regla `origen: humano\|maquina\|mixto` |
| `Decision - Estructura del Vault (Debate Multi-Agente).md` | Por qué la estructura PARA actual |
| `Decision - Reparto de Tiempo NeoZeler vs Dropshipping.md` | Decisión de negocio |
| `Diseno - …` y `Plan - Sistema de Mejora Continua de Metodologias.md` | Diseño y plan del ciclo Ficha de Investigación → Retro |
| `API.md` | **Secreto**, ignorado por git. No copiar |
| `GEMINI.md` | Copia generada del `CLAUDE.md` (no editar a mano) |
| `Panel/` | Panel ComandAi: `humano/` (solo vía `scripts/panel.py`), `maquina/` (7 archivos regenerables), `README.md` |
| `Plantillas/` | 10 plantillas: Caso de Éxito, Cliente, Identidad de Proyecto, Onboarding Cliente IA, Propuesta, Proyecto, Servicio IA, Sesión, Nota Estándar, Simulador de WhatsApp |
| `Plantillas/Proyecto Software/` | Flujo de 6 documentos (`1 - PRD` … `6 - Plan de Implementacion`) + `00 - Flujo de Software`, `01 - Tipos de producto`, `Ficha de Investigacion`, `Retro de Proyecto`, `Paleta de Componentes` |
| `Sesiones/` | **135 notas** `YYYY-MM-DD - <tema>.md`, de 2026-08-08 a 2026-11-06 |

---

## 4. `01_Projects/` — proyectos (247 archivos)

Patrón: cada proyecto tiene una **ficha** `<Nombre>.md` en la raíz de `01_Projects/` y, si es grande, una **carpeta** `<Nombre>/` con sus documentos. Código real fuera, en `~/Proyectos/`.

### 4.1 Proyectos con carpeta

| Carpeta | Archivos | Qué es |
|---|---|---|
| `Dropshipping/` | 72 | E-commerce. Subcarpetas `00_Fuente` … `11_Plan de Accion` + `Producto/` (ver §4.2) |
| `Reto-30/` | 43 | App de Factory Training (Haytham y Pedro). 12 notas de negocio + `Software/` con PRD…Plan, borradores legales, prompts de imágenes |
| `TopLeads/` | 10 | Micro SaaS de leads (Laya Leads convertido) |
| `NeoZeler Web/` | 10 | Web de la agencia |
| `Comanda Viva/` | 10 | Menú QR + inventario para restaurantes |
| `Cauce/` | 9 | SaaS PMBOK |
| `Scraper Infoproductores/` | 9 | Scraper |
| `Los Apuntes de Liyo/` | 8 | Proyecto de apuntes |
| `Battle Royale/` | 7 | Torneo de estrategias de trading |
| `ComandAi/` | 7 | Panel / agentes |
| `Laya Trader/` | 7 | Bot de trading en papel |
| `Neozeler CRM/` | 7 | Embudo de venta de webs |
| `Abisal Drill/` | 6 (+`Prompts 3D/`) | Roblox, en pausa |
| `Scalper Memecoins/` | 6 | **Abandonado** |
| `Bot de Tendencia/` | 3 | Experimental |
| `Dashboard Command AI/` | 2 | `Ficha de Investigacion` + `Retro` |
| `Eventos Bolsa/`, `Mercados Laya/`, `Ultimo en Pie - Sabotaje/` | 1 c/u | Casi vacíos |

### 4.2 `Dropshipping/` por dentro

`00_Fuente` (1) · `01_Estrategia y Mentalidad` (2) · `02_Producto` (14) · `03_Tienda Shopify` (4) · `04_Marketing y Ads` (7) · `05_Postventa y Retencion` (4) · `06_Legal y Finanzas` (7) · `07_Casos y Herramientas` (4) · `08_Marca y Posicionamiento` (2) · `09_Analitica y Tracking` (1) · `10_Lanzamiento` (2) · `11_Plan de Accion` (10) · `Producto/` (12). Entrada: `[[Dropshipping - MOC]]`.

### 4.3 Fichas sueltas (sin carpeta)

`Abisal Drill`, `Barber-DF` (+ `Propuestas de mejora`), `Battle Royale`, `Bot de Tendencia`, `Comanda Viva`, `Dashboard Command AI`, `Embudo Mensualidades Web`, `Flujo de Software`, `Laya Leads`, `Laya Trader`, `Los Apuntes de Liyo`, `NeoFlow AI` (+ `Guion del Pitch`), `Neozeler CRM` (+ `Identidad Visual`), `NeoZeler Mundo`, `NeoZeler Web`, `NM Electroclima`, `RethinkbyIA`, `Roblox - Anomaly Extraction`, `Scalper Memecoins`, `Scraper Infoproductores`, `Starter SaaS`, `Taller-Bravo`, `TopLeads`, `Ultimo en Pie - Sabotaje`, `Voice-to-Vault`.

---

## 5. `02_Areas/` — áreas continuas (43 archivos)

### `NeoZeler/` — la agencia de IA para pymes
| Subcarpeta | Contenido |
|---|---|
| `NeoZeler - MOC.md` | Entrada del área |
| `Clientes/` | `INGECONS` (ficha, guion de grabación, script demo) |
| `Implementación IA/` | MOC, metodología de software a medida, sistema de ventas (tablero) |
| `Lanzamientos/` | 14 notas numeradas (visión, onboarding, webinar, oferta, SLO, captación, anuncios, nutrición, IA externa, informe, prompts, replay, Funnelabs 2.0, conversaciones) + MOC + decisiones abiertas |
| `Servicios/` | `Servicio - Software de Gestión Operativa a Medida` |
| `Marketing/`, `Nichos/` | **Vacías** |

### `Trading con 10 euros/`
`Trading con 10 euros - MOC.md` + 6 notas numeradas (mercado, lectura de gráficos, patrones, riesgo, playbook/diario, matemática) + `Sistema de Trading/` (`00 - Sistema`, `Dashboard`, `Diario/`, `Plantillas/Plantilla - Trade`, `Playbook/` con Pine 5m, Retroceso al POC, Zona de Demanda).

---

## 6. `03_Resources/` — referencia (45 archivos)

Guía de entrada: `README.md`.

| Tema | Notas |
|---|---|
| **Claude Code** | `Sistema Claude Code - Configuracion Completa`, `Ahorro de tokens en Claude Code`, `Guia - Skills vs Agentes`, `Claude Code para SaaS y startups` (3 variantes), `Mejores prácticas webs con Claude Code`, `Awesome Claude Design` |
| **Metodología de software** | `Catalogo de Componentes`, `Biblioteca de Layouts`, `Biblioteca de Referencias Premium`, `Starter Kits NeoZeler`, `Checklist pre-cobro (micro SaaS)`, `Web Interface Guidelines` |
| **Registros** | `Registro de Identidades Visuales`, `Registro de Oportunidades`, `Registro de Retros` |
| **Roblox** | `Guia de Texturas y Materiales PBR`, carpeta `Avatar y Psicologia del Jugador` |
| **Otros** | GoHighLevel, trading (prompt de investigación), plan de aprendizaje de redes neuronales, hábitos |
| `Enlaces & Herramientas/` | 3 notas: iconos y componentes UI, Public APIs, skills de diseño web (Three.js/GSAP) |
| `Investigaciones/` | ML aplicado, ML con hardware modesto, fuentes de fitness, carpeta `claude-code-ecosystem-2026/` |

---

## 7. `04_Archive/` — trastero (36 archivos)

`README.md` explica el criterio. Contiene `AVAX-RL-Bot`, `crypto-ml-bot`, `goat-trading`, una transcripción duplicada, `Crypto-Copy-Bot/` (spec + checklist de despliegue) y `Memecoin-LSTM/` (roadmap de 17 fases, bot real v7, modelos, auditorías, planes y registros de experimentos).

---

## 8. `99_Assets/` — binarios (154 archivos, casi todo no-Markdown)

| Carpeta | Archivos | Contenido |
|---|---|---|
| `reto-30/` | 47 | `carteles/`, `demo-rescatada/`, `imagenes/` |
| `productos-imagenes/` | 25 | Fotos de producto (`shopify-peine-aplicador/`) |
| `RethinkbyIA/` | 21 | Material de marca |
| `Abisal Drill/` | 13 | `Backups/`, `Modelos 3D/` |
| `Documentos/` | 8 | PDFs (p. ej. `NeoFlow-AI-Dossier.pdf`, `NeoFlow-AI-Pitch.pdf`) |
| `Fuentes/` | 6 | Tipografías |
| `Imagenes/` | 6 | Imágenes sueltas |
| `logos/` | 5 | Logotipos |
| `Html/` | 4 | HTML sueltos |
| `Lanzamientos/` | 4 | Material de lanzamientos |
| `Certificados/` | 2 | Certificados |

---

## 9. Raíz y carpetas técnicas

**No tocar** (maquinaria):
- `.git/` — repo con auto-push. `.gitignore` excluye `.sync/`, `.stfolder/`, `graphify-out/`, `scripts/logs/`, `00_Meta/API.md` y los datos del plugin Local REST API.
- `.obsidian/` — ajustes, plugins y `snippets/` (`premium-light-theme.css` es el tema activo; también `premium-dark-theme`, `premium-light-minimal`, `custom-vault-style`, `dataview-cards-and-callouts`, `graph`).
- `.claude/` — `ARCHITECTURE_MAP`, `COMMON_MISTAKES`, `QUICK_START`, `AUDIT_VAULT_2026-08-08`, `launch.json`, `settings.local.json`, `completions/`, `sessions/{active,archive}`, `templates/`, `worktrees/`.
- `.agents/` — reglas y flujos para Gemini/Antigravity: `rules/` (10 reglas), `workflows/graphify.md`, `mcp_config.json`, `skills.json`.
- `.token-optimizer/`, `.stfolder/`, `.trash/`, `graphify-out/` (grafo del vault, regenerable con `graphify update .`).
- `docs/` — `INDEX.md`, `borrador-config/` (`global/`, `vault/`), `learnings/` y `archive/` (vacías).

**Archivos de control en raíz**: `CLAUDE.md`, `GEMINI.md`, `.mcp.json`, `.claudeignore`, `.graphifyignore`, `.gitignore`, `.diagram-design`.

> [!riesgo] Desorden en la raíz
> El `CLAUDE.md` dice que la raíz solo debe tener `CLAUDE.md`, `GEMINI.md`, `.mcp.json`, los `.ignore` y las carpetas. El 2026-11-06 se movieron 18 archivos sueltos a `99_Assets/` y se borraron 8 duplicados idénticos. Aparecieron después 15 archivos 3D (`command-totem`, `data-receiver-drone`, `data-vault-diorama`, `layth-ai-node`, `tech-core`; `.glb/.mtl/.obj`) que deberían ir a `99_Assets/` (pendiente).
>
> `ssh@192.168.0.100mp-crm-test/` (`n8n/`, `src/`, `tests/`), copia de código del CRM sacada por error con un nombre de ruta SSH, se movió el 2026-11-12 a `~/Proyectos/archive/ssh-192.168.0.100mp-crm-test-20261112/`. Ya no está en la raíz.

---

## 10. Convenciones que atraviesan todo

- **Frontmatter**: `type`, `status`, `date`, `origen` (`humano|maquina|mixto`). Notas nuevas siempre con `origen`.
- **Callouts**: `[!cliente]`, `[!resumen]` («En cristiano» al inicio de toda ficha), `[!riesgo]`.
- **Proyecto de software**: ficha en `01_Projects/<Nombre>.md` + carpeta con los 6 documentos + `Ficha de Investigacion` y `Retro` + sesión en `00_Meta/Sesiones/`.
- **MOC por área**: `NeoZeler - MOC`, `Trading con 10 euros - MOC`, `Dropshipping - MOC`, `RETO 30 - MOC`.
- **Herramientas de navegación**: `vault-search` (búsqueda por significado), `graphify` (relaciones), `obsidian-vault` (leer/crear).
