---
type: referencia
status: propuesto
date: '2026-10-30'
proyecto: Barber.DF
tags:
- barber-df
- mejoras
- revision
origen: mixto
---

# Barber.DF — Propuestas de mejora

> [!resumen] En cristiano
> Revisé el código de `~/Proyectos/barber-df` (solo lectura: no se tocó nada del repo ni de lo desplegado). La web funciona y compila limpia, pero hay **3 fallos que conviene arreglar pronto** (reservas que se pueden saltar las reglas, recordatorios que nadie dispara, ajustes del barbero que no hacen nada) y varias mejoras pensadas para una barbería. Nada se aplica hasta que Haytham diga cuáles.

## 1. Qué se revisó
Repo completo (8.7k líneas), migración SQL, middleware, reservas, cancelación, cron de recordatorios, correos, service worker, tests. `tsc` sin errores; `eslint`: 19 errores y 28 avisos (casi todo comillas sin escapar e imports sin usar). No se ejecutó `build` ni se tocó Supabase/Vercel.

## 2. Fallos encontrados (por gravedad)

> [!riesgo]
> Estos puntos pueden afectar a lo que ya está desplegado. Cada arreglo es un cambio en producción: se hace solo con tu OK.

| # | Qué pasa | Dónde | Efecto real |
|---|---|---|---|
| A1 | `bookAppointment` **no valida** la hora: acepta `endsAt` que manda el navegador, sin comprobar horario, antelación ni duración del servicio | `src/app/reservar/actions.ts` | Alguien con conocimientos puede reservar fuera de horario, o una cita de 1 min / 10 h que bloquea la agenda |
| A2 | La política RLS `appointments_client_insert` deja a un cliente crear citas con **cualquier estado** (p. ej. `completed`) directo contra la base | migración 001 | Puede fabricar una cita "completada" y dejar una reseña verificada falsa |
| A3 | La acción sigue teniendo la rama "sin sesión" (crea usuarios con la clave admin) aunque la web ya exige login; además `listUsers()` solo mira la primera página | `reservar/actions.ts` | Reservar con el correo de otra persona y cambiarle nombre/teléfono; a partir de 50 usuarios, duplicados |
| B1 | **Nadie lanza el recordatorio**: no hay `vercel.json` ni cron configurado. Y si falta `CRON_SECRET`, el endpoint queda abierto | `api/cron/send-reminders` | La dirección privada (la gracia del negocio) no llega al cliente el día de la cita |
| B2 | Ventana "hoy" calculada en UTC (`T00:00Z`) y no en hora de Madrid | mismo archivo | Citas muy temprano/tarde pueden caer en el día equivocado |
| C1 | Ajustes del barbero (antelación mínima, días vista) **se guardan pero no se usan**: la reserva fija 1 h y 90 días | `actions.ts`, `BookingFlow.tsx` | El barbero cree que manda y no manda |
| C2 | Al cancelar, el cliente lee `barber_profile`, que RLS le bloquea → siempre usa 4 h; la política SQL también tiene 4 h fijas | `mis-citas/actions.ts` | `cancel_min_hours` no funciona |
| D1 | El bucket `barber-assets` (fotos) no está en ninguna migración; el `seed.sql` trae 6 servicios de 10–22 € frente a los 4 reales de 4–6,50 € | `supabase/` | No se puede reconstruir la base desde el repo |
| D2 | Registro con correo auto-confirmado, sin verificación | commit `1aa435e` | Cualquiera puede registrarse con un correo ajeno |
| D3 | Sin límite de citas activas por cliente ni freno anti-abuso | `reservar/actions.ts` | Un cliente puede acaparar huecos |

## 3. Propuestas de mejora

