---
name: direccion
description: "Reunión de dirección de NeoZeler: lanza al CEO con una pregunta, recoge sus encargos y los reparte en paralelo a CFO, COO, CTO y CMO. Solo cuando Haytham escribe /direccion."
disable-model-invocation: true
argument-hint: "<pregunta o decisión, p. ej. «qué hacemos este mes»>"
---

# /direccion — reunión de dirección NeoZeler

Pregunta de Haytham: `$ARGUMENTS` (si está vacía, pregunta UNA vez: «¿Qué decisión quieres tomar?»).

**Avisa en una línea del coste**: hasta 5 agentes (≈5x tokens). Solo se hace porque Haytham lo pidió (regla vault §0.13: no paralelizar por defecto).

## Pasos
1. **CEO**: lanza el agente `neozeler-ceo` con la pregunta literal. Pídele prioridades y encargos separados por agente.
2. **Reparto**: del informe del CEO, extrae el encargo de cada agente (`neozeler-cfo`, `-coo`, `-cto`, `-cmo`). Solo lanza los que tengan encargo.
3. **Paralelo**: lanza todos los agentes con encargo **en el mismo mensaje** (varias llamadas Agent a la vez). A cada uno pásale su encargo literal; no resumas ni añadas. Todos leen `02_Areas/NeoZeler/Estrategia/Contexto NeoZeler.md` por su cuenta.
4. **Síntesis** (máx. 15 líneas, español sencillo): conclusión; qué dice cada agente en 1 línea; contradicciones entre ellos (p. ej. CMO quiere gastar, CFO no); la decisión que le toca a Haytham.
5. Informes largos quedan en `02_Areas/NeoZeler/Estrategia/Informes/`; enlázalos, no los pegues.

## Reglas
- Si el CEO no da encargos claros, para y dilo; no inventes encargos.
- Los agentes no envían, publican ni gastan nada: todo lo externo lo decide Haytham.
- Nunca presentes el resultado como hecho si un agente marcó «sin confirmar».
