---
type: ficha-investigacion
proyecto: "Los Apuntes de Liyo"
tipo: micro-saas
status: aprobada
date: 2026-10-28
origen: mixto
---

> [!resumen] En cristiano
> Esta ficha es la "tarea previa" del proyecto, escrita **a posteriori** (retroactiva): se hace después del PRD, el TRD y el UI-UX porque es el piloto del sistema de mejora continua. Recoge lo que ya se decidió de verdad: qué librerías, qué tipografías y qué referencias.
> El `tipo: micro-saas` es **provisional**: el PRD no lo dice y Haytham lo confirmará (es un proyecto personal suyo, no una web de cliente).
> Sirve de ejemplo para ver si el sistema evita diseños "cutres" y librerías sin investigar.

# Ficha de Investigación

## Librerías
| Necesidad | Candidata A | Candidata B | Elegida y motivo | Fuente |
|---|---|---|---|---|
| Servidor | Node + Express | FastAPI | **Bun + TypeScript**: ~25-33 MB de RAM medidos en el servidor frente a 63-89 MB de Node | TRD §1 (patrón `neozeler-crm`) |
| Búsqueda | Meilisearch/Typesense | rank-bm25 en memoria | **SQLite FTS5** (`bun:sqlite`): BM25 y quitar acentos incluidos, un solo archivo, cero dependencias | TRD §1 |
| Leer PDF | `pdf-parse` 2.4.5 (Apache-2.0) | `pdfplumber`/`PyMuPDF` (Python) | **`unpdf` 1.9.1** (MIT): texto por página probado; verificado en npm | Nota del proyecto |
| IA | `groq-sdk` | Llama 3.1 8B | **API de Groq con `fetch` nativo**, modelo `openai/gpt-oss-20b`: sin SDK que auditar | TRD §1 |
| Interfaz | React/Next | framework de componentes | **HTML + CSS propio** sin framework (móviles modestos, poca RAM; 0 motores de animación) | TRD §1.2 |
| Tipografía | — | — | **Space Grotesk** (títulos) + **Work Sans** (cuerpo), OFL, autoalojadas en `public/fonts/` | UI-UX §2 |

## Skills y agentes
- Identidad y gate de diseño: `rules/diseno.md` + `identidad-y-dinamismo.md`; UI nueva: `hallmark`; UI existente: `impeccable` (`critique`, `polish`).
- Esquema y búsqueda: `supabase-postgres-best-practices` solo como guía de SQL; la BD real es SQLite.
- Estados de carga/error y a11y: `web-animation-skills:accessible-animation`, `accesslint-audit`; antes de publicar: `pre-ship-gate` y agente `auditor-web`.
- Revisión de código por bloque: `ponytail-review` o agente `revisor-codigo`.

## Referencias
- Linear (modo oscuro): jerarquía sobria con bordes finos de 1px y mucho aire.
- Readwise Reader (modo oscuro): el resaltado como objeto real; aquí es la cita iluminada.
- Biblioteca universitaria de noche: pocos puntos de luz cálida sobre fondo frío («Luz de lámpara», azul noche + ámbar).

## Lecciones aplicables
- Motivo del piloto (Haytham): diseños anteriores "cutres", librerías sin investigar, entregas del mínimo que funciona y skills sin aprovechar a fondo.
- Rediseño del 2026-10-28: la v1 salió "muy cutre" (entrada pequeña y vacía, módulos y chat en pestañas); revisar el diseño en navegador antes de dar una pantalla por buena.
- Verificar versión y licencia en npm antes de fijar una librería (`pdf-parse` quedó sin verificar en el TRD).

## Extras de la vía

### micro-saas
Señal de demanda: pendiente (el PRD parte de una idea de Haytham; no hay entrevistas ni prueba de pago registradas). Antes de cobrar o abrir fuera de la red de Haytham: [[Checklist pre-cobro (micro SaaS)]]. Riesgo ya avisado en el PRD: subida abierta sin revisión previa (mitigación: denuncia + borrado por el admin).
