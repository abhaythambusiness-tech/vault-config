---
type: sesion
status: cerrada
date: '2026-10-28'
proyecto: '[[00 - Flujo de Software]]'
origen: mixto
---

> [!resumen] En cristiano
> Se aplicó el informe «Claude Code para micro SaaS y startups»: se guardó como nota, se creó una lista de comprobaciones antes de cobrar, se añadió un paso previo de validar demanda al flujo de software y se pusieron bloqueos de seguridad en la configuración de Claude Code.

## Qué se hizo
- Nota fuente: [[Claude Code para micro SaaS y startups]] (copia en `03_Resources/`; el original sigue en la raíz del vault, pendiente de que Haytham decida borrarlo).
- [[Checklist pre-cobro (micro SaaS)]].
- Paso 0 en [[00 - Flujo de Software]], `CLAUDE.md` §0.10 y `GEMINI.md`.
- `~/.claude/settings.json` (copia previa en `~/.claude/_backups/settings-pre-seguridad-20261028.json`): deny de `.env`, `secrets/`, claves SSH/AWS/gcloud, `terraform destroy`, `terraform apply -auto-approve` y `git push --force`; ask de `git push` y `terraform apply`.
- Hook `~/.claude/hooks/guard-destructive.py` (PreToolUse en Bash y `execute_sql` de Supabase): bloquea `DROP`, `TRUNCATE` y `terraform destroy`. Probado con tres casos.

## Aprendizajes
- Las reglas `deny` sobre Bash comparan texto y no son una frontera de seguridad (se saltan con `sh -c`); por eso el hook y, sobre todo, no dar al agente credenciales de producción.
- Los hooks se cargan al reiniciar la sesión.
