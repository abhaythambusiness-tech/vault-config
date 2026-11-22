---
type: doc-software
doc: plan-implementacion
proyecto: "Comanda Viva"
status: aprobado
date: 2026-11-04
origen: mixto
---

# 6 · Plan de Implementación

> [!resumen] En cristiano
> Orden para construir Comanda Viva en tareas pequeñas, cada una con su «cómo sé que está hecha». Primero la base de datos (ya hecha y probada), luego lo que ve el cliente, luego caja, luego la dueña y al final el panel de números, las imágenes y la puesta en marcha. Hay **dos decisiones tuyas** que bloquean el final: crear el proyecto en la nube (cuesta dinero) y decidir las imágenes. Código real en `~/Proyectos/comanda-viva/`, con git desde el primer commit y sin tocar nada en la nube sin tu permiso.

Derivado de [[1 - PRD]], [[2 - TRD]], [[3 - UI-UX Design]], [[4 - AppFlow]] y [[5 - Backend Schema]].

## 1. Fases
| Fase | Objetivo | Entregable demostrable | Historias |
|---|---|---|---|
| 0 Scaffold | Repo, `.gitignore`, `.env.example`, Node 22, `components.json` con los 7 registries, identidad copiada a `DESIGN-IDENTITY.md` | `npm run build` limpio | — |
| 1 Datos | Migración y semilla de [[5 - Backend Schema]] (ya generadas y con 20 pruebas verdes); cliente Supabase y Zod | `node supabase/tests/schema.test.mjs` verde + tipos generados | US-06, US-07, US-08, US-09, US-10 |
| 2 Núcleo cliente | Menú por QR, carrito, notas, enviar, Mi mesa, lista viva | Un comensal de prueba pide desde `/m/<token>` y baja el stock | US-01, US-02, US-03, US-04, US-05 |
| 3 Núcleo caja | Acceso, comandas en vivo, cuenta, cobro, anular, mesas | Una comanda llega a caja y se cobra | US-13, US-14, US-15, US-16, US-20 |
| 4 Núcleo dueña | Inventario, platos y recetas, plantilla, mesas y QR, ajustes, panel financiero | La dueña carga un plato con receta y ve «quedan N» en el menú | US-11, US-12, US-17, US-18, US-19, US-21 |
| 5 UI e imágenes | Identidad aplicada a todas las pantallas; huecos de imagen resueltos contigo | Demo navegable en 375/768/1280 px | (todas) |
| 6 Pulido | Estados, accesibilidad, rendimiento, concurrencia real | Checklist técnico y de marca | (todas) |
| 7 Despliegue | Staging y producción en Vercel + Supabase | URL en vivo y ciclo verificado en producción | (todas) |

Las fases 2, 3 y 4 se pueden intercalar por pantalla (cada pantalla se entrega con su interfaz ya con la identidad); la fase 5 es el repaso final y la resolución de imágenes.

## 2. Tareas
Cada tarea acaba con su commit. Todas dependen de T-01 salvo que se indique otra cosa.

**Fase 0 y 1**
- [x] T-01 · (—) Scaffold: `git init` + `.gitignore` (`.env`, `node_modules/`, `.next/`), Next 16 + React 19 + Tailwind 4 (`@tailwindcss/postcss`), Node 22 (`.nvmrc`), `.env.example` con `!.env.example` en `.gitignore`, `components.json` con `@shadcn @magicui @aceternity @bklit @componentry @spaceui @uiarc @skiper-ui`, `DESIGN-IDENTITY.md` (copia de UI-UX §2, §5, §7), `.claude/COMMON_MISTAKES.md`, fuentes autoalojadas Fraunces + Figtree · archivos `package.json`, `app/`, `components.json` · hecho cuando `npm run build` y `tsc --noEmit` pasan · depende de: —
- [x] T-02 · (US-06, US-07, US-08, US-09, US-10) Migración inicial y semilla generadas con `schema_to_migration.py`; arnés PGlite en `supabase/tests/schema.test.mjs` · hecho: 20 pruebas verdes (2026-11-04) · depende de: —. Al pasar a Vitest (T-03) se conservan las mismas comprobaciones.
- [x] T-03 · (US-06) Cliente Supabase con `@supabase/ssr` (`lib/supabase/{server,client}.ts`), `proxy.ts` para refrescar sesión, Zod para entradas y respuestas de cada RPC, tipos generados de la migración, Vitest con el arnés PGlite · hecho cuando una prueba llama `get_menu` con la semilla desde el código y los tipos compilan · depende de: T-01, T-02

