---
type: plan
status: en-progreso
date: '2026-10-23'
proyecto: '[[01_Projects/Battle Royale]]'
tags:
- panel
- ui
- ux
- plan
origen: mixto
---

> [!resumen] En cristiano
> Plan para convertir el panel en una herramienta de trabajo. Se hace como una **página web local** (que ya cabe en el servidor) mostrada dentro de la ventana de siempre, y que además podrás abrir desde tu PC. Son 8 fases pequeñas y cada una se puede revisar por separado: primero la base y el estado general con avisos; luego las candidatas con filtros y seguimiento (lo que más dinero te da); después los bots con gráficas; y al final la ventana, los avisos al móvil y el pulido. **No se ha tocado nada todavía**: necesito tu visto bueno y 5 decisiones (al final). Investigación: [[01_Projects/Battle Royale/Panel - Investigacion de librerias]].

# Panel del servidor v5 · Implementation Plan

> **Para quien lo ejecute:** usar `superpowers:subagent-driven-development` (recomendado) o `superpowers:executing-plans`, tarea a tarea, con las casillas `- [ ]`. Antes de cada tarea de interfaz: skills `hallmark` (pantallas nuevas), `dataviz` (gráficas) y, al terminar cada fase, `impeccable critique` y `impeccable audit`.

**Goal:** que el panel diga en 2 segundos si todo va bien, y que sirva para trabajar las candidatas del scraper (filtrar, marcar, copiar, exportar) y seguir los bots, tanto en el monitor del servidor como desde el PC.

**Architecture:** un servidor web pequeño (FastAPI + plantillas Jinja2 + htmx para filtros y actualizaciones, Alpine.js para detalles, uPlot para gráficas) escucha en el propio servidor; un servicio colector guarda historial de métricas en SQLite; la ventana nativa pasa a ser un envoltorio WebKitGTK a pantalla completa. El panel Cairo actual se conserva como respaldo hasta que lo apruebes.

**Tech Stack:** Python 3.12.3, FastAPI 0.161.1, uvicorn 0.54.0, Jinja2 3.1.6, sse-starlette 3.5.0, SQLite (WAL), psutil 7.2.2, PyGObject con WebKit2 4.1, htmx 2.0.11 + htmx-ext-sse 2.2.4, Alpine.js 3.17.5, uPlot 1.6.32; opcionales: SortableJS 1.15.7, segno 1.6.6, Apprise 2.0.1. Versiones verificadas el 2026-10-23.

**Spec:** [[01_Projects/Battle Royale/Panel - Investigacion de librerias]] y las ideas aprobadas en el chat del 2026-10-23 (semáforo con avisos, candidatas como herramienta, historial y gráficas, comodidad de uso).

## Intención y alcance

- **Objetivos**
  1. Un semáforo global con una frase y avisos reales; todos los datos con su edad.
  2. Candidatas como herramienta de trabajo: estados guardados, filtros, buscador, «nuevas», cola «a llamar hoy», ficha con botones de copiar, exportar a CSV, borrador de mensaje con la oferta y QR de la web.
  3. Historial de 24 h y 7 días de RAM, CPU, temperatura y disco; progreso del scraper (webs por hora, mosaico de zonas, hora estimada de fin).
  4. Bots: curva de capital de los 3 finalistas frente a la banda del azar, barra de días hasta el veredicto, y cuánto le falta a cada moneda para disparar.
  5. Se abre desde el PC por la red de casa (para revisar y trabajar) y en el monitor vertical del servidor.
- **No objetivos:** ninguna IA decidiendo (el borrador de mensaje sale de plantillas por reglas); ni Laya Trader ni los bots de cron (están retirados); ni enviar correos desde el panel; ni exponer nada a internet.
- **Anti-objetivos (sería un fracaso aunque «funcione»):** mostrar datos viejos como si fueran actuales; perder los estados de candidatas al regenerarse el CSV del scraper; escribir desde la red sin PIN; que el panel haga el servidor más lento o se coma la RAM; textos con jerga sin traducir.

## Restricciones globales (todas las tareas las incluyen)

- Python 3.12.3 en el servidor; **no hay Node ni navegador**: las librerías JS se vendorizan (se descargan una vez y se guardan en `web/estaticos/js/vendor/` con su hash en `VENDOR.md`).
- Monitor del servidor: 1080×1920 vertical, GNOME en Wayland; la interfaz también debe verse bien en 1440×900 y en 390×844 (móvil).
- Presupuesto de RAM: colector + web ≤ 200 MB y vista WebKit ≈ 370 MB (medida el 2026-10-23, a repetir en ventana real); total ≤ 700 MB de los 5,7 GB libres.
- Lenguaje sencillo en todos los textos de pantalla (regla de Haytham, 2026-10-21): conclusión primero, términos técnicos traducidos.
- Ningún secreto en el repositorio: claves de avisos en `~/.config/battle-royale/` con permisos 600.
- Todas las horas se muestran en hora local (Europe/Madrid).
- Contraste mínimo AA en todos los pares de colores; el estado nunca se indica solo con color (siempre icono o texto).
- Datos que ya existen y no se duplican: `torneo.db`, `torneo_literal.db`, `leads.db`, `salida/leads_actual.csv`, `salida/segmentos/*.csv`, journal de systemd.
- Intervalos vigentes: scraper cada 1 h con 1 h entre zonas; vivo en el minuto 02 de cada hora.

## Foco de revisión (lo que más probablemente fallaría y no está en la especificación)

