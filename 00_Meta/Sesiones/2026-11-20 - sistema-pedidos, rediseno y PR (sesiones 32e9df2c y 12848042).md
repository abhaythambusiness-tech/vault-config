---
title: 'sistema-pedidos: rediseño y PR'
date: '2026-11-20'
type: meta/sesion
origen: maquina
proyecto: ''
sesion_id: 32e9df2c-4bb6-4020-8399-76d43d30e56c
sesion_id_rama: 12848042-7502-4f1c-a246-a637345eea13
tags:
- sesion
- diseno
- pull-request
---

> [!resumen] En cristiano
> Se clonó el repo `sistema-pedidos` (pedidos de un bar), se rehízo entero como proyecto nuevo y se abrió una pull request (propuesta de cambios) en GitHub.
> Luego se fue puliendo el diseño varias veces; la última versión es una interfaz «Ticket» (papel y tinta) hecha desde cero.
> Dos sesiones comparten el mismo arranque (una es rama de la otra); aquí van juntas.

## Qué se hizo
- Proyecto nuevo `~/Proyectos/sistema-pedidos/`, rama `rediseno-v2`, **PR #1** en `melianeliezer05-a11y/sistema-pedidos` (desde el fork).
- Primera versión: React + Tailwind + shadcn; carta, carrito, seguimiento en vivo, panel admin; seguridad (sin contraseñas por defecto, límites de intentos, CSP, precios validados en servidor).
- Panel admin «herramienta profesional»: riel lateral, atajos 1-6, resumen con ventas y gráficas, tablero de pedidos con temporizador.
- Se rehízo con componentes reales: shadcn (`Sidebar`, `Command`, `Chart`…), Magic UI (`NumberTicker`, `BlurFade`, `MagicCard`, `ShimmerButton`, `BorderBeam`) y tokens de transitions.dev con `prefers-reduced-motion`.
- Fondo SVG de garabatos (commit `a4fae06`) y, después, **rediseño desde cero «Ticket»** (Geist + Geist Mono, acento naranja único, sombra dura; commit `4ff18a3`); se quitó el fondo.
- La rama `12848042` desplegó en local la versión de la última PR (`http://localhost:3000/admin`, usuario de prueba, clave temporal de esa instancia).

## Decisiones
- Un solo acento de color y solo para estado; identidad por encima de efectos.
- «Olvídate del diseño inicial, quédate con la idea»: tras varios adornos, volver a una maqueta limpia.

## Problemas
- Login y panel del fondo SVG no se revisaron a mano; la última versión sin prueba con cuenta real.

## Pendientes
- Revisar la PR #1 con la dueña del repo; probar flujo completo (pedido → cocina → entregado).
- Sin ficha en `01_Projects/` ni README/resumen del vault (regla §0.8).

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

