# Notebooks del curso de análisis textual

Las operaciones tienen títulos para facilitar su localización; las celdas de respuesta se editan con doble clic. El caso común conserva competencia y los dos documentos iniciales hasta recuperar la evidencia; luego permite otras consultas.

La práctica común tiene 14 celdas de código y explicaciones breves, distribuidas en 47 celdas totales. Permite cargar seis documentos y sus metadatos, explicar una transformación, contar palabras, comparar menciones por 1.000 palabras, buscar en el original y formular una conclusión limitada a los documentos examinados.

| Archivo | Uso |
|---|---|
| [estudiantes.ipynb](estudiantes.ipynb) | Copia individual, sin salidas ejecutadas ni respuestas resueltas |
| [docente_resuelto.ipynb](docente_resuelto.ipynb) | Mismo código y datos, con respuestas orientativas, tablas y gráfico guardados de la ejecución local |
| [prueba_local.json](prueba_local.json) | Registro de ejecución, versiones, resultados y huellas de los notebooks |
| [prueba_colab_guiada.json](prueba_colab_guiada.json) | Evidencia recibida del usuario y partes aún pendientes en Colab |

## Acceso y carga

Descargar `estudiantes.ipynb` y abrirlo mediante la opción de subir notebook en Colab; guardar una copia propia en Drive. El repositorio será público, pero todavía no tiene remoto configurado, por lo que no se incluye un botón que apunte a una dirección de GitHub inventada. El acceso desde GitHub se podrá añadir cuando exista la URL pública.

La carga común usa datos comprimidos incluidos en una celda preparada del propio notebook. No consulta investigación, una API ni una cuenta de Drive; tampoco instala bibliotecas o modelos. Esa celda se presenta como formulario en Colab para evitar mostrar a principiantes toda la implementación. El tamaño de cada notebook es de aproximadamente 0,9 MB antes de guardar salidas; la versión resuelta es mayor porque conserva los resultados.

Hay una alternativa de carga manual con [datos_estudiantes.zip](../paquetes/datos_estudiantes.zip). En Preparación, elegir `manual` y subir ese ZIP. También existen las opciones `url`, para un enlace HTTPS directo al ZIP público, y `zip_local`, para comprobaciones docentes fuera de Colab. Ninguna es necesaria para el recorrido inicial.

El ZIP y la carga inicial no incluyen clasificaciones. Las etiquetas existentes están en un segundo paquete independiente incluido exclusivamente en la celda del contraste de los minutos 90–98. Esa celda no se ejecuta durante la clasificación manual. Al distribuir un notebook público, su separación es pedagógica, no una protección frente a consultar el código por anticipado.

## Modificaciones de los estudiantes

El estudiante cambia el saludo de su primera celda y modifica al menos una decisión del análisis: cantidad de términos del ranking, documento explorado, palabra comparada, documentos incluidos o amplitud de contexto. La consulta inicial es `competencia`, con Leguía de 1921 y Alberto Fujimori de 1991. El docente debe pedir la predicción antes de ejecutar; la versión del estudiante no muestra conteos ni interpretaciones resueltas por anticipado.

Para el caso inicial, las filas 0 y 3 de contexto permiten recuperar unidades de documentos distintos. Si cambia la consulta, el estudiante debe revisar los índices. La selección muestra el texto completo de la unidad y su procedencia; si una coincidencia no tiene unidad, muestra su página completa. El notebook rechaza una selección inválida o del mismo documento con un mensaje y deja la evidencia vacía para no conservar pasajes anteriores por error.

La búsqueda usa la extracción original, conserva signos y negaciones y solo reemplaza saltos de línea por espacios en la ventana visible. La tabla muestra la ventana completa, sin el límite visual de 250 caracteres detectado durante la prueba guiada en Colab. La comparación usa el texto para conteos, por lo que la reparación de guiones y los descartes editoriales pueden producir diferencias entre ambos. Una forma exacta no agrupa variantes, sinónimos ni significados.

## Recuperación y entrega

Al minuto 36 debe haber seis documentos cargados. Si se perdió una variable, ejecutar Preparación. Si se reinició el entorno, esa celda reconstruye los datos y herramientas sin descargas. Al minuto 74, la celda Recuperación vuelve a cargar las tablas y recalcula la comparación con la consulta actual o la inicial. Las respuestas escritas en celdas de texto no se reemplazan.

