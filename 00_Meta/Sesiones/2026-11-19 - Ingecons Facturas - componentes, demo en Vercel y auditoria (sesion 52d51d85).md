---
type: meta/sesion
date: '2026-11-19'
origen: mixto
proyecto: Ingecons Facturas
sesion_id: 52d51d85-04a4-4768-8bed-c6b9fbf95733
tags:
- sesion
- cierre-nocturno
---

> [!resumen] En cristiano
> La app de facturas de INGECONS (`~/Proyectos/ingecons-facturas/`) ganó piezas nuevas (avisos, panel de cobro desde abajo, buscador de obra) y se hizo una copia demo que guarda todo en el navegador y está subida a Vercel con datos inventados. Haytham la dejó pública. Sin commit y sin ficha en el vault todavía.

## Contexto
Continúa la sesión de UI premium del mismo día ([[2026-11-19 - Ingecons Facturas - UI premium, PDF y mejoras UX]]). Sesiones hermanas con el mismo arranque: `f1a15068` (la que escribió esa nota) y `e1f986d9` (rama que solo añadió una pregunta sobre qué significa la «barrita blanca» de la regla de origen: es el borde entre tramos de factura, sin significado propio).

## Qué se hizo
- Búsqueda de mejores componentes: tanda 1 (shadcn: `drawer`, `sonner`, `combobox`, `table`, `dashboard-01` solo de referencia) y tanda 2 (21st.dev: Number Field, Currency, Swipe, Bottom Menu, Empty State, Upload).
- Instalada la tanda 1. Se usan: `CobroRapido.tsx` (panel inferior en vez de `window.confirm`), avisos `sonner` con `<Toaster />` en `layout.tsx`, y `SelectorObra.tsx` (buscador) en factura nueva y gastos. `table` instalada sin usar.
- Barra lateral `sticky top-0 h-dvh` para que «Nueva factura» no se vaya abajo con el scroll.
- Arreglo de la barra «Facturado a origen» (`ReglaOrigen.tsx`): último tramo con color distinto.
- Copia demo (`ingecons-facturas-demo`): sin Prisma ni BD, datos ficticios con fechas relativas a hoy, guardado en el navegador, banner DEMO con «Reiniciar demo», PDF en el navegador, foto del ticket en gastos y pantallas vacías. Tipos, eslint, 6 tests y `next build` pasan; probado crear factura, cobrar, gasto con foto, PDF y recarga.
- Desplegada en https://ingecons-facturas-demo.vercel.app (con `noindex`). Auditoría rápida final: sin fallos graves.

## Decisiones
- Demo con datos en navegador: no se sigue con el proyecto real hasta que el cliente pague (palabras de Haytham).
- De la tanda 2 solo se hizo foto del ticket y estados vacíos; Number Field, Currency, Swipe y Bottom Menu descartados (poco valor, complican formularios).
- Haytham eligió «Dejar pública» la URL.

## Problemas
- `vercel deploy` salió como producción sin `--prod` (primer despliegue del proyecto). Quedó público por decisión de Haytham.
- La CLI de shadcn falla con Node 18; Next 16 necesita Node 22 (`~/.local/share/fnm`). `combobox` sobrescribió `button`, `input` y `textarea`; se restauraron las versiones originales.
- Un hook bloqueó mirar la configuración de entorno; no se rodeó.

## Pendientes y próximos pasos
- Probar a mano la URL pública; el botón flotante tapa el campo de foto a 375 px; el diálogo de confirmar al emitir usa el del navegador.
- `npm audit`: 4 avisos moderados en `shadcn`/`ts-morph` (solo herramientas de desarrollo). Cabeceras de seguridad ausentes (irrelevante en demo).
- Sin Lighthouse ni axe en la demo; sin git en la copia demo.
- Documentación del proyecto pendiente (§0.8): ficha en `01_Projects`, README, `resumen.html`, marcador `.proyecto`.

## Relacionado
- [[2026-11-19 - Ingecons Facturas - UI premium, PDF y mejoras UX]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

