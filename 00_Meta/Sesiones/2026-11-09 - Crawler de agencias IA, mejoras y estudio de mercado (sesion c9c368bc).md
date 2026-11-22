---
title: "Sesión - 2026-11-09 - Crawler de agencias IA: mejoras y estudio de mercado"
date: 2026-11-09
type: meta/sesion
origen: mixto
proyecto: "[[01_Projects/Crawler Agencias IA]]"
sesion_id: c9c368bc-eaeb-40da-af07-c2ed517c1e05
tags:
  - sesion
  - crawler
  - competencia
  - neozeler
aliases: []
---

# Sesión — 2026-11-09: Crawler de agencias IA, mejoras y estudio de mercado

> [!resumen] En cristiano
> Haytham pidió opinión sobre el robot que recorre webs de agencias de IA y cómo sacarle más datos. Se aplicaron 8 mejoras, se rastrearon las webs de nuevo y se amplió la lista de 45 a 60 agencias. Después una IA leyó el texto de cada web y rellenó una ficha por agencia. Salieron dos notas de estrategia: casi todo el mercado tiene competencia y solo hay pocos huecos claros. La sesión acabó con la ampliación de muestra aún en marcha.

## Contexto
Repo `~/Proyectos/crawler-agencias-ia/` (Go + SQLite), ficha en `[[01_Projects/Crawler Agencias IA]]`. Objetivo: saber «dónde me pongo yo» frente a la competencia de NeoZeler (`[[02_Areas/NeoZeler/Estrategia/Posicionamiento]]`).

## Qué se hizo
- **Diagnóstico:** 61 semillas daban 43 agencias, casi todo desde la portada (39 de 43 con 0 páginas escaneadas; contador `PagesScanned` mal hecho). Emails sucios (texto del menú pegado) y plantillas como `tu@empresa.com`.
- **Mejoras 1 a 8:** páginas clave primero (servicios, precios, casos, contacto, aviso legal) con tope de 15 por agencia (`-max-pages`); contactos desde `mailto:`, `tel:` y JSON-LD; respeto de `robots.txt` y lectura de `sitemap.xml`; reintentos en el fetcher; modo navegador (`-browser`). Probado con 14 agencias en una base aparte.
- **Rastreo completo** de 45 semillas (copia previa `data/agencias.antes-2026-11-09.db`): 5 a 14 páginas por agencia, `seed_failures` vacía. Cifras parciales: emails 89 %, teléfono 71 %, precios públicos 40 %.
- **Chromium** bajado con Playwright (101 MB) a la carpeta de usuario, enlazado en `~/.local/bin/chromium`, sin sudo. Solo `erbi.es` ganó datos.
- **Descubrimiento:** el crawler apunta dominios externos (socios, clientes) en `discovered_domains`; el comando `discover` revisó 156 de 231 y aceptó 15 agencias nuevas → 60 agencias y `data/agencias_competencia.csv`.
- **Estudio de mercado:** se guardó el texto de las páginas (750 páginas, 59 dominios, ~6,8 MB), `scripts/estudio.py run` generó con `claude -p` las fichas de 57 agencias sin fallos, más señales de tracción y `data/estudio_mercado.csv`.
- **Notas en el vault:** `[[02_Areas/NeoZeler/Estrategia/Huecos de mercado - IA para pymes]]` y `[[02_Areas/NeoZeler/Estrategia/Enfoque web de la competencia]]`.

## Resultados clave
- 59 agencias con texto: 44 competidores directos (42 agencias pequeñas y 2 freelancers).
- Solo 9 de 59 webs publican algún precio.
- Huecos reales pocos: voz para inmobiliario y servicios profesionales con voz, formación y base de conocimiento; el resto tiene competencia.
- Tracción: solo 11 agencias con edad del dominio y 26 con fecha del último blog.

## Decisiones tomadas
- Se descartó saltarse los antibots de buscadores con Scrapling (el sistema lo bloqueó por ser evasión de detección) y se retiró esa sugerencia. Bing por HTTP devuelve basura; DuckDuckGo y Mojeek bloquean; Clutch y GoodFirms dan 403.
- Se montó el descubrimiento por enlaces cruzados en vez de buscadores.

## Problemas
- El CLI `claude` perdió la sesión (OAuth caducado) y bloqueó las fichas; Haytham hizo `claude /login` y se resolvió.
- `sherpa.ai` cierra la conexión sin responder.
- «Cruces casi vacíos» listaba también cruces con 0 competidores: corregido en el script, pero las notas actuales siguen con el fallo hasta regenerarlas.

## Pendientes / próximos pasos
- Terminar `scripts/ampliar.sh` (3 rondas de descubrir y rastrear; copia previa `data/agencias.antes-ampliar-2026-11-09.db`), rellenar fichas nuevas, regenerar informe y notas.
- Documentar: README del repo, ficha actualizada y `resumen.html` (regla §0.8 del vault).
- Quedan 75 dominios por revisar con `discover -limit` más alto; apuntar a 150-300 agencias separadas por tipo.

## Relacionado
- [[01_Projects/Crawler Agencias IA]] · [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
