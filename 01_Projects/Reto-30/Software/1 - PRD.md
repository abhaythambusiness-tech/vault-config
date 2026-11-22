---
type: doc-software
doc: prd
proyecto: "Reto 30 (app real)"
status: aprobado
date: 2026-10-14
origen: mixto
---

# 1 · PRD — RETO 30 (app real)

> [!resumen]
> **Qué**: la versión real de [[01_Projects/Reto-30/RETO 30 - MOC|RETO 30]], el reto de 30 días de Factory Training. Se construye **toda la estructura y la interfaz**, pero con solo **3 ejercicios por nivel** (9 en total). Haytham elegirá después qué ejercicios van en cada nivel, así que el contenido debe poder cambiarse sin tocar código. Se aprueba antes de pasar a [[2 - TRD]].

> [!resumen]
> **Alcance de la v1 (2026-10-17)**: se incorporan ranking por nivel, comodines de racha, reto extra, cronómetro de ejercicios, correo diario, plan Dúo, nuevo premio y nivel fijo. Origen y decisiones: [[Cambios de diseno - Ranking, comodines, sorteo y Duo]]. Lo que cambia respecto a la versión del 2026-10-14 está marcado como.

> [!cliente]
> **Proyecto propio de Haytham y su amigo Pedro** (no es un proyecto de NeoZeler) · **Cliente piloto**: Factory Training · **Precio**: 20 € por persona en el plan individual y **30 € por pareja en el plan Dúo** (decidido el 2026-10-17) · **Premio**: sorteo de **50 € + merchandising de Factory Training**, pagado por Haytham y Pedro (decidido el 2026-10-17; sustituye al 25 % del beneficio), entre quienes alcancen la racha mínima de su nivel: 21 días (básico), 26 (medio) y 30 (avanzado); mismas papeletas para todos. Sin fecha hasta lanzar la app · **Cohorte inicial**: 20–30 socios · **Reparto**: 15 % de la facturación total (cualquier plan) para el gimnasio / el resto para Haytham y Pedro, de lo que sale el premio (reparto entre ambos por definir; [[01_Projects/Reto-30/01 - Propuesta y Modelo de Negocio|modelo de negocio]]).
> **Parte de lo ya hecho**: existió una demo con los 30 días, niveles, racha y diploma, y el estado solo en el navegador; **se eliminó el 2026-10-15**. Sus 30 retos y las pruebas del esquema se salvaron en `99_Assets/reto-30/demo-rescatada/`. Este proyecto construye el producto real desde cero.

## 1. Problema
- Los socios de un gimnasio abandonan por falta de constancia, no por falta de información; cuando se dan de baja el gimnasio pierde el ingreso recurrente.
- Hoy no existe nada guiado entre sesiones: el socio entrena (o no) solo y sin seguimiento. Cifras de abandono de Factory Training: **sin dato todavía** (pedirlas a gerencia).
- Una solución con el progreso solo en el navegador, como era la demo anterior (eliminada), lo guarda en `localStorage`: si el socio cambia de móvil o borra datos, pierde su racha, y Factory Training no puede ver nada.

## 2. Usuarios y roles
| Rol | Quién es | Qué necesita | Frecuencia de uso |
|---|---|---|---|
| Participante | Socio de Factory Training, sobre todo quien no suele hacer deporte; usa el móvil. En el plan Dúo son **dos participantes, cada uno con su propia cuenta** | Entrar sin fricción, ver el reto de hoy según su nivel, hacer el ejercicio con cronómetro, marcarlo, sentir progreso y ver su puesto | Diaria, 2–5 min |
| Gerencia / entrenador | Responsable de Factory Training | Saber cuántos socios participan y cuántos siguen | Semanal |
| Admin (Haytham y Pedro) | Haytham o Pedro | Cambiar ejercicios, textos y niveles sin programar | Puntual, al cargar contenido |

## 3. Objetivos y métricas de éxito
| Objetivo | Métrica | Valor actual | Meta (propuesta, a confirmar) |
|---|---|---|---|
| Validar que pagan por el reto | Plazas activadas (pagadas en efectivo en el gimnasio) en el primer grupo | 0 | 20–30 |
| Retención al inicio | % de inscritos que completan el día 7 | sin dato | ≥ 60 % |
| Finalización | % que completa los 30 días | sin dato | ≥ 40 % |
| Contenido editable | Cambiar un ejercicio y verlo en la app | no posible | < 2 min, sin desplegar |

