---
type: meta
status: activo
date: 2026-11-22
origen: mixto
tags: [meta, errores, common-mistakes]
---

# Errores Comunes

**⚠️ CRITICAL - Read at session start**

Registro vivo de errores que Claude **ya ha cometido en este vault/proyectos**. Formato de cada entrada: **Symptom → Check/Causa → Fix/Regla**. Gobernado por `CLAUDE.md §7.1`: consultar antes de actuar en el dominio correspondiente; añadir/reforzar entrada en la misma sesión tras un error corregido por Haytham; a la 3.ª reincidencia, promover la regla a §0–§6 de `CLAUDE.md`.

Índice de dominios: Vault/frontmatter (1–5, 14) · Diseño/UI (6–10) · MCP (12, 102) · Scaffolding web (13) · Hooks y pruebas de seguridad (69–70) · Verificación visual y entorno (75–91) · Datos y automatizaciones (16–21).

---

## 🔴 Top 5 Errores Críticos — Vault

### 1. Romper el frontmatter YAML

**Symptom**: las queries Dataview de `00_Meta/Dashboard.md` dejan de mostrar la nota o fallan.

**Check**: todo `type:` debe usar uno de los valores válidos definidos en `CLAUDE.md §5` (tipo canónico: `moc`, `proyecto`, `pmbok-fase`, `servicio`, `referencia`, `estrategia`, `guia`, `plantilla`, `resource`, `meta/dashboard`); `status:` debe ser coherente con los valores permitidos (`activo`, `borrador`, `completado`/`completo`, `demo-funcional`, `en-progreso`).

**Fix**: copiar el bloque frontmatter de una nota hermana del mismo tipo en vez de inventar campos nuevos. Verificar con `graphify update .` después de cambios masivos.

---

### 2. No mantener los backlinks (`related:`) al mover o crear notas

**Symptom**: una nota queda huérfana, no aparece enlazada desde ningún MOC/hub.

**Check**: toda nota nueva debe añadirse a `related:` de su MOC/hub padre y viceversa (wikilinks `[[...]]`). Revisar que los enlaces `[[:|alias]]` también estén actualizados.

**Fix**: al crear `Nombre - Tipo`, actualizar también el MOC correspondiente (`Área - MOC`, `Proyecto - MOC`, `Recurso - MOC`). Usar la búsqueda `vault-search` para encontrar enlaces rotos.

---

### 3. Ignorar el estilo de respuesta de `00_Meta/GEMINI.md`

**Symptom**: respuestas largas, con preámbulo, emojis o resúmenes finales — el usuario ya pidió lo contrario.

**Check**: español, máximo 8 líneas, empezar por la conclusión, sin "Claro"/"Por supuesto"/emojis a menos que el usuario los solicite específicamente.

**Fix**: aplicar las mismas reglas en Claude Code, no solo en Gemini. Recordar: principio + conclusión + detalle, siempre en español.

---

### 4. Crear carpetas y notas sin seguir el método PARA

**Symptom**: la raíz del vault se llena de carpetas sueltas (`output/`, `docs/`, `graphify-out/`, `taller-bravo/`) que no tienen un lugar fijo definido.

**Check**: antes de crear una nueva carpeta en la raíz, consultar `CLAUDE.md §0.2`: ¿existe una carpeta técnica designada para este tipo de archivo? (`99_Assets` para binarios, `docs/` para meta de Claude, `graphify-out/` para grafos).

**Fix**: usar siempre la estructura PARA: `01_Projects` para entregables con fin definido, `02_Areas` para responsabilidad continua, `03_Resources` para referencia reutilizable, `04_Archive` para histórico. Si no encaja en ninguno, revisar la estructura.

---

### 5. Nombre de proyecto o área ambiguo

**Symptom**: `01_Projects/` o `02_Areas/` contienen notas sin título claro, lo que dificulta la navegación y búsqueda.

**Check**: todo proyecto debe tener una ficha en `01_Projects/<Nombre>.md` con frontmatter `type: proyecto` y `status` definido. Toda área debe tener `02_Areas/<Nombre>/` con MOC propio.

**Fix**: antes de crear, verificar que no exista ya un proyecto o área con el mismo nombre o propósito. Usar el formato `Categoría - Nombre.md` como convención.

---

## 📋 Índice de Errores por Dominio

### Vault / Frontmatter (errores 1, 5)

### Diseño / UI (por definir)

### MCP (por definir)

### Scaffolding web (por definir)

### Hooks y pruebas de seguridad (por definir)

### Verificación visual, 3D y entorno (por definir)

### Datos y automatizaciones (por definir)

---

## 📌 Reglas Generales

1. **Siempre consultar `CLAUDE.md`** antes de actuar en cualquier dominio. Las reglas §0–§6 son vinculantes; §7+ son recomendadas pero governadas por la misma autoridad.

2. **Antes de crear algo nuevo**: ¿encaja en PARA? ¿Tiene frontmatter definido? ¿Tiene backlinks? ¿No duplica esfuerzo existente?

3. **Después de corregir un error**: reforzar la entrada en esta misma sesión y considerar promover la regla a las directrices principales de `CLAUDE.md`.

4. **Mantenimiento trimestral**: revisar el índice de errores, promover reglas stabilizadas, archivar las obsolestas.

---

*Este documento es vivo y evoluciona con el uso del vault. Los números de sección hacen referencia a `CLAUDE.md` del vault actual (2026-11-22).*