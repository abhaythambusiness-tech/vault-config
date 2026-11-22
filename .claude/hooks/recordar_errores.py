#!/usr/bin/env python3
"""
PreToolUse: Recuerda errores comunes del proyecto antes de editar
"""
import sys
import json
import os

def main():
    try:
        data = json.load(sys.stdin)
        tool = data.get('tool', '')
        file_path = data.get('tool_input', {}).get('file_path', '')
        
        if tool not in ['Edit', 'Write']:
            sys.exit(0)
        
        # Buscar COMMON_MISTAKES.md en el proyecto o padres
        cwd = os.getcwd()
        current = cwd
        mistakes_file = None
        while current != '/':
            potential = os.path.join(current, '.claude', 'COMMON_MISTAKES.md')
            if os.path.exists(potential):
                mistakes_file = potential
                break
            current = os.path.dirname(current)
        
        if mistakes_file:
            print(f"💡 Revisa {mistakes_file} antes de editar - contiene errores comunes del proyecto.", file=sys.stderr)
        
        sys.exit(0)
    except Exception as e:
        print(f"Error en recordar-errores: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()