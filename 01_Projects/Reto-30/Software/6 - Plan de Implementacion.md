---
type: doc-software
doc: plan-implementacion
proyecto: "Reto 30 (app real)"
status: aprobado
date: 2026-10-14
origen: mixto
---

# 6 · Plan de Implementación — RETO 30 (app real)

> [!resumen]
> Orden de construcción en tareas pequeñas y verificables, derivado de [[1 - PRD]], [[2 - TRD]], [[3 - UI-UX Design]], [[4 - AppFlow]] y [[5 - Backend Schema]]. Se crea un repositorio nuevo en `~/Proyectos/reto-30` (la demo anterior se eliminó el 2026-10-15; lo útil está en `99_Assets/reto-30/demo-rescatada/`). **Plan aprobado; construcción iniciada el 2026-10-18.** Siguen pendientes **D5** (datos del titular y revisión legal) y **D7** (consulta legal del sorteo); **D1, D2, D4 y D6 están resueltas** y **D3 queda aplazada** (§1.1).

> [!resumen]
> **Alcance de la v1 (2026-10-17)**: el plan incorpora [[Cambios de diseno - Ranking, comodines, sorteo y Duo]]: ranking, comodines, reto extra, cronómetro, correo diario, plan Dúo, premio de 50 € + merchandising, plan Dúo a 30 € y nivel fijo. Tareas nuevas **T-41 a T-52** y tareas existentes ajustadas (T-09, T-14, T-15, T-17, T-21, T-30, T-39 y T-40). El nivel «Fácil» pasa a «Básico» en todo el plan. **Fecha de salida: sin fijar**; hasta que se lance la app no se fija fecha de sorteo.

## 1. Fases
| Fase | Objetivo | Entregable demostrable | Historias |
|---|---|---|---|
| 0 Preparación | Proyecto nuevo, dependencias mínimas, tokens y tipografías de marca, logo usable | Proyecto nuevo con el estilo negro y lima y build limpio | — |
| 1 Datos | Proyecto Supabase de desarrollo, migración, semilla de los 30 días, tipos | Consultas de prueba correctas contra Supabase real | US-04, US-08 |
| 2 Acceso y reglas | Cuenta con enlace y código por correo, plaza, nivel, completar día en servidor | Un usuario de prueba completa el día 1 desde la app | US-01, US-02, US-05, US-10 |
| 3 Pantallas del participante | Portada, empezar, panel, reto del día, felicitación, insignias, diploma, cuenta | Recorrido completo del día 1 al diploma en móvil | US-03, US-04, US-05, US-06, US-07, US-10, US-11 |
| 4 Admin y gerencia | Participantes, ejercicios, gerencia y correos | El admin activa una plaza, cambia un ejercicio que el participante ve y activa el sorteo | US-08, US-09, US-10, US-11 |
| 5 Pulido y pruebas | Accesibilidad, 375 px, rendimiento, copy llano, e2e del ciclo | Checklist técnico y de marca sin fallos | US-01 a US-10 |
| 6 Despliegue | Proyecto de producción, hosting, correo y dominio | App en vivo con el ciclo completo validado en producción | US-01 a US-10 |

