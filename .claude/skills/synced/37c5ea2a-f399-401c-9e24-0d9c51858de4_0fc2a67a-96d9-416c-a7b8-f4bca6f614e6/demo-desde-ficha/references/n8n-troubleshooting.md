# Troubleshooting durante el montaje en n8n

Catálogo de fallos que aparecen al construir una demo nodo a nodo. Ordenados por frecuencia
real, no por gravedad.

---

## 1. Editas un nodo y el output no cambia

**Síntoma**: aplicas una corrección al código de un nodo, ejecutas, y el resultado sigue
siendo idéntico al anterior.

**Causa**: n8n conserva el resultado de la última ejecución de cada nodo. Ejecutar un nodo
suelto usa el input cacheado, y los nodos posteriores siguen mostrando su resultado viejo.

**Solución**: ejecutar el workflow **completo desde el primer nodo**. Decirlo así de
explícito — "no ejecutes solo ese nodo" — porque es contraintuitivo.

**Cómo distinguirlo de un bug real**: si el output es *exactamente* igual, incluidos los
decimales, es caché. Si cambió algo pero no lo esperado, es bug.

---

## 2. El cambio no se aplicó donde tocaba

**Síntoma**: has pedido añadir una línea a un nodo y tras ejecutar el flujo completo sigue
sin tener efecto.

**Causa**: la línea se pegó en otro nodo, o dentro de un bloque que no se ejecuta (después
de un `continue`, fuera del bucle, en el nodo de cálculo en vez del de filtrado).

**Solución**: **reentregar el nodo completo** y decir "sustituye todo el contenido del nodo
por esto". No repetir la instrucción original — no funcionó por una razón, repetirla no la
cambia.

**Prevención**: entregar siempre nodos completos en vez de fragmentos a insertar, sobre todo
a partir del segundo cambio sobre el mismo nodo.

---

## 3. Estructura de datos distinta según la fuente

**Síntoma**: el código funciona con Google Sheets y devuelve vacío con Airtable (o al revés).

**Causa**: Airtable anida los campos dentro de `json.fields`; Google Sheets los deja en la
raíz de `json`.

**Solución**: helper defensivo desde el primer nodo Code:

```javascript
function getField(item, name) {
  return item.json.fields ? item.json.fields[name] : item.json[name];
}
```

Merece la pena aunque solo se vaya a usar una fuente: el usuario puede cambiar de origen a
mitad de montaje sin avisar.

---

## 4. Salen más resultados de los esperados

**Causa habitual**: falta implementar uno de los "errores a evitar" de la ficha de servicio.

**Diagnóstico**: comparar contra el oráculo. Identificar qué registros sobran y qué tienen
en común. Casi siempre son una categoría entera que debería filtrarse antes.

---

## 5. El output de la IA no es utilizable directamente

**Síntoma**: el nodo de IA devuelve el contenido correcto pero envuelto en fences de markdown
(` ```html `), precedido de "Aquí tienes el informe:", o como documento HTML completo cuando
solo se pedía el cuerpo.

**Solución**: nodo Code de depuración después de la IA, **siempre**, aunque el prompt ya lo
prohíba explícitamente. El prompt reduce la frecuencia; no la elimina.

El nodo debe cubrir:
- Extracción del texto desde las distintas rutas posibles del output según versión del nodo
  (`message.content`, `choices[0].message.content`, `content`, `text`, `output`)
- Eliminación de fences de markdown
- Extracción del contenido de `<body>` si viene documento completo
- Eliminación de texto suelto antes de la primera etiqueta

---

## 6. Un solo item cuando se esperaban varios (o al revés)

**Causa**: confusión entre "Run Once for All Items" y "Run Once for Each Item" en el nodo
Code, o falta/sobra un nodo `Aggregate`.

**Regla práctica**:
- Cálculos que agrupan o comparan entre registros → **Run Once for All Items**
- Enviar todo junto a un nodo de IA para que redacte un único texto → **Aggregate** antes
- Generar un texto por cada registro → sin Aggregate, y el nodo de IA se ejecuta N veces

---

## 7. Nodos de envío disparando durante las pruebas

**Prevención**: mantener desactivados (`disabled: true`) los nodos de Gmail, Telegram,
WhatsApp o cualquier acción con efecto externo hasta que la demo esté verificada. Activarlos
es el último paso, no el primero.
