# Plan del curso presencial de análisis textual

La sesión está prevista para el lunes 12 de octubre de 2026 y dura exactamente 110 minutos. Está dirigida a aproximadamente 30 estudiantes, principalmente de cuarto y quinto ciclo de Administración, Economía, Finanzas, Derecho, Ingeniería Empresarial e Ingeniería de la Información, con experiencia promedio casi nula en programación. Alejandro Ventura conducirá la práctica por invitación de la profesora Beatriz Rodríguez Santizabal, con una persona de apoyo para dificultades de acceso y ejecución.

## Pregunta y alcance

¿Qué instrumentos de intervención económica aparecen en estos mensajes presidenciales y qué diferencias podemos sostener al comparar palabras y leer fragmentos?

Los textos permiten estudiar instrumentos y prioridades declaradas. No bastan para establecer qué hizo efectivamente un gobierno ni para atribuir efectos causales. Los conteos localizan patrones que deben comprobarse leyendo; una palabra aislada no equivale a un rol económico.

El objetivo es que cada estudiante complete un análisis pequeño y pueda explicar y modificar sus decisiones. Las operaciones difíciles estarán preparadas. Las explicaciones de sintaxis se limitarán a lo necesario para la operación inmediata.

## Objetivos y evidencias

| Al finalizar el estudiante podrá | Evidencia observable |
|---|---|
| Cargar textos y reconocer metadatos | Identifica documentos, fechas, gobierno y significado de una fila |
| Explicar una transformación sencilla | Describe un cambio entre original y versión de conteo y una consecuencia |
| Construir frecuencias y una comparación normalizada | Presenta una tabla o gráfico con conteos, denominadores y menciones por 1.000 palabras |
| Buscar palabras en contexto | Recupera fragmentos originales con sus identificadores y amplía el contexto cuando hace falta |
| Formular una conclusión respaldada y limitada | Conecta el resultado numérico con evidencia textual y reconoce una limitación concreta |
| Adaptar el procedimiento a su carrera | Propone documentos, metadatos y una pregunta viable para otro caso |

## Condiciones de trabajo

Cada estudiante dispone de laptop y trabaja en su propia copia del notebook de Google Colab. La discusión puede ser individual, en parejas o en grupos de tres o cuatro, según asistencia y ritmo. La participación conjunta no sustituye la ejecución, modificación ni entrega individual.

El aula cuenta con internet, proyector y conexión HDMI. El notebook ofrecerá carga desde materiales públicos, carga manual y celdas para recuperar resultados intermedios. Los resultados guardados permitirán continuar interpretando mientras se resuelve una dificultad, pero no sustituyen la ejecución individual: la persona de apoyo ayudará a completarla durante la sesión.

Las predicciones se escribirán antes de ejecutar. En cada actividad analítica se repetirá: pregunta → predicción → ejecución → interpretación → comprobación con el original. Las respuestas y etiquetas del docente permanecerán fuera de la versión inicial del estudiante.

## Agenda de 110 minutos

| Intervalo | Minutos | Bloque | Resultado al terminar |
|---|---:|---|---|
| 0–10 | 10 | Motivación e hipótesis | Primera interpretación escrita |
| 10–15 | 5 | Historia y enfoques | Distinción entre categorías, conteos y modelos de lenguaje |
| 15–23 | 8 | Instrumentos y clasificación manual | Clasificación provisional con evidencia |
| 23–36 | 13 | Colab y carga | Copia propia, celda modificada y tabla cargada |
| 36–51 | 15 | Transformación y frecuencias | Tabla y explicación de una transformación |
| 51–66 | 15 | Comparación normalizada | Conteos, denominadores, tasas y gráfico |
| 66–74 | 8 | Dudas y recuperación | Punto común de comparación recuperado |
| 74–90 | 16 | Búsqueda en contexto | Dos fragmentos y revisión de la hipótesis |
| 90–98 | 8 | Etiquetas existentes y límites | Un acuerdo o desacuerdo justificado |
| 98–110 | 12 | Entrega y transferencia | Notebook individual entregado |
| Total | 110 | | |

Las preguntas y dificultades breves forman parte de todos los bloques. Los ocho minutos de recuperación constituyen una reserva adicional.

## Desarrollo minuto a minuto

### Motivación e hipótesis

**0–3.** Plantear: «¿Cómo analizarían cientos de discursos sin leerlos todos de principio a fin?». Recoger procedimientos propuestos y distinguir localizar pasajes, contar y comprender significado. Aclarar el alcance de la evidencia discursiva.

