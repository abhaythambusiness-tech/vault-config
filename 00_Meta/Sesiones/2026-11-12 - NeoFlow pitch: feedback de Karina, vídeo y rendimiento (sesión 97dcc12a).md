---
title: 'NeoFlow pitch: feedback de Karina, vídeo y rendimiento'
date: '2026-11-12'
type: meta/sesion
origen: mixto
proyecto: '[[01_Projects/NeoFlow AI]]'
sesion_id: 97dcc12a-774b-484a-b732-071c6744c969
tags:
- sesion
- cierre-nocturno
---

> [!resumen] En cristiano
> Se rehízo la presentación de NeoFlow AI siguiendo el feedback de la mentora Karina: más corta, sin hablar de clínicas (solo pymes), con el vídeo del piloto, nuevos precios y datos reales de agencias de IA. Pasa accesibilidad a cero fallos; el rendimiento en ordenador es aceptable. Queda todo subido salvo lo último (según la sesión, push hecho al final).

## Qué se hizo
- Desglose del feedback (PDFs y transcripción de Karina) y aplicación al pitch en `~/Proyectos/neoflow-pitch/`: de 14 a 10-12 diapositivas.
- Portada: «NeoFlow AI by» + logo completo de NeoZeler, texto «Sistema de atención comercial automática 24/7 para pymes que trabajan con citas». Presenta Samira Boukli (formación, logos Microsoft y Zebra).
- Dos diapositivas de problema y dos de solución (incluida la demo, que se mantuvo); demo sin mencionar clínicas.
- Vídeo del piloto en su propia diapositiva 8 (resolución original 480×854).
- Mercado sin cifras de clínicas: 3,31 M empresas, TAM/SAM/SOM pequeños; roadmap simétrico.
- Modelo de negocio con textos de Haytham: 1.300 € implementación, 250 €/mes mantenimiento, ingresos adicionales.
- Competencia: España 49 agencias de IA, Málaga 7 (rastreo propio de 115 webs, es un mínimo).
- Titular de equipo: «Experiencia de negocio. Talento tecnológico. Visión de futuro.»
- Axe 0 violaciones en 320/375/768/1280. Lighthouse móvil 0,56-0,59; escritorio 0,61-0,69 (LCP 1,3 s, CLS 0,003).
- Commits desde `305d26f` hasta el último de equipo (`29fed94` y siguiente), con pushes confirmados por Haytham.

## Decisiones tomadas
- Nunca «charla», siempre «conversación»; nunca clínica/pacientes: solo pymes, clientes potenciales o leads.
- La demo no se quita.
- Solo importa el rendimiento en ordenador.

## Problemas
- TBT 0,6-1,0 s por el fondo animado (suposición: Lighthouse sin GPU, no medido).
- Diapositiva 3 a 375 px con scroll interno (435 px de más), ya existía.
- Vídeo de WhatsApp blando a pantalla completa; haría falta el original. Pantalla completa no probada.
- Los PDF generados no se commitean.

## Pendientes y próximos pasos
- Sustituir datos de demo inventados; conseguir el vídeo sin comprimir.
- Revisar la diapositiva 3 en móvil.

## Relacionado
- [[01_Projects/NeoFlow AI]] · [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