**Fase 2 · Cliente (menú por QR)**
- [x] T-04 · (US-01, US-02) Ruta `/m/[token]`: `get_menu`, categorías con chips, tarjetas pastel de plato, hilera de yemas y texto «Quedan N» siempre visible, `marquee` · archivos `app/m/[token]/page.tsx`, `components/menu/*` · hecho cuando con la semilla se ve el menú, un plato con 2 raciones muestra 2 yemas y «Quedan 2», y un token falso lleva a C5 con el teléfono · depende de: T-03
- [x] T-05 · (US-03) Hoja de detalle (`@shadcn/drawer`) con descripción, alérgenos, cantidad y nota con contador desde el primer carácter (≤140) · hecho cuando la nota larga se bloquea suavemente y se conserva al cerrar la hoja · depende de: T-04
- [x] T-06 · (US-04, US-08, US-09) Carrito (sessionStorage), C3 Resumen (ticket dentado + stepper + línea «Pagas al final, en caja» por confirmar con la clienta), acción de servidor que llama `crear_pedido` con clave de idempotencia, errores `sin_stock` con «Cambiar por…», pantalla «Enviado · Pedido nº N» · hecho cuando enviar dos veces seguidas con la misma clave crea un solo pedido, el stock baja y un plato sin ingredientes desaparece del menú · depende de: T-05
- [x] T-07 · (US-05) Ampliar [[5 - Backend Schema]] con `get_pedidos_mesa(p_token)` (pedidos de la cuenta abierta con estado y líneas, solo para el anónimo con token) y probarla en PGlite; después C4 «Mi mesa» con varias tandas, estados y aviso de línea anulada con `sonner` · hecho cuando un segundo pedido de la misma mesa aparece sumado y una anulación de caja se ve en C4 · depende de: T-06
- [x] T-08 · (US-02) Lista viva: polling de `get_menu` cada 3 s solo con la pestaña visible; plato que se agota queda gris «Se acabó» y se quita al volver a C1; «Cargando…» y «Reintentar» a los 5 s; fotos diferidas · hecho cuando una prueba con dos pestañas muestra el plato gris sin saltos de lista · depende de: T-06

**Fase 3 · Caja**
- [x] T-09 · (US-20) Acceso A5: login email + contraseña con Supabase Auth, guarda de rutas `/caja` y `/admin` por rol (`miembros`), sesión caducada vuelve a la pantalla en que estaba · hecho cuando un anónimo no entra, caja no abre `/admin` y la dueña sí · depende de: T-03
- [x] T-10 · (US-13) K1 Comandas en vivo: canal privado `caja:<restaurante_id>` con Realtime, polling de 5 s como plan B con banda «Sin conexión en vivo», botón «Activar sonido», pestañas con contador, orden por antigüedad, punto «sin ver», botón «Servida» · hecho cuando un pedido de T-06 aparece en caja sin recargar y suena · depende de: T-06, T-09
- [ ] T-11 · (US-14, US-15) K2 Cuenta y cobro: cuenta de la mesa con todas las tandas, método con `radio-cards`, entrega y cambio, dividir en partes iguales, «Mover a mesa X», confirmación que lista las líneas pendientes, aviso rojo «Pidió después de cobrar» · hecho cuando cobrar cierra la cuenta, libera la mesa y un pedido posterior abre otra con aviso · depende de: T-10
- [ ] T-12 · (US-16) Anular línea: 3 motivos grandes, casilla «Ya estaba cocinado», toast «Deshacer» 10 s, solo la dueña tras cobrar · hecho cuando anular repone exactamente el stock y deshacer lo vuelve a descontar · depende de: T-11
- [ ] T-13 · (US-14, US-15) K3 Mesas (libre / con comanda / por cobrar) y K4 Cobradas del día con filtro por método y resumen de cierre del día · hecho cuando el resumen suma lo cobrado por método · depende de: T-11

