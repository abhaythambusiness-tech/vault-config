---
title: "Sesión - 2026-11-09 - Grid64: construcción Fase 0 a 3"
date: 2026-11-09
type: meta/sesion
origen: mixto
proyecto: "[[01_Projects/Grid64]]"
sesion_id:
  - 149a609a-7805-429e-8d23-92f07288fd20
  - e3599d39-d3b4-4cbe-b419-54d1beeac036
  - c9ff0173-f368-4bb5-906f-b9c17d7356cc
tags:
  - sesion
  - grid64
  - go
  - android
aliases: []
---

# Sesión — 2026-11-09: Grid64, construcción de la Fase 0 a la 3

> [!resumen] En cristiano
> Tras aprobar los documentos de Grid64 (app móvil de mandalas 9×9), se montó el entorno de Android, se probó en el Samsung de Haytham que la base de datos guarda los datos y se construyeron la lógica y la interfaz de las tres pestañas. Funciona en el navegador a 375 px; aún no se ha probado la interfaz en el móvil.

## Contexto
Continuación de `[[00_Meta/Sesiones/2026-11-08 - Grid64 arranque]]` (PRD, TRD, Ficha, UI-UX y Plan aprobados, sin código). Repo `~/Proyectos/grid64/`. Las otras dos sesiones (e3599d39 y c9ff0173) son ramas anteriores con el mismo arranque; la completa es 149a609a (continuada tras compactar contexto).

## Qué se hizo
- **Documentos:** PRD y TRD aprobados (cuatro puertas abiertas del PRD asumidas por defecto: acciones de hoy a mano, racha con ≥1 acción/día, días restantes por `target_date`, nombre «Grid64» en español); Ficha de Investigación (versiones comprobadas en `proxy.golang.org` y `npm view`), identidad «tablero de Go» (piedras jade sobre obsidiana, icono `assets/icon.svg`) y Plan aprobados; sin referencias de Dribbble por decisión de Haytham.
- **Fase 0:** JDK Temurin 17, Android SDK (plataforma 34, build-tools 34.0.0), NDK 27.3.13750724 y gomobile en la carpeta personal, sin sudo (SDK 2,5 GB, JDK 319 MB). **Spike T-01:** servidor Go + SQLite (`modernc.org/sqlite` v1.62.0) en una WebView Kotlin; APK debug de 15 MB. En el Galaxy S23 (SM-S911B) el contador de arranques persistió 1→2→3 (comprobado copiando `files/grid64.db`, sin leer la pantalla).
- **Fase 1 (T-02 a T-04):** esquema de 5 tablas con migraciones por `PRAGMA user_version`; crear un mandala crea en una transacción 1 proyecto, 1 meta, 8 pilares y 64 acciones.
- **Fase 2 (commit `2d46f33`):** máximo 5 acciones de hoy (`ErrDailyLimit`), racha por zona horaria del móvil, conversión de ideas a meta/pilar/acción en transacción, copia y restauración.
- **Fase 3 (commit `c79f257`):** interfaz de tres pestañas (Inicio, Mis mandalas con panorama 9×9 y enfoque 3×3, Ideas), exportación a PNG y PDF, ajustes con copia de seguridad; Alpine y fuentes OFL descargadas.
- **Comprobado:** `go test` (19 tests), axe sin violaciones en las tres pestañas y ambos modos del mandala, sin scroll horizontal a 320/375/768/1280 px; tres capturas en `.capturas/`.

## Decisiones tomadas
- Go + WebView nativa fina (Wails no soporta Android), vía micro-saas, proyecto personal de Haytham.
- Tamaño Proyecto, modo Operate, fase 0b de diseño saltada por decisión de Haytham.

## Aprendizajes
- Aceptar las licencias del SDK de Android se hizo sin petición expresa: conviene avisar antes.
- `adb` devolvió `unauthorized` hasta reiniciar su servidor.
- Un fallo de carga (el pilar se leía antes del mandala) se corrigió con el servidor de escritorio y un mandala de ejemplo.

## Problemas y pendientes
- La interfaz de la Fase 3 y la API no se han probado en el móvil; el PNG y el PDF exportados no se abrieron como archivos descargados.
- Pendientes de la Fase 0: `resumen.html` del repo (regla §0.8 del vault) y confirmar peso y licencia de las librerías de Go.
- Siguiente: las fases que quedan del Plan (12 tareas en 6 fases).

## Relacionado
- [[01_Projects/Grid64]] · [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
