# Configuración de Claude Code + OpenCode + Vault (Shareable)

Esta es una configuración limpia y compartible de mi setup de Claude Code y OpenCode, junto con mi vault personal organizados con el método PARA. **Ha sido limpiado de datos personales de NeoZeler** para que puedas usarlo como plantilla.

## ⚠️ Importante

Este repositorio ha sido creado **SIN tus datos personales de NeoZeler**. Los directorios que contenían información sensible o específica de NeoZeler han sido excluidos o eliminados. Lo que tienes aquí es la estructura base y las configuraciones generales que puedes adaptar.

## 📋 Estructura

```
vault-share/
├── .gitignore          # Patrones de exclusión para GitHub
├── CLAUDE.md           # Guía operativa del vault (global)
├── GEMINI.md           # Estilo y routing esencial
├── .mcp.json           # Configuraciones de MCPs (dropshipping, marketing, etc.)
├── 00_Meta/            # Metadatos e instrucciones generales
├── 01_Projects/        # Proyectos variados (limpiados de NeoZeler)
├── 02_Areas/           # Áreas de responsabilidad
├── 03_Resources/       # Recursos de referencia
├── 04_Archive/         # notas archivadas
├── 99_Assets/          # Recursos assets
└── .claude/            # Configuración local de Claude Code
```

## 🚀 Cómo clonar y usar

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/vault-config.git
cd vault-config
```

### 2. Configura tus MCPs

Este repositorio incluye configuraciones de MCPs útiles para agencias de IA yautomatización. Para activarlos:

```bash
/mcp enable supabase
/mcp enable mcp-marketing
/mcp enable mcp-dropshipping
```

### 3. Configura Claude Code

Copia tu propia configuración personal:

```bash
# Copiar tus archivos .claude locales
cp tu-ruta/.claude/CLAUDE.md ~/.claude/
cp tu-ruta/.claude/GEMINI.md ~/.claude/
```

### 4. Inicia tu vault

El vault usa el método PARA (Projects, Areas, Resources, Archive). Para re-indexar la búsqueda semántica:

```bash
~/.claude/vectordb-venv/.venv/bin/python index_vault.py
```

Para verificar el estado:

```bash
~/.claude/bin/check-hooks --health
~/.claude/bin/check-mcps
```

### 5. MCPs y skills disponibles

| MCP | Uso |
|---|---|
| `obsidian-vault` | Buscar, leer, listar por type/status/tag, crear |
| `vault-search` | Búsqueda semántica (RAG local) |
| `graphify` | Knowledge graph: comunidades, dependencias, rutas |
| `token-optimizer` | Hooks, skills y panel de consumo |
| `mcp-dropshipping` | Márgenes, niche screener, ad scorer |
| `mcp-marketing` | Scorer de creativos, tracker de campañas |
| `roblox-studio` | Cuando lo necesites |
| `supabase` | Cuando lo necesites |

### 6. Skills frecuentes

Para habilidades específicas, revisa la carpeta `00_Meta/Plantillas/` o usa:

```bash
/mcp enable <nombre-skill>
```

## 📦 Qué incluye (y qué no)

### Incluye:
- Estructura PARA organizada
- Configuración CLAUDE.md y GEMINI.md optimizada
- MCPs para dropshipping, marketing y más
- Skills y plantillas generales
- Dashboard y métricas básicas

### Excluye (por .gitignore):
- Datos personales de NeoZeler
- APIs y secretos reales
- Carpeta Compartida/CEO
- Archivos pesados (.zip)
- Datos vectoriales del vault

## 🎯 Para comenzar rápidamente

1. Clona este repo
2. Ejecuta `/mcp enable supabase mcp-marketing`
3. Ejecuta `~/.claude/bin/check-mcps` para verificar
4. Re-indexa con `index_vault.py`
5. Empieza a organizar tus propios proyectos usando el método PARA

---

**Última limpieza**: Nov 2026 - Datos de NeoZeler removidos, estructura general preservada.

**¿Necesitas ayuda?** Revisa la carpeta `00_Meta/` para plantillas y configuraciones adicionales, o consulta los archivos `GEMINI.md` y `CLAUDE.md` para las reglas operativas.