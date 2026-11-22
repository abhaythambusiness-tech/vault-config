---
title: "Sesión - 2026-10-28 - Sistema de mejora continua de metodologías"
date: 2026-10-28
type: meta/sesion
proyecto: "[[Los Apuntes de Liyo]]"
tags:
  - sesion
aliases: []
origen: mixto
---

# Sesión — 2026-10-28: Sistema de mejora continua de metodologías

> [!resumen] En cristiano
> Hasta ahora cada proyecto empezaba de cero y los errores se repetían. Ahora cada proyecto empieza con una ficha (qué librerías, skills y referencias de diseño vamos a usar y por qué) y termina con una retro corta (qué salió mal y cuántos retoques pidió Haytham). Si la misma lección sale en dos retros, se propone mejorar la plantilla, y Haytham aprueba antes de tocarla. Un guardián automático (hook) obliga a cumplirlo, pero solo en los proyectos marcados con un archivo `.proyecto`.

## Contexto
Diseño aprobado en [[Diseno - Sistema de Mejora Continua de Metodologias]]. Piloto en [[Los Apuntes de Liyo]], donde Haytham vio diseños flojos. Se cuida el flujo de 6 documentos de [[00 - Flujo de Software]].

## Qué se hizo
- Plantillas nuevas en `00_Meta/Plantillas/Proyecto Software/`: `Ficha de Investigacion.md` y `Retro de Proyecto.md`.
- Notas nuevas: `03_Resources/Biblioteca de Referencias Premium.md` y `03_Resources/Registro de Retros.md` (tabla Dataview).
- Hook `~/.claude/hooks/guard_proyecto.py` con pruebas en `~/.claude/hooks/tests/`. Falla abierto: ante entrada inválida avisa por stderr y no bloquea.
- Registro del hook en `~/.claude/settings.json`. **settings.json modificado**; copia de seguridad en `~/.claude/_backups/settings-antes-guard-proyecto-20261028.json`.
- Skill `~/.claude/skills/nuevo-proyecto/SKILL.md`: marcador `.proyecto`, paso 1b (ficha), paso 8 «Cerrar», vía `web-cliente`.
- Agente `~/.claude/agents/archivista.md`: «Modo revisión de lecciones» (salida futura en `00_Meta/Propuestas de Plantillas/`, carpeta aún no creada).
- Piloto Los Apuntes de Liyo: marcador `.proyecto`, `Ficha de Investigacion.md` y `Retro.md` (pendiente).
- Documentación sincronizada: `~/.claude/CLAUDE.md` (punto «ciclo ficha → retro» de §4 y «Última actualización»), `CLAUDE.md` del vault (§0.10 y §2), `~/.claude/rules/skills-frecuentes.md`, y los dos `GEMINI.md`.

> El hook (Task 3) solo afecta a repos con un marcador `.proyecto` en la raíz; bots, scripts y proyectos antiguos quedan fuera.

## Decisiones tomadas
Decisiones de Haytham (diseño §7):
- Cubre desde el principio las 4 vías (web-cliente, micro-saas, saas, startup), cada una con sus extras.
- La retro la rellena Claude solo al cerrar; Haytham solo contesta los retoques.
- Referencias iniciales: las 8 webs vistas (Linear, Stripe, Raycast, Vercel, Apple Mac, Framer, Arc, Resend); gusto: premium y limpio, sin saturar.

Llamadas de diseño que Haytham debe revisar: umbral de 2 retros; ficha tras el PRD y antes del TRD; hook opt-in por marcador; `archivista` revisa con 3 retros sin revisar; web de cliente con versión corta del flujo.

## Aprendizajes (para futuras sesiones)
- Un retoque = cada petición de Haytham, tras la entrega, de corregir diseño, funcionalidad o fallo; la retro sin cifra queda `status: pendiente` y el hook no la da por cerrada.
- La coincidencia de lecciones es mecánica gracias a los campos `dominio` y `documento-destino`.

## Próximos pasos
Pendiente de Haytham (piloto Los Apuntes de Liyo):
- Confirmar el `tipo` de Liyo: ahora `micro-saas` **provisional** (la alternativa es `web-cliente`).
- Dar la cifra de **retoques** para completar la Retro (hoy `status: pendiente`).
- Después: crear `00_Meta/Propuestas de Plantillas/` solo cuando `archivista` genere la primera propuesta.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[Biblioteca de Referencias Premium]]
- [[Registro de Retros]]
