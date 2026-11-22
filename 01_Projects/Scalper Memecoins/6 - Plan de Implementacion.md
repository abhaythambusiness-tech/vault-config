---
type: doc-software
doc: plan-implementacion
proyecto: 01_Projects/Scalper Memecoins
status: aprobado
date: '2026-10-21'
origen: mixto
---


# 6 · Plan de Implementación

> [!resumen]
> Orden de construcción en tareas pequeñas y verificables, derivado de [[1 - PRD]], [[2 - TRD]], [[3 - UI-UX Design]], [[4 - AppFlow]] y [[5 - Backend Schema]]. Código real en `~/Proyectos/scalper-memecoins/` **del servidor Zorin** (`ssh@192.168.0.100`), git desde el primer commit. **Punto de decisión tras T-02**: si Laya no cabe en RAM o tarda demasiado en este equipo, se para y se replantea antes de construir nada más.

## 1. Fases
| Fase | Objetivo | Entregable demostrable | Historias |
|---|---|---|---|
| 0 Scaffold y sandbox | Repo, entorno y medir Laya en este servidor | Informe de Laya con RAM, latencia y formato de respuesta | US-05 |
| 1 Datos | Migración y semilla ([[5 - Backend Schema]]) y datos de calibración | BD creada, tests de cascada en verde | US-04, US-05 |
| 2 Núcleo | Ingesta, precios, antifraude, broker, riesgo, Laya y motor de 3 carteras | Bot operando en papel de forma continua con auditoría | US-02, US-04, US-05, US-06 |
| 3 UI | API, SSE y las cinco pantallas ([[3 - UI-UX Design]]) | Panel navegable con datos reales | US-01, US-02, US-03, US-06, US-07, US-08 |
| 4 Pulido | Estados, accesibilidad, 375 px, ciclo completo | Checklist técnico y de marca | US-01, US-06 |
| 5 Despliegue | Servicios `systemd`, 24 h seguidas y arranque del experimento | Panel en la LAN y Gate 1 contando | US-05, US-07 |

## 2. Tareas
**Fase 0**
- [ ] T-01 · (US-05) Crear el repo en el servidor: `git init` + `.gitignore` (`.env`, `venv/`, `__pycache__/`, `dist/`, `build/`, `*.db`), `venv` con Python 3.12, `requirements.txt` con versiones exactas, `.env.example` sin valores, `ruff`/`mypy`/`pytest`, estructura `src/ tests/ sandbox/ scripts/ static/`. Hecho cuando: `pytest` y `ruff` corren vacíos sin error. Depende de: —
- [ ] T-02 · (US-05) **Sandbox de Laya** en `sandbox/`: instalar torch CPU y `laya==0.4.12`, descargar un único checkpoint (`laya-typed-decisions`), medir RAM en reposo, latencia p50/p95 por pregunta `noul` y `choice`, formato real de `Router.predict`, y leer el código de `laya.calibrate` (el README no la documenta). Hecho cuando: informe con cifras y veredicto "cabe / no cabe" frente al tope de 3,8 GB y 2 s por decisión. Depende de: T-01

**Fase 1**
- [ ] T-03 · (US-05) Módulo `db`: migración y semilla generadas con `schema_to_migration.py`, conexión con WAL, `foreign_keys=ON` y `busy_timeout`; portar el script de validación (cascadas, checks, ejemplo numérico) a `tests/test_schema.py`. Hecho cuando: tests en verde y 0 avisos de FK. Depende de: T-01
- [ ] T-04 · (US-04) Conjunto de calibración antifraude: **con tu permiso**, copiar al servidor las bases del observador de Memecoin-LSTM (1,1 GB, solo datos desde 2026-10-05 00:00 UTC) y construir un conjunto etiquetado (estafa/no estafa por vaciado de liquidez) para calibrar a Laya. Hecho cuando: CSV con etiquetas y partición temporal entrenamiento/prueba. Depende de: T-02

