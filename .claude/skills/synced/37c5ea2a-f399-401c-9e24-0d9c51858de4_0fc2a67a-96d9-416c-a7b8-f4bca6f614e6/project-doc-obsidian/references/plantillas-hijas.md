# Plantillas para Notas Hijas

Usa estas plantillas cuando el proyecto requiera un sistema de notas (MOC + hijas).
Elige las que apliquen según los componentes detectados.

---

## Plantilla: Componente Técnico

Para documentar cómo funciona un módulo, nodo, clase, servicio o pieza del sistema.

```markdown
---
title: "Nombre Proyecto - Nombre Componente"
date: YYYY-MM-DD
tags:
  - [proyecto-tag]
  - componente
  - [tecnología]
type: referencia
status: completo | en-progreso
related:
  - "[[Nombre Proyecto - MOC]]"
---

## ¿Qué hace este componente?
Una o dos líneas. Función específica dentro del sistema mayor.

## Inputs y Outputs

| | Tipo | Descripción |
|---|------|------------|
| **Input** | `tipo_dato` | Qué recibe |
| **Output** | `tipo_dato` | Qué devuelve |

## Lógica interna
Cómo procesa los datos. Puede ser pseudocódigo, diagrama de texto o explicación.

```[lenguaje]
// Fragmento de código clave si es relevante
```

## Parámetros configurables
| Parámetro | Tipo | Default | Para qué |
|-----------|------|---------|---------|
| param1 | string | "valor" | Descripción |

## Dependencias
- Requiere: [[Componente X]] activo
- Usa: `librería/servicio`

> [!warning] Limitaciones
> Lo que este componente NO hace o dónde puede fallar.

---
## 🔗 Relacionado
- [[Nombre Proyecto - MOC]]
- [[Nombre Proyecto - Setup]]
```

---

## Plantilla: Setup / Configuración

Para documentar cómo instalar o configurar el proyecto desde cero.

```markdown
---
title: "Nombre Proyecto - Setup"
date: YYYY-MM-DD
tags:
  - [proyecto-tag]
  - setup
  - configuración
type: guia
status: completo
related:
  - "[[Nombre Proyecto - MOC]]"
---

## Requisitos previos
- [ ] Herramienta A instalada (versión mínima X)
- [ ] Cuenta en Servicio B
- [ ] Variable de entorno C configurada

## Instalación paso a paso

### 1. Clonar / Descargar
```bash
comando de instalación
```

### 2. Configurar variables / credenciales
```bash
# .env o configuración equivalente
VARIABLE=valor
API_KEY=tu_clave_aqui
```

> [!important] Credenciales
> Dónde conseguir cada credencial y con qué permisos.

### 3. Primer arranque
```bash
comando para iniciar
```

### 4. Verificar que funciona
Qué ver o hacer para confirmar que está correcto.

## Configuración avanzada
Opciones opcionales para personalizar el comportamiento.

## Desinstalar / Resetear
Si aplica, cómo volver al estado inicial.

---
## 🔗 Relacionado
- [[Nombre Proyecto - MOC]]
- [[Nombre Proyecto - Manual de uso]]
```

---

## Plantilla: Manual de Uso

Para quien va a usar el proyecto sin necesitar entender cómo está hecho.

```markdown
---
title: "Nombre Proyecto - Manual de uso"
date: YYYY-MM-DD
tags:
  - [proyecto-tag]
  - manual
  - uso
type: guia
status: completo
related:
  - "[[Nombre Proyecto - MOC]]"
---

## ¿Para qué sirve esto?
Explicación en lenguaje no técnico. Qué problema resuelve para el usuario final.

## Cómo usarlo

### Caso de uso principal
Paso a paso del flujo más común:

1. Hacer X
2. Introducir Y
3. Esperar / Ver resultado Z

> [!example] Ejemplo real
> Input: `ejemplo concreto`
> Output esperado: `resultado esperado`

### Casos de uso secundarios
Otros escenarios comunes y cómo manejarlos.

## Qué NO hace
Lista corta de limitaciones conocidas para gestionar expectativas.

## Preguntas frecuentes
**¿Qué pasa si X no funciona?**
Respuesta corta.

**¿Puedo usarlo para Y?**
Respuesta corta.

---
## 🔗 Relacionado
- [[Nombre Proyecto - MOC]]
- [[Nombre Proyecto - Troubleshooting]]
```

---

## Plantilla: Referencia Técnica

Para tablas de parámetros, endpoints, comandos, o cualquier dato que se consulta frecuentemente.

```markdown
---
title: "Nombre Proyecto - Referencia"
date: YYYY-MM-DD
tags:
  - [proyecto-tag]
  - referencia
type: referencia
status: completo
related:
  - "[[Nombre Proyecto - MOC]]"
---

## Endpoints / Comandos principales

| Nombre | Ruta / Comando | Método | Descripción |
|--------|---------------|--------|-------------|
| Acción A | `/ruta/a` | GET | Qué hace |
| Acción B | `/ruta/b` | POST | Qué hace |

## Parámetros globales

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| param1 | string | Sí | Para qué |
| param2 | int | No | Para qué, default: 10 |

## Códigos de respuesta / Estados
| Código | Significado |
|--------|------------|
| 200 | Éxito |
| 400 | Error en parámetros |
| 500 | Error del servidor |

## Variables de entorno / Configuración
| Variable | Ejemplo | Descripción |
|----------|---------|-------------|
| API_KEY | `abc123` | Clave de autenticación |

---
## 🔗 Relacionado
- [[Nombre Proyecto - MOC]]
```

---

## Plantilla: Troubleshooting

Para errores conocidos y cómo resolverlos.

```markdown
---
title: "Nombre Proyecto - Troubleshooting"
date: YYYY-MM-DD
tags:
  - [proyecto-tag]
  - troubleshooting
  - errores
type: referencia
status: en-progreso
related:
  - "[[Nombre Proyecto - MOC]]"
  - "[[Nombre Proyecto - Setup]]"
---

## Errores comunes

### ❌ Error: "Mensaje de error exacto"
**Causa:** Por qué ocurre.
**Solución:**
```bash
# Comando o pasos para solucionarlo
```

### ❌ Error: "Otro mensaje de error"
**Causa:** Por qué ocurre.
**Solución:** Qué hacer.

## Checks de diagnóstico
Si algo no funciona y no sabes por qué:
- [ ] Verificar X
- [ ] Confirmar que Y está activo
- [ ] Revisar logs en Z

## Contacto / Soporte
Dónde buscar ayuda si esto no resuelve el problema.

---
## 🔗 Relacionado
- [[Nombre Proyecto - MOC]]
- [[Nombre Proyecto - Manual de uso]]
```
