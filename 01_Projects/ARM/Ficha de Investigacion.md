---
type: ficha-investigacion
proyecto: ARM
tipo: micro-saas
status: aprobada
date: '2026-11-17'
origen: mixto
---

> [!resumen] En cristiano
> Tarea previa al TRD: qué piezas ya hechas usaremos, qué herramientas ayudan y con qué nos comparamos. Las versiones se miraron el 2026-11-17 en proxy.golang.org y npm; el SDK de MCP se contrastó con context7.

# Ficha de Investigación — ARM

## Librerías
| Necesidad | Candidata A | Candidata B | Elegida y motivo | Fuente |
|---|---|---|---|---|
| Servidor API + MCP | Go + `net/http` + `chi` v5.5.0 | FastAPI (Python) | **Go**: regla global 2026-11-12 y un solo binario por cliente. Con `chi` basta | proxy.golang.org |
| Documentar la API (OpenAPI) | `huma` v2.40.0 (genera OpenAPI desde los tipos) | OpenAPI escrito a mano | Huma si el spike confirma que encaja con `chi`; si no, a mano | proxy.golang.org |
| MCP | SDK oficial `modelcontextprotocol/go-sdk` v1.8.0 (`AddTool` genérico, `NewStreamableHTTPHandler`, `auth.RequireBearerToken`) | `mark3labs/mcp-go` | **SDK oficial**: mantenimiento garantizado | context7 `/modelcontextprotocol/go-sdk` |
| Base de datos | SQLite con `modernc.org/sqlite` v1.62.0 (sin CGO) | PostgreSQL | **SQLite**: una instancia por cliente, un archivo, copia en caliente. Ya probado en Grid64 (arm64) | `librerias.md` (SQLite, FK) |
| Frontend base | Vite 8.3.8 + React + Tailwind 4.3.5 + shadcn 4.23.0 | Next 16 | **Vite SPA** embebida en el binario Go (`embed`): sin servidor Node. La web no necesita SEO | npm |
| Estado de servidor | `@tanstack/react-query` 5.108.0 | `fetch` a mano | React Query: caché y refresco | npm |
| Pipeline (kanban) | `@dnd-kit/core` 6.3.1 (último release 2024-12) | HTML5 drag nativo | Por decidir: dnd-kit lleva casi un año sin release; valorar drag nativo | npm |
| Componentes distintivos | shadcn + magicui + 21st (regla 2026-11-13: buscar antes de escribir a mano) | BoardUI (tablas, gráficas, chat) | Se elige en la Paleta de Componentes | `librerias.md` (AI Designer Toolkit) |
| HTTPS | Caddy | nginx | Caddy: certificado automático (usado en Panel de Leads) | Panel de Leads |
| Alta de instancia | Go (script) | bash | Go | CLAUDE.md global §3 |

## Skills y agentes
- PRD / TRD: `context7` para docs de librerías; `sequential-thinking` para el modelo de permisos de claves y MCP; `superpowers:brainstorming` ya cubierto por el PRD.
- Identidad y UI: `diseno-central` (obligatoria), `impeccable shape` antes de maquetar, luego `design-taste-frontend` o `hallmark`.
- Backend Go: `ponytail` activo; `revisor-codigo` al cerrar.
- Seguridad (claves, MCP, RGPD): `security-review` antes de entregar a un cliente real.
- n8n (migrar el Setter a escribir en ARM): MCP de n8n y skill `n8n-automation`.
- Cierre: `revisor-codigo` + `auditor-web` + `ponytail-audit`; `archivista`.

## Referencias
Pendiente de elegir con Haytham. Mirar en [[Biblioteca de Referencias Premium]]: un CRM ligero (Linear, Attio) para la ficha y el pipeline, y la documentación de API de Stripe como referencia de claves y OpenAPI.

- (sin elegir)

## Lecciones aplicables
- SQLite: `PRAGMA foreign_keys=ON` en **cada** conexión; sin él `ON DELETE CASCADE` no borra nada (`librerias.md`).
- Cruce por teléfono: se guarda sin prefijo 34 y sin `@s.whatsapp.net` (Setter, 2026-11-13). ARM debe normalizar el teléfono al entrar.
- n8n: `Wait` sin unidad explícita es ambiguo; poner `seconds`.
- `setter-neozeler/build.py` regenera desde un export viejo y pisaría cambios hechos a mano en n8n: sincronizarlo antes de cambiar el Setter.
- Node del sistema es 18 y rompe shadcn: usar el 22 de fnm.
- Panel de Leads (archivado): reutilizar la UI y la definición de «cualificado»; la lección del repo es no depender de tablas ajenas.
- Go local es 1.22.2: comprobar que `go-sdk` v1.8.0 y `modernc.org/sqlite` v1.62.0 compilan, o actualizar Go antes del spike.

## Extras de la vía

### micro-saas
- Señal de demanda: no se exige (decisión de Haytham, 2026-11-17). Primer cliente real: el propio Setter de NeoZeler.
- Antes de cobrar: revisar [[Checklist pre-cobro (micro SaaS)]].
- Criterio de promoción a SaaS: si pasa a venderse por separado o con varios usuarios por cliente.