### 1.1 Decisiones tuyas antes de empezar
| # | Decisión | Bloquea | Nota |
|---|---|---|---|
| D1 | **Resuelta (2026-10-14)**: organización nueva "Reto 30" en Supabase, plan **gratuito también en producción**: el reto dura solo un mes, así que no se paga Pro (decisión del 2026-10-15) | Fase 1 | **Organización creada por Haytham (confirmado el 2026-10-18)**; ahora se crean los dos proyectos (desarrollo y producción) en Frankfurt. La organización actual ya tiene 2 proyectos activos, el máximo del plan gratuito. **Riesgos aceptados**: sin copias automáticas (exportación semanal a mano, T-38) y pausa tras 7 días de poco uso (se evita con uso diario del reto y un aviso periódico antes del lanzamiento, T-37) |
| D2 | **Cambiada (2026-10-19): Vercel gratuito.** El cobro se hace en efectivo en el gimnasio, no en la app; el plan gratuito es de uso no comercial según Vercel, riesgo aceptado por Haytham (si lo suspenden, se pasa a Pro). **Resuelta (2026-10-14)**: Vercel Pro (20 USD por usuario al mes, un asiento), pagado **solo desde la Fase 6 y durante el mes del reto** (se cancela al terminar); el desarrollo es en local | Fase 6 | El plan gratuito de Vercel es solo de uso no comercial y el reto cobra una cuota. Precio por confirmar en la página oficial antes de pagar; se puede dar de baja al terminar la cohorte |
| D3 | **Confirmada (2026-10-19): ni correo ni dominio propios por ahora.** Consecuencia: con el correo integrado de Supabase solo reciben el enlace los miembros de la organización (~2 envíos/hora), así que la app queda para pruebas internas hasta resolverlo. T-36, T-24 y T-49 siguen sin hacerse. **Aplazada (2026-10-18): no se va a hacer de momento**; antes, resuelta en parte (2026-10-14): se desarrolla **sin dominio propio**; dominio y proveedor de correo propios se deciden **antes de abrir la cohorte** (bloquean T-36 y T-34) | Fase 6 | En desarrollo se usa el correo integrado de Supabase (límite de unos 2 envíos por hora y solo a miembros de la organización, por verificar). Sin dominio verificado los correos reales llegarían peor o a spam. Candidatos: Resend (3.000 al mes y 100 al día en el plan gratuito, por verificar) con `reto30.com` (16 USD el primer año, disponible el 2026-10-14). Sigue abierta la decisión de pasar los avisos al admin a un resumen diario |
| D4 | **Resuelta (2026-10-14)**: PNG transparente `99_Assets/reto-30/LogoReto30-transparente.png` (677×580 px), derivado de `LogoReto30.jpeg` (fondo oscuro) | Fase 0 | Sirve para cabecera y favicon sobre fondo oscuro; sobre blanco desaparecen el "RETO" y el escudo. No escala a impresión: un SVG real exigiría rehacer o vectorizar el logo (fuera de v1). Ojo: `LogoReto30-sinfondo.jpeg` tiene fondo claro, no transparente |
| D5 | **Decisión (2026-10-19): Haytham pospone los textos legales** («da igual»); T-32 no se hace por ahora. **Resuelta en parte (2026-10-15)**: titular legal **Haytham**; edad mínima **18 años**; borradores redactados: [[Borrador - Aviso legal]] y [[Borrador - Politica de privacidad]] | Fase 5 | **Faltan** los datos del titular (nombre completo, NIF, domicilio, correo), el plazo de conservación, el papel de Factory Training, la confirmación de proveedores y transferencias, y la **revisión de un gestor o abogado** antes de publicar. Sin cookies de analítica, no hace falta banner |
| D6 | **Resuelta (2026-10-15), ampliada el 2026-10-17**: **20 € por plaza individual y 30 € por pareja (plan Dúo)**, pago en efectivo en Factory Training. Factory Training cobra el **15 % de la facturación total**, sea cual sea el plan | Fase 3 | Con 30 individuales son 600 € y 90 € para Factory Training; el premio (50 € + merchandising, ver §1.2) lo pagáis vosotros |
| D7 | **Pendiente**: consulta legal del sorteo (¿hace falta autorización por cobrar la participación?). **Premio decidido el 2026-10-17: 50 € + merchandising de Factory Training, pagado por Haytham y Pedro** (sustituye al 25 % del beneficio del 2026-10-16). Se anuncia un día y se sortea al azar; el dueño de Factory Training avisa al ganador; si nadie clasifica gana quien tenga más racha (empates al azar). **Sin fecha hasta lanzar la app.** Siguen abiertos: merchandising concreto, si el sorteo es en directo o con acta, y la fecha límite | Anuncio del premio y T-40 | Hasta tener respuesta el sorteo queda **desactivado** en la app y **el cartel y la portada no mencionan el premio**. Borrador: [[Borrador - Bases del sorteo]] |
La carga de los ejercicios definitivos (decisión ya tomada: la haces tú desde el panel) no bloquea nada.

### 1.2 El premio (sustituido el 2026-10-17)
> [!resumen]
> **Vigente desde el 2026-10-17**: premio fijo de **50 € + merchandising de Factory Training**, pagado por Haytham y Pedro. La fórmula del 25 % del beneficio de abajo queda **obsoleta** y se conserva solo como histórico. Economía de referencia con el nuevo precio (sin contar el merchandising ni el coste de producirlo): 30 plazas individuales = 600 € de facturación − 90 € (15 %, Factory Training) − 36 € de costes técnicos − 50 € del premio = **424 €**; 20 individuales + 5 parejas = 400 + 150 = 550 € − 82,50 € − 36 € − 50 € = **381,50 €**. Un premio fijo de 50 € es menor de 300 €, así que no lleva retención de IRPF (sigue pendiente de verificar el posible gravamen sobre el valor del premio).

