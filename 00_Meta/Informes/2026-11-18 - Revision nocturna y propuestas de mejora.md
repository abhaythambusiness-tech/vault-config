---
type: informe
status: pendiente-revision
origen: maquina
date: '2026-11-18'
---

# Revisión nocturna 2026-11-18

> [!resumen] En cristiano
> **URGENTE: el disco está al 97 % (18 GB libres) y se llena en menos de un día.** Un archivo de registro del sistema (`/var/log/syslog`) pesa 92 GB porque un temporizador de ComandAi intenta copiar al servidor equivocado (IP .100, el servidor es .101) cada ~10 s y falla sin parar. Hay que parar el temporizador, corregir la IP y vaciar el log (nº 152). Aparte: 1 archivo movido de la raíz, 2 hallazgos de harness más (nº 152-154), 6 propuestas (nº 155-160) y 4 apuestas (nº 161-164).

## 2. Raíz ordenada

| Origen | Destino | Deshacer |
|---|---|---|
| `logo arm.png` (3,7 MB; ningún .md lo enlaza) | `99_Assets/Imagenes/logo arm.png` | `mv "99_Assets/Imagenes/logo arm.png" .` |

Sin mover: `Sin título.canvas`, `Sin título 1.canvas` (2 bytes, vacíos, no clasificables) y `Compartido/` (carpeta del MCP `compartido`, no es un suelto). `git status --short`: 238 entradas (sin commit desde 2026-11-13 20:30).

## 3. Estado del vault (solo propuestas)

| Prioridad | Hallazgo | Acción propuesta | Riesgo |
|---|---|---|---|
| Alta | 238 cambios sin commit, último commit 13-nov; sin cron/timer de commit (refuerza nº 111 y 60). | `vault-commit` en Go. | Bajo |
| Media | `00_Inbox/`: `2026-10-13_1223_preparacion-con-carlos.md` y `Plan futuro de aqui 3 años.md` sin clasificar. | Haytham los clasifica. | — |
| Baja | Informe «Salud del vault» 16-nov: 1 enlace roto (`2026-11-14 - Obsidian tema Rho Zero legible…` → nota del 13-nov) y 48 huérfanas. No re-medido hoy. | Corregir el enlace; enlazar huérfanas desde MOCs. | Bajo |
| Baja | Estados de `01_Projects/` sin lista cerrada (decisión abierta §7). | Aprobarla. | Bajo |

## 3B. Auditoría del harness

Medido hoy: `/` 97 % (18 GB libres; ayer 91 %, 41 GB). Claude Code 2.1.323 (existe 2.1.327). Skills: 59 invocaciones en 30 días, 43 de `diseno-central`; 59 de 63 activas sin uso (poda: **2026-12-04**, aún no toca). `sync-gemini --check`: al día. `~/.claude` 9,3 GB (`projects` 1,7 GB, `plugins` 1,3 GB); `~/.cache` 16 GB, `~/.npm` 14 GB. `cost-tracker.log` sigue sin escribirse desde 2026-10-25 en lo visible (nº 136 abierto). `MEMORY.md`: 14 líneas, 18 archivos. No se re-midió `list_task_runs` (herramienta pide `taskId`).

| nº | tipo | hallazgo y evidencia | impacto | esfuerzo | recomendación |
|---|---|---|---|---|---|
| 152 | punto ciego | `ls -l /var/log/syslog` = 92.039 MB; `syslog.1` = 6.737 MB. Causa (CTO): `comandai-sync.timer` (activo, comprobado) dispara `~/.config/systemd/user/comandai-sync.service` cada ~10 s; `~/Proyectos/comandai/scripts/sync-panel.sh` línea 8: `COMANDAI_REMOTO` por defecto `ssh@192.168.0.100:comandai-panel/` (Zorin es .101) → fallo y 5-6 líneas de log cada vez (~2.250 fallos en las últimas 20.000 líneas). | Disco lleno en <1 día: caerían Claude Code, vault, git y n8n. Libera ~99 GB | S | **Aplicar ya, en sesión aparte con permiso:** `systemctl --user stop comandai-sync.timer`; corregir IP a .101; `sudo truncate -s 0 /var/log/syslog` (borrado, requiere sí de Haytham). |
| 153 | regla | Sin tope de logs: ni `SystemMaxUse` (journald) ni `maxsize` en logrotate para syslog; el timer no tiene backoff. | Evita repetir nº 152 | S | Tope `maxsize 1G`; en el servicio, `RestartSec` largo u `OnFailure`. |
| 154 | script | El salto 91 % → 97 % pasó sin aviso (refuerza nº 110). | Aviso a tiempo | S | Go: `df /` >90 % avisa; timer horario. (Apuesta nº 161 lo amplía.) |

