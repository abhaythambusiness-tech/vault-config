---
type: referencia
status: activo
date: '2026-11-03'
proyecto: '[[01_Projects/ComandAi/1 - PRD]]'
---

> [!resumen] En cristiano
> Carpeta de datos del panel ComandAi. `humano/` es lo que escribes o decides tú, tal cual. `maquina/` es lo que traen los scripts y clasifica la IA. No mezclar.

- `humano/`: tus tareas, notas y decisiones. La IA lee, no reescribe.
- `maquina/entrada/`: datos crudos de scripts Python (sin IA), un archivo por día y fuente.
- `maquina/util/`: lo que la IA marcó como útil de `entrada/`.
- `maquina/logs/`: qué hizo la IA y cuándo.

## Protocolo para Claude Code (panel bidireccional)

Haytham usa el panel (`http://localhost:8200`); Claude Code lee y escribe los mismos archivos con `~/Proyectos/comandai/scripts/panel.py` (env `COMANDAI_PANEL` = esta carpeta). El panel se refresca solo.

```bash
python3 ~/Proyectos/comandai/scripts/panel.py tarea list|add "texto" [--dia AAAA-MM-DD]|done "fragmento"
python3 ~/Proyectos/comandai/scripts/panel.py pedidos list|done "fragmento"     # lo que Haytham pide a Claude
python3 ~/Proyectos/comandai/scripts/panel.py decision add "título" --detalle "..." | list
python3 ~/Proyectos/comandai/scripts/panel.py diario add "qué hice"
```

Al empezar sesión: `pedidos list` y `decision list`. Al terminar algo: `diario add`. Cuando necesites un sí/no de Haytham: `decision add`, no preguntar en el chat si puede esperar.