### Ahora (arreglan lo roto, bajo riesgo)
1. **Reservar con reglas en servidor**: calcular `endsAt` desde el servicio, comprobar que el hueco sale en `computeAvailableSlots` y respetar `min_lead_hours`/`max_future_days` de la base. Quitar la rama sin sesión.
2. **Cerrar el RLS**: insert de cita solo con `status='confirmed'` y duración correcta (o mover todo a una función SQL). Cancelación leyendo `public_barber_profile`.
3. **Programar el recordatorio** (cron de Vercel o el servidor Zorin con `CRON_SECRET` obligatorio) y calcular el día en Madrid. Añadir recordatorio **24 h antes** con botón de cancelar.
4. **Migraciones completas**: bucket + políticas de storage, y `seed.sql` igual al catálogo real.

### Pensado para una barbería
5. **Botón de WhatsApp** en la confirmación y en el aviso de cancelación tardía (el texto ya lo menciona, pero no hay número).
6. **Añadir al calendario** (enlace `.ics`/Google) en el correo de confirmación.
7. **Marcar "no vino"** y bloqueo suave tras 2 faltas (el estado `no_show` ya existe, falta usarlo).
8. **Repetir última cita** en un toque desde `/mis-citas` (cliente recurrente = lo que más vale).
9. **Lista de espera**: si un día está lleno, avisar por correo cuando se libere un hueco.
10. **Galería de cortes** y Instagram en la landing (prueba social; hoy solo hay foto del barbero).
11. **Tarjeta de fidelidad** (cada 10 cortes, uno gratis) con contador en `/mi-cuenta`.

### Calidad y mantenimiento
12. `npm test` real (hoy los tests se corren a mano con `tsx`) + CI en GitHub que ejecute `tsc`, `eslint` y tests.
13. Limpiar los 19 errores de lint; README real (hoy es el de `create-next-app`).
14. Dominio propio verificado en Resend (el remitente por defecto es `onboarding@resend.dev`, que puede ir a spam).
15. Procesos de la casa: marcador `.proyecto`, `COMMON_MISTAKES.md`, Ficha y Retro (hoy no existen).
16. Actualizar la ficha [[Barber-DF]]: dice Next.js 15 y reservas a 30 días; el repo es Next 16 y reserva a 90.

## 3b. Propuestas de UI y UX (añadido 2026-10-30)

> [!resumen] En cristiano
> La web ya tiene carácter (negro + verde lima, tipografía urbana) y el flujo de reserva es claro. Lo que le falta es **pulir lo que se ve en el móvil**: letra demasiado pequeña, un paso que sobra al reservar, y algunos detalles que quitan sensación de "marca seria". Son cambios solo de pantalla; no tocan la base de datos.

### Qué se midió
| Dato | Valor | Por qué importa |
|---|---|---|
| Textos de 9, 10 y 11 px | 78 usos (+251 `text-xs` de 12 px) | En móvil se lee mal; la mayoría de clientes entra desde el móvil |
| Gris tenue `#737373` sobre negro | 85 usos | Contraste justo por debajo de lo recomendado para texto pequeño |
| Color de marca `#BAF225` escrito a mano | 270 veces (el token `accent` se usa 0) | Cambiar la marca = tocar 270 sitios |
| Atributos `aria-` | 9 en todo el proyecto | Poca ayuda para lectores de pantalla |
| Botones tipo "link" de 12 px (`Cambiar Día`, `Atrás`) | varios | Zona táctil pequeña, fácil de fallar con el dedo |

