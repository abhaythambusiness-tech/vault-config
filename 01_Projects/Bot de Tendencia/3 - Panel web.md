---
type: doc-software
doc: panel
proyecto: 01_Projects/Bot de Tendencia
status: hecho
date: '2026-10-21'
origen: mixto
---


# 3 · Panel web del bot (en vivo, solo lectura)

> [!resumen] En cristiano
> Es una **página web** que abres desde el móvil o el ordenador, en tu red de casa, en **`http://192.168.0.100:8060`**. Te enseña **cuánto vale cada una de las 4 carteras ahora mismo**, qué tiene comprado, qué está haciendo el bot y **por qué**, y si todo funciona. **Solo mira:** no puede comprar ni vender ni cambiar nada, no tiene claves, y no está abierta a internet. Todo el dinero es inventado.

> [!aviso] Rediseño del 2026-10-21 (tarde): sustituye al diseño de abajo
> Haytham dijo: *«no entiendo nada de lo que está pasando, los colores no me gustan y los gráficos tampoco»*. Se rehízo el panel entero:
> - **Colores**: fondo claro, letra grande, azul para elegir, verde = gana, rojo = pierde (siempre con flecha ▲▼ y palabra, nunca solo color). Se abandonó el fondo oscuro con ámbar.
> - **Gráficos**: de «5 líneas de colores con librería externa» a **una sola línea** de la hucha elegida con una raya de puntos «aquí empezó», más **barras sencillas** de «quién va ganando». Escala mínima del 2 % para que una bajada de 0,2 % no parezca un desplome.
> - **Palabras**: ninguna sigla. T, M, F y K pasan a *Seguidor diario*, *Seguidor de 4 horas*, *Seguidor de 1 hora* y *Robot de IA (Kronos)*; «equity», «peso», «posición» y «comisión de la orden» desaparecen; cada orden se explica con una frase como «Dejó de subir: vende todo lo que tenía».
> - **Secciones**: *Inicio* (resumen en una frase, quién va ganando, detalle de la hucha elegida, lo último que hizo el bot), *Historial* (con descarga para Excel), *¿Funciona?* (semáforo con frases y progreso de la prueba de Kronos) y *Ayuda* (preguntas y respuestas).
> - **Técnico**: ya no se usan la librería de gráficos ni las tipografías descargadas (la gráfica es SVG propio y la letra es la del sistema); se pueden borrar. Verificado en navegador a escritorio y a 375 px: sin desbordes, botones de al menos 46 px, sin errores. Commit `0317add`.
> - **Pendiente de saber**: si el nuevo estilo te gusta; es fácil cambiar colores, tamaños y textos.
> **Tercera versión (2026-10-21, noche)**, a petición de Haytham («quiero ver velas, no líneas», «más dividida la información», «scalping con Kronos»): 
> - **Velas de precio** (verdes y rojas, estilo plataforma de trading) como gráfica principal, con selector de moneda (12) y de duración de vela (15 min, 1 h, 4 h, 1 día) y **flechas ▲ de compra y ▼ de venta** donde el bot operó (en Inicio, con la letra de la hucha). Siguen las líneas de valor de las huchas, con la librería TradingView Lightweight Charts y colores validados sobre fondo claro (azul, naranja, rosa, violeta y turquesa).
> - **Una página por estrategia** (Diario, 4 horas, 1 hora, Kronos diario y **Kronos scalper**): qué hace en simple, cada cuánto mira, riesgo, lo que dijeron las pruebas, cifras, velas, valor en el tiempo, lo que tiene comprado y lo último que hizo. Inicio resume las 5.
> - **Quinta hucha, Kronos scalper (S)**: ver [[01_Projects/Bot de Tendencia]].
> - Técnico: `/api/velas` (Binance, caché de 15 s) y `/api/marcas`; 19 pruebas en verde; verificado en navegador a escritorio y 375 px; la cabecera `no-cache` evita que se vea una versión vieja. Código en git (commit `c9e97cd`).
> Lo que sigue (secciones 1 a 5) describe el **primer diseño** y se conserva solo como historia.

