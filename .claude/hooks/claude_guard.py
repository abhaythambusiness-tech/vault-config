#!/usr/bin/env python3
"""
Guard general: valida operaciones comunes antes de ejecutar
"""
import sys
import json
import os

def main():
    try:
        data = json.load(sys.stdin)
        tool = data.get('tool', '')
        tool_input = data.get('tool_input', {})
        
        # Validaciones generales
        if tool == 'Bash':
            command = tool_input.get('command', '')
            # No permitir sudo sin confirmación explícita
            if command.strip().startswith('sudo '):
                print("Bloqueado por claude-guard: 'sudo' requiere confirmación explícita del usuario.", file=sys.stderr)
                sys.exit(2)
        
        if tool in ['Edit', 'Write']:
            file_path = tool_input.get('file_path', '')
            # No permitir escribir fuera del workspace sin confirmación
            workspace = os.getcwd()
            abs_path = os.path.abspath(file_path)
            if not abs_path.startswith(workspace) and not abs_path.startswith(os.path.expanduser('~/.claude')):
                print(f"Bloqueado por claude-guard: Intento de escribir fuera del workspace: {file_path}", file=sys.stderr)
                sys.exit(2)
        
        sys.exit(0)
    except Exception as e:
        print(f"Error en claude-guard: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()