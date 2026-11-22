---
date: '2026-10-31'
type: sesion
proyecto: '[[01_Projects/NeoZeler Web/Analisis UI-UX y Plan de Mejora]]'
tags:
- neozeler-web
- ui
origen: mixto
---

> [!resumen] En cristiano
> El hueco vacío al lado de las preguntas frecuentes se resolvió con una tarjeta de contacto (después de rechazar tres dibujos). El botón «Mundo: Papel/Cromo» pasó a «Modo oscuro / Modo claro». Todo está subido a GitHub y servido en el puerto 3000.

## Qué se hizo
- `faq-lista.tsx` (nuevo) y `faq.tsx`: preguntas + tarjeta «¿No ves tu duda?» con gema de fondo y los dos botones. Commit `ee9a0ce`.
- `world-switch.tsx` y política de cookies: botón claro/oscuro con luna/sol. Commit `107603a`. El mecanismo interno (papel/cromo, `data-world`) no cambia.
- Push a `origin/main` (`7bae91b..107603a`). Build de producción reiniciada en `:3000`.

## Aprendizajes
- Tres SVG seguidos rechazados (pasos, Z del logo, «?» de puntos): ante un «no me gusta», ofrecer enfoques distintos y preguntar. Ver `.claude/COMMON_MISTAKES.md` #71.
- El puerto 3000 era un `next start` con build vieja (#72); `pkill -f` mata la propia shell (#73); Node 18 por defecto rompe Next 16 (#74).
- Librerías: `librerias.md`, sección «Tailwind 4 / Next 16 (neozeler-web)».

## Pendiente / mejoras futuras
- El servidor de producción `:3000` va con `nohup npm run start`, sin supervisión: no vuelve solo tras reiniciar el PC. Hacer un servicio de usuario systemd.
- Tarjeta de contacto no revisada a 375 y 768 px; sin pasar axe ni Lighthouse en esta tanda (`rules/verificacion-web.md`).
- Texto «No ves tu duda» y botones: en 1440 px los botones se apilan; valorar ancho de la tarjeta.
- El plan de mejora UI/UX sigue abierto: `[[01_Projects/NeoZeler Web/Analisis UI-UX y Plan de Mejora]]` (portada sin propuesta de valor, acciones clave a mano en móvil).
- Ficha de Investigación / Retro del proyecto `.proyecto`: la Retro se rellena al cerrarlo.

