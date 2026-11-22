#!/usr/bin/env python3
"""
PreToolUse (Bash): Compresión de salida de comandos (rtk hook claude)
"""
import sys
import json
import subprocess
import os

def main():
    try:
        data = json.load(sys.stdin)
        command = data.get('tool_input', {}).get('command', '')
        
        # Solo comprimir salidas de comandos largos conocidos
        long_commands = ['npm install', 'pip install', 'cargo build', 'go build', 'make', 'docker build']
        if not any(cmd in command for cmd in long_commands):
            sys.exit(0)
        
        # Marcar para compresión (el hook real se ejecuta después)
        # En OpenCode, esto se maneja diferente - solo registramos la intención
        os.environ['RTK_COMPRESS'] = '1'
        
        sys.exit(0)
    except Exception as e:
        print(f"Error en rtk-hook: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()