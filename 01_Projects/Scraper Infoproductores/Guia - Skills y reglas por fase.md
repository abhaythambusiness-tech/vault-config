---
type: referencia
proyecto: "Scraper Infoproductores"
date: 2026-11-01
origen: mixto
---

# Guía — Skills y reglas por fase

> [!resumen] En cristiano
> Qué herramienta usar en cada fase del [[6 - Plan de Implementacion]] y qué reglas ya están cubiertas por tareas, para no improvisar. No cambia ningún documento aprobado.

## 1. Reglas globales cubiertas por tareas
| Regla | Tarea |
|---|---|
| Git y `.gitignore` antes del primer commit; sin secretos | T-01 |
| Ciclo completo crear → refrescar → borrar → refrescar en producción | T-21 |
| Borrado en cascada y baja efectiva | T-02, T-14 |
| Pruebas RLS sin falsos verdes | T-03, T-04 |
| Imágenes: sin inventar; wordmark propio | T-11 |

## 2. Fase → skill / herramienta
| Fase | Herramienta |
|---|---|
| 0 Scaffold | `ponytail` (presupuesto de dependencias), skill `shadcn` al existir `components.json`, `context7` para verificar versiones |
| 1 Datos | `supabase`, `supabase-postgres-best-practices`, MCP `supabase` (`list_tables`, `get_advisors`) |
| 2 Núcleo | `vercel-react-best-practices`, `vercel-composition-patterns`, `supabase` para auth |
| 3 UI | `impeccable shape`, `design-taste-frontend` (la identidad aprobada manda), `bklit-ui`, `svg-skill`, `web-animation-skills:accessible-animation`, `design:ux-copy` |
| 4 Cobro | `context7` (Stripe 23), `differential-review` |
| 5 Datos reales | `scrapling-official` y agente `scraper`; `investigador` para competencia |
| 6 Pulido | `impeccable critique\|audit\|polish\|harden`, `accesslint-audit`, `design:accessibility-review`; `humanizer` solo en copy de interfaz, nunca en textos legales |
| 7 Despliegue | `auditor-web`, `pre-ship-gate`, `revisor-codigo`, `differential-review` en créditos, pagos y datos personales |

## 3. Conflictos de solape
- Identidad aprobada (`DESIGN-IDENTITY.md`) manda sobre `hallmark`, `impeccable` y `design-taste-frontend`: ellos ejecutan, miden y critican.
- `ponytail` no relaja «código completo y tipado».
- Lo legal (aviso RGPD, términos, baja) exige revisión humana.

## 4. Checklist previo al commit
- [ ] `tsc --noEmit`, lint y `vitest` limpios
- [ ] `schema_to_migration.py` sin avisos de FK
- [ ] Checklist técnico (`stack-web.md`) y de marca (UI-UX §8)
- [ ] Sin secretos (`git check-ignore .env`)
- [ ] `.claude/COMMON_MISTAKES.md` revisado
