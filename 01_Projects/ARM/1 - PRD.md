---
type: doc-software
doc: prd
proyecto: ARM
status: aprobado
tipo: micro-saas
date: '2026-11-17'
origen: mixto
---

# 1 · PRD — ARM (Agentic Relation Manager)

> [!resumen] En cristiano
> ARM es un CRM pensado para que lo **rellenen agentes** (Mila por WhatsApp, un futuro agente de voz, automatizaciones) y lo **lean personas**. El cliente entra y ve sus leads nuevos y cualificados, sin tocar nada. Los agentes escriben por **API**. Y si el cliente acaba con demasiados leads, conecta ARM por **MCP** (un enchufe estándar) a Claude o ChatGPT y les pregunta en lenguaje normal: «¿a quién llamo hoy?». Sustituye a `Panel de Leads` (archivado), que solo leía tablas de n8n.

## 1. Problema
- **Dolor**: el Setter trabaja bien, pero el cliente no ve el resultado y los datos de los agentes viven dispersos (tablas de n8n, chats). Un CRM clásico (GoHighLevel, HubSpot) está hecho para que un humano teclee; los agentes lo usan mal y el cliente se pierde en pestañas.
- **Hoy**: leads en tablas de n8n que nadie del cliente abre; avisos a mano. `Panel de Leads` los mostraba pero era solo lectura, sin datos propios, sin API de escritura ni MCP.
- **Tipo**: `micro-saas`, una instancia por cliente (decisión de Haytham, 2026-11-17).
- **Señal de demanda (Paso 0)**: no se exige (decisión de Haytham, 2026-11-17). Sin confirmar con clientes reales.

## 2. Usuarios y roles
| Rol | Quién es | Qué necesita | Frecuencia de uso |
|---|---|---|---|
| Cliente (dueño/recepción) | Responsable de la pyme que contrata el paquete | Ver leads nuevos y cualificados, abrir la ficha, marcar si ya contactó | Diaria |
| Cliente con muchos leads | El mismo, cuando el volumen desborda la pantalla | Preguntar a su Claude/ChatGPT sobre sus leads (MCP) | Según volumen |
| Agente (Setter, voz, automatización) | Software de NeoZeler | Crear y actualizar leads, mensajes, análisis y citas por API con clave propia | Continua |
| Operador NeoZeler (Haytham) | Instala y mantiene cada instancia | Alta de cliente en minutos, emitir y revocar claves | Al instalar y dar soporte |

### 2.1 Personas
`sin confirmar`: no hay investigación con clientes reales todavía. Arranca con el perfil de Panel de Leads (clínica dental, dueño o recepción).

### 2.2 Escenarios de usuario
- Como **cliente**, la recepcionista quiere abrir ARM por la mañana y ver los leads nuevos de la noche para llamar a los cualificados primero.
- Como **agente**, Mila quiere guardar el análisis de una conversación y la cita por API para que el lead aparezca cualificado sin intervención.
- Como **cliente con muchos leads**, el dueño quiere preguntar a su Claude «¿qué leads de esta semana pidieron implantes y no tienen cita?» y que responda con datos reales.

### 2.3 Top tasks
`sin confirmar` (sin usuarios reales que voten). Hipótesis: 1) ver leads nuevos, 2) ver cualificados, 3) abrir ficha, 4) cambiar etapa, 5) preguntar a la IA.

## 3. Objetivos y métricas de éxito
| Objetivo | Métrica | Valor actual | Meta |
|---|---|---|---|
| El cliente ve el valor del servicio | Entra al menos 1 vez por semana | 0 (no existe) | por fijar con el primer cliente |
| Los agentes escriben sin intervención humana | % de leads que llegan cualificados sin editar a mano | n/a | por medir |
| El MCP resuelve la sobrecarga | El cliente conecta su IA y obtiene respuesta útil en < 5 min | n/a | probar con 1 cliente |
| Alta rápida | Tiempo de alta de una instancia | n/a | < 1 hora |

## 4. Historias de usuario (priorizadas)
| ID | Como… | Quiero… | Para… | Prioridad |
|---|---|---|---|---|
| US-01 | Cliente | entrar y ver la lista de leads nuevos y cualificados | saber a quién llamar hoy | Must |
| US-02 | Cliente | abrir la ficha de un lead (datos, qué busca, resumen de la charla, cita, historial) | preparar la llamada | Must |
| US-03 | Agente | crear y actualizar leads, mensajes, análisis y citas por API | que el CRM se rellene solo | Must |
| US-04 | Cliente | cambiar la etapa de un lead y dejar una nota | no repetir trabajo | Must |
| US-05 | Operador | emitir y revocar claves de API por agente y por instancia | controlar quién escribe | Must |
| US-06 | Cliente | conectar ARM por MCP a Claude o ChatGPT con una clave de solo lectura (o lectura y escritura acotada) | consultar mis leads en lenguaje normal | Must |
| US-07 | Operador | desplegar una instancia nueva con marca y claves propias por script | replicar sin rehacer | Must |
| US-08 | Cliente | ver los leads por etapas (vista pipeline) | ver el embudo de un vistazo | Should |
| US-09 | Cliente | ver quién (qué agente o persona) cambió cada dato y cuándo | confiar en lo que escriben los agentes | Should |
| US-10 | Cliente | recibir aviso por WhatsApp o correo cuando se cualifique un lead | enterarme sin abrir ARM | Could |
| US-11 | Cliente | resumen semanal (entrados, cualificados, con cita) | medir el valor | Could |

