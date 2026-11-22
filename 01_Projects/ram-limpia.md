---
type: proyecto
status: activo
date: '2026-11-13'
repo: ~/Proyectos/flujo-software/tools/ram-limpia/
origen: mixto
tags:
- herramienta
- claude-code
- ram
---

> [!resumen] En cristiano
> Cada vez que abres Claude Code, arranca unos 8 programitas de apoyo (los «MCP») que gastan unos 600 MB. Si cierras la sesión de golpe, esos programitas se quedan vivos sin que nadie los use y se comen la memoria del PC (el 13-nov llegaste a 13 de 15 GB). `ram-limpia` los encuentra y los cierra. Ahora corre solo cada 5 minutos, así que no tienes que acordarte de nada.

## Qué es

Herramienta en Go (tu regla: scripts nuevos en Go) que:
- **Informa**: sesiones de `claude` abiertas, cuánta RAM gasta cada una y qué procesos están huérfanos.
- **Limpia**: mata huérfanos (MCP y, a mano, dev servers de Next) o cierra una sesión entera con sus hijos.
- **Se activa sola**: timer de systemd de usuario cada 5 min, sólo sobre MCP.

Código y README: `~/Proyectos/flujo-software/tools/ram-limpia/` (`README.md` con uso, instalación y límites). Binario: `~/.local/bin/ram-limpia`.

## Uso rápido

```bash
ram-limpia                  # informe
ram-limpia -huerfanos       # mata MCP + dev servers huérfanos
ram-limpia -sesion PID      # cierra una sesión claude y su árbol
journalctl --user -u ram-limpia.service -n 20   # qué cerró el timer
```

## Lo que se aprendió

- Un proceso huérfano **no pasa al PID 1**, lo adopta el `systemd --user` (PID 1033). La primera versión miraba sólo el PID 1 y habría dado siempre «0 huérfanos».
- Los dev servers van fuera del modo automático (`-mcp`): uno lanzado a propósito también cuelga de `systemd` y se confundiría con un resto.
- Cierre en dos tiempos (TERM, 5 s, KILL): alguna sesión no caía con TERM.
- No se probó con una sesión `claude` real (gasta tokens); se simuló con un padre falso y un hijo que imita un MCP.

## Riesgos y pendientes

> [!riesgo] Límites
> - No reduce el gasto base: cada sesión nueva sigue arrancando sus MCP. Para ahorrar más, desactivar los poco usados (`rea` ≈ 210 MB por sesión, `ssh-mcp`, `shadcn`, `magicui`): decisión tuya.
> - Un MCP nuevo con otro nombre no se detecta hasta añadirlo a la regex `mcpRe` de `main.go`.
> - En la prueba de punta a punta con systemd, la primera ejecución cerró 0 (causa sin determinar); la segunda cerró 1.
> - Sin tests automáticos.

## Relacionado

- [[NeoZeler Tools]] · herramientas transversales en `~/Proyectos/flujo-software/tools/`
- Regla de scripts repetibles: `CLAUDE.md` del vault §0.12

