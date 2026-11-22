---
type: sesion
date: '2026-11-14'
proyecto: '[[ram-limpia]]'
origen: maquina
sesion_id: 6cc3439f-dd80-4f87-8e3f-46b80d7fd788
tags:
  - sesion
  - cierre-automatico
---

> [!resumen] En cristiano
> El ordenador iba justo de memoria (13 de 15 GB). Cada sesión de Claude arranca sus propios programas auxiliares (MCP) y, al cerrarse mal, los deja colgados. Se cerró una sesión vieja y se creó una herramienta, `ram-limpia`, que mata esos restos sola cada 5 minutos.

## Qué se hizo
- Auditoría: swap lleno y solo 1,4 GiB libres; node, brave y npm eran lo que más pesaba. Casi todo node/npm eran MCP: unos 600 MB por sesión de `claude`.
- Cerrada la sesión `claude` 125842 (6 h) con sus MCP y los dev servers 3100 y 3101. Disponible: 1,4 → 3,2 GiB; swap 2 GiB → 933 MiB.
- Herramienta `ram-limpia` (`~/Proyectos/flujo-software/tools/ram-limpia/`) con `-huerfanos -mcp`, activada con un timer de `systemd --user` cada 5 min.
- Prueba con un padre falso muerto con `kill -9`: el MCP huérfano se mató. La prueba vía systemd falló una vez y pasó al repetirla.
- README en el repo y ficha [[ram-limpia]] en `01_Projects/` (`origen: mixto`).

## Problemas y límites
- SIGTERM no bastó en algunos procesos; hizo falta `kill -9`.
- No se probó con una sesión `claude` real (gastaría tokens y arrancaría 8 MCP).

## Pendientes / mejoras
- Vigilar unos días que el timer no mate MCP de sesiones vivas.
- Considerar cerrar sesiones viejas antes de abrir otras.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
