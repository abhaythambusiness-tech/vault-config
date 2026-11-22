---
type: sesion
origen: maquina
date: '2026-11-14'
proyecto: Vault
---

> [!resumen] En cristiano
> Revisión nocturna automática. Se movió 1 nota suelta de la raíz a `00_Inbox/`, se auditó vault y harness y se dejó el informe con 10 hallazgos, 20 propuestas y 6 apuestas.

Informe: [[00_Meta/Informes/2026-11-14 - Revision nocturna y propuestas de mejora]].

## Aprendizajes
- El hook de sandbox exige repetir exactamente las llamadas Bash que un hook reescribe (`rtk`).
- Los agentes CEO/CTO sin acceso al vault asumen cifras; hay que marcarlas como hipótesis.
- `bash-commands.log` y `cost-tracker.log` dejaron de escribirse el 2026-11-13 00:48.
