# Slides Beamer para el curso de análisis textual

La presentación acompaña la sesión de 110 minutos con 27 slides comunes, cuatro de consulta y tres de referencias. Las slides comunes contienen preguntas, extractos literales, conceptos e instrucciones breves; la práctica y las respuestas se realizan en el notebook. El [guion docente](../docs/guion_docente.md) coordina tiempos, slides, preguntas y recuperación.

## Archivos y configuración de Overleaf

| Archivo o carpeta | Función |
|---|---|
| `1_main.tex` | Archivo principal de compilación |
| `2_preamble.tex` | Idioma, fuentes, tema, portada, bibliografía y estilos |
| `3_content.tex` | Slides, etiquetas internas y notas docentes ocultas |
| `4_bibliography.bib` | Siete referencias y documentación de herramientas |
| `images/UP_logo.jpg` | Logo original, copiado sin modificar |
| `data/comparacion_competencia.csv` | Dos registros que sustentan la tabla y el gráfico de la consulta inicial |
| `data/procedencia.json` | Unidades completas citadas, URL de los PDF y huellas del template original |
| `revision_estatica.json` | Comprobaciones de estructura y recursos, sin compilación |

Importar [beamer_overleaf.zip](../paquetes/beamer_overleaf.zip) como proyecto en Overleaf y seleccionar `1_main.tex` como archivo principal. Usar **XeLaTeX** y **Biber**. Overleaf normalmente coordina Biber con la compilación; si aparecen citas sin resolver, recompilar desde cero y revisar el log. La secuencia equivalente es XeLaTeX, Biber sobre `1_main`, y dos pasadas de XeLaTeX.

Todos los archivos compilables están en la raíz del ZIP, junto con `images/` y `data/`. Las rutas no dependen de `pd01/`, carpetas externas, Python, una clave o archivos del repositorio de investigación. Los datos de trazabilidad no se descargan durante la compilación.

Las dependencias LaTeX son Beamer, fontspec, babel con español, amsmath, amssymb, graphicx, geometry, multicol, TikZ y etoolbox, biblatex con estilo APA y su idioma español, csquotes, pgfplots y appendixnumberbeamer. Se utilizan paquetes de la distribución TeX, sin archivos de estilo privados. El gráfico de reserva usa pgfplots con compatibilidad 1.18 y coordenadas reales de la tabla incluida. Las fuentes son las predeterminadas de TeX con soporte de XeLaTeX, sin archivos tipográficos externos.

## Adaptación del template

Se conserva el formato 4:3, la composición de portada negra y blanca, el logo sin alterar proporciones, la paleta original, los encabezados de sección y el pie en tres franjas. El texto base aumenta de 9 a 11 puntos para proyección. El cuerpo pasa del gris original a negro para mayor contraste. Se ajustan las posiciones de portada para el título del curso, fecha e invitación y se usan nombres cortos en el pie.

El contenido, portada y entornos se adaptan al español. Se eliminan los comandos de calavera y carita y sus fuentes especiales, que no se utilizan en la clase. Se mantienen las definiciones de colores y bloques del template. Las referencias de macroeconomía se sustituyen por las del análisis textual y las herramientas utilizadas. El template original permanece intacto.

Las notas `\note{...}` permanecen ocultas en la configuración común. Contienen procedencia y recordatorios pedagógicos. El guion permite consultarlos sin producir una versión del PDF con notas. Si se activa la visualización de notas en Overleaf, revisar la paginación y evitar distribuir esa versión como ejercicio inicial.

## Orden pedagógico

Las slides S03 y S04 presentan fragmentos A y B sin presidente ni etiqueta. El guion indica revelar su procedencia después de la clasificación manual. S17 muestra resultados numéricos solo después de la predicción y ejecución. S21 interpreta pasajes solo después de que los estudiantes busquen en contexto. S23 revela etiquetas existentes al final.

Los extractos proyectados son literales y breves, no unidades completas. El notebook mantiene el texto completo y permite ampliar a la página original. Las referencias de los pasajes y URL de los PDF están en `data/procedencia.json`; su selección es dirigida para enseñar, no para calcular proporciones. Las slides no presentan resultados del corpus completo como resultados de estos seis mensajes.

Los cuatro apéndices y tres slides bibliográficas son recursos de consulta y no añaden tiempo a los 110 minutos. El gráfico de reserva conserva el eje desde cero y los valores sin redondeo usados por el notebook; la tabla proyectada redondea a tres decimales. La cercanía de tasas no prueba equivalencia ni significación estadística.

La referencia de Berelson de 1952 se corroboró bibliográficamente con una reseña contemporánea; no se presupone lectura íntegra del libro. General Inquirer y el estudio de Gilardi y coautores sirven como ejemplos de métodos computacionales. El estudio de Grimmer y Stewart sustenta la lectura posterior sobre oportunidades y límites. Las referencias no sustituyen la validación del proyecto. La progresión de ejercicios adapta conceptualmente los materiales locales en R, con una implementación propia en Python.

## Revisión y límites

Se revisan estáticamente rutas de entrada, imagen y bibliografía; etiquetas; claves de citas; balance de llaves y entornos; cierres de filas de tablas; correspondencia de citas con las unidades; números con el CSV; identidad del logo y conservación del template. El ZIP se comprueba contra los archivos locales y se incluye un listado de huellas propio.

**No se compiló localmente ni se verificó la compilación en Overleaf.** La revisión estática no prueba ajuste visual, ausencia de desbordes, disponibilidad de todas las versiones de paquetes ni referencias resueltas. Después de compilar, revisar especialmente la portada, el fragmento B, la tabla de aplicaciones y las tres slides bibliográficas. Si falta espacio, recortar o dividir contenido antes de reducir el texto.

La presentación no incluye un PDF. El docente lo compilará en Overleaf y lo utilizará junto con el notebook y el guion.

## Regeneración de recursos

Desde la raíz del repositorio de clase, `python scripts/preparar_beamer.py` adapta una copia del preámbulo y copia el logo desde el template, además de actualizar CSV y procedencia. No modifica investigación ni el template y no compila LaTeX. No regenera el contenido de las slides ni el guion.

`python scripts/revisar_beamer.py` comprueba la estructura local y genera el ZIP después de pasar las comprobaciones. Si se modifican los `.tex` o la bibliografía, ejecutar esta revisión antes de reemplazar el paquete para Overleaf.
