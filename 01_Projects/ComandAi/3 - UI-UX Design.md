---
type: doc-software
doc: ui-ux
proyecto: ComandAi
status: aprobado
date: '2026-11-03'
origen: mixto
---

# 3 · UI/UX Design — ComandAi

> [!resumen] En cristiano
> El panel es una **ventana a un paisaje**: cada sección (Hoy, Tareas, Novedades IA, Leads, Proyectos) tiene su propia portada ancha dibujada en capas, y la luz de esos paisajes cambia según la hora real (amanecer, día, atardecer, noche). Debajo, una barra de iconos para moverte. Lo tuyo se escribe en letra serif y lo de la IA en letra de máquina, para distinguirlo de un vistazo. Móvil primero. Referencia de sensación: panel del vídeo de Nico CMW (portadas anchas + barra de iconos), con dibujos propios.

## 1. Principios de experiencia
- Abrir y ver el día en < 5 s, sin preguntar a la IA.
- Móvil primero (375 px); en escritorio la misma pantalla, centrada y más ancha.
- Una sola acción principal por pantalla.
- Siempre se ve de quién es el dato: **humano** o **máquina**.

## 2. Identidad visual (a aprobar)
- **Idea visual central**: esta marca es **una ventana al paisaje del día** y lo demuestra **cambiando la luz de cada portada según la hora real**, en vez de decorar con stock.
- **El producto como diseño**: la portada de «Hoy» muestra el número real de tareas pendientes como «sol» o «luna» (tamaño/posición = cuántas quedan); las demás portadas llevan un contador real (novedades nuevas, leads sin tocar, proyectos activos).
- **Composición firma**: portada ancha a sangre con 3–4 capas de cordillera/silueta en SVG, título grande en serif sobre ella y la barra de iconos flotante abajo.
- **Anti-referencias**: dashboard SaaS gris de tarjetas iguales; oscuro-navy con ámbar (ya es Los Apuntes de Liyo); oscuro-negro con naranja (TopLeads).
- **Referencias**: (1) panel del vídeo de Nico CMW → se toma la portada ancha por sección y el dock inferior, **no** sus imágenes ni colores; (2) Neozeler CRM → se toma su origen de paleta (logo NeoZeler), no sus ventanas de navegador.

| Elemento | Valor |
|---|---|
| Origen de la paleta | Logo NeoZeler: grafito, plata y azul hielo; azul NeoZeler `#2563eb` y marino `#1e3a8a` de la guía del vault. Sin colores fuera de marca. |
| Fondo (grafito con temperatura fría) | `#0C1117` · `#121A23` · `#1A2531` |
| Texto | `#E8EEF4` (principal) · `#9FB0C0` (secundario, ≥ 4.5:1 sobre fondo) |
| Hielo (humano) | `#A0D0E0` y escala hasta `#DDF1F7` |
| Azul (máquina y acción) | `#2563EB` con hover `#1D4ED8`; marino `#1E3A8A` para capas lejanas |
| Estados | OK `#34D399` · aviso `#FBBF24` · error `#F87171` (solo funcionales) |
| Tipografías y motivo | **Instrument Serif** (títulos de portada y todo lo *humano*: voz de una persona, cine) + **Bricolage Grotesque** (interfaz; cambio de Haytham 2026-11-03, sustituye a Instrument Sans) + **Red Hat Mono** (todo lo *máquina*, cifras y logs: el «terminal» de la IA) |
| Radio / sombras / espaciado | Radio 14 px en tarjetas y 999 px en el dock; sombras suaves de 1 capa; escala 4/8 px |
| Tono y voz | Tranquilo y directo, tuteo, frases cortas («Hoy tienes 4 tareas», «La IA trajo 7 novedades») |

### 2.1 Tokens
```css
:root {
  --bg-0:#0C1117; --bg-1:#121A23; --bg-2:#1A2531;
  --text:#E8EEF4; --text-2:#9FB0C0;
  --ice:#A0D0E0; --ice-hi:#DDF1F7;
  --brand:#2563EB; --brand-hover:#1D4ED8; --navy:#1E3A8A;
  --ok:#34D399; --warn:#FBBF24; --err:#F87171;
  --radius:14px; --ease:cubic-bezier(.16,.84,.3,1);
  --font-human:"Instrument Serif",serif;
  --font-ui:"Bricolage Grotesque",system-ui,sans-serif;
  --font-machine:"Red Hat Mono",ui-monospace,monospace;
}
```
(Solo modo oscuro en v1: es un panel de uso nocturno y el paisaje lo pide; el modo claro queda fuera de alcance.)

