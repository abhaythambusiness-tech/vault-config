---
type: doc-software
doc: prd
proyecto: "Los Apuntes de Liyo"
status: aprobado
date: 2026-10-27
origen: mixto
---

# 1 · PRD — Product Requirements Document

> [!resumen]
> **Qué**: el problema, para quién y qué significa éxito. **No** incluye tecnología (eso es el TRD). Se aprueba antes de pasar a `2 - TRD`.

## 1. Problema
- Dolor concreto: los alumnos de grado medio de informática (de distintos centros) tienen apuntes dispersos — en el móvil, en papel, en Drives sueltos — y cuando les surge una duda de estudio tardan en encontrar el apunte exacto que la responde, o directamente no lo encuentran porque lo tiene un compañero de otra clase.
- Cómo lo resuelven hoy y por qué falla: buscan en sus propios apuntes (si los tienen bien organizados, que no siempre), preguntan en grupos de WhatsApp/Telegram (respuesta lenta, sin fuente, a veces errónea) o buscan en Google/ChatGPT genérico (responde sin el contenido real de su módulo, puede alucinar o no ajustarse al temario de su profesor).

## 2. Usuarios y roles
| Rol | Quién es | Qué necesita | Frecuencia de uso |
|---|---|---|---|
| Alumno | Estudiante de grado medio de informática, de cualquier centro | Subir sus apuntes/PDFs a un módulo y preguntar dudas de estudio con respuestas basadas en esos apuntes | Varias veces por semana, más en época de examen |
| Admin (Haytham) | Gestiona el catálogo de módulos/asignaturas y vigila abuso | Crear/editar módulos, moderar contenido denunciado, ver uso y coste de la API | Puntual |

## 3. Objetivos y métricas de éxito
| Objetivo | Métrica | Valor actual | Meta |
|---|---|---|---|
| Responder dudas más rápido que buscando a mano | Tiempo desde pregunta hasta respuesta útil | N/A (no existe) | < 10 s |
| Que la comunidad aporte contenido real | Documentos indexados por módulo tras 1 mes | 0 | ≥ 15 documentos en al menos 3 módulos |
| Respuestas fiables, no inventadas | % de respuestas que citan la fuente (documento/página) | N/A | 100% (si no hay contexto suficiente, decirlo en vez de inventar) |

## 4. Historias de usuario (priorizadas)
| ID | Como… | Quiero… | Para… | Prioridad (MoSCoW) |
|---|---|---|---|---|
| US-01 | alumno | subir un PDF o apuntes a un módulo/asignatura | que la comunidad tenga ese material disponible | Must |
| US-02 | alumno | preguntar algo en un chat tipo ChatGPT | recibir una respuesta basada en los apuntes reales del módulo, con la fuente citada | Must |
| US-03 | alumno | elegir el módulo/asignatura antes de preguntar | que la búsqueda no mezcle contenido de otras materias | Must |
| US-04 | alumno | ver qué documentos hay ya subidos en un módulo | no subir duplicados y saber qué cubre la base | Should |
| US-05 | admin | crear, renombrar o archivar módulos | mantener el catálogo ordenado por ciclo/curso | Should |
| US-06 | admin | denunciar y borrar un documento subido | quitar contenido erróneo, con copyright o inapropiado | Must |

## 5. Requisitos funcionales
- RF-01: ingesta de PDF/texto — extracción y fragmentación (chunking) en bloques de ~300-500 palabras con metadata (módulo, archivo, página).
- RF-02: tokenización tradicional de cada bloque (minúsculas, sin acentos/puntuación, eliminación de stop words en español) e indexado en un índice invertido (SQLite FTS5 / BM25).
- RF-03: al preguntar, tokenizar la pregunta con las mismas reglas y recuperar los N bloques más relevantes del módulo seleccionado.
- RF-04: armar un prompt con esos bloques como único contexto y enviarlo a la API de Groq; la respuesta debe citar el documento y página de origen.
- RF-05: si no hay bloques relevantes suficientes, el chat debe decirlo en vez de responder sin contexto.
- RF-06: organización del contenido por asignatura/módulo (catálogo editable por el admin).
- RF-07: subida de documentos por cualquier alumno registrado, sin paso de aprobación previa (comunidad abierta) pero con botón de "denunciar documento" visible para todos.
- RF-08: panel mínimo de admin para borrar documentos denunciados y ver qué módulos existen.