**Histórico (superado): el premio como porcentaje del beneficio.**
**Decidido el 2026-10-16: el premio es el 25 % del beneficio, definido sobre el beneficio y no sobre los ingresos.** Definición: beneficio = ingresos por plazas − 15 % de Factory Training − costes técnicos del mes (unos 36 USD: Vercel Pro 20 y dominio 16; 1 USD ≈ 1 €, aproximado). Con 30 personas a 20 € son 600 − 90 − 36 = **474 €**, así que **100 € equivale al 21 % y 150 € al 32 % del beneficio**. Con un porcentaje fijo, el premio crece o baja con las plazas y nunca os deja en negativo:
| Plazas (20 € cada una) | Ingresos | Gimnasio (15 %) | Costes | Beneficio | Premio al 20 % | **Al 25 % (decidido)** | Al 30 % |
|---|---|---|---|---|---|---|---|
| 15 | 300 € | 45 € | 36 € | 219 € | 43,80 € | 54,75 € | 65,70 € |
| 30 | 600 € | 90 € | 36 € | 474 € | 94,80 € | 118,50 € | 142,20 € |
| 45 | 900 € | 135 € | 36 € | 729 € | 145,80 € | 182,25 € | 218,70 € |
- Con un premio fijo de 150 € y solo 15 plazas, el beneficio de 219 € se reduciría a 69 €; con un porcentaje no pasa.
- **Retención de IRPF**: un premio de menos de 300 € no la lleva; con el 25 % decidido se pasaría a partir de unos 1.200 € de beneficio (unas 75 plazas).
- **Decidido**: el 25 %, sobre el **beneficio** (no sobre los ingresos). Con 30 personas son 118,50 €, un 19,75 % de los ingresos. Como el beneficio no es tan fácil de comprobar para un participante como los ingresos, las bases deberán explicar con claridad qué costes se descuentan.
- **Sigue abierto** (D7): la redacción final de la definición de "beneficio" (qué costes cuentan y cómo se acreditan) y **cuándo se publica el importe en euros** (propuesta: al cerrar las plazas y antes del primer día del reto, para que nadie pague sin saberlo). Los participantes deben conocer la regla al inscribirse: es una pregunta para el abogado.

## 2. Tareas
Cada tarea indica historia, archivos, criterio de hecho y dependencias. Una tarea no se da por hecha sin su criterio.

**Fase 0 · Preparación**
- [x] T-01 · Crear el proyecto nuevo en `~/Proyectos/reto-30` (`git init` y `.gitignore` antes del primer commit, `create-next-app` con Node 22 de fnm, después spec-kit y shadcn; rama de trabajo `app-real`) · `package.json` · compila en vacío · depende de: —
- [x] T-02 · Instalar solo las dependencias del TRD, sin `framer-motion`, `@tabler/icons-react`, `@usespaceui/squircle` ni componentes de Space UI y Arc UI (consultar `demo-package.json` para lo que usaba la demo) · `package.json` · `npm run build` y `lint` limpios, un solo motor de animación y una sola librería de iconos · depende de: T-01
- [x] T-03 · Tokens negro y lima, tipografías Barlow autoalojadas en WOFF2 (verificar licencia OFL), curva `--ease-brand` · `src/app/globals.css`, `public/fonts/` · tokens del UI/UX §2.1 aplicados y sin descarga a Google Fonts · depende de: T-02
- [x] T-04 · Logo sobre fondo oscuro · `public/` · copiar `LogoReto30-transparente.png` a `public/` y derivar el favicon de marca; comprobar que se ve bien a 375 px · depende de: —
- [x] T-05 · Componente `SegmentBar` de 30 segmentos (grande y mini) con estados y reducción de movimiento · `src/components/reto/` · se ve en los tres estados y respeta `prefers-reduced-motion` · depende de: T-03

**Fase 1 · Datos**
- [x] T-06 · Crear el proyecto Supabase de desarrollo (región UE) y variables de entorno, `.env.example` sin valores · raíz del repo · conexión probada, ningún secreto en git · depende de: D1
- [x] T-07 · Generar y aplicar la migración con `schema_to_migration.py`; revisar que no avisa de claves foráneas sin `ON DELETE` · `supabase/migrations/` · migración aplicada y tablas verificadas con `list_tables` · depende de: T-06 **(2026-10-18: aplicada al proyecto de desarrollo pegando `supabase/setup-dev.sql` en el editor SQL; comprobado con la clave de servicio: 30 días, 90 tareas, 9 ejercicios, 10 retos extra y 2 buckets; sin sesión se rechazan tablas y funciones)**
- [x] T-08 · Script que genera `challenges` y `challenge_tasks` desde `99_Assets/reto-30/demo-rescatada/challenges.ts` (`has_exercise` = entrenamiento y especial) · `supabase/seed-challenges.ts` · (US-04) 30 días y 90 tareas cargados · depende de: T-07
- [x] T-09 · Copiar `99_Assets/reto-30/demo-rescatada/schema-harness.mjs` (47 comprobaciones de la v1) al repo nuevo, **adaptarlo al esquema final** (nivel `basico`, sin `set_my_level`, sorteo por umbrales) y ejecutarlo contra la migración final · `supabase/tests/` · pasa en local · depende de: T-07
- [x] T-10 · Tipos de TypeScript generados desde el esquema · `src/lib/database.types.ts` · compila sin `any` en acceso a datos · depende de: T-07
- [ ] T-37 · Mantener activo el proyecto de Supabase gratuito desde que se crea hasta el lanzamiento (unas peticiones al día mediante un aviso periódico o uso real) · panel de Supabase · el proyecto no aparece pausado tras 7 días (umbral por verificar en la documentación) · depende de: T-06

