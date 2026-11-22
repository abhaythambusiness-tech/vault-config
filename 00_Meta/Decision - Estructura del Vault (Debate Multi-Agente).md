---
title: "Decisión - Estructura del Vault (Debate Multi-Agente)"
date: 2026-08-11
tags: [decision, vault, obsidian, para, estructura, debate]
type: nota
status: activo
related: ["[[00_Meta/Dashboard]]", "[[00_Meta/Decision - Reparto de Tiempo NeoZeler vs Dropshipping]]"]
---

# Debate multi-agente sobre la estructura del vault (skill agent-debate)

4 agentes con encuadres distintos (Purista PARA, Auditor de usabilidad/navegación, Auditor de escalabilidad, Contrarian sobreingeniería) evaluaron la estructura de carpetas y MOCs del vault de forma independiente.

## 🔴 El punto más incómodo (Contrarian)

Mientras el vault genera 12 fichas + 12 demos de servicios especulativos (NeoZeler, sin cliente detrás) y 13 subcarpetas para Dropshipping (sin lanzar), el único cliente real (Clínica Marbella) llevaba 5+ semanas sin precio cerrado. La estructura no es el problema en sí, pero su nivel de detalle crece más rápido que el negocio real — señal a vigilar, no veredicto cerrado. (Nota: resuelto/en curso según [[00_Meta/Decision - Reparto de Tiempo NeoZeler vs Dropshipping]].)

## Inconsistencia estructural real (confirmada por 3 de 4 agentes)

- **NeoZeler vive en `02_Areas` pero se comporta como Proyecto** (objetivo de facturación, no mantenimiento continuo); **Dropshipping vive en `01_Projects` pero parte de su contenido es material de referencia reutilizable** (32 transcripciones) que encajaría mejor en `03_Resources`.
- **4 carpetas en la raíz rompían la taxonomía PARA sin que nadie lo hubiera decidido**: `docs/`, `graphify-out/`, `output/`, `taller-bravo/` — residuos de herramientas que se multiplican con cada skill nueva si no se les da un sitio fijo. → **Documentado en CLAUDE.md** (sesión 2026-08-11).
- **Convención de nombres inconsistente entre Projects y Areas**: NeoZeler usa prefijos (`NeoZeler -`, `Cliente -`), Dropshipping no. A 5-10x notas, buscar "todo lo de Dropshipping" por nombre de archivo dejará de funcionar. **Pendiente** (renombrar rompe wikilinks existentes, requiere sesión dedicada).

## Navegación real (auditor de usabilidad)

- El Dashboard no enlazaba Dropshipping (55 notas), ni `03_Resources`, `04_Archive`, `99_Assets`. → **Arreglado** (sesión 2026-08-11).
- Llegar a una ficha de servicio de NeoZeler exige 4 saltos, 5 niveles de carpeta. **Pendiente.**
- `Demos/` y `Fichas/` de un mismo servicio son casi indistinguibles por título en el buscador rápido. **Pendiente.**

## Escalabilidad (auditor de crecimiento)

- La numeración `00-11` de Dropshipping se rompe en cuanto haya que insertar algo en medio, y no es reusable para un segundo proyecto de ecommerce sin duplicar toda la estructura. **Pendiente.**
- Los MOCs se crean ad-hoc, sin plantilla ni regla ("crear MOC cuando haya ≥N notas"). **Pendiente** (nota: al revisar, Solar y Talleres no tienen MOC de servicios porque aún no tienen fichas/demos — no es inconsistencia real, es esperado).
- `04_Archive` estaba vacío — las reglas de archivado nunca se habían ejercitado. → Parcialmente resuelto: primer archivado real hecho en esta sesión (transcripción duplicada de NeoZeler/Servicios).

## Arreglos ya aplicados (sesión 2026-08-11)

1. Dashboard: añadidas filas de Dropshipping, Resources, Archive, Assets.
2. `output/servicios-resumen.pdf` (huérfano, sin enlaces) → movido a `99_Assets/`; carpeta `output/` eliminada.
3. `transcripciones_completas_ecommerce.md` en NeoZeler/Servicios (duplicado, ya integrado en Dropshipping según su propio texto) → archivado en `04_Archive/`.
4. CLAUDE.md documenta ahora las 4 carpetas técnicas fuera de PARA (`99_Assets`, `docs/`, `graphify-out/`, `taller-bravo/`).

## Pendiente de decisión del usuario

- `dvida_water_tabla_csv (Default View).csv` en NeoZeler/Servicios — datos de conversación con teléfonos reales, sin ninguna nota que lo referencie. No categorizado sin confirmar de qué es.
- `taller-bravo/` — mini-proyecto web (HTML/CSS/JS) huérfano, cero enlaces en el vault. Decidir: archivar / convertir en proyecto propio en `01_Projects/` / eliminar.
- Convención de nombres y numeración de carpetas: no tocado (renombrar rompe wikilinks existentes), requiere sesión dedicada si se quiere abordar.
