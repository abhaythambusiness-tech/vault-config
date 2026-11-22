#!/usr/bin/env python3
"""
PreToolUse (Bash): Frena comandos destructivos (destroy de IaC, borrado de tablas, git push --force/-f)
"""
import sys
import json
import re

def main():
    try:
        data = json.load(sys.stdin)
        command = data.get('tool_input', {}).get('command', '')
        
        # Patrones destructivos
        destructive_patterns = [
            r'terraform\s+destroy',
            r'terraform\s+apply\s+-auto-approve',
            r'git\s+push\s+--force',
            r'git\s+push\s+-f\b',
            r'rm\s+-rf\s+/',
            r'rm\s+-rf\s+~',
            r'DROP\s+TABLE',
            r'TRUNCATE\s+TABLE',
            r'DELETE\s+FROM\s+\w+\s*;',
        ]
        
        for pattern in destructive_patterns:
            if re.search(pattern, command, re.IGNORECASE):
                print(f"Bloqueado por guard-destructive: Comando destructivo detectado: {command}", file=sys.stderr)
                sys.exit(2)
        
        sys.exit(0)
    except Exception as e:
        print(f"Error en guard-destructive: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()