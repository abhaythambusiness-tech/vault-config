---
type: plan
status: borrador
date: '2026-10-28'
tags:
- metodologia
- mejora-continua
---

# Sistema de Mejora Continua de Metodologías: plan de construcción

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Que cada proyecto (web de cliente, micro-SaaS, SaaS, startup) pase por una ficha de investigación antes de construir y una retro al cerrar, con un hook que lo exige y un proceso que sube las lecciones repetidas a las plantillas.

**Architecture:** Plantillas y notas de Markdown en el vault (ficha, retro, biblioteca de referencias, registro Dataview), un hook de Python (solo biblioteca estándar) que lee un archivo marcador `.proyecto` en cada repo, y cambios en la skill `/nuevo-proyecto` y el agente `archivista` para crear y revisar esos documentos. Opt-in: lo que no tiene marcador no se toca.

**Tech Stack:** Markdown + Dataview (vault), Python 3.12 con `unittest` (no hay pytest instalado), `~/.claude/settings.json` para registrar el hook.

**Spec:** `[[00_Meta/Diseno - Sistema de Mejora Continua de Metodologias]]` (aprobado por Haytham el 2026-10-28).

> [!resumen] En cristiano
> Se construyen siete piezas pequeñas: dos plantillas (ficha y retro), dos notas de apoyo (referencias premium y tabla de retros), un vigilante automático (hook) que impide empezar a programar sin ficha o cerrar sin retro, la puesta al día de la skill que arranca proyectos y del agente que revisa lecciones, y un piloto con `los-apuntes-de-liyo`. Nada toca tus proyectos actuales hasta que les pongas un marcador.

## Global Constraints

- Lenguaje sencillo y recuadro `> [!resumen] En cristiano` de 3-5 líneas al inicio de cada nota nueva (global §1, vault §0.11).
- Notas nuevas solo en `00_Meta/` y `03_Resources/`; no reorganizar PARA (vault §0.2).
- Ficha: máximo 1 página. Retro: máximo 10 líneas de contenido.
- Marcador `.proyecto` en la raíz del repo, formato `clave: valor` por línea, claves `nombre-vault` y `tipo`; `tipo` ∈ `web-cliente | micro-saas | saas | startup`.
- Ficha en `01_Projects/<nombre-vault>/Ficha de Investigacion.md`; retro en `01_Projects/<nombre-vault>/Retro.md`; ficha va después del PRD y antes del TRD.
- Retro completa = frontmatter `status: completa` y `retoques:` entero. Pendiente = `status: pendiente`.
- Umbral de subida a plantillas: 2 retros con el mismo par `dominio` + `documento-destino`; `archivista` revisa cuando hay 3 retros con `revisada: false`.
- Haytham aprueba antes de modificar cualquier plantilla existente; `archivista` solo escribe propuestas nuevas.
- El hook falla abierto: ante entrada inválida o marcador malformado sale con código 0 (solo avisa por stderr).
- Sin secretos en el vault (auto-push). Cambios en `CLAUDE.md` o `rules/` se replican en ambos `GEMINI.md` en el mismo turno.
- Copia de seguridad de `~/.claude/settings.json` antes de editarlo.

## Review Focus

Entradas o fallos que el diseño implica y cada tarea fija con una prueba:
1. Marcador `.proyecto` sin `nombre-vault` o con `tipo` desconocido: el hook no bloquea y avisa (Task 3).
2. Edición de un archivo muy anidado (`src/a/b/c.ts`): el marcador se encuentra subiendo carpetas (Task 3).
3. Archivos que NO son código (`.md`, `.gitignore`, `package.json`, `spec.md`, `.proyecto`) no se bloquean aunque falte la ficha (Task 3).
4. `retoques: dos` o vacío no cuenta como retro completa (Task 3).
5. `git commit -m "fix: release notes"` no se bloquea; solo mensajes que empiezan por `release` o `cierre` (Task 3).

---

## File Structure

| Archivo | Responsabilidad |
|---|---|
| `00_Meta/Plantillas/Proyecto Software/Ficha de Investigacion.md` | Plantilla de la ficha |
| `00_Meta/Plantillas/Proyecto Software/Retro de Proyecto.md` | Plantilla de la retro |
| `03_Resources/Biblioteca de Referencias Premium.md` | Referencias por tipo de proyecto |
| `03_Resources/Registro de Retros.md` | Tabla Dataview de retros y tendencia |
| `~/.claude/hooks/guard_proyecto.py` | Lógica y entrada del hook |
| `~/.claude/hooks/tests/test_guard_proyecto.py` | Pruebas `unittest` del hook |
| `~/.claude/settings.json` | Registro del hook (modificar) |
| `~/.claude/skills/nuevo-proyecto/SKILL.md` | Marcador, ficha, tipo `web-cliente`, paso «cerrar» (modificar) |
| `~/.claude/agents/archivista.md` | Revisión de lecciones (modificar) |

