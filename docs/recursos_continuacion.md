# Recursos para continuar con análisis textual

La continuación empieza por repetir un análisis pequeño y explicar sus decisiones. Los tiempos siguientes son propuestas de práctica personal, no requisitos de la clase. Ninguna actividad necesita pagos, claves API ni modelos grandes.

## Ruta de práctica

| Práctica propuesta | Tiempo orientativo | Producto |
|---|---:|---|
| Cambiar una palabra y ampliar el contexto en el notebook de clase | 20 minutos | Comparación con dos pasajes y revisión de la hipótesis |
| Retirar un documento o modificar el ranking y explicar qué cambia | 30 minutos | Resultado con su selección y denominador explícitos |
| Preparar dos documentos de tu carrera con la ruta de adaptación | 45–60 minutos | Originales, metadatos y una pregunta delimitada |

En cada práctica registra predicción, modificación, resultado, comprobación textual y limitación. Puedes encontrar una hipótesis que no se sostiene: documentarla es parte del análisis.

## Herramientas para el recorrido inicial

| Recurso público | Qué consultar primero | Cómo usarlo |
|---|---|---|
| [Introducción oficial de Python](https://docs.python.org/3/tutorial/introduction.html) | Cadenas de texto y listas | Cambiar valores pequeños y predecir el resultado; no hace falta leer todo el tutorial |
| [Tutoriales oficiales de pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html) | Tablas, lectura de datos, selección y columnas calculadas | Relacionar cada operación con una pregunta de tus documentos |
| [Counter en la biblioteca estándar de Python](https://docs.python.org/3/library/collections.html#collections.Counter) | Conteo de elementos | Comprobar qué forma exacta estás contando y qué conserva la regla |
| [Tutorial de pyplot de Matplotlib](https://matplotlib.org/stable/tutorials/pyplot.html) | Ejes, etiquetas y gráficos sencillos | Etiquetar unidades y denominadores antes de personalizar el aspecto |
| [Preguntas frecuentes de Colab](https://research.google.com/colaboratory/faq.html) | Guardado, carga y descarga de notebooks | Distinguir la copia guardada del notebook de los archivos temporales del entorno |

Las versiones de documentación pueden ser posteriores a las bibliotecas del entorno de clase. Los ejemplos básicos elegidos se deben comprobar en el entorno donde se ejecuten. El [registro local](../notebooks/prueba_local.json) conserva las versiones con las que se probó nuestro notebook; la prueba en Colab se registra por separado.

## Lecturas opcionales para interpretar y diseñar

**Grimmer, J. y Stewart, B. M. (2013).** *Text as Data: The Promise and Pitfalls of Automatic Content Analysis Methods for Political Texts*. Political Analysis, 21(3), 267–297. [Ficha editorial y artículo](https://doi.org/10.1093/pan/mps028). Pregunta de lectura: ¿qué parte de mi interpretación necesita conocimiento del contexto y comprobación, aunque el procedimiento sea automático?

**Gentzkow, M., Kelly, B. y Taddy, M. (2019).** *Text as Data*. Journal of Economic Literature, 57(3), 535–574. [Ficha de la American Economic Association](https://www.aeaweb.org/articles?id=10.1257%2Fjel.20181020) y [copia en el sitio académico del autor](https://web.stanford.edu/~gentzkow/research/text-as-data.pdf). Introduce el uso de texto como dato en investigación económica y revisa métodos y aplicaciones. Para empezar, leer la introducción y elegir una aplicación relacionada con tu carrera; las secciones técnicas pueden quedar para después.

**Gilardi, F., Alizadeh, M. M. y Kubli, M. (2023).** *ChatGPT outperforms crowd workers for text-annotation tasks*. Proceedings of the National Academy of Sciences, 120(30), e2305016120. [Artículo y ficha original](https://doi.org/10.1073/pnas.2305016120). Pregunta de lectura: ¿qué tareas y comparadores estudia el artículo y qué necesitaría comprobar antes de trasladar una clasificación a mis propios textos? Sus resultados no validan las etiquetas del caso peruano.

**General Inquirer.** [Sitio académico](https://inquirer.sites.fas.harvard.edu/). Permite conocer un ejemplo histórico de análisis de contenido asistido por computadora y diccionarios. Pregunta de lectura: ¿qué gana una regla de diccionario en consistencia y qué ambigüedad debe resolver leyendo?

Las referencias se verificaron mediante documentación y fichas originales. La ficha de Gentzkow, Kelly y Taddy también coincide con la bibliografía del proyecto de investigación. La selección y las preguntas de lectura son propuestas pedagógicas de este curso; no se afirma haber realizado una lectura integral de cada artículo para esta lista. Se proporcionan enlaces, sin redistribuir copias locales de libros o artículos protegidos.

## Técnicas para una etapa posterior

| Técnica | Qué pregunta añade | Qué conviene dominar antes |
|---|---|---|
| Matriz documento–término | Cómo organizar conteos de muchos términos por documento | Filas, columnas y denominadores |
| Keyness | Qué términos distinguen un conjunto frente a otro | Selección de grupos, frecuencias y lectura contextual |
| Modelado de temas | Qué agrupaciones de vocabulario aparecen bajo un modelo | Calidad de textos, elección de unidades y evaluación de resultados |
| Sentimientos | Qué orientación expresa un texto según una regla o modelo | Adecuación al idioma y dominio, negación y validación |
| Clasificación automática | Cómo asignar categorías con reglas o modelos | Categorías explícitas, revisión humana independiente y casos difíciles |

Esta tabla delimita posibilidades, no promete resultados ni recomienda un modelo concreto. Probit, entrenamiento de modelos y formalización teórica requieren preparación adicional y permanecen fuera de los 110 minutos.

## Aplicación a documentos nuevos

Sigue la [ruta de adaptación](adaptacion_nuevos_documentos.md). Define primero qué documentos y unidades responden a tu pregunta. Conserva los originales y la procedencia; no reutilices las etiquetas de los discursos como si clasificaran contratos, reportes o reclamos.
