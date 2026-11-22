---
title: "Sesión - 2026-11-04 - Comanda Viva"
date: 2026-11-04
type: meta/sesion
origen: mixto
proyecto: "[[01_Projects/Comanda Viva]]"
tags:
  - sesion
aliases: []
---

# Sesión — 2026-11-04: Comanda Viva

> [!resumen] En cristiano
> Se diseñó entera una app de menú por QR, inventario y caja para Desayunos de Monika: los 6 documentos del flujo quedaron aprobados, tres clientes ficticios la probaron en papel, y la base de datos se escribió y se probó en local. Todavía no hay código de aplicación ni nada en la nube.

## Contexto
`/nuevo-proyecto` para [[01_Projects/Comanda Viva]]. Vía web-cliente, proyecto personal de Haytham. Nombre genérico Comanda Viva, marca blanca Monika Viva.

## Qué se hizo
- PRD, Ficha de Investigación, TRD, identidad visual, Paleta de Componentes, UI/UX, AppFlow, Backend Schema y Plan (26 tareas), todos aprobados por Haytham en orden.
- Referencias de Dribbble: menú = mezcla de los shots 2 y 5; caja y admin = mezcla de 6 y 7.
- Simulación con tres roles ficticios y cascada a PRD, TRD e identidad.
- Migración, semilla y 20 pruebas en PGlite; repo con git sin commit.

## Decisiones tomadas
- Proyecto personal de Haytham, no de NeoZeler; reparto con la clienta sin cerrar.
- Bklit en lugar de Recharts para las gráficas (un solo motor de animación).
- Entra el pedido directamente y caja puede anular; la confirmación previa es una opción apagada.
- Fuera de v1: propina, ticket impreso, dividir por líneas, «Pedir la cuenta», variantes de plato, cobro sin conexión.
- Texto crítico recto y de 18 px mínimo; las pegatinas giradas quedan solo como decoración.

## Aprendizajes (para futuras sesiones)
- Un agente que simula a la usuaria real encontró 24 atascos que la revisión de documentos no vio (p. ej. 40 ingredientes a mano la hacían abandonar la app); merece hacerse siempre antes de aprobar.
- En RLS, un `update` sin permiso no da error: afecta a 0 filas. Las pruebas deben comprobar `returning` vacío.
- Un ingrediente compartido deja varios platos sin stock a la vez; la prueba de «todo o nada» debe esperarlo.
- El buscador MCP de shadcn veía 0 registries sin `components.json`; con la línea de comandos y Node 22 sí.

## Próximos pasos
- T-01 del plan: scaffold del repo con Node 22.
- Decidir hosting, imágenes y reparto con la clienta.
- Ampliar el doc 5 con `get_pedidos_mesa` y métricas antes de la T-07 y la T-18.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[03_Resources/Registro de Identidades Visuales]]
