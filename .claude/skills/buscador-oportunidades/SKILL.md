---
name: buscador-oportunidades
description: Usar cuando Haytham no sabe qué construir o quiere ideas con base real. Cazar problemas con poca competencia y dinero, generar ideas de app, web, SaaS, micro SaaS o startup partiendo de cero, proponer funciones nuevas para una app existente, y sacar ideas de marketing e implementación técnica para una idea elegida. Frases típicas, "no sé qué montar", "busca problemas que resolver", "qué función añado", "ideas de SaaS", "nichos sin competencia", "cómo la vendo". Es la fase anterior a validar y a nuevo-proyecto.
---

# buscador-oportunidades

Genera y filtra ideas **con evidencia**. No valida a fondo ni construye: eso lo hacen `before-you-build`, `project-idea-validator` y `nuevo-proyecto`. Lenguaje sencillo (global §1): primero la conclusión, términos traducidos.

## Perfil de Haytham (no repreguntar; corregir aquí si cambia)

- Trabaja solo; dirige NeoZeler (implantación de IA en pymes, mercado Málaga). Tiempo y presupuesto disponibles: **asumidos bajos, confirmar una vez** y anotarlo aquí.
- Stack propio: TypeScript web, Supabase, Bun, `Starter SaaS` (`~/Proyectos/starter-saas`); servidor Zorin con poca RAM (medir antes de proponer algo pesado).
- Canal que ya domina: contacto directo con pymes y outbound (Laya Leads, Neozeler CRM, Perfil GTM).
- Prefiere: micro SaaS y servicio con software que cobre pronto; evitar productos que necesiten comunidad enorme, hardware o equipo.
- Ya existentes (no proponerlos de nuevo): TopLeads, Laya Leads, Neozeler CRM, Cauce, Reto 30, Laya Trader.

## Reglas

1. **Evidencia o etiqueta.** Cada afirmación lleva fuente (URL, cita corta, cifra con origen) o la marca `[hipótesis]`. Nunca inventar datos de mercado, volúmenes ni competidores. Cada fila de la tabla final lleva al menos una URL; sin URL, la fila es `[hipótesis]`. Fuente caída = decirlo.
2. **Primero cazar, luego opinar.** No proponer de memoria sin buscar señales reales (modos A y C). En modo B se parte de las preguntas, pero se contrasta antes de puntuar.
3. **Evidencia en contra antes de puntuar.** Para cada candidata, buscar por qué podría no funcionar: «<tema> failed», «<competidor> churn / cerrado», quejas de que nadie paga, mercado ya saturado. Si no se busca, la idea no se puntúa.
4. **Pocas ideas, bien filtradas.** Máximo 5 al final, ordenadas por puntuación.
5. **Cierre con acción.** Cada idea termina con la prueba más barata para comprobarla en menos de una semana, no con «construir el producto».
6. Respuesta final corta con tabla; el detalle va a una nota si Haytham lo pide.

## Memoria (leer al empezar, escribir al terminar)

Registro único: `03_Resources/Registro de Oportunidades.md` (nota del vault). **Leerlo antes de buscar** (con `obsidian-vault`) para no repetir ideas ya evaluadas ni volver a proponer las descartadas sin dato nuevo. **Al terminar**, añadir una fila por idea evaluada: fecha, idea, modo, puntos, veredicto (`seguir | probar | descartada`), motivo y enlaces. Es aditivo: no pide permiso. Tras añadir, no hace falta más papeleo salvo que se cree proyecto (entonces `nuevo-proyecto`).

## Fuentes: estado verificado el 2026-11-02

| Fuente | Estado | Uso |
|---|---|---|
| API de Hacker News (`hn.algolia.com/api/v1/search?query=...`) | Responde 200 | Buscar «alternative to», «I wish there was», «Ask HN» con `WebFetch` |
| `WebSearch` | Disponible | Fragmentos de reseñas con `site:g2.com <producto> reviews`, «<X> alternatives», «<X> too expensive» |
| `last30days` | Python 3.12.3 listo; **sin configurar** (`~/.config/last30days/` no existe: la primera ejecución lanza su asistente; avisar a Haytham antes) | Quejas recientes en Reddit, X, YouTube, TikTok, HN |
| G2, Capterra, Trustpilot, Reddit directo | **403 al acceder sin navegador.** No saltarse el bloqueo (el sistema deniega el scraping evasivo) | Pedir a Haytham que pegue el texto o una captura, o usar fragmentos de `WebSearch` |
| `anthropic-skills:google-trends-analyzer` | Sin probar | Tendencia de una búsqueda; declarar si no responde |
| Vault (`vault-search`, `02_Areas/NeoZeler/Nichos/`) | Local | Dolores de clientes y leads propios |

Para investigación larga o multi-fuente, delegar al agente `investigador`. Si una fuente falla, decirlo y seguir con las demás; nunca sustituirla en silencio.

## Elegir modo

