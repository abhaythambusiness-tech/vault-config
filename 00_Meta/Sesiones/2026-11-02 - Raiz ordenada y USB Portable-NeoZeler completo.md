---
type: sesion
date: '2026-11-02'
proyecto: Portable-NeoZeler
status: completado
origen: mixto
---

> [!resumen] En cristiano
> Se vació la raíz del vault (todo lo suelto está ahora en su carpeta) y se rehízo el USB para que instale TODO tu entorno en otro Linux: Claude, Gemini, plugins, MCP, herramientas, reglas, memoria, vault con git y claves cifradas.

## Raíz
- Imágenes → `99_Assets/Imagenes/`; PDF y CSV → `99_Assets/Documentos/`; HTML → `99_Assets/Html/`; txt y `Programacio Desde 0` → `00_Inbox/`; 3 notas .md → `03_Resources/`.
- `ssh@192.168.0.100mp-crm-test/` (copia de código del CRM con nombre accidental) → `~/Proyectos/crm-test-ssh/`.

## USB (`Portable-NeoZeler`)
- Scripts nuevos: `usar.sh` (10 pasos, opciones `--secretos --forzar --sin-internet --desktop`), `empaquetar.sh`, `guardar.sh`, `limpiar.sh`, `crear-secretos.sh`, `lib.sh`. Originales en `copias/scripts-*/`.
- Rutas `/home/haytham` se reescriben a la casa del otro usuario.

## Aprendizajes
- Los `vault*.tar.gz` antiguos del USB llevaban `00_Meta/API.md` y la clave de `obsidian-local-rest-api` **en claro**. Ahora esos dos archivos se excluyen del tar y viajan solo en `secretos.tar.gz.gpg`.
- `headroom` (6,7 GB) y el entorno vectorial (5,8 GB) no caben en FAT32 (límite 4 GB por archivo) ni son relocalizables: se reinstalan con internet.

