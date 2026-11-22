---
title: "Sesión - 2026-11-10 - NeoZeler Web: escenas animadas, fondo 3D y Lighthouse"
date: 2026-11-10
type: meta/sesion
origen: mixto
proyecto: "[[01_Projects/NeoZeler Web]]"
sesion_id:
  - 150e9f0a-2822-41d2-b474-c0ee41bea11e
  - 3c145515-1ce9-4ec3-8a7b-6ec34b34213d
tags:
  - sesion
  - neozeler-web
  - diseno
  - animacion
aliases: []
---

# Sesión — 2026-11-10: NeoZeler Web con escenas animadas, fondo 3D y Lighthouse

> [!resumen] En cristiano
> Haytham pidió auditar la web de NeoZeler y hacerla más viva, como el pitch de NeoFlow. Se rehicieron portada, Problema, Servicios, Resultados y Proceso como escenas animadas. Se cambió la gema por un fondo 3D (cinta de Möbius y constelación de nodos) y se rehicieron las preguntas frecuentes y los botones. Todo está subido a GitHub; en móvil la web saca 80 en rendimiento (antes 39). El 3D no se probó con tarjeta gráfica real.

## Contexto
Repo `~/Proyectos/neozeler-web/` (ficha `[[01_Projects/NeoZeler Web]]`). La sesión `3c145515` es una rama de la principal (`150e9f0a`): mismo arranque, y en ella se exploró el branding 3D con maquetas en la carpeta temporal.

## Qué se hizo
- **Auditoría de UI/UX** de toda la web (portada, problema, servicios, resultados, proceso, FAQ, cierre) con el pitch NeoFlow como referencia.
- **Branding distinto a la gema:** primero 3 variantes de una Z 3D; Haytham pidió otros ejemplos y eligió la cinta de Möbius y la constelación de nodos (maquetas `formas.html`, `hero.html`, `fondo.html`).
- **Portada:** escena «un día del negocio» (chat, flujo, CRM y panel en un bucle CSS de 14 s), sin que el agente sea el protagonista; se quitó el hueco y se puso la bandeja a la izquierda.
- **Problema:** bandeja de WhatsApp que se llena y se enfría (9 s al verse, sin scroll fijado).
- **Servicios:** micro-simulaciones animadas en vez de tarjetas vacías.
- **Resultados:** cifras que cuentan hasta su valor con mini-gráfico y frase de contexto; se pidió que la conversión no pareciera «ayuda poca» (42 pasó a 30).
- **Proceso:** lienzo horizontal con cámara que recorre las 4 semanas.
- **Ajustes:** se quitaron flechas y barra del lienzo, se arregló el interruptor de la semana 3, el tema pasó a un círculo luna/sol, se revisaron CTAs, degradados y transiciones.
- **Fondo 3D** aplicado en la web (cambia de pose por sección y de luz claro/oscuro) y logo completo en cabecera y pie; FAQ rediseñada (tarjetas numeradas, acordeón animado, CTA fija); unificación del azul (el malo era el del botón de arriba).
- **Axe y Lighthouse** sobre el build de producción; commit `0c5da3d` en `origin/main`.

## Decisiones y porqué
- Escenas con CSS en bucle, sin librerías nuevas (excepción de anime.js solo para el embudo, ficha del proyecto).
- El 3D no se carga si el navegador pinta por software: en el Chrome de pruebas bloqueaba la página 154 s.
- Cifras de Resultados (+30 %, 18 h, 72 h): Haytham confirmó que valen «para la demo», no como datos de clientes.

## Resultados medidos
| | Rendimiento | Accesibilidad | Buenas prácticas | SEO |
|---|---|---|---|---|
| Móvil | 80 (antes 39) | 100 | 100 | 100 |
| Escritorio | 98 | 100 | 100 | 100 |

Axe: 0 violaciones en escritorio claro y oscuro, `/caso` y `/agendar`; 3 avisos de contraste a 375 px en las mini-simulaciones de Servicios (se miden en pleno fundido).

## Problemas
- El panel del navegador no tiene WebGL: el 3D solo se vio con Chromium headless.
- El servidor de desarrollo servía CSS viejo (aviso «Cita confirmada» fuera de sitio); se resolvió limpiando caché.

## Pendientes y próximos pasos
- Probar el 3D con GPU real en móvil, 320 px y el modo oscuro global.
- Revisar `/caso`, `/agendar` y páginas legales en móvil.
- Sustituir las cifras demo por datos reales cuando haya clientes.
- Actualizar la ficha `[[01_Projects/NeoZeler Web]]` (aún dice «falta construir»).

## Relacionado
- [[01_Projects/NeoZeler Web]] · [[01_Projects/NeoFlow AI]] · [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
