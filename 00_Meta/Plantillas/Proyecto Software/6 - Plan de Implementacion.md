---
type: doc-software
doc: plan-implementacion
proyecto: "<% tp.file.folder() %>"
status: borrador
date: <% tp.date.now("YYYY-MM-DD") %>
origen: humano
---

# 6 · Plan de Implementación

> [!resumen]
> Orden de construcción en tareas pequeñas y verificables, derivado de los 5 documentos anteriores. Código real en `~/Proyectos/<nombre>/` (git desde el primer commit).

## 1. Fases
| Fase | Objetivo | Entregable demostrable | Historias |
|---|---|---|---|
| 0 Scaffold | Repo, `.gitignore`, CI, `.env.example` | build limpio | — |
| 1 Datos | Migraciones y semilla ([[5 - Backend Schema]]) | tablas verificadas | |
| 2 Núcleo | Flujo principal ([[4 - AppFlow]]) | ciclo completo OK | |
| 3 UI | Identidad aplicada y pantallas ([[3 - UI-UX Design]]); imágenes pendientes resueltas con Haytham | demo navegable + `DESIGN-IDENTITY.md` en el repo | |
| 4 Pulido | Estados, a11y, rendimiento | checklist técnico | |
| 5 Despliegue | Producción y verificación | URL en vivo | |

## 2. Tareas
- [ ] T-01 · (US-01) descripción · archivos · criterio de hecho · depende de:

## 2.1 Starter kits reutilizados
Módulos de [[Starter Kits NeoZeler]] que se reaprovechan y su coste de adaptación:
| Kit | Fase | Adaptación |
|---|---|---|

## 3. Estrategia de pruebas
- Unitarias de reglas de negocio, e2e del ciclo crear → refrescar → borrar → refrescar **en producción**.

## 4. Despliegue y operación
- Variables de entorno, dominio, backups, monitorización.

## 5. Riesgos y plan B
> [!riesgo]
> -

## 6. Definición de terminado
- [ ] `trace_lint.py` en `RESULTADO: OK` y `schema_to_migration.py` sin avisos de FK
- [ ] Build y type-check limpios
- [ ] Checklist técnico/SEO y de marca
- [ ] Pruebas de intercambio y de lejos superadas; cero imágenes pendientes o inventadas; fila añadida a [[Registro de Identidades Visuales]]
- [ ] README en el repo
- [ ] Ficha en `01_Projects/` y sesión registrada
- [ ] `.claude/COMMON_MISTAKES.md` actualizado

---
Anterior: [[5 - Backend Schema]]
