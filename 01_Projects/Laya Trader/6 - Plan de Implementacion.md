---
type: doc-software
doc: plan-implementacion
proyecto: "Laya Trader"
status: aprobado
date: 2026-10-22
origen: mixto
---

# 6 · Plan de Implementación — Laya Trader

> [!resumen] En cristiano
> Veintiuna tareas pequeñas, en orden, cada una con una prueba que dice si está hecha. Primero se comprueba lo que más puede salir mal (que Laya conteste lo bastante rápido), luego el motor del bot, después el servidor del panel y las cinco pantallas, y al final se deja corriendo en el servidor Zorin. Nada de dinero real. Código en `~/Proyectos/laya-trader/` dentro del servidor, con git desde el primer commit. Decisión que te toca: aprobar el plan para empezar a construir.

## 1. Fases
| Fase | Objetivo | Entregable demostrable | Historias |
|---|---|---|---|
| 0 Scaffold | Repo, entorno, calidad | `pytest`, `ruff` y `mypy` en verde sobre un proyecto vacío | — |
| 1 Datos | Migraciones y semilla ([[5 - Backend Schema]]) | 13 tablas creadas y probadas en el servidor | US-08, US-09 |
| 2 Núcleo | Bot completo en papel ([[4 - AppFlow]] flujos 2 y 4) | `laya-trader paper --seed 42` repetible, con informe de calibración | US-01 a US-10 |
| 3 UI | API y 5 pantallas ([[3 - UI-UX Design]]) | panel en `http://192.168.0.100:8070` con datos reales | US-11 (y vistas de US-01 a US-09) |
| 4 Pulido | Lenguaje llano, estados, móvil, accesibilidad | checklist de marca y de contraste | US-11 |
| 5 Despliegue | `systemd`, copias, prueba de ciclo completo | bot y panel vivos 7 días sin tocar | US-10, US-11 |

## 2. Tareas
Cada tarea indica archivos (dentro de `~/Proyectos/laya-trader/`), criterio de hecho y dependencias. Las tareas del servidor se ejecutan por `zorin-ssh` (un comando por línea, procesos largos con `nohup`, scripts largos por `sftp-upload`).

**Fase 0**
- [x] T-00 (2026-10-22, commit `1a30e4f`; `pytest`, `ruff` y `mypy` en verde; `requirements.lock` de 53 paquetes) · Repo y entorno: `git init`, `.gitignore` (`.env`, `data/`, `venv/`, `__pycache__/`), `python3 -m venv`, `requirements.txt` con los pines del TRD §1.1 (torch con `--index-url https://download.pytorch.org/whl/cpu`), `pyproject.toml`, `.env.example` vacío. Hecho cuando: `pytest -q`, `ruff check` y `mypy src` salen limpios. Depende de: —.

**Fase 1: datos**
- [x] T-01 (2026-10-22, commit `111607e`; 13 pruebas de esquema: restricciones, `restrict`, `set null`, cascada y solo lectura) · (US-08, US-09) `migrations/001_init.sql` copiado tal cual de `5 - Backend Schema` §2, `src/laya_trader/db.py` (abre con `foreign_keys=ON`, WAL, `user_version`, modo solo lectura para el panel) y `tests/test_schema.py` (las comprobaciones ya probadas: restricciones, `restrict`, `set null`, cascada). Hecho cuando: los tests pasan en el servidor. Depende de: T-00.