## 4. Historias de usuario (priorizadas)
| ID | Como… | Quiero… | Para… | Prioridad (MoSCoW) |
|---|---|---|---|---|
| US-01 | Participante | crear mi cuenta y entrar sin fricción | conservar mi progreso en cualquier dispositivo | Must |
| US-02 | Participante | elegir mi nivel (Básico, Medio, Avanzado) al empezar; **no se puede cambiar a mitad del reto** | que el reto se ajuste a mi capacidad y las reglas de comodines y ranking sean justas | Must |
| US-03 | Participante | ver un panel con mi día actual, racha y calendario de 30 días | saber dónde voy y qué me queda | Must |
| US-04 | Participante | ver el reto de hoy con su "por qué", "cómo" y consejo, y su ejercicio de mi nivel | entender qué hago y evitar lesiones | Must |
| US-05 | Participante | marcar el día como completado y recibir felicitación y racha | sentir recompensa inmediata y desbloquear el siguiente día | Must |
| US-06 | Participante | superar los 4 retos especiales semanales y ganar insignias | tener hitos que me motiven | Should |
| US-07 | Participante | obtener un diploma digital al día 30 y compartirlo | celebrar el logro y difundir el reto | Should |
| US-08 | Admin | crear y editar ejercicios (nombre, nivel, descripción, media) desde un panel | cambiar el contenido sin tocar código | Must |
| US-09 | Gerencia | ver cuántos participantes hay y cuántos siguen activos | medir si el reto retiene a los socios | Should |
| US-10 | Participante | reservar mi plaza (el pago se hace en efectivo en Factory Training) | acceder al reto cuando el gimnasio la active | Must |
| US-11 | Participante | saber si sigo en carrera para el sorteo del premio (racha mínima de mi nivel: 21, 26 o 30 días); y como admin, ver quiénes son elegibles | entender las reglas y poder organizar el sorteo fuera de la app | Should |
| US-12 | Participante | ganar **comodines** (uno cada 7 días en básico y medio, cada 10 en avanzado) que se gastan solos al fallar un día y lo dan por cumplido | no perder la racha por un fallo puntual | Must |
| US-13 | Participante | ver el **ranking de mi nivel** con nombre, racha, comodines gastados y retos extra, y mi puesto | compararme y motivarme | Should |
| US-14 | Participante | hacer un **reto extra opcional cada 3 días** | sumar puntos de desempate | Could |
| US-15 | Participante | usar un **cronómetro** en el ejercicio (repeticiones, tiempo límite y descanso) | saber cuánto tiempo tengo y cuándo descansar | Must |
| US-16 | Participante | recibir un **correo cada día** con el reto, mi racha, mis comodines, mi puesto y el aviso del reto extra | no olvidarme del reto | Should |
| US-17 | Pareja | contratar el **plan Dúo** (30 €), con cuenta propia cada uno, ver la racha del otro y una racha conjunta | motivarnos entre los dos sin mezclar ranking ni sorteo | Should |
| US-18 | Admin | ver los vídeos de la librería de ejercicios y subir el mío si el ejercicio no existe, y programar repeticiones, tiempo y descanso de cada ejercicio | que el cronómetro y los vídeos salgan del panel, sin tocar código | Must |