### Reserva (lo que más vale)
1. **Fusionar "Día" y "Hora" en una sola pantalla**: al tocar un día aparecen las horas debajo. Hoy son 4 pasos y 2 pulsaciones más de las necesarias; el cliente de barbería quiere reservar en menos de 30 s.
2. **Quitar el paso "Ver Horas Libres"**: al elegir día ya se pasa solo; el botón extra confunde (¿hace falta pulsarlo?).
3. **Selector de día más corto**: hoy es un carrusel de 90 días con filtro por mes. Proponer **"Hoy · Mañana · Elegir otro"** + los próximos 14 días, y el calendario completo solo bajo demanda.
4. **Mostrar el primer hueco libre** en la tarjeta de cada servicio ("Próximo hueco: hoy 18:30") y un botón "Reservar el primero disponible".
5. **Horas agrupadas** en Mañana / Tarde y las ya ocupadas en gris (no ocultas) para que se vea que el día está lleno.
6. **Resumen con precio y dirección clara**: dejar el aviso de dirección privada como bloque propio (ahora va en letra de 11 px dentro de la tarjeta) y añadir "Se paga en el local" si es así.
7. **Pantalla de éxito**: botones grandes "Añadir al calendario" y "Abrir WhatsApp"; ya existe el enlace a Google Calendar, falta darle protagonismo.

### Visual y marca
8. **Subir la letra mínima a 13–14 px** (cuerpo y ayudas) y dejar 11–12 px solo para etiquetas en mayúsculas.
9. **Tokens de color en vez de hex**: usar `bg-accent`, `text-muted` (ya definidos en `globals.css`) y subir `#737373` a `#8A8A8A` para texto pequeño.
10. **Quitar emojis de las etiquetas** ("Elegir en calendario 📅"): rompen el estilo; el icono de `lucide` ya está al lado.
11. **Cabeceras de paso con un solo tipo de botón "volver"** (hoy hay "Cambiar Servicio", "Atrás", "Elegir otro día" y "Probar con otro día" con estilos distintos).
12. **Galería de cortes + Instagram** en la landing, y reseñas verificadas más arriba (prueba social antes del servicio).
13. **Logo en SVG** (hoy `logo.png` pesa 255 KB y `scissors-3d.jpg` 332 KB; sin optimizar en `public/brand`).

### Móvil y accesibilidad
14. **Zonas táctiles mínimas de 44 px** (el Navbar usa `min-h-[36px]`).
15. **Barra de reserva fija abajo** en la landing (solo móvil): botón "Reservar" siempre a mano.
16. **`aria-label`, `aria-current` en el paso activo y `role="status"` en errores** del flujo; foco al primer elemento de cada paso.
17. **Estados vacíos con imagen o ilustración** (sin citas, sin huecos): regla global §4 de "cero pantallas vacías".

### Panel del barbero
18. **Agenda "Hoy" primero**: abrir en la vista del día con las citas en lista y un toque para "Marcar llegada / No vino / Terminada".
19. **Acciones rápidas por cita**: llamar, WhatsApp y cobrar sin abrir detalle.
20. **Dividir `BarberAgenda.tsx` (842 líneas)** en componentes: hoy es difícil de mantener y de probar.

### Maquetas aprobadas por Haytham (2026-10-30)
Haytham dio por buenas dos maquetas, salvo la galería de la primera versión (los dibujos de cabezas no gustaron: se cambian por huecos para fotos reales). Siguen sin aplicarse al repo.
- Reserva en 3 pasos (propuestas 1-9): https://claude.ai/artifact/XnaAtrEWEzdMBSEHJXxDeW
- Landing y panel del barbero, con SVG propuestos (propuestas 10, 12, 13, 15, 18, 19): https://claude.ai/artifact/7nPMCoNFA4qbAPnnBA2fGv
- Pendiente para aplicar: fotos reales del barbero para la galería y su Instagram.

## 4. Preguntas abiertas
1. ¿Hacemos primero los fallos A1–A3 y B1 (recomendado) o prefieres empezar por mejoras visibles?
2. ¿Dónde corre el recordatorio: cron de Vercel (plan Hobby: 1 vez al día) o el servidor Zorin?
3. ¿Hay número de WhatsApp del barbero que mostrar?
4. ¿Se quiere señal/prepago (Bizum) para reducir faltas, o se descarta?
5. ¿Se aplican cambios de base (Supabase) directamente o primero en un proyecto de prueba?

## 5. Estado (2026-10-30)
Solo propuesta. **Ningún archivo del repo, de Supabase ni de Vercel fue modificado.**

