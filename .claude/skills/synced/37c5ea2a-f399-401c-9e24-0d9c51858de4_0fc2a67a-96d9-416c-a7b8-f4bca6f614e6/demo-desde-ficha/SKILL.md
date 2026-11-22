---
name: demo-desde-ficha
description: >
  Convierte una ficha de servicio de NeoZeler en una demo funcional montada paso a paso,
  con datos de prueba, verificación independiente y documentación final en Obsidian.
  Úsame SIEMPRE que el usuario quiera construir, montar o preparar la demo de un servicio,
  automatización o sistema que ya tiene documentado en una nota. Actívame con frases como:
  "quiero crear la demo para esto", "monta este servicio", "ayúdame a construir esto paso a paso",
  "vamos a montar el flujo", "prepara la demo de X", "quiero implementar este servicio",
  "hazme la demo para enseñar al cliente", "montar el workflow de esta nota",
  "implementar la ficha de servicio", "pasar esto de papel a n8n".
  También actívame cuando el usuario suba una nota de servicio, ficha, guía o especificación
  y diga que quiere construirlo, probarlo o enseñarlo a un prospecto — aunque no diga "demo".
---

# Skill: De ficha de servicio a demo funcional

Conviertes una especificación escrita en una demo que funciona de verdad y que se puede
enseñar a un prospecto sin que se caiga en directo.

El principio que gobierna todo: **una demo que falla delante del cliente cuesta más que no
hacer demo**. Por eso este proceso prioriza la verificación por encima de la velocidad.

---

## FASE 0 — Leer la ficha y extraer el contrato

Antes de tocar nada, lee la nota del servicio y extrae:

| Qué buscas | Dónde suele estar |
|-----------|-------------------|
| **Qué hace el sistema** | Sección "Qué hace el sistema" — la lista numerada es tu arquitectura |
| **Stack** | Tabla de herramientas — te dice qué nodos/servicios necesitas |
| **Paso a paso** | Ya trae el orden de montaje; respétalo salvo que veas un fallo |
| **La regla que hace que funcione** | Callouts `[!warning]` o `[!tip]` — es la lógica de negocio central |
| **Errores a evitar** | 🔑 **Esto son filtros de código, no consejos.** Ver FASE 3 |
| **El gancho comercial** | Cómo se vende — condiciona qué debe verse en pantalla |

> [!important] La conversión clave
> "Errores a evitar" no es una sección informativa: cada punto es una **regla que debe
> estar implementada en el código**. Si la ficha dice "no mezcles clientes de proyecto
> único con recurrentes", eso es un `if (...) continue;` en un nodo Code, no una nota
> mental. Los errores a evitar que no se convierten en código, reaparecen en la demo.

---

## FASE 1 — Alinear antes de construir

Usa `ask_user_input_v0` (no preguntes en prosa) con estas tres preguntas:

1. **Datos**: ¿reales de un prospecto / de ejemplo inventados / aún no los tiene?
2. **Modo de ayuda**: ¿JSON listo para importar / guía nodo a nodo / ambas?
3. **Conectores**: ¿qué tiene ya conectado y funcionando?

Estas tres respuestas cambian completamente el resto del proceso. No las asumas.

**Si elige "guía nodo a nodo"**: entrega **un nodo cada vez** y espera confirmación antes
del siguiente. No adelantes tres nodos "para ir avanzando" — el usuario está montando en
paralelo y necesita ver el output de cada paso antes de continuar.

---

## FASE 2 — Datos de prueba con trampas deliberadas

Si va con datos inventados, genera el dataset con un script (Python o Node) y **mete a
propósito los problemas que aparecerán con datos reales**.

Un dataset limpio da una falsa sensación de que el flujo funciona. Un dataset sucio revela
los bugs en el taller, no delante del cliente.

Trampas que casi siempre valen la pena:

- **Entidades duplicadas con distinta grafía** (`Talleres Ruiz S.L.` / `TALLERES RUIZ SL` / `T. Ruiz`)
- **Casos borde de la lógica de negocio** (un registro con 2 datos donde el cálculo necesita varios)
- **Al menos un caso de cada categoría del resultado esperado** (unos que sí disparan, otros que no)
- **Variación realista** (usa distribuciones, no valores idénticos)

Fija la semilla aleatoria (`random.seed(42)`) para que el dataset sea reproducible entre sesiones.

Lee `references/datos-demo.md` para la receta detallada y ejemplos por tipo de servicio.

---

## FASE 3 — Definir el resultado esperado ANTES de montar

Este es el paso que más se salta y el que más caro sale.

Antes de construir el flujo, calcula **por tu cuenta** (script independiente en Python)
cuál debe ser el resultado exacto con esos datos. Guárdalo como tabla:

```
Cliente                          | pedidos | días sin comprar | ¿debe salir? | por qué
Componentes Neumáticos del Norte |      10 |              250 | SÍ           | dormido real
Suministros de Obra Redondo      |       2 |              210 | NO           | proyecto único
```

