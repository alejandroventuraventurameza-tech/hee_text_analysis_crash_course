# Colab: Las palabras como datos

Las versiones de estudiantes y docente siguen las 42 diapositivas del Beamer final proporcionado por Alejandro Ventura en `paquetes/hee_text_analysis_crash_course.zip`. El ZIP y los archivos de `slides` no se modifican. La correspondencia se conserva en `alineacion_beamer.json`, junto con la huella SHA256 del ZIP leído.

El recorrido comprende motivación, variable proxy, fuentes presidenciales y API conceptual, flujo del NLP, corpus y clasificación manual, procesamiento en español, frecuencias y comparación normalizada, contexto, contraste de etiquetas y límites. Se conservan del Colab anterior recuperación, respuestas individuales, entrega formativa sin calificación y desafío opcional. El Beamer final tiene la sección Cierre sin diapositivas; el notebook conserva las instrucciones de guardado y entrega acordadas.

| Archivo | Uso |
|---|---|
| [estudiantes.ipynb](estudiantes.ipynb) | Copia individual, sin salidas ni respuestas resueltas |
| [docente_resuelto.ipynb](docente_resuelto.ipynb) | Mismo código, respuestas orientativas y salidas de ejecución local |
| [alineacion_beamer.json](alineacion_beamer.json) | Correspondencia de las 42 diapositivas con celdas |
| [prueba_local.json](prueba_local.json) | Ejecución local, versiones, resultados y huellas |
| [prueba_colab_guiada.json](prueba_colab_guiada.json) | Evidencia histórica del recorrido anterior en Colab |

## Procesamiento en español

NLTK realiza tokenización de oraciones y palabras, consulta de stop words españolas y stemming con `SnowballStemmer("spanish")`. Los ejemplos de sentence tokenization, word tokenization y consulta de stop words se leen directamente del código del ZIP del Beamer. Después se aplica eliminación de stop words a un pasaje real, protegiendo las negaciones, manejo de puntuación española y lowercasing.

**Excepción autorizada:** spaCy se utiliza únicamente para lematizar con el modelo español `es_core_news_sm`. Se compara palabra por palabra con el stemming de NLTK, primero en una oración didáctica identificada como tal y después en un pasaje real de Leguía de 1921. No se usa WordNetLemmatizer para español. No se llama a una API de IA ni se entrena un clasificador.

La preparación comprueba y, si hace falta, instala bibliotecas y descarga recursos lingüísticos. La primera ejecución requiere internet. Las versiones de referencia están en las celdas y el informe de prueba. Tras reiniciar el entorno, ejecutar desde el inicio; para recuperar solamente la comparación, ejecutar Preparación, Preparar NLTK y Recuperación de la comparación.

## Datos, conteos y evidencia

Los seis documentos, 148 páginas y 619 unidades sin etiquetas están incluidos en el notebook. La carga inicial se presenta como formulario en Colab. También se conserva la carga manual de `datos_estudiantes.zip`, la opción URL con un enlace proporcionado por el docente y la carga local para pruebas.

La tabla de las diapositivas exige contar formas exactas con la regla documentada de `texto_conteo`. NLTK tokeniza esa versión para los seis documentos. Se comprueban sus denominadores: Leguía de 1921 tiene 4.527 palabras y Fujimori de 1991 tiene 23.348. La comparación inicial de competencia produce 2 y 11 menciones, aproximadamente 0,442 y 0,471 por 1.000 palabras.

Las técnicas de normalización son alternativas: no se aplica stemming ni lematización a la consulta de forma exacta. Ocultar stop words del ranking no las retira del denominador. El texto original conserva signos y negaciones para leer en contexto. Las filas 0 y 3 de la consulta inicial recuperan `u00126` y `u14275`; al cambiar la consulta hay que revisar los índices.

Las etiquetas existentes se cargan por separado al final, después de la clasificación manual de A y B. La confianza categórica no es una probabilidad calibrada; el segundo anotador fue otro modelo y la referencia de 30 unidades tiene poco soporte para clases raras. La separación de etiquetas es pedagógica: el código de un notebook público puede consultarse anticipadamente.

## Uso y entrega

Abrir estudiantes.ipynb en Colab, guardar una copia en Drive y seguir al docente. Las celdas **Mi respuesta** se editan con doble clic. Cambiar una instrucción, volver a ejecutar y explicar su efecto. Los encabezados no muestran tiempos; los emojis permiten localizar las etapas.

La comprobación antes de guardar detecta consultas cambiadas sin actualizar tabla y evidencia. Guarda CSV complementarios; el gráfico se conserva como PNG. No califica las explicaciones. La entrega principal es apellido_nombre_analisis_textual.ipynb, con respuestas y salidas, en la carpeta indicada por el docente usando la cuenta institucional UP.

## Regeneración y pruebas

```powershell
python scripts/crear_notebooks.py
python scripts/probar_notebooks.py
```

El generador adapta ambas versiones mediante adaptar_colab_final.py, que solo lee el ZIP final. No ejecutar sobre copias personales con respuestas nuevas. La prueba requiere Jupyter, ipykernel, pandas y matplotlib, además de los recursos preparados por las celdas; ejecuta cada versión en un kernel nuevo y guarda salidas únicamente en la versión docente.

Las nuevas comprobaciones incluyen segmentación de oraciones, negaciones conservadas, signos españoles, raíces, lemas y denominadores de los seis textos. También se conserva la comprobación de tasas guardadas, consultas inválidas, tildes, recuperación y carga de los bytes del ZIP. La interfaz files.upload() se simula localmente y no sustituye una prueba real de Colab.

**La versión nueva debe comprobarse en Colab.** La evidencia guiada anterior no valida las instalaciones nuevas ni la representación actual de imágenes y emojis. El informe prueba_local.json documenta exclusivamente ejecución local.