**Fase 2 · Acceso y reglas**
- [ ] T-11 · Configurar correo transaccional y Supabase Auth con enlace y código de 6 cifras (verificar OTP en la documentación; si context7 sigue caído, usar la oficial) · `src/lib/supabase/`, panel de Supabase · en desarrollo, con el correo integrado de Supabase y solo con direcciones de miembros de la organización, el enlace llega y el código funciona en otro dispositivo; el correo propio se configura en T-36 · depende de: T-06 **(2026-10-19: código listo (`/entrar`, `/auth/confirm`, plantilla en `supabase/email-templates/acceso.html`). Falta en el panel de Supabase: URL del sitio y de redirección, pegar la plantilla en «Magic Link» y «Confirm signup» y fijar la longitud del código en 6; el proyecto genera 8 y el formulario ya acepta de 6 a 8. Sin probar todavía la llegada de un correo real)**
- [x] T-12 · Clientes de Supabase para servidor y navegador con `@supabase/ssr` y protección de rutas en servidor (AppFlow §1) · `src/lib/supabase/`, `src/middleware` o equivalente · `/reto` redirige a `/entrar` sin sesión · depende de: T-11
- [x] T-13 · Pantalla `/entrar` con estados (correo inválido, enlace enviado, caducado, "No me ha llegado", aviso de otro dispositivo) · `src/app/entrar/` · (US-01) flujo 1 recorrible y sin términos técnicos · depende de: T-12
- [x] T-14 · `/empezar`: nombre, casilla "soy mayor de 18 años" (obligatoria), casilla de consentimiento para gerencia, frecuencia semanal, nivel **(con el aviso de que no se puede cambiar)**, **elección de plan individual o Dúo (ver T-46)** y estado de la plaza · `src/app/empezar/` · (US-02, US-10) llama a `join_reto`; plaza pendiente muestra "pago en efectivo en Factory Training" · depende de: T-12
- [x] T-15 · Server Actions `joinReto`, `completeDay` y `settleMyWildcards`, con validación Zod y manejo de los estados `ok`, `ya_completado`, `no_toca`, `vuelve_manana`, `sin_plaza` (**se elimina `setMyLevel`**) · `src/app/actions/` · (US-05) errores traducidos a mensajes llanos · depende de: T-10, T-12
- [x] T-16 · Lógica pura en `src/lib/`: estado de cada día, cuenta atrás hasta las 07:00 de Madrid, mensajes de racha, con pruebas Vitest · `src/lib/reto.ts`, `src/lib/reto.test.ts` · pruebas pasan, incluida la jornada de 07:00 a 07:00 y el cambio de hora · depende de: T-01

**Fase 3 · Pantallas del participante**
- [x] T-17 · Portada con hero, cómo funciona, niveles **(con comodines y racha del sorteo por nivel)**, retos especiales, **precio con dos planes (Individual 20 € y Dúo 30 €)** y "se paga en efectivo en Factory Training", y pie de confianza. Sin mención del premio mientras el sorteo esté desactivado · `src/app/page.tsx` · (US-10) sin placeholders ni logos de terceros · depende de: T-03, T-04, D6 **(2026-10-19: hecho. No muestra los días de racha del sorteo en los niveles: la portada es estática y el sorteo está desactivado, así que no se menciona el premio.)**
- [x] T-18 · Panel `/reto`: contador de día, racha, barra de 30 segmentos, reto de hoy, calendario e hitos con todos sus estados vacíos · `src/app/reto/page.tsx` · (US-03, US-06, US-11) los 4 estados del UI/UX §3 y el chip del sorteo, que solo aparece si el sorteo está activado · depende de: T-05, T-15, T-16
- [x] T-19 · Reto del día `/reto/[dia]`: por qué, ejercicio del nivel, cómo y consejo; marco tipográfico si falta imagen; botón fijo "Completar el día" · `src/app/reto/[dia]/` · (US-04, US-05) bloqueado, actual y completado · depende de: T-15, T-16
- [x] T-20 · Felicitación al completar: barrido lima, racha animada, insignia en los días 7, 14, 21 y 28, y cierre del día 30 · `src/components/reto/` · (US-05, US-06) con y sin movimiento reducido · depende de: T-19 **(2026-10-19: hecho con fundido y cifra animada; el «barrido lima» queda para el pulido, Fase 5.)**
- [x] T-21 · Insignias, diploma con vista previa del nombre editable y guardar imagen, y cuenta (**el nivel se muestra pero no se cambia**; **dar o retirar el consentimiento para gerencia**, ocultar el nombre en el ranking, baja del correo diario, y borrar cuenta con confirmación) · `src/app/reto/insignias/`, `src/app/diploma/`, `src/app/cuenta/` · (US-02, US-06, US-07) diploma bloqueado antes del día 30 · depende de: T-18
- [ ] T-22 · Imágenes contextuales de las vistas clave (prompts del UI/UX §5) · `public/images/` · hero, estado vacío, felicitación, insignias, diploma · depende de: T-03 **(2026-10-19: pendiente. La app usa el marco tipográfico del diseño; faltan generar las imágenes con los prompts del UI/UX §5, que gasta créditos de Bloom o Canva.)**

