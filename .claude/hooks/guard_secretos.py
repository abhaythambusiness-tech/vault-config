#!/usr/bin/env python3
"""
PreToolUse (Edit|Write|Bash): Escanea secretos en contenido nuevo y comandos git
"""
import sys
import json
import re
import os

# Patrones de secretos comunes
SECRET_PATTERNS = [
    (r'(?i)(api[_-]?key|apikey|secret|password|token|auth)[\s:=]+["\']?[a-zA-Z0-9_\-]{20,}["\']?', 'API key/token'),
    (r'(?i)(aws[_-]?access[_-]?key|aws[_-]?secret)[\s:=]+["\']?[A-Z0-9]{20,}["\']?', 'AWS credentials'),
    (r'gh[pousr]_[A-Za-z0-9_]{36,}', 'GitHub token'),
    (r'sk-[a-zA-Z0-9]{48,}', 'OpenAI API key'),
    (r'xox[baprs]-[a-zA-Z0-9-]{10,}', 'Slack token'),
    (r'-----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----', 'Private key'),
]

def check_content(content, context=""):
    for pattern, desc in SECRET_PATTERNS:
        if re.search(pattern, content):
            return f"Secreto detectado ({desc}) en {context}"
    return None

def main():
    try:
        data = json.load(sys.stdin)
        tool = data.get('tool', '')
        tool_input = data.get('tool_input', {})
        
        if tool in ['Edit', 'Write']:
            new_content = tool_input.get('new_string') or tool_input.get('content', '')
            file_path = tool_input.get('file_path', '')
            if new_content:
                result = check_content(new_content, file_path)
                if result:
                    print(f"Bloqueado por guard-secretos: {result}", file=sys.stderr)
                    sys.exit(2)
        
        elif tool == 'Bash':
            command = tool_input.get('command', '')
            if 'git commit' in command or 'git push' in command:
                # Escanear archivos staged
                import subprocess
                try:
                    result = subprocess.run(
                        ['git', 'diff', '--cached'],
                        capture_output=True,
                        text=True,
                        timeout=5
                    )
                    if result.stdout:
                        result_check = check_content(result.stdout, 'git staged changes')
                        if result_check:
                            print(f"Bloqueado por guard-secretos: {result_check}", file=sys.stderr)
                            sys.exit(2)
                except Exception:
                    pass
        
        sys.exit(0)
    except Exception as e:
        print(f"Error en guard-secretos: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()