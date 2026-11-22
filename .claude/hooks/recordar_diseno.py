#!/usr/bin/env python3
"""
PreToolUse (Edit|Write): Bloquea editar UI hasta invocar diseno-central
"""
import sys
import json
import os

def main():
    try:
        data = json.load(sys.stdin)
        tool = data.get('tool', '')
        file_path = data.get('tool_input', {}).get('file_path', '')
        
        # Extensiones de UI
        ui_extensions = ['.tsx', '.jsx', '.vue', '.svelte', '.astro', '.html', '.css', '.scss']
        if not any(file_path.endswith(ext) for ext in ui_extensions):
            sys.exit(0)
        
        # Verificar si se invocó diseno-central en esta sesión
        # Usamos un archivo temporal como flag
        flag_file = os.path.expanduser('~/.claude/.diseno_invoked')
        if not os.path.exists(flag_file):
            print("Bloqueado por recordar-diseno: Debes invocar 'diseno-central' antes de editar UI. Usa la skill o comando correspondiente.", file=sys.stderr)
            sys.exit(2)
        
        sys.exit(0)
    except Exception as e:
        print(f"Error en recordar-diseno: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()