---

### Task 1: Plantillas de ficha y retro

**Files:**
- Create: `00_Meta/Plantillas/Proyecto Software/Ficha de Investigacion.md`
- Create: `00_Meta/Plantillas/Proyecto Software/Retro de Proyecto.md`

**Interfaces:**
- Produces: frontmatter de la ficha `{type: ficha-investigacion, proyecto, tipo, status: borrador|aprobada, date}`; frontmatter de la retro `{type: retro, proyecto, tipo, status: pendiente|completa, retoques: <entero|vacío>, revisada: false, date}`. Tasks 3, 4, 5 y 6 dependen de estos nombres.
- Cuerpo de la ficha, secciones `##` en este orden: `Librerías`, `Skills y agentes`, `Referencias`, `Lecciones aplicables`, `Extras de la vía`.
- Cuerpo de la retro, secciones `##`: `Retoques`, `Nivel frente a referencias`, `Skills previstas vs usadas`, `Librerías`, `Lecciones`; cada lección es una fila de tabla con columnas `Síntoma | Causa | Regla | dominio | documento-destino`, donde `documento-destino` ∈ `PRD | TRD | UI-UX | AppFlow | Schema | Plan`.

- [ ] **Step 1: Verificación que debe fallar**

Run: `ls "00_Meta/Plantillas/Proyecto Software/" | grep -E "Ficha de Investigacion|Retro de Proyecto"`
Expected: sin salida (no existen).

- [ ] **Step 2: Crear la ficha con `obsidian-vault.create_note` (frontmatter como dict)**

Cada sección lleva una línea de instrucción. `Librerías`: tabla `Necesidad | Candidata A | Candidata B | Elegida y motivo | Fuente` con la orden de búsqueda (`librerias.md` → `vault-search` → context7 → internet). `Extras de la vía`: cuatro subapartados `web-cliente` (marca e imágenes), `micro-saas` (señal de demanda y `[[Checklist pre-cobro (micro SaaS)]]`), `saas` (multi-equipo y RLS), `startup` (métricas e inversión); el proyecto borra los tres que no apliquen.

- [ ] **Step 3: Crear la retro con `create_note`**

Una línea bajo `Retoques`: «Cada petición de Haytham, tras la entrega, de corregir diseño, funcionalidad o un fallo de lo entregado». Claude cuenta las peticiones en la sesión, escribe la cifra y la confirma con Haytham antes de poner `status: completa`.

- [ ] **Step 4: Verificar**

Run: `cd "00_Meta/Plantillas/Proyecto Software" && grep -c "^## " "Ficha de Investigacion.md" "Retro de Proyecto.md" && grep -E "^(retoques|revisada|status):" "Retro de Proyecto.md"`
Expected: `5` para cada archivo y las líneas `retoques:`, `revisada: false`, `status: pendiente`.

- [ ] **Step 5: Commit**

```bash
git add "00_Meta/Plantillas/Proyecto Software/Ficha de Investigacion.md" "00_Meta/Plantillas/Proyecto Software/Retro de Proyecto.md"
git commit -m "docs: plantillas de ficha de investigacion y retro de proyecto"
```

---

### Task 2: Biblioteca de referencias y registro de retros

**Files:**
- Create: `03_Resources/Biblioteca de Referencias Premium.md`
- Create: `03_Resources/Registro de Retros.md`

**Interfaces:**
- Consumes: frontmatter de la retro de Task 1.
- Produces: biblioteca con tabla `Referencia | URL | Tipo de proyecto | Qué tomar | Aviso`; consulta Dataview del registro.

- [ ] **Step 1: Crear la biblioteca**

Ocho filas con estas URLs exactas: `linear.app`, `stripe.com`, `raycast.com`, `vercel.com`, `apple.com/mac`, `framer.com`, `arc.net`, `resend.com`. Tipo y «qué tomar» según lo mostrado a Haytham (SaaS oscuro sobrio; claro con color y detalle; app con brillos; minimalismo técnico; historia al hacer scroll; atrevido y creativo; marca con carácter; serif elegante). Columna `Aviso`: «puede saturar: tomar la idea, no la densidad». Regla al inicio: **premium pero limpio; menos elementos, mejor ejecutados**. Sección final «Cómo se amplía»: solo con referencias aprobadas por Haytham.

