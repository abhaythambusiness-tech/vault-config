---
title: "Sesión - 2026-11-11 - NeoZeler Web multipágina, transición de cámara y Lighthouse"
date: 2026-11-11
type: meta/sesion
origen: maquina
proyecto: "[[01_Projects/NeoZeler Web]]"
sesion_id:
  - 99a3469a-2944-4b34-a7b1-1d08091dba5e
tags:
  - sesion
  - neozeler-web
  - cierre-automatico
aliases: []
---

# Sesión — 2026-11-11: NeoZeler Web multipágina, transición de cámara y Lighthouse

> [!resumen] En cristiano
> La web de NeoZeler dejó de ser una landing de un solo scroll. Ahora la portada es un resumen con cinco tarjetas y cada apartado tiene su página (Problema, Servicios, Resultados, Proceso), con una transición de cámara como en NeoFlow. Se quitó la página de preguntas, se pasaron axe (0 violaciones), Lighthouse y `next build`, y se arregló lo que se solapaba en móvil. Todo está subido a GitHub (commits `355da49` y `bea53fb`).

## Contexto
Proyecto [[01_Projects/NeoZeler Web]] (`~/Proyectos/neozeler-web/`). Parte de [[00_Meta/Sesiones/2026-11-10 - NeoZeler Web sin Lanzamientos, auditoria UI-UX y Z 3D (sesiones b6b95b2a y 81d8bf92)|la sesión anterior]]. Haytham pidió que la web no fuese un solo scroll sino un resumen en la primera página y el resto de apartados accesibles desde botones.

## Qué se hizo
- `/` pasó a ser el resumen: hero y cinco tarjetas con un dato clave (15 min, 7 servicios, +30 %, 4 semanas, 6 preguntas), cada una enlaza a su página; cierra con la llamada a la auditoría.
- Una página por apartado (`/problema`, `/servicios`, `/resultados`, `/proceso`) con su título y su entrada en el sitemap; en móvil, botón «Menú».
- Transición de cámara estilo NeoFlow: la página actual se aleja con zoom-out y la nueva entra desde el lado contrario (1,1 s). La dirección depende de la posición en el lienzo (`LIENZO`); la cabecera queda fija. Sin soporte del navegador o con movimiento reducido, navegación normal. El fondo 3D cambia de pose según la página, ya no según el scroll.
- Ajustes por capturas de Haytham: menú que empieza por «Inicio»; tarjetas del resumen más vivas (entrada escalonada, contadores, mini-animación en bucle, foco de luz que sigue al cursor); páginas que llenan la pantalla (`/resultados` con título visible y tarjetas más grandes; contenido centrado en vertical en `page-shell.tsx`).
- Quitada `/preguntas` (enlace, tarjeta, sitemap y transición). El componente sigue en `sections/faq.tsx`.
- Verificación: 15 saltos entre las 5 rutas en ambos sentidos; axe 0 violaciones en 10 rutas, 375 y 1280 px, claro y oscuro; `next build` y `tsc` limpios; capturas en `.capturas/`.
- Arreglos que salieron: cabecera clara sobre páginas oscuras (variable `top` sin definir en `zona-header.tsx`), contraste 1,09 del titular en portada oscura (`hero-split.tsx`), fondo oscuro del `body` en `/resultados` y `/proceso`, orden de títulos h1→h3.
- Revisión en móvil: cabecera opaca (el texto se veía detrás), 3D a resolución 2× (antes 1×) y objetos 3D desplazados a los bordes para no tapar titulares.
- Commits: `355da49` (multipágina) y `bea53fb` (móvil, cabecera opaca y 3D a 2×), ambos en `origin/main`.

## Decisiones tomadas
- Estructura multipágina con resumen en portada, en lugar de landing de un scroll.
- Sin sección de preguntas frecuentes en la web.
- El 3D se apaga solo cuando el render es por software.

## Aprendizajes (para futuras sesiones)
- Lighthouse corre sin GPU, así que no mide el 3D real ni el coste de la GPU; con el equipo cargado (load average ≈ 11) el rendimiento móvil varió entre 75 y 93 en la misma página.
- Una animación de cámara solo se comprueba por código y estado en este entorno: no se pudo capturar un fotograma intermedio.

## Problemas abiertos
- Lighthouse móvil: rendimiento 75–89 (portada con TBT de 1,3 s en la primera tanda); accesibilidad de la portada móvil 96 en una repetición sin saber qué auditoría falló.
- El 3D no se vio con tarjeta gráfica real ni en un móvil de verdad.
- En `/servicios` el 3D aún roza el texto por el borde derecho en móvil.

## Próximos pasos
- Probar en un móvil real y con GPU; repetir Lighthouse con el equipo en reposo.
- Revisar `/caso`, `/agendar` y legales en móvil (pendiente de antes).
- Actualizar la ficha [[01_Projects/NeoZeler Web]] con la estructura multipágina.

## Relacionado
- [[01_Projects/NeoZeler Web]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
