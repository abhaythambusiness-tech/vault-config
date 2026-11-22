---
type: doc-software
doc: plan-implementacion
proyecto: ARM
status: aprobado
date: '2026-11-17'
origen: mixto
---

# 6 · Plan de Implementación — ARM

> [!resumen] En cristiano
> Orden de trabajo en pasos pequeños. Primero el núcleo sin pantallas (datos, API, claves, MCP), que es lo que valida la idea; la web va después, cuando la identidad visual esté aprobada. Nada de código hasta aprobar este plan.

Código real en `~/Proyectos/arm/` (git desde el primer commit).

## 1. Fases
| Fase | Objetivo | Entregable demostrable | Historias |
|---|---|---|---|
| 0 Scaffold | Repo Go, `.gitignore`, `.env.example`, spike de versiones (Go, go-sdk, Huma) | build y test vacíos en verde | — |
| 1 Datos | Migración y semilla de [[5 - Backend Schema]] aplicadas por la app | tablas verificadas con SQLite real | US-03 |
| 2 Núcleo | Servicio de dominio: cualificado, idempotencia, registro de eventos | tests del servicio en verde | US-03, US-04 |
| 3 API y claves | `/api/v1`, claves con alcance, límite por clave, OpenAPI | `curl` con clave de agente rellena un lead cualificado | US-03, US-05 |
| 4 MCP | Herramientas MCP, spike OAuth, guía de conexión | Claude Desktop o Claude Code responde con datos reales | US-06 |
| 5 Setter | El Setter de n8n escribe en ARM; script de importación de tablas viejas | un lead de WhatsApp real aparece cualificado | US-03 |
| 6 UI | Identidad aplicada y pantallas ([[3 - UI-UX Design]]) | demo navegable + `DESIGN-IDENTITY.md` en el repo | US-01, US-02, US-04, US-08, US-09 |
| 7 Alta y despliegue | `arm-alta`, Docker + Caddy, copia diaria | instancia en un VPS con HTTPS | US-07 |
| 8 Extras | Avisos, resumen semanal | según prioridad | US-10, US-11 |

## 2. Tareas
- [x] T-01 · (US-03) Scaffold Go: `go mod`, estructura `cmd/arm`, `cmd/arm-alta`, `internal/`; **spike**: ¿compilan `go-sdk` v1.8.0, `modernc.org/sqlite` v1.62.0 y Huma con la versión de Go instalada? · criterio: `go build ./...` en verde y versiones fijadas en el TRD · depende de: —
- [x] T-02 · (US-03) Capa de datos: aplicar migración al arrancar, `PRAGMA foreign_keys=ON` y WAL en cada conexión · criterio: test crea, lee y borra con cascada · depende de: T-01
- [x] T-03 · (US-03, US-04) Servicio de dominio: alta idempotente por `(origen, external_id)`, normalizar teléfono, regla de cualificado, etapas y eventos · criterio: tests con los casos de la semilla (`l1`, `l2` cualificados; `l5` no) · depende de: T-02
- [x] T-04 · (US-05) Claves: generar, hashear, alcances, caducidad, revocación, último uso · criterio: clave sin alcance recibe 403, revocada 401 · depende de: T-03
- [x] T-05 (sin Huma ni OpenAPI: pendiente) · (US-03) API REST `/api/v1` según [[5 - Backend Schema]] §4 con OpenAPI y límite por clave · criterio: reintento no duplica; contrato validado · depende de: T-04
- [x] T-06 · (US-06) Servidor MCP en `/mcp`: `buscar_leads`, `ver_lead`, `listar_cualificados`, `cambiar_etapa`, `anadir_nota`; paginación máx. 50; escritura solo con alcance · criterio: cliente del SDK lista y lee; sin alcance no ve herramientas de escritura · depende de: T-05
- [x] T-07 (resultado: [[Spike T-07 - OAuth para el MCP]]; nace T-07b OAuth mínimo tras T-10) · (US-06) Spike OAuth: ¿admite Claude.ai/ChatGPT clave estática o hace falta OAuth? Documentar el resultado y el plan B · criterio: nota con la prueba real · depende de: T-06
- [ ] T-08 · (US-03) Importar tablas viejas del Setter (`setter_clientes`, `setter_mensajes`, `setter_citas`) y cambiar los workflows de n8n a escribir en ARM; resolver antes `build.py` desactualizado · criterio: un lead real de WhatsApp aparece cualificado · depende de: T-05
- [ ] T-09 · (US-10) Webhooks de salida con reintento y firma · criterio: n8n recibe `lead.cualificado` · depende de: T-05
- [ ] T-10 · (US-01, US-02, US-04, US-08, US-09) Identidad visual, Paleta de Componentes y web: login, lista, ficha, notas, pipeline, registro de cambios · criterio: flujo 1 del [[4 - AppFlow]] completo en 375/768/1280 px, axe a cero · depende de: T-05 y UI-UX aprobada
- [ ] T-11 · (US-06) Pantalla Conexiones: crear claves de IA y guía paso a paso para Claude y ChatGPT · criterio: un cliente conecta su IA sin ayuda · depende de: T-06, T-10
- [ ] T-12 · (US-11) Resumen semanal (leads entrados, cualificados, con cita) · depende de: T-10
- [ ] T-13 · (US-07) `arm-alta`: volumen, `.env`, migración, usuario, claves y marca · criterio: instancia nueva en menos de 1 hora · depende de: T-05
- [ ] T-14 · (US-07) Docker + Caddy, HTTPS y copia diaria `VACUUM INTO` · criterio: restaurar una copia en otra máquina · depende de: T-13

