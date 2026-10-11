# Diccionario de columnas de los datos didácticos

Los archivos de texto usan UTF-8 y saltos de línea LF, fijados para `data/` en `.gitattributes` para conservar las huellas al descargar mediante Git en distintos sistemas. Los PDF y ZIP se conservan como archivos binarios. Las fechas usan `AAAA-MM-DD`. Los campos numéricos se cargan como números al analizar; en un CSV son representaciones de texto. Las rutas de `metadatos.csv` son relativas a `data/`. Los valores vacíos de etiquetas secundarias indican que el modelo no asignó una segunda etiqueta, no que falte una fila.

## Documentos y metadatos

`documentos.json` contiene una lista de seis objetos; cada objeto es un documento completo. `metadatos.csv` contiene los mismos campos excepto los dos textos largos.

| Campo | Tipo | Significado |
|---|---|---|
| `documento_id` | Texto | Identificador didáctico único, por ejemplo `leguia_1920`; no reemplaza un identificador de unidad |
| `archivo` | Texto | Nombre del PDF en investigación y en `originales/` |
| `gobierno` | Texto | Denominación heredada del inventario de investigación |
| `orador` | Texto | Nombre legible del presidente |
| `fecha` | Fecha | Fecha del mensaje |
| `anio` | Entero | Año del mensaje |
| `tipo` | Texto | Tipo documental heredado, `mensaje` en esta selección |
| `audiencia_declarada` | Texto | Destinatarios expresados en la cabecera o inicio; no identifica todos los receptores efectivos |
| `ocasion` | Texto | Criterio común de selección del mensaje anual |
| `observacion_comparabilidad` | Texto | Diferencia institucional o de ocasión relevante para interpretar |
| `emisor` | Texto | Tipo de voz del inventario, `oficial` en los seis casos |
| `duplicado` | Booleano | Marca documental heredada, falso en los seis casos |
| `n_paginas_pdf` | Entero | Número de páginas del PDF copiado |
| `n_palabras_manifest` | Entero | Conteo heredado del inventario; no es el denominador de la clase |
| `n_palabras_conteo` | Entero | Total de secuencias de letras tras el procesamiento didáctico; denominador de la tasa léxica |
| `n_unidades` | Entero | Número de unidades existentes correspondientes al documento |
| `url_pagina` | URL | Página oficial que enlaza el mensaje |
| `url_pdf` | URL | Enlace específico al PDF oficial |
| `ruta_pdf` | Ruta | Copia local íntegra del PDF |
| `ruta_texto_original` | Ruta | Extracción completa del PDF sin limpieza para frecuencias |
| `ruta_texto_conteo` | Ruta | Versión separada para contar palabras |
| `sha256_pdf` | Texto hexadecimal | Huella completa de la copia PDF |
| `sha256_texto_original` | Texto hexadecimal | Huella de los bytes UTF-8 del texto original extraído |
| `sha256_texto_conteo` | Texto hexadecimal | Huella del TXT procesado, incluido el salto de línea final del archivo |
| `commit_fuente` | Texto hexadecimal | Commit fijo de investigación utilizado para la copia |
| `texto_original` | Texto | Solo JSON: todas las páginas extraídas, con contenido editorial, signos y saltos |
| `texto_conteo` | Texto | Solo JSON: palabras en minúsculas separadas por espacios, sin salto final |

El salto final del TXT procesado no crea una palabra adicional. No se deben comparar huellas del texto del JSON y del TXT sin atender esa diferencia explícita.

## Unidades

`unidades.csv` tiene 619 filas, una por unidad existente, y no contiene etiquetas.

| Campo | Tipo | Significado |
|---|---|---|
| `unidad_id` | Texto | Identificador estable del segmento en investigación |
| `documento_id` | Texto | Vínculo con la tabla de documentos |
| `archivo` | Texto | PDF al que pertenece el segmento |
| `gobierno` | Texto | Gobierno heredado de la unidad |
| `fecha` | Fecha | Fecha del documento vinculado |
| `emisor` | Texto | Voz de la unidad, oficial |
| `tipo` | Texto | Tipo documental, mensaje |
| `duplicado` | Booleano | Falso; las copias duplicadas están excluidas |
| `orden` | Entero | Posición de la unidad dentro del documento, desde 0 |
| `n_palabras_unidad_fuente` | Entero | Conteo original del segmento por separación de espacios |
| `pagina_inicio` | Entero | Primera página del PDF que contiene la unidad, desde 1 |
| `pagina_fin` | Entero | Última página del PDF que contiene la unidad, desde 1 |
| `char_inicio_original` | Entero | Posición inicial en `texto_original`, desde 0 |
| `char_fin_original` | Entero | Posición final exclusiva en `texto_original` |
| `texto` | Texto | Segmento copiado exactamente del archivo congelado de unidades |

No se supone que una unidad sea un párrafo tipográfico ni que contenga un solo tema. Los límites de caracteres son una localización del segmento en la extracción completa; pueden incluir contenido editorial que el segmentador omitió.

## Páginas

`paginas.csv` tiene 148 filas, una por página de PDF.