## 3. Inventario de pantallas
| Pantalla | Rol | Historia | Layout base | Estados |
|---|---|---|---|---|
| Hoy | Dueño | US-01, US-02 | portada + resumen | vacío · cargando · error |
| Tareas | Dueño | US-01 | lista | vacío («Nada pendiente») · cargando · error · éxito |
| Novedades IA | Dueño | US-02 | lista | vacío · cargando · error |
| Leads | Dueño | US-03 | lista-detalle | vacío · cargando · error (CRM caído) |
| Proyectos | Dueño | US-04 | lista | vacío · error |

## 4. Slots por pantalla (a completar con la Paleta de Componentes)
Pendiente: tras aprobar identidad, copiar `Paleta de Componentes.md` y elegir componentes distintivos por sección con `search_items_in_registries`.

## 5. Imágenes (origen decidido por Haytham: **SVG propios**)
- **Estilo**: paisaje en capas planas con degradados suaves, sin texto, sin personas, siluetas de cordillera/bosque/costa, 3–4 capas.
- Todas con `viewBox` fijo, colores solo con variables de la identidad, `role="img"` + `<title>`, optimizadas, sin metadatos del editor.

| Vista | Imagen (16:7, SVG) | Origen | Estado |
|---|---|---|---|
| Hoy | Cordillera con sol/luna (= tareas) | SVG propio | pendiente (se dibuja tras aprobar) |
| Tareas | Colinas con camino | SVG propio | pendiente |
| Novedades IA | Costa con faro y estrellas | SVG propio | pendiente |
| Leads | Valle con ciudad lejana | SVG propio | pendiente |
| Proyectos | Archipiélago | SVG propio | pendiente |
| Variantes de hora | Mismo SVG con 4 paletas (amanecer, día, tarde, noche) por variables CSS | SVG propio | pendiente |

## 6. Responsive y accesibilidad
- 375 / 768 / 1280 px. Objetivo táctil ≥ 44 px, contraste AA, foco visible, `prefers-reduced-motion` (sin parallax ni cambio animado de luz).
- Títulos sobre portada: velo degradado para contraste ≥ 4.5:1.

## 7. Movimiento y dinamismo (revisado 2026-11-03 tras revisar el vídeo)
- **Nivel 2 (dinámico)**: Haytham pidió la fluidez del panel del vídeo. Es una app de una sola página: no recarga al navegar.
- **Elementos vivos**: (1) carrusel de portadas en «Hoy» con las vecinas asomando, escala y opacidad según la distancia al centro, flechas, puntos y arrastre; (2) la portada pulsada «viaja» hasta la cabecera de su sección (View Transitions); (3) el indicador del dock se desliza entre secciones.
- **Curva propia**: `cubic-bezier(.16,.84,.3,1)`. Entrada escalonada de listas. Luz del paisaje por hora real.
- **Sin librerías**: JS propio (~120 líneas) y CSS; solo `transform` y `opacity`. `prefers-reduced-motion` lo apaga todo.
- **Fallback**: sin View Transitions el cambio es instantáneo; sin JS la web funciona con recarga normal.

## 8. Checklist de marca
- [ ] Prueba del intercambio
- [ ] Prueba de lejos
- [ ] Fila añadida al [[Registro de Identidades Visuales]] (al aprobar)
- [ ] Contraste verificado
- [ ] Pantallas hechas: Hoy, Tareas, Novedades IA, Leads, Proyectos + dock

---
Anterior: [[2 - TRD]] · Siguiente: [[4 - AppFlow]]

## 9. Trazabilidad añadida
- US-05 (acceso móvil): todas las pantallas se diseñan a 375 px; la URL de Tailscale abre «Hoy».
- US-06 (humano/máquina): cada tarjeta lleva marca de origen: serif + hielo = humano; mono + azul = máquina.


## 11. Añadidos 2026-11-03 (tira, decidir, embudo, sincronía)

- **Tira de la semana** (Hoy y Tareas): lun-dom, hoy marcado, punto en los días con tareas, enlace `?dia=AAAA-MM-DD` filtra Tareas.
- **Te toca decidir** (`/decidir`): decisiones que Claude o un script dejan en `maquina/util/decisiones.json`; botones Aprobar/Rechazar; también «Pedir a Claude» (`humano/para-claude.md`).
- **Tarjetas en embudo** (Leads y Hoy): cifras con flecha entre pasos; en móvil 2 columnas sin flechas.
- **Diario de hoy**: línea de tiempo con tareas hechas, acciones de la IA (`maquina/logs/ia.jsonl`) y novedades.
- **Sincronía en vivo**: el panel consulta `/estado` cada 4 s y se refresca solo si Claude, un script u Obsidian cambian los archivos (no pisa lo que escribes).