1. **Colector parado** → la pantalla enseñaría datos viejos con aspecto de actuales. Debe aparecer «DATOS VIEJOS» y semáforo crítico a los 2 min. (test en F2)
2. **Candidatas que cambian de nombre o desaparecen** del CSV tras un ciclo → el estado guardado se pierde o queda huérfano. La clave es el `dominio`; huérfanos se conservan y se marcan. (test en F4)
3. **Escritura desde la red sin PIN** (cualquiera en casa podría marcar candidatas). (test en F6)
4. **Tres procesos escribiendo en SQLite** (colector, web, vivo) → «database is locked». WAL, `timeout` y prueba de concurrencia. (F0 y F1)
5. **Fuga de memoria** de la vista WebKit con actualizaciones en vivo 24 h seguidas. Medición de 24 h y reinicio de la vista cada noche si crece. (F6)
6. **Lista de candidatas creciendo** de 261 a miles (el scraper sigue por zonas) → paginación en el servidor desde el inicio. (F4)

## Modelo de datos nuevo (`data/panel.db`, SQLite STRICT, WAL)

```
muestras(t INTEGER PRIMARY KEY, ram_pct REAL, cpu_pct REAL, temp REAL, disco_pct REAL, red_rx REAL, red_tx REAL)   -- una cada 30 s, 30 días
scraper_hora(hora INTEGER PRIMARY KEY, webs_leidas INTEGER, empresas INTEGER, con_correo INTEGER)                    -- por hora, desde leads.db
avisos(id INTEGER PRIMARY KEY, regla TEXT, severidad TEXT, desde INTEGER, hasta INTEGER, texto TEXT, notificado INTEGER)
candidatas_estado(dominio TEXT PRIMARY KEY, estado TEXT, nota TEXT, primera_vez INTEGER, actualizado INTEGER)
candidatas_historial(id INTEGER PRIMARY KEY, dominio TEXT, estado TEXT, nota TEXT, cuando INTEGER)
equity_vivo(dia TEXT, nombre TEXT, capital REAL, PRIMARY KEY(dia, nombre))
ajustes(clave TEXT PRIMARY KEY, valor TEXT)
```

Estados de candidata (mi suposición, ver decisiones): `nueva` → `por_llamar` → `contactada` → `respondio` → `reunion`, y `descartada` (oculta por defecto).

## Reglas de aviso iniciales (umbrales propuestos por mí)

| Regla | Aviso | Crítico |
|---|---|---|
| Disco | ≥ 85 % | ≥ 95 % |
| RAM | ≥ 90 % durante 5 min | ≥ 97 % durante 5 min |
| Temperatura | ≥ 80 °C | ≥ 90 °C |
| Servicio nuestro en fallo (`failed`) | — | siempre |
| Scraper sin ciclo | > 2 h | > 6 h |
| Zonas con error de Overpass | 3 seguidas | 6 seguidas |
| Vivo sin ciclo | > 90 min | > 3 h |
| Colector sin muestras | — | > 2 min («datos viejos») |
| Candidatas A nuevas | informativo: «N nuevas desde ayer» | — |

## Estructura de archivos

```
src/battle_royale/
  panel_db.py              abrir() y migraciones de panel.db
  colector.py              muestrear_sistema, muestrear_scraper, purgar, serie, bucle
  alertas.py               Regla, Contexto, evaluar_todas, estado_global
  candidatas.py            Filtros, listar, cambiar_estado, exportar_csv, borrador
  senales.py               estado_senal, proximas_senales
  notificar.py             (opcional) envío con Apprise
  ventana.py               ventana GTK + WebKit2 a pantalla completa
  web/
    app.py                 create_app()
    rutas_general.py  rutas_candidatas.py  rutas_torneos.py  rutas_ajustes.py
    plantillas/            base.html general.html candidatas.html torneos.html ajustes.html parciales/*.html mensajes/*.txt
    estaticos/             css/panel.css  js/vendor/*  js/panel.js  fonts/*  VENDOR.md
scripts/vendorizar_web.py
tests/ test_panel_db.py test_colector.py test_alertas.py test_candidatas.py test_senales.py test_web_*.py test_vendor.py
```

## Fases y tareas

Tamaños: S pequeña, M media, L grande. Cada fase termina con algo que puedes revisar.

### Fase 0 · Cimientos (M) — revisable: `/salud` responde y la base existe
- [x] **T0.1 Vendorizar librerías.** Files: `scripts/vendorizar_web.py`, `web/estaticos/js/vendor/*`, `web/estaticos/fonts/*`, `web/estaticos/VENDOR.md`, test `tests/test_vendor.py`. Interfaz: `vendorizar(paquete: str, version: str, archivos: dict[str, Path]) -> None` (baja el `.tgz` de `registry.npmjs.org`, comprueba el `sha512` de `dist.integrity`, extrae solo lo necesario, anota versión y hash). Hecho cuando: los 5 archivos JS y las fuentes Inter están y `test_vendor` verifica que el hash de cada archivo coincide con `VENDOR.md`.
- [x] **T0.2 Base de datos.** Files: `panel_db.py`, `tests/test_panel_db.py`. Interfaz: `abrir(ruta: Path = PANEL_DB) -> sqlite3.Connection` (WAL, `timeout=30`, crea el esquema de arriba con migraciones numeradas). Test: abrir dos veces es idempotente; dos hilos escribiendo a la vez no lanzan `database is locked`.
- [x] **T0.3 Aplicación web mínima.** Files: `web/app.py`, `web/plantillas/base.html`, unidad `panel-web.service` (`127.0.0.1:8090`), `tests/test_web_base.py`. Interfaz: `create_app(db_path: Path | None = None, ahora: Callable[[], float] = time.time) -> FastAPI`; `GET /salud -> {"ok": true, "version": str}`. Test con `TestClient`.
- [x] **T0.4 Línea base de RAM.** Medir el servicio vacío y anotarlo en la nota (objetivo ≤ 100 MB).

