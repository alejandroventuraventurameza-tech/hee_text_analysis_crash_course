# Discursos presidenciales bajo la lupa

La presentación corresponde a Historia Económica y Empresarial, semestre 2026 II, y acompaña la sesión de 110 minutos con 33 slides comunes, cuatro de consulta y tres de referencias. Las slides comunes contienen preguntas, extractos literales, conceptos e instrucciones breves; la práctica y las respuestas se realizan en el notebook. El [guion docente](../docs/guion_docente.md) coordina tiempos, slides, preguntas y recuperación.

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
| `revision_visual.json` | Compilación local y revisión visual del PDF actualizado |
| `hee_text_analysis_crash_course.pdf` | PDF actualizado para proyectar |
| `images/*_pagina1.png` | Cuatro facsímiles renderizados de los PDF oficiales, con procedencia registrada |

Importar [hee_text_analysis_crash_course.zip](../paquetes/hee_text_analysis_crash_course.zip) como proyecto en Overleaf y seleccionar `1_main.tex` como archivo principal. Usar **XeLaTeX** y **Biber**. Overleaf normalmente coordina Biber con la compilación; si aparecen citas sin resolver, recompilar desde cero y revisar el log. La secuencia equivalente es XeLaTeX, Biber sobre `1_main`, y dos pasadas de XeLaTeX.

Todos los archivos compilables están en la raíz del ZIP, junto con `images/` y `data/`. Las rutas no dependen de `pd01/`, carpetas externas, Python, una clave o archivos del repositorio de investigación. Los datos de trazabilidad no se descargan durante la compilación.

Las dependencias LaTeX son Beamer, fontspec, babel con español, amsmath, amssymb, graphicx, geometry, multicol, TikZ y etoolbox, biblatex con estilo APA y su idioma español, csquotes, pgfplots y appendixnumberbeamer. Se utilizan paquetes de la distribución TeX, sin archivos de estilo privados. El gráfico de reserva usa pgfplots con compatibilidad 1.18 y coordenadas reales de la tabla incluida. Las fuentes son las predeterminadas de TeX con soporte de XeLaTeX, sin archivos tipográficos externos.

## Adaptación del template

Se conserva el formato 4:3, la composición de portada negra y blanca, el logo sin alterar proporciones, la paleta original, los encabezados de sección y el pie en tres franjas. El texto base aumenta de 9 a 11 puntos para proyección. El cuerpo pasa del gris original a negro para mayor contraste. La portada incluye el título Discursos presidenciales bajo la lupa, el subtítulo Análisis textual con Python, Historia Económica y Empresarial, 2026 II y el correo al.venturam@up.edu.pe debajo del nombre. No muestra duración ni invitación. Los títulos usan el tono magenta más oscuro de la misma paleta para aumentar el contraste.

El contenido, portada y entornos se adaptan al español. Se eliminan los comandos de calavera y carita y sus fuentes especiales, que no se utilizan en la clase. Se mantienen las definiciones de colores y bloques del template. Las referencias de macroeconomía se sustituyen por las del análisis textual y las herramientas utilizadas. El template original permanece intacto.

Las notas `\note{...}` permanecen ocultas en la configuración común. Contienen procedencia y recordatorios pedagógicos. El guion permite consultarlos sin producir una versión del PDF con notas. Si se activa la visualización de notas en Overleaf, revisar la paginación y evitar distribuir esa versión como ejercicio inicial.

## Orden pedagógico

Las slides S03 y S04 presentan fragmentos A y B sin presidente ni etiqueta. El guion indica revelar su procedencia después de la clasificación manual. S17 muestra resultados numéricos solo después de la predicción y ejecución. S21 interpreta pasajes solo después de que los estudiantes busquen en contexto. S23 revela etiquetas existentes al final.

Los extractos proyectados son literales y breves, no unidades completas. El notebook mantiene el texto completo y permite ampliar a la página original. Las referencias de los pasajes y URL de los PDF están en `data/procedencia.json`; su selección es dirigida para enseñar, no para calcular proporciones. Las slides no presentan resultados del corpus completo como resultados de estos seis mensajes.

Los cuatro apéndices y tres slides bibliográficas son recursos de consulta y no añaden tiempo a los 110 minutos. El gráfico de reserva conserva el eje desde cero y los valores sin redondeo usados por el notebook; la tabla proyectada redondea a tres decimales. La cercanía de tasas no prueba equivalencia ni significación estadística.

La referencia de Berelson de 1952 se corroboró bibliográficamente con una reseña contemporánea; no se presupone lectura íntegra del libro. General Inquirer y el estudio de Gilardi y coautores sirven como ejemplos de métodos computacionales. El estudio de Grimmer y Stewart sustenta la lectura posterior sobre oportunidades y límites. Las referencias no sustituyen la validación del proyecto. La progresión de ejercicios adapta conceptualmente los materiales locales en R, con una implementación propia en Python.

## Revisión y límites

Se revisan estáticamente rutas de entrada, imagen y bibliografía; etiquetas; claves de citas; balance de llaves y entornos; cierres de filas de tablas; correspondencia de citas con las unidades; números con el CSV; identidad del logo y conservación del template. El ZIP se comprueba contra los archivos locales y se incluye un listado de huellas propio.

La nueva apertura añade seis slides sobre problemática, proxy, orientación declarada, canales, API y objetivos. El cuerpo usa Latin Modern Sans con tamaño uniforme y el encabezado muestra las cuatro secciones. [GUIA_EDICION.md](GUIA_EDICION.md) explica los controles de portada y la imagen pendiente del presidente.

La versión actual se compiló localmente con XeLaTeX y Biber el 11 de octubre de 2026. Se revisaron las 40 páginas renderizadas y el registro final de compilación, sin avisos de desbordes ni citas sin resolver. El detalle y las huellas están en [revision_visual.json](revision_visual.json). Los PDF anteriores fueron retirados por el docente antes de esta revisión; el archivo actual es `hee_text_analysis_crash_course.pdf`.

La revisión de proyección y legibilidad desde el aula sigue pendiente. Overleaf es opcional; no se ha verificado esta versión dentro de esa plataforma.

## Compilación local

Desde la carpeta `slides`, con MiKTeX o TeX Live disponibles:

```powershell
xelatex '-interaction=nonstopmode' '-halt-on-error' 1_main.tex
biber 1_main
xelatex '-interaction=nonstopmode' '-halt-on-error' 1_main.tex
xelatex '-interaction=nonstopmode' '-halt-on-error' 1_main.tex
```

El resultado es `1_main.pdf`. No sobrescribe el PDF revisado ni el PDF original que aportó el docente. El ZIP contiene las fuentes y los facsímiles, y también permite compilar sin acceso al repositorio de investigación.

## Regeneración de recursos

Desde la raíz del repositorio de clase, `python scripts/preparar_beamer.py` adapta una copia del preámbulo y copia el logo desde el template, además de actualizar CSV, facsímiles y procedencia. La renderización de las primeras páginas usa PyMuPDF (`fitz`), ya disponible en el entorno docente. No modifica investigación ni el template y no compila LaTeX. No regenera el contenido de las slides ni el guion.

`python scripts/revisar_beamer.py` comprueba la estructura local y genera el ZIP después de pasar las comprobaciones. Si se modifican los `.tex` o la bibliografía, ejecutar esta revisión antes de reemplazar el paquete para Overleaf.
