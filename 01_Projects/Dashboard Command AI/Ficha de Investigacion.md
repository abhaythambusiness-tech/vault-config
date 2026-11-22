---
type: ficha-investigacion
proyecto: Dashboard Command AI
tipo: saas
status: aprobada
date: 2026-11-05
origen: mixto
---

> [!resumen] En cristiano
> Piezas ya hechas que usa el panel, herramientas de Claude por fase y con qué compararlo. Hecha después de construir (el proyecto arrancó como prueba rápida), así que recoge lo que de verdad se usó. Pendiente de que Haytham la apruebe.

# Ficha de Investigación

## Librerías
| Necesidad | Candidata A | Candidata B | Elegida y motivo | Fuente |
|---|---|---|---|---|
| 3D en navegador | Three.js | react-three-fiber | **Three.js 0.170**: sin React, un solo bundle pequeño | `[[NeoZeler Mundo]]` |
| Compilar | Vite | esbuild a mano | **Vite 5 + TypeScript**: stack estándar de `rules/web.md` | rules/web.md |
| Servidor | Node `http` + `ws` | Express / Bun | **Node `http` + `ws` 8.18**: un proceso, dos dependencias | package.json |
| Etiquetas sobre el 3D | CSS2DRenderer | sprites de textura | **CSS2DRenderer**: texto real, accesible y clicable | three/examples |
| Reflejos | RoomEnvironment (PMREM) | HDRI externo | **RoomEnvironment**: 0 descargas | three/examples |

## Skills y agentes
- Diseño: `diseno-central` (Operate), `threejs-*` (13, CloudAI-X/threejs-skills; instaladas 2026-11-05), `impeccable` para pulido.
- Verificación: Chrome headless (swiftshader) por CDP, porque el panel integrado no tiene WebGL.
- Cierre: `archivista`, `auditor-web` + `revisor-codigo` + `ponytail-audit` (auditoría puntual).

## Referencias
- animejs.com (dinamismo con personalidad, ver memoria de diseño).
- Dashboards 3D tipo mission-control de Linear/Vercel: sobriedad, vidrio, color solo en lo accionable. Pendiente enlazar dos concretas desde [[Biblioteca de Referencias Premium]].

## Lecciones aplicables
- El panel integrado no tiene WebGL: no dar el 3D por visto sin captura headless.
- Cambiar ids del servidor exige reiniciarlo; cliente nuevo contra servidor viejo falla.
- Blanco quemado = luces + entorno + suelo claro + bloom a la vez.

## Extras de la vía
### saas
Dos usuarios fijos (Haytham, Sam), sin multi-equipo. Sin `PIN_ACCESO` no hay autenticación real: no abrir a la red sin él. `/api/proyectos` da 403 a Sam (datos del vault).

- Pendiente: PIN para red local y login de la CLI de Claude.