### Fase 1 · Colector e historial (M) — revisable: gráficas de 24 h con datos reales
- [x] **T1.1 Muestras del sistema.** Files: `colector.py`, `tests/test_colector.py`. Interfaces: `muestrear_sistema(con, ahora: float) -> None` (usa `sistema.memoria()`), `purgar(con, dias: int = 30) -> int`, `serie(con, metrica: str, desde: float, hasta: float, puntos: int = 240) -> list[tuple[int, float]]` (promedia por cubos). Tests: insertar 1.000 muestras sintéticas, `serie` devuelve ≤ 240 puntos ordenados y con la media correcta; `purgar` borra solo lo viejo.
- [x] **T1.2 Progreso del scraper por hora.** Interfaz: `muestrear_scraper(con, leads_db: Path) -> None` (cuenta `rastreado_en` por hora, solo lectura sobre `leads.db`). Test con una base temporal.
- [x] **T1.3 Bucle y servicio.** `bucle(intervalo_s: int = 30) -> None`; subcomando `python -m battle_royale colector`; unidad `panel-colector.service` (`Restart=on-failure`). Hecho cuando el servicio lleva 1 h y la tabla tiene ~120 filas.

### Fase 2 · Avisos y semáforo (M) — revisable: semáforo real arriba, probado con fallos simulados
- [x] **T2.1 Motor de reglas.** Files: `alertas.py`, `tests/test_alertas.py`. Interfaces: `Aviso(regla: str, severidad: Literal["info","aviso","critico"], texto: str)`, `Contexto(muestras: list, scraper: dict, proyectos: list, combate: dict, ahora: float)`, `evaluar_todas(ctx) -> list[Aviso]`, `estado_global(avisos) -> tuple[Literal["ok","aviso","critico"], str]` (la frase en lenguaje sencillo: «Todo bien», «1 aviso: el scraper lleva 3 h sin ciclo»). Un test por regla de la tabla (con valores justo debajo y justo encima del umbral).
- [x] **T2.2 Frescura.** `edad_datos(ctx) -> float`; si el último muestreo tiene más de 2 min, aviso crítico «DATOS VIEJOS». Test del foco 1.
- [x] **T2.3 Persistencia.** Guardar avisos con `desde`/`hasta` sin duplicar mientras sigan activos; `GET /api/avisos`.

### Fase 3 · Interfaz general (L) — revisable: página «General» completa en el navegador de tu PC
- [x] **T3.1 Diseño base.** Files: `web/estaticos/css/panel.css`, `web/plantillas/base.html`. Variables CSS con la paleta actual (fondo `#060a14`/`#0c1530`, azul `#3b82f6`, cian `#22d3ee`, violeta `#a78bfa`, verde `#34d399`, ámbar `#fbbf24`, rojo `#f87171`), Inter, escala tipográfica fluida, rejilla de tarjetas, barra superior fija (semáforo + frase + reloj + «datos de hace N s»), navegación por pestañas (General · Candidatas · Torneos · Ajustes), modo noche y tamaño de letra «cerca/lejos» guardados en `localStorage`. Test: un script comprueba que todos los pares texto/fondo cumplen contraste AA.
- [x] **T3.2 Tarjetas.** Parciales `servidor.html` (anillo de RAM en SVG, tiles de disco/temperatura/encendido/red, gráfica uPlot con selector 3 h · 24 h · 7 d), `bots.html`, `scraper.html` (webs por hora, **mosaico de las 33 zonas** con estado hecha/en curso/pendiente, hora estimada de fin, segmentos «a llamar ya / correo frío / descartar»), `actividad.html`. Rutas `GET /` y `GET /parciales/<nombre>`.
- [x] **T3.3 Tiempo real.** `GET /stream` con `sse-starlette`: eventos `metricas`, `avisos`, `actividad` cada 3 s solo si cambian; la página usa `hx-ext="sse"` con reconexión automática. Si el flujo se corta 10 s, aparece «Sin conexión con el servidor».
- [x] **T3.4 Revisión visual.** Comprobar en 1080×1920, 1440×900 y 390×844 con el navegador integrado (capturas), y pasar `impeccable critique` y `audit`. Hecho cuando no hay desbordes y todo texto es legible a 2 m (prueba real en el monitor).

### Fase 4 · Candidatas como herramienta de trabajo (L) — revisable: la usas con candidatas reales
- [x] **T4.1 Lógica.** Files: `candidatas.py`, `tests/test_candidatas.py`. Interfaces: `Filtros(niveles: set[str], sectores: set[str], contacto: set[str], estados: set[str], solo_nuevas: bool, texto: str)`, `listar(con, filtros, orden: str, pagina: int, por_pagina: int = 50) -> Pagina`, `cambiar_estado(con, dominio: str, estado: str, nota: str, ahora: float) -> None`, `cambiar_en_bloque(con, dominios: list[str], estado: str, ahora: float)`, `exportar_csv(con, filtros) -> str`, `borrador(candidata: dict) -> str`. Los datos salen de `leads.db` en solo lectura y los estados de `panel.db`. Tests: filtros combinados; «nuevas» = primera vez vista en las últimas 24 h; **huérfanos** (foco 2); paginación a 261 y a 5.000 filas.
- [x] **T4.2 Rutas.** `GET /candidatas`, `GET /candidatas/tabla` (fragmento htmx con filtros, orden y buscador con retraso de 250 ms), `GET /candidatas/{dominio}` (ficha en `<dialog>`), `POST /candidatas/{dominio}/estado`, `POST /candidatas/bloque`, `GET /candidatas.csv`.
- [x] **T4.3 Vistas.** Lista y tablero (arrastrar con SortableJS) con interruptor «mostrar descartadas» (ocultas por defecto), vistas guardadas («por llamar hoy», «nuevas», «nivel A con correo»), contador de la cola «a llamar hoy», orden por defecto por prioridad.
- [x] **T4.4 Ficha.** Botones de copiar correo, teléfono y web (Alpine; respaldo sin portapapeles moderno), borrador de primer mensaje en `plantillas/mensajes/<tipo_de_oferta>.txt` (por reglas, sin IA), QR de la web en SVG (`segno`), historial de cambios de estado y notas.
- [x] **T4.5 Seguridad de escritura.** Todo `POST` exige cookie de sesión local o PIN cuando se accede por la red (ver F6); registro de cambios en `candidatas_historial`.

