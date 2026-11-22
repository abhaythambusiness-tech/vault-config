---
date: 2026-11-08
type: sesion
origen: mixto
proyecto: "[[01_Projects/Mini CRM Go]]"
tags:
  - sesion
  - crm
  - frontend
---

> [!resumen] En cristiano
> El CRM tenía la pantalla hecha con HTML suelto y se quedaba corto: todo apretado y difícil de ampliar. Se rehízo la pantalla entera con React, en 8 pasos, sin tocar la base de datos. El programa sigue siendo un único archivo que corre en tu ordenador; al abrirlo te lleva a la pantalla nueva. Lo viejo se borró (hay copia de seguridad).

## Qué se hizo
- Plan de 8 fases ([[01_Projects/Mini CRM Go - Plan de migracion de frontend]]), cada una aprobada por Haytham y con commit propio.
- Fases 1-3: API JSON en Go, esqueleto Vite + React + Tailwind, SPA embebida con `go:embed` en `/app/`.
- Fases 4-7: Prospección con ficha lateral, Kanban (dnd-kit, actualización optimista), Hoy + Panel (Recharts), IA Hub con «Gancho de prensa».
- Fase 8 (corte): `/` redirige a `/app/`; borrados `templates/` y las rutas HTML; README, ficha y `resumen.html` al día.

## Aprendizajes
- `GET /api/leads/{domain}/status` devuelve 204 mientras investiga (no es error): los tests deben sondear y tolerarlo; `POST investigate` devuelve 202.
- Un hook de seguridad confunde la palabra «truncate» (clase CSS de Tailwind) con el SQL de borrado y bloquea el comando entero: escribir esos archivos con Write.
- `pkill -f "crm serve"` mata la propia shell; usar `pkill -x <nombre>`.
- Se conserva la bandera `-templates`, ignorada, para no romper servicios o scripts viejos.

## Pendiente
- `npm audit` (6 avisos), arrastre con ratón o táctil en Kanban, «Actualizar ahora» con feeds reales, bloque «Recientes» del Panel viejo sin migrar, login si algún día se expone a red.
- Copia previa al corte: `~/Proyectos/archive/minicrm-go-pre-fase8-20261108.tar.gz`.