**Fase 2: núcleo**
- [~] T-02 (2026-10-22: medido, **NO cumple el criterio**: 6 preguntas p50 2.959 ms y p95 3.034 ms frente al límite de 1.800 ms; ver ficha) · (US-04) **Medir Laya primero** (`scripts/medir_laya.py`): cargar el checkpoint `typed-decisions` ya en caché, contestar las 6 preguntas sobre 50 resúmenes sintéticos, anotar RAM y latencia p50/p95. Hecho cuando: p95 de las 6 preguntas ≤ 1,8 s; si no, se sube `block_seconds` (TRD §8) y se anota. Depende de: T-00.
- [x] T-03 (2026-10-22, commit `28ea166`; 10 min reales: 0 huecos en vivo y 0 errores de lectura; 29 pruebas en verde) · (US-01) `state/feed.py`: libro `depth` y `aggTrade` de BTC/ETH/SOL por WebSocket, sincronización inicial por REST, reconexión con retroceso, edad de los datos. Hecho cuando: 10 minutos sin pérdidas de secuencia y reconecta tras cortar la red (`tests/test_feed.py` con un feed grabado). Depende de: T-00.
- [x] T-04 (2026-10-22, commit tras `28ea166`; 72 pruebas en verde; resumen real de 106-108 tokens medidos por Laya) · (US-02, US-03) `state/features.py` y `state/snapshot.py`: los rasgos del Backend Schema §6.2 y el texto ≤ 380 tokens medidos con el tokenizador de Laya. Hecho cuando: tests con casos conocidos (microprecio, desequilibrio) y el recorte nunca quita mid ni spread. Depende de: T-02, T-03.
- [x] T-05 (2026-10-22; probado con 30 estados reales: las 6 respuestas válidas siempre; primera llamada 7,5 s y el resto p95 3,0 s, por eso `warm_up()`) · (US-04) `judgment/laya.py` (batería de 6 preguntas con `laya.Router`) y `judgment/fallback.py` (el juez de reserva de §6.1). Hecho cuando: ambos devuelven las 6 respuestas válidas y tipadas, y el fallback es determinista. Depende de: T-02, T-04.
- [x] T-06 (2026-10-22; 107 pruebas en verde; ejemplo numérico exacto 84.502,71 / 84.680,37; Kelly normalizado aprobado por Haytham) · (US-05) `policy/` y `pricing/`: política §6.3, tamaño Kelly fraccional y precios Avellaneda-Stoikov §6.4. Hecho cuando: el ejemplo numérico (σ=4, q=0,5, mid 84.600 → 84.502,7 / 84.680,4) sale exacto y los precios respetan `tick_size`. Depende de: T-05.
- [x] T-07 (2026-10-22; 140 pruebas en verde entre T-07 y T-08; un test por veto con su frontera y por escalón) · (US-06, US-07) `risk/` y `loop/ladder.py`: los 6 vetos de §6.5, el interruptor y la escalera de 5 escalones. Hecho cuando: un test por veto y por escalón, y tras `kill_switch` el bot no reanuda solo. Depende de: T-06.
- [x] T-08 (2026-10-22; órdenes post-only con cola, comisión 0,10 %, cierre contra el libro real y resultado a 900 s) · (US-08) `execution/paper.py`: órdenes post-only, cola estimada, ejecución al imprimirse una operación real, comisión 0,10 %, y `outcome` a 900 s (§6.6 y §6.7). Hecho cuando: tests de ejecución, no ejecución por cola y valoración del resultado. Depende de: T-06.
- [x] T-09 (2026-10-22; repetición de la grabación real de 10 min con el motor completo: 149 turnos en 2 s y dos repeticiones dan huellas idénticas en las 11 tablas; feed sintético de 25 min con ejecuciones, resultados y caja cuadrada con las ejecuciones guardadas) · (US-07, US-10) `loop/` y CLI `laya-trader paper --seed N [--replay ARCHIVO]`: los dos jueces con el mismo bloque, carteras separadas, plazo del bloque y degradación a reserva. Hecho cuando: dos ejecuciones con la misma semilla y el mismo feed grabado dan resultados idénticos. Depende de: T-07, T-08, T-01.
- [x] T-10 (2026-10-22; 184 pruebas en verde en total; sello con los tres estados sobre muestras construidas; informe en español con `laya-trader calibrate`) · (US-09, US-11) `calibration/`: JSONL, Brier, log loss, ECE, curva de fiabilidad, Platt, bootstrap con bloques de 1 h y `verdict_snapshot` cada minuto (§6.8); CLI `laya-trader calibrate`. Hecho cuando: contra datos sintéticos conocidos devuelve «todavía no se sabe» con poca muestra y el veredicto correcto con una muestra construida. Depende de: T-09.

