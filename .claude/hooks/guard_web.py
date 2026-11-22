#!/usr/bin/env python3
"""
PreToolUse (Edit|Write): Bloquea tocar .env reales o carpetas generadas
"""
import sys
import json
import os

def main():
    try:
        data = json.load(sys.stdin)
        tool = data.get('tool', '')
        file_path = data.get('tool_input', {}).get('file_path', '')
        
        # Bloquear .env reales
        if file_path and ('.env' in file_path and not file_path.endswith('.example')):
            print("Bloqueado por guard-web: No se pueden editar archivos .env reales", file=sys.stderr)
            sys.exit(2)
        
        # Bloquear carpetas generadas
        generated_dirs = ['dist', 'build', '.next', 'out', 'target', 'node_modules', '__pycache__']
        for d in generated_dirs:
            if f'/{d}/' in file_path or file_path.startswith(f'{d}/'):
                print(f"Bloqueado por guard-web: No se pueden editar archivos en {d}/", file=sys.stderr)
                sys.exit(2)
        
        sys.exit(0)
    except Exception as e:
        print(f"Error en guard-web: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()