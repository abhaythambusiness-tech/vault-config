---
title: "Estructura del Vault y limpieza de la raíz - 2026-11-06"
date: 2026-11-06
type: meta/sesion
origen: mixto
proyecto: ""
sesion_id:
  - 09fddc25-8bfd-4e1c-b54d-f051447f4316
tags:
  - sesion
  - vault
aliases: []
---

# Estructura del Vault y limpieza de la raíz (6 nov 2026)

> [!resumen] En cristiano
> Haytham pidió una nota que describa todas las carpetas del vault. Claude la creó, y de paso propuso mover los archivos sueltos de la raíz a `99_Assets/` y borrar copias repetidas. Haytham dijo que sí a las dos cosas. No se perdió ningún dato: antes de cada borrado se comprobó que existía una copia idéntica.

## Qué se hizo
- Creada [[00_Meta/Estructura del Vault]]: árbol de `00_Inbox` a `99_Assets`, carpetas técnicas, detalle de `01_Projects` (incluido Dropshipping por dentro) y convenciones.
- Movidos 18 archivos de la raíz: los 5 pitch decks `Copia de …` y `CRITERIOS DE EVALUACION.pdf` a `99_Assets/Documentos/`, imágenes (`Oferta barber df.jpeg`, `ponytail-card.png`, etc.) a `99_Assets/Imagenes/`, HTML a `99_Assets/Html/`, material de Reto 30 a `99_Assets/reto-30/`.
- Borradas 8 copias de la raíz (1 PDF, 2 CSV, 3 imágenes, 2 txt). Se corrigió una cuenta anterior de 10: eran 8. Cada borrado se precedió de `cmp` contra una copia idéntica en `99_Assets/` o `00_Inbox/`.
- Al final aparecieron en la raíz 15 archivos 3D (los de Vault OS); hoy están en `99_Assets/3d/`.

## Decisiones
- Mover y borrar copias repetidas con permiso expreso de Haytham (dos «Sí»).
- Raíz limpia según la regla del `CLAUDE.md` del vault (solo `CLAUDE.md`, `GEMINI.md`, `.mcp.json`, `.ignore` y carpetas PARA/meta).

## Problemas
- Una cuenta inicial de borrados era errónea (10 en vez de 8); se corrigió antes de decirlo como hecho.
- Todo queda sin commit: en `git status` los movimientos aparecen como renombrados sin confirmar y los borrados como `D`.

## Pendientes
- Hacer commit por temas (la mezcla con otros trabajos del vault dificulta revisar).
- Actualizar `CLAUDE.md` y `GEMINI.md` si la nota de estructura pasa a ser referencia oficial (regla §0.5 del vault).

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