**3–7.** Mostrar dos fragmentos reales, sin identificar inicialmente al presidente y sin etiquetas. Cada estudiante escribe qué intervención económica reconoce y subraya la expresión que sostiene su interpretación. Discutir una ambigüedad antes de revelar la procedencia. Los fragmentos y sus referencias se fijarán después de revisar los datos; no se utilizarán ejemplos inventados como citas.

**7–10.** Pedir una hipótesis sobre diferencias entre los documentos. Conectar el procedimiento con obligaciones en contratos y normas, riesgos en reportes financieros, prioridades empresariales y problemas recurrentes en noticias, reclamos o encuestas abiertas. Presentar la entrega individual para que el estudiante sepa qué irá construyendo.

**Comprobación:** distinguir «este mensaje declara» de «este gobierno ejecutó».

### Historia y enfoques

**10–12.** Explicar el análisis de contenido: interpretación sistemática mediante categorías y reglas explícitas. Situar la sistematización de Berelson en 1952 como un antecedente, sin afirmar que allí nació toda lectura sistemática de textos.

**12–14.** Presentar el análisis asistido por computadora, ejemplificado por General Inquirer: los diccionarios permiten aplicar categorías y contar de manera consistente. Explicar que los métodos computacionales incluyen técnicas diversas; los modelos de lenguaje son una familia dentro de ese ámbito, no una etapa que sustituye todo lo anterior.

**14–15.** Presentar el uso de modelos de lenguaje para clasificar textos mediante instrucciones, con el estudio de Gilardi, Alizadeh y Kubli de 2023 como ejemplo. Solicitar que los estudiantes identifiquen qué enfoque ayuda a establecer reglas, cuál facilita conteos y qué resultados exigen revisión.

**Comprobación:** la automatización amplía la escala, pero no elimina la necesidad de definir conceptos y comprobar errores. No extrapolar el desempeño de ese estudio al corpus peruano.

### Instrumentos y clasificación manual

**15–18.** Definir los roles por el instrumento dominante: empresario, propiedad y control de producción estatal; regulador, reglas generales y supervisión de mercados; facilitador, promoción selectiva sin requerir propiedad estatal. Explicar que son categorías del caso de investigación. Presentar asistencial y no aplica como opciones adicionales; «evidencia insuficiente» será una respuesta didáctica provisional, no una etiqueta automática nueva.

**18–21.** Volver a los dos fragmentos y pedir clasificación provisional, evidencia y una duda. Mantener ocultas las etiquetas existentes. Para un caso ambiguo, preguntar qué información adicional permitiría decidir. No atribuir a toda una presidencia la etiqueta de un fragmento.

**21–23.** Compartir dos razonamientos distintos. Registrar la decisión inicial para revisarla al minuto 90. Explicar que las unidades del conjunto son segmentos reconstruidos y no necesariamente los párrafos tipográficos del documento.

**Comprobación:** evaluar el instrumento descrito y su finalidad declarada, en lugar de clasificar por una palabra aislada.

### Colab y carga

**23–26.** Explicar tres elementos: Python es el lenguaje en que escribimos instrucciones; una biblioteca reúne herramientas reutilizables; Colab es el entorno donde editamos el notebook y ejecutamos Python. Un notebook combina explicaciones, instrucciones y resultados. Abrir y guardar una copia propia.

**26–29.** Ejecutar una celda pequeña y cambiar el valor de una variable. Mostrar el orden de ejecución y cómo volver a ejecutar una celda después de modificarla. La persona de apoyo atiende accesos y copias mientras el docente mantiene el ejemplo común.

**29–33.** Presentar pandas cuando se necesite leer y explorar la tabla. Cargar los datos públicos; activar la carga manual si la primera vía falla. Mostrar las primeras filas y el número de documentos.

**33–36.** Cada estudiante identifica fecha, gobierno e identificador, explica qué representa una fila y verifica que no son unidades ni etiquetas. No cargar todavía las clasificaciones.

**Recuperación al minuto 36:** copia propia abierta y tabla de documentos disponible. Una celda preparada volverá a cargarla sin repetir la explicación inicial. Mantener visible a quién falta ayudar.

### Transformación y frecuencias

**36–39.** Mostrar original y versión para conteos. Pedir una predicción sobre qué cambia al convertir mayúsculas en minúsculas y separar palabras. Definir token como cada aparición de una palabra según la regla utilizada. Conservar tildes y negaciones.

