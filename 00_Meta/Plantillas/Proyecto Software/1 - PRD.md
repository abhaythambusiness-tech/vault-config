---
type: doc-software
doc: prd
proyecto: "<% tp.file.folder() %>"
status: borrador
tipo: <micro-saas | saas | startup | a-medida>
date: <% tp.date.now("YYYY-MM-DD") %>
origen: humano
---

# 1 · PRD — Product Requirements Document

> [!resumen]
> **Qué**: el problema, para quién y qué significa éxito. **No** incluye tecnología (eso es el TRD). Se aprueba antes de pasar a `2 - TRD`.

## 1. Problema
- Dolor concreto (con cifras si las hay) y quién lo sufre a diario:
- Cómo lo resuelven hoy y por qué falla:

## 2. Usuarios y roles
| Rol | Quién es | Qué necesita | Frecuencia de uso |
|---|---|---|---|
|  |  |  |  |

### 2.1 Personas (basadas en investigación, no inventadas)
Una por público central; la periferia solo si hay tiempo. Salen de entrevistas, encuestas o datos reales, sobre todo de **comportamiento** (no solo edad y género). Sin investigación, marcar `sin confirmar`.
| Nombre | Rol / empresa | Cómo usa hoy la herramienta (dispositivo, dónde, cuánto tiempo) | Miedos y aspiraciones | Fuente (entrevista, encuesta, dato) |
|---|---|---|---|---|
|  |  |  |  |  |

### 2.2 Escenarios de usuario
Uno por persona y objetivo. Formato: «Como [rol], [persona] quiere [acción] para [meta]».
- **Entorno** (dónde está, qué distracciones, conexión):
- **Disparador** (qué evento la trae aquí hoy):
- **Recorrido** (entrada → pasos → meta). Si el recorrido da vueltas o no llega, es un problema de estructura: arreglarlo antes del TRD:
- Cada escenario traza a una historia `US-xx` de la sección 4.

### 2.3 Top tasks (qué priorizar)
Lista de 10-20 tareas en lenguaje del usuario, sin jerga, en orden aleatorio. Pedir a 5-10 usuarios reales que elijan las 5 que más les importan; contar votos / nº de usuarios. Se espera una «cola larga»: las pocas primeras (≈20 %) resuelven la mayoría del valor. Las del cuerpo de la cola son `Should`/`Could` de la sección 4.
| Tarea | Votos | % usuarios | Prioridad MoSCoW |
|---|---|---|---|
|  |  |  |  |

## 3. Objetivos y métricas de éxito
| Objetivo | Métrica | Valor actual | Meta |
|---|---|---|---|
|  |  |  |  |

## 4. Historias de usuario (priorizadas)
| ID | Como… | Quiero… | Para… | Prioridad (MoSCoW) |
|---|---|---|---|---|
| US-01 |  |  |  | Must |

## 5. Requisitos funcionales
- RF-01:

## 6. Requisitos no funcionales
Rendimiento, seguridad, accesibilidad, idioma, dispositivos, disponibilidad.

## 7. Fuera de alcance (v1)
-

## 8. Riesgos y supuestos
> [!riesgo]
> -

## 9. Criterios de aceptación globales
- [ ]

## 10. Demo provocadora (reunión 1)
Prototipo rápido con **datos sintéticos realistas** (nombres, cifras y casos del sector del cliente) para provocar reacciones y descubrir quién sufre el dolor diario.
- Qué pantalla provoca la reacción y con qué datos:
- Quién del cliente la ve (y quién *no* debería usar el móvil):
- Reacciones recogidas / rechazos → ajustes al alcance:
- Si hay rechazo de operarios de campo: descartar app móvil y centrar en el flujo de oficina.

## 11. Carácter de marca (insumo de la identidad visual)
Sin tecnología ni colores todavía: solo lo que el cliente y Haytham quieren que se sienta. Alimenta la identidad del [[3 - UI-UX Design]].
- 3 adjetivos que debe transmitir:
- Qué NO debe parecer (anti-referencias):
- 2 referencias que le gustan al cliente o a Haytham, y por qué:
- Qué del negocio se puede enseñar en vivo (datos, oficio, proceso, lugar) en vez de ilustrarlo con stock:
- Material propio disponible (fotos reales, logo vectorial, textos) y qué imágenes habrá que pedir:

---
Siguiente: [[2 - TRD]]
