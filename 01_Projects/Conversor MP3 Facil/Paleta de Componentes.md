---
type: doc-software
doc: paleta-componentes
proyecto: Conversor MP3 Facil
status: aprobada
date: '2026-11-16'
origen: mixto
---

> [!resumen] En cristiano
> Piezas de pantalla elegidas de librerías ya hechas (en vez de dibujarlas a mano). Pantalla única, 3 secciones.

| Sección | Componente | Origen | Motivo | Descartado |
|---|---|---|---|---|
| Paso 1: buscar o pegar | Input + Tabs (Buscar / Pegar enlace) | shadcn/ui | accesibles por teclado y lector | Command (demasiado denso para mayores) |
| Paso 1: resultados | Card con miniatura grande | shadcn/ui | una tarjeta = una canción | Carrusel (se pierde el contexto) |
| Paso 2: convertir | Button 72 px + Progress que se llena | shadcn/ui + motion | motion anima el relleno (único motor) | Magic UI Animated Progress (descartado por decisión B2, 2026-11-18) |
| Paso 3: descargar | Button + Alert (éxito/error/aviso) | shadcn/ui | mensajes claros en español | Toast (desaparece solo, mal para mayores) |
| Animación | motion (fundido y ligero desenfoque de entrada, relleno de progreso) | motion | único motor de animación; sustituye a Blur Fade | Magic UI Blur Fade, Border Beam (descartados por decisión B2, 2026-11-18) |
| Fondo / tarjeta | Card con vidrio fino (borde 1 px al 8 %) + `motion` para la entrada | shadcn/ui + motion | sustituye a Magic Card | Magic Card (descartado por decisión B2, 2026-11-18) |
| Iconos | lucide | stack | — | — |

Peso: sin dependencias extra salvo `motion`. Un solo motor de animación.

> [!riesgo] Ancla de decisión B2 (2026-11-18)
> **Premium = vidrio fino + calma.** NO = haz de borde, brillo que sigue al cursor, bling. Magic UI queda fuera por decisión, no por descuido: no volver a añadirla porque «premium».

> [!aviso] Pendiente de revisar (PRD)
> Esta paleta nació para mayores. Con la dirección oscura: «Command (demasiado denso para mayores)» y «Button 72 px» dependen del público del PRD, que aún no está actualizado. Cada fila nueva se confirma cuando Haytham apruebe el PRD.