## 2.1 Starter kits reutilizados
| Kit | Fase | Adaptación |
|---|---|---|
| `Panel de Leads` (archivado: UI, pipeline, alta en Go, Docker + Caddy) | 6, 7 | Reaprovechar pantallas y script de alta; cambiar la fuente de datos de n8n a la API de ARM |
| `minicrm-go` (Go + SQLite + HTMX) | 1-3 | Mirar su estructura y pruebas; no su frontend (la regla exige React + shadcn) |
| `setter-neozeler` | 5 | Esquema de las tablas actuales para la importación |

## 3. Estrategia de pruebas
- Unitarias: servicio de dominio (cualificado, etapas, idempotencia, teléfono) y permisos por alcance.
- Contrato: la API contra su OpenAPI; el MCP con el cliente del SDK.
- Seguridad: claves revocadas y caducadas, límite por clave, un lead con texto malicioso no puede disparar herramientas de escritura.
- e2e del ciclo crear → refrescar → editar → borrar → refrescar **en producción**.

## 4. Despliegue y operación
- Variables de entorno en `.env` (`chmod 600`, nunca en el repo), dominio por cliente, Caddy con HTTPS automático.
- Copia diaria con `VACUUM INTO` y prueba de restauración; registro de arranque y errores en logs.

## 5. Riesgos y plan B
> [!riesgo]
> - El MCP puede no conectar con Claude.ai o ChatGPT con clave estática (T-07). Plan B: Claude Desktop/Code con clave, u OAuth con el paquete `auth` del SDK.
> - Versión de Go o de librerías incompatible (T-01). Plan B: actualizar Go o fijar versiones anteriores del SDK.
> - Repetir el patrón de CRM abandonado: v1 se limita a fases 0-5 y un cliente real (el propio Setter); revisión de continuidad al terminar la fase 5.
> - Migrar el Setter sin perder datos: copia previa de las tablas de n8n y periodo en paralelo.

## 6. Definición de terminado
- [ ] `trace_lint.py` en `RESULTADO: OK` y `schema_to_migration.py` sin avisos de FK
- [ ] `go vet`, `go test ./...`, `tsc --noEmit` y build limpios
- [ ] Checklist técnico/SEO y de marca
- [ ] Pruebas de intercambio y de lejos superadas; cero imágenes pendientes o inventadas; fila añadida a [[Registro de Identidades Visuales]]
- [ ] README y `resumen.html` en el repo
- [ ] Ficha en `01_Projects/` y sesión registrada
- [ ] `.claude/COMMON_MISTAKES.md` actualizado

---
Anterior: [[5 - Backend Schema]]
