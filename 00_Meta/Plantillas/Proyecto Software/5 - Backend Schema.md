---
type: doc-software
doc: backend-schema
proyecto: "<% tp.file.folder() %>"
status: borrador
date: <% tp.date.now("YYYY-MM-DD") %>
origen: humano
---

# 5 · Backend Schema

> [!resumen]
> Modelo de datos y API que sostienen los flujos de [[4 - AppFlow]]. Verificar el esquema real de la BD remota antes de asumir tablas.

## 1. Diagrama entidad-relación
```mermaid
erDiagram
  USUARIO ||--o{ REGISTRO : crea
```

## 2. SQL ejecutable
Los bloques ```` ```sql ```` se concatenan en la migración y los ```` ```sql seed ```` en la semilla con `schema_to_migration.py`. Toda FK lleva `ON DELETE` (el script falla si falta).
```sql
create table cliente (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now()
);
create table registro (
  id uuid primary key default gen_random_uuid(),
  cliente_id uuid not null references cliente(id) on delete cascade,
  created_at timestamptz not null default now()
);
```
```sql seed
-- datos de prueba realistas
```
Generar: `python3 ~/Proyectos/flujo-software/tools/schema_to_migration.py "<este archivo>" <proyecto>/supabase`

## 2.1 Documentación de tablas
### `tabla`
| Columna | Tipo | Nulo | Default | Notas |
|---|---|---|---|---|
| id | uuid | no | gen_random_uuid() | PK |
| created_at | timestamptz | no | now() |  |

- Claves foráneas con **ON DELETE CASCADE / SET NULL** explícito (decidir y justificar):
- Índices:

## 3. Seguridad de datos
- RLS por rol (traza a permisos del AppFlow):
- Almacenamiento de ficheros (Storage), nada en disco efímero.

## 4. API / endpoints
| Método | Ruta | Rol | Entrada | Salida | Errores |
|---|---|---|---|---|---|

## 5. Migraciones
- Orden, datos semilla, reversibilidad.

## 6. Cálculos y reglas de negocio
Fórmulas exactas (tarifas, horas extra, totales) con ejemplo numérico.

---
Anterior: [[4 - AppFlow]] · Siguiente: [[6 - Plan de Implementacion]]
