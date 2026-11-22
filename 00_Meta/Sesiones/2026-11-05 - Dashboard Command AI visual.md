---
type: sesion
origen: mixto
proyecto: "[[01_Projects/Dashboard Command AI]]"
date: 2026-11-05
---
> [!resumen] En cristiano
> Se arregló el 3D que se veía blanco, se mezcló mejor con el HTML y Jason pasó a llamarse Haytham. Se instalaron las skills threejs.

## Aprendizajes
- El panel integrado no tiene WebGL: verificar 3D con Chrome headless (swiftshader) vía CDP.
- Blanco = suma de luces + entorno + suelo claro + bloom; bajar todo a la vez.
- Cambiar ids del servidor exige reiniciarlo: cliente nuevo contra servidor viejo falla.