- [ ] **Step 2: Crear el registro con esta consulta Dataview**

````
```dataview
TABLE tipo AS "Vía", date AS "Fecha", retoques AS "Retoques", status AS "Estado", revisada AS "Revisada"
FROM "01_Projects"
WHERE type = "retro"
SORT date DESC
```
````
Más una segunda consulta con `WHERE type = "retro" AND revisada = false AND status = "completa"` y `length(rows)` por `GROUP BY true`, titulada «Retros sin revisar (3 activan a archivista)».

- [ ] **Step 3: Verificar**

Run: `grep -c "https\?://\|\.net\|\.app\|\.com" "03_Resources/Biblioteca de Referencias Premium.md"; grep -c '```dataview' "03_Resources/Registro de Retros.md"`
Expected: al menos `8` y `2`.

- [ ] **Step 4: Commit**

```bash
git add "03_Resources/Biblioteca de Referencias Premium.md" "03_Resources/Registro de Retros.md"
git commit -m "docs: biblioteca de referencias premium y registro de retros"
```

---

### Task 3: Hook `guard_proyecto.py` (con pruebas primero)

**Files:**
- Create: `~/.claude/hooks/tests/test_guard_proyecto.py`
- Create: `~/.claude/hooks/guard_proyecto.py`
- Modify: `~/.claude/settings.json` (registro, Step 8)

**Interfaces:**
- Produces, en `guard_proyecto.py`:
  - `VAULT = "/home/haytham/Documentos/vault"` (constante; las pruebas la reemplazan con `unittest.mock.patch`).
  - `read_marker(start: str) -> dict[str, str] | None`: sube desde `start` buscando `.proyecto`; devuelve dict con `nombre-vault` y `tipo`, o `None` si no hay marcador o es inválido (falta `nombre-vault` o `tipo` fuera de la lista).
  - `is_source_code(path: str) -> bool`: `True` solo para extensiones `.ts .tsx .js .jsx .mjs .py .css .html .sql .svelte .vue`; `False` para `.md`, `.json`, `.toml`, `.yml`, `.yaml`, `.gitignore`, `.proyecto`, `.env*` y cualquier ruta bajo `node_modules/`, `dist/`, `build/`, `.next/`.
  - `ficha_exists(marker: dict[str, str]) -> bool`: existe `{VAULT}/01_Projects/{nombre-vault}/Ficha de Investigacion.md`.
  - `retro_complete(nombre_vault: str) -> bool`: existe `Retro.md` con `status: completa` y `retoques:` entero.
  - `decide(payload: dict) -> tuple[int, str]`: `(0, "")` permite; `(2, mensaje)` bloquea. Reglas: (a) `Edit|Write` de código con marcador válido y sin ficha → bloquea; (b) `Bash` con comando `git tag ...` o `git commit` cuyo mensaje (`-m`) empieza por `release` o `cierre` (sin distinguir mayúsculas), ejecutado con `cwd` dentro de un repo con marcador y sin `retro_complete` → bloquea; (c) `Edit|Write` cuyo `file_path` está en `{VAULT}/01_Projects/<Nombre>.md` y cuyo contenido nuevo (`content` o `new_string`) contiene `status: cerrado`, con `Retro.md` de `01_Projects/<Nombre>/` sin completar → bloquea.
  - `main() -> int`: lee JSON de stdin, llama a `decide`, imprime el mensaje en stderr y devuelve el código; cualquier excepción devuelve 0.

- [ ] **Step 1: Escribir las pruebas que fallan**

