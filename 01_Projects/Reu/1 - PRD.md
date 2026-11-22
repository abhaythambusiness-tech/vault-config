---
type: doc-software
doc: prd
proyecto: Reu
status: aprobado
tipo: a-medida
date: '2026-11-13'
origen: mixto
---

# 1 · PRD — Reu

> [!resumen] En cristiano
> **Reu** es una extensión de Chrome que, mientras estás en una reunión de Google Meet, copia los subtítulos que Meet ya muestra y los guarda como texto en tu propio ordenador. Después abres un panel con todas tus reuniones, lees cada conversación y la exportas. Sin IA, sin resúmenes, sin cuentas, sin pagar nada. Es una réplica pequeña de lo que hace Tactiq, hecha desde cero.
> **Decisión que te toca**: confirmar el alcance de la v1 (§4 y §7) y de quién es el proyecto (§8).

## 1. Problema
- Las reuniones de Meet se dicen y se pierden. Para recuperar lo hablado hay que acordarse o pagar una herramienta (Tactiq, Otter) que además guarda tus conversaciones en su nube.
- Hoy: sin transcripción, o Tactiq (de pago para casi todo, datos fuera de tu control).

## 2. Usuarios y roles
| Rol | Quién es | Qué necesita | Frecuencia |
|---|---|---|---|
| Único | Haytham (uso personal, reuniones con clientes y equipo) | Tener el texto de cada reunión y poder buscarlo y exportarlo | Varias veces por semana |

## 3. Objetivos y métricas de éxito
| Objetivo | Métrica | Meta |
|---|---|---|
| Capturar sin esfuerzo | Reuniones guardadas sin tocar nada tras entrar | 100 % de las que tengan subtítulos activos |
| Texto fiable | Frases perdidas o duplicadas en una reunión de 30 min | Pocas (menos de 2 %) |
| Recuperar rápido | Tiempo desde abrir el panel hasta encontrar una frase | Menos de 15 s |
| Coste | Euros al mes | 0 |

## 4. Historias de usuario
| ID | Como… | Quiero… | Para… | Prioridad |
|---|---|---|---|---|
| US-01 | usuario | que al entrar en una reunión de Meet se empiece a guardar la conversación | no olvidarme de activarlo | Must |
| US-02 | usuario | ver en la propia página de Meet que se está capturando, con botón de pausa | saber el estado y poder parar | Must |
| US-03 | usuario | que cada frase quede con quién la dijo y la hora | entender la conversación | Must |
| US-04 | usuario | un panel con la lista de mis reuniones (título, fecha, duración, nº de frases) | encontrar la que busco | Must |
| US-05 | usuario | abrir una reunión y leerla entera | recuperar lo que se habló | Must |
| US-06 | usuario | exportar una reunión a `.txt`, `.md` y `.json`, y copiarla al portapapeles | llevarla a otra herramienta o al vault | Must |
| US-07 | usuario | buscar texto dentro de todas mis reuniones | hallar «lo del presupuesto» sin recordar cuándo | Should |
| US-08 | usuario | borrar una reunión | quitar lo que no quiero conservar | Should |
| US-09 | usuario | que la extensión active sola los subtítulos de Meet | no depender de pulsar CC | Could |
| US-10 | usuario | exportar todas las reuniones de una vez | copia de seguridad | Could |

## 5. Requisitos funcionales
- RF-01: detectar la página de una reunión de Meet (`meet.google.com/xxx-xxxx-xxx`) y observar el bloque de subtítulos.
- RF-02: unir las actualizaciones parciales de una misma frase en una sola línea (Meet reescribe el texto mientras la persona habla).
- RF-03: guardar por reunión: título, código, fecha de inicio y fin, participantes, frases (quién, texto, hora).
- RF-04: panel (página de la extensión) con lista, vista de detalle, búsqueda, borrado y exportación.
- RF-05: exportaciones `.txt` (legible), `.md` (con cabecera de la reunión) y `.json` (datos completos).

## 6. Requisitos no funcionales
- Todo se guarda **en local** en el navegador (IndexedDB). Sin servidor, sin cuenta, sin enviar nada fuera.
- Idioma de la interfaz: español. El texto sale en el idioma que Meet esté subtitulando.
- Solo Chrome de escritorio. Permisos mínimos: `meet.google.com`, almacenamiento.
- Aguanta reuniones de 2 h sin ralentizar la pestaña.

## 7. Fuera de alcance (v1)
- Resúmenes, tareas pendientes o cualquier IA.
- Zoom, Teams y móvil.
- Grabar audio o vídeo.
- Sincronizar entre ordenadores o compartir con otras personas.
- Publicar en Chrome Web Store (uso personal, se instala como extensión sin empaquetar).

## 8. Riesgos y supuestos
> [!riesgo]
> - **Meet cambia su página por dentro** y la extensión deja de leer los subtítulos. Mitigación: un único fichero con los selectores, y aviso visible si no encuentra subtítulos.
> - **Solo se captura lo que Meet subtitula**: hay que tener los subtítulos activos (US-09 lo automatiza) y Meet no los muestra en todos los idiomas.
> - **Avisar a los participantes** de que se transcribe: en muchos países es obligatorio. Responsabilidad de Haytham; la extensión muestra un indicador pero no avisa a los demás.
> - **Supuesto sin confirmar**: el proyecto es personal de Haytham, no de NeoZeler.

## 9. Criterios de aceptación globales
- [ ] Entro en una reunión real de Meet, activo subtítulos, hablo 5 min con otra persona y la reunión aparece en el panel con las frases correctas.
- [ ] La exportación `.md` pegada en el vault se lee bien.
- [ ] Cerrar y reabrir Chrome no pierde nada.
- [ ] Borrar una reunión la quita del panel y de la búsqueda.

## 10. Demo provocadora
No aplica: herramienta personal, sin cliente.

## 11. Carácter de marca
- Adjetivos: sobrio, rápido, silencioso.
- No debe parecer: una herramienta de oficina corporativa, ni un chat.
- Referencias: Tactiq (la función), Linear (panel limpio).
- Material propio: ninguno; icono sencillo propio.

---
Siguiente: [[6 - Plan de Implementacion]] (TRD, UI-UX, AppFlow y Backend Schema: `no-aplica`, herramienta pequeña; el TRD cabe en el Plan).
