# Comprobación final de la sesión

Los materiales están preparados para revisar el recorrido de principio a fin antes de la clase del 12 de octubre de 2026. Este registro separa evidencia ya obtenida de tareas pendientes; una instrucción escrita no equivale a una comprobación realizada.

## Estado al 11 de octubre de 2026

| Componente | Estado y evidencia |
|---|---|
| Plan y ejercicio individual | Preparados; agenda consecutiva de 110 minutos y criterios formativos |
| Datos | Seis PDF trazables, 148 páginas y 619 unidades; integridad y procedencia comprobadas |
| Notebooks | Ambas versiones ejecutadas completas localmente; [registro](../notebooks/prueba_local.json) |
| Carga manual | Lectura local y subida mediante interfaz real de Colab comprobadas; el usuario recibió 6 documentos y 619 unidades |
| Colab | Recorrido común recibido mediante prueba guiada, con guardado y reapertura confirmados. Copia descargada revisada con texto, gráfico y tablas. Recuperación final recibida y versiones registradas; reinicio real sin confirmación explícita |
| Beamer | Revisión estática, compilación local y revisión visual de 34 páginas realizadas; [registro visual](../slides/revision_visual.json) |
| Overleaf | Alternativa opcional; la presentación ya se compiló localmente |
| Acceso público | Repositorio local sin remoto configurado; publicación a cargo del autor |
| Entrega en Drive | Carpeta creada y prueba docente recibida; acceso institucional de estudiantes pendiente |

Las versiones de la prueba local fueron Python 3.13.14, pandas 3.0.2 y matplotlib 3.10.9, sobre Windows. No se presupone que Colab tenga esas versiones ni que su formulario y descarga se comporten exactamente igual.

El 11 de octubre se abrió Colab en el navegador integrado y se observó el enlace Iniciar sesión. No se ejecutó el notebook en esa sesión. El usuario continuó una prueba guiada propuesta para Brave y compartió salidas de Colab: carga incluida, seis filas, original y conteo, ranking cambiado de 10 a 8 con denominador intacto, tasas y gráfico, tabla tras recuperación, 13 coincidencias y dos unidades completas con páginas y enlaces. También compartió el contraste con las etiquetas esperadas y la comprobación técnica de entrega, con tabla marcada como recalculada. El [registro guiado](../notebooks/prueba_colab_guiada.json) conserva el alcance de esa evidencia. No equivale a una comprobación completa ni a control directo del navegador.

Las ventanas ampliadas aparecían recortadas por un límite visual de 250 caracteres. Se retiró ese límite en las dos versiones del notebook y el usuario compartió la salida corregida sin truncamiento. La tabla de etiquetas también recortaba justificaciones: se retiró el límite en esa celda, pendiente de ejecutar el cambio de tabla en la copia del usuario. Las justificaciones completas se recibieron mediante una celda adicional de impresión. Los textos originales, conteos y etiquetas no cambian.

El usuario confirmó el guardado, descarga y reapertura. Se inspeccionó la copia local `estudiantes_prueba_11_10_1811pm.ipynb`, conservando su archivo sin modificaciones: contiene Prueba de guardado, un gráfico PNG, seis salidas de tabla HTML, las justificaciones completas y ninguna salida de error. La copia descargada respalda la conservación de texto y resultados; el guardado en Drive y la reapertura se registran según la confirmación del usuario. La carga manual real del ZIP también fue confirmada por el usuario con la salida de seis documentos y 619 unidades. Después de las instrucciones de reinicio y carga incluida, se recibió nuevamente la comparación correcta. El reinicio no se observó directamente ni se confirmó de forma explícita. El usuario compartió las versiones reales de Colab: Python 3.13.16, pandas 2.2.3 y matplotlib 3.10.0.

## Revisión del afinamiento

El notebook tiene ahora títulos en todas las celdas de código e instrucciones más precisas para escribir, conservar la consulta común y explorar después. Las dos versiones se ejecutaron de nuevo localmente. Falta observar estos títulos e instrucciones en Colab; la evidencia guiada anterior no comprueba automáticamente esta revisión. Las decisiones están en [afinamiento](afinamiento.md).

## Prueba completa en Colab

Usar una copia de prueba del notebook de estudiantes. Esta comprobación docente puede ejecutar el recorrido completo; durante la clase se conserva el orden de predicciones antes de resultados.