### Fase 5 · Torneos y bots (L) — revisable: por qué hay 0 operaciones, a la vista
- [x] **T5.1 Distancia a la señal.** Files: `senales.py`, `tests/test_senales.py`. Interfaces: `estado_senal(estrategia: str, mercado: Mercado) -> dict` (`distancia_pct`, `condicion`, `texto`), `proximas_senales(con, mercados) -> list[dict]` ordenadas de más cerca a más lejos. Para `donchian`: distancia del cierre al máximo de 55 velas; para `squeeze_volumen`: percentil del ancho de Bollinger y volumen frente a su media. Tests con mercados sintéticos.
- [x] **T5.2 Curva de capital y azar.** Guardar `equity_vivo` cada día desde `vivo_ops`; `banda_azar(con, dias: int = 30, reps: int = 200) -> tuple[list[float], list[float]]` reutilizando `azar.py`. Endpoint `/api/equity`.
- [x] **T5.3 Página «Torneos».** Curvas uPlot de los 3 finalistas con la banda del azar, barra «día X de 30» con lo que decide el veredicto, tabla del pasado (R1-R3) y del literal con y sin comisión, y repetición de 30 días bajo demanda (`vivo.repetir(con, dias) -> dict`, a partir de `scripts/repetir_vivo.py`).

### Fase 6 · Ventana WebKit y acceso desde el PC (M) — revisable: en el monitor del servidor y en tu navegador
- [x] **T6.1 Ventana.** Files: `ventana.py`, cambio en `__main__.py` (`panel` abre la ventana WebKit; `panel --cairo` conserva la actual). GTK3 + WebKit2 4.1, `http://127.0.0.1:8090/?kiosko=1`, pantalla completa, F11/Esc/Ctrl+Q, recarga sola si el servidor se reinicia. Decidir con la medida real si hace falta `WEBKIT_DISABLE_COMPOSITING_MODE=1`.
- [x] **T6.2 Acceso por la red de casa.** `--lan` (escucha en `192.168.0.100:8090`); lectura libre; escritura con **PIN** (hash en `ajustes`, cookie de 30 días, límite de intentos). Test del foco 3: `POST` sin PIN desde una IP no local devuelve 403.
- [ ] **T6.3 Servicios.** `panel-ventana.service` pasa a ejecutar la ventana con `After`/`Wants` de web y colector. Medir RAM de 24 h (foco 5); si crece, reinicio nocturno de la vista.

### Fase 7 · Avisos al móvil (S, opcional) — revisable: llega un aviso de prueba
- [ ] **T7.1** `notificar.py`: `enviar(aviso: Aviso) -> bool` con Apprise (o `curl` a ntfy si lo eliges), solo avisos **críticos** y un resumen diario a las 09:00; enfriamiento de 30 min por regla; claves en `~/.config/battle-royale/notificaciones.env` (600). Test con un servicio falso.

### Fase 8 · Pulido, documentación y entrega (M)
- [ ] **T8.1** Ajustes (umbrales, tema, tamaño de letra, PIN), `impeccable polish`, `accessible-animation` si hay movimiento, revisión final en el monitor a distancia real.
- [ ] **T8.2** README del repositorio, ficha del vault, sesión del día, `CLAUDE.md` y `GEMINI.md` (regla de sincronía), `graphify update .`.
- [ ] **T8.3** Retirar el panel Cairo **solo si tú lo apruebas**.

## Cómo lo revisarás
- Tras cada fase te paso la dirección (`http://192.168.0.100:8090` si aceptas el acceso por la red, o capturas si no) y una lista corta de qué mirar.
- Hay tres paradas de revisión obligatorias: tras la Fase 3 (general), tras la Fase 4 (candidatas) y tras la Fase 6 (ventana).
- Lo que no se pueda comprobar sin el monitor real (tamaño de letra a distancia, RAM de la ventana) quedará marcado como «pendiente de tu vista».

## Riesgos conocidos
- WebKitGTK fuera de pantalla no tiene OpenGL: se mide en ventana real.
- uPlot tiene documentación floja y su última versión es de marzo de 2025: si da problemas, plan B Chart.js 4.6.1 (MIT, activo).
- Leaflet y los mapas de OpenStreetMap quedan fuera de la primera entrega (el mosaico de zonas basta); si se añaden, atribución y User-Agent propio.
- Más piezas en marcha (web + colector + ventana + vivo): se vigilan con el propio panel.

## Decisiones que te tocan (mi recomendación primero)
1. **Camino:** página web local + ventana WebKit (recomendado) frente a seguir con Cairo.
2. **Acceso desde tu PC por la red de casa:** sí, lectura libre y escritura con PIN (recomendado).
3. **Estados de candidata:** `nueva`, `por llamar`, `contactada`, `respondió`, `reunión`, `descartada` (mis supuestos): ¿te valen o quieres otros?
4. **Avisos al móvil:** ntfy (el más simple), Telegram o ninguno (en la Fase 7, se puede dejar para más tarde).
5. **Mapa de zonas:** mosaico sin mapa (recomendado) o mapa con Leaflet.

## Autorrevisión del plan
- Cobertura: semáforo y avisos (F2), frescura (F2), candidatas con estados, filtros, buscador, nuevas, cola, ficha, copiar, borrador, QR, exportar (F4), historial 24 h/7 d (F1, F3), progreso del scraper, mosaico y hora de fin (F1, F3), curva de capital, barra de 30 días y distancia a la señal (F5), modo noche y tamaño de letra (F3, F8), avisos al móvil (F7), acceso desde el PC (F6).
- Proporción: plan largo pero cada tarea lleva interfaces, pruebas y criterio de «hecho»; el código no se escribe aquí.
- Pendiente tras tu aprobación: convertir cada fase en pasos pequeños de pruebas primero con `superpowers:writing-plans` en `docs/superpowers/plans/` del repositorio del servidor y empezar por la Fase 0.


## Registro de ejecución

