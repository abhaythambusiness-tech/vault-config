---
date: '2026-11-21'
type: sesion
origen: mixto
proyecto: '[[01_Projects/Setter Dashboard]]'
tags:
- setter
- dashboard
---

# 2026-11-21 · Setter Dashboard (Resumen, Kanban, Agenda)

> [!resumen] En cristiano
> Se construyó un panel premium enlazado al Setter con tres pantallas. Para enlazarlo se creó en n8n un workflow nuevo de solo lectura. Funciona con datos reales (poquísimos aún) y con datos de ejemplo.

## Qué se hizo
- Workflow n8n `Setter - Dashboard API` (`kOpuEvLWSbtURpsY`, publicado): webhook GET con token → clientes, mensajes y citas en JSON.
- App `~/Proyectos/setter-dashboard/`: Resumen, Kanban, Agenda; interruptor Real/Demo; tema oscuro con acento azul NeoZeler.

- Segunda pasada de UI/UX:
  - Esqueletos de carga.
  - La ficha del lead se abre con un clic en cualquier sitio.
  - Tendencia de 7 días.
  - Agenda con botones de semana y «Hoy».
  - Una tendencia del 0 % sale como «Igual que 7 días antes», no como un «+0 %» verde.

## Aprendizajes
- `alwaysOutputData` + `executeOnce` en los nodos Data table evita que una tabla vacía (citas) corte el workflow y que se multipliquen filas.
- El hook `guard-destructive` bloquea cualquier comando Bash que contenga la palabra `truncate` en minúsculas (también la clase Tailwind `truncate`) y `rm -r` fuera de /tmp: escribir esos archivos con Write.
- `next build` falla con «Cannot find module for page: /_not-found» si el servidor de desarrollo está activo sobre el mismo `.next`: pararlo antes.
- Tipografía: la variable de Geist cuelga del `body`, así que `font-family` va en `body`, no en `html`.