**39–43.** Ejecutar el procesamiento preparado y comparar un pasaje antes y después. Explicar la regla usada y una limitación, como diferencias entre formas singular y plural. El código conservará por separado el texto para lectura y la versión para frecuencias.

**43–47.** Construir una tabla de frecuencias. Cada estudiante cambia el número de términos mostrados y anticipa qué aparecerá. Si se ocultan palabras frecuentes de escaso interés para la visualización, explicar que esa decisión no las elimina del denominador acordado.

**47–51.** Interpretar el ranking, revisar un término en su pasaje original y completar la respuesta sobre una transformación. Recoger una duda. Una palabra muy frecuente puede tener usos distintos dentro del mismo texto.

**Comprobación:** el estudiante explica qué contó el código y qué conservó para leer.

### Comparación normalizada

**51–54.** Preguntar si un discurso más largo podría acumular más menciones sin una mayor presencia relativa. Cada estudiante registra una predicción sobre una palabra de su elección entre las opciones que se preparen tras revisar los documentos.

**54–58.** Ejecutar una comparación con conteo, total de palabras y tasa: menciones por 1.000 palabras = 1.000 × menciones / palabras del documento procesado. El denominador incluye todas las palabras obtenidas por la misma regla, incluso las ocultas del ranking. Mostrar resultados por documento.

**58–62.** Cambiar la palabra consultada. Presentar matplotlib cuando se necesite representar las tasas. Ejecutar el gráfico preparado y leer ejes y unidades. No exigir personalización del diseño.

**62–66.** Comparar predicción y resultado. Guardar una tabla o gráfico para la entrega. Si se agrupa por gobierno, explicar que la tasa conjunta divide la suma de menciones por la suma de palabras, no el promedio simple de tasas; el recorrido común prioriza la comparación por documento.

**Comprobación:** expresar «X menciones por 1.000 palabras en los documentos seleccionados». No convertir la tasa en porcentaje de unidades con un rol.

### Dudas y recuperación

**66–68.** Comprobar quién tiene una comparación disponible y recoger el obstáculo más común. La persona de apoyo prioriza quienes aún no ejecutaron o modificaron código.

**68–72.** Reanudar mediante la celda que recupera datos y operaciones hasta la comparación. Quien ya esté listo verifica su denominador y guarda su salida. Si las dificultades están resueltas, usar hasta dos minutos para una pausa breve dentro de este intervalo.

**72–74.** Confirmar que cada estudiante identifica la palabra buscada, los documentos y el denominador. Anticipar que la interpretación puede cambiar al leer.

**Recuperación al minuto 74:** tabla de comparación utilizable. Los resultados guardados sirven para la discusión durante la reparación, y cada estudiante retoma después su ejecución.

### Búsqueda en contexto

**74–77.** Formular: «¿La palabra significa lo que supusimos?». Registrar una predicción sobre su uso. Definir búsqueda en contexto como localizar una palabra junto con el texto que permite interpretar su significado.

**77–81.** Ejecutar la búsqueda preparada sobre el texto conservado. Mostrar una ventana breve y ampliar hasta la unidad completa cuando sea necesario. Mantener negaciones, fechas y referencias.

**81–86.** Cada estudiante cambia la palabra o amplía el contexto y conserva dos fragmentos de documentos distintos que informen la comparación. Puede utilizar un fragmento que cuestione la hipótesis. Si una palabra no aparece, registrar la ausencia y buscar otra que permita comprobar el argumento; no inventar evidencia ni tratar ausencia léxica como ausencia del concepto.

**86–90.** Escribir una conclusión provisional que relacione conteos y fragmentos. Preguntar qué cambió al leer y qué sigue incierto. Elegir una limitación concreta.

**Recuperación al minuto 90:** resultado numérico y dos fragmentos identificables reunidos en el notebook.

### Etiquetas existentes y límites

**90–92.** Cargar las etiquetas separadas y explicar la diferencia entre una fila de documento y una fila de unidad. Las etiquetas provienen de un modelo de lenguaje que aplicó reglas de clasificación; no son verdad indiscutible.

**92–95.** Volver a la clasificación manual inicial y contrastar un caso con la etiqueta y justificación existentes. El estudiante conserva o modifica su decisión citando la evidencia, y puede mantener una duda.

**95–98.** Explicar las limitaciones de la validación del proyecto: el segundo anotador fue otro modelo de lenguaje; el conjunto de referencia de 30 unidades contiene solo un caso empresario y uno regulador. No describir el acuerdo como validación entre dos humanos. No calcular una mezcla de roles a partir de los ejemplos dirigidos. Si posteriormente se muestra una tabla de roles, debe declarar selección y denominador.