### Fase 0 · Cimientos — hecha el 2026-10-23
> [!resumen] En cristiano
> El servidor ya tiene una pequeña página web propia funcionando (todavía vacía), con su base de datos y las librerías guardadas dentro del proyecto. Gasta 50 MB de RAM, muy por debajo del límite de 100 MB. Hasta la Fase 3 no verás pantallas nuevas.

- **T0.1 Vendorizar**: `scripts/vendorizar_web.py` baja de npm htmx 2.0.11, htmx-ext-sse 2.2.4, Alpine 3.17.5, uPlot 1.6.32 e Inter 5.3.0 (latin 400-800), comprueba el sha512 del paquete y escribe `VENDOR.md` con el sha256 de cada archivo (15 archivos, 344 KB). `tests/test_vendor.py` (4 pruebas) verifica existencia, versión, licencia y hash.
- **T0.2 Base de datos**: `panel_db.py` con migraciones por `PRAGMA user_version`, WAL, tablas STRICT y `timeout=30`. 5 pruebas, incluida la de 4 hilos escribiendo a la vez sin «database is locked» (foco de revisión 4).
- **T0.3 App web**: `web/app.py` (`create_app(db_path, ahora)`), `GET /salud`, `GET /`, estáticos locales, plantilla `base.html` sin ningún recurso externo (probado). Unidad `panel-web.service` en `127.0.0.1:8090`, activada. Subcomando `python -m battle_royale web`. 6 pruebas.
- **T0.4 RAM base**: 50 MB de RSS tras 20 peticiones; la portada responde en ~1,3 ms. Plan para colector + web ≤ 200 MB: va holgado.
- Suite completa: **147 pruebas pasan**.

**Mis decisiones en esta fase (revísalas):**
1. `TestClient` de esta versión de FastAPI/Starlette exige el paquete **`httpx2`**: añadido como dependencia de desarrollo.
2. **Alpine.js no trae archivo de licencia en npm**: `licencias/alpinejs.LICENSE` es un aviso con la licencia MIT que consta en npm y no el texto íntegro. No inventé el texto.
3. La firma de `vendorizar` quedó como `vendorizar(paquete, version, licencia, archivos, destino) -> list[Vendorizado]` (añade `licencia` y devuelve lo escrito para generar `VENDOR.md`).
4. La tipografía Inter es el subconjunto «latin» (incluye acentos y ñ). Las flechas y símbolos (→ ● ◀ ▶) usan la fuente del sistema.
5. El servicio escucha solo en `127.0.0.1`: el acceso desde el PC y el PIN llegan en la Fase 6, como se aprobó.
6. Nada de esto toca el panel actual: la ventana Cairo sigue funcionando como respaldo.

### Fase 1 · Colector e historial — hecha el 2026-10-23
> [!resumen] En cristiano
> El servidor ya apunta solo, cada 30 segundos, cuánta RAM, CPU, temperatura y disco usa, y cada 5 minutos cuántas webs ha leído el scraper en cada hora. Con eso las gráficas de las próximas fases tendrán historial real desde ya (las de 24 horas estarán completas mañana). Cuesta 19 MB de RAM.

- **T1.1** `colector.py`: `muestrear_sistema`, `purgar` (30 días) y `serie` (promedia en cubos, máximo 240 puntos; la métrica solo puede ser de una lista fija para evitar inyección SQL).
- **T1.2** `muestrear_scraper`: webs rastreadas y con correo por hora desde `leads.db` abierta **solo en lectura** (probado que el archivo no cambia). Con datos reales: 1.370 webs en 4 horas con actividad; el ciclo de la 01:40 (Fuengirola) aparece como 108 webs.
- **T1.3** `bucle` + `python -m battle_royale colector` + `panel-colector.service` (reinicio automático, prioridad baja). Un fallo puntual se apunta y el bucle sigue (probado). Se detiene limpio con SIGTERM.
- **Extra de esta fase**: `GET /api/serie?metrica=ram_pct&rango=3h|24h|7d` en la web (formato de uPlot), con validación (422 si la métrica o el rango no son válidos).
- **Medido en el servidor**: colector 19 MB y 0,1 % CPU; web 50 MB. Suite completa verde.

**Mis decisiones en esta fase (revísalas):**
1. En `scraper_hora`, `empresas` es el **acumulado de webs rastreadas** hasta esa hora (no el total de empresas en la base): es lo que se puede reconstruir sin guardar instantáneas.
2. Las horas se guardan en UTC y se mostrarán en hora local en la interfaz.
3. La primera muestra de red tras arrancar sale a 0 (no hay lectura previa) y la de CPU se descarta al arrancar.
4. Retención de 30 días de muestras (≈ 86.000 filas, unos 5 MB); `scraper_hora` se conserva siempre (pocas filas).

### Cambio de nombres — 2026-10-23
Los servicios del panel ya no llevan «battle-royale»: `panel-web.service`, `panel-colector.service` y `panel-ventana.service` (antes `battle-royale-web/colector/panel`). El torneo conserva `battle-royale-vivo.timer`. Actualizados: unidades de systemd, código, tests, README, `CLAUDE.md`, `GEMINI.md` y las notas del vault. El paquete Python sigue llamándose `battle_royale` porque contiene el torneo y el panel. `scripts/parche_*.py` son parches de un solo uso y conservan los nombres antiguos.

### Fase 2 · Avisos y semáforo — hecha el 2026-10-23
> [!resumen] En cristiano
> El servidor ya sabe decir solo si todo va bien: cada minuto revisa disco, RAM, temperatura, servicios caídos, el scraper y el vivo, y deja escrito cuándo empieza y termina cada aviso. Hoy marca «Todo bien». Si el guardián del historial se para, la propia consulta dice «DATOS VIEJOS» en vez de enseñar cifras antiguas como si fueran de ahora.

