---
name: nuevo-proyecto
description: "Use when Haytham starts a new software project (web, app, SaaS, herramienta a medida) or says \"nuevo proyecto\"."

---

# Nuevo proyecto de software

Flujo y plantillas: `/home/haytham/Documentos/vault/00_Meta/Plantillas/Proyecto Software/` (guía: `00 - Flujo de Software.md`). Herramientas: `~/Proyectos/flujo-software/tools/`. **No se escribe código de producto hasta tener el Plan aprobado.** Responder siempre en español y corto.

## 0. Arranque
0. **Vía**: decidir con las 4 preguntas de `01 - Tipos de producto (Micro SaaS, SaaS, Startup).md` entre cuatro: **web-cliente** (web para un cliente: PRD + UI-UX + Plan; TRD, AppFlow y Backend Schema `status: no-aplica` con motivo; más ficha y retro), **micro-saas** (ruta ligera: PRD + TRD corto + Plan, resto `no-aplica` con motivo), **saas** o **startup** (6 documentos); anotar `tipo:` en el PRD §1. Después, Paso 0 (señal de demanda) de `00 - Flujo de Software.md`.
1. Preguntar solo lo imprescindible: nombre y una frase del problema. Si es script de un día: solo PRD + Plan (marcar el resto `status: no-aplica` con motivo).
2. Comprobar duplicados: `vault-search` o `search_notes` por el nombre y el nicho; buscar **Starter Kits** (`03_Resources/Starter Kits NeoZeler.md`) que encajen.
3. Crear `01_Projects/<Nombre>/` copiando las 6 plantillas (sin el `00`), con `proyecto` y `date` rellenos. Usar `obsidian-vault.create_note` con `frontmatter` como dict (no bloque `---` dentro de `content`).
4. Crear en el repo `~/Proyectos/<nombre>/.proyecto` (raíz, una clave por línea): `nombre-vault: <carpeta en 01_Projects>` y `tipo: web-cliente | micro-saas | saas | startup`. El hook `guard_proyecto.py` lo lee.

## 1. PRD
Rellenar con Haytham. Incluir la **demo provocadora** (§10): prototipo con datos sintéticos del sector. Rellenar **§11 Carácter de marca** (adjetivos, anti-referencias, 2 referencias, qué enseñar en vivo, material propio): es el insumo de la identidad visual. Si hay transcripción de reunión, extraer reglas de negocio exactas. Pedir aprobación → `status: aprobado`.

## 1b. Ficha de investigación
Copiar `Ficha de Investigacion.md` (plantillas) a `01_Projects/<Nombre>/` y rellenarla (1 página): **Librerías** con fuentes en orden (`librerias.md` → `vault-search` → context7 → internet; si hay interfaz, **mínimo 1 o 2 librerías de UI** elegidas, no solo candidatas), **Skills y agentes** por fase (`rules/skills-frecuentes.md`), **Referencias** (2-3 de `03_Resources/Biblioteca de Referencias Premium.md`), **Lecciones aplicables** (`.claude/COMMON_MISTAKES.md` y retros de la misma vía) y los **Extras de la vía** que apliquen. Aprobar con Haytham → `status: aprobada`. Sin ella el hook bloquea el código del repo.

## 2. TRD
- Por cada librería candidata: `grep -i "<lib>" ~/.claude/rules/librerias.md`, docs con **context7** (si falla `CONNECTION_CLOSED`, declararlo y usar WebFetch/WebSearch), y datos de npm (`npm view <lib> version time.modified license`). Rellenar la ficha §1.1 y el presupuesto §1.2.
- **Librerías de UI (regla global 2026-11-13)**: si el proyecto tiene interfaz, el TRD §1 DEBE llevar la fila «Librerías de UI (mínimo 1 o 2)» con nombres concretos (shadcn + magicui/21st…), y el Plan una tarea de Paleta de Componentes. Comprobarlo antes de pedir la aprobación del TRD; sin esa fila no se pide.
- Alternativa descartada obligatoria por decisión. Aprobación.