## 6. Requisitos no funcionales
- Coste y recursos bajos: SQLite local (sin base vectorial ni servidor de búsqueda pesado), pensado para correr con poca RAM.
- Idioma: español.
- Dispositivos: web responsive, uso principal desde el móvil.
- Seguridad mínima: registro simple de alumno (nombre + centro, sin datos sensibles) para poder atribuir y moderar subidas.
- Sin alucinaciones de datos: la IA solo redacta con los fragmentos recuperados, nunca inventa a partir de "lo que ya sabe".

## 7. Fuera de alcance (v1)
- Cuentas con roles complejos, gamificación, quizzes generados automáticamente.
- Revisión/aprobación editorial de cada documento antes de indexarlo (se modera después, no antes).
- App móvil nativa.
- Multi-idioma.

## 8. Riesgos y supuestos
> [!riesgo]
> - **Comunidad abierta sin revisión previa** (decisión tomada): cualquier alumno puede subir contenido erróneo, con copyright de terceros (apuntes de una editorial, exámenes de un profesor) o inapropiado antes de que un admin lo vea. Mitigación mínima: botón de denuncia + borrado rápido por el admin, y aviso legal de que el contenido subido es responsabilidad de quien lo sube.
> - Uso de la API de Groq a escala: si crece mucho el número de alumnos, el coste y los límites de la API pueden ser un cuello de botella — vigilar cuota/coste desde el principio.
> - Supuesto: los alumnos tienen un mínimo de buena fe y suben material real de su módulo, no spam.

## 9. Criterios de aceptación globales
- [ ] Un alumno sube un PDF a un módulo y, en minutos, puede preguntarle algo que esté en ese PDF y recibir una respuesta citando el documento y la página.
- [ ] Si la pregunta no tiene relación con ningún documento del módulo, el chat lo dice en vez de inventar.
- [ ] El admin puede borrar un documento denunciado y desaparece de las respuestas futuras.

## 10. Demo provocadora (reunión 1)
- Qué pantalla provoca la reacción y con qué datos: un chat ya cargado con apuntes sintéticos realistas de un módulo típico de grado medio (p. ej. "Montaje y Mantenimiento de Equipos" o "Programación"), con 2-3 preguntas tipo examen ya resueltas citando página.
- Quién del cliente la ve: alumnos reales de grado medio de informática (no hay "operarios de campo" aquí, todos usan móvil con normalidad).
- Reacciones recogidas / rechazos → ajustes al alcance: pendiente de hacer la demo con alumnos reales.
- No aplica el descarte de app móvil (el público objetivo sí usa el móvil a diario).

## 11. Carácter de marca (insumo de la identidad visual)
- 3 adjetivos que debe transmitir: cercano, claro, de fiar (como el apunte de un compañero aplicado, no como un producto corporativo).
- Qué NO debe parecer (anti-referencias): nada de "asistente de IA genérico" (robot azul, chispas moradas), nada de aspecto de LMS institucional soso (Moodle).
- 2 referencias que le gustan al cliente o a Haytham, y por qué: Notion (tarjetas de documento limpias, legibles en móvil) y Hypothesis/Readwise (el subrayado real como elemento de interfaz, no decorativo) — definidas con Haytham el 2026-10-27, detalle en [[3 - UI-UX Design]] §2.
- Qué del negocio se puede enseñar en vivo: apuntes y preguntas reales de alumnos de grado medio, en vez de ilustrarlo con stock.
- Material propio disponible: sin logo previo (proyecto personal, sin cliente); las dos imágenes mínimas de la v1 (wordmark e icono de estado vacío) se resuelven en SVG propio, decisión tomada el 2026-10-27 ([[3 - UI-UX Design]] §5).

---
Siguiente: [[2 - TRD]]
