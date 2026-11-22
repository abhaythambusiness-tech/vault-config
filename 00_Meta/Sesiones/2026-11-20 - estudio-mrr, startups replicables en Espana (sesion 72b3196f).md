---
title: 'estudio-mrr: startups replicables en España'
date: '2026-11-20'
type: meta/sesion
origen: maquina
proyecto: ''
sesion_id: 72b3196f-4cef-46f1-8bfb-66c4a77662aa
tags:
- sesion
- investigacion
- go
- startups
---

> [!resumen] En cristiano
> Se hizo un programa que descarga datos de startups reales (ingresos mensuales, crecimiento) de TrustMRR y Facto, para buscar ideas fáciles de copiar en España.
> Se filtraron 118 startups jóvenes con mucho crecimiento y categoría sencilla. El programa quedó guardado en git, sin subir a ningún sitio.

## Qué se hizo
- `~/Proyectos/estudio-mrr/` (Go): TrustMRR (API paginada con clave; endpoint público limitado a 50) y Facto (sitemap, ~161 fichas). `arr.club` caído, omitido. Reintentos ante 429.
- Primera tanda: 461 startups (300 + 161). Descarga completa (13.313 startups, ~2 h 15 min por el límite de 10 peticiones/minuto) **cancelada**; queda lo bajado y se puede reanudar con `-todo`.
- Filtro «jóvenes» (`salida-jovenes/`): ~1 mes de vida, ≥500 de ingresos y ≥100 % de crecimiento en 30 días, sin cripto, hardware, fintech, legal, salud, juegos ni inmobiliaria: **118**. Un valor atípico (6,4 M) se descartó.
- Commit `72619b9` con identidad local `abhaythambusiness-tech`; sin remoto, sin push; datos y binario fuera del commit.

## Decisiones
- La clave de la API vive solo en variable de entorno; no está en el repo.

## Riesgos
- La clave se pegó en el chat y Haytham decidió no rotarla: sigue expuesta en el historial.

## Pendientes
- Elegir qué startups de la lista de 118 replicar en España (criterio: simples o problema muy gordo).
- Sin ficha en `01_Projects/` (regla §0.8).

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

