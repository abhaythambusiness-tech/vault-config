---
type: doc-software
doc: plan-implementacion
proyecto: "Grid64"
status: aprobado
date: 2026-11-08
origen: mixto
---

# 6 · Plan de Implementación — Grid64

> [!resumen] En cristiano
> Orden de trabajo: primero comprobar que Go + SQLite funcionan en Android (prueba pequeña), luego el cerebro en Go con tests, luego la pantalla, y al final el APK. No se escribe código hasta aprobar PRD, TRD, identidad visual y este plan.

## 1. Fases
| Fase | Objetivo | Entregable demostrable | Historias |
|---|---|---|---|
| 0 Spike | Instalar SDK/NDK/gomobile; AAR mínimo con SQLite que abre una WebView | APK «hola» que guarda y lee una fila tras reinicio | — |
| 1 Datos | Esquema y servicios Go con tests | `go test` verde, 1+8+64 en transacción, cascada | US-01, US-02, US-05, US-09 |
| 2 Núcleo | API local + conversión idea→destino + prioridades de hoy + racha | ciclo completo por `curl` en escritorio | US-06, US-09, US-11, US-14 |
| 3 UI | Identidad y 3 pestañas, enfoque 3×3, panorama, hoja inferior | demo en navegador móvil + `DESIGN-IDENTITY.md` | US-03, US-04, US-07, US-08, US-10, US-12 |
| 4 Android | Empaquetado, gestos, háptico, copia de seguridad | APK instalado en el móvil | US-13, US-14 |
| 5 Pulido | a11y, rendimiento, estados vacíos | checklist técnico y de marca | todas |

## 2. Tareas
- [x] T-01 (probado en Galaxy S23 el 2026-11-08: contador SQLite persiste tras force-stop) · (US-01) Spike Android: instalar JDK 17, SDK, NDK, `gomobile init`; AAR con `modernc.org/sqlite`; Activity con WebView · `build/android/`, `cmd/app` · criterio: persiste tras kill y reinicio · depende de: nada. **Si falla, decidir plan B del TRD §8 con Haytham.**
- [x] T-02 (hecho 2026-11-08, `go test` verde) · (US-01, US-02) `pkg/database` y migraciones del esquema (TRD §2.1) con `ON DELETE` en toda FK · criterio: tests de cascada · depende de T-01.
- [x] T-03 (hecho 2026-11-08, `go test` verde) · (US-01, US-02) `pkg/models` y creación transaccional 1+8+64 · criterio: UNIQUE(idx) respetado · depende de T-02.
- [x] T-04 (hecho 2026-11-08, `go test` verde) · (US-05) Cálculo de progreso de pilar y mandala · criterio: test con casos 0/50/100 % · depende de T-03.
- [x] T-05 (hecho 2026-11-08, tests verdes) · (US-06, US-07) Acciones de hoy (máx. 5 por `daily_date`) · criterio: la sexta se rechaza · depende de T-03.
- [x] T-06 (hecho 2026-11-08, tests verdes) · (US-11) Racha por `completed_at` · criterio: tests con huecos de días · depende de T-04.
- [x] T-07 (hecho 2026-11-08, tests verdes) · (US-08, US-09) Ideas y `services/convert.go` a meta/pilar/acción · criterio: idea queda `linked` y se conserva el vínculo · depende de T-03.
- [x] T-08 (hecho 2026-11-08, tests verdes) · (US-14) Exportar/importar `.db` · criterio: restaurar en limpio recupera todo · depende de T-02.
- [x] T-09 (hecho 2026-11-08, tests verdes) · (US-12) API HTTP local con token y `127.0.0.1` · criterio: petición sin token da 401 · depende de T-04..T-07.
- [x] T-10 (hecho 2026-11-08: 3 pestañas, panorama, enfoque con swipe, hojas, ideas; axe 0 violaciones en las 3 pestañas; falta probar en el móvil) · (US-03, US-04, US-07, US-08, US-10, US-12) Frontend de las 3 pestañas · tras identidad aprobada y paleta · criterio: navegable en 375 px · depende de T-09.
- [x] T-11 (hecho 2026-11-08: PNG y PDF generados en cliente, PDF validado) · (US-13) Exportador PNG/PDF del mandala · depende de T-10.
- [ ] T-12 · (todas) Empaquetado APK firmado y prueba en el móvil real · depende de T-10.

## 2.1 Starter kits reutilizados
| Kit | Fase | Adaptación |
|---|---|---|
| [[Mini CRM Go]] (Go + SQLite + HTMX) | 1-2 | Reutilizar estructura de servicios y migraciones; revisar antes de copiar |

## 3. Estrategia de pruebas
- Unitarias Go para reglas (progreso, límite de 5, conversión, racha). Cascada de borrado probada.
- Ciclo crear → refrescar → borrar → refrescar en el móvil real.
- 375/768/1280 px en navegador durante la fase 3; axe a cero.

## 4. Despliegue y operación
- APK firmado con keystore local fuera del repo. Sin servidor ni dominio. Backups = exportar `.db`.

## 5. Riesgos y plan B
> [!riesgo]
> - Spike T-01 falla con modernc: `mattn/go-sqlite3` + NDK o SQLite de Android vía puente JS.
> - Toolchain Android pesado: instalar solo lo mínimo (cmdline-tools, platform, NDK).

## 6. Definición de terminado
- [ ] `trace_lint.py` en `RESULTADO: OK`
- [ ] Build y tests limpios
- [ ] Checklist técnico y de marca
- [ ] Pruebas de intercambio y de lejos; cero imágenes inventadas; fila en [[Registro de Identidades Visuales]]
- [ ] README en el repo y `resumen.html`
- [ ] Ficha en `01_Projects/` y sesión registrada
- [ ] `.claude/COMMON_MISTAKES.md` actualizado

---
Anterior: [[5 - Backend Schema]]
