---
title: "Sesión - 2026-11-02 - TopLeads (documentos 1 a 6)"
date: 2026-11-02
type: meta/sesion
proyecto: "[[TopLeads]]"
tags:
  - sesion
aliases: []
origen: mixto
---

# Sesión — 2026-11-01/02: TopLeads

> [!resumen] En cristiano
> Se convirtió el rastreador de negocios de Laya Leads en el diseño de un servicio de pago llamado TopLeads, con dos barras de créditos. Quedó todo aprobado menos lo que depende de ti: validar que alguien pague, el abogado y medir el coste de rastrear. No hay código de la web todavía.

## Qué se hizo
PRD, Ficha de Investigación, TRD, UI-UX con identidad «Radar de barrio», Paleta de Componentes, AppFlow (no aplica), Backend Schema (58 comprobaciones en PGlite) y Plan (33 tareas, lint de trazabilidad OK). Repo `~/Proyectos/topleads/` con git, `.proyecto`, migraciones, semilla y pruebas. Nada se cambió en el servidor Zorin ni en Supabase remoto.

**Construcción (misma sesión)**: T-01 a T-04 y T-06 hechas y comprometidas (4 commits, sin remoto): base `starter-saas` lite, tokens y fuentes propias, registries y componentes `dotted-map` y `ripple`, tipos de la base. **T-05 (Supabase staging) abierta**: `.env.local` existe en `~/Proyectos/topleads/` (600) pero con las claves sin rellenar (`supabaseUrl is required`); falta rellenarlas, aplicar migraciones y semilla en el panel y correr la verificación. T-07, T-09 y T-12 dependen de ello.

## Aprendizajes
- Un deny del entorno impide leer `.env*`: comprobar su contenido solo por el efecto (el script de verificación), nunca con `cat`/`awk`.
- Tailwind 4 necesita `@tailwindcss/postcss` + `postcss.config.mjs`; `--signal-600` da 3,97:1 sobre papel, el texto de marca usa `--signal-700` (6,02:1).
- Dos barras de crédito con ventana común: saldo atómico por usuario con candado (`for update`) y recarga perezosa al consultar o gastar; el diario solo añade y siempre cuadra con el saldo, por lo que el ciclo se prueba comparando ambos.
- Contacto protegido en tabla aparte con RLS por desbloqueo; los leads básicos se leen solo tras pagar la búsqueda de esa zona y sector.
- Reembolso al fallar el rastreo con la misma clave del gasto, acotado al tope del plan para no regalar créditos tras una recarga.
- `shadcn-registries` MCP no ve registries sin `components.json`: buscar con la CLI desde una carpeta temporal. `@aceternity` y `@spaceui` fallan por certificado (no se desactivó la verificación).
- `trace_lint.py` exige que AppFlow cite todas las historias aunque sea `no-aplica`: se dejó una tabla historia → pantalla → función.
- PGlite es una sola conexión: la concurrencia real se prueba en staging.

## Decisiones abiertas
Paso 0 saltado (kill a 60-90 días sin 5 clientes), revisión legal por entregar correos, coste de rastreo, cantidades de créditos y precios, nombre del plan superior, PRD §11 (carácter de marca), hosting Vercel, proyecto Supabase de staging.
