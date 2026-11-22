#!/usr/bin/env python3
"""
PreToolUse (Edit|Write|Bash): En repos con .proyecto: Ficha antes del código, Retro antes de cerrar; bloquea git tag, commits release/cierre
"""
import sys
import json
import os

def main():
    try:
        data = json.load(sys.stdin)
        tool = data.get('tool', '')
        cwd = data.get('cwd', os.getcwd())
        
        # Verificar si hay archivo .proyecto en el directorio o padres
        has_proyecto = False
        current = cwd
        while current != '/':
            if os.path.exists(os.path.join(current, '.proyecto')):
                has_proyecto = True
                break
            current = os.path.dirname(current)
        
        if not has_proyecto:
            sys.exit(0)
        
        # Verificar ficha de investigación antes de código
        if tool in ['Edit', 'Write']:
            file_path = data.get('tool_input', {}).get('file_path', '')
            if file_path.endswith(('.py', '.js', '.ts', '.go', '.rs', '.java')):
                ficha_path = os.path.join(current, 'Ficha de Investigacion.md')
                if not os.path.exists(ficha_path):
                    print("Bloqueado por guard-proyecto: Falta 'Ficha de Investigacion.md'. Créala con /nuevo-proyecto antes de programar.", file=sys.stderr)
                    sys.exit(2)
        
        # Verificar comandos git peligrosos
        if tool == 'Bash':
            command = data.get('tool_input', {}).get('command', '')
            if 'git tag' in command or 'release' in command.lower() or 'cierre' in command.lower():
                print("Bloqueado por guard-proyecto: git tag, commits release/cierre requieren Retro.md", file=sys.stderr)
                sys.exit(2)
        
        sys.exit(0)
    except Exception as e:
        print(f"Error en guard-proyecto: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()