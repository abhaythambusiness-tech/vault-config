---
title: "Sesión - 2026-08-28 - bodega-cero - landing y subida a GitHub"
date: 2026-08-28
type: meta/sesion
proyecto: "bodega-cero"
sesion_id: dad5594d-bca0-48cf-8c9c-48f559bca5e9
tags:
  - sesion
  - cierre-automatico
aliases: []
origen: mixto
---

# bodega-cero — landing de una tienda de ebooks y publicación

> [!resumen] En cristiano
> Se creó una web demo inventada de una tienda de ebooks de dropshipping. Haytham rechazó el primer intento por genérico y se hizo un diseño más atrevido, adaptado a móvil y subido a Vercel y GitHub. **Aviso:** en el chat se pegó un token de GitHub; hay que revocarlo.

## Contexto
Sesión de agosto recogida hoy porque su archivo se volvió a tocar el 2026-11-02. Ya existe una nota más completa: [[2026-08-28 - Creación de bodega-cero (landing NOCTURNO) y convención de 3 opciones de diseño]]. Esta nota solo enlaza y resume. El proyecto está en `~/Proyectos/bodega-cero/` (Vite + React + TypeScript) y figura en [[00_Meta/Proyectos Pendientes a Futuro]].

## Qué se hizo
- Primer intento rechazado: muy genérico, casi igual a la demo de infoproductor (mismos colores, botones, iconos, todo cuadrado). Se dijo además «no me vuelvas a generar un artefacto cuando te pido una página web».
- Segundo intento: landing NOCTURNO, con retoques al ebook en 3D. Haytham pidió cerrar la sesión diciendo que le gustó el diseño y la idea de ofrecer tres opciones de diseño, «algo a repetir».
- Adaptación a móvil, `vercel.json` y despliegue; repo en GitHub (`bodega-cero`, público).
- Memorias nuevas: «web = proyecto real» y «evitar la dirección de arte de un proyecto hermano».

## Decisiones tomadas
- Ante una petición de web: proyecto real en `~/Proyectos/`, nunca un artefacto suelto.
- Ofrecer tres opciones de diseño antes de construir.

## Aprendizajes (para futuras sesiones)
- Dos demos seguidas no pueden compartir paleta ni componentes: se nota y se rechaza.

## Próximos pasos
- **Revocar el token de GitHub (`ghp_…`) pegado en el chat durante esta sesión** (regla dura §0.1). No se copia aquí. La sesión terminó con un script que lo recibía como argumento; si se reutilizó, avisar cada vez.
- Dar ficha propia a bodega-cero en `01_Projects/` si se retoma.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[2026-11-02 - Cierre nocturno]]
