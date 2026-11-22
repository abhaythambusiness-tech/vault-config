#!/usr/bin/env python3
"""
PostToolUse: Sincroniza GEMINI.md con CLAUDE.md cuando cambian convenciones
"""
import sys
import json
import os

def main():
    try:
        data = json.load(sys.stdin)
        tool = data.get('tool', '')
        file_path = data.get('tool_input', {}).get('file_path', '')
        
        # Solo si se editan archivos de configuración/reglas
        config_files = ['CLAUDE.md', 'AGENTS.md', 'GEMINI.md', 'rules/', '.claude/CLAUDE.md']
        if not any(f in file_path for f in config_files):
            sys.exit(0)
        
        print("💡 Archivo de configuración modificado: considera ejecutar 'sync-gemini' para sincronizar GEMINI.md", file=sys.stderr)
        
        sys.exit(0)
    except Exception as e:
        print(f"Error en sync-gemini: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()