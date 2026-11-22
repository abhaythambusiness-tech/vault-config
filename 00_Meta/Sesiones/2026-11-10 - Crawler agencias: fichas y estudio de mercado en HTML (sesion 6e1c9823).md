---
title: "Sesión - 2026-11-10 - Crawler de agencias: fichas, estudio de mercado y HTML"
date: 2026-11-10
type: meta/sesion
origen: mixto
proyecto: "[[01_Projects/Crawler Agencias IA]]"
sesion_id: 6e1c9823-8868-417b-8f38-cf66906b6f6a
tags:
  - sesion
  - crawler
  - competencia
  - neozeler
aliases: []
---

# Sesión — 2026-11-10: fichas de agencias, estudio de mercado y HTML

> [!resumen] En cristiano
> Terminada la ampliación del rastreo, se rellenaron las fichas de las agencias nuevas (115 fichas en total, 49 rivales reales). Con ellas se escribió un estudio de mercado en el vault y una página HTML para leerlo. Conclusión: el mercado está lleno de generalistas, casi nadie publica precios y hay poca confianza; hay huecos en voz y bases de conocimiento. Los precios citados no están verificados a mano.

## Contexto
Continúa `[[00_Meta/Sesiones/2026-11-09 - Crawler de agencias IA, mejoras y estudio de mercado (sesion c9c368bc)]]`. Repo `~/Proyectos/crawler-agencias-ia/`, ficha `[[01_Projects/Crawler Agencias IA]]`.

## Qué se hizo
- Rellenar fichas con `estudio.py run`, regenerar tracción, informe y CSV, y contar agencias directas por tipo.
- Estudio escrito en `[[02_Areas/NeoZeler/Estrategia/Estudio de mercado - Agencias de IA para pymes en Espana]]` (`origen: mixto`, a revisar).
- `estudio_mercado.html` en el repo: página sola, sin librerías, 10 secciones, modo oscuro automático. Sin scroll horizontal a 375 px.
- Se paró un bucle de espera (`while pgrep -f "scripts/ampliar.sh"`) que se encontraba a sí mismo y llevaba 16 h; la ampliación había terminado la noche anterior a las 23:57.

## Hallazgos del estudio
- 42 de 50 agencias venden a «cualquier pyme»; automatizar (92 %) y chatbots (78 %) lo ofrece casi todo el mundo; voz/llamadas (26 %) y bases de conocimiento (18 %) están poco trabajadas.
- 45 de 50 no publican precio. Referencias de las que sí: auditoría 690–1.750 €, proyecto desde ~990 €, cuota mensual 100–1.500 €.
- Gancho saturado: 65 % «llamada gratis», 45 % «auditoría gratis»; solo 7 ofrecen demo y 6 calculadora de ROI.
- Casi ninguna da garantía de resultado.

## Problemas
- Gate de diseño parcial: se saltó la fase 0b (informe interno), una sola ronda de revisión, sin capturas en `.capturas/`, sin axe ni Lighthouse; el panel mide 529 px, así que no se vio a 768 ni 1280.

## Pendientes y próximos pasos
- Verificar a mano los precios citados.
- Revisión visual completa del HTML antes de commitear (el hook `guard-ui-commit` puede exigirla).
- Corregir «Cruces casi vacíos» del informe (ver `[[2026-11-11 - HTML de competencia para reunion con CEO]]`: el informe cuenta 6 y su tabla marca 9).
- Documentar README, ficha y `resumen.html` del crawler.

## Relacionado
- [[02_Areas/NeoZeler/Estrategia/Huecos de mercado - IA para pymes]] · [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
