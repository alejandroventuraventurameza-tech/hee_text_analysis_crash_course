# Guion docente del curso de análisis textual

La sesión dura 110 minutos, incluidos preguntas, dificultades y entrega. Las slides acompañan el razonamiento y las instrucciones; el notebook concentra la ejecución y las respuestas. Cada estudiante trabaja en su laptop y entrega individualmente sin calificación. La distribución para discutir se decide según asistencia y ritmo.

## Materiales y control del tiempo

Mantener abiertos el [notebook resuelto](../notebooks/docente_resuelto.ipynb), la copia que se ejecutará en vivo y el PDF de slides compilado localmente o en Overleaf. Distribuir únicamente el [notebook de estudiantes](../notebooks/estudiantes.ipynb) para la práctica. Tener disponible el [ZIP de datos](../paquetes/datos_estudiantes.zip) y el [ejercicio individual](../actividades/ejercicio_individual.md). La versión docente tiene resultados orientativos y no se comparte como ejercicio inicial.

La preparación del aula incluye comprobar proyector y HDMI, acceso al notebook y enlace de la carpeta de entrega en Drive. El acceso, copia, guardado y ejecución en Colab se comprobarán después de concluir los materiales. No afirmar que la prueba local sustituye esa comprobación. El estudiante debe conservar las salidas al descargar su `.ipynb`.

Pedir a la persona de apoyo que priorice problemas de acceso y ejecución y que identifique quién aún no ha ejecutado o modificado código. El docente mantiene la pregunta del bloque y atiende dudas de interpretación. La discusión colectiva puede continuar con una salida guardada mientras se repara una laptop, pero cada estudiante debe retomar la ejecución.

Mantener visibles tres metas de avance: seis documentos al minuto 36; comparación al 74; tabla y dos fragmentos al 90. Iniciar el cierre al 98. Los apéndices y referencias de las slides son de consulta y no agregan minutos al recorrido común.

## Agenda y coordinación entre slides y notebook

| Minutos | Slides comunes | Celdas del notebook | Meta y decisión de avance |
|---|---|---|---|
| 0–10 | S01–S05 | Primera hipótesis | Interpretación inicial escrita, sin etiquetas ni presidente |
| 10–15 | S06 | Categorías, conteos y modelos | Historia breve y relación entre enfoques |
| 15–23 | S07–S08, volver a S03–S04 | Clasificación manual | Decisión, evidencia y duda antes de revelar procedencia |
| 23–36 | S09–S12 | Primera celda, Preparación, tabla | Copia propia, código modificado y seis filas |
| 36–51 | S13–S14 | Original y conteo, frecuencias | Transformación explicada y ranking modificado |
| 51–66 | S15–S17 | Predicción, tasas, gráfico | Denominador y comparación individual |
| 66–74 | S18 | Recuperación | Reanudar y comprobar la consulta antes del contexto |
| 74–90 | S19–S22 | Contextos, evidencia, interpretación | Dos documentos distintos y conclusión provisional |
| 90–98 | S23–S24 | Contraste final y respuesta | Un acuerdo, desacuerdo o duda justificada |
| 98–110 | S25–S27 | Conclusión, limitación, aplicación, comprobación | Guardar y entregar individualmente |

Los nombres de slide son referencias estables de guion; las etiquetas internas permiten localizar cada frame en `3_content.tex`. No es necesario proyectar todas las slides mientras los estudiantes están ejecutando.

## Apertura de 0 a 10 minutos

**0–3, S02.** Preguntar: «¿Cómo analizarían cientos de discursos sin leerlos completos?». Recoger dos procedimientos y preguntar qué puede contarse y qué requiere lectura. Decir: «Hoy estudiaremos lo que los mensajes declaran. Para establecer qué se ejecutó necesitamos otras fuentes».

**3–7, S03–S04.** Mostrar A y B, primero sin presidente. Pedir una expresión y una duda. Las slides contienen extractos breves; las unidades completas están en el notebook. No asignar aún una etiqueta ni anticipar quién habla. Si alguien reconoce al presidente, pedir que igualmente justifique con el texto, no con su reputación histórica.

