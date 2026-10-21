# Personalizar la presentación

El archivo principal es `1_main.tex`. El ZIP se mantiene como `hee_text_analysis_crash_course.zip`.

## Fuente y tamaños

Edita `configuracion.tex`, no el template original. `FuenteTexto` define la misma familia para texto, títulos y citas. La versión preparada usa Latin Modern Sans, cercana a la de «Lo declarado en un discurso». La negrita enfatiza y el tamaño de títulos conserva su jerarquía; las preguntas del cuerpo ya no usan un tamaño mayor. Los iconos y símbolos matemáticos son recursos gráficos, no cambios de familia en el texto.

Para cambiar la fuente, sustituye `Latin Modern Sans` en `FuenteTexto` por el nombre de una fuente instalada en el entorno donde compilas. XeLaTeX debe poder encontrarla; una fuente disponible en tu laptop puede no estar en Overleaf.

| Control | Qué modifica |
|---|---|
| `TamTituloPortada` | Tamaño del título principal; 22 puntos |
| `InterlineadoTituloPortada` | Distancia entre las dos líneas del título; 25 puntos |
| `TamNombrePortada` | Tamaño del expositor; 14 puntos |
| `TamSubtituloPortada` | Análisis textual con Python; 12 puntos |
| `TamCursoPortada` | Nombre del curso; 11 puntos |
| `TamSemestrePortada` | Semestre; 10 puntos |
| `NotaExpositor` | Texto de la nota marcada con asterisco junto al nombre |

Por ejemplo, para aumentar el título cambia `\newcommand{\TamTituloPortada}{22}` a `\newcommand{\TamTituloPortada}{24}` y ajusta su interlineado a 27. Recompila y revisa que el subtítulo no se solape. Las posiciones verticales de portada están en `2_preamble.tex`, dentro de `title page`, en los valores `yshift`. Cambiar tamaños no mueve automáticamente esos elementos.

`1_main.tex` fija el tamaño base del cuerpo en `\documentclass[11pt,handout]{beamer}`. Mantener 11 puntos conserva el ajuste revisado. El código usa una fuente de ancho fijo para mostrar su sintaxis; el texto explicativo usa la familia común.

## Nota del expositor

El asterisco se muestra junto al nombre y al pie de la portada:

> Todo lo dicho en esta sesión es responsabilidad del expositor.

El correo continúa debajo del nombre. La nota se configura en `NotaExpositor`.

## Imagen del presidente

Coloca tu imagen como `slides/images/presidente.png`, o `images/presidente.png` dentro del proyecto descomprimido. La slide detecta el archivo automáticamente; si todavía no existe, muestra un espacio identificado. Mantiene las proporciones de la imagen.

Para una imagen JPEG, cambia las dos referencias `presidente.png` de `apertura.tex` a su nombre real. Un PDF convencional no reproduce animaciones GIF: exporta un fotograma a PNG para la presentación PDF, o muestra la animación aparte durante la exposición.

Los canales usan iconos de Font Awesome y un rótulo X. Puedes sustituirlos por imágenes mediante `includegraphics`, conservando el ancho de cada columna. No representan acontecimientos concretos.

## Contenido y regeneración

`apertura.tex` contiene la problemática, la proxy, orientación declarada, canales, API y objetivos. `3_content.tex` contiene el resto del recorrido; sus etiquetas permiten localizar cada slide.

El esquema de API es editable en TikZ y es conceptual: no hace solicitudes a una plataforma ni requiere claves.

El encabezado tiene rótulos visibles con el mismo color. La versión anterior permitía que algunos enlaces heredaran negro sobre negro; ahora el texto de las cuatro secciones se dibuja directamente.

`scripts/preparar_beamer.py` regenera `2_preamble.tex`; tus preferencias persistentes de tipografía deben quedar en `configuracion.tex`. Si modificas posiciones de portada en el preámbulo y luego ejecutas ese script, traslada el cambio también a su bloque `COVER`. `scripts/revisar_beamer.py` comprueba las fuentes y vuelve a generar el ZIP con el nombre acordado.