La alternativa de resultados guardados está desactivada por defecto y se usa únicamente después de escribir la predicción. Su tabla queda marcada como `guardada`, para distinguirla de una comparación recalculada por el estudiante. La ejecución individual debe retomarse cuando se resuelva la dificultad.

Al minuto 90 debe haber comparación y dos fragmentos. En el cierre, la comprobación técnica detecta si se cambió la palabra o los documentos sin actualizar tabla y evidencia. No evalúa la calidad de las respuestas. Cuando ambos resultados corresponden a la consulta actual, guarda complementos CSV; el gráfico se guarda como PNG. Las explicaciones, limitación, clasificación y aplicación siguen siendo responsabilidad del estudiante.

La entrega principal es el notebook `.ipynb` con respuestas y salidas visibles, no los complementos. Se descarga y entrega en la carpeta de Drive que comunicará el docente. La copia y el guardado ya cuentan con evidencia de una prueba guiada; aún falta verificar la recepción en la carpeta de entrega de la clase.

## Prueba local y límites de la comprobación

El 11 de octubre de 2026 se ejecutaron las 14 celdas de código de cada versión, en orden, en kernels nuevos de Python sobre Windows. Entorno: Python 3.13.14, pandas 3.0.2 y matplotlib 3.10.9. Se configuró el modo gráfico inline en el kernel de prueba. La versión docente conserva las salidas de ese recorrido común; el estudiante recibe celdas sin salidas.

Se comprobaron: seis documentos, 619 unidades, 148 páginas, las 30 tasas guardadas frente a cálculos nuevos, tildes y mayúsculas, consultas sin coincidencias, negaciones en ventanas, rechazo de consultas inválidas, selección de evidencia de documentos distintos, recuperación tras perder variables, salida guardada identificada y desafío opcional. La tabla inicial produjo 2 menciones entre 4.527 palabras y 11 entre 23.348, equivalentes aproximadamente a 0,442 y 0,471 por 1.000 palabras. Las dos unidades de evidencia fueron `u00126` y `u14275`.

La lectura del ZIP distribuido se comprobó con sus bytes reales. La respuesta de `files.upload()` se simuló para probar la recepción de esos mismos bytes, sin usar la interfaz de Colab. La opción URL y una descarga pública del repositorio no se comprobaron; todavía no hay un remoto configurado.

**La comprobación completa en Colab sigue pendiente.** El usuario compartió resultados del recorrido común hasta el contraste y la comprobación técnica de entrega. La ampliación de contexto ya se recibió sin truncamiento, y las justificaciones completas mediante una celda adicional. Confirmó el guardado, descarga y reapertura; la copia local de prueba conserva el texto escrito, gráfico y tablas, sin salidas de error. El registro separado distingue inspección del archivo y confirmación del usuario. La carga manual real del ZIP también fue confirmada. Después de las instrucciones de reinicio se recibió otra comparación correcta; no se observó ni confirmó explícitamente el reinicio. Las versiones comunicadas por el usuario son Python 3.13.16, pandas 2.2.3 y matplotlib 3.10.0. No se necesitan GPU ni pagos.

## Regeneración docente

Desde la raíz del repositorio de la clase:

```powershell
python scripts/crear_notebooks.py
python scripts/probar_notebooks.py
```

El primer script regenera ambas versiones sin salidas a partir de los datos revisados y de las respuestas orientativas. El segundo las ejecuta en kernels independientes, guarda resultados en la versión docente y registra las pruebas. La regeneración reemplaza el contenido de esas dos versiones: no debe ejecutarse sobre notebooks personales con respuestas nuevas que se quieran conservar.

El código de creación usa la biblioteca estándar. La comprobación local requiere el entorno docente con `jupyter_client`, `ipykernel`, pandas y matplotlib; no instala dependencias. Los estudiantes solo necesitan Colab y su notebook.

Los títulos de celdas y las instrucciones de afinamiento se verificaron mediante ejecución local de las dos versiones. Su presentación en Colab todavía no se observó directamente; la prueba guiada anterior corresponde a la versión previa.

## Presentación visual

Los encabezados ya no muestran intervalos ni minutos. La portada incluye título, curso, expositor, semestre y el logo UP embebido, sin depender de una descarga externa. Los emojis distinguen etapas y operaciones, conservando sus nombres. La presentación del logo y los iconos dentro de Colab aún debe observarse en la interfaz; la ejecución de cálculos ya fue verificada localmente.