**7–10, S05.** Presentar la pregunta y la entrega. Cada estudiante escribe su primera hipótesis. Conectar brevemente con un documento de su carrera: contratos y excepciones, riesgos en reportes, prioridades empresariales, noticias, reclamos o encuestas abiertas. No pedir que todos expliquen su aplicación en este momento.

## Historia de 10 a 15 minutos

**S06.** Explicar categorías y reglas de análisis de contenido, situar Berelson en 1952 y presentar General Inquirer como ejemplo computacional con diccionarios. Introducir modelos de lenguaje mediante el estudio de Gilardi, Alizadeh y Kubli de 2023. No atribuir a Berelson el nacimiento de toda lectura sistemática ni extrapolar el desempeño del estudio reciente a esta investigación.

Preguntar qué enfoque permite fijar reglas, qué operación amplía la escala y qué resultados exigen volver al texto. Aclarar que los modelos de lenguaje también son métodos computacionales. Los enfoques conviven; la cronología no demuestra que los anteriores se hayan vuelto innecesarios. Detener la historia al minuto 15.

## Clasificación manual de 15 a 23 minutos

**15–18, S07.** Definir roles por instrumento dominante. Empresario exige propiedad y control de producción; regulador refiere a reglas generales y supervisión de mercados; facilitador refiere a promoción selectiva sin requerir propiedad. También existen asistencial y no aplica. Aceptar evidencia insuficiente como respuesta provisional didáctica, no como una etiqueta nueva del modelo.

**18–21, S08 y retorno a fragmentos.** Pedir decisión, expresión y duda sobre A y B. No preguntar solo «¿qué rol es?». Preguntar quién produce, qué se transfiere y qué finalidad se declara. Advertir que en B la oración anterior llama al Estado ente promotor: leer esa oración en el notebook antes de cerrar la interpretación.

**21–23.** Recoger dos razonamientos y revelar oralmente la procedencia: A es Velasco 1970, `u11860`, p. 10; B es Alberto Fujimori 1991, `u14275`, p. 10. Conservar ocultas las etiquetas automáticas. Recordar que una unidad es un segmento reconstruido y puede reunir asuntos distintos. Las etiquetas se contrastarán al minuto 90.

## Colab y carga de 23 a 36 minutos

**23–26, S09.** Distinguir lenguaje, biblioteca y entorno. Mostrar la copia propia y cómo editar una celda de texto. La persona de apoyo atiende accesos; mantener una explicación común breve.

**26–29, S10.** Ejecutar el saludo, cambiarlo y volver a ejecutar. Explicar únicamente variable, asignación, comillas y mostrar resultados. No convertir este paso en una introducción completa a Python.

**29–33, S11.** Presentar pandas cuando resuelve la tabla. Ejecutar Preparación con carga incluida; los datos están dentro del notebook. La implementación extensa permanece en una celda preparada. Si se necesita el ZIP, elegir manual y subir el archivo indicado. No hace falta enseñar Git ni montar Drive.

**33–36, S12.** Ejecutar la tabla. Preguntar qué representa una fila, qué metadatos permiten comparar y qué diferencia hay entre documento y unidad. Distinguir la tabla agrupada de tres pares en las slides de las seis filas del notebook. No cargar clasificaciones.

**Punto de recuperación:** seis documentos disponibles. Si falta un nombre, ejecutar Preparación; si se reinició el entorno, la misma celda reconstruye datos y herramientas. La persona de apoyo mantiene registro de quienes aún necesitan completar este paso.

## Transformación y frecuencias de 36 a 51 minutos

**36–43, S13.** Pedir una predicción sobre original y versión para conteos; ejecutar la celda que recupera ambas. El procesamiento se hizo durante la preparación de datos, no con un modelo lingüístico en vivo. Explicar minúsculas, secuencias de letras, descarte editorial y conservación de negaciones. Mostrar por qué quitar «no» puede cambiar el sentido. El ejemplo de la slide es literal y localizable en Leguía de 1921, p. 11.