- **T2.1** `alertas.py`: 7 reglas (disco 85/95 %, RAM sostenida 5 min 90/97 %, temperatura 80/90 °C, servicio fallido, scraper sin ciclo >2 h / >6 h, Overpass 3/6 zonas seguidas, vivo >1,5 h / >3 h y errores del vivo) y `estado_global` con la frase en lenguaje sencillo («Todo bien», «1 aviso: …», «Atención: … (+N más)»). Pruebas en los dos lados de cada umbral.
- **T2.2** Frescura: `edad_datos` y `aviso_frescura` (>2 min sin muestras = crítico «DATOS VIEJOS»). Se calcula al consultar, no se guarda (foco de revisión 1, probado con el colector «parado»).
- **T2.3** Persistencia en `avisos` (abre, actualiza y cierra sin duplicar), `GET /api/avisos` (nivel, frase, activos y los 10 últimos cerrados) y el colector evalúa cada minuto.
- Datos nuevos para las reglas: `ciclo_ts` del scraper, `vivo_ultimo_ts` del vivo y caché de eventos ampliada a 40 (corrige que una llamada con otro `n` devolvía la caché del anterior).
- **Real**: contexto en 0,09 s; colector 21 MB, web 50 MB; **199 pruebas pasan**.

**Mis decisiones (revísalas):**
1. La regla de candidatas nuevas (informativa) se deja para la Fase 4: necesita los estados de candidatas.
2. Servicios caídos: se miran todos los `failed` que empiezan por battle-royale, panel, laya, trend, crypto, scalper o jev.
3. El colector evalúa cada 60 s; un error al evaluar se anota y no para el historial.
4. Sin notificaciones al móvil todavía (Fase 7).

### Fase 3 · Interfaz general — hecha el 2026-10-23
> [!resumen] En cristiano
> Ya existe la página «General» del panel, hecha como web: arriba el semáforo con su frase, y debajo el servidor (RAM, CPU, disco, temperatura, red y una gráfica de 3 h, 24 h o 7 días), el bot Battle Royale, el scraper con el mosaico de las 33 zonas, la hora estimada de fin y las webs leídas por hora, y la actividad reciente. Se actualiza sola cada 3 segundos. Todavía no se ve en el monitor del servidor (eso llega en la Fase 6), pero la puedes abrir desde tu PC con un túnel (ver abajo).

- **T3.1 Diseño base**: `panel.css` con la paleta del panel Cairo y fuente Inter local; barra con semáforo (icono + frase + edad de los datos), reloj, botones de **modo noche** (auto 00-07 h, noche, día) y **tamaño de letra** (normal/grande) guardados en el navegador; `?kiosko=1` agranda la letra y esconde las pestañas. Prueba automática de contraste: **todos los pares texto/fondo cumplen AA (≥ 4,5:1)**, 56 casos.
- **T3.2 Tarjetas**: servidor (anillo SVG, tiles, gráfica uPlot RAM+CPU con selector 3 h/24 h/7 d), bots y servicios, scraper (webs leídas, % accesibles, niveles A/B/C/D, segmentos, **mosaico de zonas** hecha/siguiente/pendiente con «+N», **hora estimada de fin**, gráfica de barras de webs por hora), actividad reciente. El estado de cada bot lleva texto además de color (probado).
- **T3.3 Tiempo real**: `GET /stream` (SSE) envía solo los fragmentos que cambian; aviso «Sin conexión con el servidor» si se corta; `GET /parciales/<nombre>`, `/api/serie_multiple`, `/api/scraper_hora`.
- **T3.4 Revisión visual**: comprobada en el navegador integrado a 1080×1920, 1440×900 y 375×812 (móvil), con datos reales. Encontré y arreglé: el `%` del anillo en tres líneas, el eje de la gráfica en 12 h (ahora 24 h) y el desborde horizontal en móvil (la barra de pestañas). Sin desborde en los tres tamaños.
- **Medido**: página en 0,1 s, fragmentos y APIs en ~2 ms; web 56 MB y colector 22 MB; **256 pruebas pasan**.

**Error real encontrado y corregido:** FastAPI abre la conexión de SQLite en un hilo y el endpoint la usa en otro, y fallaba a ratos con 500 (por eso algunas gráficas salían vacías). Solución: `panel_db.abrir(..., compartida=True)` en las peticiones, con prueba que reproduce el fallo (primero fallaba, luego pasa). Ya lo tenía anotado en mis notas de librerías y lo repetí: el cliente de pruebas no lo reproduce.

**Pendiente de tu vista (no puedo comprobarlo yo):** que el texto se lea a la distancia real del monitor vertical y cómo se ve la página dentro de la ventana WebKit (Fase 6).

**Cómo verla ahora desde tu PC** (túnel temporal; en la Fase 6 habrá acceso directo con PIN):
```bash
ssh -L 8090:127.0.0.1:8090 ssh@192.168.0.100
```
y abre `http://localhost:8090` mientras esa terminal siga abierta (añade `?kiosko=1` para el modo pantalla grande).

**Mis decisiones (revísalas):**
1. Las pestañas Candidatas, Torneos y Ajustes se ven pero desactivadas hasta sus fases.
2. Las gráficas no tienen globo al pasar el ratón; se añade si lo quieres.
3. El «auto» del modo noche usa la hora del navegador (00:00-07:00) y baja el brillo al 55 %.
4. **No pasé las skills `hallmark`/`dataviz`/`impeccable`** que el plan sugería (límite de contexto de la sesión): la revisión fue con capturas y comprobaciones automáticas. Propongo pasar `impeccable audit` en la Fase 8.

### Fase 4 · Candidatas como herramienta de trabajo — hecha el 2026-10-23
> [!resumen] En cristiano
> La pestaña **Candidatas** ya sirve para trabajar: ves las 363 candidatas A y B del scraper, buscas por nombre, sector o correo, filtras (con correo, nuevas, por estado…) y cambias el estado de cada una (nueva, por llamar, contactada, respondió, reunión, descartada) desde la propia lista, o de varias a la vez. Al pulsar una se abre su ficha con la oferta, los problemas de su web, copiar correo/teléfono/web con un clic, un QR para abrir la web en el móvil, un primer mensaje ya redactado (por reglas, sin IA) y una nota con historial. Lo que marques se guarda y no se pierde aunque el scraper regenere su lista. Puedes exportar lo que ves a CSV.

