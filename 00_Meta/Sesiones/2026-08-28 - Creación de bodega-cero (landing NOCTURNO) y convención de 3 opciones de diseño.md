---
type: sesion
status: cerrada
fecha: '2026-08-28'
proyecto: bodega-cero
tags:
- diseño
- landing
- convención
origen: mixto
---

## Contexto

Petición: "una página web para un ecommerce que vende ebooks de cómo hacer dropshipping, invéntate todo, es para una demo".

## Qué se hizo

- Proyecto nuevo en `~/Proyectos/bodega-cero/` (Vite + React 19 + TS + Tailwind v4 + GSAP + `@phosphor-icons/react`). Git desde el primer commit.
- 1er intento entregado como Artifact HTML → **rechazado**: "no me vuelvas a generar un artefacto cuando te pido una página web" + "se parece casi idéntica a infoproductor-demo, mismos colores, mismos botones, mismos iconos, todo muy cuadrado".
- 2º intento: se ofrecieron **3 direcciones de arte con preview ASCII** (NOCTURNO dark cinematográfico / MERCADO maximalista de color / ATELIER galería editorial). El usuario eligió **NOCTURNO**.
- Entregado: landing completa (hero + libro 3D, marquesina, catálogo asimétrico, método, testimonios, precio, capítulo gratis, FAQ, footer). Aurora ámbar + grano, cristal, botones magnéticos, easing propio, `prefers-reduced-motion`.
- Retoque posterior del libro 3D: modelo de caja real de 6 caras con vars `--w/--h/--t`, lomo con título, canto de páginas, halo y sombra de contacto.
- Registrado en `.claude/COMMON_MISTAKES.md`: #13 reforzada (Artifact ≠ "página web", 2ª ocurrencia) y #15 nueva (clonar la dirección de arte de un proyecto hermano).

## Aprendizajes / convención fijada

- **"Página web" = proyecto real en `~/Proyectos/`**, nunca Artifact ni `.html` suelto. "Es para una demo" no cambia esto. Artifact solo si pide explícitamente "un archivo suelto".
- **Antes de maquetar una landing, abrir los tokens del proyecto hermano del mismo dominio** (`infoproductor-demo`: `#ff3d00`, `border-radius:0`, Inter Tight+Playfair+JetBrains Mono, Lucide) y prohibirse su acento, radius, tipografías e iconos.
- **Ofrecer 3 direcciones de arte con preview y dejar elegir** — el usuario lo pidió explícitamente como flujo a repetir para cualquier web nueva, no solo tras un rechazo.
- Salida rápida del look "IA": iconos Phosphor (no Lucide), fuentes Fontshare (no Inter/Geist por reflejo).
- No se pudo verificar en navegador real (Chrome DevTools bloqueado); se avisó en cada entrega.

