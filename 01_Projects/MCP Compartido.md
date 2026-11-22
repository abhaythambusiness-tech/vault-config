---
type: proyecto
status: en-progreso
date: 2026-11-17
repo: ~/Proyectos/mcp-compartido
origen: mixto
---

> [!resumen] En cristiano
> Una carpeta `Compartido/` que existe igual en tu vault, en el del CEO y en Zorin, y se copia sola entre los tres en segundos (lo hace Syncthing, un programa que sincroniza carpetas). El MCP en Go es lo que permite que Claude Code de cada uno lea, busque y escriba ahí sin pisar lo del otro. Del resto de tu vault no sale nada.

## Decisiones
- **Zorin como intermediario**: sí. Está siempre encendido; los dos PCs solo se emparejan con él.
- **Solo una carpeta, no el vault entero**: el vault tiene notas privadas y hace auto-push a GitHub.
- **Sincronizar con Syncthing, no con código propio**: ya está instalado en Zorin y resuelve conflictos y reconexión.
- **MCP stdio sobre la copia local**, no HTTP: más simple, funciona sin red, sin token que exponer.

## Alcance hecho (2026-11-17)
- MCP en Go sin dependencias: `listar`, `leer`, `buscar`, `escribir` (con `hash_base` anticonflicto), `cambios`. 5 tests pasan; probado por JSON-RPC.
- README con instalación y pasos de Syncthing para los 3 equipos.

## Pendiente
- Arrancar Syncthing en Zorin y emparejar los 3 equipos (hace falta el ID del PC del CEO).
- Añadir `Compartido/` al `.gitignore` del vault (si no, el auto-push sube las notas del CEO a GitHub) y excluirla de `vault-search`/graphify si se quiere.
- Registrar el MCP en Claude Code de ambos (`claude mcp add`, comando en el README).
- Binario para el sistema operativo del CEO (compilar aquí).
- Reglas de convivencia: una subcarpeta por persona + una común; no editar la misma nota a la vez.

## Riesgos
- Syncthing abre el puerto 22000 en Zorin (cifrado, solo dispositivos emparejados).
- Nunca poner secretos en `Compartido/`.
