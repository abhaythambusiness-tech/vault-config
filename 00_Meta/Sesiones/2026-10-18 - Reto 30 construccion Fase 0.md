---
type: sesion
date: '2026-10-18'
proyecto: '[[01_Projects/Reto-30/Reto 30 - App real]]'
tags:
- reto-30
- sesion
- construccion
origen: mixto
---

# 2026-10-18 · Reto 30: notas corregidas y Fase 0

## Qué se hizo
- Haytham aclaró que **no hay v2** (todo va en la v1), que el **1 de noviembre era un ejemplo**, que el **plan Dúo está confirmado**, que la **organización de Supabase está creada** y que **D3 (correo y dominio) se ignora de momento**.
- Se quitaron las marcas "v2" y la fecha en los seis documentos, el Plan, el MOC, la ficha, la nota 07 y la sesión del 17-oct. La nota `Cambios v2` pasó a [[Cambios de diseno - Ranking, comodines, sorteo y Duo]] y quedó aprobada; [[Idea - Pase Duo]] pasó a confirmada.
- **Fase 0 del Plan hecha (T-01 a T-05)** en `~/Proyectos/reto-30`, rama `app-real`: Next 16.4.1, dependencias del TRD, tokens negro y lima, Barlow autoalojada, logo, favicon y `SegmentBar` con 6 pruebas de Vitest. Lint, tipos y build limpios; comprobado en el navegador a 375 px sin desbordes.

