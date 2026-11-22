---
type: doc-software
doc: paleta-componentes
proyecto: "Grid64"
status: aprobada
date: 2026-11-08
origen: mixto
---

# Paleta de componentes — Grid64

> [!resumen] En cristiano
> Grid64 **no usa librerías de componentes** (ni shadcn ni Magic UI): no hay React, y la pieza central, la «piedra» sobre el tablero, es propia de la marca. Todo se hace con Alpine.js y CSS propio. Aprobado por Haytham el 2026-11-08 («Sí, aprobada como no aplica»).

## 1. Insumo
Idea visual central: tablero de Go, la piedra se rellena y se asienta ([[3 - UI-UX Design]] §2, §7). Adjetivos: calmado, preciso, motivador.

## 2. Registries buscados
Ninguno: no aplica. Stack sin React ni Tailwind de componentes ([[2 - TRD]] §1; [[3 - UI-UX Design]] §4).

## 3. Elección por sección
| Sección / pantalla | Componente | Registry | Por qué encaja | Peso / motor | Alternativa descartada |
|---|---|---|---|---|---|
| Inicio | Métricas, tarjeta de objetivo, lista de hoy | propio | datos reales del tablero | CSS | tarjetas shadcn (genéricas) |
| Mandalas | Piedra, anillo de pilar, panorama 9×9, enfoque 3×3 | propio | es la identidad | CSS + Web Animations | cualquier registry |
| Ideas | Lista con filtros y conversión | propio | vocabulario de Airtable (§9 UI-UX) | CSS | n/a |
| Todas | Hoja inferior, barra de pestañas | propio | gestos móviles | CSS | n/a |

## 4. Control anti-parecido
Sin componentes de registry, no puede repetir los de otros proyectos. Una sola librería de movimiento: ninguna (CSS y Web Animations).

## 5. Instalación
Ninguna. Alpine.js 3.17.5 local (`frontend/alpine.min.js`).