## 1. Qué documentos se revisaron (a petición de Haytham, 2026-10-21)
| Documento | Qué se tomó |
|---|---|
| Petición original (Scalper Memecoins) | «Una interfaz web donde ver las ganancias en tiempo real y al bot tomando decisiones y operando». Se cumple con la pantalla *En vivo* (valor por cartera en tiempo real + feed de órdenes con su explicación). |
| [[01_Projects/Scalper Memecoins/3 - UI-UX Design\|UI/UX aprobado de Scalper Memecoins]] | Identidad (carbón cálido y ámbar, IBM Plex, ▲▼ además del color), banner «PAPEL», glosario con tooltips, gráfica con leyenda, tabla alternativa y verificación a 375 px, tarjetas de salud, botones de al menos 44 px, recuadros «En cristiano». |
| [[01_Projects/Scalper Memecoins/4 - AppFlow\|AppFlow aprobado]] | Flujo en tiempo real por SSE con reconexión visible; estados vacío/cargando/caído. |
| [[01_Projects/Bot de Tendencia/1 - PRD\|PRD de este proyecto]] §6 | Decía que el panel quedaba fuera de alcance hasta que alguna cartera validara. **Haytham lo pidió igualmente**: pasa a estar dentro de alcance (queda anotado en el PRD). |
| Regla de lenguaje sencillo (2026-10-21) | Textos sin jerga, «En cristiano» en las pantallas, glosario. |

## 2. Qué pantallas hay y qué se dejó fuera
| Pantalla del diseño anterior | En este panel | Motivo |
|---|---|---|
| En vivo | **Sí**: 4 tarjetas (T, M, F, K) con valor en vivo, variación ▲▼ y comisiones; gráfica de las 4 carteras + línea de «solo Bitcoin»; posiciones por cartera; feed de órdenes | Cubre «ganancias en tiempo real y el bot operando» |
| Decisiones | **Fusionada** en el feed y en Operaciones: cada orden lleva su «por qué» en una frase | No hay texto de Laya que enseñar |
| Operaciones | **Sí**, con filtro por cartera y descarga CSV | US-03, US-08 |
| Gate 1 | **No aplica** | El criterio de T, M, F y K se evalúa en el backtest y en la prueba de Kronos, no en vivo |
| Control (pausar, cerrar todo, límites) y Acceso con token | **Diferido** | Con dinero falso no hace falta; y un panel sin escritura tiene riesgo cero. Si algún día hay dinero real, esto es lo primero que habría que diseñar con seguridad |
| Salud | **Sí** (nueva): bot, precios y velas, previsión y progreso de la prueba de Kronos, servidor y titulares de cripto | Para no fiarse de datos viejos |
| Glosario | **Sí** | Regla de lenguaje sencillo |

## 3. Cómo funciona (resumen técnico)
- API FastAPI en el servidor (`~/Proyectos/trend-bot-paper/src/panel_api.py`): lee `papel.db` en modo solo lectura, pide a Binance el precio de las 12 monedas cada 5 s, calcula el valor en vivo y lo empuja al navegador por SSE; las órdenes llegan en cuanto el bot las hace.
- Página sin framework (HTML, CSS y JS) con TradingView Lightweight Charts 5.2.1 y fuentes IBM Plex autoalojadas; paleta de 4 series **validada para daltónicos** (ámbar, azul, rosa, violeta; separación de color 12 o más).
- Un `cron` cada minuto (`scripts/panel_vigilante.sh`) lo levanta si se cae y también al reiniciar. 14 pruebas automáticas (cálculo del valor, coste medio, explicaciones, CSV, salud); `ruff` y `mypy` limpios. Código en git (commit `e80a3d9`).

## 4. Verificación hecha (2026-10-21)
- Navegador integrado, escritorio y móvil a 375 px: carga con datos reales, 4 tarjetas, gráfica con las 5 líneas, 42 órdenes en Operaciones, 12 posiciones más efectivo, Salud y Glosario; sin errores en consola.
- Fallos encontrados **y corregidos**: un «Aún no hay órdenes» falso (mi estilo anulaba el atributo `hidden`), desbordamiento horizontal en móvil (tarjetas en 2 columnas) y 5 botones por debajo de 44 px.
- **No verificado**: cómo se ve en un móvil real; el contraste medido en el navegador (solo calculado por diseño); el comportamiento tras un reinicio completo del servidor (el `cron @reboot` está puesto, no probado).

## 5. Límites y riesgos
> [!riesgo]
> - **Sin cortafuegos** en el servidor: cualquier aparato de tu red local puede abrir el panel (es solo lectura). No abrir el puerto 8060 a internet sin añadir acceso con contraseña.
> - El **«por qué»** de T, M y F es genérico («la tendencia es alcista; su parte objetivo es X %»): el bot no guarda cuántas de las 7 señales estaban activas. Mejora pendiente: guardar la señal en cada orden.
> - El valor «en vivo» usa el precio del último trato de Binance, sin tener en cuenta la comisión de venta ni la diferencia de precio.
> - Los números del panel no demuestran nada sobre si las estrategias ganan: ver el [[01_Projects/Bot de Tendencia/1 - PRD|PRD]] y la [[01_Projects/Bot de Tendencia/2 - Prueba Kronos|prueba de Kronos]].

---
Relacionado: [[01_Projects/Bot de Tendencia]]

