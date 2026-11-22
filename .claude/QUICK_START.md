# Quick Start Commands

---

## Navegación del vault

- **Dashboard central**: `00_Meta/Dashboard.md` (queries Dataview de proyectos/áreas activos y últimas notas)
- **Instrucciones de estilo**: `00_Meta/GEMINI.md`
- **Plantillas** (Templater, `<% tp.file... %>`): `00_Meta/Plantillas/`
  - `Plantilla - Cliente.md`, `Plantilla - Proyecto.md`, `Plantilla - Propuesta.md`, `Plantilla - Servicio IA.md`, `Plantilla - Onboarding Cliente IA.md`, `Plantilla_Nota_Estandar.md`

## Hubs por ámbito (MOC = Mapa de Contenido)

- **Cauce** (proyecto SaaS PMBOK): `01_Projects/Cauce/Cauce - Master Command Center.md`
- **NeoZeler** (área de consultoría IA): `02_Areas/NeoZeler/NeoZeler - Master Command Center.md`
  - Clientes: `02_Areas/NeoZeler/Clientes/NeoZeler - MOC de Clientes.md`
  - Nichos: `02_Areas/NeoZeler/Nichos/NeoZeler - MOC de Nichos.md`
  - Servicios: `02_Areas/NeoZeler/Servicios/NeoZeler - MOC de Servicios.md` (con sub-MOCs por nicho en `Servicios/` y demos en `Servicios/Demos/`)

## Crear una nota nueva

1. Copiar la plantilla correspondiente de `00_Meta/Plantillas/`.
2. Respetar el frontmatter YAML (`title`, `type`, `status`, `tags`, `related`).
3. Enlazar la nota nueva desde el MOC/hub relevante (`related:` + wikilink).
4. Seguir la convención de nombre: `Categoría - Nombre.md` (ej. `Cliente - X`, `Servicio - X`, `Nicho - X`).

---

**Last Updated**: 2026-08-07
