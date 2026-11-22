---
type: retro
proyecto: Conversor MP3 Facil
tipo: micro-saas
status: completa
retoques: 9
revisada: false
date: 2026-11-19
origen: mixto
---

> [!resumen] En cristiano
> Qué aprendimos al cerrar el conversor: el diseño cambió de rumbo (de «para mayores» a «oscuro y premium para todos») y el PRD se quedó atrás; se arregló y se midió todo (axe 0, Lighthouse A11y 100). Cifra de retoques (9) confirmada por Haytham el 2026-11-19.

# Retro de Proyecto

## Retoques
- **Cifra: 9**, confirmada por Haytham (peticiones de corrección tras la entrega, sesión 2026-11-18).
- Qué se corrigió: dirección visual (A/B/C → B2), 4 ajustes de B2, PRD v1 desfasado (público y alcance), quitar tema claro y `@magicui`, exportador de DESIGN.md con una sola fuente, notas de Capa 3 (título, `ui/button`, `animate-*`), 3 verificaciones (reduced-motion, contraste de foco, `prefers-contrast`) y la corrección de la medida de foco.

## Nivel frente a referencias
- Referencias: 21st (Signal Bars Loader, Waveform, MP3 Player). **Cumple** en carácter (barras ecualizadoras, vidrio fino, calma); **no cumple** en reproductor/onda real (no se implementó).
- Resultado medido: axe 0 en 375/768/1280, Lighthouse A11y 100 / BP 100 / Perf 90-100 / SEO 60 (por `noindex` intencional).

## Skills previstas vs usadas
- Previstas: `superpowers:test-driven-development`, `diseno-central`, `impeccable`, `accessible-animation`, `auditor-web`, `revisor-codigo`.
- Usadas: `impeccable` (critique/audit/detect), axe, Lighthouse, `slop-gate`, MCP `diseno`. Sobró `diseno-central` (huérfana, solo su exportador). Faltó `review-animations`: solo la lanza el usuario (`disable-model-invocation`), se hizo checklist manual.

## Librerías
- Elegidas: yt-dlp, ffmpeg, stdlib Go, shadcn/ui, motion. Acabaron: igual, **sin Magic UI** (B2); `ui/alert|card|input|progress` quedan sin usar (deuda).
- Trampas: Playwright pide Node ≥ 20 y chromium local con `--no-sandbox`; medir foco con transiciones activas da contraste falso (a mitad de fundido). Apuntar en `librerias.md` si Haytham lo aprueba.

## Medición tras publicar
Pendiente: rellenar a las 2-4 semanas de publicar (B2 aún no desplegado a producción).
- **Qué se mide**: conversiones completadas (≥ 30 en 2 semanas) y tasa de error (< 10 %) del PRD §3.
- **Mapas de calor y sesiones**: `no medido`.
- **Prueba A/B**: no aplica.
- **Prueba de usuario** (≥ 3 personas fuera del círculo): pendiente.
- **Qué hallazgo vuelve al diseño**: pendiente.

## Lecciones
| Síntoma | Causa | Regla | dominio | documento-destino |
|---|---|---|---|---|
| El diseño derivó en 3 commits sin tocar el PRD y se perdió la tipografía para baja visión | Cambios de dirección sin actualizar documentos | Todo cambio de dirección actualiza PRD, Paleta, README y DESIGN* en el mismo commit | proceso | PRD |
| Contraste de foco medido 3,2:1 (real 10,14:1) | Medido a mitad de `transition-colors` | Desactivar transiciones (`*{transition:none!important}`) y esperar antes de medir | diseno | UI-UX |
| `animate-spin/pulse` ignoraban `reducedMotion` | `MotionConfig` no cubre clases CSS de Tailwind | Añadir `motion-reduce:animate-none` y comprobarlo en render | diseno | UI-UX |
| Capa 3 auditada solo en estado inicial | No se probaron estados con datos reales (cola, resultados, error) | Medir axe/contraste también con datos reales y estados de carga | proceso | Plan |
| Borrado a 10 min desalineado entre API, web y README | Valor repetido en tres sitios | Cambiar los tres en el mismo commit; en producción sigue 30 min hasta desplegar | despliegue | Plan |
| Componentes shadcn instalados y sin uso | Se instalaron «por si acaso» | Borrar lo no usado antes de cerrar la fase | librerias | Plan |
