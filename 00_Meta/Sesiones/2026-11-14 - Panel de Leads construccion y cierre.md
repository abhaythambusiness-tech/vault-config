---
title: "Sesión - 2026-11-14 - Panel de Leads construcción y cierre"
date: 2026-11-14
type: meta/sesion
origen: mixto
proyecto: "[[01_Projects/Panel de Leads]]"
tags:
  - sesion
aliases: []
---

# Sesión — 2026-11-14: Panel de Leads, construcción y cierre

> [!resumen] En cristiano
> Se construyó el Panel de Leads entero en un día: pipeline, lista, ficha, resumen semanal, login, alta de cliente por script y Docker con HTTPS. Funciona con datos de muestra y dentro de un contenedor; falta probarlo con un n8n real. Proyecto cerrado con su Retro.

## Contexto
Panel por cliente sobre las Data Tables de n8n del [[Setter NeoZeler]]. Documentos 1-6 aprobados el 13-nov. Repo: `~/Proyectos/panel-de-leads/`. Ficha: [[01_Projects/Panel de Leads]]. Retro: [[Retro]].

## Qué se hizo
- T-04 a T-13 del Plan: tabla `panel_estado`, cliente n8n, cruce de leads, pipeline, ficha, alta en Go, login y marca por instancia, Docker + Caddy, lista con búsqueda y filtro, resumen semanal.
- Verificado en el navegador a 375 y 1280 px y en un contenedor real en Zorin (usuario `ssh` añadido al grupo `docker` con permiso).
- Cierre: Retro, `resumen.html` en el repo y esta sesión.

## Decisiones tomadas
- API pública de n8n aunque la clave no se pueda acotar; mitigación: un VPS por cliente y clave solo en el servidor.
- Pipeline sin arrastre (selector «Mover a») porque 21st exige membresía.
- «Leads nuevos esta semana» queda fuera: las tablas no guardan fecha de alta.

## Aprendizajes (para futuras sesiones)
- Next (`.env.local`) y Compose expanden los `$`: hash con comillas simples en el `.env`, `\$` en `.env.local`.
- Probar el contenedor real con sus restricciones destapó un 0700 en la carpeta de la instancia que ningún test local veía.
- El lint de trazabilidad no perdona documentos «no aplica»: hay que citar las historias igualmente.

## Próximos pasos
- Probar con un n8n real y una clave nueva; **rotar la clave de prueba pegada en el chat**.
- Sincronizar `setter-neozeler/build.py` con los cambios manuales del workflow.
- Certificado real con dominio público; axe y Lighthouse; elegir referencias premium.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
