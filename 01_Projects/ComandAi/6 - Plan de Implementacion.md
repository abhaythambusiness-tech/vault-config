---
type: doc-software
doc: plan
proyecto: ComandAi
status: aprobado
date: '2026-11-03'
origen: mixto
---

# 6 · Plan de Implementación — ComandAi

> [!resumen] En cristiano
> Orden de trabajo: primero las carpetas y un script, luego el servidor con datos reales, después el diseño, y al final Tailscale y el móvil. Cada paso cita la historia del PRD que cumple.

| # | Tarea | Historia | Hecho cuando |
|---|---|---|---|
| 0 | Identidad visual + portadas aprobadas (UI-UX §2, §5, §7) | US-01..04 | Haytham aprueba; sin esto no se maqueta |
| 1 | Crear `humano/` y `maquina/{entrada,util,logs}` en `02_Areas/NeoZeler/Comercial/` y `00_Meta/Panel/` | US-06 | Carpetas y README de cada una |
| 2 | Script Python de novedades de IA (RSS públicos) → `maquina/entrada/` | US-02 | Crea archivos con fecha; probado aislado |
| 3 | Servidor Bun: lee carpetas, ruta `/` (Hoy) y `/novedades` | US-02, US-06 | Se ve en `localhost:8200` |
| 4 | Tareas: leer/marcar checklist Markdown | US-01 | Marcar y refrescar persiste |
| 5 | Leads: lectura del CRM `:8100` y Laya Leads | US-03 | Lista real sin duplicar datos |
| 6 | Proyectos y contenido desde `01_Projects` | US-04 | Estados correctos |
| 7 | UI final: portadas, dock de iconos, móvil 375 px | US-01..06 | axe 0 violaciones, Lighthouse |
| 8 | Instalar Tailscale (Zorin, PC, móvil) — lo haces tú con `sudo` | US-05 | Los tres se ven en `tailscale status` |
| 9 | Desplegar en Zorin con `systemd --user` y timers; bind a IP Tailscale | US-05 | Abre desde el móvil; sobrevive a reinicio |
| 10 | Medir RAM, README, ficha, HTML resumen, sesión | todas | RAM < 150 MB |

## Starter kits reutilizados
| Kit | Para qué |
|---|---|
| Neozeler CRM (Bun) | Estructura del servidor y despliegue en Zorin |

---
Anterior: [[5 - Backend Schema]]
