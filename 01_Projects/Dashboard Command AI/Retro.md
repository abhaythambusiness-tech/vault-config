---
type: retro
proyecto: Dashboard Command AI
tipo: saas
status: completa
retoques: 1
revisada: false
date: 2026-11-05
origen: mixto
---

> [!resumen] En cristiano
> Retro provisional: el proyecto sigue en curso. En la primera entrega hubo un retoque grande (el 3D salía blanco en el navegador de Haytham, había que mezclarlo mejor con la web y cambiar Jason por Haytham). Falta que Haytham confirme la cifra.

# Retro de Proyecto

## Retoques
- 1 (confirmado por Haytham 2026-11-05): 3D quemado en su navegador, mezcla 3D/HTML más premium y renombrado Jason → Haytham.

## Nivel frente a referencias
- Sin comparar todavía; falta fijar dos referencias en la ficha.

## Skills previstas vs usadas
- Usadas: `diseno-central`, `threejs-*` (instaladas en el retoque). Faltó verificar antes en navegador con WebGL real.

## Librerías
- Three.js, Vite, `ws` como se previó. Sin trampas nuevas en `librerias.md`.

## Lecciones
| Síntoma | Causa | Regla | dominio | documento-destino |
|---|---|---|---|---|
| 3D blanco en el navegador del usuario | Luces, entorno, suelo claro y bloom sumados; probado sin WebGL real | Verificar 3D con Chrome headless (swiftshader) y exposición baja desde el inicio | diseno | UI-UX |
| Cliente nuevo falla contra servidor viejo | Ids de usuario cambiados sin reiniciar el servidor | Tras cambiar ids o API, reiniciar el servidor antes de probar | despliegue | Plan |
