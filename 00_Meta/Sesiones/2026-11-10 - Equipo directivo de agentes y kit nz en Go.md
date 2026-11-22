---
title: "Sesión 2026-11-10 — Equipo directivo de agentes y kit nz en Go"
date: 2026-11-10
type: meta/sesion
origen: mixto
proyecto: "[[01_Projects/NeoZeler Tools]]"
tags: [sesion, agentes, neozeler, go]
---

# Sesión — 2026-11-10: equipo directivo de agentes y kit `nz` en Go

> [!resumen] En cristiano
> Haytham pidió un organigrama de agentes para NeoZeler (CEO, CFO, COO, CTO, CMO). Se crearon los cinco con sus skills, se optimizaron (contexto compartido, memoria, salida a archivo, modelos) y se les dio un kit de herramientas propio en Go. Todo está probado con datos reales, pero los agentes aún no se han usado en una tarea de verdad.

## Qué se hizo
- 5 agentes en `~/.claude/agents/neozeler-{ceo,cfo,coo,cto,cmo}.md`, todos `sonnet` salvo el COO en `haiku`, con `memory: user`.
- Hoja única de contexto: `[[02_Areas/NeoZeler/Estrategia/Contexto NeoZeler]]`; informes largos a `Estrategia/Informes/`.
- Skill manual `/direccion` (`~/.claude/skills/direccion/`): lanza CEO y reparte encargos en paralelo.
- Repo `~/Proyectos/neozeler-tools/` con el CLI `nz` (10 herramientas, 21 tests). Ficha: `[[01_Projects/NeoZeler Tools]]`.

## Decisiones y porqué
- **Go, no Python:** mismo stack que el Mini CRM Go, un binario sin dependencias de entorno.
- **Solo lectura:** las herramientas no escriben ni envían; lo externo lo decide Haytham.
- **Sin tarifas ni cifras inventadas:** `cto tokens` exige precios y `cfo` rotula sus supuestos.
- **`memory: user`** (fuera del repo del vault, que se sube solo a GitHub).

## Pendientes
- Usar `/direccion` en una decisión real y medir tokens.
- Confirmar con Haytham/Sam coste por hora, churn y precios finales; rellenar los huecos del Contexto.
- Decidir si algún agente necesita herramientas de escritura.
