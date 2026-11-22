---
type: ficha-investigacion
proyecto: "Comanda Viva"
tipo: web-cliente
status: aprobada
date: 2026-11-04
origen: mixto
---

> [!resumen] En cristiano
> Antes de escribir el TRD, apuntamos qué piezas ya hechas vamos a usar, qué herramientas de Claude ayudan en cada fase y con qué nos vamos a comparar. Las librerías están elegidas por lo que ya funcionó en otros proyectos del vault; **falta confirmar sus docs con context7 en el TRD**. Al aprobarla, `status` pasa a `aprobada`.

# Ficha de Investigación

## Librerías
Fuentes: `librerias.md` (trampas ya vividas) y `npm view` del 2026-11-04. Docs con context7: pendiente (TRD §1.1).

| Necesidad | Candidata A | Candidata B | Elegida y motivo | Fuente |
|---|---|---|---|---|
| Web + rutas (cliente, caja, admin) | Next 16 + React 19 | Vite + React | **Next 16**: ya dominado en reto-30/topleads; trampas anotadas (`cacheComponents`, `proxy.ts`) | `librerias.md` |
| Datos, login y **tiempo real** (comanda a caja, stock) | Supabase (Postgres + Auth + Realtime) | Firebase | **Supabase**: SQL con transacción para descontar stock atómico (RF-05) y RLS; Realtime cubre caja. Firebase no da SQL ni transacciones tan claras | `librerias.md`, `supabase-js` 2.119.0 MIT |
| Sesión en Next | `@supabase/ssr` | `auth-helpers-nextjs` | **`@supabase/ssr`**: el otro está deprecado | `librerias.md` (reto-30) |
| Validar SQL sin Docker | PGlite | Supabase local (Docker) | **PGlite**: arnés de RLS ya hecho en starter-saas | `librerias.md` |
| QR por mesa | `qrcode` 1.5.4 (MIT) | `qrcode.react` 4.2.0 (ISC) | **`qrcode`** en servidor para generar SVG/PNG imprimible; `qrcode.react` solo si se pinta en pantalla | `npm view` |
| Gráficas del panel | Recharts 3.10.1 (MIT) | Gráficas SVG propias | Por decidir en el TRD según peso y diseño (regla `dashboards-saas.md`) | `npm view` |
| Validación de entradas | Zod 4.6.7 (MIT) | Valibot | **Zod**: ya usado; pedidos del cliente son entrada no confiable | `npm view` |
| Estilos | Tailwind 4 + shadcn | CSS propio | **Tailwind 4** con `@tailwindcss/postcss` (trampa conocida de topleads) | `librerias.md` |

## Skills y agentes
- Antes de nada: `diseno-central`, `dribbble-scrape` (5-8 referencias enseñadas a Haytham).
- TRD y datos: `supabase`, `supabase-postgres-best-practices`, `context7`, `sequential-thinking` (descuento atómico de stock y concurrencia).
- Esquema: `schema_to_migration.py`, PGlite; comprobar `ON DELETE` en toda FK.
- Identidad y pantallas: `local-business-rebuild`, `small-business:brand-style`, `hallmark`, `modern-web-design`, `design-taste-frontend`, `design:ux-copy`.
- Animación (menú vivo, contador de raciones): `web-animation-skills:accessible-animation` y luego motor elegido (`motion-framer-choreographer`).
- Panel financiero: `dataviz`, `data-visualization`, `rules/dashboards-saas.md`.
- Build: `vercel-react-best-practices`, `test-driven-development` (lógica de disponibilidad).
- Calidad: `accesslint-audit`, `design:accessibility-review`, `pre-ship-gate`; auditoría puntual en paralelo: `auditor-web` + `revisor-codigo` + `ponytail-audit`; cierre: `archivista`.
- Starter kits que encajan: [[Starter SaaS]] (auth + RLS probada) y «Dashboard base». Nada de restaurante hecho antes (buscado en vault: sin duplicados).

## Referencias
Se fijan tras `dribbble-scrape` y la elección de Haytham. Candidatas de partida de la [[Biblioteca de Referencias Premium]]:
- **Arc** (arc.net): marca con carácter, color y voz propios → carácter «cercano» del menú.
- **Linear** (linear.app): jerarquía y sobriedad → panel de caja y finanzas (poco ruido, mucha claridad).
- Menú de cliente: buscar 2 referencias de cafés/brunch premium (Dribbble/Mobbin); pendiente de que Haytham las vea y apruebe.

## Lecciones aplicables
- Nunca entregar la web como un único `.html`/Artifact: es un proyecto real en `~/Proyectos/comanda-viva/` (COMMON_MISTAKES §13).
- Dominios ya hechos: abrir tokens previos y prohibirse su acento/radius/tipografía/iconos para no repetir look (§8: bodega-cero ≈ infoproductor-demo).
- Nada de contenedores grises vacíos ni fotos fotorrealistas inventadas de personas: si faltan fotos de platos, **parar y preguntar** (§6, §7).
- Probar el SQL en PGlite y volver a `reset role` tras cada error esperado (reto-30).
- Validar el ciclo completo crear → refrescar → anular → refrescar **en producción** antes de dar nada por hecho.
- Contraste en tema oscuro (§10) si la caja va oscura; la caja se usa con luz de local.
- No asumir esquemas de BD remota: preguntar si existe proyecto Supabase antes de crear uno (puede costar).

## Extras de la vía

### web-cliente
- **Marca de la clienta**: logo, colores y tipografía de Desayunos de Monika **sin recibir**; mirar su ficha de Google Maps y redes. Pedir logo vectorial (si es JPEG de fondo claro, avisar).
- **Imágenes**: sin fotos de platos todavía. Hueco por hueco: foto real de la clienta / prompt para Gemini / SVG propio; decide Haytham, no se rellena en silencio.
- **Marca blanca**: nombre, logo y colores del restaurante en tokens/BD, no en código, para replicar `Comanda Viva` a otros locales (RF-13). La marca `Monika Viva` es la primera instancia.
- **Tabla de huecos**: carta (platos, precios, alérgenos), ingredientes, mesas, logo, fotos.
