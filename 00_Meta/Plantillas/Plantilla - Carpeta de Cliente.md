---
type: meta
status: activo
date: 2026-11-22
origen: mixto
tags: [plantilla, carpeta, cliente]
---

# Plantilla - Carpeta de Cliente

> [!resumen] En cristiano
> Estructura de carpetas para organizar la documentación y activos de un cliente en el vault. Sirve como modelo para cualquier cliente nuevo.

## Estructura recomendada

```
02_Areas/
└── Área del Cliente/
    ├── Cliente - MOC.md           # Entrada del área (MOC de enlaces)
    ├── Cliente - Ficha.md          # Ficha principal del cliente
    ├── Cliente - Onboarding.md     # Registro de onboarding y pasos iniciales
    ├── Proyecto - <Nombre>.md      # Ficha del proyecto activo (si aplica)
    └── ...                        # Demos, propuestas, casos de éxito, etc.
```

## Contenido mínimo en la ficha del cliente

| Campo | Valor |
|---|---|
| **Nombre del cliente** | |
| **Tipo de negocio** | |
| **Fecha de incorporación** | |
| **Objetivos principal** | |
| **Resultado esperado** | |
| **Estado actual** | |

## Organización de documentos

- **Fichas sueltas** en la raíz de la carpeta del cliente: `Beneficios`, `Contacto`, `Acuerdos`, etc.
- **Proyectos activos** con su ficha `<Nombre>.md` y carpeta con flujo de 6 documentos.
- **Demostraciones** y casos de éxito en `99_Assets/` o subcarpetas propias.
- **Documentos archivados** en `04_Archive/` cuando el proyecto termina.

## Vinculación con el sistema

- Relacionar la ficha del cliente con el `Área - MOC.md` correspondiente.
- Vincular proyectos del cliente a `03_Resources/` para plantillas reutilizables.
- Usar `vault-search` para encontrar información del cliente rápidamente.

---

*Plantilla genérica para cualquier cliente. Las referencias a `NeoZeler/Clientes/` y estructura específica han sido removidas a favor de una convención nombrable por el usuario.*