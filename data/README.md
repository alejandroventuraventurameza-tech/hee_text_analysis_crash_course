# Datos didácticos de mensajes presidenciales

Este conjunto contiene seis mensajes completos del 28 de julio y 619 unidades de texto procedentes de la investigación congelada en `v1.0-ccl`. Permite explorar palabras, comparar menciones por 1.000 palabras y revisar instrumentos económicos en contexto. Los resultados describen estos documentos; no son estimaciones de gobiernos completos ni del corpus de investigación.

## Selección y comparabilidad

La regla de selección se estableció antes de calcular resultados: tomar, para Leguía, Velasco y Alberto Fujimori, los dos primeros mensajes anuales del 28 de julio disponibles después del inicio del gobierno. Se excluyen mensajes de investidura, manifiestos, decretos, renuncias, duplicados y otras voces. Se conservan los documentos completos, sin seleccionar solo las secciones económicas.

| Documento | Fecha | Audiencia declarada | Páginas del PDF | Palabras para conteos | Unidades existentes |
|---|---|---|---:|---:|---:|
| `leguia_1920` | 28/07/1920 | Congreso | 14 | 5.807 | 55 |
| `leguia_1921` | 28/07/1921 | Congreso Nacional | 13 | 4.527 | 42 |
| `velasco_1969` | 28/07/1969 | Nación | 18 | 8.539 | 82 |
| `velasco_1970` | 28/07/1970 | Nación | 21 | 10.068 | 92 |
| `alberto_fujimori_1991` | 28/07/1991 | Congreso Nacional y pueblo del Perú | 50 | 23.348 | 216 |
| `alberto_fujimori_1992` | 28/07/1992 | Nación | 32 | 13.426 | 132 |
| Total | | | 148 | 65.715 | 619 |

La selección se mantiene para la clase después de revisar las cabeceras, el inicio, el cierre y la extracción. Su comparabilidad es parcial: comparten fecha conmemorativa, voz presidencial y carácter de balance posterior al inicio del gobierno, pero difieren en audiencia, situación institucional y extensión. Velasco no presenta un balance parlamentario; la nota editorial de 1969 sitúa su mensaje en el Salón Dorado de Palacio de Gobierno. Fujimori de 1992 cambia de audiencia respecto de 1991. Leguía de 1921 conmemora además el centenario; Velasco de 1970 trata la reconstrucción tras el sismo.

Estas diferencias quedan visibles en los metadatos. Normalizar por longitud resuelve una diferencia de exposición léxica, no esas diferencias históricas. El ejercicio común compara documentos por separado. Si se agrupan los dos documentos de un gobierno, el resultado solo resume ese par.

## Qué cargar y cuándo

| Archivo o carpeta | Contenido y uso |
|---|---|
| [documentos.json](documentos.json) | Seis registros con metadatos, `texto_original` y `texto_conteo`; entrada principal del futuro notebook |
| [metadatos.csv](metadatos.csv) | Una fila por documento, sin textos largos; permite inspeccionar selección y procedencia |
| [unidades.csv](unidades.csv) | 619 segmentos existentes, sin etiquetas, con documento, orden y localización |
| [paginas.csv](paginas.csv) | Una fila por página del PDF, con extracción y posiciones dentro del texto original |
| [ejemplos_manuales.csv](ejemplos_manuales.csv) | Dos casos comunes y cuatro de reserva, inicialmente sin presidente, procedencia ni etiquetas |
| `originales/` | Seis PDF públicos copiados byte por byte desde el commit congelado |
| `textos_originales/` | Extracción completa por documento para lectura y búsqueda |
| `textos_conteo/` | Versión independiente para frecuencias |
| `docente/` | Etiquetas existentes, referencias de ejemplos y guía de discusión; cargar después del ejercicio manual |
| [resultados_guardados/comparacion_palabras.csv](resultados_guardados/comparacion_palabras.csv) | Treinta resultados de recuperación: cinco palabras exactas en seis documentos |
| [seleccion.json](seleccion.json) | Regla operativa por documento: identificadores, fuentes, saludo inicial y nota editorial excluida del conteo |
| `trazabilidad/` | Huellas de entradas, revisión de extracción, comprobación de fuentes y descartes editoriales |
| [diccionario de columnas](diccionario_columnas.md) | Significado de campos, filas, tipos y medidas |