| Campo | Tipo | Significado |
|---|---|---|
| `documento_id` | Texto | Vínculo con el documento |
| `pagina_pdf` | Entero | Página desde 1; corresponde al visor del PDF |
| `char_inicio_original` | Entero | Inicio de la página dentro del texto original concatenado |
| `char_fin_original` | Entero | Fin exclusivo de la página antes del separador añadido |
| `texto` | Texto | Extracción completa de esa página |

## Ejemplos manuales y referencias

`ejemplos_manuales.csv` tiene seis filas sin etiquetas ni identificación del presidente. A y B son comunes; C a F son de reserva. Las referencias separadas permiten revelar procedencia después de registrar la hipótesis.

| Campo de ejemplos | Tipo | Significado |
|---|---|---|
| `ejemplo_id` | Texto | Letra que identifica el ejemplo |
| `uso` | Texto | `comun` o `reserva` |
| `texto` | Texto | Unidad completa sin recortar su contenido; puede contener pistas sobre autor o época |

`docente/referencias_ejemplos.csv` tiene una fila por ejemplo.

| Campo de referencias | Tipo | Significado |
|---|---|---|
| `ejemplo_id` | Texto | Vínculo con el ejemplo mostrado |
| `uso` | Texto | Uso común o de reserva |
| `unidad_id` | Texto | Unidad original; permite cruzar con etiquetas |
| `documento_id` | Texto | Documento de procedencia |
| `pagina_inicio` | Entero | Primera página del pasaje en el PDF |
| `pagina_fin` | Entero | Última página del pasaje en el PDF |
| `motivo_didactico` | Texto | Razón dirigida de selección; no es una categoría automática |

## Clasificaciones existentes

`docente/clasificaciones_existentes.csv` tiene 619 filas, una por unidad, sin crear nuevas etiquetas. Se une a las unidades por `unidad_id` en una relación uno a uno.

| Campo | Tipo | Significado |
|---|---|---|
| `unidad_id` | Texto | Clave del segmento etiquetado |
| `documento_id` | Texto | Documento vinculado |
| `etiqueta_primaria` | Texto | Categoría dominante asignada por el modelo: empresario, regulador, facilitador, asistencial o no aplica (`no_aplica`) |
| `etiqueta_secundaria` | Texto o vacío | Categoría secundaria del modelo; no crea otra unidad |
| `confianza` | Texto | Valoración categórica del modelo, no probabilidad calibrada |
| `justificacion` | Texto | Explicación original del modelo; también requiere revisión |
| `procedencia_etiqueta` | Texto | `modelo_de_lenguaje` |
| `commit_fuente` | Texto hexadecimal | Commit de investigación del que procede la etiqueta |

## Resultados guardados

`resultados_guardados/comparacion_palabras.csv` tiene 30 filas: una combinación de documento y palabra por fila. Se limita a cinco palabras exactas y no es una tabla de roles.

| Campo | Tipo | Significado |
|---|---|---|
| `documento_id` | Texto | Documento contado |
| `palabra` | Texto | Forma exacta buscada, en minúsculas con tildes |
| `menciones` | Entero | Apariciones de esa forma en `texto_conteo` |
| `n_palabras_conteo` | Entero | Total del mismo documento procesado |
| `menciones_por_1000` | Decimal | `1000 × menciones / n_palabras_conteo`; no es porcentaje |

## Configuración y trazabilidad

`seleccion.json` tiene un objeto por documento. Usa `documento_id`, `archivo`, `anio`, `orador`, `audiencia_declarada`, `observacion_comparabilidad`, `url_pagina` y `url_pdf` con el significado definido arriba. `saludo_inicio` es la línea que delimita el inicio conservado para conteos; `notas_editoriales_excluir` enumera las líneas editoriales excluidas; `sha256_pdf_web_verificado` y `fecha_verificacion_web` registran la comparación con la fuente pública.

`trazabilidad/entradas.json` tiene una fila por archivo de investigación consultado: `ruta_en_investigacion` es una ruta relativa, `commit` fija la versión, `sha256` identifica sus bytes y `bytes` mide el tamaño. No incluye rutas personales.

`trazabilidad/descartes_conteo.json` tiene un registro por descarte editorial, con `documento_id`, `pagina`, `motivo` y `texto` excluido. No enumera cada signo o número descartado por la expresión regular.

`trazabilidad/revision_extraccion.json` registra fecha de revisión, versiones de Python y PyMuPDF, patrón de palabras y número de unidades localizadas. Por documento registra páginas, páginas sin texto, caracteres de reemplazo, conteos de espacio por página, extractos inicial y final e identidad entre PDF web y copia congelada. Los conteos por página son diagnósticos de extracción, no denominadores del ejercicio.

`trazabilidad/verificacion_web.json` registra por año `url_pagina`, `url_pdf`, código de respuesta `http`, huellas `sha256_pdf_web` y `sha256_pdf_tag`, y el booleano `igual_al_tag`. La fecha de esa comprobación está en la configuración de selección.

`SHA256SUMS.txt` registra la huella y ruta de cada archivo de datos, excepto el propio listado. Permite comprobar integridad; no prueba exactitud de interpretaciones ni elimina errores de la fuente.
