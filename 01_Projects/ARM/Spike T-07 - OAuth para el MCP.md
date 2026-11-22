---
type: doc-software
doc: spike
proyecto: ARM
status: completa
date: '2026-11-17'
origen: mixto
---

# Spike T-07 — ¿Claude.ai y ChatGPT aceptan una clave fija?

> [!resumen] En cristiano
> **No (según la documentación y las incidencias que he leído).** Los conectores remotos de Claude.ai y ChatGPT esperan que el servidor tenga un «inicio de sesión» estándar (OAuth), no una clave pegada. Con la clave fija de ARM sí funcionan Claude Code, Claude Desktop (con un puente) y herramientas para programadores. Para que el cliente final lo conecte desde Claude.ai o ChatGPT, ARM necesita un OAuth mínimo. **No lo he probado en las aplicaciones reales**: es lectura de documentación, no una prueba.

## Qué encontré
- **Claude.ai**: los conectores personalizados siguen un flujo OAuth (callback `https://claude.ai/api/mcp/auth_callback`), con registro dinámico de cliente (DCR) o con ID y secreto introducidos a mano en «Advanced settings». No encontré ninguna opción de clave fija; hay una petición abierta para añadir «sin autenticación». Varias incidencias reportan fallos justo después del callback.
- **ChatGPT (modo desarrollador)**: tres opciones, OAuth, sin autenticación y mixta. Tampoco hay «cabecera Bearer con mi clave». Los planes que permiten escritura: las fuentes no coinciden, comprobar antes de prometerlo.
- **Claude Desktop** con servidores locales o con un puente (`mcp-remote`) sí admite cabecera con clave; **Claude Code** también (`--header`).

## Decisión propuesta
| Opción | Qué da | Coste | Riesgo |
|---|---|---|---|
| A. Solo clave (hoy) | Claude Code, Desktop con puente, scripts | 0 | El cliente normal no puede conectar desde Claude.ai/ChatGPT |
| **B. OAuth mínimo en ARM (recomendada)** | Claude.ai y ChatGPT | Medio: metadatos del recurso protegido, registro dinámico de clientes, `/authorize` (el cliente entra con su usuario de ARM y elige permisos), `/token` con PKCE; el token equivale a una clave de ARM con alcances | Hay que probarlo con las apps reales; fallos conocidos tras el callback |
| C. «Sin autenticación» con la clave en la URL | Conecta fácil | Bajo | **Inseguro**: la clave queda en historiales y registros. Descartada |

El `go-sdk` incluye el paquete `auth` (metadatos del recurso protegido y verificación de token) que ayuda con la mitad del trabajo.

## Siguiente
Tarea nueva **T-07b** (tras T-10, porque necesita el login web de ARM): OAuth mínimo + prueba con Claude.ai y ChatGPT reales. Hasta entonces, la guía de «Conexiones» ofrece Claude Code y Claude Desktop.

> [!riesgo]
> La v1 (fases 0-5) puede cerrarse con la opción A y un cliente real; el OAuth no debe bloquear la entrega del Setter.

## Fuentes
- [Conectores personalizados de Claude (ayuda de Anthropic)](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp.md)
- [Incidencias de claude-ai-mcp](https://github.com/anthropics/claude-ai-mcp/issues/212) y [Twenty #19847](https://github.com/twentyhq/twenty/issues/19847)
- [ChatGPT Developer mode (OpenAI)](https://developers.openai.com/api/docs/guides/developer-mode.md)

