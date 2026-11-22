---
title: Sesión - 2026-10-22 - Laya Trader, del diseño al bot en vivo
date: '2026-10-22'
type: meta/sesion
proyecto: '[[01_Projects/Laya Trader]]'
tags:
- sesion
- laya
- trading
- bot
- panel
aliases: []
origen: mixto
---

# Sesión — 2026-10-22: Laya Trader, del diseño al bot en vivo

> [!resumen] En cristiano
> Se cogió el gist de drillan (catálogo de bots que usan Jev), se cambió Jev por Laya y en un solo día se pasó de la idea a un **bot de papel corriendo en el servidor Zorin con panel web**: 6 documentos aprobados, 21 tareas del plan hechas (menos los 7 días de prueba) y 210 pruebas en verde. El bot empezó a medir a las **16:13**; el veredicto «Laya sirve / no sirve» no puede darse antes del **2026-10-29 16:13**. Se abandona el proyecto de memecoins y no se usa nada del bot de tendencia.

## Contexto
Haytham encontró [el gist](https://gist.github.com/drillan/6916b16e8ea31a8ec36c8f59d6483150) y pidió empezar un proyecto nuevo sustituyendo Jev por Laya. Proyecto: [[01_Projects/Laya Trader]]. Reemplaza a [[01_Projects/Scalper Memecoins]] (abandonado). Repo: `~/Proyectos/laya-trader/` en el servidor.

## Qué se hizo
- Leyó el gist y el repo `buberlo/jev-trader` (9 etapas, 6 juicios, escalera de reserva, calibración); el README no publica opciones, campos ni umbrales: se definieron aparte y se congelaron.
- Flujo de 6 documentos (`/nuevo-proyecto`) aprobado paso a paso; control de trazabilidad en OK; cliente simulado que encontró 14 fallos de lenguaje y estados, corregidos.
- **Motor** (Python 3.12): feed de Binance con libro sincronizado, rasgos y resumen de ~107 tokens, Laya y juez de reglas, política con Kelly normalizado, Avellaneda-Stoikov, 6 vetos + interruptor + escalera, broker de papel con cola y comisiones, resultado a 15 min, calibración y veredicto con bootstrap por bloques de 1 h.
- **Panel** (FastAPI + SSE de solo lectura y HTML/CSS/JS sin Node): 5 pantallas con gráficos de `lightweight-charts`, lenguaje llano, claro/oscuro, accesibilidad comprobada a 375 y 1200 px.
- **Despliegue**: servicios de usuario de systemd con `linger`, copia diaria, permisos 600, panel solo en la red local.
- Pruebas en producción: reinicio del servicio y congelado de 30 s con frenos, escalón 3 y recuperación.

## Decisiones tomadas
- Mercado BTC/ETH/SOL en Binance spot, solo papel; Laya contra un «programa de reglas» (juez de reserva) con los mismos datos.
- Turnos de 4 s por moneda (Laya tarda ~3 s); aprobado antes de medir.
- **Kelly normalizado por número de clases** (`(c − 1/3)/(2/3)`): la fórmula original daba tamaño 0 con confianza < 0,5 y Laya nunca habría operado; cambiado antes de medir y anotado con fecha.
- Panel en lenguaje normal con ayuda por pantalla (regla de Haytham).
- Nada del Bot de Tendencia ni de Scalper Memecoins; solo se reutilizó el checkpoint de Laya y los pines de versiones.
- Un reinicio no parte el experimento: el veredicto suma las puestas en marcha con la misma configuración.

## Aprendizajes (para futuras sesiones)
- **Laya sin entrenar casi no opera con las reglas congeladas**: probabilidades casi planas (seguridad 0,35–0,44) y `inventory_pressure = high` casi siempre; en 10 min reales propuso 4 compras contra 17 del juez de reglas. Se mide tal cual, sin ajustar.
- Un error que las pruebas no vieron: la conexión SQLite de cada petición se abría en un hilo y se usaba en otro (500 solo en el servidor real). Regla en `.claude/COMMON_MISTAKES.md`.
- El generador sintético de pruebas tenía el libro cruzado y las pruebas pasaban igual: validar invariantes de los datos sintéticos.
- El servidor bloquea escribir en `/etc/systemd` (política de `zorin-ssh`): servicios de usuario + `loginctl enable-linger`.
- `pkill -f` y `pgrep -f` se auto-coinciden con la línea de órdenes (segunda vez); usar `fuser -k PUERTO/tcp`.
- `zorin-ssh` rechaza órdenes con saltos de línea y se corta a los 60 s: scripts por `sftp-upload` y procesos largos en segundo plano.
- GateGuard exige hechos antes del primer `Edit` de cada archivo: con varias ediciones en paralelo hay que comprobar cuáles se aplicaron.

## Próximos pasos
- T-20: 7 días de ejecución sin tocar; revisar el sello a diario en el panel o con `laya-trader calibrate`.
- Antes de dar el veredicto: `ponytail-audit` y `impeccable audit` (no se ejecutaron en esta sesión).
- 2026-10-29 16:13: primera fecha posible para decidir; si Laya falla cualquiera de las dos reglas, cerrar el proyecto y archivarlo.

## Relacionado
- [[01_Projects/Laya Trader]] · [[01_Projects/Laya Trader/Guia - Skills y reglas por fase]] · [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

