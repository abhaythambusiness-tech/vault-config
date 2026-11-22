---
type: guia
proyecto: "Comanda Viva"
status: activa
date: 2026-11-04
origen: mixto
---

# Guía — Skills y reglas por fase

> [!resumen] En cristiano
> Qué herramienta de Claude usar en cada fase del [[6 - Plan de Implementacion]] y qué reglas no se saltan. Sirve para no improvisar al retomar el proyecto.

| Fase | Skills y herramientas | Reglas que no se saltan |
|---|---|---|
| 0 Scaffold | `superpowers:test-driven-development`, Node 22 | Git y `.gitignore` antes del primer commit; sin secretos |
| 1 Datos | `supabase`, `supabase-postgres-best-practices`, `schema_to_migration.py`, PGlite | Toda FK con `ON DELETE`; el doc 5 manda y la migración se regenera |
| 2 Cliente | `diseno-central` primero, `web-animation-skills:accessible-animation`, `vercel-react-best-practices`, `context7` | Texto crítico recto y ≥ 18 px; «Quedan N» siempre en texto; nada de imágenes inventadas |
| 3 Caja | `supabase` (Realtime), `design:ux-copy` | Plan B por polling; botón «Activar sonido» |
| 4 Dueña | `dataviz`, `rules/dashboards-saas.md`, Bklit, `humanizer` para textos | Frases sencillas en el panel; margen solo con costes |
| 5 UI | `hallmark`, `impeccable`, `dribbble-scrape` si hace falta otra referencia | Identidad aprobada manda; imagen que falta = parar y preguntar |
| 6 Pulido | `accesslint-audit`, `pre-ship-gate`, `auditor-web` + `revisor-codigo` + `ponytail-audit` en paralelo | 375/768/1280 px, `axe` a cero, Lighthouse |
| 7 Despliegue | `superpowers:verification-before-completion` | Ciclo crear → refrescar → borrar → refrescar en producción; permiso antes de gastar |

Cierre: `archivista` y rellenar la Retro (`/nuevo-proyecto`, paso «Cerrar»).