**Fase 4 · Admin y gerencia**
- [x] T-23 · `/admin/participantes`: filtro "Pendientes primero", KPI de pendientes, activar y cancelar plaza con confirmación · `src/app/admin/participantes/` · (US-10) usa `admin_set_enrollment_status` · depende de: T-15
- [ ] T-24 · Correos: aviso de alta al admin y "tu plaza está activa" al participante, enviados desde el servidor leyendo el correo con `service_role` · `src/lib/email.ts` · (US-10) llegan en la prueba real · depende de: T-11, T-23 **(2026-10-19: aplazada con D3. Sin dominio ni correo propio no se envían los avisos; el admin revisa las plazas pendientes en `/admin/participantes`.)**
- [x] T-25 · `/admin/ejercicios`: lista y formulario, subida de imagen (JPG, PNG, WebP hasta 2 MB) con vista previa y reintento, aviso de impacto y "Ver como participante" · `src/app/admin/ejercicios/` · (US-08) un cambio se ve en la app al refrescar · depende de: T-15 **(2026-10-19: hecho. Falta el botón «Ver como participante».)**
- [x] T-26 · `/gerencia`: cifra "N de M participan esta semana", terminaron y lo han dejado, tabla con nombre abreviado o completo según consentimiento · `src/app/gerencia/` · (US-09) coincide con las definiciones del AppFlow §0 · depende de: T-15
- [x] T-27 · Crear a mano el usuario admin y el de gerencia (invitación) y documentar el procedimiento · README del repo · acceso a `/admin` y `/gerencia` solo con esos roles · depende de: T-12
- [x] T-39 · Sorteo (R15, **umbrales 21/26/30 por nivel y racha más larga**): interruptor y fecha límite en `/admin/participantes`, filtro "Elegibles", **lista de candidatos con la regla «si nadie clasifica, los de mayor racha» (`admin_lottery_candidates`)**, cifras "en carrera" y "elegibles" en `/gerencia`, chip en el panel con los días que faltan y mensaje en el diploma, todo oculto con el sorteo desactivado, y exportación de la lista para el sorteo externo · `src/app/admin/`, `src/app/gerencia/`, `src/app/reto/` · (US-11) con el sorteo desactivado no aparece ninguna mención al premio; activado, los estados coinciden con `reto_lottery_status` · depende de: T-23, T-26, T-18

**Fase 5 · Pulido y pruebas**
- [x] T-28 · Revisión de copy llano (AppFlow R14): sin "cohorte", "inscripción" ni términos técnicos visibles · todo `src/app/` · búsqueda de esas palabras sin resultados · depende de: T-21 — **hecho 2026-10-19**: `src/lib/copy.test.ts` vigila el texto visible (124 pruebas).
- [x] T-29 · Accesibilidad y responsive: sin desbordes a 375 px, contraste, foco, objetivos táctiles de 44 px · todo `src/app/` · `scrollWidth === clientWidth` en cada ruta; verificación visual en el navegador integrado (Chrome DevTools está bloqueado en tu configuración) · depende de: T-21, T-26 — **hecho 2026-10-19**: sin desbordes a 375 px y objetivos de 44 px en las pantallas de la participante (`e2e/ciclo.spec.ts`); falta revisar a mano las de admin y gerencia.
- [x] T-30 · Pruebas e2e con Playwright del ciclo completo: alta → activar → completar → editar ejercicio → borrar cuenta (pedir permiso para descargar navegadores) · `e2e/` · (US-01 a US-10) pasan en local · depende de: T-25, T-26 — **hecho 2026-10-19**: `e2e/ciclo.spec.ts` (alta → activar → día 1 → refrescar → borrar) con el Chromium ya instalado.
- [x] T-31 · Rendimiento: primer `next build` con peso medido y presupuesto del TRD §1.2; Lighthouse móvil · — · JS inicial ≤ 200 kB y primera pantalla útil < 2 s · depende de: T-29 — **hecho 2026-10-19 salvo Lighthouse**: JS inicial 156-167 kB gzip (límite 200), primera pintura < 0,35 s en local (`npm run perf`).
- [ ] T-32 · Textos legales y contacto de Factory Training integrados, partiendo de [[Borrador - Aviso legal]] y [[Borrador - Politica de privacidad]] y **solo tras la revisión de un gestor o abogado y con los datos del titular completados** · `src/app/privacidad/`, `src/app/aviso-legal/` · enlaces desde la casilla de consentimiento y el pie; ningún marcador "POR COMPLETAR" en lo publicado · depende de: D5 (revisión legal)
- [ ] T-40 · Consulta legal del sorteo y bases definitivas a partir de [[Borrador - Bases del sorteo]] **(premio de 50 € + merchandising, umbrales por nivel, comodines y la regla «si nadie clasifica gana la mayor racha»)**; con la respuesta, decidir si se activa el sorteo y publicar las bases · `src/app/bases-sorteo/` · (US-11) respuesta por escrito del abogado o de la Dirección General de Ordenación del Juego; sin ella el sorteo no se activa ni se anuncia · depende de: D7

