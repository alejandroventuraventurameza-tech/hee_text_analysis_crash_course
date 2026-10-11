# Curso presencial de análisis textual con Python

Materiales para una sesión de 110 minutos prevista para el lunes 12 de octubre de 2026, a cargo de Alejandro Ventura, por invitación de la profesora Beatriz Rodríguez Santizabal. El curso utiliza Google Colab y mensajes presidenciales peruanos como caso para aprender a comparar palabras y comprobar interpretaciones con evidencia textual.

## Diseño acordado

El recorrido común comprende cargar textos y metadatos, explicar una transformación, construir frecuencias, comparar menciones por 1.000 palabras, buscar en contexto y formular una conclusión con una limitación. Cada estudiante ejecuta y modifica código en su laptop y realiza una entrega individual formativa, sin calificación. La discusión puede realizarse individualmente, en parejas o en grupos según asistencia y ritmo.

Los discursos permiten estudiar instrumentos y prioridades declaradas. Para establecer cómo actúa efectivamente un gobierno hacen falta otras fuentes. Las frecuencias de palabras no identifican por sí solas roles económicos ni relaciones causales.

## Materiales disponibles

Para estudiantes: empezar por la [preparación breve](docs/preparacion_estudiantes.md) y abrir el notebook individual. La versión docente, los resultados guardados y las etiquetas se utilizan en los momentos indicados por el docente.

| Material | Uso |
|---|---|
| [Plan de la sesión](docs/plan_sesion.md) | Tiempos, objetivos, actividades, comprobaciones y recuperación |
| [Ejercicio individual](actividades/ejercicio_individual.md) | Consigna, estructura de respuestas y autoevaluación |
| [Datos didácticos](data/README.md) | Seis discursos, unidades sin etiquetas, fuentes, selección y límites |
| [Diccionario de columnas](data/diccionario_columnas.md) | Significado de filas, campos y denominadores |
| [Paquete de datos para estudiantes](paquetes/datos_estudiantes.zip) | Descarga para carga manual, sin clasificaciones |
| [Notebook para estudiantes](notebooks/estudiantes.ipynb) | Práctica individual con datos incluidos y preguntas antes de ejecutar |
| [Notebook resuelto para el docente](notebooks/docente_resuelto.ipynb) | Respuestas orientativas y salidas de la ejecución local |
| [Uso y pruebas de los notebooks](notebooks/README.md) | Carga, recuperación, entrega y diferencias respecto de Colab |
| [Guion docente](docs/guion_docente.md) | Coordinación de tiempos, preguntas, errores y recortes |
| [Slides Beamer](slides/README.md) | Archivos editables y configuración para Overleaf |
| [ZIP para Overleaf](paquetes/beamer_overleaf.zip) | Proyecto autocontenido para XeLaTeX y Biber |
| [Preparación de estudiantes](docs/preparacion_estudiantes.md) | Acceso, primera celda, carga y guardado |
| [Recursos para continuar](docs/recursos_continuacion.md) | Prácticas y lecturas opcionales verificadas |
| [Adaptación a documentos nuevos](docs/adaptacion_nuevos_documentos.md) | Pregunta, selección, metadatos, conteos y evidencia |
| [Comprobación final](docs/comprobacion_final.md) | Estado, pruebas reales pendientes y registro de incidencias |

## Comprobaciones antes de la clase

1. Comprobación en Colab de acceso, ejecución, carga, copia y guardado al concluir los materiales.
2. Compilación y revisión visual de las slides en Overleaf a cargo del docente.
3. Publicación del repositorio por el autor y comprobación del acceso público.
4. Carpeta de entrega en Drive y recepción de una entrega de prueba.

Los nueve entregables de preparación están disponibles. Las comprobaciones anteriores siguen pendientes y deben registrarse antes de considerar verificada la sesión completa.

## Organización del aula virtual

```text
actividades/   Ejercicio individual y autoevaluación
data/          Originales, textos, metadatos, unidades y trazabilidad
data/docente/  Etiquetas separadas y guía de ejemplos
docs/          Plan, guion, preparación, adaptación y recursos
notebooks/     Versiones de estudiantes y docente, con prueba local
slides/        Proyecto Beamer editable y revisión estática
paquetes/      ZIP de datos y ZIP autocontenido de Overleaf
scripts/       Preparación y comprobación docente reproducibles
```

La selección revisada comprende los mensajes del 28 de julio de Leguía de 1920 y 1921, Velasco de 1969 y 1970, y Alberto Fujimori de 1991 y 1992: seis PDF, 148 páginas y 619 unidades existentes. La documentación conserva diferencias de audiencia y ocasión. Los resultados describen esos documentos, sin extrapolarse al corpus completo.

## Acceso y entrega

Este repositorio será público. El acceso a los materiales no requiere aprender Git ni acceder al repositorio de investigación. El notebook incluye los datos y dispone de una alternativa de carga manual con ZIP y resultados guardados. Ambos notebooks se probaron completos localmente. La prueba guiada en Colab confirmó resultados hasta el contraste y la comprobación técnica de entrega; su [registro](notebooks/prueba_colab_guiada.json) distingue los pasos recibidos de las comprobaciones aún pendientes.

La entrega se realizará en una carpeta de Drive cuyo enlace se comunicará en clase. Cada estudiante entregará su notebook con las respuestas y salidas guardadas. La prueba completa de Colab se realizará después de concluir el diseño y los materiales.

## Procedencia y preparación

El caso procede de la versión `v1.0-ccl` de la investigación sobre roles económicos en discursos presidenciales peruanos. Los extractos didácticos se prepararon aquí con trazabilidad; el repositorio de investigación y el template Beamer original se conservan sin modificaciones. Los materiales locales de análisis textual en R sirven como referencia conceptual y pedagógica para la adaptación a Python.

La preparación avanza por entregables revisables en la rama `first_branch`. El autor realiza los commits y la publicación. Este repositorio no incluye claves, documentos personales ni copias de bibliografía cuya redistribución no esté permitida.
