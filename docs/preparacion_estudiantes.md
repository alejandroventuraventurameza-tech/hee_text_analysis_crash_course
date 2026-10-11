# Preparación breve para trabajar en Colab

Esta comprobación toma aproximadamente cinco minutos. Usa la misma cuenta de Google y laptop que llevarás a la clase. Necesitas navegador, internet y el [notebook de estudiantes](../notebooks/estudiantes.ipynb). No necesitas instalar Python ni aprender Git.

## Abrir y guardar una copia

1. Descarga `estudiantes.ipynb` desde el enlace proporcionado por el docente. Si lo ves como texto en GitHub, utiliza la descarga del archivo original.
2. Abre [Google Colab](https://colab.research.google.com/) e inicia sesión en tu cuenta. En la portada, pulsa **Subir cuaderno** y selecciona el archivo descargado.
3. Guarda una copia propia en Drive y cambia su nombre a `apellido_nombre_analisis_textual`. Si el archivo ya se guardó en tu Drive, confirma su nombre y ubicación antes de continuar.

La portada en español y el botón Subir cuaderno se comprobaron el 11 de octubre de 2026. Una prueba guiada posterior confirmó la carga incluida y resultados de tablas, gráfico y contexto; copia, guardado y descarga siguen pendientes de comprobación. Los nombres pueden aparecer en español o inglés. La documentación oficial confirma que Colab admite subir notebooks y guardarlos en Drive. [Preguntas frecuentes de Colab](https://research.google.com/colaboratory/faq.html).

## Ejecutar y cargar

4. En la primera celda de código, cambia el saludo, pulsa el botón de ejecución junto a la celda y comprueba que aparece tu texto. Si Colab solicita conectar el entorno de ejecución, sigue esa indicación. Usa el entorno habitual de Python, sin GPU.
5. Ejecuta la celda Preparación de datos con `modo_carga = "incluida"`. Los datos están dentro del notebook; deja vacíos los otros campos. Debe aparecer el mensaje de seis documentos y 619 unidades sin etiquetas.
6. Ejecuta la tabla de documentos. Debes ver seis filas con fecha, orador, audiencia y conteos. Guarda tu copia y comprueba que al volver a abrirla permanecen el saludo modificado y su resultado.

Detén esta comprobación aquí. Las predicciones, clasificaciones y el resto del análisis se realizan en clase. No ejecutes por anticipado la celda final de etiquetas.

## Si algo falla

| Problema | Qué intentar |
|---|---|
| El archivo se abre como texto | Descargar el `.ipynb` original y subirlo desde Colab |
| No aparece el saludo cambiado | Ejecutar otra vez la celda después de editarla |
| Falta un nombre o variable | Ejecutar Preparación antes de la tabla |
| La carga incluida falla | Descargar [datos_estudiantes.zip](../paquetes/datos_estudiantes.zip), elegir `manual` en Preparación y subir solo ese ZIP |
| No se guarda tu copia | Comprobar inicio de sesión y ubicación en Drive; avisar al docente |

Anota qué paso completaste y el mensaje de error si persiste. La persona de apoyo ayudará durante la sesión.

## Entrega al final de la clase

Guarda y descarga el notebook `.ipynb` con tus respuestas y salidas visibles. Súbelo a la carpeta de Drive que indicará el docente y comprueba que aparece. La entrega es individual y no tiene calificación. Los CSV y el gráfico son complementos; la entrega principal debe conservar tu razonamiento.

Los archivos creados en el entorno de ejecución no se incorporan automáticamente al notebook o a tu Drive. Guarda o descarga expresamente lo que necesites conservar. Si hay un problema de subida, mantén el archivo descargado y avisa al docente. [Documentación de almacenamiento y descarga de Colab](https://research.google.com/colaboratory/faq.html).
