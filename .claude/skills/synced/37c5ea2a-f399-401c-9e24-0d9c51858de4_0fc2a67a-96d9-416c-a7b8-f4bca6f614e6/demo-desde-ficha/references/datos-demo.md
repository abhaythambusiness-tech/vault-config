# Generación de datos de demo

## Por qué no sirven los datos limpios

Un dataset perfecto valida que el código se ejecuta, no que el código es correcto. Los bugs
que matan una demo en directo son siempre los que vienen de la suciedad de los datos reales:
nombres inconsistentes, casos borde, registros que no encajan en la categoría prevista.

La regla: **el dataset de prueba debe contener, a propósito, cada problema que la ficha de
servicio menciona en "Errores a evitar"**. Si la ficha te avisa de algo, ese algo tiene que
estar en los datos para que puedas comprobar que lo filtras bien.

---

## Receta general

```python
import random
random.seed(42)   # reproducible entre sesiones
```

1. **Define las entidades con sus parámetros de comportamiento**, no los registros sueltos.
   Una lista de tuplas `(nombre, cadencia, importe_medio, estado_deseado)` es mucho más
   manejable que generar filas a mano.

2. **Genera hacia atrás desde el estado deseado.** Si quieres un cliente que lleve 250 días
   sin comprar, calcula su última compra como `HOY - 250 días` y genera el histórico hacia
   atrás desde ahí. Al revés es imposible de controlar.

3. **Usa distribuciones, no valores fijos.** `random.gauss(importe_medio, importe_medio*0.18)`
   produce datos que parecen reales. `importe = 2000` en todas las filas, no.

4. **Incluye al menos un caso de cada categoría del resultado esperado.** Si el sistema
   clasifica en "en riesgo / sano", necesitas ambos. Si además hay una categoría que debe
   ser filtrada antes de clasificar, también.

5. **Documenta las trampas** en la conversación cuando entregues el archivo. El usuario debe
   saber qué está a punto de encontrarse y por qué está ahí.

---

## Catálogo de trampas por tipo de trampa

### Entidades duplicadas con distinta grafía
La más universal. En cualquier sistema alimentado por un ERP o CRM, la misma empresa aparece
escrita de varias formas.

```
"Talleres Ruiz S.L."  /  "TALLERES RUIZ SL"  /  "T. Ruiz"
```

Efecto que provoca si no se limpia: la entidad se parte en varias, cada trozo tiene pocos
registros, y los cálculos agregados (medias, frecuencias) salen distorsionados. Suele
producir **falsos positivos**, que es peor que un falso negativo en una demo — enseñas al
gerente un cliente "perdido" que en realidad sigue comprando y pierdes credibilidad.

### Registros insuficientes para el cálculo
Una entidad con 2 registros donde el cálculo necesita varios para tener sentido estadístico.
Con 2 pedidos, la "frecuencia media de compra" es un único intervalo — ruido, no patrón.

Efecto: se cuela en el resultado con números que parecen válidos pero no significan nada.
Se resuelve con un umbral mínimo (`if (n < 4) continue;`).

### Casos que deben quedar fuera por naturaleza
Clientes de proyecto único, pedidos internos, devoluciones, cuentas de prueba. Todo sistema
real los tiene y todo informe se ensucia con ellos.

### Extremos de la escala
Una entidad muy grande y una muy pequeña. Verifica que la lógica de priorización o
puntuación se comporta razonablemente en los dos extremos y que el orden final tiene sentido.

---

## Adaptación por tipo de servicio

| Tipo de servicio | Qué genera | Trampas propias |
|------------------|-----------|-----------------|
| **Análisis de histórico** (radar de clientes, alertas de stock) | Series temporales por entidad | Grafías duplicadas, entidades con pocos registros, extremos de escala |
| **Procesamiento de entradas** (pedidos por email/WhatsApp, tickets) | Mensajes de texto realistas | Mensajes ambiguos, sin datos clave, en varios formatos, con erratas |
| **Enriquecimiento / clasificación** (leads, categorización) | Registros con campos incompletos | Campos vacíos, valores fuera de catálogo, duplicados parciales |
| **Cruce de fuentes** (conciliación, matching) | Dos datasets con solapamiento parcial | Registros que están en uno y no en otro, coincidencias parciales |

---

## Formato de entrega

Entrega el CSV (o el formato que pida el stack de la ficha) como archivo descargable, y en
el mensaje explica:

- Cuántos registros y cuántas entidades
- Qué trampas lleva y por qué están ahí
- Qué debería pasar con cada trampa cuando el flujo esté bien montado

Esto último es el germen del oráculo de la FASE 3 del SKILL.md.
