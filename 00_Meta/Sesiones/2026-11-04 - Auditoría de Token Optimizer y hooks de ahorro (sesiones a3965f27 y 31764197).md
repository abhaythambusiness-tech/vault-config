---
title: "Sesión - 2026-11-04 - Auditoría de Token Optimizer y hooks de ahorro"
date: 2026-11-04
type: meta/sesion
origen: mixto
proyecto: ""
sesion_id:
  - a3965f27-181a-4958-b1f6-dcad9499d11b
  - 31764197-71f8-4378-a607-ec139d9aa9b1
tags:
  - sesion
  - tokens
  - configuracion
aliases: []
---

# Sesión — 2026-11-04: auditoría de Token Optimizer y hooks de ahorro

> [!resumen] En cristiano
> Haytham creía que ahorraba menos tokens que antes. Se revisó: Token Optimizer no está roto, sus números del panel eran engañosos (decía «1.300 millones ahorrados» y lo medido eran unos 5 millones). El gasto real viene de sesiones larguísimas y de un arranque pesado. Se recortó el arranque a la mitad, se archivaron 114 skills sin uso y se añadieron dos hooks que bloquean lecturas gigantes y commits de UI sin capturas.

`a3965f27` (por la tarde) revisa el plugin y el panel; `31764197` (por la noche) hace la auditoría completa y aplica los recortes. La segunda también rediseñó el sistema de UI: eso está en [[2026-11-04 - Rediseno del sistema de UI (diseno-central)]].

## Qué se hizo
- **Revisión del plugin**: `doctor` da 14/14, hooks activos. La cifra «1.3B / $300 ahorrados» venía de comparar con una foto vieja del 7-ago; los ahorros medidos eran ~5M. «Duración media 175 min» cuenta reloj con la sesión abierta aunque esté parada. El «weekly limit» desfasado es limitación de la app de escritorio.
- **Correcciones** (Haytham dijo «Sí, corrige ambos»): quitar `ANTHROPIC_BASE_URL` de `settings.json` (puerto muerto que daba «conexión rechazada» en terminal) y recalibrar la línea base con `measure.py snapshot before`.
- **Token Coach** (30 días): calidad media de 73 a 50; 64 % de sesiones D o peor; arranque de 83,7K tokens antes de escribir nada; caché al 92 %.
- **Auditoría completa**: 278 sesiones en 30 días, de 174 min de media. Aplicados 3 de 4 recortes: ventana de compactación 400k → 200k, 114 skills archivadas (de 13.910 a 3.774 tokens), `librerias.md` (37 KB) movido a `~/.claude/reference/`. Arranque estimado de 115.905 a 57.510 tokens.
- **Dos hooks nuevos** en `~/.claude/hooks/`: `guard-ui-commit.py` (bloquea `git commit` de UI sin 2 capturas de 375 y 1280 px en `.capturas/` de las últimas 12 h; se salta con `UI_CAPTURAS=off`) y `guard-read-grande.py` (bloquea `Read` de >800 líneas sin `offset`/`limit`; `READ_GRANDE=off`).

## Decisiones
- Una tarea, una sesión: `/clear` al cambiar de tema, `/compact` al cerrar un hito.
- Lo que antes parecía «ahorrar 50M» no se pudo ni confirmar ni desmentir: el contador solo lleva un día de histórico.
- Hipótesis sin probar: `rtk` reescribe Bash antes que Token Optimizer, por eso cinco ahorros marcan cero.

## Problemas
- Los conectores de cuenta de claude.ai (ventas, finanzas, small-business…) no se pueden desactivar desde aquí; los quita Haytham en Ajustes.
- Los hooks nuevos no se probaron en una sesión nueva.

## Archivos afectados
`~/.claude/settings.json` (copias en `_backups/settings-20261104-pre-port-fix.json` y `_backups/optimizacion-20261104/`), `~/.claude/hooks/`, `~/.claude/skills-archivo/optimizacion-20261104/` (con `_LISTA.txt`), `~/.claude/CLAUDE.md`, ambos `GEMINI.md`.

## Mejoras propuestas
- Itemizar los ~45K de arranque que aún no se explican (plugins, agentes, reglas) con `/token-optimizer`.
- Abrir el panel en el navegador para ver el efecto visual de la recalibración; `baseline_state.json` (7-sep) sigue sin recalibrar.

## Pendientes
- Probar los dos hooks en sesión nueva; si fallan, restaurar `settings-pre-hooks.json`.
- Quitar los conectores de claude.ai que no se usen.

## Relacionado
- [[2026-11-02 - Token Coach, scripts zorin y progreso, revisión de skills]]
- [[2026-11-04 - Skills de vídeos de YouTube, limpieza de skills y MCPs (sesiones 4dce9f31 y 178671e5)]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