En `test_guard_proyecto.py`, con `unittest` y directorios temporales para repo y vault (parcheando `VAULT`). Una clase por regla. Nombres y aserciones:
  - `test_marker_found_from_deep_path`: marcador en la raíz, ruta `repo/src/a/b/c.ts` → `read_marker` devuelve `{"nombre-vault": "X", "tipo": "web-cliente"}`.
  - `test_marker_missing_name_returns_none` y `test_marker_unknown_tipo_returns_none`.
  - `test_source_extensions`: `.ts` y `.py` → `True`; `spec.md`, `package.json`, `.gitignore`, `.proyecto`, `repo/node_modules/x.js` → `False`.
  - `test_edit_blocked_without_ficha`: `decide({"tool_name": "Edit", "tool_input": {"file_path": ".../src/app.ts"}})[0] == 2` y el mensaje contiene `Ficha de Investigacion`.
  - `test_edit_allowed_with_ficha`: tras crear la ficha → `0`.
  - `test_edit_allowed_without_marker`: repo sin `.proyecto` → `0`.
  - `test_markdown_allowed_without_ficha`: `.../README.md` → `0`.
  - `test_retro_complete_requires_integer`: `retoques: dos` → `retro_complete` `False`; `retoques: 2` y `status: completa` → `True`; `status: pendiente` → `False`.
  - `test_commit_release_blocked_without_retro`: Bash `git commit -m "release: v1"` con `cwd` en repo con marcador → `2`.
  - `test_commit_normal_allowed`: `git commit -m "fix: release notes"` → `0`.
  - `test_tag_blocked_without_retro`: `git tag v1.0.0` → `2`.
  - `test_cerrar_note_blocked_without_retro`: Write a `{VAULT}/01_Projects/X.md` con `status: cerrado` y sin retro completa → `2`.
  - `test_invalid_payload_fails_open`: `main()` con stdin `"no es json"` → `0`.

- [ ] **Step 2: Ejecutar y ver que fallan**

Run: `cd ~/.claude/hooks && python3 -m unittest discover -s tests -v`
Expected: `ModuleNotFoundError: No module named 'guard_proyecto'`.

- [ ] **Step 3: Implementar `guard_proyecto.py`**

Cabecera de docstring en el estilo de `guard-web.py` (`"""PreToolUse (Edit|Write|Bash): ..."""`), solo biblioteca estándar, firmas de la sección Interfaces. Mensajes de bloqueo en español, una línea cada uno, que digan qué falta y dónde crearlo (por ejemplo «Bloqueado por guard-proyecto: falta `01_Projects/X/Ficha de Investigacion.md`. Créala con /nuevo-proyecto antes de programar»). El módulo se ejecuta con `if __name__ == "__main__": sys.exit(main())`. Nota: el nombre lleva guion bajo para poder importarlo en las pruebas; el comando registrado usa ese mismo nombre.

- [ ] **Step 4: Ejecutar y ver que pasan**

Run: `cd ~/.claude/hooks && python3 -m unittest discover -s tests -v`
Expected: todas las pruebas `ok`, `OK` al final.

- [ ] **Step 5: Prueba manual del arranque real**

Run: `echo '{"tool_name":"Edit","tool_input":{"file_path":"/tmp/nada/x.ts"}}' | python3 ~/.claude/hooks/guard_proyecto.py; echo "código=$?"`
Expected: `código=0`.

- [ ] **Step 6: Copia de seguridad de `settings.json`**

Run: `cp ~/.claude/settings.json ~/.claude/_backups/settings-antes-guard-proyecto-20261028.json`
Expected: el archivo copiado existe (`ls ~/.claude/_backups/ | grep guard-proyecto`).

- [ ] **Step 7: Registrar el hook**

En `hooks.PreToolUse` de `~/.claude/settings.json` añadir el comando `python3 $HOME/.claude/hooks/guard_proyecto.py` con `matcher: "Edit|Write|Bash"`, como entrada nueva (sin tocar `guard-web` ni `guard-destructive`). Usar la skill `update-config`. Validar el JSON:

Run: `python3 -c "import json;d=json.load(open('/home/haytham/.claude/settings.json'));print([h['matcher'] for h in d['hooks']['PreToolUse']])"`
Expected: la lista incluye `'Edit|Write|Bash'`.

- [ ] **Step 8: Commit** (solo lo que esté bajo control de versiones; `~/.claude` no es repo, así que se deja constancia en la sesión de Task 7)

---

### Task 4: Skill `/nuevo-proyecto`

**Files:**
- Modify: `~/.claude/skills/nuevo-proyecto/SKILL.md`

**Interfaces:**
- Consumes: plantillas de Task 1, formato del marcador (Global Constraints), `retro_complete` de Task 3 como criterio de cierre.

- [ ] **Step 1: Verificación que debe fallar**

Run: `grep -c "Ficha de Investigacion\|\.proyecto\|web-cliente" ~/.claude/skills/nuevo-proyecto/SKILL.md`
Expected: `0`.