Ahora tienes un oráculo. Cuando el flujo devuelva algo distinto, sabes **inmediatamente**
si el bug está en el flujo o en tu expectativa — en vez de mirar 6 filas y preguntarte
"¿esto está bien?".

> [!tip] Por qué esto importa tanto
> Sin oráculo, el usuario te enseña un output y la única respuesta honesta es "parece
> razonable". Con oráculo, la respuesta es "faltan 2 y sobra 1, el problema es X".

---

## FASE 4 — Montar nodo a nodo

Para cada nodo:

1. **Di qué hace y por qué** en una línea antes del código o la configuración.
2. **Entrega el nodo completo**, no un fragmento a insertar. Cuando alguien tiene que
   localizar dónde pegar 3 líneas dentro de 40, se equivoca. Si hay que modificar un
   nodo ya existente, reentrega el nodo entero.
3. **Di qué debe ver el usuario** al ejecutarlo ("deberías ver ~18 clientes con sus números").
4. **Espera confirmación** antes del siguiente.

Escribe el código defensivo respecto a la fuente de datos: Airtable anida los campos en
`fields`, Google Sheets los deja en la raíz. Un helper `getField()` que cubra ambos evita
tener que reescribir el nodo cuando el usuario cambia de fuente a mitad de montaje.

---

## FASE 5 — Depurar contra el oráculo

Cuando el output no cuadre con el resultado esperado, **no pidas más capturas: replica el
cálculo en Python** con los mismos datos y compara. Es más rápido y da un diagnóstico
concreto en vez de una hipótesis.

Los tres fallos que aparecen una y otra vez en n8n:

| Síntoma | Causa casi siempre | Solución |
|---------|-------------------|----------|
| Editas un nodo y el output no cambia | Caché de ejecución de n8n | Ejecutar el flujo **completo desde el primer nodo**, no el nodo suelto |
| Aparecen entidades duplicadas o con datos raros | Nombres sin unificar en el origen | Ctrl+H en la fuente antes de calcular |
| Salen más resultados de los esperados | Falta un filtro de los "errores a evitar" | Convertir el error a evitar en código |

Lee `references/n8n-troubleshooting.md` para el catálogo completo.

> [!warning] Si un cambio no se aplica dos veces seguidas
> No repitas la misma instrucción esperando otro resultado. Reentrega el **nodo entero**
> y di explícitamente "sustituye todo el contenido del nodo por esto". Es casi siempre
> un problema de dónde se pegó el cambio, no de que el usuario no entienda.

---

## FASE 6 — Cerrar la demo

Antes de dar por terminado, comprueba:

- [ ] El resultado coincide con el oráculo de la FASE 3
- [ ] Todos los "errores a evitar" de la ficha están implementados como código
- [ ] Los nodos que envían cosas de verdad (email, WhatsApp, Telegram) están **desactivados**
      hasta que se use con un prospecto real
- [ ] Hay un nodo de depuración de output si hay IA generando texto o HTML de por medio
- [ ] El flujo escala: lo que funciona con 18 registros de prueba debe aguantar 600 reales
      (¿falta un `Limit`? ¿un filtro de umbral?)

Luego **exporta el JSON del workflow** y documéntalo.

---

## FASE 7 — Documentar

Invoca la skill `project-doc-obsidian` para generar la nota de implementación. No dupliques
esa lógica aquí.

Lo que esta skill aporta a esa documentación y que no está en ningún otro sitio:

- **Los bugs que aparecieron durante el montaje y cómo se detectaron** — es lo que evita
  repetirlos en el siguiente servicio
- **El resultado esperado (oráculo)** — para poder verificar tras cualquier cambio futuro
- **Lo que falta para producción** (trigger programado, nodos de envío activados, límites)
- **Enlace a la ficha de servicio original** — la nota de implementación es hija de la ficha,
  no la sustituye

---

## Principios que gobiernan las decisiones

**Verificar > confiar.** Un output que "parece bien" no es un output correcto. Si no tienes
con qué comparar, constrúyelo.

**Un nodo cada vez.** El usuario está montando en paralelo. Adelantarse produce confusión,
no velocidad.

**Los errores a evitar son código.** Es la conversión más valiosa de todo el proceso y la
que más se olvida.

**Los datos sucios son una funcionalidad.** Meter las trampas a propósito en el dataset de
prueba es lo que hace que la demo no se rompa con datos reales.

**La demo real se hace con datos del prospecto.** Los datos sintéticos sirven para construir
y verificar el flujo. Recuerda al usuario que el efecto comercial solo aparece cuando el
gerente ve el nombre de un cliente suyo.

---

## Referencias

- `references/datos-demo.md` — Cómo generar datasets de prueba con trampas útiles, por tipo de servicio
- `references/n8n-troubleshooting.md` — Catálogo de fallos frecuentes en n8n durante el montaje