| Situación | Modo |
|---|---|
| «No sé qué construir», «busca problemas», «nichos sin competencia» | **A. Cazar problemas** |
| Quiere montar algo pero tiene poca idea o conocimiento del sector | **B. Idea desde cero** |
| Ya hay una app o proyecto y quiere función nueva o mejora | **C. Funciones para algo existente** |
| Ya hay idea elegida y faltan marketing, precio, stack o alcance del MVP | **D. Cómo llevarla a la calle** |

Si no está claro, **una** pregunta: «¿Parto de cero, de una app que ya tienes o de una idea elegida?».

## A. Cazar problemas

Buscar dolor repetido y pagado, con las fuentes de la tabla de arriba:

- Quejas reales: frases como «odio tener que», «alguien sabe una herramienta para», «pago X pero no hace Y».
- Reseñas bajas de herramientas líderes: lo que repiten es hueco de producto.
- «Alternativas a X» y «X es demasiado caro o complejo».
- Trabajos que los freelancers cobran por hacer a mano.
- Dolores de pymes que ya conoce Haytham (clientes, leads, notas de Nichos).

**Puntuación (1 a 5 por criterio; la suma pondera el perfil de Haytham, máximo 40):**

| Criterio | Pregunta | Peso |
|---|---|---|
| Dolor | ¿Les cuesta tiempo o dinero cada semana? | ×1 |
| Pago | ¿Hay presupuesto o ya pagan algo parecido? | ×1 |
| Hueco | ¿Competencia floja, cara, vieja o inexistente? | ×1 |
| Alcance | ¿Se llega a ellos con un canal que Haytham ya domina? | ×2 |
| Construcción | ¿MVP en 2 a 4 semanas con el stack propio, solo? | ×2 |
| Recurrencia | ¿Se puede cobrar cada mes? | ×1 |

Descartar lo que saque 1 en Dolor, Pago o Alcance, aunque sume mucho, y lo que tenga evidencia en contra sin respuesta.

## B. Idea desde cero

Las respuestas del perfil ya están arriba: **no repreguntar**. Preguntar solo lo que falte y sea decisivo, en un solo mensaje: sector o problema que quiera explorar o evitar, e ingreso rápido (servicio con software) frente a producto que escale. Generar 8 candidatas en tres cubos: **micro SaaS** (una función, una persona que paga), **SaaS** (equipos, varios módulos), **servicio con software** (agencia con herramienta propia). Pasarlas por el modo A (evidencia y evidencia en contra) y quedarse con 3 a 5.

## C. Funciones para algo existente

1. Leer el proyecto: README, ficha del vault (`01_Projects/<Nombre>`), PRD y esquema si existen. No pedir al usuario lo que está en el repo.
2. Sacar el **trabajo que el usuario contrata** a la app (qué quiere conseguir, no qué botones hay).
3. Buscar huecos: funciones de la competencia que esta no tiene, reseñas de competidores sobre lo que esta podría resolver, puntos del flujo donde el usuario se atasca o abandona. Buscar también evidencia en contra (¿la gente pide esto de verdad?).
4. Proponer funciones y puntuar **Impacto** (retención, ingreso, adquisición) frente a **Esfuerzo** (horas). Tabla: función, por qué, impacto, esfuerzo, cómo se implementa (módulos y tablas tocadas, librerías ya instaladas antes que nuevas).
5. Cada función con su prueba barata: ¿cómo saber que se usa antes de pulirla?

Implementación técnica: respetar el stack del proyecto; para librerías de terceros `context7` antes de afirmar la API; esquema en Supabase → skill `supabase`.

## D. Llevarla a la calle

Para una idea ya elegida, entregar en este orden y breve:

- **Primer cliente**: quién exactamente, dónde está, cómo contactarlo esta semana. Outbound en frío → Perfil GTM (`~/.claude/skills-gtm/toggle.sh on`, sesión nueva).
- **Mensaje**: una frase de promesa y la prueba (`marketing-skills:copywriting`, `page-cro`).
- **Precio**: por valor, no por horas (`growth-diagnostic-consultant`, `marketing-skills:pricing-strategy`).
- **Canal de distribución** probable y por qué (SEO, comunidades, outbound, directorios, alianzas). El más barato primero.
- **MVP**: qué entra y qué se queda fuera; base `Starter SaaS` si encaja.
- **Riesgo mayor** y cómo comprobarlo antes de programar.

## Traspaso

Idea elegida pero sin comprobar → `before-you-build` (compra, flujo, distribución) y, si Haytham quiere dureza, agente `project-idea-validator`. Idea validada → `/nuevo-proyecto` (Paso 0 exige señal de demanda; micro SaaS: `Checklist pre-cobro (micro SaaS)`). No saltarse este paso en producto propio.

## Formato de salida

```
Conclusión: <1 frase: qué idea o función va primera y por qué>
| # | Idea | Dolor y fuente (URL) | Evidencia en contra | Hueco | Puntos /40 | Prueba barata (<1 semana) |
Fuentes que fallaron: <lista o "ninguna">
Riesgos: <1-2 líneas, con [hipótesis] donde toque>
¿Sigo con <siguiente paso>?
```

Cerrar actualizando `03_Resources/Registro de Oportunidades.md`.
