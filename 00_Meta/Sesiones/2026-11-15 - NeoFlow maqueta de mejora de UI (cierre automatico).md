---
type: sesion
date: '2026-11-15'
proyecto: '[[NeoFlow AI]]'
origen: maquina
sesion_id: 5130e54b-b321-40fd-ab1e-c1b57fe21600
tags:
  - sesion
  - cierre-automatico
---

> [!resumen] En cristiano
> Se hizo una maqueta del pitch de NeoFlow con componentes modernos puestos encima del original, sin tocar su HTML ni su CSS. Se verificó en móvil y tablet con cero fallos de accesibilidad. Al final Haytham pidió quitar el nombre «NeoFlow AI» visible y los marcos animados.

## Qué se hizo
- Carpeta `~/Proyectos/neoflow-pitch/maqueta-ui/`: copia exacta del pitch (9 diapositivas) más una capa nueva en `ui-upgrade.css` y `ui-upgrade.js`; `index.html` solo difiere en 4 líneas.
- Bugs arreglados: el chat no se veía (la animación acababa en `transform:none` y Motion lo leía como `scale(0)`); las listas del modelo de negocio salían apretadas (fallo que ya traía el original); la etiqueta «MODELO DE NEGOCIO» pisaba el título en móvil.
- Verificación a 375, 768 y 320 px: sin desborde, axe 4.10 con 0 violaciones en las 9 diapositivas; Lighthouse móvil: rendimiento 82, accesibilidad, prácticas y SEO 100. Un `<aside>` se cambió por `<div role="group">`.
- Título de la diapositiva de modelo ahora «SaaS B2B» (sin «.ai»).
- Última petición: quitar «NeoFlow AI» de portada, título, «Así funciona NeoFlow.» y «NeoFlow by»; quitados los 8 marcos de luz giratoria. Hecho, **sin comprobar en el navegador**.

## Pendientes
- Revisar en el navegador tras quitar marca y marcos.
- Rendimiento móvil 82: margen de mejora.

## Relacionado
- [[01_Projects/NeoFlow AI]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
