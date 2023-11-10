# Plantilla para cupones

Plantilla para cupones y generador de numeración.

## Requerimientos

- [Inkscape](https://inkscape.org)
- [Python 3](https://python.org)
- El módulo `pypdf` de Python. Se puede instalar con `pip install pypdf`

## Modo de uso

1. Editar `plantilla.svg` para estilizarla a gusto.
2. Editar los archivos relacionados a la plantilla.
3. Editar `configuracion.py` para especificar:
   - Total de cupones.
   - Cantidad de cupones por página.
   - Nombre de archivo final.
   - Archivos relacionados a la plantilla.
   - ...
4. Ejecutar el script `plantilla.py`.
