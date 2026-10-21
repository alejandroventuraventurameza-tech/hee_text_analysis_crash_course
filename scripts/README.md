# Preparación docente de los datos

`preparar_datos.py` copia los seis documentos seleccionados y sus unidades y etiquetas desde el commit fijo de investigación `72fcac7d3ea06b737c3a3f35f37b818411c6dead`, correspondiente a `v1.0-ccl`. Solo ejecuta lecturas de Git sobre investigación; las salidas se escriben en este repositorio de clase.

Requiere Python y PyMuPDF. No instala herramientas, descarga modelos ni usa claves. Los estudiantes no necesitan ejecutar este script: leerán las salidas ya preparadas con el notebook.

Desde la raíz del repositorio de clase:

```powershell
python scripts/preparar_datos.py --repo-investigacion ../discursos_presidenciales
```

La configuración revisada está en `data/seleccion.json`. El script verifica PDF contra huellas del archivo congelado y de la comprobación pública; oficialidad y exclusión de duplicados; páginas con texto; localización ordenada de las unidades; igualdad del conteo de espacios heredado por unidad; e identificadores únicos y cobertura de etiquetas. Registra las versiones de preparación y genera tasas guardadas de cinco palabras exactas.

La comprobación pública se realizó separadamente el 10 de octubre de 2026 y se conserva en `data/trazabilidad/verificacion_web.json`. Regenerar localmente los datos no repite esa comprobación de internet ni prueba Colab. El script usa la fecha de la revisión inicial en su informe y no debe interpretarse como fecha de una nueva consulta a la web.

El script regenera datos, no documentación ni ZIP. Después de editar la documentación de `data/`, volver a generar el listado SHA-256 y el ZIP para carga manual. El ZIP debe excluir `data/docente/` y el listado global de huellas, que también contiene referencias a archivos del docente ausentes del paquete. Mantener el paquete en `paquetes/`, fuera del árbol de datos para evitar referencias circulares al calcular huellas.

## Preparación de notebooks

`crear_notebooks.py` construye la versión de estudiantes y la resuelta a partir de los datos revisados, con dos cargas independientes: documentos sin etiquetas al inicio y clasificaciones al final. No necesita bibliotecas externas para generar los archivos.

`probar_notebooks.py` ejecuta las dos versiones en kernels nuevos, guarda salidas en el notebook docente y registra comprobaciones y versiones. Requiere `jupyter_client`, `ipykernel`, pandas y matplotlib en el entorno docente. No prueba la interfaz de Colab. El alcance y las instrucciones están en [notebooks/README.md](../notebooks/README.md).

## Preparación de Beamer

`preparar_beamer.py` adapta una copia del preámbulo del template, conserva el logo y registra la procedencia de pasajes y valores. `revisar_beamer.py` comprueba rutas, referencias, estructura y coherencia con datos, y prepara el ZIP para Overleaf. La preparación usa además PyMuPDF (`fitz`) para renderizar cuatro primeras páginas de los PDF oficiales; la revisión utiliza Python estándar. Ninguno compila LaTeX. El contenido de las slides y el guion se editan por separado. Consultar [slides/README.md](../slides/README.md).
