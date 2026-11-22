---
type: ficha-investigacion
proyecto: "Grid64"
tipo: micro-saas
status: aprobada
date: 2026-11-08
origen: mixto
---

> [!resumen] En cristiano
> Antes de seguir, apunto qué piezas ya hechas voy a usar (verificadas hoy contra los registros oficiales), qué herramientas ayudan en cada fase y qué lecciones de errores pasados valen aquí. Referencias de diseño: **omitidas por decisión de Haytham** (2026-11-08).
> **Decisión que te toca:** aprobar la ficha (`aprobada`) para que el hook deje escribir código.

# Ficha de Investigación — Grid64

## Librerías
Verificadas el 2026-11-08 con `proxy.golang.org` y `npm view` (no de memoria). `librerias.md` no tiene entradas de estas.

| Necesidad | Candidata A | Candidata B | Elegida y motivo | Fuente |
|---|---|---|---|---|
| SQLite sin CGO | `modernc.org/sqlite` v1.62.0 (2026-11-07) | `mattn/go-sqlite3` (CGO) | A: lo pide el spec; **android/arm64 sin comprobar** → spike T-01, plan B la B con NDK | proxy.golang.org |
| Puente Go → Android | `golang.org/x/mobile` (gomobile bind) | Wails | A: Wails no cubre Android | proxy.golang.org (v0.0.0-20261011) |
| Markdown de las notas | `github.com/yuin/goldmark` v1.8.7 | render en cliente | A: servidor, un sitio; sanear HTML | proxy.golang.org |
| Interactividad móvil | Alpine.js 3.17.5 (MIT) | HTMX | A: swipe y hoja inferior piden estado de cliente; HTMX solo si un fragmento lo pide | `npm view` |
| Estilos | Tailwind 4.3.5 (MIT), CLI standalone | CSS a mano | A: lo pide el spec; compilar a `frontend/dist`, sin Node en runtime | `npm view` |

Pendiente en el TRD §1.1: peso exacto y licencia de las de Go (revisar `go.mod` tras `go get`).

## Skills y agentes
- Documentos y arranque → `nuevo-proyecto`, `superpowers:brainstorming`.
- Identidad y pantallas → `diseno-central` (+ `impeccable shape` antes del v0); sin `dribbble-scrape` por decisión de Haytham.
- Go: `superpowers:test-driven-development` para reglas (progreso, límite de 5, conversión, racha).
- Cada fase del Plan → `revisor-codigo`; antes de entregar → `auditor-web` y `superpowers:verification-before-completion`.
- Sobreingeniería → `ponytail-review`. Android: sin skill propia; context7 para docs de gomobile y WebView.
- Cierre → `archivista`.

## Referencias
Omitidas por decisión de Haytham (2026-11-08). Para la comparación final, usar la identidad aprobada en [[3 - UI-UX Design]] y el mandala de [[NeoZeler HQ]] como punto de partida de producto (no de diseño).

## Lecciones aplicables
- Validar el ciclo crear → refrescar → borrar → refrescar en el dispositivo real, no solo en tests.
- Toda FK con `ON DELETE` explícito; probar el SQL antes de aprobar (en Go: test con base en memoria).
- Alpine 3.17.5 no trae archivo de licencia en npm (`librerias.md`, battle-royale).
- Cero imágenes inventadas: si falta una (icono de la app), parar y preguntar.
- Comprobar el esquema real antes de asumir; no cambiar parámetros de negocio sin avisar (límite de 5 acciones/día es del spec).

## Extras de la vía

### micro-saas
- Señal de demanda: **no aplica en v1** (uso propio). Antes de publicar o cobrar: entrevistas, canal y prueba de pago, más [[Checklist pre-cobro (micro SaaS)]].
