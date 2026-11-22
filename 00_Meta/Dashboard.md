---
title: "Dashboard Central"
type: meta/dashboard
tags:
  - meta/dashboard
created: 2026-08-06
updated: 2026-09-29
---

# 🚀 Vault Master Command Center

> [!abstract] Sistema de Gestión PARA
> Navegación centralizada por proyectos, áreas y recursos del vault.

---

## ⚡ Mapas de Contenido (MOCs)

| Ámbito | Proyecto / Área / Cliente | Acceso directo |
| :--- | :--- | :--- |
| **Cliente** | 🏗️ [Nombre del Cliente] | [[02_Areas/[NOMBRE ÁREA]/Clientes/[NOMBRE]]\|Ficha de Cliente] |
| **Proyecto** | 🌊 Cauce (PMBOK SaaS) | [[01_Projects/Cauce/Cauce - Master Command Center\|Master Command Center - Cauce]] |
| **Proyecto** | 📦 Dropshipping | [[01_Projects/Dropshipping/Dropshipping - MOC\|MOC - Dropshipping]] |
| **Área** | 📁 [Nombre del Área] | [[02_Areas/[NOMBRE ÁREA] - MOC\|Área - MOC]] |

| Sección | Acceso directo |
| :--- | :--- |
| 📚 Recursos | [[03_Resources/README\|03_Resources]] |
| 📦 Archivo histórico | [[04_Archive/README\|04_Archive]] |
| 🖼️ Assets | `99_Assets/` |

---

## 📌 Proyectos Activos (`01_Projects`)

```dataview
TABLE status as Estado, type as Tipo, file.folder as Ubicación
FROM "01_Projects"
SORT file.name ASC
```

---

## 🏢 Áreas de Responsabilidad (`02_Areas`)

```dataview
TABLE status as Estado, type as Tipo
FROM "02_Areas"
SORT file.name ASC
```

---

## 🕒 Últimas Notas Modificadas

```dataview
TABLE type as Tipo, file.folder as Ubicación, file.mtime as "Última Modificación"
FROM ""
WHERE file.folder != "00_Meta" AND file.folder != "99_Assets" AND file.folder != "scratch"
SORT file.mtime DESC
LIMIT 8
```

---

## 🧠 Sesiones y Aprendizajes

```dataview
TABLE proyecto as Proyecto
FROM "00_Meta/Sesiones"
SORT date DESC
LIMIT 5
```
→ Ver todas: [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

---

## 🛠️ Utilidades & Meta
- 📋 **[[00_Meta/Plantillas/Plantilla_Nota_Estandar|Plantilla Nota Estándar]]**
- 📋 **[[00_Meta/Plantillas/Plantilla - Sesion|Plantilla Sesión]]**
- 🎨 **[[00_Meta/GEMINI.md|Instrucciones de Agente (GEMINI.md)]]**
