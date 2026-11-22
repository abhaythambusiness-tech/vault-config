---
date: 2026-11-13
type: informe
status: borrador
origen: mixto
fuente: https://github.com/walkinglabs/awesome-harness-engineering
---

> [!resumen] En cristiano
> El «harness» es todo lo que rodea a Claude: instrucciones, avisos automáticos (hooks), permisos y memoria. El tuyo ya es bueno: hooks en Go con tests, reglas por tema y destilado de esta misma lista el 12-nov. Los puntos flojos son pocos y concretos: nada impide un `rm` o `git reset` accidental (y hay un permiso que los aprueba solos), las tareas nocturnas no tienen tope de gasto, y no hay una comprobación automática de «terminado de verdad».

## Qué hay (verificado 2026-11-13)

- 10 hooks Go en `~/.claude/bin` (14 binarios, 1688 líneas, 42 tests Go pasan). Todos cargan y salen con exit 0; `guard-destructive` bloqueó en vivo un comando con «terraform destroy».
- Solo eventos `PreToolUse` y `PostToolUse` en `settings.json`. Ninguno con `timeout`.
- Permisos: 19 `deny`, 2 `ask`, 0 `allow` globales; el vault añade 41 `allow` en `.claude/settings.local.json`.
- 2 tareas programadas (`cierre-nocturno-sesiones` 02:00, `revision-nocturna-vault-mejoras` 04:00), 4 timers systemd de usuario.
- 11 archivos en `rules/` (~120 KB, cargados por `paths`), `CLAUDE.md` global 10 KB.

## Puntos débiles (por gravedad)