**Fase 3: panel**
- [x] T-11 (2026-10-22, commit `8252c7e`; 8 rutas más el canal en vivo, 21 pruebas de API, incluida una de regresión para el uso de la conexión entre hilos que solo fallaba en el servidor real) · (US-11) `panel/api.py`: FastAPI de solo lectura con las 8 rutas y el SSE del AppFlow §5, textos de error en lenguaje llano, base abierta con `mode=ro`. Hecho cuando: tests de cada ruta, incluidos 404 y 400, y el SSE reanuda con `Last-Event-ID`. Depende de: T-01, T-10.
- [x] T-12 (2026-10-22; comprobado en el navegador integrado: 5 rutas sin desplazamiento horizontal a 375 px, objetivos táctiles ≥ 44 px, claro y oscuro, contraste AA en todos los pares, estados de carga, vacío, error de conexión y recuperación automática) · (US-11) Base visual: tokens CSS, tipografías Plex autoalojadas (`npm pack @fontsource/ibm-plex-sans @fontsource/ibm-plex-mono`, licencia OFL), `lightweight-charts` 5.2.1 vendorizado con su licencia, carril y barra inferior, punto en vivo, conmutador claro/oscuro, los seis estados globales. Hecho cuando: la cáscara carga sin errores en 375 px y 1200 px, claro y oscuro. Depende de: T-11.
- [x] T-13 (2026-10-22, commit `ff2e8a8`; sello con los tres estados, línea «qué falta», 4 cifras con frase llana, curva de dinero con etiqueta directa, leyenda, tabla alternativa y selector de periodo; revisado en navegador a 375 px y 1200 px, claro y oscuro) · (US-11, US-09) P1 Veredicto: sello, línea «qué falta», 4 KPI con frase llana, curva de dinero Laya vs reserva con etiqueta directa y tabla alternativa. Hecho cuando: con datos de prueba muestra los tres estados del sello. Depende de: T-12.
- [x] T-14 (2026-10-22; precio con `series.update()` y marcas con `createSeriesMarkers`, un clic en la flecha abre esa decisión (comprobado en el navegador), 6 tarjetas de preguntas con respuesta y seguridad de Laya y del programa de reglas, libro de 10 niveles (3 en móvil), lo último que decidió cada uno) · (US-01, US-02, US-04, US-08) P2 Mercado: pestañas por moneda, gráfica con `series.update()` y `createSeriesMarkers`, chips de los 6 juicios con su frase llana, mini-libro (lista simple en móvil). Hecho cuando: las marcas llevan a `#/registro?id=…`. Depende de: T-12, T-11.
- [x] T-15 (2026-10-22, commit `b736ec2`; comparación con «mejor» marcado, curva de fiabilidad en SVG con círculos y cuadrados, tabla alternativa, medidor de casos y qué preguntas se pueden comprobar) · (US-09) P3 Calibración: tarjetas Brier/log loss/ECE con explicación, curva de fiabilidad en SVG, tabla por pregunta, estado «muestra insuficiente». Depende de: T-12, T-10.
- [x] T-16 (2026-10-22; nivel de prudencia con sus 5 pasos y su historial, seis frenos con semáforo, leyenda y enlace a las decisiones afectadas —filtro `veto` nuevo en la API—, aviso del interruptor con comando copiable e histograma de la rapidez de Laya) · (US-06, US-07, US-10) P4 Riesgo y sistema: semáforo con leyenda, vetos clicables, escalera, histograma de latencia, comando de reinicio copiable. Depende de: T-12, T-07.
- [x] T-17 (2026-10-22; lista con filtros por moneda, quién, acción y freno, «cargar más», detalle con el texto exacto que leyó Laya, las seis respuestas, órdenes, ejecuciones y resultado; en móvil el detalle ocupa la pantalla con «Volver a la lista»; solo orden de más reciente a más antigua, el orden contrario no se hizo) · (US-07, US-09) P5 Registro: lista con filtros, orden y «cargar más», detalle con el texto exacto que leyó Laya. Depende de: T-12, T-11.

**Fase 4: pulido**
- [x] T-18 (2026-10-22; barrido automático de contraste de todo el texto en las 5 pantallas, claro y oscuro: cumple (los 3 «fallos» del barrido eran un error de lectura de `color-mix`, comprobado a mano: 18,7 / 5,1 / 7,7); 1 título por pantalla sin saltos, todos los botones con nombre, foco visible con teclado, `prefers-reduced-motion`; se añadieron USDT y Binance a la ayuda) · (US-11) Lenguaje y accesibilidad: diccionario de etiquetas (UI/UX §4.2), botón «¿Cómo leo esto?» en cada pantalla, foco visible, `prefers-reduced-motion`, contraste AA medido (`ink-3` en claro y oscuro), objetivos táctiles ≥ 44 px, `scrollWidth === clientWidth` en las 5 rutas. Hecho cuando: pasa el checklist de marca del UI/UX §8 con el navegador integrado de Claude. Depende de: T-13 a T-17.

**Fase 5: despliegue y documentación**
- [x] T-19 (2026-10-22; **el bot corre en vivo desde las 16:13 CEST**. Servicios de **usuario** de systemd con `linger` (el servidor no deja escribir en `/etc/systemd`), copia diaria a las 04:00, permisos 600, panel solo en `192.168.0.100:8070`. Pruebas: reinicio del servicio (el panel no se cae, nueva puesta en marcha que el veredicto suma) y congelación del bot 30 s (frenos `stale_feed`, escalón 3, conexión caída y recuperada, vuelta a normal)) · (US-10, US-11) `systemd` (motor y panel como dos servicios), `chmod 600` de datos, copia diaria `sqlite3 .backup`, rotación de JSONL, panel en la IP de la LAN, puerto 22 sin tocar. Hecho cuando: sobrevive a `systemctl restart` y a un corte de red de 30 s (AppFlow §7). Depende de: T-09, T-18.
- [ ] T-20 · (US-09, US-11) Ciclo de aceptación: 24 h supervisadas y luego 7 días; cada día se anota el sello en la ficha. Hecho cuando: se cumplen los criterios del PRD §9. Depende de: T-19.
- [x] T-21 (2026-10-22; README del repo, sesión, guía de skills, `CLAUDE.md` y `GEMINI.md` del vault, `COMMON_MISTAKES` (47-57), `librerias.md`, Scalper Memecoins marcado como abandonado y grafo actualizado) · Documentación (CLAUDE.md §0.8): ficha `01_Projects/Laya Trader.md`, `README.md` del repo, sesión en `00_Meta/Sesiones/`, `GEMINI.md`/`CLAUDE.md` del vault, `Guia - Skills y reglas por fase.md`, `.claude/COMMON_MISTAKES.md`, trampas nuevas en `librerias.md`, marcar «Scalper Memecoins» como abandonado y actualizar el grafo con `graphify update .`. Depende de: T-19.

