# Ejemplos de Documentación por Complejidad

Tres ejemplos de referencia para calibrar cuándo usar 1, 2 o 3+ notas.

---

## EJEMPLO 1: Nota única
**Proyecto:** Script de Python para renombrar archivos en batch
**Decisión:** Una sola nota — proyecto puntual, sin subcomponentes, menos de 100 líneas real

### `Proyecto - Renombrador de archivos batch.md`

```markdown
---
title: "Proyecto - Renombrador de archivos batch"
date: 2025-04-01
tags:
  - proyecto
  - python
  - utilidades
type: proyecto
status: completo
related:
  - "[[Python - Scripts de utilidades]]"
---

## 🎯 Qué hace
Script de Python que renombra archivos en masa aplicando un patrón configurable
(fecha + nombre original, quitar caracteres especiales, añadir prefijo, etc.).

## ⚙️ Cómo funciona
Lee todos los archivos en una carpeta, aplica transformaciones al nombre según
las reglas definidas en `config.py`, y renombra con opción de dry-run (simular sin ejecutar).

## 🛠️ Stack
- **Python 3.10+**: lógica principal
- **pathlib**: manejo de rutas
- **rich**: output formateado en terminal

## 📋 Uso rápido

```bash
# Simular (sin renombrar)
python rename.py --folder ./fotos --dry-run

# Ejecutar
python rename.py --folder ./fotos --pattern "{date}_{original}"
```

## 📁 Archivos
- `rename.py` — script principal
- `config.py` — patrones disponibles y configuración
- `tests/test_rename.py` — tests básicos

## ⚠️ Gotchas
> [!warning] Sin deshacer automático
> No hay función de undo. Siempre usar --dry-run primero.

## 🔄 Ideas futuras
- [ ] Soporte para subcarpetas (recursivo)
- [ ] Preview visual antes de confirmar

## 📅 Log
### 2025-04-01
Versión inicial. Funciona para casos de uso de fotos y documentos escaneados.

---
## 🔗 Relacionado
- [[Python - Scripts de utilidades]]
- [[Proyecto - Organizador de descargas]]
```

---

## EJEMPLO 2: Dos notas
**Proyecto:** Bot de Telegram que envía alertas de precios de crypto
**Decisión:** Dos notas — la lógica técnica es compleja, pero el uso es simple e independiente

### Nota 1: `Bot Telegram Crypto - MOC.md`

```markdown
---
title: "Bot Telegram Crypto - MOC"
date: 2025-03-15
tags:
  - moc
  - proyecto
  - telegram
  - crypto
type: moc
status: completo
---

## 🗺️ Qué es
Bot de Telegram que monitorea precios de criptomonedas en tiempo real y envía alertas
cuando se alcanzan umbrales configurados por el usuario.

## 📐 Arquitectura
```
[CoinGecko API] → [Monitor de precios] → [Evaluador de alertas] → [Bot Telegram]
                                                ↑
                                        [Config del usuario]
```

## 📚 Índice
- [[Bot Telegram Crypto - Implementación técnica]] — cómo está construido
- [[Bot Telegram Crypto - Manual de uso]] — cómo configurar alertas

## 📊 Estado
> [!note] Status: Completo v1.2
> Funcionando en producción. Pendiente: alertas por RSI (v2.0).

## 🔄 Versiones
- **v1.0**: alertas básicas por precio
- **v1.2**: cooldown entre alertas, múltiples usuarios

---
## 🔗 Relacionado
- [[Telegram Bots - Guía general]]
- [[CoinGecko API - Referencia]]
```

### Nota 2: `Bot Telegram Crypto - Manual de uso.md`
*(nota hija usando plantilla de Manual de Uso)*

---

## EJEMPLO 3: Sistema completo (MOC + 4 notas hijas)
**Proyecto:** Sistema de automatización CRM con n8n
**Decisión:** MOC + hijas — múltiples workflows independientes, setup complejo, varios colaboradores

### Notas a crear:
1. `Sistema n8n CRM - MOC.md` — índice y arquitectura general
2. `Sistema n8n CRM - Workflow Captación.md` — flujo de nuevos leads
3. `Sistema n8n CRM - Workflow Seguimiento.md` — secuencias de emails
4. `Sistema n8n CRM - Setup.md` — instalación y credenciales
5. `Sistema n8n CRM - Referencia webhooks.md` — endpoints y payloads

**Razonamiento:** Cada workflow puede ser editado/consultado de forma independiente.
El Setup es algo que se hace una vez y se consulta raramente. La referencia de webhooks
la necesitan integraciones externas. Sin MOC, sería imposible entender qué va con qué.
```
