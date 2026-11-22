---
type: referencia
status: confirmada
date: '2026-10-15'
proyecto: '[[01_Projects/Reto-30/Reto 30 - App real|RETO 30 - App real]]'
tags:
- reto-30
- idea
- precios
- pase-duo
origen: mixto
---


# Idea — Pase Dúo (30 € para dos personas, una sola plaza)

> [!resumen]
> **Idea guardada el 2026-10-15; NO está aplicada al diseño aprobado.** Se vende por **plazas** y no por personas: aforo de 30 accesos. El **Pase Individual (20 €)** da entrada a 1 persona y consume 1 acceso; el **Pase Dúo (30 €)** da entrada a 2 personas, que comparten una misma plaza y consumen **1 solo acceso**. Para el usuario sale a 15 € por persona; para vosotros entran 30 € ocupando un solo cupo.

## La idea tal como se planteó
- **Cupo:** 30 accesos en total para vender.
- **Individual (20 €):** 1 persona, 1 acceso; quedan 29.
- **Dúo (30 €):** 2 personas (por ejemplo con un enlace de invitación), 1 plaza compartida; consume 1 acceso y quedan 29 aunque haya 2 usuarios dentro.
- **Incentivo:** el usuario paga 15 € por persona si invita a un amigo o pareja; vosotros ingresáis 30 € de golpe.

## Números (ejemplo con premio fijo de 150 €; el premio pasó a ser un porcentaje del beneficio, así que estas cifras subirían o bajarían con las plazas; costes de 36 €, 15 % para Factory Training, 1 USD ≈ 1 €)
| Escenario con 30 plazas vendidas | Ingresos | Gimnasio (15 %) | Personas dentro | Os queda tras premio y costes |
|---|---|---|---|---|
| 30 individuales | 600 € | 90 € | 30 | 324 € |
| 20 individuales + 10 dúos | 700 € | 105 € | 40 | 409 € |
| 30 dúos | 900 € | 135 € | 60 | 579 € |
Notas: el premio del sorteo no cambia aunque haya más gente. Con más personas, cada una tiene menos probabilidad de ganar, pero también hay más candidatas a completar los 30 días. Factory Training cobra por plaza vendida, no por persona: queda por acordar si el 15 % se aplica sobre los 30 € del dúo.

## Qué cambiaría en el diseño (no aplicado)
| Documento | Cambio necesario |
|---|---|
| [[1 - PRD]] | Nueva historia: invitar a otra persona a mi plaza; aforo máximo de plazas; precio dúo |
| [[4 - AppFlow]] | Flujo de invitación (enlace o código), estados de la plaza dúo (una pagada, dos personas), qué pasa si la segunda persona no se une o si una de las dos abandona; reglas del sorteo para cada persona |
| [[3 - UI-UX Design]] | Elegir tipo de pase en la portada y en `/empezar`; pantalla o bloque para invitar; panel del admin con la plaza y sus miembros |
| [[5 - Backend Schema]] | Hoy `enrollments` es una plaza por persona. Haría falta una tabla de **plazas** (tipo individual o dúo, estado, quién la activó) y que cada persona pertenezca a una plaza; el aforo se guardaría en `reto_settings`; las reglas de activación y cancelación pasarían a la plaza |
| [[6 - Plan de Implementacion]] | Tareas nuevas de modelo, invitación, aforo y pantallas |

## Decisiones que habría que tomar
1. **Una cuenta compartida o dos cuentas?** La idea original menciona las dos opciones. **Recomendación: dos cuentas, una plaza.** Con una sola cuenta compartida la racha, el progreso y el sorteo se mezclan y no se sabe quién cumple. Con dos cuentas cada persona tiene su racha, su diploma y su estado en el sorteo.
2. **¿Cada persona del dúo entra por separado en el sorteo?** Si es así, un dúo da dos opciones al premio por 30 €.
3. **Si una persona del dúo abandona**, la otra sigue; la plaza no se devuelve.
4. **Aforo duro de 30 plazas**: ahora el diseño no tiene tope; haría falta un límite que avise cuando se agoten.
5. **Cobro en efectivo:** el gimnasio tiene que saber si cobra 20 o 30 € y a nombre de quién. Haría falta una **referencia de plaza** que el participante muestre al pagar.
6. **Consentimiento y edad:** la persona invitada también tiene que ser mayor de 18 años y dar su propio consentimiento (cada cuenta lo hace en su alta).
7. **Datos de la invitada:** la política de privacidad debe cubrir que una persona aporta el correo de otra.

## Riesgos y matices
- **Sorteo:** más participantes por plaza no cambia el análisis legal pendiente (ver [[Borrador - Bases del sorteo]]), pero conviene mencionar el dúo en la consulta.
- **Precio:** el dúo baja el precio medio por persona a 15 €, lo que prueba el límite bajo de vuestra hipótesis de 15–20 €. Es una ventaja para medir interés, pero reduce el ingreso por persona.
- **Complejidad:** es una función de **versión 1.1**, no imprescindible para validar la hipótesis. Con una sola cohorte de un mes, también se puede **vender el dúo a mano** (dos cuentas individuales y un cobro de 30 € por pareja) sin tocar la app.

## Estado
Guardada como idea. Para llevarla al diseño hace falta tu aprobación, porque modifica documentos ya aprobados.