## 5. Requisitos funcionales
- RF-01: registro e inicio de sesión con persistencia del progreso en servidor (US-01).
- RF-02: niveles Básico, Medio y Avanzado; el nivel se elige al empezar y **queda fijo durante todo el reto** (US-02).
- RF-03: calendario de 30 días con estados bloqueado, actual y completado, racha y barra de progreso (US-03).
- RF-04: vista del reto del día con "por qué", "cómo", consejo y ejercicio del nivel del participante (US-04).
- RF-05: completar el día solo si es el actual; felicitación, suma de racha y desbloqueo del siguiente (US-05).
- RF-06: 4 retos especiales semanales con insignia coleccionable (US-06).
- RF-07: diploma e insignia final, descargables o compartibles, solo con los 30 días completados (US-07).
- RF-08: el **contenido de ejercicios es dato, no código**: se edita desde un panel de administración, y la app arranca con **3 ejercicios por nivel** (US-08).
- RF-09: los 30 días del calendario funcionan completos aunque haya solo 9 ejercicios: los días de entrenamiento reutilizan los ejercicios del nivel por rotación hasta que se carguen más (US-04, US-08).
- RF-10: panel de gerencia de solo lectura con inscritos, activos y finalizados (US-09).
- RF-11: reserva de plaza con estados pendiente, activa o cancelada; el pago es en efectivo en Factory Training y la app no gestiona ningún pago (US-10).
- RF-12: un admin activa o cancela plazas desde un panel y el participante recibe un correo al activarse (US-10).
- RF-13: la app calcula si cada participante está **en carrera** o es **elegible** para el sorteo: su **racha más larga** (comodines incluidos) alcanza el umbral de su nivel, **21 días (básico), 26 (medio) o 30 (avanzado)**, dentro de una fecha límite configurable. Lo muestra al participante solo cuando el sorteo está activado y da al admin la lista de elegibles. **Si nadie es elegible**, da al admin los participantes con la racha más larga de todos los niveles (los empates se sortean al azar fuera de la app). Mismas papeletas para todos los elegibles. **La app no realiza el sorteo, no entrega el premio ni avisa al ganador**: lo avisa el dueño de Factory Training (US-11).
- RF-15: **comodines**. Se ganan uno por cada 7 días cumplidos (básico y medio) o cada 10 (avanzado). Si pasa una jornada sin completar el día y queda algún comodín, se gasta solo, ese día se da por cumplido y la racha sigue. Sin comodines, la racha vuelve a 0 y el progreso se conserva (US-12).
- RF-16: **ranking por nivel** con puesto, nombre (nombre de pila + inicial del apellido; quien lo oculte aparece como «Anónimo»), racha, comodines gastados y retos extra cumplidos. Orden: más racha, luego **menos comodines gastados**, luego **más retos extra**. Nunca se muestra el correo (US-13).
- RF-17: **reto extra opcional** cada 3 días (días 3, 6, 9… 30), con contenido editable desde el panel de admin; cuenta para el desempate del ranking (US-14).
- RF-18: **cronómetro** en el ejercicio con repeticiones, tiempo límite y descanso programados por el admin para cada ejercicio. El día se da por completado cuando la persona lo **marca a mano** tras acabar; el cronómetro no demuestra el cumplimiento (US-15).
- RF-19: **correo diario** a las 07:00 (hora de Madrid) a cada participante con plaza activa: reto del día, racha, comodines que quedan, puesto en el ranking y aviso de reto extra si toca. Con enlace de baja visible en `/cuenta` y en el propio correo (US-16).
- RF-20: **plan Dúo**. Dos personas, dos cuentas independientes (cada una con su racha, comodines, ranking y papeletas del sorteo), unidas por un código de pareja. Una pestaña de pareja muestra la racha del otro, si ya hizo el reto de hoy y una **racha conjunta** (días en que ambos cumplen, comodines incluidos) que **no cuenta para el sorteo**. Se paga una sola vez, 30 €, en efectivo en Factory Training (US-17).
- RF-21: cada ejercicio admite **vídeo**: primero el de la librería de ejercicios ya hechos ([[Fuentes de Ejercicios y Multimedia Fitness]]) y, si el ejercicio no existe, un vídeo propio grabado por Haytham y Pedro (US-18).
- RF-14: casilla obligatoria "soy mayor de 18 años" al registrarse y posibilidad de dar o retirar el consentimiento para gerencia desde la cuenta (US-01, US-09).

## 6. Requisitos no funcionales
- Móvil primero (el reto se consume en el teléfono), usable desde 375 px sin desbordes.
- Acceso diario en menos de 3 toques desde la apertura.
- Español de España; accesibilidad AA y respeto de `prefers-reduced-motion`.
- Carga rápida: primera pantalla útil en menos de 2 s con conexión 4G.
- Datos personales mínimos (nombre y correo) bajo RGPD; ningún secreto en el repositorio.

## 7. Fuera de alcance (v1)
- La biblioteca completa de ejercicios y su grabación en vídeo: se graban solo algunos ejercicios clave más adelante ([[01_Projects/Reto-30/03 - Contenidos y Produccion Audiovisual|decisión del 2026-10-14]]).
- Comunidad y chat. (El ranking por nivel entra en la v1, RF-16.)
- App nativa para tiendas.
- **Realizar el sorteo, avisar al ganador y entregar el premio**: la app solo identifica a los elegibles (RF-13); el sorteo se hace fuera, se anuncia un día y se hace al azar, el dueño de Factory Training avisa al ganador, con bases públicas y **tras la consulta legal previa** (ver riesgos). Sin fecha hasta lanzar la app. Tampoco se gestiona la emisión de descuentos reales en Factory Training (se anuncian, no se gestionan).
- Cualquier pago dentro de la app (Stripe, n8n, etc.): la cuota se cobra en efectivo en Factory Training y la app no gestiona pagos. La [[01_Projects/Reto-30/06 - Automatizacion de Inscripciones (n8n)|nota 06]] queda obsoleta para esta versión.

