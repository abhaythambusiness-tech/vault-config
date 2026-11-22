---
type: sesion
date: '2026-10-17'
proyecto: '[[01_Projects/Reto-30/Reto 30 - App real]]'
tags:
- reto-30
- sesion
- diseno
origen: mixto
---


# 2026-10-17 · Reto 30: ranking, comodines, sorteo y Dúo

## Qué se hizo
- Conversación de brainstorming con Haytham que recogió las ideas nuevas del reto y creó [[Cambios de diseno - Ranking, comodines, sorteo y Duo]].
- Actualización de los seis documentos aprobados ([[1 - PRD]], [[2 - TRD]], [[3 - UI-UX Design]], [[4 - AppFlow]], [[5 - Backend Schema]], [[6 - Plan de Implementacion]]) y del [[Borrador - Bases del sorteo]], todos marcados `revision: v2`.
- Prompt de cartel de lanzamiento (fecha de inicio sin fijar; la del 1 de noviembre era solo un ejemplo) entregado en el chat; no se ha generado ninguna imagen.

## Decisiones
- Ranking por nivel; desempate: menos comodines gastados, luego más retos extra.
- Comodines: uno cada 7 días (básico y medio) o cada 10 (avanzado); se gastan solos y cumplen el día.
- Sorteo: un premio de 50 € + merchandising de Factory Training, pagado por Haytham y Pedro; umbrales de racha 21/26/30 por nivel; mismas papeletas; sin fecha hasta lanzar la app; el dueño de Factory Training avisa al ganador; si nadie clasifica gana la mayor racha.
- Plan Dúo a 30 €: misma app, dos cuentas independientes y ranking separado, con pestaña de pareja y racha conjunta que no cuenta para el sorteo. Factory Training cobra el 15 % de la facturación total.
- Nivel fijo durante todo el reto.

## Aprendizajes
- Los umbrales por nivel y los comodines cambian el sentido de «sin fallar» del sorteo: las bases y la consulta legal hay que rehacerlas con las reglas nuevas.
- El SQL final está escrito pero no ejecutado; el arnés de PGlite de la v1 (47 comprobaciones) hay que adaptarlo y ampliarlo antes de aplicar nada.
- Un comodín que se gasta aunque la racha ya esté rota vale como día cumplido pero penaliza en el ranking; se aceptó por simplicidad.
- Pendiente: merchandising, sorteo en directo o con acta, fecha del sorteo y logo de Factory Training para el cartel.