- [ ] **Step 2: Editar la skill (cinco cambios puntuales)**

  1. Línea 12 (paso 0): sustituir el nombre antiguo de la nota por `01 - Tipos de producto (Micro SaaS, SaaS, Startup).md` y ofrecer cuatro vías: añadir `web-cliente` (PRD + UI-UX + Plan, resto `no-aplica` con motivo).
  2. Paso 3 de «Arranque»: además de las plantillas, crear en el repo `~/Proyectos/<nombre>/.proyecto` con `nombre-vault:` y `tipo:`.
  3. Nueva sección «1b. Ficha de investigación» entre PRD y TRD: copiar `Ficha de Investigacion.md` a `01_Projects/<Nombre>/`, rellenarla (librerías con las fuentes en orden, skills por fase de `rules/skills-frecuentes.md`, 2-3 referencias de `Biblioteca de Referencias Premium.md`, lecciones de `COMMON_MISTAKES.md` y de retros de la misma vía) y pasar a `status: aprobada` con Haytham. Sin ella, el hook bloquea el código.
  4. Nueva sección «8. Cerrar» al final del flujo: crear `Retro.md` desde la plantilla, contar las peticiones de corrección de Haytham tras la entrega, mostrarle la cifra, ajustarla con su respuesta y poner `status: completa`; después añadir la fila a las lecciones con `dominio` y `documento-destino`, y cambiar el `status` de `01_Projects/<Nombre>.md` a `cerrado`. Si hay 3 retros con `revisada: false`, lanzar el agente `archivista` en modo revisión (Task 5).
  5. Sección «Aprendizaje» final: añadir «la retro es la vía principal; no duplicar en notas sueltas».

- [ ] **Step 3: Verificar**

Run: `grep -c "Ficha de Investigacion" ~/.claude/skills/nuevo-proyecto/SKILL.md; grep -c "web-cliente" ~/.claude/skills/nuevo-proyecto/SKILL.md; grep -c "Micro SaaS vs Startup SaaS" ~/.claude/skills/nuevo-proyecto/SKILL.md`
Expected: al menos `1`, al menos `1` y `0`.

---

### Task 5: Agente `archivista` en modo revisión

**Files:**
- Modify: `~/.claude/agents/archivista.md`

**Interfaces:**
- Consumes: retros con `revisada: false`, `status: completa` (Task 1); `Registro de Retros` (Task 2).
- Produces: nota `00_Meta/Propuestas de Plantillas/YYYY-MM-DD.md` con una tabla `dominio | documento-destino | retros que la citan | regla propuesta | plantilla a modificar`.

- [ ] **Step 1: Leer el agente y comprobar que no menciona retros**

Run: `grep -c "Retro" ~/.claude/agents/archivista.md`
Expected: `0`.

- [ ] **Step 2: Añadir la sección «Modo revisión de lecciones»**

Pasos del modo: listar retros con `list_notes(type="retro")`, filtrar `revisada: false` y `status: completa`; agrupar lecciones por par `dominio` + `documento-destino`; proponer solo los pares con 2 o más retros; escribir la propuesta en `00_Meta/Propuestas de Plantillas/` (nota nueva con `create_note`); **nunca editar plantillas ni retros**; devolver a Haytham la ruta de la propuesta y qué retros incluyó. Al aplicar Haytham la propuesta (acción suya), las retros se marcan `revisada: true`.

- [ ] **Step 3: Verificar**

Run: `grep -c "revisada" ~/.claude/agents/archivista.md; grep -c "nunca editar plantillas" ~/.claude/agents/archivista.md`
Expected: al menos `1` y `1`.

---

### Task 6: Piloto con `los-apuntes-de-liyo`

**Files:**
- Create: `~/Proyectos/los-apuntes-de-liyo/.proyecto`
- Create: `01_Projects/Los Apuntes de Liyo/Ficha de Investigacion.md`
- Create: `01_Projects/Los Apuntes de Liyo/Retro.md`

**Interfaces:**
- Consumes: plantillas (Task 1), hook (Task 3).

- [ ] **Step 1: Marcador**

Contenido exacto de `.proyecto`: `nombre-vault: Los Apuntes de Liyo` y `tipo: web-cliente`... **Comprobar antes** con Haytham si Liyo es micro-SaaS o web-cliente; usar el valor que confirme.

- [ ] **Step 2: Verificar que el hook bloquea sin ficha**

Run: `echo '{"tool_name":"Edit","tool_input":{"file_path":"/home/haytham/Proyectos/los-apuntes-de-liyo/src/x.ts"}}' | python3 ~/.claude/hooks/guard_proyecto.py; echo "código=$?"`
Expected: mensaje de bloqueo y `código=2`.

- [ ] **Step 3: Ficha retroactiva**