Para la primera actividad manual se muestran únicamente los ejemplos A y B de `ejemplos_manuales.csv`. Después de registrar hipótesis y evidencia se revela la procedencia. La tabla de documentos puede cargarse entonces; las clasificaciones se incorporan al final. Los ejemplos C a F son alternativas de discusión, no tareas adicionales obligatorias. Estos ejemplos se eligieron deliberadamente para enseñar instrumentos, polisemia y ambigüedad; no son una muestra para estimar proporciones de roles.

La separación de archivos organiza el momento pedagógico de acceso. Al ser un repositorio público, no constituye una barrera de seguridad ni impide consultar por anticipado los archivos del docente. El notebook no los cargará en el primer ejercicio.

## Texto conservado y procesamiento

El PDF es el original documental de referencia. `texto_original` reproduce la extracción de todas sus páginas con PyMuPDF, en orden, unidas por un salto de línea. Conserva cabecera, subtítulos, numeración, nota editorial, puntuación y negaciones. No equivale a una transcripción corregida ni reconstruye el formato visual. Los saltos de línea y algunos errores tipográficos de la fuente se mantienen. Para comprobar una cita se puede abrir el PDF o recuperar su página.

La versión para conteos aplica únicamente estas decisiones:

1. Excluir el rótulo y subtítulo iniciales anteriores al saludo del orador. Conservar el saludo y los encabezados internos del discurso.
2. Excluir la línea que contiene solo el número de su página.
3. Excluir del conteo la nota editorial de la primera página de Velasco de 1969: la nota informa dónde se pronunció el mensaje, no forma parte del discurso. Permanece en el original.
4. Reparar cortes escritos como guion seguido inmediatamente por salto de línea, uniéndolos. Esta regla simple puede unir casos que no sean cortes de palabra; no realiza corrección lingüística automática.
5. Convertir a minúsculas y extraer secuencias de letras españolas mediante `[a-záéíóúüñ]+`. Los números y signos no cuentan como palabras; una palabra con guion se separa si el guion no es un corte de línea. Nombres con letras ajenas a este conjunto pueden quedar separados.
6. Unir las palabras con espacios para formar `texto_conteo`. Conservar tildes, `ñ` y negaciones. No reducir a raíces, no agrupar singular y plural y no eliminar palabras frecuentes.

Los descartes específicos están registrados en [descartes_conteo.json](trazabilidad/descartes_conteo.json). El denominador `n_palabras_conteo` es el número de palabras de esa versión. Si el notebook oculta palabras del ranking, no cambiará ese total. Una consulta de palabra exacta distingue `empresa` de `empresas` e `inversion` de `inversión`.

`n_palabras_manifest` es un conteo heredado de la investigación con otra regla y contenido editorial. `n_palabras_unidad_fuente` es el conteo heredado de cada segmento, calculado separando por espacios. Ninguno sustituye a `n_palabras_conteo`.

## Unidades y etiquetas

Cada unidad conserva exactamente el texto, identificador y orden de `unidades.csv` en el commit de investigación. No se resegmentaron ni reclasificaron textos. El segmentador original reconstruyó bloques, descartó números y encabezados cortos en mayúsculas y agrupó oraciones con un objetivo aproximado de 90 palabras. Por ello puede reunir temas diferentes, incorporar una nota editorial o cortar el contexto visual del PDF. No debe llamarse párrafo original ni suponerse que todas las unidades tienen la misma longitud. No se afirma que exista un máximo de 220 palabras efectivamente aplicado.

Para localizar las unidades en la extracción completa se reprodujeron los descartes de encabezados del segmentador y se ignoraron espacios al buscar. Las posiciones se devuelven al texto original. `pagina_inicio` y `pagina_fin` usan numeración de PDF desde 1. Las posiciones de caracteres usan índices desde 0 y fin exclusivo. El intervalo del original puede contener encabezados, saltos y números omitidos en el texto de la unidad; la localización no implica identidad literal del intervalo sin esos ajustes.

Las 619 clasificaciones existentes están separadas en `docente/clasificaciones_existentes.csv`. Son salidas de un modelo de lenguaje, no etiquetas humanas independientes ni respuestas indiscutibles. Incluyen cinco categorías: empresario, regulador, facilitador, asistencial y no aplica. Las etiquetas secundarias pueden estar vacías. La confianza es una valoración categórica del modelo, no una probabilidad calibrada.