Definir token como cada aparición según la regla. Singular, plural y sinónimos siguen separados. Mostrar la diferencia entre conservar textos para leer y preparar una copia para contar, sin explicar expresiones regulares durante el recorrido común.

**43–47, S14.** Antes de ejecutar, pedir una predicción sobre el ranking. Presentar Counter como herramienta estándar para conteos. Ejecutar y cambiar `numero_palabras` de 10 a 8. Explicar que ocultar palabras del ranking no modifica el denominador.

**47–51.** Pedir que expliquen su modificación y una transformación. Comprobar un término en el original o señalar que lo harán con la búsqueda preparada. Aceptar una pregunta breve sobre ambigüedad, sin empezar técnicas nuevas.

## Comparación de 51 a 66 minutos

**51–54, S15.** Mantener oculta S17. Pedir la predicción y advertir que mayor extensión permite más menciones absolutas. El ejemplo común es competencia en Leguía 1921 y Alberto Fujimori 1991; se puede cambiar la palabra o los documentos.

**54–58, S16.** Ejecutar tasas y explicar numerador y denominador. Leer «menciones por mil palabras». No llamar porcentaje a la tasa. Mostrar la tabla con menciones, palabras y tasas, sin ocultar el denominador.

**58–62, S17 y notebook.** Mostrar S17 solo después de que los estudiantes hayan escrito y ejecutado. En la consulta inicial hay 2/4.527 y 11/23.348, aproximadamente 0,442 y 0,471 por mil. Preguntar qué cambió frente al conteo. Presentar matplotlib cuando se necesita el gráfico. El apéndice A02 conserva un gráfico de reserva.

**62–66.** Guardar tabla o gráfico y una interpretación provisional. No convertir la cercanía de tasas en prueba de igualdad ni su diferencia en significación estadística. Si alguien cambia la consulta, interpretar su resultado; los valores de S17 solo describen la consulta inicial.

## Recuperación de 66 a 74 minutos

**S18.** Dedicar dos minutos a identificar problemas, cuatro a reanudar y dos a comprobar que todos entienden palabra, documentos y denominador. Si los problemas están resueltos, una pausa de hasta dos minutos cabe dentro del bloque. La celda Recuperación vuelve a cargar tablas y recalcula; si el entorno se reinició, ejecutar Preparación primero.

Los resultados guardados son una alternativa indicada por el docente después de la predicción. Se marcan como guardados y permiten interpretar durante la reparación. La ejecución individual debe retomarse. No presentar esa salida como cálculo realizado por el estudiante.

## Contexto de 74 a 90 minutos

**74–77, S19.** Pedir una predicción de significado y explicar búsqueda en contexto. Se busca en la extracción original, no en una versión sin negaciones. Guiones reparados y rótulos excluidos pueden producir diferencias respecto del conteo.

**77–81, S20.** Ejecutar contextos y cambiar amplitud de 100 a 180 caracteres. Explicar que son caracteres a cada lado, no palabras. Pedir dos filas de documentos distintos. Para la consulta inicial sirven 0 y 3; otros términos requieren revisar los índices.

**81–86.** Recuperar las unidades completas. Si no hay unidad asociada, la celda recupera la página. Mostrar S21 después de que hayan examinado sus pasajes: Leguía utiliza competencia para capacidad profesional y el pasaje de Fujimori refiere al mercado. Los dos ejemplos no clasifican todas las ocurrencias. `u00126` continúa con fomento agrícola, lo que ilustra una unidad con varios temas.

**86–90, S22.** Redactar una conclusión provisional y una limitación concreta. Si la palabra no produce coincidencias útiles, cambiarla y explicarlo. No inventar fragmentos ni tratar la ausencia léxica como ausencia conceptual.

**Punto de recuperación:** resultado numérico y dos fragmentos identificados, con sus páginas y unidades.

## Etiquetas de 90 a 98 minutos