## 8. Riesgos y supuestos
> [!riesgo]
> - **Ejercicios provisionales visibles al público**: si el piloto sale con solo 9 ejercicios repetidos, el usuario lo notará. Mitigación: Haytham carga los definitivos antes de abrir la cohorte.
> - **Supuesto**: los textos "por qué / cómo / consejo" de los 30 días de la demo eliminada, salvados en `challenges.ts`, se reaprovechan; solo los ejercicios concretos se reducen a 3 por nivel.
> - **Supuesto**: gerencia aprueba el canal de difusión y las recompensas (pendiente de validar).
> - **Sorteo con participación de pago**: cobrar por participar puede colocar el sorteo en el régimen de juego (Ley 13/2011) y exigir autorización previa, salvo que encaje como sorteo promocional sin sobreprecio. **No se anuncia el premio hasta consultar a un abogado o a la Dirección General de Ordenación del Juego.** Con el diseño final el premio es de **50 € + merchandising** (menos de 300 €: sin retención de IRPF, con un posible gravamen sobre el valor del premio por verificar). Preguntas nuevas para el abogado: umbrales distintos por nivel, comodines y la regla «si nadie clasifica, gana quien tenga más racha». Borrador de [[Borrador - Bases del sorteo|bases]] preparado, sin revisión legal.
- **Comodines**: con 4 comodines un participante de nivel básico puede llegar a 21 días de racha habiendo fallado hasta 4 días; es una decisión de diseño, no un fallo. La penalización de los comodines gastados está en el desempate del ranking.
- **Correo diario**: exige proveedor de correo propio con SPF y DKIM antes de abrir la cohorte (D3); sin él los correos pueden caer en spam o superar los límites del plan gratuito. Debe haber baja sencilla (RGPD).
- **Vídeos de la librería**: verificar licencia, atribución y si permite incrustar o enlazar antes de usarlos ([[Fuentes de Ejercicios y Multimedia Fitness]]).
- **Plan Dúo**: si una de las dos personas abandona, la otra sigue sola con su racha y su cuenta; la racha conjunta se queda parada.
> - **Licencias**: si se usan imágenes de datasets de ejercicios, verificar licencia y atribución ([[Fuentes de Ejercicios y Multimedia Fitness]]).

## 9. Criterios de aceptación globales
- [ ] Un participante nuevo recorre registro → nivel → día 1 → completar → día 2 → … → diploma con solo 9 ejercicios cargados.
- [ ] Cambiar un ejercicio en el panel admin se refleja en la app tras refrescar, sin desplegar.
- [ ] El progreso se conserva al cambiar de dispositivo.
- [ ] Ciclo completo validado en producción: crear → refrescar → editar → refrescar → borrar → refrescar.
- [ ] Sin desbordes a 375 px en ninguna ruta.
- [ ] Un día fallado con comodín disponible se da por cumplido y la racha sigue; sin comodines la racha vuelve a 0 y el progreso se conserva.
- [ ] El ranking de cada nivel ordena por racha, luego menos comodines gastados, luego más retos extra, y no muestra correos.
- [ ] El cronómetro cuenta el tiempo y el descanso de un ejercicio con sus valores programados y se puede usar sin conexión una vez cargado el reto.
- [ ] Una pareja del plan Dúo tiene dos cuentas independientes, cada una con su ranking y su estado en el sorteo, y la racha conjunta no cuenta para el sorteo.
- [ ] El correo diario llega a las 07:00 con racha, comodines, puesto y aviso de reto extra, y la baja funciona.

## 10. Demo provocadora (reunión 1)
**Atención:** la demo anterior se eliminó el 2026-10-15, así que para la reunión hay que preparar una demo nueva con la marca negro y lima. Para la reunión con Factory Training:
- **Pantalla que provoca la reacción**: el panel con el calendario de 30 días y la racha, y la felicitación al completar un día.
- **Quién la ve**: gerencia y un par de entrenadores; los socios no deberían ver aún la plataforma.
- **Datos sintéticos**: nombres y niveles ficticios de socios, para enseñar también el futuro panel de gerencia (US-09).
- **Qué preguntar**: qué recompensa real aceptan, cómo la difunden y cuántos socios creen que se apuntarían.
- Si los operarios o entrenadores rechazan el móvil como canal: no aplica aquí, el uso es del socio.

---
Siguiente: [[2 - TRD]]
