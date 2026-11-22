# Architecture Map

---

## Directory Structure (método PARA)

```
Haytham/
├── 00_Meta/                  # Meta: dashboard, plantillas, instrucciones de agente
│   ├── Dashboard.md          # Hub central (queries Dataview)
│   ├── GEMINI.md             # Reglas de estilo de respuesta
│   └── Plantillas/           # Plantillas Templater (Cliente, Proyecto, Propuesta, Servicio IA...)
├── 01_Projects/               # Proyectos con entregable/fin definido
│   └── Cauce/                 # SaaS bajo metodología PMBOK (5 fases + análisis)
├── 02_Areas/                  # Áreas de responsabilidad continua
│   └── NeoZeler/               # Agencia de implantación de IA en pymes — organizada por función GTM
│       ├── NeoZeler - Master Command Center.md  # Hub — único archivo suelto en la raíz
│       ├── Estrategia/          # Posicionamiento, hoja de ruta, modelo de precios (2 vías)
│       ├── Marketing/           # Contenido, marca, LinkedIn — awareness/inbound
│       ├── Comercial/           # Pipeline, prospección, diagnóstico, cold email, guion de llamada — outbound
│       ├── Clientes/            # Una carpeta por cliente (Cliente/Onboarding/Propuesta/Proyecto)
│       ├── Nichos/              # Un nicho por vertical (barberías, distribución, transporte...)
│       └── Servicios/           # Catálogo de servicios IA
│           ├── Fichas/           # Ficha por servicio, agrupada por nicho
│           └── Demos/            # Demo por servicio, agrupada por nicho
├── 03_Resources/              # Referencia sin acción asociada (vacío por ahora)
├── 04_Archive/                # Notas inactivas (vacío por ahora)
├── 99_Assets/                 # Adjuntos/imágenes (vacío por ahora)
└── docs/                      # Documentación del propio setup de Claude Code
```

## Key File Locations

- **Dashboard / entrada principal**: `00_Meta/Dashboard.md`
- **Instrucciones de estilo de agente**: `00_Meta/GEMINI.md`
- **Plantillas**: `00_Meta/Plantillas/*.md`
- **Hub Cauce**: `01_Projects/Cauce/Cauce - Master Command Center.md`
- **Hub NeoZeler**: `02_Areas/NeoZeler/NeoZeler - Master Command Center.md`
- **MOC Clientes**: `02_Areas/NeoZeler/Clientes/NeoZeler - MOC de Clientes.md`
- **MOC Nichos**: `02_Areas/NeoZeler/Nichos/NeoZeler - MOC de Nichos.md`
- **MOC Servicios**: `02_Areas/NeoZeler/Servicios/NeoZeler - MOC de Servicios.md`
- **Estrategia NeoZeler**: `02_Areas/NeoZeler/Estrategia/` (hoja de ruta, modelo de precios)
- **Marketing NeoZeler**: `02_Areas/NeoZeler/Marketing/` (contenido, marca, LinkedIn)
- **Comercial NeoZeler**: `02_Areas/NeoZeler/Comercial/` (pipeline, prospección, diagnóstico, cold email, guion de llamada)
- **Plantilla Caso de Éxito**: `00_Meta/Plantillas/Plantilla - Caso de Éxito.md`

## Convenciones de nombre

`Categoría - Nombre.md` — ej. `Cliente - Clínica Marbella Estética.md`, `Servicio - Agenda Blindada.md`,
`Nicho - Barberías y peluquerías.md`, `Demo - Servicio - X.md`, `MOC - Servicios - <Nicho>.md`.

---

**Last Updated**: 2026-08-07
