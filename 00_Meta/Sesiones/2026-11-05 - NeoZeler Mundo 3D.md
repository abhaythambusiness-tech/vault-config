---
date: 2026-11-05
proyecto: "[[01_Projects/NeoZeler Mundo]]"
type: sesion
origen: mixto
---

> [!resumen] En cristiano
> Haytham pidió «transformar NeoZeler en un mundo 3D» y rechazó las preguntas. Construí una v0 con Three.js reutilizando la identidad de `neozeler-web`. Queda por confirmar que es lo que imaginaba.

## Qué se hizo
- Proyecto nuevo `~/Proyectos/neozeler-mundo/` (Vite + TS + Three.js), README y `resumen.html`.
- Fase 0b (referencias Dribbble) saltada a propósito: Haytham dijo «sin preguntas». Identidad: la ya aprobada de NeoZeler Web.
- Flujo de 6 documentos (§0.10) saltado: prototipo pedido sin brief. Si se convierte en producto, hacer PRD + Plan.

## Aprendizajes
- El navegador del panel de Claude no crea contexto WebGL; sirve Chromium de Playwright con `--use-angle=swiftshader --enable-unsafe-swiftshader --virtual-time-budget`.
- Pabellones planos: orientarlos hacia fuera (`lookAt`) o se ven de canto desde la cámara por defecto.
- Se añadió `.claude/launch.json` en el vault para el servidor de pruebas (puerto 5174).
- Pulido tras «Sí, pulir»: `main.ts` pasó a ser cargador y la escena vive en `mundo.ts`; el desplazamiento lateral de cámara en móvil se calibró a ojo (2.5 se pasaba, 1.4 encaja).
- Auditoría: Lighthouse 11 y axe-core instalados solo en el scratchpad (Lighthouse actual exige Node 22; aquí Node 18). Python Playwright del venv de scrapling sustituye a Playwright de Node.
