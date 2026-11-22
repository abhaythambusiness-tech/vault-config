---
date: '2026-10-13'
proyecto: INGECONS
status: completado
tags:
- neozeler
- ingecons
- software-a-medida
- supabase
- nextjs
type: sesion
origen: mixto
---

# Sesión — 2026-10-13: Software a medida INGECONS y sincronización de partes

> [!abstract] Resumen
> Estabilización de la app INGECONS (`~/Proyectos/ingecons`): resolución definitiva de la sincronización de partes de trabajo con las obras, integración de la plantilla real de operarios y bypass de la caché persistente de Next.js sobre Supabase Storage.

## Contexto
Continuación del desarrollo del software de gestión operativa para constructora [[02_Areas/NeoZeler/Clientes/INGECONS|INGECONS]], vinculado al nuevo servicio [[02_Areas/NeoZeler/Servicios/Servicio - Software de Gestión Operativa a Medida|Software a Medida de NeoZeler]].

## Qué se hizo
- **Sincronización Obra ↔ Partes**: Se unificaron los partes diarios en la vista de detalle de cada obra (`/admin/obras/[id]`) y en la tarjeta de resumen (`/admin/obras`). Ahora se recalculan en tiempo real los costes de mano de obra, horas trabajadas y semáforo presupuestario.
- **Plantilla real de operarios**: Conexión de `/admin/partes` con la tabla `personnel` de Supabase para que el selector de trabajadores muestre la plantilla real (Antonio Ruiz, Francisco López, Mohamed El Amrani, etc.) en lugar de IDs mock hardcodeados.
- **Bypass de Next.js Data Cache**: Se sustituyó el método `download()` de `@supabase/storage-js` por llamadas HTTP directas con `cache: 'no-store'` y parámetro de tiempo dinámico (`?t=${Date.now()}`), eliminando la retención de partes borrados en el servidor.
- **Resiembra controlada**: Corrección de la lógica de re-seeding para que un array vacío (`[]`) se respete como estado válido deliberado.
- **Auditoría completa**: Verificación de todas las rutas principales (`/admin/obras`, `/admin/partes`, `/admin/empleados`, `/admin/facturas`, `/admin/informes/mensual`, `/api/pdf/*`) respondiendo 200 OK en producción.

## Decisiones tomadas
- Persistir los partes de trabajo en Supabase Storage JSON con bypass forzado de caché en Next.js App Router para evitar dependencias de esquemas DDL no aplicados en la BD remota.
- Vincular la mano de obra en expedientes de obra tanto a los partes volcados en oficina como a los fichajes de campo si existiesen.
- Registrar errores 37 a 41 en [[.claude/COMMON_MISTAKES.md]] para prevenir rectificaciones futuras en proyectos similares.

## Aprendizajes (para futuras sesiones)
- **Supabase Storage en Next.js 14/15**: Las llamadas a Storage mediante el SDK usan `fetch` global sin directivas de no-store, por lo que Next.js almacena las respuestas indefinidamente en Data Cache. Siempre implementar bypass directo con timestamp y `cache: 'no-store'`.
- **Props a estado local en React**: En componentes cliente donde los datos mutan vía Server Actions y revalidación, sincronizar el estado reactivo comparando props previas con actuales (`if (initialPartes !== prevInitialPartes)`).

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[02_Areas/NeoZeler/Clientes/INGECONS]]
- [[02_Areas/NeoZeler/Servicios/Servicio - Software de Gestión Operativa a Medida]]

