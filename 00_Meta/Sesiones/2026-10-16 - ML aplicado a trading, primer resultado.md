---
title: "Sesión - 2026-10-16 - ML aplicado a trading, primer resultado"
date: 2026-10-16
type: meta/sesion
proyecto: "[[03_Resources/Investigaciones/ML aplicado a Claude, trading y vida - ideas v2]]"
tags:
  - sesion
  - trading
  - ml
aliases: []
origen: mixto
---

# Sesión — 2026-10-16: ML aplicado a trading, primer resultado

> [!abstract] Resumen
> Se empezó a aplicar T1 y T2 sobre el `crypto-copy-bot`. Los datos desmontaron las dos ideas tal como estaban escritas, y eso dejó un plan más corto y honesto.

## Contexto
Investigación del 2026-10-15 ([[03_Resources/Investigaciones/ML aplicado a Claude, trading y vida - ideas v2]]), limitada a Claude, trading y vida. Haytham pidió "empezar a aplicar" la sección de trading.

## Qué se hizo
- Script de solo lectura `scripts/analisis_edge_vs_costes.py` en el repo del bot (rama `copybot-v2`, sin commit).
- Resultado y plan corregido en la sección 10 de la nota v2.

## Decisiones tomadas
- No tocar el bot ni sus parámetros.
- T2 deja de ser un modelo; T1, T4 y T5 esperan a tener datos o ventaja bruta.

## Aprendizajes (para futuras sesiones)
- Con 71 operaciones y costes de ~5,5 %, la ventaja bruta (-0,33 %) no se distingue de cero. Es el mismo patrón que cerró Memecoin-LSTM.
- El coste del papel es una fórmula del bot: no se puede "aprender" y hay que medirlo en cadena. Registrado como error 43 en `.claude/COMMON_MISTAKES.md`.

## Próximos pasos
- Decidir si se registran como "observadas" todas las señales para ganar datos por trader.
- Medir costes reales con cotizaciones antes de cualquier decisión de tamaño de lote.