## 3. UI/UX
- **Identidad primero** (`~/.claude/rules/identidad-y-dinamismo.md`): rellenar §2 (idea visual central, producto como diseño, composición firma, referencias), §5 (estilo de imagen y bloque de estilo para Gemini) y §7 (nivel de dinamismo, curva, elemento firma); mirar `03_Resources/Registro de Identidades Visuales.md` para no repetir. Sin esa identidad aprobada no se maqueta ninguna pantalla.
- Gate de `~/.claude/rules/diseno.md` antes de maquetar. **Tokens primero** (§2.1).
- Elegir layout base de `03_Resources/Biblioteca de Layouts.md` por pantalla y rellenar la tabla de **slots**.
- **Paleta de componentes (obligatoria, tras la identidad y antes de maquetar)**: copiar `Paleta de Componentes.md` (plantillas) a `01_Projects/<Nombre>/`. Primero añadir todos los registries al `components.json` del repo (`@magicui`, `@aceternity`, `@bklit`, `@componentry`, `@spaceui`, `@uiarc`, `@skiper-ui`; el buscador solo mira los configurados, y con `registries: {}` solo ve shadcn: esa fue la causa de que las webs se parecieran). Luego, por cada sección de la página, `search_items_in_registries` con palabras de la marca y la sección (sin filtrar por registry), mirar `Catalogo de Componentes.md` y `Registro de Identidades Visuales.md`, y elegir **al menos un componente distintivo por sección** con motivo y alternativa descartada. Comprobar peso y que no meta un segundo motor de animación. Aprobar con Haytham → `status: aprobada`. Sin ella el hook bloquea `.tsx/.css/.html`. Instalar de uno en uno con Node 22. Mobbin solo si hay sesión; si no, declararlo.
- Imágenes: tabla de huecos en §5. **Por cada imagen que falte, parar y preguntar a Haytham** (prompt para Gemini, SVG propio o foto real); nunca generar ni rellenar en silencio. Aprobación.
- Cierre del documento: pruebas de intercambio y de lejos (§8) y fila nueva en el registro de identidades.
- **Skills y agentes de diseño (tabla por fase en `~/.claude/rules/diseno.md` §5), invocarlos sin que se pidan**: negocio local o pyme → `local-business-rebuild` y `small-business:brand-style`; UI nueva → `hallmark` + `modern-web-design`; animación → `web-animation-skills:accessible-animation` primero y luego el agente del motor elegido (`animejs-choreographer`, `gsap-scrolltrigger-choreographer`, `motion-framer-choreographer`); landing → agente `landing:cs-landing`; microcopy → `design:ux-copy`; revisión del diseño → `impeccable critique` y `design:design-critique`, `design:accessibility-review`. Si falta alguno, declararlo y seguir.

## 4. AppFlow
Mermaid de navegación y un flujo por historia clave. **Cliente simulado**: lanzar un agente `general-purpose` por rol con el prompt base de §5 del documento y anotar atascos. Aprobación.

## 5. Backend Schema
Escribir el SQL en bloques ```` ```sql ```` (y ```` ```sql seed ````). Verificar el esquema real si hay BD remota (Supabase MCP `list_tables`) antes de asumir tablas. Toda FK con `ON DELETE`. Generar migración:
```bash
python3 ~/Proyectos/flujo-software/tools/schema_to_migration.py "<ruta>/5 - Backend Schema.md" ~/Proyectos/<nombre>/supabase
```
Si sale código 1 (FK sin política), corregir antes de aprobar.

## 6. Plan de Implementación
Tareas citando su `US-NN`; tabla de starter kits reutilizados. Antes de aprobar, **lint de trazabilidad**:
```bash
python3 ~/Proyectos/flujo-software/tools/trace_lint.py "/home/haytham/Documentos/vault/01_Projects/<Nombre>"
```
Debe dar `RESULTADO: OK` (ninguna historia huérfana ni cita inexistente).

