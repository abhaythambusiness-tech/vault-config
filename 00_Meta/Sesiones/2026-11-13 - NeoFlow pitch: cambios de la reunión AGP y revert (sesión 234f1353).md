---
title: 'NeoFlow pitch: cambios de la reunión AGP y revert'
date: '2026-11-13'
type: meta/sesion
origen: mixto
proyecto: '[[01_Projects/NeoFlow AI]]'
sesion_id:
- 234f1353-3308-4048-aff7-83c9d98dfc6e
tags:
- sesion
- neoflow
- pitch
---

> [!resumen] En cristiano
> De la reunión con los mentores se sacó una lista de mejoras para el pitch de NeoFlow AI: mercado en euros, precio, competencia con nombre, testimonio y gancho. Se aplicaron y se subieron a GitHub, pero luego Haytham pidió devolver `main` a la versión anterior y se hizo con un commit de revert.

## Qué se hizo
- Resumen de la transcripción «SAMIRA S2 - AGP FI» y del recap de Fathom (PDF) con propuestas de cambio.
- Cinco cambios en `index.html`: tercer nivel «Premium» como paquete de servicios adicionales; cinco competidores (Zerolagia de Málaga, Ciberfobia, Zululabs, Naxia, Vectoryal) del rastreo de agencias de IA; texto junto al testimonio aclarando que NeoFlow AI es el sistema instalado; gancho con Javier dueño de un negocio de filtros de agua; primer hito del roadmap «Q4 2026».
- Antes: precio subido de 1.300 € a 1.900 € (Salva lo veía bajo). Commit `88a77b4` a `main`.
- Revert: `d93f465` deja `main` igual que `a40b202`; `88a77b4` queda en el historial.

## Decisiones
- Revert con commit nuevo, sin `reset --hard` ni `push --force` (destructivo; habría que confirmarlo).

## Problemas
- No se vio el pitch en el navegador: sin comprobar 375/768/1280 px ni demo/vídeo. Los PDF y la ficha del vault no están actualizados.
- Tamaño de mercado en euros: solicitado por los jueces; no consta que se haya cerrado la cifra.

## Pendientes
- Decidir qué cambios se re-aplican tras el revert.
- Probar demo y vídeo en local (se denegó antes arrancar servidor).
- Revisar que los competidores listados sirvan (listado ruidoso).

## Relacionado
[[01_Projects/NeoFlow AI]]

