---
type: sesion
origen: maquina
date: 2026-11-22
proyecto: "[[00_Meta/Informes/2026-11-22 - Revision nocturna y propuestas de mejora]]"
---

> [!resumen] En cristiano
> Revisión nocturna automática. No se movió ningún archivo (raíz ya ordenada). Se encontró `syslog.1` de ~104 GB aún en disco y el temporizador `comandai-sync` fallando. Informe con 7 hallazgos de harness, 10 propuestas y 6 apuestas; nada aplicado.

Informe: [[00_Meta/Informes/2026-11-22 - Revision nocturna y propuestas de mejora]].

## Aprendizajes
- El clasificador del modo auto bloquea llamadas Bash que el hook `rtk` reescribe; en tareas nocturnas conviene evitar comandos compuestos.