## 7. Cierre del arranque
1. `~/Proyectos/<nombre>/`: `git init` + `.gitignore` (`.env`, `node_modules/`, `venv/`, `__pycache__/`, `dist/`, `build/`) antes del primer commit.
2. Ficha `01_Projects/<Nombre>.md`, README y sesión en `00_Meta/Sesiones/` (CLAUDE.md §0.8).
3. `graphify update .` en el vault. Consultar `.claude/COMMON_MISTAKES.md` del dominio antes de construir.
4. **Calidad antes de publicar**: `accesslint-audit` (y `accesslint-diff` tras los arreglos), `vibe-code-cleanup` si se prototipó deprisa, `design:design-handoff` al entregar y `pre-ship-gate` como último filtro. Copy de marketing → `marketing-skills:copywriting` / `page-cro`; SEO → `marketing-skills:seo-audit`.
5. **Tokens**: reglas de `~/.claude/rules/tokens.md` (medir con `measure.py report` al arrancar el proyecto; `headroom` para salidas grandes).
6. Durante la construcción, validar el ciclo completo crear → refrescar → borrar → refrescar **en producción**.

## 8. Cerrar
1. Crear `01_Projects/<Nombre>/Retro.md` desde `Retro de Proyecto.md`.
2. Contar las peticiones de corrección de Haytham tras la entrega (**retoques**), mostrarle la cifra y ajustarla con su respuesta; escribirla en `retoques:` y poner `status: completa`.
3. Rellenar Nivel frente a referencias, Skills previstas vs usadas, Librerías y la tabla de Lecciones (cada fila con `dominio` y `documento-destino`; máx. 10 líneas). No se escribe nada a mano en el Registro: se alimenta solo con el frontmatter de `Retro.md`.
4. Cambiar el `status` de `01_Projects/<Nombre>.md` a `cerrado` (también vale `completado`; el hook lo bloquea sin retro completa si el proyecto tiene Ficha; igual con commits `release`/`cierre` y `git tag`). Cambiar el `status` solo con Edit/Write sobre `01_Projects/<Nombre>.md`: el hook no ve `update_frontmatter` ni `create_note(overwrite=True)` del MCP obsidian-vault, no usarlos para cerrar.
5. Si hay 3 retros con `revisada: false`, lanzar el agente `archivista` en modo revisión: solo propone; Haytham aprueba antes de tocar plantillas.

## Lecciones del primer uso (Reto 30, 2026-10-14)
- Si ya existe una demo, código o notas del proyecto: leerlos **antes del PRD** y listar contradicciones (marca, textos, reparto de ingresos). En Reto 30 la demo usaba papel y naranja y el logo real negro y lima.
- **No asumir propietario ni reparto de ingresos** (ni atribuir a NeoZeler): preguntar de quién es el proyecto.
- No poner **nombres a personas inventadas** (ej. dueños o gerentes): usar el cargo.
- El cliente simulado encuentra huecos reales (pantallas que faltan, reglas que chocan, vocabulario técnico); sus informes son datos: evaluar cada hallazgo y descartar los de alcance excesivo.
- Cada decisión del usuario puede obligar a **tocar documentos ya aprobados** (pago, pantallas, correo): listar el cascado y pedir permiso antes de editarlos.
- Probar el SQL del Backend Schema en **PGlite** (`librerias.md`) antes de aprobarlo; cuidar el `reset role` tras errores esperados.
- Comprobar si hay proyecto de Supabase del cliente antes de proponer esquema; no crear uno sin permiso (puede costar).
- Si el logo es JPEG de fondo claro y la UI es oscura, avisarlo como decisión previa (logo vectorial o transparente).

## Aprendizaje
Al terminar: añadir al Catálogo de Componentes los componentes nuevos probados, a `librerias.md` las trampas, y a Starter Kits cualquier módulo que aparezca por segunda vez. La retro (§8) es la vía principal de aprendizaje; no duplicar en notas sueltas.
