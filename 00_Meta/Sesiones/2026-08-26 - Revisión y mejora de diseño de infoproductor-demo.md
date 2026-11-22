---
title: Sesión - 2026-08-26 - Revisión y mejora de diseño de infoproductor-demo
type: meta/sesion
date: '2026-08-26'
proyecto: infoproductor-demo
origen: mixto
---


# Sesión — 2026-08-26: Revisión y mejora de diseño de infoproductor-demo

> [!abstract] Resumen
> Auditoría de diseño de `~/Proyectos/infoproductor-demo` (landing "Método Pluma") y resolución de todos los huecos detectados a nivel de código/componentes, sobre todo la ausencia total de imágenes.

## Contexto
Continuación de la sesión previa de agent-debate sobre el diseño de la demo (motion, componentes premium). Hoy tocaba revisión de código/componentes con foco en que la web no tenía ninguna imagen real.

## Qué se hizo
- Auditoría de los 14 componentes (`app/components/*.tsx`) + `page.tsx`: motion y microinteracción ya resueltos (GSAP, Reveal, MagneticButton), el hueco real era 100% visual/imágenes.
- Intenté onboardear el proyecto en `Bloom` (`bloom_list_brands`) — no hay brand para este proyecto ni URL pública que crawlear (demo local, sin deploy). Bloom no ejecutable aquí; declarado explícitamente en vez de fallar en silencio.
- Resuelto el hueco de imágenes con SVG/código propio (sin dependencias nuevas):
  - `BrandMark.tsx` — glifo de marca (trazo de pluma), reutilizado en `Nav`, `Footer` e `Instructor` como firma visual recurrente.
  - `Instructor.tsx` — placeholder del "retrato" elevado con patrón halftone en acento + marcas de esquina tipo visor + watermark del glifo, sin fabricar una foto real de Nicolás Prado (persona ficticia).
  - `TemplateStack.tsx` — gráfico abstracto de fichero apilado en la tarjeta "40 plantillas swipe" de `ValueGrid.tsx`.
  - `Curriculum.tsx` — icono Lucide por fase (Compass/Layers/Rocket): era la única sección 100% texto sin icono.
  - `app/opengraph-image.tsx` — OG image dinámica vía `next/og`, con tipografía/colores de marca. `favicon.ico` ya existía.
  - `layout.tsx` — añadido `metadataBase` (quitaba warning de build).
- Verificación: `npx tsc --noEmit` limpio, `npx next build` limpio sin warnings.

## Decisiones tomadas
- No fabricar una foto fotorrealista de Nicolás Prado (instructor ficticio) aunque sea demo — regla dura del CLAUDE.md. Placeholder elevado con recursos gráficos abstractos en vez de imagen falsa.
- No forzar Bloom sin URL pública real que crawlear — se declara el MCP no disponible y se resuelve con SVG inline coherente con los tokens de marca (Tailwind vars en `globals.css`), sin dependencia externa.

## Aprendizajes (para futuras sesiones)
- Para proyectos de código en `~/Proyectos/` sin deploy/URL pública, `bloom_onboard_brand` no es viable (necesita crawlear un sitio o Instagram real) — el fallback correcto es SVG/código propio usando los design tokens existentes, no forzar el MCP ni saltarse la regla anti-imagen-falsa.
- El GateGuard de `.claude` pide declarar hechos (importadores, API afectada, verbatim del usuario) antes de cada `Edit`/`Write` **por archivo nuevo tocado en la sesión** — repetir la llamada sin volver a declarar falla aunque se dijera segundos antes.

## Próximos pasos
- Si Haytham consigue foto real de Nicolás Prado o despliega el sitio con URL pública → onboardear Bloom de verdad y generar assets de producto reales.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

