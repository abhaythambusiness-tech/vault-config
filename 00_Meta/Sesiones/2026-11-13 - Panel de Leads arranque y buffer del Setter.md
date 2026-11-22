---
type: sesion
date: '2026-11-13'
proyecto: Panel de Leads
origen: mixto
---

> [!resumen] En cristiano
> Dos cosas. (1) Se recuperó en el Setter de n8n el buffer de mensajes seguidos y la separación de respuestas en varios mensajes, que se habían perdido en una mejora. (2) Se abrió el proyecto Panel de Leads: web por cliente con sus leads cualificados, con los 6 documentos (4 aplican) aprobados.

## Decisiones
- Buffer del Setter: Wait de 8 s + `Agrupar` + `If EsUltimoMensaje?` visible; solo contesta la ejecución del último mensaje y une los pendientes. Mensajes separados con `Basic LLM Chain` + `SeparadorMensajes` + `SepararObjetos` + bucle de envío (quitado `Trocear`). Waits con unidad `seconds` explícita; filtro de `MarcarProcesado` con `keyName: id`. Publicado en n8n (versión `2e3d7a64`), sin probar con tráfico real.
- Panel de Leads: vía micro SaaS ligera; cualificado = cita o análisis; etapas y pipeline opcional; datos por API pública de n8n con clave acotada (plan B webhooks); mínimo 1-2 librerías de UI.

## Aprendizajes
- Un `Wait` de n8n sin unidad es ambiguo: poner siempre `seconds`.
- `~/Proyectos/setter-neozeler/build.py` regenera desde un export viejo y pisaría los cambios hechos a mano.
- Error 92 en COMMON_MISTAKES: no fijar las librerías de UI obligatorias en Ficha/TRD; skill y plantilla TRD corregidas.
- El lint de trazabilidad exige que UI-UX y AppFlow citen las historias aunque estén `no-aplica`.

## Pendiente
Probar la clave acotada de n8n, identidad visual, definir cuánto del `analisis` basta.

