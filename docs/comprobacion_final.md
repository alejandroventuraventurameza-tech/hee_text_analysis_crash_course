# Comprobación final de la sesión

Los materiales están preparados para revisar el recorrido de principio a fin antes de la clase del 12 de octubre de 2026. Este registro separa evidencia ya obtenida de tareas pendientes; una instrucción escrita no equivale a una comprobación realizada.

## Estado al 11 de octubre de 2026

| Componente | Estado y evidencia |
|---|---|
| Plan y ejercicio individual | Preparados; agenda consecutiva de 110 minutos y criterios formativos |
| Datos | Seis PDF trazables, 148 páginas y 619 unidades; integridad y procedencia comprobadas |
| Notebooks | Ambas versiones ejecutadas completas localmente; [registro](../notebooks/prueba_local.json) |
| Carga manual | Lectura del ZIP real probada localmente; recepción de bytes de la subida simulada |
| Colab | Prueba guiada parcial: carga, metadatos, frecuencias modificadas, tasas, gráfico, contextos y evidencia recibidos. Etiquetas, reinicio real, carga manual, copia y guardado pendientes |
| Beamer | Revisión estática aprobada; [registro](../slides/revision_estatica.json) |
| Overleaf | Compilación y revisión visual pendientes, a cargo del docente |
| Acceso público | Repositorio local sin remoto configurado; publicación a cargo del autor |
| Entrega en Drive | Carpeta y enlace por definir y comprobar |

Las versiones de la prueba local fueron Python 3.13.14, pandas 3.0.2 y matplotlib 3.10.9, sobre Windows. No se presupone que Colab tenga esas versiones ni que su formulario y descarga se comporten exactamente igual.

El 11 de octubre se abrió Colab en el navegador integrado y se observó el enlace Iniciar sesión. No se ejecutó el notebook en esa sesión. El usuario continuó una prueba guiada propuesta para Brave y compartió salidas de Colab: carga incluida, seis filas, original y conteo, ranking cambiado de 10 a 8 con denominador intacto, tasas y gráfico, tabla tras recuperación, 13 coincidencias y dos unidades completas con páginas y enlaces. El [registro guiado](../notebooks/prueba_colab_guiada.json) conserva el alcance de esa evidencia. No equivale a una comprobación completa ni a control directo del navegador.

Las ventanas ampliadas aparecían recortadas por un límite visual de 250 caracteres. Se retiró ese límite en las dos versiones del notebook; los textos originales y los conteos no cambian. La celda corregida debe ejecutarse también en la copia de Colab del usuario. Aún faltan etiquetas, carga manual real, reinicio del entorno, guardado, descarga y reapertura.

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

## Revisión en Overleaf y proyección

Importar [beamer_overleaf.zip](../paquetes/beamer_overleaf.zip), seleccionar `1_main.tex`, XeLaTeX y Biber. Revisar el log y las referencias. Comprobar especialmente portada, fragmento B, tabla de aplicaciones y las tres slides bibliográficas, además de las restantes páginas. Revisar que notas ocultas no aparezcan en el PDF distribuido.

Proyectar unas slides con fragmentos, una tabla y el gráfico para comprobar legibilidad desde el aula. Confirmar HDMI y que alternar PDF y notebook no oculta instrucciones relevantes. Si el contenido desborda, recortar o dividir antes de reducir el tamaño del texto. La revisión estática no sustituye estas acciones.

## Acceso a materiales y entrega

El autor realiza los commits y publica el repositorio; la preparación de materiales no incluye publicaciones automáticas. Después de publicar, comprobar el acceso al notebook de estudiantes y al ZIP desde una sesión sin privilegios sobre investigación. Añadir enlaces reales de Colab y descarga solo cuando exista la URL pública.

Crear o identificar la carpeta de Drive para la entrega. Definir una vía que permita subir el trabajo individual y verificar los permisos con una cuenta de estudiante o la persona de apoyo. No exigir compartir públicamente el notebook personal ni asumir que visualizar una carpeta permite subir archivos. Comunicar el enlace de entrega mediante el canal de clase.

Realizar una entrega de prueba de un notebook sin datos personales innecesarios, comprobar recepción y que no se sobrescribe otra entrega. El nombre acordado es `apellido_nombre_analisis_textual.ipynb`. Si hay restricciones de subida, establecer y comunicar una alternativa antes de la sesión.

## Registro para completar después de las pruebas

| Comprobación | Fecha y entorno | Resultado o incidencia |
|---|---|---|
| Ejecución completa real en Colab | Pendiente | |
| Carga manual mediante interfaz | Pendiente | |
| Copia y guardado en Drive | Pendiente | |
| Descarga y reapertura con salidas | Pendiente | |
| Compilación de Overleaf y referencias | Pendiente | |
| Revisión visual de todas las slides | Pendiente | |
| Acceso a materiales públicos | Pendiente | |
| Recepción de entrega de prueba | Pendiente | |
| Proyector y HDMI | Pendiente | |