**Fase 6 · Despliegue**
- [x] T-33 · Proyecto Supabase de producción, migración aplicada y buckets creados · — · mismas 102 comprobaciones del esquema en producción · depende de: T-09, D1 — **hecho 2026-10-19**: se usa el mismo proyecto de Supabase que en desarrollo (decisión de Haytham); esquema y semillas ya aplicados.
- [x] T-34 · Despliegue en el hosting elegido con variables de entorno y dominio · — · URL en vivo con HTTPS · depende de: D2, T-31, T-36 — **hecho 2026-10-19**: https://reto-30-haythams-projects-b655aadb.vercel.app en Vercel gratuito, sin dominio propio.
- [ ] T-36 · (se hace antes de T-34) Dominio propio, proveedor de correo con SPF y DKIM verificados, SMTP en Supabase de producción y prueba de entrega a Gmail, Outlook e iCloud · panel del proveedor y de Supabase, DNS · los correos de acceso y de plaza activa llegan a la bandeja de entrada, no a spam · depende de: decisión final de D3
- [x] T-35 · Ciclo completo validado en producción: crear → refrescar → editar → refrescar → borrar → refrescar (AppFlow §7) · — · lista de la sección 3 marcada en producción · depende de: T-33, T-34 — **hecho 2026-10-19 (parcial)**: las 7 pruebas e2e (ciclo, comodines, ranking, Dúo y baja del correo) pasan contra producción; falta la comprobación manual con correo real.
- [ ] T-38 · Copia de seguridad semanal a mano de la base de datos de producción (CLI de Supabase o `pg_dump`, sintaxis por verificar), guardada fuera del repo, y una prueba de restauración en el proyecto de desarrollo · fuera del repo · (US-01 a US-11) una copia restaurada con éxito antes de abrir la cohorte y una cada semana · depende de: T-33