- **T4.1 Lógica** (`candidatas.py`): lectura del CSV sin duplicados ni filas sin nombre, clave por dominio, estados y notas en `panel.db`, «nueva» = vista por primera vez en las últimas 24 h, filtros combinados, orden, paginación (probada con 5.000 filas), cambio en bloque conservando notas, exportación CSV y borrador. Foco de revisión 2 probado: **si una candidata desaparece del CSV su seguimiento se conserva (cuenta como «fuera del CSV») y reaparece si vuelve**.
- **T4.2 Rutas**: `/candidatas`, `/candidatas/tabla` (htmx, buscador con retraso de 300 ms), `/candidatas/{dominio}` (ficha), `POST /candidatas/{dominio}/estado`, `POST /candidatas/bloque`, `/candidatas.csv` (respeta filtros, con BOM para Excel), `/qr?url=`.
- **T4.3 Vistas**: lista y tablero (columnas por estado, 20 por columna), vistas rápidas «Por llamar hoy», «Nuevas», «Nivel A con correo» y «Todas», interruptor «Mostrar descartadas» (ocultas por defecto).
- **T4.4 Ficha**: botones de copiar (con respaldo para páginas sin https), QR en SVG, borrador, nota e historial de cambios.
- **T4.5 Seguridad (foco 3)**: toda escritura exige venir del propio servidor **y** la cabecera de htmx (frena formularios de otras páginas); desde otra IP devuelve 403 aunque lea bien (probado). El PIN para escribir desde la red llega en la Fase 6.
- **Revisión real** en el navegador con las 363 candidatas: la ficha abre con QR y borrador, el cambio de estado desde la fila actualiza el contador al instante, sin desborde. Los cambios de prueba (una candidata) se deshicieron.
- **279 pruebas pasan**; página en 0,1 s.

**Mis decisiones (revísalas):**
1. «Por llamar hoy» es el estado `por llamar`, sin fecha de llamada (si quieres recordatorios por fecha, es una mejora aparte).
2. El tablero cambia el estado con un selector en la ficha; **no se arrastran tarjetas** (no vendoricé SortableJS: lo añado si lo quieres).
3. La primera vez que se abre la pestaña, las candidatas que ya existían cuentan como antiguas; solo las que entren después saldrán como «NUEVA» durante 24 h.
4. Los mensajes borrador están en el código (no en archivos `.txt`): 5 plantillas por tipo de oferta, escritas en tono cercano y sin prometer resultados. Revísalas: las firmo como Haytham de NeoZeler.
5. La regla de aviso «N candidatas nuevas» (informativa) **queda pendiente**; el contador «nuevas» ya sale en la propia pestaña.
6. Dependencias nuevas: `python-multipart` 0.0.32 y `segno` 1.6.6 (QR).

### Fase 5 · Torneos y bots — hecha el 2026-10-23
> [!resumen] En cristiano
> La pestaña **Torneos** enseña el combate en vivo: «día X de 30», el capital de cada luchador frente a la franja donde habría caído alguien que entra al azar, lo cerca que está cada moneda de disparar (por eso hay 0 operaciones: todavía ninguna cumple las reglas), el pasado (3 rondas) y la versión «al pie de la letra» con y sin comisión. Un botón repite los últimos 30 días para comprobar que las reglas sí operan: salieron 50, 4 y 19 operaciones, **las tres con pérdida**.

- **T5.1 Señales** (`senales.py`): `estado_senal` mide cuánto le falta al cierre para romper el máximo de 55 velas (donchian) y qué condiciones faltan en el squeeze (compresión, precio, volumen). `proximas_senales` ordena las 36 combinaciones de más cerca a más lejos. El ciclo horario del vivo las guarda en `progreso.senales`, así la web no necesita red.
- **T5.2 Capital y azar** (`torneos.py`): `equity` calcula la curva al pedirla desde `vivo_ops` (cerradas al cerrar; abiertas al final, repartido entre las 12 monedas como `vivo_resumen`). `banda_azar` simula entradas al azar con los mismos stops, objetivos y ritmo de operaciones del historial en los últimos 30 días (percentiles 5 y 95, 200 repeticiones; 1,2 s). El colector la refresca una vez al día en `ajustes`. API: `GET /api/equity`.
- **T5.3 Página** (`/torneos`): barra de días y veredicto, tabla de luchadores, distancia a la señal, tres curvas uPlot con la franja, pasado R1-R3 desplegable, literal con y sin comisión y botón «Repetir 30 días» (`vivo.repetir`, copia temporal; `POST` solo desde el propio servidor con la cabecera de htmx).
- **Revisión real**: probado con los datos del servidor a 1080×1920 y 375 px, sin desborde; el botón de repetir se ejecutó con datos reales de Binance y la base real no cambió (hay prueba).
- **300 pruebas pasan.**

**Mis decisiones (revísalas):**
1. **No uso la tabla `equity_vivo`**: la curva se recalcula de `vivo_ops` (que el ciclo reconstruye entera cada hora), así no hay dos fuentes que puedan discrepar. La tabla queda sin uso.
2. La franja del azar es **una por luchador** (no una sola) y se calcula con los últimos 30 días de velas, no con el futuro: es una referencia de «cuánto da la suerte», no una predicción. Sale por debajo de 1000 porque las comisiones se comen al azar.
3. Con 0 operaciones la gráfica dice «no hay nada que comparar con el azar» en vez de «por encima de la franja» (con 1000 parecía ganar al azar sin haber operado).
4. El texto de «qué decide el veredicto» («compara con el azar, ya con comisiones, tras 30 días») es mío: revísalo.
5. **Hallazgo:** en la repetición de 30 días las tres estrategias perdieron (−2,2 %, −0,4 %, −1,5 %). Coincide con el pasado: no superan al azar. No es una conclusión (un mes es poco), pero no aporta esperanza.
6. `POST /torneos/repetir` repite la regla de escritura local de Candidatas; la Fase 6 las unifica con el PIN.