La validación de la investigación tuvo como segundo anotador otro modelo de lenguaje y el conjunto de referencia de 30 unidades contiene un solo caso empresario y uno regulador. La clase utiliza esos resultados para discutir razonamientos y límites, sin presentar acuerdo entre dos humanos ni exactitud garantizada para cada clase.

## Filas y denominadores

| Medida | Qué representa el numerador | Denominador |
|---|---|---|
| Frecuencia absoluta de una palabra | Apariciones de la forma exacta | No tiene denominador |
| Menciones por 1.000 palabras de un documento | Apariciones × 1.000 | `n_palabras_conteo` del mismo documento |
| Tasa conjunta de varios documentos | Suma de apariciones × 1.000 | Suma de palabras de los documentos incluidos |
| Incidencia productiva si se explora posteriormente | Unidades empresario, regulador o facilitador | Todas las unidades oficiales seleccionadas |
| Mezcla productiva si se explora posteriormente | Unidades de un rol productivo | Solo unidades empresario, regulador o facilitador seleccionadas |

No se calcula una mezcla con los seis ejemplos dirigidos. Las etiquetas secundarias no añaden una segunda unidad al conteo. El conjunto didáctico de 619 unidades no comparte denominador con las 22.365 unidades oficiales o las 6.899 productivas del corpus completo. La entrega común necesita frecuencias y contexto, no una nueva estimación de roles.

## Procedencia y comprobaciones

Fuente pública: [archivo de mensajes presidenciales del Museo del Congreso](https://www3.congreso.gob.pe/participacion/museo/congreso/mensajes-presidenciales/). Cada documento incluye enlace a su página y al PDF específico. Los enlaces se comprobaron el 10 de octubre de 2026: las seis descargas respondieron y sus huellas SHA-256 coincidieron con las copias congeladas. Esa comprobación no garantiza disponibilidad futura.

Origen de las copias: tag `v1.0-ccl`, commit `72fcac7d3ea06b737c3a3f35f37b818411c6dead`. Se extrajeron desde ese commit, no desde resultados regenerados ni archivos intermedios sin versionar. Los archivos fuente fueron `manifest.csv`, `unidades.csv`, `clasificacion_llm.csv`, el inventario SHA-256 y los seis PDF. Sus rutas relativas y huellas completas están en [entradas.json](trazabilidad/entradas.json).

La revisión incluyó: identidad de los seis PDF; cabeceras e inicio; continuidad de extracción por página y cierres; ausencia de páginas sin texto o caracteres de reemplazo; localización de las 619 unidades; y revisión visual de las primeras páginas, últimas páginas y páginas de los seis ejemplos. No fue una corrección manual palabra por palabra de las 148 páginas. Los errores de edición o extracción que subsistan deben comprobarse en el PDF.

El script [preparar_datos.py](../scripts/preparar_datos.py) registra las versiones del entorno de preparación y verifica integridad, relaciones y conteos. Solo lee la investigación y escribe en el repositorio de la clase. Su dependencia de PyMuPDF es para preparación docente; los estudiantes no necesitan instalarla ni ejecutar ese script.

Los [resultados guardados](resultados_guardados/comparacion_palabras.csv) se calcularon localmente con esta regla sobre `estado`, `empresa`, `empresas`, `inversión` y `competencia`. Son salidas de recuperación que se consultan después de la predicción. No incluyen interpretación de roles ni demuestran ejecución en Colab. El notebook y su prueba en Colab son el siguiente entregable.

## Carga manual y redistribución

El paquete [datos_estudiantes.zip](../paquetes/datos_estudiantes.zip) incluye documentos, unidades sin etiquetas, páginas, ejemplos y originales, junto con documentación y resultados de recuperación. Excluye la carpeta `docente/`. Se descargará y cargará manualmente en Colab si falla el acceso a los archivos públicos; el notebook preparará la extracción del ZIP y lectura de datos. El ZIP por sí solo no ejecuta el análisis.

Se atribuyen los documentos al archivo oficial del Congreso y las unidades y clasificaciones al proyecto de investigación. No se declara una licencia abierta para toda la colección por el mero hecho de estar en un repositorio público. No se incluyen documentos personales, claves ni libros o artículos de la bibliografía local. Las rutas personales del proyecto no se trasladan a los datos de clase.