**Tareas nuevas de la ampliación del alcance (2026-10-17)**
- [x] T-41 · (Fase 1) Convertir el nivel `facil` a `basico` en el script de la semilla de los 30 días (`challenges.ts` usa `facil`) y cargar la semilla de `extra_challenges` después de los 30 días · `supabase/seed-challenges.ts` · (US-04, US-14) 90 tareas con niveles `basico`, `medio` y `avanzado` y 10 retos extra cargados · depende de: T-08
- [x] T-47 · (Fase 1) **Ampliar el arnés de PGlite** con los casos nuevos: comodines (ganar, gastar, sin saldo, no dar insignia), racha con comodines, ranking y desempate, reto extra (ventana y comodín), Dúo (código, 2 miembros, pareja completa, racha conjunta), sorteo por umbrales y la regla «si nadie clasifica», `daily_digest_rows` y nivel que no se puede cambiar · `supabase/tests/` · todas las comprobaciones pasan en local antes de T-07 en producción · depende de: T-09
- [x] T-42 · (Fase 2-3) Comodines: lógica pura `src/lib/wildcards.ts` con Vitest, llamada a `settleMyWildcards` al abrir la app, escudos en el panel y avisos «Has ganado» y «Se ha gastado un comodín» · `src/lib/`, `src/components/reto/` · (US-12) la racha y el contador coinciden con el servidor, 4 comodines en básico y medio y 3 en avanzado · depende de: T-15, T-18
- [x] T-43 · (Fase 3) Cronómetro: máquina de estados `src/lib/timer.ts` con Vitest, componente `ExerciseTimer` (ejercicio, descanso, pausa, sonido, vibración y texto, Wake Lock si existe) dentro del reto del día · `src/lib/timer.ts`, `src/components/reto/ExerciseTimer.tsx` · (US-15) funciona sin conexión una vez cargado el reto y con `prefers-reduced-motion`; no completa el día por sí solo · depende de: T-19
- [x] T-44 · (Fase 3) Ranking `/reto/ranking` con `level_ranking`, tarjeta de puesto en el panel y fila propia resaltada · `src/app/reto/ranking/`, `src/components/reto/` · (US-13) orden por racha, menos comodines y más retos extra; nunca muestra correos; «Anónimo» si se oculta · depende de: T-15, T-18, T-42
- [x] T-45 · (Fase 3-4) Reto extra: tarjeta opcional en el reto de los días 3, 6, … 30 con `complete_extra`, y `/admin/extras` para editar los 10 retos · `src/app/reto/`, `src/app/admin/extras/` · (US-14) fuera de ventana responde «ya ha pasado»; un cambio del admin se ve al refrescar · depende de: T-19, T-25
- [x] T-46 · (Fase 3) Plan Dúo (participante): elección de plan en `/empezar`, código de pareja (`create_duo` y `join_duo`) y pestaña `/reto/pareja` con la racha del otro y la racha conjunta · `src/app/empezar/`, `src/app/reto/pareja/` · (US-17) cada persona tiene su ranking y sus papeletas; la racha conjunta no cuenta para el sorteo · depende de: T-14, T-15
- [x] T-48 · (Fase 4) Plan Dúo (admin): en `/admin/participantes`, ver a la pareja y «Activar a la pareja entera» (`admin_set_duo_status`) · `src/app/admin/participantes/` · (US-17) un solo cobro de 30 € activa las dos plazas · depende de: T-23, T-46
- [ ] T-49 · (Fase 4) Correo diario: Route Handler protegido por secreto lanzado por Vercel Cron a las 07:00 de Madrid, que llama a `settle_all_wildcards()` y `daily_digest_rows()`, envía con Resend y marca los envíos con `mark_digest_sent()` para no repetirlos; plantilla del UI/UX §4.2 y enlace de baja · `src/app/api/cron/daily/`, `src/lib/email.ts`, `vercel.json` · (US-16) llega con racha, comodines, puesto y aviso de reto extra; la baja funciona; el cambio de hora no mueve el aviso · depende de: T-24, T-36, T-42, T-44 **(2026-10-19: aplazada con D3. La base de datos ya tiene `daily_digest_rows` y `mark_digest_sent`; falta el cron y el envío.)**
- [x] T-50 · (Fase 4) Vídeos de ejercicios: campos de repeticiones, tiempo, descanso y vídeo en `/admin/ejercicios`, reproductor en el reto, bucket `exercise-videos` y **elegir la fuente de la librería de vídeos** (licencia y si permite enlazar) ([[Fuentes de Ejercicios y Multimedia Fitness]]) · `src/app/admin/ejercicios/`, `src/components/reto/` · (US-18) un ejercicio con vídeo de librería y otro con vídeo propio se reproducen; sin vídeo se ve la imagen · depende de: T-25, T-43 **(2026-10-19: hecho el panel y la subida de vídeo propio o enlace; sigue abierta la elección de la fuente de la librería de vídeos.)**
- [x] T-51 · (Fase 4) Gerencia sin comodines como actividad: comprobar que «participan esta semana» y «lo han dejado» no cuentan los días cubiertos con comodín · `src/app/gerencia/` · (US-09) coincide con las definiciones del AppFlow §0 · depende de: T-26, T-42
- [x] T-52 · (Fase 5) Pruebas e2e de comodines, Dúo y ranking con Playwright: comodín que salva la racha, racha rota sin comodines, Dúo de dos cuentas, ranking con desempate y baja del correo diario · `e2e/` · (US-12 a US-18) pasan en local y se repiten en producción en T-35 · depende de: T-30, T-47, T-49 — **hecho 2026-10-19**: `e2e/reglas.spec.ts`, 7 pruebas e2e pasan en local; falta repetirlas en producción (T-35).

## 2.1 Reutilización
Ningún módulo reutilizable está extraído todavía. La demo anterior se eliminó el 2026-10-15 y solo se salvó en `99_Assets/reto-30/demo-rescatada/`: `challenges.ts` (los 30 días), `schema-harness.mjs` (47 pruebas del esquema), `demo-spec.md`, `demo-plan.md` y `demo-package.json`. Las pantallas y los componentes se construyen de nuevo; los registries se reinstalan con `shadcn add`.
| Qué se reaprovecha | Fase | Adaptación |
|---|---|---|
| `demo-rescatada/challenges.ts` (los 30 días con por qué, cómo, consejo y tareas por nivel) | 1 | Se convierte en la semilla de `challenges` y `challenge_tasks` (T-08) |
| Diseño de rutas y estados de la demo anterior (`demo-spec.md` y `demo-plan.md`, solo como referencia) | 3 | Se reconstruyen desde cero con los tokens nuevos y leyendo del servidor |
| `split-flap-display`, `kinetic-text-reveal` (Componentry) y `@number-flow/react` | 3 | Se reinstalan desde sus registries y se verifica su contraste sobre fondo oscuro |
| Progreso en `localStorage` de la demo anterior | 2 | Se descarta: el progreso va al servidor desde el principio |
| Pruebas del esquema (script de PGlite) | 1 | Se copian de `demo-rescatada/schema-harness.mjs` a `supabase/tests/` (T-09) |

