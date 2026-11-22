---
title: "USB: perfil personal, reglas del amigo y panel de tokens - 2026-11-03"
date: 2026-11-03
type: meta/sesion
origen: mixto
proyecto: "Portable-NeoZeler"
sesion_id:
  - 98d508d9-344e-47fb-a34a-f081a6965285
  - c90dc0cd-c49a-4bc3-8719-f374b7145ce1
tags:
  - sesion
  - usb
  - token-optimizer
  - cierre-automatico
aliases: []
---

# USB: perfil personal, versión amigo y panel de tokens (3 nov 2026)

> [!resumen] En cristiano
> Haytham quería que, al enchufar el USB en otro ordenador, tuviera el mismo ahorro de tokens que aquí. Se encontró y quitó un ajuste que habría impedido conectar (una dirección local que solo existe en este PC), se completó la versión para un amigo con skills y reglas básicas, se arregló el panel de tokens y se volvió a empaquetar todo. Nada se probó todavía en otro ordenador.

Nota de cierre automático. La primera parte (menú de perfiles, `.mcp.json` portable, `Portable-Amigo`) ya estaba en [[2026-11-03 - USB con perfiles y version para amigo]]; aquí va lo que vino después. `c90dc0cd` es el arranque de la misma conversación.

## Qué se hizo
- Comprobación inicial: `.mcp.json` apuntaba a `/home/alumno2627/...` (8 servidores caídos); pasó a `${HOME}`. Reglas 8d, 11, 12 y 13 sincronizadas a `GEMINI.md`.
- `Portable-Amigo`: 24 skills de diseño y código añadidas (hallmark, impeccable, design-taste-frontend, diagram-design, humanizer, shadcn, accesslint-audit…), plantillas de `CLAUDE.md`/`GEMINI.md` sin datos personales y un juego de reglas base escritas desde cero (`empezar-proyecto.md`, `stack-web`, `verificacion-web`, `dashboards-saas`, `tokens`). La instalación no pisa skills que el amigo ya tenga. Mínimo garantizado: token-optimizer, caveman y ponytail.
- Perfil personal: el USB lleva los 121 plugins (17 activados como aquí, el resto apagados). Se detectó que `settings.json` llevaba `ANTHROPIC_BASE_URL=http://127.0.0.1:17094`, un proxy local; se quita al guardar y al instalar.
- Panel de token-optimizer: la tarjeta del límite semanal salía vieja porque el plugin lee `~/.claude/token-optimizer/rate-limits.json`, que solo se refresca desde la barra de estado; los «$211» son una estimación, no un gasto real. El aviso `CONNECTION_CLOSED` del servidor MCP del plugin no afecta al ahorro (lo dan hooks y skills).
- Re-empaquetado completo del USB (27 GB libres, sin errores) y estimación de tiempos por paso de `empaquetar.sh` (plugins ~1 min 40 s, Node ~35 s, Claude Code ~2 s).

## Decisiones
- Perfil personal con todos los plugins; amigo con lo mínimo más 24 skills básicas.
- Quitar `ANTHROPIC_BASE_URL` del `settings.json` empaquetado.
- Reglas del amigo escritas desde cero, no copiadas de las de Haytham.

## Problemas
- Falsos positivos del escáner de fugas (datos de prueba de plugins públicos; salto de línea vacío) — ver nota anterior.
- Panel con datos contradictorios (−1,1 % frente a $211): dato viejo del límite, no fallo grave.

## Pendientes
- Probar la instalación del USB en otro ordenador real (nunca se hizo; solo con `HOME` falso).
- Decidir si se arregla de verdad la lectura del límite semanal del panel.
- Investigar `plugin:token-optimizer` con `CONNECTION_CLOSED` (npx), no urgente.

## Relacionado
- [[2026-11-03 - USB con perfiles y version para amigo]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
