---
type: proyecto
status: en-progreso
date: '2026-10-22'
tags:
- trading
- servidor-zorin
- sin-ia
repo: ~/Proyectos/battle-royale (servidor Zorin)
origen: mixto
---

# Battle Royale de estrategias - Diseño (PRD)

> [!resumen] En cristiano
> Es un torneo entre unas 15 estrategias de trading hechas con reglas fijas, sin IA. Primero pelean contra el pasado (años de velas de 12 monedas) y van cayendo por rondas. Las que sobreviven operan después con dinero ficticio en vivo. Todo se ve en una ventanita en la pantalla del servidor, junto con la memoria, los procesos y el estado del scraper de empresas. Si ninguna le gana al azar, la ventana lo dice claro en vez de coronar a una.

## Intención
Saber si alguna de las estrategias de los dos CSV (`Estrategias de Trading Basadas en Volumen y Operativa`, `Estrategias de Trading con Bots para Maximizar Ganancias`) tiene ventaja real, con un método fijado antes de medir (regla de Haytham). Proyecto de Haytham, no de NeoZeler.

## Objetivos
- Ventana nativa (GTK) en el monitor del servidor Zorin con tres paneles: sistema (RAM, procesos), scraper Laya Leads (ciclo, webs leídas, correos, A/B/C/D, zonas), combate (fase, ronda, marcador, caídas).
- Fase 1 (pasado): todas las estrategias contra las mismas velas y comisiones; rondas con eliminación.
- Fase 2 (vivo en papel): las supervivientes operan cada hora con datos públicos de Binance.
- Veredicto honesto: una estrategia solo "gana" si supera al azar con el mismo riesgo.

## No objetivos
- Nada de IA/Laya para decidir. Nada de dinero real. Nada de apalancamiento ni cortos (solo spot en largo).
- Las estrategias que necesitan 5 min o libro de órdenes (flujo de órdenes, CVD, absorción, barrido asiático/FVG, SFP de 5m) quedan fuera: no hay datos.

## Anti-objetivos (sería un fracaso aunque "funcione")
- Coronar a una ganadora por suerte o por haber visto los datos de examen.
- Ventana que se cuelga, se come la RAM o deja de refrescar sin avisar.

## Decisiones (mías salvo indicación)
- Datos: `~/Proyectos/trend-bot-paper/data/velas/*.csv` (12 monedas, 1h/4h/1d), solo lectura. Marcos usados: 1h y 4h.
- Comisión 0,1 % por lado + 0,05 % de deslizamiento. Capital ficticio 1.000 por estrategia; riesgo 1 % por operación; una posición por moneda.
- Separación: 60 % inicial para entrenar y 40 % final como examen que nadie ve hasta la ronda 2.
- Rondas: R1 (entrenamiento) cae la peor mitad por estadístico t de la ganancia neta por operación; R2 (examen) cae quien no supera al percentil 95 de 200 estrategias aleatorias con la misma frecuencia, stop y salida; R3 (robustez) cae quien no es positiva en ≥60 % de las monedas o con comisiones x2.
- Vivo: cada hora (:02) baja velas cerradas de la API pública de Binance, ejecuta señales y apunta operaciones en SQLite. Ganadora provisional tras 30 días; veredicto final solo si supera al azar.
- Ventana: GTK3 (PyGObject ya instalado), arranca como servicio de usuario con la sesión de GNOME (Wayland) del usuario `ssh`.
- Estado compartido: SQLite en modo WAL; la ventana solo lee.

## Lo que queda al constructor
Parámetros exactos de cada estrategia (los de los CSV: EMA 20/50, ATR 1, R/B 1:2, SMA20 de volumen, etc.), diseño visual de la ventana, nombres de archivos.