## 2.1 Starter kits reutilizados
| Kit | Fase | Adaptación |
|---|---|---|
| Dashboard base (solo el layout de [[Biblioteca de Layouts]]) | 3 | Se usa la estructura de slots; el código se escribe nuevo (HTML/CSS/JS sin React) |
| Nada del Bot de Tendencia ni de Scalper Memecoins | — | Por decisión de Haytham (2026-10-22): no se copia código ni diseño. Solo se reutilizan el checkpoint de Laya ya en caché y los pines de versiones de `librerias.md` |

Candidato a kit nuevo al terminar: «Panel de solo lectura con SSE y lightweight-charts».

## 3. Estrategia de pruebas
- **Unitarias** por módulo con casos numéricos conocidos (rasgos, precios, vetos, ejecución, métricas de calibración).
- **Reproducibilidad**: mismo feed grabado + misma semilla = mismos resultados (T-09).
- **Contrato de API**: un test por ruta y por error (T-11).
- **Datos sintéticos de veredicto**: se construye una muestra donde Laya es claramente peor, igual y mejor que la reserva, y el sello debe dar los tres resultados correctos (T-10).
- **Ciclo equivalente en producción** (T-19): arrancar → ver el primer bloque → F5 → reiniciar servicio → cortar el feed → restaurar, sin puntos duplicados.
- **Pruebas visuales** en el navegador integrado de Claude (DevTools de Chrome no disponible): 375 px y 1200 px, claro y oscuro; declarar cualquier cosa que no se pueda ver.

## 4. Despliegue y operación
- Todo en Zorin: `~/Proyectos/laya-trader/` con `venv`, `data/` (SQLite, JSONL, copias) fuera de git. Dos servicios `systemd`: `laya-trader` (motor) y `laya-panel` (panel :8070).
- Sin secretos ni claves de exchange. `.env.example` sin valores. Antes de cada comando destructivo o que toque `systemd`, confirmar con Haytham.
- Memoria: ~2,5 GB en uso con Laya cargada; vigilar los 7,6 GB totales del servidor. Los otros proyectos del servidor no se tocan.
- Reinicio tras interruptor de emergencia: solo manual por SSH.

## 5. Riesgos y plan B
> [!riesgo]
> - **Laya demasiado lenta** (T-02): subir `block_seconds`; si aun así p95 > 4 s, reducir a 3 preguntas y anotarlo como cambio de v1 (invalida la comparación con el diseño de 6 preguntas, se decide con Haytham).
> - **Binance corta o bloquea**: la escalera deja el bot en `hold`; plan B, REST con sondeo cada 2 s solo para pruebas.
> - **Pocas ejecuciones por el spread de 10,5 bps**: es esperado; el sello seguirá en «todavía no se sabe» y la ficha lo dirá; no se baja el spread para ver más operaciones (regla congelada).
> - **RAM del servidor**: si Laya y el panel superan 5 GB, reiniciar el motor y avisar; no se cargan modelos extra.
> - **Tentación de ajustar tras ver resultados**: prohibido; cualquier cambio de §6 del Backend Schema abre un `run` nuevo y se anota con fecha.

## 6. Definición de terminado
- [x] `trace_lint.py` en `RESULTADO: OK`
- [x] `schema_to_migration.py`: no aplica (SQLite); sustituido por `tests/test_schema.py` en verde
- [x] `pytest`, `ruff` y `mypy` limpios en el servidor (210 pruebas)
- [x] Checklist de marca del UI/UX §8 y contraste AA verificado (el punto «no parece plantilla» es opinión de Haytham)
- [x] README en el repo (con la IP del panel como marcador)
- [x] Ficha en `01_Projects/` y sesión registrada
- [x] `.claude/COMMON_MISTAKES.md` actualizado
- [ ] 7 días de ejecución sin intervención y veredicto anotado

---
Anterior: [[5 - Backend Schema]]
