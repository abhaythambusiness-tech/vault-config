---
title: "Sesión - 2026-08-25 - Reseteo de propuesta de valor de NeoZeler"
date: 2026-08-25
type: meta/sesion
proyecto: "[[02_Areas/NeoZeler/NeoZeler - MOC|NeoZeler - MOC]]"
tags:
  - sesion
aliases: []
origen: mixto
---

# Sesión — 2026-08-25: Reseteo de propuesta de valor de NeoZeler

> [!abstract] Resumen
> Se borran todos los nichos, servicios, fichas y demos anteriores y se reconstruye el área desde cero: 5 nichos nuevos, 6 servicios transversales y 7 paquetes, con auditoría de nicho y matriz de encaje.

## Contexto

Decisión del fundador de reconstruir la propuesta de valor de [[02_Areas/NeoZeler/NeoZeler - MOC|NeoZeler - MOC]]. El catálogo anterior estaba organizado por nicho (cada nicho con sus propios servicios), lo que multiplicaba las fichas y dejaba el NeoZeler - Modelo de Precios permanentemente desactualizado. La inconsistencia ya estaba señalada en el MOC de Servicios desde el 2026-08-19 sin resolver.

## Qué se hizo

- Borrado de 5 fichas de nicho, 18 fichas de servicio, 12 demos y 3 MOC de servicios por nicho (recuperables en git).
- 5 auditorías de nicho nuevas: infoproductores, energía solar, clínicas dentales, academias físicas y digitales, alquiler de barcos/motos/vehículos de ocio.
- 6 fichas de servicio transversales y 7 fichas de paquete comercial.
- Nueva nota NeoZeler - Matriz Nicho x Paquete con el cruce completo.
- Reescritura de NeoZeler - MOC de Nichos, NeoZeler - MOC de Servicios y NeoZeler - Modelo de Precios.
- 18 agentes en paralelo, en tres oleadas: nichos → servicios → paquetes.

## Decisiones tomadas

- **Los servicios dejan de organizarse por nicho.** Son transversales; lo que se adapta al nicho es el paquete y el argumentario, no el componente.
- **Se separan servicios (componentes, documentación interna) de paquetes (lo que se cotiza).** En reunión nunca se cotiza un componente suelto.
- **Jerarquía de precios**: manda la ficha de paquete. La ficha de servicio manda en costes, horas y riesgos técnicos.
- **Estructura de carpetas**: `Servicios/Fichas/` (componentes) y `Servicios/Paquetes/` (comercial), ambas planas, sin subcarpeta por nicho.

## Aprendizajes (para futuras sesiones)

- **Lanzar agentes en oleadas paralelas produce precios incoherentes.** Los agentes de la oleada 2 y 3 leyeron la carpeta antes de que aterrizaran los ficheros de la oleada anterior, así que varios inventaron precios que luego chocaban. El paquete 5 llegó a costar más que comprar por separado los paquetes 2 y 4, anunciando un descuento inexistente. **Regla para la próxima**: si las tareas comparten cifras, o se pasan las cifras cerradas en el prompt, o se espera a que la oleada anterior termine.
- **La reconciliación de precios hay que hacerla siempre a mano al final.** No es opcional ni delegable: es donde se detecta el bundle que no ahorra nada.
- **El paquete 2 (agente de texto + seguimiento) sale como puerta de entrada en 4 de 5 nichos.** No estaba planeado; emergió del cruce de auditorías independientes. Simplifica el argumentario a uno solo.
- **Reglamento de IA, art. 50, aplicable desde el 2026-08-02**: obliga a declarar que el interlocutor es un sistema automático, con multas de hasta 15 M€. Afecta al agente de texto y al de voz. Hay que meterlo en todos los guiones.
- Las auditorías de dental y academias no usaron búsqueda web: sus cifras son estimación y están marcadas como tal. No usarlas en una propuesta firmada sin validar.

## Próximos pasos

- Validar con entrevistas reales las cifras estimadas de dental y academias.
- Meter la declaración del art. 50 en el guion del agente de texto.
- Resolver el suelo de inversión publicitaria en academias (600 €/mes de la ficha de Ads es alto para el sector).
- Actualizar NeoZeler - Plantillas de Cold Email por Nicho y NeoZeler - Pipeline Comercial & Prospección, que siguen apuntando a los nichos retirados.
- Decidir qué hacer con Diseño-servicios-neozeler y NeoZeler - Competencia, también desactualizados.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- NeoZeler - Matriz Nicho x Paquete
- NeoZeler - Modelo de Precios