**Fase 2**
- [ ] T-05 · (US-05) `price_service`: Jupiter Price v3 por lotes y DexScreener de uno en uno como respaldo; ausencia = "sin dato", no 0; antigüedad del precio por moneda. Tests con fixtures grabadas, sin red. Depende de: T-03
- [ ] T-06 · (US-05) `ingestor`: señales de monedas nuevas y alertas (omitir `replay:true`); necesita `FOMOAPI_KEY` gratuita (tuya, solo en `.env`). Hecho cuando: señales entran a `senales` y `tokens` sin duplicar. Depende de: T-03
- [ ] T-07 · (US-04) `safety`: RugCheck v2/v3 + filtro de Laya "¿estafa?"; si RugCheck no responde, la moneda se salta y se registra en `descartes` (nunca se simula aprobada). Depende de: T-04, T-06
- [ ] T-08 · (US-05) `paper_broker`: comisión, deslizamiento, FIFO y estados según [[5 - Backend Schema]] §6. Hecho cuando: el ejemplo numérico (+5,15 %) sale exacto en un test. Depende de: T-03
- [ ] T-09 · (US-06) `risk`: tamaño, máx. posiciones, exposición, corte diario −20 %, rangos duros de `config`; reanudar exige confirmación y no reinicia el contador. Hecho cuando: tests prueban que el corte detiene las entradas de verdad. Depende de: T-03
- [ ] T-10 · (US-02, US-04) `laya_worker`: preguntas tipadas `estafa`/`entrada`/`salida`, texto compacto del estado, resumen de una frase, niveles alta/media/baja calibrados, descarte por `laya_max_ms` con motivo `laya_lenta`. Depende de: T-02, T-04
- [ ] T-11 · (US-02, US-05) `engine`: las tres carteras (Laya, Reglas, Azar) con las mismas señales, salidas por stop/trailing/tiempo/liquidez muerta/Laya, `equity` por minuto, `eventos` y `descartes`. Hecho cuando: una repetición grabada de señales reproduce las mismas decisiones. Depende de: T-05, T-07, T-08, T-09, T-10
- [ ] T-12 · (US-05) Retención diaria y copia diaria de la BD; servicio `systemd` del bot con `MemoryMax=3800M` y reinicio automático. Depende de: T-11

**Fase 3**
- [ ] T-13 · (US-01, US-03) API FastAPI: `/api/snapshot`, `/api/stream` (SSE con `Last-Event-ID`), `/api/health`, `/api/glossary`, autenticación por token con cookie. Depende de: T-03, T-11
- [ ] T-14 · (US-01, US-03) Pantalla **En vivo**: tokens CSS, `StatTile`, `EquityChart` (lightweight-charts), `PositionTable`, `DecisionFeed`, `LegendCard`, `FunnelBar`, `HealthCard`. Primero con una maqueta de datos sintéticos para validar el diseño contigo, después con datos reales. Depende de: T-13
- [ ] T-15 · (US-02) Pantallas **Decisiones** (lista + detalle) y **Glosario** con tooltips. Depende de: T-13
- [ ] T-16 · (US-03, US-08) Pantalla **Operaciones** con tabla y exportación CSV. Depende de: T-13
- [ ] T-17 · (US-06) Pantallas **Control** y **Acceso**: límites con rangos, pausar, reanudar con motivo, cerrar todo escribiendo CERRAR. Depende de: T-09, T-13
- [ ] T-18 · (US-07) `scripts/gate1.py` (bootstrap IC90, mitades, sin top 3, diferencia con Azar) y pantalla **Gate 1**. Depende de: T-11, T-13

**Fase 4**
- [ ] T-19 · (US-01, US-02) Estados vacío/carga/error de todas las pantallas con sus ilustraciones, `prefers-reduced-motion`, 375 px sin desbordes y contraste en navegador. Depende de: T-14, T-15, T-16, T-17, T-18
- [ ] T-20 · (US-06) Ciclo completo en el servidor: abrir panel → pausar → refrescar → reanudar; reiniciar el bot y comprobar que equidad y posiciones se conservan; cortar el feed y ver que se recupera sin duplicar eventos. Depende de: T-12, T-19

**Fase 5**
- [ ] T-21 · (US-05, US-07) Arrancar el experimento en papel, vigilar 24 h seguidas (RAM, swap, cola, latencia de Laya) y dejarlo corriendo hasta el veredicto del Gate 1. Depende de: T-20
- [ ] T-22 · (US-05) Documentación de cierre del arranque (CLAUDE.md §0.8): README del repo, ficha `01_Projects/Scalper Memecoins.md`, sesión en `00_Meta/Sesiones/`, `COMMON_MISTAKES.md` y `librerias.md`. Depende de: T-21

