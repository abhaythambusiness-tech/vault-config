---
title: "Sesión - 2026-08-25 - Personalización de Obsidian y grafo"
date: 2026-08-25
type: meta/sesion
proyecto: ""
sesion_id: 33467a5d-611c-408e-9b11-eea2c43b271a
tags:
  - sesion
  - cierre-automatico
aliases: []
origen: mixto
---

# Personalización de Obsidian y arreglo del grafo

> [!resumen] En cristiano
> Haytham quería su Obsidian más limpio, con los mismos colores pero sin fallos: nombres de notas que no se veían, grafo regular y colores rotos. Se rehízo la configuración, se añadió la referencia de diseño «Awesome Design» y se descubrió por qué el grafo volvía a estropearse.

## Contexto
Sesión de agosto, recogida hoy porque su archivo se volvió a tocar el 2026-11-02. Ya existe la nota detallada [[2026-08-26 - Fix de personalización del grafo de Obsidian]]; esta solo la resume y enlaza.

## Qué se hizo
- Limpieza de `snippets/graph.css`, `graph.json` y `appearance.json`.
- Borrado de `ai-tech-theme.css` y revisión del contenido del vault frente a la nueva configuración.
- Añadido «Awesome Design» al vault y a `CLAUDE.md` (dónde encontrarlo): [[03_Resources/Awesome Claude Design]].
- Obsidian se cerró, se reaplicó el arreglo del grafo, se abrió para comprobarlo y se mató el proceso en segundo plano.

## Decisiones tomadas
- Mantener los colores, pero con configuración limpia.

## Aprendizajes (para futuras sesiones)
- Obsidian **sobrescribe `graph.json` si el proceso sigue vivo en segundo plano**, aunque la ventana esté cerrada: hay que matar el proceso antes de editar y volver a abrir después.

## Próximos pasos
- Ninguno abierto.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[2026-11-02 - Cierre nocturno]]