Cachés recuperables (CTO, informativo; refuerza nº 131): `~/.cache/uv` 11 GB, `~/.npm` 13 GB (`_cacache` 9,6 GB), `~/Descargas/Comprimidos` 21 GB, `~/Proyectos/archive` 7,7 GB, Steam 89 GB. Con permiso: `uv cache prune`, `npm cache verify`.

**Ahorro de tokens estimado**: sin medir (esta noche no hubo hallazgos de arranque nuevos).

**Candidatos a script/hook (Go)**: `nz guard` (152-154, 161), `vault-commit` (111), compresor de transcripciones (132).

## 4. Propuestas de mejora

| nº | área | propuesta | beneficio | coste/riesgo | fuente | recomendación |
|---|---|---|---|---|---|---|
| 155 | Servicio | Piloto de 30 días con línea base: la clínica da ausencias y ticket medio antes; al final, informe en € (citas × ausencias × ticket); setup se cobra al cerrar | Cifras propias en vez de las de proveedores; justifica precio por valor | Puede que la clínica no tenga datos | CEO; [Aurora Inbox](https://www.aurorainbox.com/chatbot-clinicas-dentales-whatsapp/) (fecha sin confirmar; fuente de proveedor) | probar con 1 clínica |
| 156 | Captación | Medir a mano en 10 de los 106 leads tier A cuánto tardan en contestar un WhatsApp de noche; enviar el dato al dueño | Gancho con dato propio | Es un mensaje externo: permiso de Haytham y consulta al gestor (LSSI/RGPD) | CEO | probar, solo tras revisar el texto |
| 157 | Flujo vault | Rellenar `Contexto NeoZeler` §6 (precio, garantía, nicho, capacidad, objetivo trimestre; sigue `borrador` desde 2026-11-10) y pasarla a `activo` | Todos los agentes leen datos firmes | Obliga a decidir | CEO | aplicar (20 min con Sam) |
| 158 | Seguridad | Poner `CLAUDE_CODE_DISABLE_SHELL_HEAD_START=1` en el entorno: en 2.1.327 los archivos de arranque del shell pueden ejecutarse antes de aprobar el primer Bash | Cierra un hueco | Toca settings/entorno | [changelog](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md), leído hoy | probar (sesión aparte) |
| 159 | Harness | Actualizar a 2.1.327: `claude mcp add-json <nombre> -` lee por stdin (token fuera de la línea de comandos) y arregla que `mcp add/remove` borraba claves de `.mcp.json`. Refuerza nº 135/137 | Seguridad y menos fallos | Probar guards tras actualizar | changelog | aplicar |
| 160 | Limpieza | `uv cache prune` y `npm cache verify` (~20 GB) | Disco | Cachés, se regeneran; permiso | CTO | aplicar tras nº 152 |

Skills de n8n, Obsidian, SEO, ventas, Go y WhatsApp en skills.sh: la tabla por tema carga con JavaScript y vino vacía; no se afirma nada. Solo el ranking global (find-skills 4,4 M, grill-me, design-mobile-apps…) sin descripciones fiables.

## 4B. Apuestas atrevidas

Ronda de reto: no se hizo ronda cruzada CEO↔CTO esta noche (se consultaron en paralelo); la «prueba» de cada apuesta queda en su fila.

| nº | idea | por qué es atrevida | experimento ≤1 día | riesgo y reversión | coste | apuesta |
|---|---|---|---|---|---|---|
| 161 | **Guardia de disco y bucles** (`nz guard`, Go): cada 5 min mira `/var/log`, servicios en `failed` repetido y `df`; si algo falla más de N veces/hora, para esa unidad y deja nota en el Panel | Actúa solo, no solo avisa | Simular un servicio de prueba que falla cada 10 s, en directorio temporal | Para algo necesario: solo unidades de usuario, lista permitida, `systemctl --user start` | 0 € | 3 · probar en sandbox |
| 162 | **Copia que se prueba sola**: cada noche Go clona el vault desde la copia a temporal y comprueba que `graphify` y `vault-search` responden | Prueba la restauración, no solo la copia | Una noche, en `/tmp`, sobre copia de solo lectura | Ocupa disco (cuidado con el 97 %); borrar temporal | 0 € | 4 · probar tras liberar disco |
| 163 | **Precio publicado con garantía**: «si Mila no agenda X citas en 30 días, no pagas la mensualidad» | Solo 10 de 115 rivales publican precio (estudio del vault 2026-11-10) | Con conversaciones reales del setter, calcular la X que cubre el 80 % de casos | X mal calculada = meses gratis; revertir = no publicar | ~0 € | 3 · probar en sandbox |
| 164 | **Publicar la tasa de errores de Mila**: 50 conversaciones sintéticas difíciles (dolor, urgencia, queja, precio) con un LLM como juez | Nadie enseña sus fallos | Ejecutar las 50 y medir cuántas veces deriva a humano cuando debe | Si sale baja, solo se arregla el prompt; nada se publica | unos € de tokens (sin medir) | 2 · probar en sandbox |

Precedentes (investigador): memoria que se cura sola: «Auto Dream» de Claude Code (fuentes contradictorias, sin confirmar, [levelup](https://levelup.gitconnected.com/your-ai-coding-agent-now-needs-sleep-heres-what-dream-actually-does-81d32977ec25), mar-2026) y «Dreaming» para Managed Agents (6-may-2026, fuente secundaria [inventivehq](https://inventivehq.com/blog/claude-agents-dreaming-explained)). Pago por resultado en salud: [Novoflow](https://ai.novoflow.io/success-based-pricing-medical-ai-automation) (web del vendedor); modelo habitual híbrido ([MedCity](https://medcitynews.com/2026/03/ai-startups-hospitals-healthcare/)). Para WhatsApp de clínicas dentales no hay oferta de pago por cita: solo cuota mensual (p. ej. [Hyperleap](https://hyperleap.ai/dental-agents), 40-200 USD/mes). Hueco posible, sin demanda probada. Normativa: guía AEPD de agentes de IA (feb-2026) vía [Ecija](https://www.ecija.com/actualidad-insights/agentes-de-ia-y-tratamiento-de-datos-personales-las-claves-de-la-nueva-guia-de-la-aepd/) (fecha sin confirmar).

## 5. Novedades de internet (18-nov)

- Claude Code 2.1.327 (únicas versiones nuevas sobre 2.1.326; fecha no visible): `mcp add-json -` por stdin, arreglo de `.mcp.json`, ajuste `attributionProject`, confirmación nueva en `/export` y `ExitWorktree`, cambio de seguridad del shell (nº 158). [Changelog](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md).
- Diseño web: guía de Fireart actualizada el 2-nov-2026 (texto como elemento principal, [fuente](https://fireart.studio/blog/the-best-web-design-trends/)); titulares enormes, fuentes variables y texto cinético ([Line25](https://line25.com/articles/web-design-trends-2026/)); 3D con Spline/R3F sin dañar velocidad ([Lovable](https://lovable.dev/it/guides/website-design-trends-2026)). Todo blogs de agencias que venden lo que recomiendan; sin informe fiable de noviembre.

## 6. Lo que NO se hizo / límites

- Nada aplicado salvo el movimiento de `logo arm.png`. No se paró el timer ni se tocó el log (pide permiso y es un borrado).
- Verifiqué yo mismo: tamaño de `syslog`, timer activo, IP en `sync-panel.sh` y 97 %. El resto de cifras del CTO (Steam, uv, npm, Comprimidos) no se re-midió.
- No se re-midieron enlaces rotos/huérfanas ni `list_task_runs`. No se comprobó si nº 155-164 repiten pruebas ya hechas en `Setter robustez` (sesión 17-nov, no leída). No se leyó el informe del 17-nov completo por el CTO; la numeración la he comprobado yo (continúa en 152).
- skills.sh: sin búsqueda por tema.

## 7. Siguiente paso

Haytham marca por nº qué se aplica. **Primero el 152 (hoy, antes de que se llene el disco).** Tocan settings/hooks/entorno o borran datos (sesión aparte con permiso): 152, 153, 154, 158, 159, 160, 161, 162.

Límites activados: ninguno (≈14 llamadas, 3 agentes).