## 2.1 Starter kits reutilizados
En [[Starter Kits NeoZeler]] **ningún kit está extraído todavía**. Código de referencia ya existente en `~/Proyectos/crypto-copy-bot/src/` (rama `copybot-v2`, en tu PC, no en el servidor); se **revisa antes de copiar** y se adapta al esquema SQLite, sin dependencias nuevas:
| Origen | Fase | Adaptación |
|---|---|---|
| `price_provider.py` (Jupiter + DexScreener) | 2 | Revisar y adaptar a `precios`; mantener la regla "ausencia ≠ 0" |
| `rugcheck.py` | 2 | Adaptar al flujo de `safety` y a los motivos de `descartes` |
| `paper_wallet.py` (FIFO) y `risk.py` | 2 | Cambiar los parámetros por los de `config`; añadir el corte diario con confirmación |
| `state_store.py` (snapshot atómico) | 2 | Sustituir por SQLite (el snapshot pasa a la BD) |
| `dashboard.py` (ámbar sobre carbón) | 3 | Solo referencia visual: se reescribe con SSE y los tokens del UI/UX |
| Kit candidato "Dashboard base" | 3 | Si se extrae más tarde, este panel sería su segundo uso |

## 3. Estrategia de pruebas
- **Unitarias** (`pytest`, sin red): broker (ejemplo numérico), riesgo (corte diario), esquema (cascadas), `gate1` (con datos sintéticos de resultado conocido), parser del feed (con fixtures reales).
- **Reproducción**: motor alimentado con señales grabadas debe dar decisiones idénticas.
- **Integración**: SSE con reconexión y `Last-Event-ID`; API con y sin token.
- **Ciclo completo** (T-20) **en el servidor real**: crear → refrescar → pausar → reiniciar → refrescar → borrar (reinicio de cartera) → refrescar.
- **Visual**: navegador integrado de Claude a escritorio y 375 px (Chrome DevTools no disponible).
- Línea base de Laya: se compara siempre con `azar` y `reglas`; sin eso no hay resultado.

## 4. Despliegue y operación
- Servicios `systemd` de usuario: `scalper-bot.service` y `scalper-api.service`, con `MemoryMax`, reinicio automático y `journalctl`. Linger activado para que sobrevivan al cierre de sesión.
- Variables en `.env` (`chmod 600`): `SCALPER_TOKEN`, `FOMOAPI_KEY`, `HELIUS_RPC_URL`, `LAYA_*`. Nada de claves de wallet.
- Panel en `http://192.168.0.100:<puerto>` solo en la LAN; comprobar `ufw`.
- Backups: copia diaria de la BD en otro directorio del servidor (misma máquina = no es copia externa; decidir si se baja a tu PC).
- Monitorización: `HealthCard` del panel (RAM, swap, cola, latencia de Laya, antigüedad del precio).

## 5. Riesgos y plan B
> [!riesgo]
> - **Laya no cabe o es lenta en CPU** → T-02 lo mide primero. Plan B: `laya` multilingüe más pequeño (322 M parámetros), o la cartera Laya solo decide "estafa/no" y la entrada la toman las reglas.
> - **Laya no aporta sobre texto numérico** → la cartera `azar` lo evidencia; el Gate lo cierra. No se reentrena Laya en v1.
> - **Paquete de 2 días** → versión y revisión del checkpoint fijadas; leer el código antes de ejecutarlo.
> - **Memoria** (7,6 GiB, swap ya usada antes) → `MemoryMax`, un solo checkpoint, contenedores de Supabase parados.
> - **Costes supuestos** → hasta tener cotizaciones reales, el Gate es indicativo; sustituir `deslizamiento_k` por medidas.
> - **Falta de datos de calibración** → T-04 depende de copiar las bases del PC; sin ellas, la parte "estafa" de Laya se mide solo con RugCheck.
> - **FomoAPI gratis (1000 peticiones/mes)** → priorizar el feed por WebSocket y no gastar peticiones REST.

## 6. Definición de terminado
- [ ] `trace_lint.py` en `RESULTADO: OK` y `schema_to_migration.py` sin avisos de FK
- [ ] Build y type-check limpios (`ruff` y `mypy` sin errores, `pytest` en verde)
- [ ] Checklist técnico y de marca ([[3 - UI-UX Design]] §8) verificado en el navegador a escritorio y 375 px
- [ ] README en el repo
- [ ] Ficha en `01_Projects/` y sesión registrada
- [ ] `.claude/COMMON_MISTAKES.md` actualizado
- [ ] Ciclo completo validado en el servidor (T-20)
- [ ] Criterio de cierre del Gate 1 escrito y sin cambios desde el PRD

---
Anterior: [[5 - Backend Schema]]

