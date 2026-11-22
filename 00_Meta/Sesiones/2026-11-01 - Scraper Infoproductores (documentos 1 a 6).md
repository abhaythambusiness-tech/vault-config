---
title: "Sesión - 2026-11-01 - Scraper Infoproductores (documentos 1 a 6)"
date: 2026-11-01
type: meta/sesion
proyecto: "[[Scraper Infoproductores]]"
tags:
  - sesion
aliases: []
origen: mixto
---

# Sesión — 2026-11-01: Scraper Infoproductores

> [!resumen] En cristiano
> Se definió y aprobó entero el diseño de un SaaS donde se buscan infoproductores gastando créditos. No hay código todavía: antes hace falta validar que alguien pague.

## Qué se hizo
PRD, Ficha de Investigación, TRD, UI-UX con identidad «libro mayor», Paleta de Componentes, AppFlow, Backend Schema (probado en PGlite, 21/21) y Plan (21 tareas). Repo `~/Proyectos/scraper-infoproductores/` con git y `.proyecto`.

## Aprendizajes
- Clasificar con reglas de código y no con Laya: Laya Leads ya descartó la IA por no servir; Laya queda para una v2.
- Los créditos van en un libro de movimientos con claves de idempotencia y candado por usuario; así reintentos y doble clic no cobran dos veces.
- Estimar facturación solo con precio y alumnos públicos; sin datos queda vacío, no inventado.
- `shadcn-registries` MCP devuelve vacío sin `components.json`: buscar con la CLI (`npx shadcn@latest search @ns`). `@aceternity` falla por certificado.
- `trace_lint.py` exige que toda US aparezca en UI-UX y AppFlow, incluso las fuera de v1.

## Decisiones abiertas
Paso 0 (entrevistas y preventa), fuentes de v1, precios y créditos, hosting Vercel, revisión legal RGPD.
