---
type: sesion
date: '2026-11-18'
proyecto: ''
origen: maquina
sesion_id: 05bd2f55-621a-48c9-8797-e6ad8a319289
tags:
- sesion
- diseno
- claude-code
- capas
---

> [!resumen] En cristiano
> Se montó el sistema de diseño de 5 capas («Ruta B») en la configuración de Claude Code: un candado que exige `PRODUCT.md` y `DESIGN.md` antes de tocar UI, la skill Taste para webs nuevas, las skills de Emil para animación, Impeccable para revisar y `stageshow`. Se probó con una web de cafetería de prueba (`prueba-cafeteria`): accesibilidad 100 y cero fallos de axe. Queda por probar `init` + `document` de verdad en un proyecto real.

## Contexto
Haytham pegó un plan por pasos (revisado por otro asistente) para migrar a 5 capas: Capa 0 puerta `PRODUCT.md`+`DESIGN.md` (hook `recordar-diseno`), Capa 1 Taste (`design-taste-frontend`, solo greenfield), Capa 2 Emil, Capa 3 Impeccable (+ hook `slop-gate`), Capa 4 `stageshow`. Ver [[03_Resources/Sistema Claude Code - Configuracion Completa]]. Continuada tras un resumen de contexto a las 21:44.

## Qué se hizo
- **Diagnóstico inicial**: faltaban skills de Emil y `stageshow`; no existía `slop-gate`; `recordar-diseno` era binario Go sin fuente localizado; Node de zsh era v18 (Taste pide ≥22); faltaba `MAX_THINKING_TOKENS`.
- **Instalado**: `stageshow` y 9 skills de Emil (`emil-design-eng`, `animate`, `review-animations`, `improve-animations`, `find-animation-opportunities`, `remove-animations`, `break-ui`, `pick-ui-library`, `prototype`, `learn-taste`). `MAX_THINKING_TOKENS=10000` en `settings.json`.
- **Hooks en Go** (`~/.claude/tools-go/cmd/`): `recordar-diseno` reescrito con tests (backup del binario viejo en `bin/_backups`), `slop-gate` nuevo (siempre exit 2 si falla `detect`, porque Claude Code solo bloquea con 2). Mensaje del hook corregido: `init` crea solo `PRODUCT.md`; `DESIGN.md` sale de `/impeccable document` (o a mano si no hay código). Escape `SKIP_CAPA0=1`.
- **Node/zsh**: `fnm` con v22.23.3 por defecto; el `eval "$(fnm env --use-on-cd --shell zsh)"` y el `PATH` de fnm se añadieron a `~/.zshrc` (backup hecho). `CHROME_PATH` apunta al symlink `~/.local/bin/chromium` (no a la ruta versionada) en `.zshrc`, `.bashrc` y `settings.json`.
- **Reglas/Docs**: `rules/diseno.md` (5 capas, solape, raíz de proyecto por `package.json` o `src/`, nota de `transition-all`, LCP gana a la estética en el primer viewport), `rules/web.md` §4 (trampas de shadcn/Tailwind/TS 7, axe en `127.0.0.1`, excepción Go para `axe-url.sh`) y `CLAUDE.md` global y del vault sin `diseno-central` en el routing (backups hechos). `diseno-central` sigue instalada solo como referencia/exportador.
- **Pruebas**: `prueba-diseno` (Capa 0/slop-gate) y `prueba-cafeteria` (web de pedido de café). Resultados: `tsc`/`vite build` limpios, Taste `lint.mjs` 0 FAIL, `inspect.mjs` 0 FAIL en 390/768/1440, `impeccable detect` limpio, axe 0 violaciones, Lighthouse Accessibility/Best Practices/SEO 100 en 375/768/1280; Performance 96/~90/90 (768: mediana de 3 pasadas = 90, TBT 200-280 ms).
- **`~/.claude/bin/axe-url.sh <URL> [--width N]`**: envoltorio bash+Node (`axe-core` + `playwright-core` en `~/.claude/tools-node/axe/`), sale 1 con violaciones critical/serious.

## Decisiones tomadas
- `transition-all` de shadcn: tras cada `shadcn add`, correr `sed -i 's/transition-all/transition-colors/g' src/components/ui/*.tsx`; si anima otra propiedad, nombrarla a mano.
- Se acepta `axe-url.sh` como excepción a la regla «scripts en Go» (solo envuelve Node).
- Performance no es bloqueante en `web.md` (sí Accessibility); el 89 de 768 no se corrige.
- Se quitó el componente Ripple de Magic UI (gradiente y sombra rompen las reglas de la casa); fallback por CLI anotado.

## Problemas
- `guard-destructive` bloquea `rm -r` fuera de `/tmp`: `.taste-skill/` de `prueba-diseno` lo borró Haytham a mano.
- Taste no clasifica el sector solo (`draw.mjs` exige `--sector`); `init` no fue interactivo ni `document` creó el archivo desde cero (se escribieron a mano).
- MCP `magicui` dio `CONNECTION_CLOSED` (transitorio; arranca a mano). Lighthouse con `localhost` da `CHROME_INTERSTITIAL_ERROR`: usar `127.0.0.1`.
- `prueba-cafeteria`: sin ficha en el vault ni README, foto genérica de Picsum, 10 tamaños de letra (deuda anotada en su `DESIGN.md`), sin vídeo y poco movimiento.

## Aprendizajes (para futuras sesiones)
- Un hook solo bloquea con exit 2; los hooks no cargan `.bashrc`/`.zshrc`, así que `slop-gate` antepone el Node de fnm al `PATH`.
- Las rutas de Chromium deben ser el symlink, no la resuelta con `readlink -f`: se rompe al actualizar.
- Una web no está «hecha» sin 375/768/1280 + axe + Lighthouse (`web.md`).

## Próximos pasos
- Primer proyecto UI real: correr `init` + `document` de verdad y comprobar que Taste clasifica el sector solo (hasta entonces valen las notas de `diseno.md`).
- Decidir si `prueba-cafeteria` se archiva o se documenta (ficha/README), y si se reescribe `axe-url.sh` en Go.
- Reflejar la migración en [[03_Resources/Sistema Claude Code - Configuracion Completa]] (hooks `slop-gate`, skills nuevas).
- En 30 días: valorar un gate automático para `transition-all`/`ease-in` (hoy lo revisa `review-animations`).

## Relacionado
- [[03_Resources/Sistema Claude Code - Configuracion Completa]]
- [[2026-11-18 - Conversor MP3 Facil: rediseno B2, PRD v2 y cierre de Capa 3 (sesion a581fb2d)]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