### Fase 6 · Ventana WebKit y acceso desde el PC — hecha el 2026-10-23 (falta la medida de 24 h y tu vista)
> [!resumen] En cristiano
> El monitor del servidor ya muestra el panel web (la misma página «General», en modo kiosko, a pantalla completa) en vez de la ventana antigua; si el servidor web tarda en arrancar, la ventana reintenta sola. Desde tu PC abres `http://192.168.0.100:8090`: **mirar es libre, pero cambiar algo (estados de candidatas, repetir el vivo) pide un PIN** que fijas tú en el servidor. Probado: desde otro equipo se lee todo y escribir da «403» hasta tener PIN.

- **T6.1 Ventana** (`ventana.py`): WebKitGTK a pantalla completa con `http://127.0.0.1:8090/?kiosko=1`; F11, Esc, F5, Ctrl+Q; reintenta cada 5 s si la web no responde y recarga si el proceso de dibujo se cae; cursor oculto en pantalla completa. `panel --cairo` conserva la ventana antigua; `panel --captura-web RUTA.png` guarda una captura fuera de pantalla (verificada a 1080×1920).
- **T6.2 Red y PIN** (`seguridad.py`, `web/acceso.py`): `web --lan` escucha en toda la red; PIN de 4 a 12 cifras guardado como hash scrypt con sal; cookie firmada de 30 días (`HttpOnly`, `SameSite=Strict`); 5 fallos seguidos bloquean 5 minutos por IP; cambiar el PIN cierra todas las sesiones. **Una sola puerta de escritura** para Candidatas y Torneos (exige PIN o servidor local, y la cabecera de htmx). 9 pruebas nuevas; **309 pasan**.
- **T6.3 Servicios**: `panel-ventana.service` ahora abre la ventana web, con `After`/`Wants` de web y colector; `panel-web.service` usa `--lan`. Copias de las unidades anteriores junto a ellas (`*.bak`, `*.cairo.bak`).
- **RAM medida**: ventana WebKit ≈ **311 MB** (Cairo: 44 MB) con 5,5 GB libres. **Falta la medida a 24 h**: si crece, se añade un reinicio nocturno de la ventana.

**Lo que te toca a ti:** fijar el PIN en el servidor (pide teclearlo, no puedo hacerlo yo):
`ssh -t -i ~/.ssh/id_ed25519_zorin ssh@192.168.0.100 'cd ~/Proyectos/battle-royale && PYTHONPATH=src venv/bin/python -m battle_royale pin'`

**Mis decisiones (revísalas):**
1. `--lan` escucha en `0.0.0.0` (también en las redes internas de Docker), no solo en 192.168.0.100: no hay cortafuegos y es una red de casa. Si prefieres otra cosa, se cambia.
2. Leer es libre para cualquier equipo de la red, **incluidas las fichas de candidatas** (datos de contacto de empresas).
3. El monitor muestra solo «General» (sin pestañas). La ventana Cairo antigua rotaba tres páginas; si quieres que la web rote entre General, Candidatas y Torneos, es un añadido pequeño.
4. No pude fotografiar el monitor real (no hay herramienta de captura en GNOME/Wayland): la comprobación es la captura fuera de pantalla y que la página carga (el servidor registra sus peticiones). **Pendiente de tu vista**: legibilidad a distancia y que la ventana ocupa todo el monitor.
5. HTTP sin cifrar: en la red de casa el PIN viaja en claro. Vale para este uso; no lo expongas fuera de casa.

### Fase 8 · Pulido, documentación y entrega — hecha el 2026-10-23 (queda tu OK para retirar Cairo)
> [!resumen] En cristiano
> Ya hay pestaña **Ajustes**: eliges tema y tamaño de letra (por pantalla), cambias desde qué valores el semáforo pasa a ámbar o rojo (disco, RAM, temperatura) y ves si el PIN está fijado. Con esto el panel queda completo salvo los avisos al móvil (Fase 7, opcional) y tu revisión en el monitor. La ventana antigua (Cairo) **sigue ahí como respaldo**: solo se retira si tú lo dices.

- **T8.1 Ajustes**: umbrales de aviso editables (`alertas.cargar_umbrales`/`guardar_umbrales`, claves `umbral:*` en `ajustes`; se validan los seis a la vez y el aviso debe ir antes que lo crítico; «Restablecer» vuelve a los de siempre), apariencia por navegador, estado del PIN y datos del panel. Guardar exige la misma puerta que el resto (servidor local o PIN). Si el servidor rechaza una petición de htmx, ahora se dice por qué en vez de no hacer nada. Movimiento reducido respetado en el indicador de carga. 323 pruebas pasan; probado en el navegador a 1080×1920 (guardar, valor malo, restablecer; sin desborde).
- **T8.2 Documentación**: README del repositorio, ficha, nota de sesión, `CLAUDE.md` y `GEMINI.md` sincronizados, `graphify update .`.
- **T8.3 Retirar Cairo**: **no hecho, espera tu OK** (copias `panel-ventana.service.cairo.bak`; `panel --cairo` sigue funcionando).

**Honestidad sobre el pulido:** no pasé las skills `impeccable audit/polish` ni `accessible-animation` (consumen mucho contexto): la revisión fue por capturas, comprobación de desborde, contraste automático (ya en las pruebas) y movimiento reducido. Si quieres esa pasada, se puede hacer aparte.

**Decisiones mías:** (1) tema y tamaño siguen siendo por navegador, no globales; (2) el PIN no se cambia desde la web, solo en el servidor; (3) los umbrales no cubren scraper ni vivo (sus horas siguen fijas: 2/6 h y 1,5/3 h).
