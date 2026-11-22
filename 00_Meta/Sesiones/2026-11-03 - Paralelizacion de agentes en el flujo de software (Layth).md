---
title: "Sesión - 2026-11-03 - Paralelización de agentes en el flujo de software (Layth)"
date: 2026-11-03
type: meta/sesion
proyecto: ""
tags:
  - sesion
aliases: []
origen: mixto
---

# Sesión — 2026-11-03: Paralelización de agentes en el flujo de software (Layth)

> [!abstract] Resumen
> Haytham propuso un agente "Layth" (modelo barato, en paralelo) para optimizar el flujo de 6 documentos; se analizó el flujo real y se documentó dónde paralelizar compensa y dónde no, sin crear un agente nuevo.

## Contexto
Haytham pegó un análisis externo (generado con otra IA) sobre `Flujo Completo - Nuevo Proyecto de Software.html`, proponiendo un agente "Layth" que ejecutase tareas en paralelo con un modelo barato (tipo Haiku) en cada etapa del flujo de software ([[00 - Flujo de Software]]). Pidió revisar el flujo completo buscando optimizaciones, no solo esa idea, priorizando siempre el menor uso de tokens con el mayor rendimiento.

## Qué se hizo
- Se revisó `00 - Flujo de Software.md`, `~/.claude/rules/tokens.md` y la skill `superpowers:dispatching-parallel-agents` antes de responder.
- Se comprobó que el mecanismo pedido («Layth») ya existe en el harness: `Agent` con `subagent_type`/`model: haiku` y los forks (heredan contexto, sin coste de reconstrucción).
- Se identificaron los 4 puntos del flujo donde paralelizar compensa (Paso 0, identidad visual durante docs 3-6, revisión en fase Build, cierre) y por qué los documentos 1→6 no deben paralelizarse.
- Se añadió la sección «Paralelización de agentes (2026-11-03)» a `00 - Flujo de Software.md`.
- `graphify update .` (4160 nodos, 5633 aristas, 396 comunidades).

## Decisiones tomadas
- No se crea un agente "Layth" nuevo: sería redundante con `Agent`/fork + `investigador`/`archivista`/`revisor-codigo`/`auditor-web` (regla de no duplicar).
- Paralelizar solo en: investigación del Paso 0, búsqueda de identidad visual en paralelo con los docs 3-6, revisión multi-ángulo en Build (código/UX/UI/seguridad a la vez) y cierre (ya cubierto por `archivista`).
- Los documentos 1→6 se mantienen secuenciales: la aprobación de Haytham entre cada uno (§0.10 del `CLAUDE.md` del vault) es una barrera dura; paralelizarlos arriesga inconsistencias más caras que el tiempo que ahorrarían.

## Aprendizajes (para futuras sesiones)
> Solo lo no obvio.
- Un equipo de agentes en paralelo cuesta ~7× tokens frente a uno solo (regla ya fijada en `tokens.md`); por eso "más paralelismo" no es sinónimo de "menos tokens" — el ahorro real viene de agrupar peticiones, usar `vault-search`/`graphify` antes de research nuevo y reservar los equipos de agentes para tareas voluminosas y autocontenidas.
- Antes de proponer un agente nuevo para un patrón, comprobar si el harness ya lo resuelve (Agent tool + fork) y si una skill/agente existente ya lo cubre — evita construir una capa de orquestación que ya está disponible.

## Próximos pasos
-

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[00 - Flujo de Software]]
