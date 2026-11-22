---
title: MCP de diseño v2 y configuración de diseño a nivel experto
date: '2026-11-20'
type: sesion
proyecto: '[[MCP Diseno]]'
origen: mixto
tags:
- diseno
- mcp
- configuracion
---

> [!resumen] En cristiano
> El ayudante de diseño (MCP `diseno`) era un catálogo con los ojos cerrados: recomendaba librerías sin mirar qué había puesto ya en el proyecto.
> Ahora lee el proyecto y además revisa el código buscando las animaciones mal hechas que ninguna herramienta comprobaba.
> También se arregló un fallo que dejaba la puerta de identidad cerrada aunque estuviera todo rellenado.
> Las reglas de diseño y el README quedan al día; el MCP ya estaba registrado, lo que faltaba era declararlo bien.
> Las dos herramientas nuevas no se pueden llamar hasta reiniciar la sesión de Claude Code.

## Qué se hizo

- **`proyecto.go` (nuevo)**: lee `package.json`, `components.json`/`boardui.json` y `DESIGN-IDENTITY.md`. Detecta framework, Tailwind, base de componentes, motor de animación e iconos, el estado de la Capa 0 y los conflictos (P0 dos bases o dos motores de animación, P1 varias familias de iconos).
- **`auditar.go` (nuevo)**: gate determinista de las reglas duras de motion sobre el código, con archivo y línea. P0 `transition-all` y `ease-in` crudo; P1 duración >300 ms, color a pelo en componentes, `<img>` sin `alt`, animación sin `prefers-reduced-motion`, `.html` sin `package.json`.
- **`main.go`**: `stack` y `elegir` aceptan `ruta` y quedan supeditados a lo instalado y a la identidad aprobada; catálogo en disco por encima del embebido (`$MCP_DISENO_CATALOGO`); protocolo `2025-06-18`; versión `2.0.0`; autotest de 11 a **25 comprobaciones** con un repo de prueba completo.
- **Bug de `identidad` arreglado**: buscaba una sección «movimiento» cuando la plantilla la llama «Dinamismo», así que una identidad completa devolvía `PUERTA CERRADA`. Ahora acepta `dinamismo|movimiento|cubic-bezier`, con test de regresión.
- **Configuración**: `~/.claude/rules/diseno.md` (Capa 2 con gate determinista, punto 0 de la puerta con `stack`/`elegir` restaurados, firmas verificadas), alta del MCP en `~/.claude/rules/mcps-seleccion.md` («Diseño y UI», primera línea), README y `resumen.html` del repo, ficha `[[MCP Diseno]]`.

## Aprendizajes

- **El MCP estaba registrado pero mal declarado.** `~/.claude.json` ya tenía `diseno` y las cinco herramientas v1 funcionaban; lo que faltaba era que las reglas y `mcps-seleccion.md` lo contaran. Un MCP que no está en las reglas no se usa aunque exista.
- **Por qué `stack` y `elegir` estaban degradados.** El 18 de noviembre devolvieron Magic UI y un modo que contradecía la Paleta aprobada de un proyecto, así que `rules/diseno.md` los bajó del paso 0. La causa era ser ciego al repo, no el catálogo. Arreglada la causa, vuelven al paso 0 **solo con `ruta`**.
- **`impeccable detect` no cubre las dos reglas más duras.** No tiene regla para `transition-all` ni para `ease-in` (la de ESLint es `no-transition-all`). Por eso el gate vive en el MCP propio y no en una skill de terceros.
- **Go `regexp` no tiene lookahead.** `ease-in-out` y `ease-in-expo` se descartan mirando a mano el carácter siguiente a la coincidencia (`easeInSuelto`), no con `(?!-)`.
- **Decisión: no enganchar `auditar` a `slop-gate`.** Ese hook sale con código 2 y bloquearía la edición de UI; convertir un aviso en un bloqueo es decisión de Haytham, no mía. Queda como oferta.

## Pendiente

- Reiniciar Claude Code para que aparezcan `mcp__diseno__proyecto` y `mcp__diseno__auditar` y para que `stack`/`elegir` acepten `ruta`.
- Decidir si `auditar` entra en `slop-gate`.
- Nada committeado todavía, ni en el vault ni en `~/Proyectos/mcp-diseno/`.

## Enlaces

- [[MCP Diseno]]
- [[2026-11-16 - MCP de diseño propio]]
- Reglas: `~/.claude/rules/diseno.md`, `~/.claude/rules/mcps-seleccion.md`
