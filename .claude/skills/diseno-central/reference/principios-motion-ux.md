# Principios de animación (12 de Disney) y leyes de UX
Complementa `movimiento.md` (que da los números). Aquí el porqué y cómo se traduce a UI. Usar como lista de comprobación al diseñar o revisar movimiento y flujos.

## A. 12 principios de animación → UI
| Principio | En UI | Regla concreta |
|---|---|---|
| Squash & stretch | Peso y elasticidad del elemento | Press `scale(.97)`; chips/botones al rebote ≤ `scale(1.04)`. Nunca deformar texto. |
| Anticipation (windup) | Preparar la acción antes de ejecutarla | Pequeño paso atrás (2-4 px / `scale .98`, 80-120 ms) antes de abrir o lanzar. Solo en acciones grandes. |
| Staging | Dirigir el foco | Un solo foco por momento: atenuar el resto (opacity .6, backdrop). Una animación autoral por pantalla. |
| Straight-ahead / pose-to-pose | Definir estados clave y dejar que el navegador interpole | Escribir estado inicial y final explícitos; interpolar solo `transform`/`opacity`. |
| Follow-through & overlapping | Las partes no frenan a la vez | Stagger 50-60 ms/ítem (tope 500); el contenido llega 40-80 ms después del contenedor. |
| Slow in, slow out | Aceleración natural | Curvas `ease-out` fuertes para entrar, `in-out` para mover; nunca `linear` salvo progreso/hold. |
| Arcs | Trayectorias curvas | Elementos que viajan largo (FAB, modal desde trigger): origen en el trigger (`transform-origin`) y trayecto con eje X e Y a curvas distintas. |
| Secondary action | Detalle que apoya la acción principal | Icono que cambia + color + toast a la vez, nunca compitiendo con la acción principal. |
| Timing | Ritmo = sensación | Press 100-160 · hover 150-180 · UI 240 · overlay 300-500 · salida 75 % de la entrada. |
| Exaggeration | Feedback visible | Exagerar solo el feedback de éxito/error (shake de campo inválido 4-6 px, 3 ciclos 300 ms); reduced-motion lo sustituye por color+texto. |
| Solid drawing | Volumen coherente | Sombras, perspectiva y profundidad consistentes (una sola fuente de luz; capas con elevación creciente). |
| Appeal | Carácter | Una curva propia del proyecto, reutilizada en todo; coherencia antes que variedad. |

Puerta previa (de `movimiento.md`): acción de alta frecuencia → no animar.

## B. Leyes de UX → decisiones
| Ley | Idea en cristiano | Aplicación |
|---|---|---|
| Hick | Más opciones = decidir más lento | Máx. 5-7 opciones por menú/paso; acción principal destacada; revelar progresivamente. |
| Miller | Se retienen unas 7±2 cosas | Agrupar en bloques de 3-5 (teléfonos, tarjetas, formularios por pasos). |
| Doherty | Respuesta < 400 ms mantiene el flujo | Respuesta inmediata al toque (<100 ms visual); si tarda >400 ms, skeleton/progreso; optimistic UI. |
| Postel (la «Pastel's» del texto) | Ser tolerante con lo que entra | Aceptar `+34 600 000 000`, espacios, mayúsculas; normalizar; errores que dicen cómo arreglarlo. |
| Jakob | Los usuarios esperan que funcione como otras apps | Patrones conocidos (logo → inicio, carrito arriba-derecha, buscador). Innovar en el contenido, no en la convención. |
| Frecuencia de uso | Lo frecuente, a mano | Lo usado a diario, visible y a un toque; lo raro, en menú secundario. Combina con la puerta «no animar lo frecuente». |
| Fitts (si aplica) | Objetivo grande y cercano = fácil | Zona táctil ≥ 44×44 px; acciones principales al alcance del pulgar. |

## C. Checklist rápido de revisión
1. ¿Hay un único foco y un único momento autoral por pantalla?
2. ¿Cada animación comunica estado, guía atención o da continuidad? Si no, borrar.
3. ¿Misma curva en todo? ¿Salidas más cortas que entradas?
4. ¿Respuesta < 100 ms al input y skeleton si >400 ms?
5. ¿≤ 7 opciones por decisión y patrón conocido?
6. ¿`prefers-reduced-motion` respetado y feedback sin movimiento?