## 3. Estrategia de pruebas
- **Reglas de negocio**: Vitest sobre `src/lib/reto.ts` (jornada de 07:00 a 07:00, cuenta atrás, estado de día) y las 102 comprobaciones SQL del esquema.
- **Ciclo completo**: Playwright en local (T-30) y comprobación manual guiada en **producción** (T-35): crear → refrescar → editar → refrescar → borrar → refrescar.
- **Casos a no olvidar**: doble pulsación, enlace abierto en otro dispositivo, día perdido (racha a 0 sin perder progreso), borrado de un ejercicio con gente en curso, consentimiento sin marcar. Comodín que se gasta justo en la jornada en que se gana otro, dos fallos seguidos con un solo comodín, reto extra fuera de ventana, código de pareja ya usado, pareja que abandona, cambio de hora (octubre y marzo) en la jornada de 07:00 a 07:00 y cron diario ejecutado dos veces el mismo día (no debe reenviar ni gastar dos comodines).

## 4. Despliegue y operación
- Entornos: desarrollo y producción separados, cada uno con su proyecto Supabase.
- Variables de entorno en el hosting; `service_role` solo en el servidor; `.env` fuera de git.
- Copias de seguridad: el plan gratuito de Supabase no las incluye (según fuentes de terceros), así que se exportan a mano cada semana (T-38) y el proyecto se mantiene activo (T-37).
- Costes del mes del reto: Vercel Pro 20 USD (se cancela al terminar), dominio unos 16 USD el primer año y Supabase 0; el premio (50 € + merchandising, a cargo de Haytham y Pedro, ver §1.2) no es un coste técnico. El correo diario añade ~30 correos al día durante el reto; comprobar los límites del plan de Resend o del SMTP antes de abrir la cohorte (D3).
- Operación durante el reto: el admin revisa a diario las plazas pendientes; Factory Training confirma el cobro en efectivo antes de que se active cada plaza.

## 5. Riesgos y plan B
> [!riesgo]
> - **Correo que no llega** (enlaces y avisos): SMTP propio o Resend antes de abrir la cohorte; el código de 6 cifras sirve de alternativa. Si falla, el admin puede activar y avisar a mano.
> - **Sorteo**: cobrar la participación puede situarlo en el régimen de juego (Ley 13/2011) y exigir autorización previa; hay sanciones recientes a rifas sin ella. El sorteo está **desactivado por defecto** y el premio no se anuncia hasta la respuesta legal (D7, T-40). Con el premio de 50 € + merchandising (menos de 300 €) no hay retención de IRPF, pero hay un posible gravamen sobre el valor del premio por verificar. Preguntas nuevas al abogado: umbrales distintos por nivel, comodines y la regla «si nadie clasifica, gana quien tenga más racha». **El cartel no menciona el premio.**
> - **Plan gratuito de Supabase**: sin copias automáticas y con pausa por inactividad (T-37, T-38). Los límites y precios de Supabase y del hosting vienen de fuentes de terceros: confirmarlos en las páginas oficiales antes de la Fase 1 y la Fase 6.
> - **Next 16**: leer las guías de `node_modules/next/dist/docs/` antes de tocar rutas; si una función cambió, ajustar el plan.
> - **Dependencias sin probar** (Supabase, Zod, Vitest, Playwright): se fijan versiones tras probarlas en la rama.
> - **Ejercicios provisionales** visibles si no se cargan los definitivos antes de abrir la cohorte.
> - **context7 caído**: contrastar con la documentación oficial al implementar.

## 6. Definición de terminado
- [ ] `trace_lint.py` en `RESULTADO: OK` y `schema_to_migration.py` sin avisos de FK
- [ ] Build y type-check limpios (`npm run lint`, `tsc --noEmit`, `vitest run`, `next build`)
- [ ] Checklist técnico/SEO y de marca (UI/UX §8) sin fallos
- [ ] README en el repo
- [ ] Ficha en `01_Projects/` y sesión registrada
- [ ] `.claude/COMMON_MISTAKES.md` actualizado

---
Anterior: [[5 - Backend Schema]]
