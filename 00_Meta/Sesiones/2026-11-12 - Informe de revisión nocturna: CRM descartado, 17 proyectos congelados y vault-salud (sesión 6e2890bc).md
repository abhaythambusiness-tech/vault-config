---
title: 'Informe de revisión nocturna: CRM descartado, proyectos congelados y vault-salud'
date: '2026-11-12'
type: meta/sesion
origen: mixto
proyecto: ''
sesion_id:
- 6e2890bc-04d9-4ff9-84b2-76f5bb5015c2
- 6cf329d3-bc7e-4fea-86a5-30358dcc0b20
tags:
- sesion
- cierre-nocturno
---

> [!resumen] En cristiano
> Haytham leyó el informe de la revisión nocturna y decidió: ningún CRM le convence y los 17 proyectos quedan congelados. Se aplicaron las mejoras seguras (herramienta `vault-salud` en Go con aviso semanal, ajuste de coste de agentes, arreglos de notas). Nada está commiteado.

## Qué se hizo
- Resumen de [[00_Meta/Informes/2026-11-12 - Revision nocturna y propuestas de mejora]] (la sesión `6cf329d3` fue el primer intento, interrumpido; se duplicó en `6e2890bc`).
- Memoria: «CRM: ninguno vigente». Notas corregidas en `Estado de Proyectos.md` y `Contexto NeoZeler.md` (aditivo).
- Los 17 proyectos ya figuraban `congelado` en sus fichas (cambio sin commit, autor desconocido).
- `CLAUDE_CODE_SUBAGENT_EFFORT=low` en `~/.claude/settings.json` (copia en `_backups/settings-20261113.json`).
- `vault-salud` en Go (`~/Proyectos/flujo-software/tools/vault-salud/`), temporizador systemd de usuario cada lunes 08:00 (primera vez 2026-11-16); genera `Salud del vault.md` y `Estado de Proyectos (auto).md`.
- Se corrigieron falsos positivos de la herramienta (barra `\` de tablas, adjuntos): enlaces rotos de 71 a 41.
- Notas mínimas `origen: maquina`: Roadmap de Reto-30 e `ingecons_architecture_and_schema`.
- `Estructura del Vault.md`: quitada la carpeta `ssh@192.168.0.100mp-crm-test/`, ya archivada.
- `graphify update .` (5.039 nodos); reindexado de `vault-search` quedó en segundo plano.
- Kit Digital explicado: ayuda del Gobierno vía Red.es.

## Decisiones tomadas
- Ningún CRM vigente (ni minicrm-go ni Neozeler CRM).
- Propuestas #24, #26, #27, #28, #31, #33 solo como «pendientes de aprobar» en `Contexto NeoZeler.md` §7. Haytham dijo «No, déjalos» a una última propuesta.

## Problemas
- `crontab` denegado: se usó systemd.
- Reindexado de `vault-search` superó 10 min.

## Pendientes y próximos pasos
- Aprobar lista cerrada de estados (CLAUDE.md §7), #30 Kit Digital (verificar Red.es/BOE) y #32 cold email (consultar gestor, LSSI art. 21).
- Revisar y commitear los cambios sin guardar.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