**Fase 4 · Dueña**
- [ ] T-14 · (US-06, US-11, US-12) A2 Inventario: alta con unidad sugerida y unidad de compra, «Llegó compra», merma de un toque, Recuento, aviso bajo mínimo, `sparkline` de consumo de 7 días · hecho cuando entrada, merma y recuento cuadran el histórico y un ingrediente bajo mínimo avisa en A2 · depende de: T-09
- [ ] T-15 · (US-07, US-08, US-09, US-10, US-21) A3 Platos y recetas: receta con medidas caseras, vista previa de yemas, «Oculto: faltan huevos» + «Añadir stock», «Sin control de stock», botón «Cargar plantilla de desayunos» (`aplicar_plantilla_desayunos`) · hecho cuando con la plantilla cargada y stock metido el menú ofrece los platos y el aviso de oculto explica la causa · depende de: T-14
- [ ] T-16 · (US-19) A4 Mesas y QR: crear mesa, token, «Regenerar QR» con confirmación, hoja de impresión A6 con `qrcode` · hecho cuando el QR impreso abre el menú de esa mesa y el regenerado invalida el antiguo · depende de: T-09
- [ ] T-17 · (US-19) Menú gestionable: CRUD de categorías y platos, alérgenos de los 14 de la UE, activar/desactivar, fotos en Supabase Storage (WebP ≤ 80 kB) · hecho cuando el ciclo crear → refrescar → editar → refrescar → borrar → refrescar pasa con el historial intacto · depende de: T-15
- [ ] T-18 · (US-17, US-18) Ampliar [[5 - Backend Schema]] con las funciones de métricas (`resumen_ventas`, ranking de platos, horas punta, consumo real frente a teórico y margen) y probarlas en PGlite con ejemplo numérico · hecho cuando las cifras de la semilla coinciden con las calculadas a mano · depende de: T-13, T-14
- [ ] T-19 · (US-17, US-18) A1 Panel financiero: `stat-card-area-01`, `bar-chart`, `area-chart` de Bklit, selector Hoy / 7 días / Mes, frases sencillas («Cada mesa gasta 14 € de media»), margen solo con costes cargados · hecho cuando muestra los estados «sin ventas» y «sin costes» y las cifras de T-18 · depende de: T-18
- [ ] T-20 · (US-19) A6 Ajustes: nombre de marca, logo, colores del tema (`restaurantes.tema`), umbral de «quedan» y opción de confirmación · hecho cuando cambiar el acento en A6 cambia el menú sin tocar código · depende de: T-04, T-09

**Fase 5 a 7 · Cierre**
- [ ] T-21 · (US-01) Imágenes: **decide Haytham hueco por hueco** (logo, fotos de platos, iconos de categoría, SVG de estados vacíos, ambiente del local). Hasta entonces, marcadores honestos de «pendiente», nunca imagen inventada · hecho cuando la tabla de [[3 - UI-UX Design]] §5 no tiene ninguna fila «pendiente» · depende de: T-04
- [ ] T-22 · (US-01, US-13, US-17) Verificación visual y de accesibilidad: 375/768/1280 px, `axe` a cero violaciones, Lighthouse, contraste, `prefers-reduced-motion`, texto mínimo 18 px y nada crítico girado; prueba del intercambio y de lejos · hecho cuando `rules/verificacion-web.md` está cumplido · depende de: T-19, T-20, T-21
- [ ] T-23 · (US-04, US-05, US-15, US-16) Pruebas de extremo a extremo (Playwright): ciclo crear → refrescar → anular → refrescar → cobrar → refrescar; dos pestañas pidiendo la última ración · hecho cuando pasan contra staging · depende de: T-12, T-13, T-25
- [ ] T-24 · (US-08) Revisión de seguridad: `supabase-postgres-best-practices` y `get_advisors` sobre las funciones `security definer`, `auditor-web` + `revisor-codigo` + `ponytail-audit` en paralelo · hecho cuando no queda ningún hallazgo alto · depende de: T-22
- [ ] T-25 · (US-04) **Con tu permiso**: crear proyecto Supabase de staging, aplicar migración, bucket `platos`, política de `realtime.messages`, `purgar_notas` programada, y probar la concurrencia real de `crear_pedido` · hecho cuando 20 pedidos simultáneos por 5 raciones dejan exactamente 5 aceptados · depende de: T-03
- [ ] T-26 · (US-13) **Con tu permiso**: despliegue a Vercel, variables de entorno, dominio, verificación en producción del ciclo completo, `resumen.html` y ficha final · hecho cuando la URL pública pasa T-23 · depende de: T-24, T-25

