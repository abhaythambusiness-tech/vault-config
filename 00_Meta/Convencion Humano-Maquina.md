---
title: Convención Humano-Máquina
date: 2026-11-04
type: meta/convencion
origen: humano
tags:
  - meta
  - convencion
aliases: []
---

> [!resumen] En cristiano
> Cada nota dice quién la hizo con una etiqueta: `origen: humano`, `maquina` o `mixto`. Lo tuyo, Claude no lo reescribe. Lo de máquina, Claude lo puede rehacer cuando toque. Lo mixto es un borrador de IA que tú revisas. Más adelante un script separará las carpetas usando solo esta etiqueta.

## Etiqueta (frontmatter)

| `origen` | Qué es | Qué hace Claude |
|---|---|---|
| `humano` | Escrito o decidido por Haytham: tareas, ideas, decisiones, notas propias | Lee. Solo edita si se lo pides y, por defecto, añadiendo; nunca reescribe ni borra |
| `maquina` | Salida de scripts o IA: novedades, logs, índices, informes automáticos | Puede regenerarlo o sobrescribirlo; no lo trata como decisión tuya |
| `mixto` | Borrador de IA que Haytham revisa o edita (fichas, sesiones, PRD) | Propone cambios; no sobrescribe. Cuando Haytham lo da por bueno se añade `revisado: true` |

Nota sin `origen`: se trata como `humano` (lo más prudente) hasta que se etiquete.

## Panel ComandAi

Misma idea en carpetas: `00_Meta/Panel/humano/` (tareas, pedidos a Claude) y `00_Meta/Panel/maquina/` (entrada de scripts, decisiones pendientes, diario de la IA). Claude usa `scripts/panel.py` del repo `~/Proyectos/comandai/`; no edita `humano/` a mano.

## Quién la usa

- Reglas para Claude: `~/.claude/rules/humano-maquina.md` y `CLAUDE.md` del vault (§0.14).
- Plantillas nuevas llevan `origen`. Para etiquetar notas antiguas: `python3 ~/Proyectos/flujo-software/tools/etiquetar_origen.py` (simulacro por defecto, `--aplicar` escribe).
- Fase 2 (pendiente): script que separe físicamente notas según `origen`. Antes, aprobar el resultado del etiquetado.