| # | Problema | Evidencia | Arreglo |
|---|---|---|---|
| 1 | **`rm` sin freno y auto-aprobado.** El vault permite `Bash(rm *)` y `Bash(rm -rf ~/.agents/skills)`. Ningún hook cubre `rm -rf`, `git reset --hard`, `git clean`, `git checkout .`. Tus reglas §0.2/§0.3 solo existen como texto. | `vault/.claude/settings.local.json`; `tools-go/cmd/guard-destructive/main.go` solo mira terraform, DROP, TRUNCATE, push forzado | Quitar `Bash(rm *)` del allow. Ampliar `guard-destructive` (Go): `rm -rf`/`-r` fuera de `/tmp` y del scratchpad, `git reset --hard`, `git clean -f`, `git checkout .`/`restore .` con árbol sucio (consultar `git status --porcelain`). Añadir casos a `main_test.go`. |
| 2 | **Tareas nocturnas sin cortacircuitos.** `harness.md` §5 exige límite de pasos, duración y coste; ninguna de las dos lo tiene. | `scheduled-tasks/*/SKILL.md` | Añadir a cada una: máximo N sesiones/archivos por noche, parar tras 3 errores iguales, y un tope de coste que se escriba en el informe. Comprobar que se cumple, no solo que está escrito. |
| 3 | **Nadie comprueba el «terminado».** La propia lista lo marca («don't let the agent grade its own homework»). No hay hook `Stop`. | `settings.json` solo tiene Pre/PostToolUse | Hook `Stop` en Go: si hubo ediciones de código y no hay build/test verde reciente en `Progreso.md`, avisar. Empezar en modo aviso, no bloqueo. |
| 4 | **`guard-secretos` solo mira `git commit/push`.** Un secreto escrito con `Edit/Write` en el vault se detecta tarde, y el vault se sube solo a GitHub (el mecanismo del auto-push no lo localicé: `comandai-sync` no hace commit). | `guard-secretos/main.go` | Pasar los mismos patrones por un hook `PreToolUse Edit|Write` sobre `content/new_string`. Localizar quién hace el auto-push y ponerle el mismo escáner. |
| 5 | **Reglas que viven solo como prosa.** CLAUDE.md pide «comprobar `git status` antes de destruir», «consultar COMMON_MISTAKES antes del primer Edit/Bash», «invocar `diseno-central`». Solo lo último tiene hook. `COMMON_MISTAKES.md` mide 52 KB y no se actualiza desde el 31-oct. | `.claude/COMMON_MISTAKES.md` | Regla de `harness.md` §6: lo que no puede fallar va en hook. Recortar COMMON_MISTAKES a lo vigente y buscar por dominio con `grep`, como ya dice el CLAUDE.md. |
| 6 | **Contexto inflado.** 9 plugins activos y 21 marketplaces; el listado de skills incluye cientos de ajenas a tu trabajo (`small-business:*`, `sales:*`, `finance:*`, `fastly-*`, `buildkite:*`, `qt-*`, `searchfit-seo:*`) y ~34 MCP pendientes de autorizar. Cada una pesa en cada sesión. | listado de skills de la sesión; `extraKnownMarketplaces` | Plugins de empresa que no usas: desactivar. Mismo criterio que el informe de uso del 2026-12-04 (`bin/informe-uso-skills 30`), pero adelantado para lo que ya se ve que no usas. Alternativa de la lista: perfiles por repo (`harness-scope`). |
| 7 | **`autoMode.environment` desordenado.** Entradas duplicadas y contradictorias: dos vaults distintos (`/Documentos/Haytham` y `/Documentos/vault`), «sin remotos» junto a un remoto configurado, un usuario con typo (`abhaythambusiden-tech`). | `settings.json` → `autoMode` | Dejar una sola versión correcta. El clasificador decide con ese texto. |
| 8 | **Sin timeouts en hooks y fallo silencioso.** Todos «fallan abierto» ante JSON ilegible (decisión razonable), pero ningún hook tiene `timeout` y nadie avisa si uno se rompe. | `settings.json`; `main.go` de cada hook | Poner `timeout` (5-10 s) a cada hook. Un `check-hooks` en Go, parecido a `check-mcps`, que ejecute cada binario con una entrada de prueba al arrancar la sesión. |
| 9 | **Logs sin tope.** `bash-commands.log` 3,5 MB, `cost-tracker.log` 3,6 MB, `projects/` 1,5 GB, `cleanupPeriodDays: 99999`. | `du` | Rotar los dos logs; bajar `cleanupPeriodDays` a un valor real (p. ej. 90). |
| 10 | **Sin evals.** Hay 42 tests de los hooks, pero ninguna medida de si las reglas, skills y agentes mejoran algo. Hay telemetría (`uso-skills`, `costs.jsonl`) sin lectura periódica automática. | `~/.claude/uso-skills`, `metrics/` | Empezar pequeño: 5-10 tareas fijas con comprobación determinista y repetirlas tras cada cambio grande del harness (patrón «OpenAI/OpenHands skill evals» de la lista). |

## Arreglado

- **#1 (2026-11-13):** quitados `Bash(rm *)`, `Bash(rm -rf ~/.agents/skills)` y `Bash(rmdir ~/.agents)` de `vault/.claude/settings.local.json`. `guard-destructive` (Go, `borrado.go` + tests) ahora bloquea `rm -r` fuera de `/tmp`, `git reset --hard`, y `git clean -f` / `git checkout .` / `git restore .` con cambios sin guardar. Límites: no cubre `rm` sin `-r`, ni `git checkout <archivo>`, ni comandos metidos en `bash -c`. Copias previas en el scratchpad de la sesión.

- **#2:** añadida sección «Cortacircuitos» a las dos tareas de `~/.claude/scheduled-tasks/` (tope de sesiones, minutos, llamadas, agentes; parar tras 3 fallos iguales; el informe dice si algún límite saltó). Falta comprobar en la primera noche que se cumplen.
- **#3:** nuevo hook `Stop` en Go, `verificar-cierre`: si se editó código y no hubo test/build/lint después, muestra un aviso. Solo avisa, no bloquea.
- **#4:** `guard-secretos` ahora también revisa lo que se escribe con `Edit`/`Write` (registrado en `settings.json`). Tests rehechos. Fallo mío: al añadir tests sobrescribí un `main_test.go` previo (2 tests, sin copia); lo reescribí con 4 tests que cubren cada patrón y el git.
- **#5:** no tocado. `COMMON_MISTAKES.md` no se carga solo (se consulta con `grep`), así que su tamaño no cuesta contexto, y recortarlo sería reescribir una nota tuya.
- **#6:** 181 skills de plugins de cuenta que no usas (sales, finance, small-business, fastly, buildkite, qt, base44, apollo, operations, data, engineering, product-management, enterprise-search, airtable, vpai, cowork) puestas en `name-only` en `skillOverrides`. Para quitarlas del todo hay que desactivar los plugins en claude.ai (no se puede desde aquí). Pendiente comprobar en sesión nueva que `plugin:skill` es una clave válida.
- **#7:** `autoMode.environment` de 33 a 25 líneas: quitadas las versiones antiguas contradictorias (ruta `/Haytham`, «sin remotos») y corregido el typo del usuario de GitHub.
- **#8:** `timeout` (10-30 s) en todos los hooks; nuevo `check-hooks` que se ejecuta al empezar cada sesión (`SessionStart`) y avisa si un hook se rompe.
- **#9:** `bash-commands.log` y `cost-tracker.log` (sin escritura desde el 25-oct) archivados en `~/.claude/logs-archivo/*.gz` y recortados a 3000 líneas. `cleanupPeriodDays` de 99999 a 180 (la sesión más vieja tiene 98 días, así que hoy no se borra nada).
- **#10:** `~/.claude/evals/hooks.json` con 17 casos fijos (qué debe bloquear o dejar pasar cada hook), ejecutados por `check-hooks`. Cubre hooks, no skills ni agentes: eso queda por hacer.

Copias previas en el scratchpad de la sesión: `settings.json.bak`, `scheduled-tasks.bak`.

## Lo que ya está bien (no tocar)

- Hooks en Go con tests y la regla «scripts nuevos en Go».
- `CLAUDE.md` corto + `rules/` por `paths` (lo que pide «Writing a good CLAUDE.md»).
- `run-silent` para contener salida de tests; `Owns:`/partición de archivos documentado; planes con `status: sustituido`.
- Marca `origen: humano|maquina|mixto` en notas.
- `deny` de lecturas sensibles (`.env`, `~/.ssh`, `~/.aws`).

## Orden recomendado

1. #1 (quitar `rm *`, ampliar guard): 30 min, el mayor riesgo real.
2. #4 y #7: pequeños, protegen el vault público-ish.
3. #2 y #8: topes y timeouts.
4. #3, #5, #6, #9, #10: según tiempo.

## Límites de esta auditoría

- No ejecuté los hooks con payloads reales de Claude Code más allá de la comprobación en vivo de `guard-destructive`.
- No verifiqué `guard-proyecto` ni `guard-ui-commit` en profundidad.
- No localicé el mecanismo del auto-push del vault.
- Un patrón `AKIA…` en `99_Assets/Html/Recorrido RETO 30.html` parece falso positivo (datos incrustados), sin confirmar.