## 2.1 Starter kits reutilizados
Módulos de [[Starter Kits NeoZeler]] que se reaprovechan y su coste de adaptación:
| Kit | Fase | Adaptación |
|---|---|---|
| [[Starter SaaS]] (arnés PGlite de RLS, patrón de `proxy.ts`, `@supabase/ssr`) | 0, 1, 3 | Bajo: se copia el arnés; auth con roles propios (`miembros`) en vez de organizaciones |
| Dashboard base (tarjetas KPI y gráficas) | 4 | Medio: se rehace con Bklit sobre Motion y la identidad de Comanda Viva |
| TopLeads (`components.json` con los 7 registries) | 0 | Bajo: copia de configuración |

## 3. Estrategia de pruebas
- **Reglas de negocio en SQL** (disponibilidad, descuento, anular, cobrar, RLS): arnés PGlite, ya con 20 pruebas; se añaden las de `get_pedidos_mesa` y métricas.
- **Unitarias de código**: Vitest para Zod, cálculo de dividir cuenta y cambio, formato de céntimos.
- **Concurrencia real**: solo en Postgres real de staging (T-25); PGlite no la cubre.
- **Extremo a extremo (T-23)**: ciclo crear → refrescar → anular → refrescar → cobrar → refrescar **en producción**, y dos pedidos simultáneos por la última ración.
- **Cliente simulado** otra vez sobre la maqueta terminada: comensal, caja en hora punta y dueña.

## 4. Despliegue y operación
- **Entornos**: local (PGlite + Supabase local si hay Docker), staging y producción. No existe ningún proyecto en la nube: crearlos cuesta dinero y requiere tu permiso.
- **Variables**: `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`; `SUPABASE_SERVICE_ROLE_KEY` solo en servidor y nunca en el repo.
- **Dominio y marca blanca**: un dominio por cliente o subruta; la marca va en `restaurantes.tema`.
- **Backups**: copia diaria de Supabase y exportación mensual de ventas.
- **Monitorización**: avisos de Vercel y Supabase; `purgar_notas` diaria (notas a 90 días, RGPD).
- **Pendiente**: coste y plan de Vercel + Supabase sin verificar; decidir quién paga mientras el reparto con la clienta no esté cerrado.

## 5. Riesgos y plan B
> [!riesgo]
> - **Carrera de stock en Postgres real**: sin comprobarla en T-25 no se da el sistema por bueno. Plan B: `serializable` o cola por restaurante.
> - **Recetas imprecisas**: el stock deriva de la realidad. Mitigación: Recuento y merma (T-14); consumo real frente a teórico en el panel.
> - **Adopción de la dueña**: 40 ingredientes a mano la hacen abandonar. Mitigación: plantilla y medidas caseras (T-15); formarla en persona.
> - **Pedidos falsos**: límites del esquema + caja puede anular; opción `requiere_confirmacion` si hace falta.
> - **Realtime caído o bloqueado**: polling de 5 s (T-10).
> - **Fiscal**: v1 es control interno, **no** ticket fiscal. Comprobar VeriFactu antes de enlazar TPV.
> - **Huecos abiertos de este plan**: `get_pedidos_mesa` y las funciones de métricas aún no están en el doc 5 (T-07, T-18); la línea «Pagas al final» está sin confirmar con la clienta; imágenes sin decidir (T-21); reparto y cobro con la clienta sin cerrar.
> - **Parecido con ComandAi** (panel propio de Haytham): vigilar nombre y mensajes de marca.

## 6. Definición de terminado
- [ ] `trace_lint.py` en `RESULTADO: OK` y `schema_to_migration.py` sin avisos de FK
- [ ] Build y type-check limpios
- [ ] Checklist técnico/SEO y de marca
- [ ] Pruebas de intercambio y de lejos superadas; cero imágenes pendientes o inventadas; fila añadida a [[Registro de Identidades Visuales]]
- [ ] Concurrencia real probada en staging y ciclo completo verificado en producción
- [ ] README en el repo
- [ ] Ficha en `01_Projects/` y sesión registrada
- [ ] `.claude/COMMON_MISTAKES.md` actualizado

---
Anterior: [[5 - Backend Schema]]