Crear la ficha desde la plantilla con lo que ya se decidió en el TRD y UI-UX del proyecto, y anotar en `Lecciones aplicables` el motivo del piloto (diseños poco cuidados vistos por Haytham). `status: aprobada`.

- [ ] **Step 4: Verificar que el hook permite con ficha**

Run: el mismo comando del Step 2.
Expected: `código=0`.

- [ ] **Step 5: Retro**

Crear `Retro.md`. Contar las peticiones de corrección de Haytham sobre Liyo y **preguntarle la cifra** (única pregunta). Hasta que conteste: `status: pendiente`.

- [ ] **Step 6: Verificar el registro**

Run: `grep -E "^(status|retoques|revisada):" "01_Projects/Los Apuntes de Liyo/Retro.md"`
Expected: las tres líneas presentes.

- [ ] **Step 7: Commit** (vault y, aparte, el repo del proyecto con el marcador)

```bash
git add "01_Projects/Los Apuntes de Liyo/Ficha de Investigacion.md" "01_Projects/Los Apuntes de Liyo/Retro.md"
git commit -m "docs: piloto del sistema de mejora en Los Apuntes de Liyo"
cd ~/Proyectos/los-apuntes-de-liyo && git add .proyecto && git commit -m "chore: marcador .proyecto para el sistema de mejora"
```

---

### Task 7: Sincronización y cierre de documentación

**Files:**
- Modify: `~/.claude/CLAUDE.md` (§4 y §5), `/home/haytham/Documentos/vault/CLAUDE.md` (§0.10 y §2)
- Modify: `~/.claude/rules/skills-frecuentes.md`
- Modify: `~/.gemini/config/GEMINI.md`, `00_Meta/GEMINI.md`
- Create: `00_Meta/Sesiones/2026-10-28 - Sistema de mejora continua de metodologias.md`

- [ ] **Step 1: Añadir cuatro líneas, sin reescribir secciones**

En ambos `CLAUDE.md`: el ciclo (ficha → retro → subida), el marcador `.proyecto`, el hook `guard_proyecto.py` y las dos notas nuevas. En `skills-frecuentes.md`: la retro como cierre obligatorio. Actualizar la línea «Última actualización» del global.

- [ ] **Step 2: Replicar en los dos `GEMINI.md`** (regla de sincronía) con el mismo texto.

- [ ] **Step 3: Nota de sesión** desde `Plantilla - Sesion`, con las llamadas de Haytham (§7 del diseño) y los archivos creados; dejar constancia de `settings.json` modificado y su copia de seguridad.

- [ ] **Step 4: Verificar**

Run: `grep -l "guard_proyecto" ~/.claude/CLAUDE.md /home/haytham/Documentos/vault/CLAUDE.md ~/.gemini/config/GEMINI.md /home/haytham/Documentos/vault/00_Meta/GEMINI.md | wc -l`
Expected: `4`.

- [ ] **Step 5: Actualizar grafo y registro**

Run: `cd /home/haytham/Documentos/vault && graphify update .`
Expected: termina sin error. Después, `index_vault.py` (vault §6) si se quiere búsqueda semántica de las notas nuevas.

- [ ] **Step 6: Commit**

```bash
git add 00_Meta/Sesiones/ 00_Meta/GEMINI.md CLAUDE.md
git commit -m "docs: sincronizar sistema de mejora continua en CLAUDE y GEMINI"
```

---

## Autorevisión

- **Cobertura del diseño:** §4.1 → Task 2; §4.2 → Tasks 1 y 4; §4.3 → Tasks 1, 4 y 6; §4.4 → Task 2; §4.5 → Task 5; §4.6 → Task 3; §5 restricciones → Global Constraints y Task 7; §6 piloto → Task 6; §8 llamadas (retoque, cierre, opt-in, orden, `dominio`/`documento-destino`, trigger de 3 retros, web-cliente) → Tasks 1, 3, 4 y 5.
- **Consistencia de nombres:** `Ficha de Investigacion.md`, `Retro.md`, `.proyecto`, `nombre-vault`, `tipo`, `retoques`, `status: completa|pendiente`, `revisada` y `documento-destino` se escriben igual en todas las tareas.
- **Proporción:** el plan decide nombres, firmas, valores y pruebas, y deja a quien construye los cuerpos de las funciones, el texto de las plantillas y las consultas.
- **Pendiente de confirmar con Haytham durante la ejecución:** si Liyo es `web-cliente` o `micro-saas` (Task 6 Step 1) y su cifra de retoques (Task 6 Step 5).

