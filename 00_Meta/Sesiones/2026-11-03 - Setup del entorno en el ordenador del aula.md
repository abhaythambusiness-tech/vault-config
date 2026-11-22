---
title: "Sesión - 2026-11-03 - Setup del entorno en el ordenador del aula"
date: 2026-11-03
type: meta/sesion
proyecto: ""
tags:
  - sesion
aliases: []
origen: mixto
---

# Sesión — 2026-11-03: Setup del entorno en el ordenador del aula

> [!resumen] En cristiano
> Haytham instaló todo su entorno de trabajo (Claude Code, vault, claves, herramientas) en un ordenador del instituto usando el USB "Portable-NeoZeler". Casi todo quedó bien a la primera; tocó arreglar 3 rutas mal copiadas y se descubrió que ese ordenador no tiene instalado el programa `git` (y Haytham no tiene permiso para instalarlo él mismo).

> [!abstract] Resumen
> Instalación completa del entorno NeoZeler (Claude Code, vault, MCP, skills, secretos) en un equipo ajeno (`profesor-OptiPlex-3040`, usuario `alumno2627`) vía USB Portable-NeoZeler, con 3 rutas corregidas y un bloqueo real (sin `git`, sin sudo).

## Contexto
Primera vez usando el USB Portable-NeoZeler en un ordenador del aula, compartido con otras cuentas (`alumno`, `profesor`, `saul`). No hay proyecto concreto detrás, es puesta en marcha del entorno de trabajo.

## Qué se hizo
- Localizado el USB (montado como `/media/alumno2627/USB HAYTHAM/Portable-NeoZeler`, no en la ruta que se esperaba inicialmente).
- Leído `LEEME.md` del USB para confirmar el procedimiento.
- Ejecutado `usar.sh --secretos` (sin `--desktop`, sin sudo) directamente por Haytham (la contraseña del cifrado no pasó por el chat).
- Verificados binarios (`claude`, `node`, `uv`, `gh`, `graphify`, `headroom`, `rojo`, `rtk`, `zorin`, `progreso`), secretos descifrados (SSH, `~/.claude/reference` con permisos 600/700), `~/.claude.json`, `settings.json`, hooks, `skills-gtm/toggle.sh`, vault (509 notas + `.git`) y los dos `CLAUDE.md`.
- Corregidas 3 rutas en `~/.claude.json` que seguían apuntando a `/home/haytham/.../fnm/...` (MCP `context7`, `shadcn-registries`, `zorin-ssh`), que además usaban una ruta de `fnm` que no existe en este equipo (aquí `node` se instaló en `~/.local/opt/node`, no vía `fnm`). Se dejaron en `/home/alumno2627` con el PATH real.
- Detectado que `token-optimizer` (y sus skills `fleet-auditor`, `token-coach`, `token-dashboard`, `resume-checkpoint`) no aparecían en la sesión aunque estaban instalados y `enabled: true`: la lista de skills se cargó al arrancar la sesión, antes de que `usar.sh` instalara nada. Pendiente confirmar que aparecen tras abrir una terminal nueva.

## Decisiones tomadas
- Instalar con `--secretos` (necesario para que los MCP con claves funcionen) pero sin `--desktop` (no se necesita Claude Desktop en este equipo).
- No ejecutar `limpiar.sh` al terminar: Haytham va a seguir usando este mismo ordenador del aula próximamente, así que de momento se deja instalado.

## Aprendizajes (para futuras sesiones)
- El USB puede montarse con un nombre distinto al esperado (`USB HAYTHAM` en vez de `Portable-NeoZeler`); comprobar con `lsblk`/`ls /media/<usuario>` antes de asumir la ruta.
- `usar.sh` reescribe la mayoría de rutas `/home/haytham` automáticamente, pero **no todas**: los campos `env.PATH` y `env.SSH_MCP_KEY` dentro de `mcpServers` en `~/.claude.json` se quedaron con la ruta antigua en esta instalación. Revisar siempre `grep -c "/home/haytham" ~/.claude.json` tras un `usar.sh` antes de dar la instalación por buena.
- La ruta de Node que trae el USB no es la misma en todos los equipos: aquí `node` quedó en `~/.local/opt/node/bin`, no en `~/.local/share/fnm/node-versions/.../bin` (que es lo que tenían cableado los `env.PATH` de algunos MCP). Si un MCP de `npx` falla con ENOENT, comprobar primero `readlink -f ~/.local/bin/node` y ajustar el PATH a esa carpeta real, no asumir `fnm`.
- Los plugins/skills instalados o habilitados **durante** una sesión no aparecen en esa misma sesión (el listado de skills es un snapshot de arranque). Hace falta reiniciar `claude` para verlos, no basta con que `enabled: true` esté en `settings.json`.
- `zorin-ssh` (servidor `192.168.0.100`) da timeout desde este equipo porque es la red doméstica de Haytham, no la del aula: es una limitación de red esperada, no un fallo de instalación.
- Bloqueo real y no resoluble desde la sesión: este equipo no tiene `git` instalado y el usuario `alumno2627` no tiene sudo (`apt-cache policy git` muestra el paquete disponible pero "Instalados: (ninguno)"). Sin `git` no funciona nada del vault que dependa de él (status, commits, el auto-push a GitHub). Hace falta que alguien con sudo (profesor/admin del aula) instale `git`.

## Próximos pasos
- ~~Abrir una terminal nueva y confirmar que `token-optimizer` y sus skills aparecen ya en el listado.~~ Hecho: confirmado tras reiniciar sesión.
- ~~Gestionar la instalación de `git`...~~ Resuelto sin profesor/administrador (ver actualización).
- Si se vuelve a usar este mismo ordenador del aula más adelante y deja de ser necesario, recordar ejecutar `limpiar.sh` antes de irse (equipo no es suyo).

## Actualización (mismo día, sesión posterior)
El bloqueo de `git` sin sudo se resolvió sin esperar al profesor: `apt-get download git git-man` (no necesita sudo) + `dpkg-deb -x` en `~/.local/opt/git-portable/` + un wrapper en `~/.local/bin/git` que exporta `GIT_EXEC_PATH`/`GIT_TEMPLATE_DIR`. Con git funcionando, Claude Code resincronizó solo 11 marketplaces "fantasma" (declaradas en `settings.json` pero nunca clonadas); `caveman`, `ponytail` y `token-optimizer@alexgreensh-token-optimizer` necesitaron además `claude plugin marketplace add <owner>/<repo>` + `claude plugin install <id>@<marketplace>` manual (el formato debe ser exactamente `owner/repo`, no una URL, o falla por "network source differs"). También se corrigieron las rutas `/home/haytham` del `.mcp.json` del proyecto (no las tocaba `usar.sh`).

**Llevado al USB** (`Portable-NeoZeler`, mismo día): `usar.sh` instala git-portable solo si falta y no hay sudo (paquete nuevo `git-portable.tar.gz`, paso "2b/10"); reescribe el `.mcp.json` del proyecto tras traer el vault (antes no lo cubría); avisa al final que los plugins activados a mitad de sesión necesitan una terminal nueva. Detalle completo en `LEEME.md` del USB, sección «Aprendizajes (2026-11-03, ordenador del aula)».

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