**Comprobación:** frecuencia de palabras, clasificación semántica y actuación efectiva del gobierno son medidas diferentes.

### Entrega y transferencia

**98–102.** Completar la conclusión y verificar que la tabla o gráfico tiene palabra consultada, documentos, unidades y denominador. Revisar las referencias de los fragmentos.

**102–106.** Escribir una limitación que indique qué interpretación restringe y una aplicación a documentos de su carrera. Completar la autoevaluación del ejercicio individual.

**106–109.** Guardar y descargar el notebook con respuestas y salidas; subirlo a la carpeta de Drive indicada. La persona de apoyo atiende problemas de guardado y entrega. No se exige compartir públicamente el trabajo personal.

**109–110.** Cierre oral: cada estudiante identifica una decisión que puede modificar y una afirmación que sus datos no permiten sostener. Confirmar entregas pendientes.

## Ajustes según el ritmo

Si se acumulan unos cinco minutos de retraso, usar una sola palabra común en la comparación, conservar la tabla como resultado suficiente y reducir la discusión colectiva a dos intervenciones. Mantener la modificación individual de una variable, la lectura del original y los doce minutos de cierre.

Si al minuto 74 persisten problemas de ejecución, usar el código de recuperación y la tabla como producto común. Reducir el contraste con etiquetas a un caso breve y transferir el tiempo restante a completar la comparación y la entrega. Registrar qué estudiantes requieren apoyo para terminar su ejecución; una salida guardada por el docente no demuestra que hayan ejecutado el análisis.

Los desafíos avanzados son opcionales: retirar un documento y observar el efecto; comparar la tasa conjunta con el promedio de tasas; modificar el filtrado del ranking y explicar qué cambia y qué no. Se realizan cuando el producto común está completo y no condicionan la entrega.

## Criterios para cerrar la selección de datos

La selección revisada comprende dos mensajes por gobierno: Leguía, 28 de julio de 1920 y 1921; Velasco, 28 de julio de 1969 y 1970; Alberto Fujimori, 28 de julio de 1991 y 1992. La regla usa los primeros mensajes anuales disponibles posteriores al inicio del gobierno, antes de observar resultados. Se comprobó la extracción y se conservaron diferencias de audiencia y ocasión en los metadatos. La coincidencia de fecha no elimina diferencias institucionales. El detalle está en la [documentación de datos](../data/README.md).

Se compararán documentos completos. Los pasajes seleccionados para enseñar conceptos se identificarán como ejemplos dirigidos y no determinarán la muestra comparativa. Los textos originales se conservarán separados del procesamiento; cada extracto mantendrá identificador y procedencia desde `v1.0-ccl`.

## Referencias y adaptaciones

La progresión de texto, metadatos, transformaciones, frecuencias y búsqueda en contexto adapta conceptualmente los materiales locales de formación en R. La implementación será propia en Python. No se trasladan instalaciones, rutas personales ni técnicas avanzadas del recorrido original.

- Berelson, B. (1952). *Content Analysis in Communication Research*. Referencia bibliográfica corroborada mediante la [reseña contemporánea en The Library Quarterly](https://www.journals.uchicago.edu/doi/10.1086/617924). No se presupone consulta del libro completo.
- [General Inquirer, sitio académico de Harvard](https://inquirer.sites.fas.harvard.edu/). Ejemplo de análisis de contenido asistido por computadora.
- Gilardi, F., Alizadeh, M. M. y Kubli, M. (2023). [ChatGPT outperforms crowd workers for text-annotation tasks](https://doi.org/10.1073/PNAS.2305016120). Ejemplo de aplicación de modelos de lenguaje a tareas de anotación.
- Grimmer, J. y Stewart, B. M. (2013). [Text as Data: The Promise and Pitfalls of Automatic Content Analysis Methods for Political Texts](https://www.cambridge.org/core/journals/political-analysis/article/text-as-datathe-promise-and-pitfalls-of-automatic-content-analysis-methods-for-politicaltexts/F7AAC8B2909441603FEB25C156448F20). Fundamento para relacionar automatización e interpretación.
- [Documentación de pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html) y [preguntas frecuentes de Colab](https://research.google.com/colaboratory/faq.html). Referencias para preparar la práctica y el acceso.

Las divisiones de tiempo, actividades, recuperación y entrega son decisiones de diseño de esta sesión, no resultados de esas fuentes. Los fragmentos, conteos y respuestas resueltas se incorporarán después de revisar y probar los materiales.