1. Abrir el `.ipynb`, guardar una copia en Drive y anotar el nombre real de los controles utilizados.
2. Modificar y ejecutar el saludo, escribir una respuesta de prueba y guardarla.
3. Ejecutar Preparación con carga incluida: comprobar seis documentos y 619 unidades sin etiquetas.
4. Ejecutar frecuencias, tasas y gráfico. Para competencia en Leguía 1921 y Fujimori 1991 deben aparecer 2/4.527 y 11/23.348, aproximadamente 0,442 y 0,471 por 1.000 palabras.
5. Buscar contexto, ampliar la ventana y recuperar evidencia de documentos distintos. La consulta inicial con índices 0 y 3 recupera `u00126` y `u14275`.
6. Contrastar las etiquetas en la celda independiente del final. Confirmar que no se cargaron al iniciar la práctica.
7. Probar recuperación después de perder variables y tras reiniciar el entorno: Preparación primero y Recuperación después. Las respuestas guardadas de texto deben mantenerse en la copia del notebook.
8. Probar la carga manual con `datos_estudiantes.zip` mediante la interfaz real, sin sustituirla por una simulación. Volver al recorrido común después de esa prueba.
9. Guardar y descargar el `.ipynb` con respuestas y salidas; volver a abrir el archivo descargado y comprobar tabla, gráfico y respuesta de prueba.
10. Registrar fecha, versiones del entorno, resultado y diferencias respecto de la prueba local. No marcar verificado si un paso no se completó.

No hacen falta claves, instalaciones de modelos ni GPU. Si aparece un fallo, registrar celda y mensaje, reparar la causa y repetir el tramo afectado; si se modifica código del recorrido común, volver a ejecutar el notebook completo.

## Compilación y proyección

La versión actual ya se compiló localmente con XeLaTeX y Biber y se revisaron las 34 páginas. Como alternativa, importar [beamer_overleaf.zip](../paquetes/beamer_overleaf.zip), seleccionar `1_main.tex`, XeLaTeX y Biber. Revisar el log y las referencias. Comprobar especialmente portada, fragmento B, tabla de aplicaciones y las tres slides bibliográficas, además de las restantes páginas. Revisar que notas ocultas no aparezcan en el PDF distribuido.

Proyectar unas slides con fragmentos, una tabla y el gráfico para comprobar legibilidad desde el aula. Confirmar HDMI y que alternar PDF y notebook no oculta instrucciones relevantes. Si el contenido desborda, recortar o dividir antes de reducir el tamaño del texto. La revisión estática no sustituye estas acciones.

## Acceso a materiales y entrega

El autor realiza los commits y publica el repositorio; la preparación de materiales no incluye publicaciones automáticas. Después de publicar, comprobar el acceso al notebook de estudiantes y al ZIP desde una sesión sin privilegios sobre investigación. Añadir enlaces reales de Colab y descarga solo cuando exista la URL pública.

Crear o identificar la carpeta de Drive para la entrega. Definir una vía que permita subir el trabajo individual y verificar los permisos con una cuenta de estudiante o la persona de apoyo. No exigir compartir públicamente el notebook personal ni asumir que visualizar una carpeta permite subir archivos. Comunicar el enlace de entrega mediante el canal de clase.

Realizar una entrega de prueba de un notebook sin datos personales innecesarios, comprobar recepción y que no se sobrescribe otra entrega. El nombre acordado es `apellido_nombre_analisis_textual.ipynb`. Si hay restricciones de subida, establecer y comunicar una alternativa antes de la sesión.

## Registro para completar después de las pruebas

| Comprobación | Fecha y entorno | Resultado o incidencia |
|---|---|---|
| Recorrido común real en Colab | 11/10/2026, prueba guiada | Salidas esperadas recibidas; recuperación final correcta. Reinicio real sin confirmación explícita |
| Versiones reales de Colab | 11/10/2026, salida del usuario | Python 3.13.16, pandas 2.2.3 y matplotlib 3.10.0 |
| Carga manual mediante interfaz | 11/10/2026, Colab, prueba guiada | ZIP subido y seis documentos con 619 unidades cargados |
| Copia y guardado en Drive | 11/10/2026, prueba guiada | Confirmados por el usuario |
| Descarga y reapertura con salidas | 11/10/2026, prueba guiada y archivo local | Texto, gráfico y tablas conservados en la copia revisada; reapertura confirmada por el usuario |
| Compilación local y referencias | 11/10/2026, XeLaTeX y Biber | PDF de 34 páginas, referencias resueltas y sin avisos de desbordes |
| Revisión visual de todas las slides | 11/10/2026, PDF renderizado | 34 páginas revisadas; proyección en aula pendiente |
| Acceso a materiales públicos | Pendiente | |
| Recepción administrativa de archivo docente | 11/10/2026, conector Drive | Subida y ubicación verificadas; cuenta del docente |
| Entrega desde cuenta institucional distinta | Pendiente | Permisos y subida estudiantil todavía no comprobados |
| Proyector y HDMI | Pendiente | |

La carpeta de recepción continúa privada. Su creación y la subida docente no comprueban los permisos de las cuentas institucionales de la UP. El detalle está en [ensayo del cierre](ensayo_cierre.md).