**90–95, S23.** Ejecutar la celda independiente de etiquetas existentes. Volver a la primera clasificación: el modelo asignó empresario con confianza alta a A y regulador con confianza media a B, además de asistencial como secundaria en B. Preguntar por un acuerdo, desacuerdo o duda y exigir evidencia. Aceptar una revisión de la decisión inicial sin borrarla.

**95–98, S24.** Explicar dos límites: el segundo anotador fue otro modelo de lenguaje, y la referencia de 30 unidades solo contiene un caso empresario y uno regulador. La confianza no es una probabilidad calibrada. No presentar validación entre dos humanos ni calcular proporciones con los seis ejemplos dirigidos.

## Entrega de 98 a 110 minutos

**98–102, S25.** Completar conclusión y verificar palabra, documentos, denominadores y localización de los dos fragmentos. La tabla basta si falta tiempo. El cierre técnico solo comprueba que tabla y evidencia corresponden a la consulta actual; no evalúa las respuestas.

**102–106, S25–S26.** Completar una limitación que restrinja una afirmación y la aplicación a documentos de la carrera. Usar la tabla de aplicaciones como apoyo, sin exigir que todos compartan oralmente. Realizar autoevaluación sin puntos.

**106–109, S27.** Guardar y descargar `.ipynb` con respuestas y salidas; subir a la carpeta de Drive indicada y comprobar que aparece. Los CSV y PNG complementarios no sustituyen la entrega. Si falla la subida, conservar el archivo y registrar la incidencia.

**109–110.** Pedir una decisión que puedan modificar y una afirmación que todavía no puedan sostener. Confirmar entregas pendientes.

## Errores frecuentes y respuestas breves

| Situación | Respuesta o recuperación |
|---|---|
| Editó pero no ve cambios | Volver a ejecutar la celda modificada y las que dependen de ella |
| Un nombre no existe | Ejecutar Preparación y retomar el punto correspondiente |
| Identificador escrito distinto | Copiarlo de la tabla de documentos, sin repetirlo |
| Busca varias palabras como una | El ejercicio usa una forma exacta; elegir una sola y conservar tildes |
| No hay coincidencias | Revisar forma, acento y documentos; registrar ausencia y elegir otra si hace falta |
| Quitó palabras del ranking y usa ese total | Recuperar el total de `texto_conteo`, no el ranking filtrado |
| Cree que competencia siempre significa mercado | Ampliar el contexto y comprobar el instrumento y la finalidad |
| Selecciona dos filas del mismo documento | Elegir otra fila; revisar índices después de cambiar la consulta |
| Cambió consulta y dejó evidencia antigua | Volver a ejecutar tasas, contexto y selección; comprobar al cerrar |
| Una unidad tiene dos temas | Reconocer la reconstrucción y leer la página original |
| Describe una etiqueta como verdad | Pedir evidencia y revisar justificación, contexto y validación |
| El trabajo final solo trae un gráfico | Pedir conclusión, fragmentos, limitación y aplicación dentro del notebook |

## Recortes para proteger el recorrido común

Si hay unos cinco minutos de retraso, mantener competencia y los dos documentos iniciales, conservar la tabla sin personalizar el gráfico y reducir intervenciones colectivas. Cada estudiante debe modificar al menos una decisión sencilla y explicar el efecto. Conservar los dos fragmentos y los doce minutos de cierre.

Si al minuto 74 persisten problemas, recuperar tablas, leer dos pasajes de la consulta común y reducir el contraste con etiquetas a un caso breve. Trasladar ese tiempo a ejecución y entrega, registrando quién necesita apoyo. No agregar el desafío opcional a quienes todavía construyen su producto común.

Los apéndices A01–A04 y las referencias se reservan para consultas y continuación. Los datos, citas y respuestas orientativas proceden de los materiales revisados; la [guía de ejemplos](../data/docente/guia_ejemplos.md) amplía los casos de reserva. La [documentación de slides](../slides/README.md) explica la compilación local, la alternativa de Overleaf y la revisión visual realizada.
