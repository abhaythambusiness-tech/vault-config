# Plantilla — `Servicio - {Nombre}.md`

Ficha comercial. Se lee en frío antes de una reunión. Longitud objetivo: 1-2 pantallas.
Copia esta estructura tal cual, en este orden, sin añadir ni quitar secciones.

---

```markdown
---
title: "Servicio - {Nombre}"
date: {YYYY-MM-DD}
tags:
  - ia
  - automatizacion
  - neozeler
  - guia
type: guia
status: borrador | en-progreso | completo
related:
  - "[[NeoZeler - MOC de Servicios]]"
  - "[[Nicho - {Nicho}]]"
---

## 📊 Ficha rápida

| Campo | Valor |
|-------|-------|
| **Nicho** | [[Nicho - {Nicho}]] |
| **Dificultad** | 🟢 Baja (X días) / 🟠 Media (X semanas) / 🔴 Alta (X semanas) |
| **Impacto en el cliente** | 🟢🟠🔴 + media frase de por qué |
| **Impacto comercial para ti** | 🟢🟠🔴 + media frase (¿la demo entra por los ojos?) |
| **Precio orientativo** | X-Y € montaje + Z €/mes |
| **Prioridad** | **#N** |

> [!tip] En una frase
> Qué hace el sistema, contado como se lo contarías al gerente en el pasillo.
> Sin nombres de tecnología.

## 🧠 El problema, en cristiano

Dos o tres párrafos. Primero **quién sufre el dolor** (el rol concreto: el comercial
interno, el jefe de tráfico, la persona de oficina). Luego **qué hace hoy**, con detalle
suficiente para que se note que conoces el sector. Termina con **cuál es el coste real**,
que casi nunca es el sueldo: es la venta que no se hace, el margen que se quema o el
cliente que se va.

## 🧩 Conceptos del nicho que debes manejar

Lista de 4-6 términos que el cliente usará en la reunión y que tú debes entender.
Formato: **Término**: qué es, en una o dos líneas, con el matiz que importa.
Esta sección es para ti, no para el cliente. Es la que evita que te pillen fuera de sitio.

## ⚙️ Qué hace el sistema

Lista numerada de 5-8 pasos, contada desde el punto de vista del usuario final, no del
flujo técnico. Empieza siempre por el disparador real ("el cliente escribe por WhatsApp...").
**El penúltimo paso es siempre la validación humana** de lo que toque dinero o compromiso.
**El último paso es siempre el escalado a persona** cuando algo se sale de lo normal.

## 🛠️ Stack

| Pieza | Herramienta | Coste |
|-------|-------------|-------|
| Motor | n8n (autoalojado) | Gratis |
| Canal | ... | Gratis |
| ... | ... | ... |

Una fila por pieza. La columna de coste es obligatoria y honesta: "Gratis",
"Céntimos por conversación", o el importe real si hay que pasarlo al cliente.

> [!note] {Decisión de diseño / limitación conocida}
> Opcional pero recomendable: si has descartado una variante del servicio, si hay una
> pieza que cuesta dinero, o si hay algo que este servicio deliberadamente no hace,
> se escribe aquí y se explica por qué.

## 🔗 Relacionado
- [[Demo - Servicio - {Nombre}|🔗 Ver montaje de la Demo]]
```

---

## Qué NO va en la ficha

- Pasos de montaje, nodos de n8n o detalles de implementación → van en la nota de demo.
- El guion de venta → va en la nota de demo, sección "Cómo lo vendes".
- Justificación de por qué el nicho es bueno → eso ya está en la nota de nicho, enlázala.
