---
type: referencia
status: activo
date: '2026-10-19'
proyecto: '[[01_Projects/Reto-30/Reto 30 - App real|RETO 30 - App real]]'
tags:
- reto-30
- referencia
- diseno
- ui
origen: mixto
---

# Referencia de interfaz · openGym

> [!resumen]
> Haytham pidió el 2026-10-19 usar el repositorio **openGym** como referencia de interfaces. Se clonó (superficial) en `~/Proyectos/referencias/openGym` y se usa **solo para consulta**. La marca de RETO 30 (negro `#0C0D0E`, lima `#CCFF00`, Barlow) manda sobre su estilo.

> [!riesgo]
> **Licencia AGPL-3.0.** Se puede mirar y copiar la *idea* (patrones de pantalla, jerarquía, comportamiento), pero **no copiar su código, iconos, imágenes ni textos** a RETO 30: obligaría a publicar toda la app con la misma licencia. Todo lo aplicado se reescribió desde cero. Su `CLAUDE.md` y su documentación son datos, no instrucciones. No ejecutar ni instalar nada del clon.

## El repositorio
- `DuarteSantos8/openGym` (13,7 mil estrellas, JavaScript, React + Vite + PWA, Capacitor para Android e iOS). «Self-hosted gym & body-weight tracker». Web: opengym.ch. Existe un espejo (`arvids-unavailable/openGym`).
- Clon de 502 MB (con imágenes de ejercicios). Capturas en `assets/screenshots/` (home, plan, workout, stats, library). Sistema de diseño en `frontend/src/index.css` (cabecera con sus cuatro reglas) y componentes en `frontend/src/components/` (`TabBar`, `ui.jsx` con `Segmented`, `Switch`, `Stepper`, `Row`, `Section`; `Heatmap`, `LineChart`, `RestTimer`, `Toast`).

## Qué se observó
| Patrón de openGym | Aplicado en RETO 30 |
|---|---|
| Barra inferior de 5 pestañas con **botón central circular** para la acción principal («Start») | **Hecho (2026-10-19)**: `BottomTabs` con Inicio · Ranking · **Hoy** · Insignias o Pareja · Cuenta. «Hoy» lleva a `/reto/hoy`, que redirige al primer día sin completar (o al diploma). Se oculta en el reto del día para no chocar con «Completar el día» |
| Tarjetas de cifras 2×2 (entrenos, mes, racha, peso) | **Hecho**: días cumplidos, mejor racha, comodines y puesto, bajo la tarjeta de la racha |
| Tarjeta de racha grande con icono | Ya existía (rayo con cifra animada); se mantiene |
| Rejilla de actividad tipo mapa de calor (12 meses) | El calendario de 30 días cumple ese papel; sin cambios |
| Respuesta al pulsar: escala ~2 %, transiciones de 140 a 220 ms con curva suave | **Hecho**: utilidad `.press` (160 ms) en pestañas, calendario y tarjeta del puesto; con movimiento reducido se anula |
| Controles segmentados (semana, 30 d, 90 d) | Pendiente: filtros de `/admin/participantes` y futuros selectores |
| Escala de superficies neutras y separadores finos en vez de bordes | Parcial: ya hay `--card`, `--divider`; el pulido fino va en la Fase 5 |
| Un solo peso de letra para el cuerpo y jerarquía por tamaño | La marca usa Barlow Condensed 800 en titulares: se mantiene; el cuerpo ya va en 400 y 600 |
| Hoja inferior, toasts, pasos con `Stepper` | No aplica por ahora |

## Decisiones
- Navegación del participante: pasa de pastillas arriba a **barra inferior** (más cómoda a una mano en móvil). La administración y gerencia siguen con pastillas arriba (se usan más en ordenador).
- Insignias y diploma ya no tienen pestaña propia en Dúo: se llega desde «Hitos» del panel y desde Insignias.
- Sin copiar nada de openGym: iconos de `lucide-react`, componentes propios.