## 5. Requisitos funcionales
- RF-01: **modelo de datos propio** (lead, conversación/mensajes, análisis, cita, etapa, notas, eventos). ARM es la fuente de verdad; n8n y los agentes escriben en ARM, no al revés.
- RF-02: **API REST** documentada (OpenAPI), con claves por agente y alcance (`leads:read`, `leads:write`, `citas:write`…). Idempotente por `external_id` para que un agente reintente sin duplicar.
- RF-03: **servidor MCP** que expone las mismas operaciones a Claude/ChatGPT: buscar y filtrar leads, leer ficha, listar cualificados, cambiar etapa, añadir nota. Claves del cliente distintas de las de los agentes, con alcance mínimo.
- RF-04: **cualificado** = cita agendada **o** análisis del Setter con tipo de negocio, problema o servicio de interés rellenado (heredado de Panel de Leads, por confirmar). Lo calcula ARM al recibir datos.
- RF-05: **etapas**: `nuevo` → `en proceso` → `cualificado` → `agendado` → `ganado` / `descartado`. Lista por confirmar con el primer cliente.
- RF-06: **registro de cambios** (quién, cuándo, qué) para cada lead; los agentes quedan identificados.
- RF-07: web con login por cliente, vista lista, ficha y pipeline. Un cliente nunca ve datos de otro.
- RF-08: marca blanca por instancia (nombre, logo, color), igual que Panel de Leads.
- RF-09: alta de instancia por script reproducible (Go).
- RF-10: **webhooks de salida** opcionales (lead cualificado, cita creada) para que n8n u otros reaccionen.

## 6. Requisitos no funcionales
- Idioma: español. Móvil y escritorio.
- Seguridad: datos personales de terceros (RGPD); claves con alcance, rotables y revocables; ningún secreto en el repo; limitación de peticiones por clave.
- **MCP y datos personales**: al conectar ARM a una IA externa, los datos del lead salen a ese proveedor (OpenAI/Anthropic). Debe ser decisión consciente del cliente, con aviso y alcance de solo lectura por defecto.
- Disponibilidad: una instancia por cliente en su VPS; si cae, los agentes reintentan (idempotencia).
- Mantenimiento: una persona (Haytham) para todas las instancias.

## 7. Fuera de alcance (v1)
- Multi-cliente en una sola instalación (una instancia por cliente).
- Hablar con el lead desde ARM (sigue en WhatsApp/voz).
- Facturación, campañas de email, automatizaciones propias (eso es n8n).
- Importación masiva desde otros CRM.
- Agente de voz: v1 solo deja la API lista; el agente se conecta después.

## 8. Riesgos y supuestos
> [!riesgo]
> - Es un CRM nuevo: el vault ya registra que «ningún CRM le convence» a Haytham (minicrm-go, Neozeler CRM, 17 proyectos congelados). Riesgo de repetir el patrón; mitigación: v1 mínima, un solo cliente real (Setter) y fecha de revisión.
> - Solapa con `NeoZeler HQ` (CRM interno de NeoZeler, absorbe Neozeler CRM). Aclarar: ARM es para **clientes de NeoZeler**, HQ es **interno**. Decisión pendiente si comparten código.
> - Datos personales de leads en un panel web y vía MCP a IA externa: RGPD, contrato de encargado de tratamiento, política de privacidad.
> - Seguridad del MCP: una IA conectada con permisos de escritura puede modificar leads por error o por instrucciones maliciosas escondidas en un mensaje del lead (inyección de instrucciones). Por defecto, solo lectura.
> - Migración: el Setter hoy escribe en tablas de n8n; hay que cambiarlo a escribir en ARM sin perder datos.
> - Supuesto: un VPS por cliente con n8n propio.

## 9. Criterios de aceptación globales
- [ ] El Setter crea un lead, su análisis y su cita en ARM por API y el lead aparece cualificado sin tocar nada.
- [ ] Un cliente de prueba ve solo sus leads y la ficha completa.
- [ ] Una clave sin alcance de escritura recibe 403 al intentar escribir.
- [ ] Claude se conecta por MCP con la clave del cliente y responde «¿qué leads cualificados no tienen cita?» con datos reales.
- [ ] Reintentar la misma llamada de un agente no duplica el lead.
- [ ] Alta de instancia por script sin tocar código.
- [ ] Ciclo crear → refrescar → borrar → refrescar comprobado en producción.

## 10. Demo provocadora (reunión 1)
Pendiente. Idea: instancia con 30 leads sintéticos de una clínica dental y un Claude conectado por MCP respondiendo en directo «¿a quién llamo hoy?». Enseñar a dueño y recepción.

## 11. Carácter de marca (insumo de la identidad visual)
Decidido con Haytham el 2026-11-17 (sustituye la propuesta de Panel de Leads):
- 3 adjetivos: **cálido, técnico, premium**.
- Anti-referencias: que no parezca un CRM cualquiera; que no tenga aspecto de IA (sin degradados morados, sin brillos «mágicos», sin robots ni chispas).
- Referencias: GoHighLevel (lo que le gusta de su aspecto y flujo), [Twenty](https://github.com/twentyhq/twenty) (CRM abierto moderno con API; la más cercana y escalable), [Huly](https://github.com/hcengineering/platform) (gestión de proyectos; densidad y velocidad) y [Akaunting](https://github.com/akaunting/akaunting) (contabilidad; orden de tablas y fichas). Son referencia de **aspecto y modelo**, no se copia código.
- Qué se enseña en vivo: leads reales y la pregunta a la IA con su respuesta.
- Marca: **marca ARM con logo y color de acento del cliente** (elegida por escalabilidad: una sola identidad que mantener; decisión delegada por Haytham, 2026-11-17).
- Material propio: logo y color de cada cliente al dar de alta la instancia.

---
Siguiente: [[2 - TRD]]
