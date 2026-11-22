---
type: sesion
date: 2026-11-02
proyecto: "[[01_Projects/Neozeler CRM]]"
origen: mixto
---
> [!resumen] En cristiano
> Rediseñé el CRM del servidor sin preguntar, como pidió Haytham: más claro, con buscador y acciones rápidas. Ya está en producción (puerto 8100).

## Aprendizajes
- `pkill -f` por línea de comandos mata también la sesión SSH que lo lanza y puede coincidir con el servicio real: matar por PID.
- En modo solo lectura faltaba la barra de selección y el JS se rompía; ahora está protegido.
- Los tests dependían de la vista «tarjetas» por defecto; ahora la lista lo es y las tarjetas se piden con `?vista=tarjetas`.
