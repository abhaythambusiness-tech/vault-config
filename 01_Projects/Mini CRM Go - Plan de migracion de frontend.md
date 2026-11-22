---
date: 2026-11-08
type: plan
status: completado
proyecto: "[[Mini CRM Go]]"
repo: ~/Proyectos/minicrm-go
origen: mixto
---

# Mini CRM Go: plan de migración del frontend (HTMX → React)

> **Hecho (2026-11-08): las 8 fases están completas y commiteadas.** Desde la fase 8 `/` redirige a `/app/` y no queda HTML de plantillas.

> [!resumen] En cristiano
> El CRM funciona, pero las pantallas (Kanban, ficha, panel) ya no caben bien en plantillas HTML sueltas. Plan: el programa de Go sigue igual por dentro (base de datos, scraper, reglas) y solo cambia lo que ve el usuario, que se rehace en React por piezas. Al final sigue siendo **un solo programa** que se abre en el navegador, sin Node en el servidor. Se migra pantalla a pantalla, así el CRM nunca deja de funcionar.

## 1. Decisión y límites

- **Se queda**: `internal/{db,importer,scraper,servicios,leads,hub}` y `cmd/crm`. Cero cambios de lógica.
- **Cambia**: `templates/` (3 archivos, ~850 líneas) y las rutas de `internal/server/` que devuelven HTML.
- **Stack nuevo** (carpeta `web/`): Vite + React + TypeScript + Tailwind + shadcn/ui + Lucide + TanStack Query (datos) + Recharts (gráficos) + dnd-kit (Kanban). Se descarta Wails (se usa por navegador) y Tremor.
- **Entorno**: Node 18.19 → fijar Vite 5 (Vite 7 pide Node 20). Go 1.22 ya vale para `go:embed`.
- **Identidad visual**: la de `DESIGN-IDENTITY.md` («tablero de azulejos»: neutros cal, tinta, 4 colores de servicio, Onest + Azeret Mono). Antes de tocar UI: `diseno-central`, y referencias con `dribbble-scrape` si se rediseña pantalla.
- **Sin login y solo `127.0.0.1`** hoy; no se cambia. Si algún día se abre a la red hay que añadir token + CSRF (puerta abierta, no en este plan).

## 2. Contrato de la API (fase 1)

Las rutas actuales ya separan datos de HTML; los structs (`Pagina`, `Ficha`, `Tarjeta`, `Panel`, `Agenda`, `Lead`) pasan a JSON casi tal cual.

| Hoy (HTML) | API nueva (JSON) |
|---|---|
| `GET /leads` | `GET /api/leads?servicio&q&etapa&multi&caliente&contacto&cms&estado&n&orden` → `{items, total}` |
| `GET /leads/{d}` | `GET /api/leads/{d}` → ficha completa (señales, contactos, huella, seguimiento) |
| `POST …/etapa`, `/seguimiento`, `/notas`, `/investigate` | mismos verbos bajo `/api/leads/{d}/…`, cuerpo JSON |
| `GET …/status` | `GET /api/leads/{d}/status` (204 investigando / 200 listo) |
| `/feed`, `/scraper`, `/vencen` | `GET /api/feed`, `/api/scraper`, `/api/vencen` |
| vista Hoy / Panel | `GET /api/hoy`, `GET /api/panel` |
| `/ia-hub/*` (13 rutas) | `/api/hub/{noticias,ideas,implementaciones}` + `GET /api/leads/{d}/hub` |

Reglas: errores como `{error: "texto"}` con el código HTTP correcto; validación sigue en Go (`Filtro.Validar`, `EtapaValida`); tipos TS generados a mano en `web/src/api/tipos.ts` (3 pantallas, no merece generador).

## 3. Fases

| # | Fase | Hecho cuando |
|---|---|---|
| 0 | **Línea base**: `go test ./...` en verde, captura de las 4 vistas actuales (`.capturas/`), commit limpio | tests pasan; capturas guardadas |
| 1 | **API JSON** en `internal/server/api.go` junto a las rutas HTML (conviven). Tests en `server_test.go` por endpoint | todas las rutas de §2 responden y tienen test |
| 2 | **Esqueleto web**: `web/` con Vite, Tailwind, shadcn, tokens de la identidad, layout (barra lateral, atajos `/`, `1-4`), cliente de API | `npm run build` limpio; `npm run dev` con proxy a `:8080` |
| 3 | **Embebido**: `web/dist` → `go:embed` en `cmd/crm`; ruta `/app/*` sirve la SPA (con fallback a `index.html`) | `go build` produce un solo binario que sirve `/app` |
| 4 | **Ficha lateral + Tabla** (`/app/leads`): tabla densa, filtros combinados guardados en la URL, panel deslizante (Sheet) con notas autoguardadas, etapa, seguimiento, investigar y estado | paridad con la ficha HTMX actual |
| 5 | **Kanban** con dnd-kit: mover tarjeta = `POST etapa` con actualización optimista y vuelta atrás si falla | arrastrar cambia la etapa y sobrevive a recargar |
| 6 | **Hoy + Panel**: vencidas/hoy/próximos, insignia, KPIs, embudo y penetración con Recharts, feed y estado del scraper por sondeo | paridad con vistas Hoy y Panel |
| 7 | **IA Hub**: noticias, ideas (estados), catálogo y «Gancho de prensa» en la ficha | paridad con `/ia-hub` |
| 8 | **Corte**: `/` redirige a `/app`; se borran `templates/` y las rutas HTML; README, ficha del vault, `resumen.html` y sesión (vault §0.8) | no queda HTML de plantillas |

Orden de valor: 4 y 5 resuelven el dolor actual (UI apretada); 6 y 7 pueden esperar y seguir en HTMX mientras tanto. Cada fase termina con commit propio.

## 4. Verificación (global §3, web.md)

- `go test ./...` + `npm run build` + type-check antes de cada commit.
- Vistas a **375 / 768 / 1280 px**, `axe` a cero violaciones, Lighthouse.
- Probar el ciclo completo en la base real de copia: crear/mover/editar → refrescar → comprobar que persiste.
- Medir RAM del binario antes y después (regla «web con poca RAM»): objetivo, sin subida apreciable porque el JS corre en el navegador.
- Copia de `data/crm.db` antes de la fase 1 y de la 8 (la migración no toca esquema, pero se hace igual).

## 5. Riesgos

- **Dos interfaces a la vez** entre fases 3 y 8: aceptado; las rutas HTML no se tocan hasta el corte.
- **Duplicar reglas de filtro en el cliente**: no. Todo filtro se resuelve en Go; el cliente solo envía parámetros.
- **Crecimiento de dependencias** (npm): fijar versiones exactas y `npm audit` en el cierre.
- **Atajos y accesibilidad** que HTMX daba gratis (foco, teclado): comprobar con axe y a mano en el Kanban (dnd-kit trae teclado, activarlo).

## 6. Puertas abiertas (decide Haytham)

1. ¿Redibujar con la identidad actual tal cual o aprovechar para refrescarla (pasaría por `dribbble-scrape` y `diseno-central`)?
2. ¿Todo el IA Hub en esta migración o dejarlo en HTMX hasta una segunda ronda?
3. ¿Se abrirá algún día a más gente (Sam) por red? Si sí, login entra en el plan.
