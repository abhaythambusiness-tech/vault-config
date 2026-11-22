---
type: sesion
date: '2026-11-15'
proyecto: '[[Setter NeoZeler]]'
origen: maquina
sesion_id: 4c174cc9-002c-4cb5-a061-9c43cda68065
tags:
  - sesion
  - cierre-automatico
---

> [!resumen] En cristiano
> Se hizo una página HTML que explica cómo funciona el setter: pasos, tiempos y costes, con una calculadora. Se creó su ficha en el vault. Y se limpiaron de las cuatro tablas las filas de prueba de los lotes 5 y 6.

## Qué se hizo
- `~/Proyectos/setter-neozeler/resumen.html`: un solo archivo sin build. Reproduce en JS puro el Flowchart que pegó Haytham (lienzo de puntos, conectores curvos, tarjetas arrastrables); cada paso con su tiempo y coste y detalle al pulsar, más una calculadora. Sin errores de consola; capturas revisadas.
- Ficha en el vault: [[01_Projects/Setter NeoZeler]] y [[Setter NeoZeler - Auditoria de simplificacion]].
- Con el «Sí, bórralas» de Haytham: borradas filas de prueba de los lotes 5 y 6 en las 4 tablas, verificado a 0. Truco: `setter_clientes` y `setter_citas` guardan el teléfono sin prefijo `34` y no tienen `chat_id`; la primera pasada solo limpió mensajes y hubo que repetirla con el formato real. Workflow temporal archivado.

## Relacionado
- Antecedente: [[2026-11-15 - Setter Mila v2 y buffer de 20 s (sesion 36bd7f22)]]
- [[2026-11-15 - Oferta central y ficha de servicio del Setter]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