## Aprendizajes
- `vitest@5` no se instala con npm 10 sin `--legacy-peer-deps` (y falta `vite` a mano). Detalle en `~/.claude/rules/librerias.md`.
- `.gitignore` de Next ignora `.env.example`: hay que añadir la excepción.
- Error propio apuntado: la fecha de ejemplo y la "v2" se dieron por ciertas (`COMMON_MISTAKES` #44).

## Pendiente
- **D3** aplazada (bloquea el correo propio y el despliegue final), **D5** (datos del titular y revisión legal) y **D7** (consulta legal del sorteo).
- Sin commit todavía en `~/Proyectos/reto-30`; falta pasar spec-kit (parte de T-01).
- Siguiente: Fase 1 (T-06 en adelante): proyecto Supabase de desarrollo y migración. Necesita las claves del proyecto, que van en `.env.local` y nunca en el repo.


## Fase 1 (parte local, misma sesión)
- Migración generada con `schema_to_migration.py` (12 tablas, sin avisos de FK) y semilla de los **30 días y 90 tareas** (`supabase/seed-challenges.ts`, nivel `basico`) más los 10 retos extra y 9 ejercicios provisionales.
- Arnés de PGlite copiado a `supabase/tests/` y ampliado: **102/102 comprobaciones** (las 47 de la v1 adaptadas más comodines, ranking, reto extra, Dúo, candidatos al sorteo y correo diario). `npm run db:test`.
- El conector de Supabase de esta sesión solo ve la organización antigua (Constructora y BarberDF): no se tocó. Falta crear el proyecto de desarrollo en la organización "Reto 30" y aplicar la migración (T-06, T-07, T-10).
- Trampa del arnés: `throws` devuelve la sesión a superusuario tras el primer error; hay que repetir `as(usuario)` antes de cada comprobación de permisos.

## Fase 1 cerrada (2026-10-19)
- Haytham pegó `supabase/setup-dev.sql` en el proyecto de desarrollo (organización "Reto 30") sin errores. Comprobado desde fuera con la clave de servicio: 30 días, 90 tareas, 9 ejercicios, 10 retos extra, 2 buckets; las tablas y `settle_all_wildcards` rechazan a quien no tiene sesión.
- Las claves se pegaron por error en `.env.example` (archivo versionable). Se movieron a `.env.local` (permisos 600, ignorado por git) y el example quedó vacío; no llegó a haber commit. La clave de servicio pasó por el chat: rotarla antes del despliegue de producción.
- Tipos generados con postgres-meta sobre PGlite (`src/lib/database.types.ts`), sin Docker ni `DATABASE_URL`.
- Pendiente de la Fase 1: T-37 (mantener activo el proyecto gratuito de Supabase). `DATABASE_URL` sigue vacía; solo hará falta para scripts contra la base real.

## Fase 2, parte 1 (2026-10-19)
- Hechos T-12 a T-16: clientes de Supabase y `proxy.ts`, `/entrar` (correo, código y reenvío a los 60 s), `/auth/confirm`, `/empezar` en tres pasos con plan Individual o Dúo y pantalla de estado de la plaza, Server Actions (`joinReto`, `completeDay`, `settleMyWildcards`, parejas) y lógica pura de jornadas (07:00 de Madrid, cambios de hora incluidos). 54 pruebas de Vitest, lint, tipos y build limpios.
- Probado con un usuario temporal creado con `generateLink` (sin enviar correos) y borrado después: enlace → sesión → `/empezar`; enlace usado o inválido vuelve a `/entrar`; alta con Dúo guardó perfil, plaza (medio, Dúo, pendiente) y pareja; recargar conserva el estado; salir cierra la sesión.
- Hallazgo: el proyecto genera códigos de **8 cifras**; el formulario acepta de 6 a 8 y el AppFlow decía 6.
- T-11 queda a medias: falta tu parte en el panel de Supabase (URLs, plantilla de correo en dos sitios y longitud del código) y probar un correo real.

## Fase 3, participante completo (2026-10-19)
- Hechos T-17 a T-21 y T-42 a T-46: portada, panel (racha, barra, comodines, calendario, hitos, puesto, chip del sorteo si está activado), reto del día con ejercicio por rotación, cronómetro (máquina de estados con 14 pruebas, sonido, vibración y pantalla encendida), reto extra, felicitación con insignia y comodín, ranking, pareja, insignias, diploma en canvas y cuenta con borrado. 68 pruebas de Vitest, lint, tipos y build limpios.
- Recorrido real en el navegador con usuarios temporales (todos borrados): día 1 y día 7 con insignia y comodín, reto extra, pareja con racha conjunta, diploma con los 30 días, ajustes de cuenta y borrado de cuenta (ciclo completo: crear, refrescar, borrar, refrescar). La base de desarrollo quedó a cero.
- Aprendizajes: en el navegador integrado el streaming de Next solo se revela con un fotograma pintado (hace falta una captura antes de leer); `usePathname()` fuera de Suspense rompe el build con `cacheComponents`; un archivo `"use server"` no puede exportar constantes.
- Decisión: la portada no muestra los días de racha del sorteo por nivel (el UI/UX lo pedía, pero es estática y el sorteo está desactivado; T-17 prohíbe mencionar el premio).
- Pendiente de la fase: T-22 (imágenes de las vistas clave: usan el marco tipográfico hasta generarlas) y el «barrido lima» de la felicitación (pulido). Sin commit todavía.

## Fase 4, admin y gerencia (2026-10-19)
- Hechos T-23, T-25, T-26, T-27, T-39, T-45 (admin), T-48, T-50 y T-51: `/admin/participantes` (cifras, filtros, activar o cancelar plazas, Dúo entero, sorteo con fecha límite, candidatos y CSV), `/admin/ejercicios` (con aviso de impacto y subida de imagen y vídeo desde el navegador), `/admin/extras`, `/gerencia` y el script `npm run staff:create` para crear admin y gerencia. 81 pruebas de Vitest, lint, tipos y build limpios.
- Recorrido real con usuarios temporales (todos borrados): una acción activó a las dos plazas del Dúo; sorteo activado con candidatos de respaldo y CSV; ejercicio creado, visible y borrado (avisó de 1 participante afectado); reto extra editado; gerencia con nombres abreviados y sin acceso a `/admin`; el admin sube a Storage y un participante es rechazado por RLS. Sorteo, ejercicios y extras quedaron como estaban.
- Aplazadas con D3 (correo y dominio): T-24 (avisos por correo) y T-49 (correo diario con cron). La base de datos ya tiene las funciones; falta el envío.
- Pendiente menor: botón «Ver como participante» en `/admin/ejercicios`, y elegir la fuente de la librería de vídeos (T-50). Sin commit todavía.

## Fase 5 (2026-10-19): commits y pulido

- **Commits** en `~/Proyectos/reto-30`, rama `app-real`, sin push: `95b35be` (fases 0 a 4 e interfaz móvil) y `a35812c` (fase 5).
- **T-28**: `copy.test.ts` falla si el texto visible usa jerga. **T-29/T-30**: Playwright con el Chromium de `~/.cache/ms-playwright` (sin descargas); el ciclo completo pasa en 20 s. **T-31**: JS inicial 156-167 kB gzip (límite 200), primera pintura < 0,35 s en local; Lighthouse sin ejecutar.
- **Aprendizajes**: la auditoría táctil encontró fallos reales que no se veían a ojo (botón «Salir» 32 px, `Button` por defecto 32 px, «Ver insignias» 20 px, desplegables 24 px): ahora `Button` es 44/44/48 px (default/sm/lg). Una regla global `summary {}` en `@layer base` no se aplicó; se puso `py-2.5` en cada `summary`. Localizadores de Playwright: `getByLabel("Tu nombre")` choca con la casilla de consentimiento (usar `getByRole("textbox")`), y «Hoy» exige `exact: true`.
- **Pendiente**: T-32 (D5), T-52 (e2e de comodines, Dúo y ranking), Lighthouse, revisión táctil de admin/gerencia, panel de Supabase (T-11) y Fase 6.
- **T-52 (2026-10-19)**: `e2e/reglas.spec.ts` cubre comodín que salva la racha, racha rota, ranking con desempate, Dúo (código, pareja completa, racha conjunta) y baja del correo diario; 7 pruebas e2e en total, commit en `app-real`. Aprendizajes: el aviso «se ha gastado un comodín» solo sale en la primera carga tras entrar (esperar la redirección, no recargar); el ranking cuenta a todas las plazas activas del nivel, así que cada prueba debe borrar sus usuarios (`afterEach`); el progreso pasado se siembra con jornadas antiguas en `progress`.

## Fase 6 (2026-10-19): despliegue en Vercel gratuito
- Decisiones de Haytham: sin correo ni dominio propios por ahora (D3), Vercel gratuito porque el cobro es en efectivo en el gimnasio (D2), el mismo proyecto de Supabase como producción (D1), textos legales después (D5), sorteo desactivado.
- URL en vivo: `https://reto-30-haythams-projects-b655aadb.vercel.app`; variables solo las dos públicas de Supabase; protección SSO de Vercel desactivada para que sea pública. Las 7 pruebas e2e pasan contra producción y no quedan usuarios de prueba.
- **Error propio**: `vercel deploy` no asignó `reto-30.vercel.app` (ya es de otra persona, una web de fútbol). Di por buena esa URL tras ver 200 y mis primeras pruebas e2e fallaron contra una web ajena (solo se enviaron tokens de acceso de usuarios sintéticos ya borrados). Regla: comprobar el título de la página y el alias real (`vercel alias ls`) antes de dar por válido un despliegue.
- Aviso: `vercel link` reescribió `.env.local` (añadió `VERCEL_OIDC_TOKEN`); se quitó. Antes de abrir: poner la URL en Supabase (Site URL y Redirect URLs), correo propio y rotar la clave `service_role`.

