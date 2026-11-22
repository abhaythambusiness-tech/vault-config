# Plantillas

Índice:
1. Ficha de servicio (Fase 3)
2. Guía de demo (Fase 4)
3. Plan de proyecto SaaS (Fase 5)

---

## 1. Ficha de servicio

Usa esta estructura literalmente, sin añadir ni quitar secciones.

```
## [Nombre comercial del servicio]

**Nicho:**
**Dolores que resuelve:** (referencia los # de la Fase 1)
**Promesa en una frase:** (qué gana el cliente, en su idioma, no en el tuyo)

### Qué incluye
- Entregable 1
- Entregable 2

### Arquitectura técnica
- Stack: n8n + [resto]
- Flujo resumido: trigger → pasos → salida
- Integraciones necesarias
- Puntos de fallo previsibles y cómo se manejan

### Modelo de precio
- Setup inicial: X €
- Mantenimiento mensual: Y €/mes
- Justificación del precio: (ROI para el cliente, no coste para ti)

### Argumentario de venta
- Gancho de apertura
- 3 objeciones típicas y su respuesta
- Prueba o dato que sustenta la promesa

### Esfuerzo de implementación
- Horas estimadas de montaje
- Dificultad: baja / media / alta
```

**Criterios de calidad:**
- La promesa se escribe en el lenguaje del cliente ("dejas de perder citas los fines de semana"),
  nunca en lenguaje técnico ("orquestación de webhooks").
- La justificación del precio compara con el coste actual del dolor, no con horas de trabajo.
- Si no sabes estimar el ROI, dilo en vez de inventar un número.

---

## 2. Guía de demo

```
## Demo — [Nombre del servicio]

**Objetivo:** qué momento "wow" busca provocar
**Tiempo de montaje:** X h (máximo 3)

### Montaje
1. Nodos de n8n concretos, en orden
2. Credenciales / integraciones necesarias
3. Datos de prueba a usar (nombres, emails y casos ficticios pero realistas)

### Guion de 5 minutos
- Minuto 0-1: el dolor, en voz del cliente
- Minuto 1-3: la demo en vivo
- Minuto 3-4: qué pasa por detrás (superficial)
- Minuto 4-5: cierre y siguiente paso

### Qué NO enseñar todavía
- [Funcionalidad que queda detrás del contrato]
```

---

## 3. Plan de proyecto SaaS

Diagrama de referencia:

```
Inicio → Planificación → Ejecución → Seguimiento y Control → Cierre
                ↑              ↑              │
                └──────────────┴──────────────┘
```

Tabla obligatoria:

| Fase | Actividades concretas | Entregables | Criterio de salida | Duración estimada |
|---|---|---|---|---|
| Inicio | | | | |
| Planificación | | | | |
| Ejecución | | | | |
| Seguimiento y Control | | | | |
| Cierre | | | | |

Después de la tabla, añade siempre:

**Bucle Seguimiento y Control → Ejecución**
Se dispara cuando: [ajustes menores dentro del alcance: bugs, microcopy, ajustes de UX,
rendimiento]. No requiere renegociar plazo ni precio.

**Bucle Seguimiento y Control → Planificación**
Se dispara cuando: [desvío de alcance, coste o plazo por encima del umbral acordado; cambio de
requisitos del cliente; hallazgo técnico que invalida la arquitectura]. Requiere replanificar y
comunicar al cliente.

**Métricas de seguimiento**
- MRR y ARPU
- Churn mensual
- Tenants activos / tenants totales
- Tasa de activación (tenants que completan el onboarding)
- Uptime y tiempo medio de resolución de incidencias

**Consideraciones multi-tenant** (incluir siempre que aplique):
- Aislamiento de datos entre tenants y política de backups
- Onboarding autoservicio vs. asistido
- Coste de infraestructura por tenant y punto de rentabilidad
- RGPD: responsable vs. encargado del tratamiento, contrato de encargo, derecho de supresión
