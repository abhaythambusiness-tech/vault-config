# Cómo pushear este repositorio a GitHub

Sigue estos pasos para subir la configuración limpia a tu repositorio de GitHub:

## 1. Crear el repositorio en GitHub

Ve a https://github.com y crea un nuevo repositorio llamado `vault-config` (o el nombre que prefieras).

**Importante:** Marca la opción "Add a README" NO (ya incluimos uno). Elige "Add .gitignore" → "Linux" y "Choose a license" si deseas, o déjalo sin licencia.

## 2. Agregar el repositorio remoto y push

```bash
# Desde la carpeta donde clonaste (o desde cero):
git remote add origin git@github.com:tu-usuario/vault-config.git
# O si usas HTTPS:
# git remote add origin https://github.com/tu-usuario/vault-config.git

git branch -M main  # o master, según sea tu rama por defecto
git push -u origin main  # o master
```

## 3. Verificar en GitHub

Entra a tu repositorio en GitHub y verifica que:
- ✅ No aparecen datos personales de NeoZeler
- ✅ El `.gitignore` está aplicado (no debería verse `NeoZeler CRM`, bases de datos, etc.)
- ✅ Los archivos clave están: `CLAUDE.md`, `GEMINI.md`, `.mcp.json`, `README.md`
- ✅ La estructura `00_Meta/`, `01_Projects/`, `02_Areas/` está presente

## 4. Instrucciones para que tus amigos clon y usen

Una vez que el repositorio esté en GitHub, tus amigos pueden clonarlo y configurarlo así:

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/vault-config.git mi-vault

# 2. Entrar al directorio
cd mi-vault

# 3. Configurar MCPs esenciales
/mcp enable supabase
/mcp enable mcp-marketing
/mcp enable mcp-dropshipping

# 4. Configurar Claude Code (usando sus propios archivos .claude)
# Copiar sus CLAUDE.md y GEMINI.md personales:
cp mi-ruta/.claude/CLAUDE.md ~/.claude/
cp mi-ruta/.claude/GEMINI.md ~/.claude/

# 5. Re-indexar la búsqueda semántica
~/.claude/vectordb-venv/.venv/bin/python index_vault.py

# 6. Verificar el estado
~/.claude/bin/check-hooks --health
~/.claude/bin/check-mcps

# 7. ¡Listo! El vault está organizado con el método PARA
#    - 01_Projects: tus proyectos activos
#    - 02_Areas: responsabilidades continuas
#    - 03_Resources: referencia reutilizable
#    - 04_Archive: histórico

# 8. MCPs disponibles:
#    - obsidian-vault: buscar, leer, crear notas
#    - vault-search: búsqueda semántica RAG local
#    - graphify: grafo de dependencias y comunidades
#    - token-optimizer: ahorro de tokens y panel de consumo
#    - mcp-dropshipping: márgenes, niche screener, ad scorer
#    - mcp-marketing: scorer de creativos, tracker de campañas
#    - roblox-studio: cuando lo necesites
#    - supabase: cuando lo necesites
```

## 5. Estructura del repositorio compartido

El repositorio incluye:

```
vault-config/
├── .gitignore          # Patrones de exclusión (datos personales, secretos, NeoZeler)
├── CLAUDE.md           # Guía operativa del vault (global optimizada)
├── GEMINI.md           # Estilo y routing esencial
├── .mcp.json           # Configuraciones de MCPs (dropshipping, marketing, etc.)
├── README.md           # Estas instrucciones
├── 00_Meta/            # Metadatos e instrucciones generales
│   ├── Dashboard.md
│   ├── GEMINI.md
│   ├── Estructura del Vault.md
│   ├── Decision - Estructura del Vault (Debate Multi-Agente).md
│   ├── Plantillas/     # 10 plantillas genéricas (Caso de Éxito, Cliente, Propuesta, Proyecto, Servicio IA, etc.)
│   └── ...
├── 01_Projects/        # Proyectos variados (limpiados de NeoZeler)
│   ├── Dropshipping/
│   ├── Reto-30/
│   ├── Cauce/
│   ├── Abisal Drill/
│   └── ...
├── 02_Areas/           # Áreas de responsabilidad
│   ├── Trading con 10 euros/
│   └── Área principal/
├── 03_Resources/       # Recursos de referencia
├── 04_Archive/         # Notas archivadas
├── 99_Assets/          # Recursos assets (imágenes, PDFs)
└── .claude/            # Configuración local de Claude Code
    ├── ARCHITECTURE_MAP.md
    └── ...
```

## 6. Qué fue removido (limpieza de NeoZeler)

Los siguientes datos personales de NeoZeler fueron removidos del repositorio:

- ✅ `01_Projects/Neozeler CRM/` - completo
- ✅ `01_Projects/NeoZeler Web/` - completo
- ✅ `01_Projects/NeoZeler Tools/` - completo
- ✅ `01_Projects/NeoZeler Mundo/` - completo
- ✅ `02_Areas/NeoZeler/` - área de agencia removida (contenido genérico preservado)
- ✅ `00_Meta/Decision - Reparto de Tiempo NeoZeler vs Dropshipping.md` - removido
- ✅ `00_Meta/Estado de Proyectos.md` - removido (datos de instancia)
- ✅ `00_Meta/Salud del vault.md` - removido (datos de instancia)
- ✅ Múltiples notas de sesión sobre NeoZeler (2026-08-19, 2026-10-31, 2026-11-06, 2026-11-08, 2026-11-20)
- ✅ Referencias a `NeoZeler CRM`, `NeoZeler Web`, `NeoZeler HQ` en documentación de instancia
- ✅ Datos de contactos, precios y clientes específicos de NeoZeler

## 7. Qué se preservó (valor compartible)

- Estructura PARA organizadad (00_Meta, 01_Projects, 02_Areas, 03_Resources, 04_Archive, 99_Assets)
- Configuración CLAUDE.md y GEMINI.md optimizada
- MCPs configurados: dropshipping, marketing
- 10 plantillas genéricas (Caso de Éxito, Cliente, Propuesta, Proyecto, Servicio IA, Sesión, Nota Estándar, Onboarding Cliente IA, Carpeta de Cliente, Simulador de WhatsApp)
- Dashboard y MOCs del vault
- Skills yruting esencial
- Convenciones de frontmatter y callouts
- Metodología de software de 6 documentos
- Proyectos genéricos: ARM, Abisal Drill, Battle Royale, Bot de Tendencia, Cauce, Comanda Viva, ComandAi, Conversor MP3 Facil, Grid64, Kit Samira, Laya Leads, Laya Trader, Los Apuntes de Liyo, Mini CRM Go, MCP Compartido, MCP Diseno, Starter SaaS, Taller-Bravo, Ultimo en Pie - Sabotaje, Voice-to-Vault

---

**Hecho posible**: Estructura limpia, plantillas genéricas y .gitignore configurado para que puedas clonar y adaptar este repositorio sin datos de NeoZeler.