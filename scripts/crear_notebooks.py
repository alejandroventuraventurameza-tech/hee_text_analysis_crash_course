"""Construye las dos versiones del notebook con datos de clase incluidos.

No requiere bibliotecas externas. La ejecución de los notebooks sí usa pandas
y matplotlib. Las etiquetas se incluyen en una celda independiente al final.
"""

import base64
import csv
import io
import json
from pathlib import Path
import textwrap
import zipfile


RAIZ = Path(__file__).resolve().parents[1]
DATOS = RAIZ / "data"
DESTINO = RAIZ / "notebooks"


def paquete_incluido(nombres):
    salida = io.BytesIO()
    with zipfile.ZipFile(salida, "w", compression=zipfile.ZIP_DEFLATED) as archivo:
        for nombre in nombres:
            info = zipfile.ZipInfo(nombre, date_time=(2026, 10, 11, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            archivo.writestr(info, (DATOS / nombre.removeprefix("data/")).read_bytes())
    return base64.b64encode(salida.getvalue()).decode("ascii")


PREPARACION = '''
# @title Preparación de datos y herramientas de recuperación
# Ejecuta esta celda preparada. No necesitas editar su implementación.
modo_carga = "incluida" # @param ["incluida", "manual", "url", "zip_local"]
url_paquete = "" # @param {type:"string"}
ruta_zip_local = "" # @param {type:"string"}

import base64, io, json, re, zipfile
from pathlib import Path
from urllib.request import urlopen
from collections import Counter
import pandas as pd
from IPython.display import display

PAQUETE_INCLUIDO = "__PAQUETE__"
if modo_carga == "incluida":
    paquete_actual = base64.b64decode(PAQUETE_INCLUIDO)
elif modo_carga == "manual":
    from google.colab import files
    subidos = files.upload()
    if len(subidos) != 1:
        raise ValueError("Selecciona un solo archivo datos_estudiantes.zip.")
    paquete_actual = next(iter(subidos.values()))
elif modo_carga == "url":
    if not url_paquete.startswith("https://"):
        raise ValueError("Falta el enlace HTTPS al ZIP público. Usa incluida o manual.")
    try:
        with urlopen(url_paquete, timeout=20) as respuesta:
            paquete_actual = respuesta.read()
    except Exception as error:
        raise ValueError("No se pudo descargar. Cambia modo_carga a incluida o manual.") from error
elif modo_carga == "zip_local":
    paquete_actual = Path(ruta_zip_local).read_bytes()
else:
    raise ValueError("Elige una de las opciones de carga.")

ARCHIVOS_TABLAS = ["documentos.json", "unidades.csv", "paginas.csv",
                   "ejemplos_manuales.csv", "resultados_guardados/comparacion_palabras.csv"]
CARPETA_DATOS = Path("datos_curso")
CARPETA_DATOS.mkdir(exist_ok=True)
with zipfile.ZipFile(io.BytesIO(paquete_actual)) as paquete:
    for nombre in ARCHIVOS_TABLAS:
        destino = CARPETA_DATOS / nombre
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_bytes(paquete.read("data/" + nombre))

def cargar_tablas():
    documentos = pd.DataFrame(json.loads((CARPETA_DATOS / "documentos.json").read_text(encoding="utf-8")))
    unidades = pd.read_csv(CARPETA_DATOS / "unidades.csv", keep_default_na=False)
    paginas = pd.read_csv(CARPETA_DATOS / "paginas.csv", keep_default_na=False)
    ejemplos = pd.read_csv(CARPETA_DATOS / "ejemplos_manuales.csv", keep_default_na=False)
    guardados = pd.read_csv(CARPETA_DATOS / "resultados_guardados/comparacion_palabras.csv")
    if len(documentos) != 6 or len(unidades) != 619:
        raise ValueError("Este paquete no corresponde a los datos revisados de la clase.")
    return documentos, unidades, paginas, ejemplos, guardados

def validar_consulta(documentos, palabra, ids):
    palabra = palabra.strip().lower()
    if not re.fullmatch(r"[a-záéíóúüñ]+", palabra):
        raise ValueError("Escribe una sola palabra española, con sus tildes y sin signos.")
    if len(ids) < 2 or len(set(ids)) != len(ids):
        raise ValueError("Elige al menos dos documentos distintos, sin repetir identificadores.")
    if not set(ids).issubset(set(documentos["documento_id"])):
        raise ValueError("Copia los identificadores tal como aparecen en la tabla.")
    return palabra

def comparar_palabra(documentos, palabra, ids):
    palabra = validar_consulta(documentos, palabra, ids)
    filas = []
    for documento_id in ids:
        documento = documentos.loc[documentos["documento_id"] == documento_id].iloc[0]
        palabras = documento["texto_conteo"].split()
        menciones = palabras.count(palabra)
        filas.append({"documento_id": documento_id, "fecha": documento["fecha"],
                      "palabra": palabra, "menciones": menciones,
                      "n_palabras_conteo": len(palabras),
                      "menciones_por_1000": 1000 * menciones / len(palabras)})
    tabla = pd.DataFrame(filas)
    tabla.attrs["palabra"] = palabra
    tabla.attrs["ids"] = list(ids)
    tabla.attrs["origen"] = "recalculada"
    return tabla

def buscar_contextos(documentos, unidades, paginas, palabra, ids, amplitud):
    palabra = validar_consulta(documentos, palabra, ids)
    if not isinstance(amplitud, int) or amplitud < 0:
        raise ValueError("La amplitud debe ser un número entero de caracteres, desde cero.")
    filas = []
    patron = re.compile(r"\\b" + re.escape(palabra) + r"\\b", re.IGNORECASE)
    for documento_id in ids:
        documento = documentos.loc[documentos["documento_id"] == documento_id].iloc[0]
        original = documento["texto_original"]
        for hallazgo in patron.finditer(original):
            candidatas = unidades.loc[(unidades["documento_id"] == documento_id)
                & (unidades["char_inicio_original"] <= hallazgo.start())
                & (unidades["char_fin_original"] > hallazgo.start())]
            pagina = paginas.loc[(paginas["documento_id"] == documento_id)
                & (paginas["char_inicio_original"] <= hallazgo.start())
                & (paginas["char_fin_original"] > hallazgo.start())].iloc[0]
            fragmento = original[max(0, hallazgo.start() - amplitud):hallazgo.end() + amplitud]
            filas.append({"documento_id": documento_id, "fecha": documento["fecha"],
                          "pagina_pdf": int(pagina["pagina_pdf"]),
                          "unidad_id": candidatas.iloc[0]["unidad_id"] if len(candidatas) else "",
                          "char_inicio_original": hallazgo.start(),
                          "char_fin_original": hallazgo.end(), "palabra": palabra,
                          "contexto": fragmento.replace("\\n", " ")})
    tabla = pd.DataFrame(filas, columns=["documento_id", "fecha", "pagina_pdf", "unidad_id",
        "char_inicio_original", "char_fin_original", "palabra", "contexto"])
    tabla.attrs["palabra"] = palabra
    tabla.attrs["ids"] = list(ids)
    return tabla

documentos, unidades, paginas, ejemplos, resultados_guardados = cargar_tablas()
print("Datos listos:", len(documentos), "documentos y", len(unidades), "unidades sin etiquetas.")
'''


def crear(docente=False):
    celdas = []

    def agregar(tipo, identificador, texto, preparado=False):
        lineas = texto.strip("\n").split("\n")
        texto = (lineas[0].strip() + "\n" + textwrap.dedent("\n".join(lineas[1:]))).strip() + "\n"
        celda = {"cell_type": tipo, "id": identificador, "metadata": {}, "source": texto.splitlines(keepends=True)}
        if tipo == "code":
            celda.update(execution_count=None, outputs=[])
            if preparado:
                celda["metadata"] = {"cellView": "form", "tags": ["codigo_preparado"]}
        celdas.append(celda)

    def md(identificador, texto):
        agregar("markdown", identificador, texto)

    def codigo(identificador, texto, preparado=False):
        titulos = {
            "primera-celda": "Saludo: tu primer resultado",
            "tabla-documentos": "Tabla de los seis documentos",
            "original-conteo": "Texto original y versión para conteos",
            "frecuencias": "Frecuencias: cambia de 10 a 8 palabras",
            "tasas": "Comparación: conteos y menciones por 1.000 palabras",
            "grafico": "Gráfico de la comparación",
            "contextos": "Contextos: amplía de 100 a 180 caracteres",
            "evidencia": "Dos fragmentos completos y su procedencia",
            "comprobacion-entrega": "Comprobación antes de guardar",
            "usar-guardados": "Resultados guardados: solo si el docente lo indica",
            "desafio-codigo": "Desafío opcional: retirar un documento",
        }
        agregar("code", identificador, texto, preparado)
        if identificador in titulos:
            celdas[-1]["source"].insert(0, "# @title " + titulos[identificador] + "\n")

    def respuesta(identificador, consigna, resuelta):
        md(identificador, consigna + ("\n\n**Ejemplo docente de respuesta, no respuesta única.**\n\n" + resuelta if docente else "\n\n**Mi respuesta:** completa aquí."))

    filas_ejemplos = list(csv.DictReader((DATOS / "ejemplos_manuales.csv").open(encoding="utf-8")))
    a, b = (next(r["texto"] for r in filas_ejemplos if r["ejemplo_id"] == letra) for letra in ["A", "B"])
    md("portada", f'''# Discursos presidenciales bajo la lupa

    Análisis textual con Python · Historia Económica y Empresarial · 2026 II

    {"Versión resuelta para el docente. Sus respuestas son ejemplos para discutir; no constituyen etiquetas humanas validadas." if docente else "Notebook individual para estudiantes. Ejecuta y modifica código en tu propia laptop, aunque discutas con otras personas."}

    Alejandro Ventura · al.venturam@up.edu.pe

    **Pregunta:** ¿Qué instrumentos de intervención económica aparecen en estos mensajes y qué diferencias podemos sostener al comparar palabras y leer fragmentos?

    Los discursos permiten estudiar instrumentos y prioridades declaradas. Para saber qué se ejecutó hacen falta otras fuentes; estos datos no permiten establecer causalidad. La selección de seis mensajes no representa gobiernos completos.
    ''')
    md("uso", '''## Cómo trabajar y qué entregar

    Antes de cada resultado escribe una predicción, ejecuta, interpreta y comprueba con el original. Cambia los valores señalados y vuelve a ejecutar. Las celdas tituladas Preparación ya resuelven las operaciones difíciles; no necesitas copiarlas ni entender toda su implementación.

    **Para escribir:** haz doble clic en una celda que diga **Mi respuesta** y reemplaza «completa aquí» por tu explicación. Usa las celdas ya incluidas. Las respuestas se escriben como texto; los cálculos se ejecutan con el botón ▶ de las celdas de código. Conserva tu primera hipótesis si cambia.

    **Para encontrar una operación:** busca su título, por ejemplo **Recuperación de la comparación** o **Comprobación antes de guardar**. Puedes usar Ctrl+F en el navegador. Si un título de código no aparece como encabezado, está escrito en la primera línea de la celda.

    Al final entrega este notebook con una tabla o gráfico, dos fragmentos identificados, conclusión, limitación y aplicación a tu carrera. La actividad no tiene calificación.

    **Antes de ejecutar:** guarda una copia propia en Drive y ponle `apellido_nombre_analisis_textual`. En clase sigue el ritmo del docente y escribe tus predicciones antes de obtener resultados. Si todavía no tienes el notebook abierto en la primera discusión, anota A y B en papel y transfiere tus respuestas cuando abras tu copia.
    ''')
    md("fragmentos-ciegos", f'''## 0–10 minutos Primera hipótesis

    ¿Cómo analizarías cientos de discursos sin leerlos todos completos? Estos fragmentos son reales; su procedencia se revelará después. No necesitas reconocer al presidente.

    **Fragmento A**

    > {a}

    **Fragmento B**

    > {b}

    ¿Qué intervención económica describe cada uno? Señala una expresión que sostenga tu interpretación y una duda. Todavía no consultes etiquetas.
    ''')
    respuesta("hipotesis-manual", "**Primera hipótesis:** describe A y B sin necesidad de asignar todavía un rol.",
              "A describe ampliación de producción petrolera en una empresa estatal. B propone políticas generales y transferencia de producción al sector privado, aunque también emplea el término promotor. Debe comprobarse qué instrumento predomina; nombrar promoción no resuelve la clasificación.")
    md("historia", '''## 10–15 minutos Categorías, conteos y modelos

    El análisis de contenido interpreta textos mediante categorías y reglas explícitas. Berelson sistematizó este enfoque en 1952. El análisis asistido por computadora, como General Inquirer, permite aplicar diccionarios y contar a escala. Los modelos de lenguaje son una familia de métodos computacionales que también puede asignar categorías mediante instrucciones.

    Estos enfoques pueden combinarse. Ninguno elimina la necesidad de comprobar interpretaciones y errores. ¿Qué parte de nuestro problema requiere reglas, cuál admite conteos y cuál exige volver al fragmento?

    Referencias: [Berelson, reseña de 1952](https://www.journals.uchicago.edu/doi/10.1086/617924), [General Inquirer](https://inquirer.sites.fas.harvard.edu/) y [Gilardi, Alizadeh y Kubli, 2023](https://doi.org/10.1073/PNAS.2305016120). El desempeño del último estudio no se extrapola a los discursos peruanos.
    ''')
    md("roles", '''## 15–23 minutos Clasificación manual

    Para este caso distinguimos instrumentos dominantes:

    - **Empresario:** propiedad y control estatal de producción.
    - **Regulador:** reglas generales y supervisión de mercados.
    - **Facilitador:** promoción selectiva sin requerir propiedad estatal.

    También hay categorías asistencial y no aplica en la investigación. Si el fragmento no permite decidir, puedes responder evidencia insuficiente y explicar qué falta. Esa respuesta didáctica no crea una etiqueta automática nueva.

    Clasifica A y B, apoya cada decisión con una expresión y registra una duda. Una palabra aislada no determina un rol; tampoco una unidad caracteriza toda una presidencia.
    ''')
    respuesta("decision-manual", "**Decisión manual antes de ver al modelo:** A: … Evidencia: … Duda: … B: … Evidencia: … Duda: …",
              "A: empresario, porque una empresa estatal ampliaría refinación y producción; el texto no prueba la ejecución. B: regulador como lectura provisional, por políticas generales y producción privada bajo competencia; la atención de servicios básicos y las excepciones añaden ambigüedad. La justificación importa más que coincidir con una etiqueta.")
    md("python-colab", '''## 23–36 minutos Primera celda y carga

    **Python** es el lenguaje de instrucciones; una **biblioteca** reúne herramientas reutilizables; **Colab** es el entorno donde editamos el notebook y ejecutamos Python. Una celda puede contener explicación o código. Las variables son nombres que conservan valores: `=` asigna y las comillas delimitan texto. `print()` muestra un valor.

    Ejecuta la siguiente celda, cambia el saludo y vuelve a ejecutarla. El cambio debe aparecer en tu resultado.
    ''')
    codigo("primera-celda", 'saludo = "Estoy explorando textos de mi carrera"\nprint(saludo)')
    md("pandas", '''Necesitamos organizar documentos en una tabla: usaremos **pandas**. `import` carga una biblioteca y `pd` es el nombre breve con el que la utilizaremos. Un `DataFrame` es una tabla de filas y columnas. Documentación: [introducción oficial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html).

    La preparación siguiente incluye los datos en el propio notebook y funciona sin descargar modelos ni usar claves. Mantén `modo_carga = "incluida"` para el recorrido común. Si hace falta carga manual, el docente indicará el ZIP y elegirás manual. La opción url se utilizará solo si el docente proporciona un enlace HTTPS directo al ZIP público.
    ''')
    principales = ["data/documentos.json", "data/unidades.csv", "data/paginas.csv", "data/ejemplos_manuales.csv", "data/resultados_guardados/comparacion_palabras.csv"]
    codigo("preparacion", PREPARACION.replace("__PAQUETE__", paquete_incluido(principales)), True)
    md("metadatos", '''**Pregunta:** ¿qué representa una fila? Los metadatos describen el documento: fecha, orador, audiencia y procedencia. Las unidades son segmentos de otra tabla; no confundas documentos, unidades y palabras. Antes de mirar la tabla, predice si todos los mensajes tienen la misma extensión y audiencia.
    ''')
    codigo("tabla-documentos", '''columnas = ["documento_id", "fecha", "orador", "audiencia_declarada", "n_palabras_conteo", "n_unidades"]
    display(documentos[columnas])''')
    respuesta("respuesta-fila", "**Documentos y fila:** identifica los documentos que compararás y explica qué representa una fila de esta tabla.",
              "Compararé leguia_1921 y alberto_fujimori_1991. Cada fila representa un mensaje completo. La tabla de unidades tiene una fila por segmento reconstruido; sus conteos no son denominadores de palabras. Las audiencias declaradas deben comprobarse aun cuando las fechas coincidan.")
    md("recuperacion-carga", '''**Punto de recuperación al minuto 36.** Debes ver seis documentos. Si una celda indica que un nombre no existe, ejecuta Preparación antes de continuar. Si reiniciaste el entorno, vuelve a ejecutar esa celda: los datos incluidos permiten retomar sin una descarga. Tus respuestas escritas en celdas de texto se conservan en la copia guardada del notebook.
    ''')
    md("transformacion", '''## 36–51 minutos Transformación y frecuencias

    **Predice:** ¿qué cambia entre la extracción completa y el texto preparado para conteos? El original conserva títulos, números de página, signos y negaciones. La versión de conteo excluye rótulos iniciales, números de página y una nota editorial; repara guiones de fin de línea, convierte a minúsculas y separa secuencias de letras españolas. Conserva tildes y negaciones. No agrupa singular y plural.

    Un **token** es cada aparición de una palabra según esa regla. Los textos están preparados para evitar una instalación de modelos. El procedimiento está documentado en los materiales de datos.

    `documento_id` guarda el documento que explorarás. Los corchetes seleccionan una columna y `==` comprueba igualdad; aquí el filtro selecciona el documento. El código preparado recupera la primera fila que coincide. Cambia el identificador si quieres explorar otro.
    ''')
    codigo("original-conteo", '''documento_id = "leguia_1921"
    documento = documentos.loc[documentos["documento_id"] == documento_id].iloc[0]
    print("ORIGINAL, comienzo con cabecera:")
    print(documento["texto_original"][:350])
    print("\\nVERSIÓN PARA CONTEOS, comienzo después del rótulo:")
    print(documento["texto_conteo"][:350])
    print("\\nPalabras para conteos:", documento["n_palabras_conteo"])''')
    md("frecuencias-explicacion", '''**Predice:** ¿qué palabras ocuparán el primer lugar? `split()` separa por espacios la versión ya preparada; `Counter` cuenta cada forma exacta y es una herramienta estándar de Python, no una biblioteca que debas instalar. [Documentación de Counter](https://docs.python.org/3/library/collections.html#collections.Counter).

    La celda siguiente construye la tabla y ordena los conteos. Ejecuta y modifica `numero_palabras`, por ejemplo de 10 a 8. Las palabras de `palabras_a_ocultar` se ocultan solo del ranking; siguen formando parte del denominador. No ocultamos negaciones.
    ''')
    codigo("frecuencias", '''numero_palabras = 10
    palabras_a_ocultar = ["de", "la", "el", "y", "en", "a", "que", "los", "del", "las", "se", "un", "por", "con", "para"]
    palabras = documento["texto_conteo"].split()
    frecuencias = pd.DataFrame(Counter(palabras).items(), columns=["palabra", "menciones"])
    frecuencias = frecuencias.sort_values(["menciones", "palabra"], ascending=[False, True])
    ranking = frecuencias.loc[~frecuencias["palabra"].isin(palabras_a_ocultar)]
    display(ranking.head(numero_palabras))
    print("El denominador sigue siendo", len(palabras), "palabras.")''')
    respuesta("respuesta-transformacion", "**Transformación y modificación:** explica una transformación y su límite. Identifica el cambio que hiciste en código y su efecto.",
              "Las mayúsculas pasan a minúsculas, lo que reúne Competencia y competencia. No resuelve sus distintos significados ni une competencia con competencias. Cambiar numero_palabras de 10 a 8 modifica la cantidad de filas visibles, no el total de palabras ni los conteos. En la versión del docente se conserva 10 para mostrar el ejemplo completo; el estudiante debe ejecutar su propio cambio.")
    md("comparacion", '''## 51–66 minutos Comparación normalizada

    **Antes de ejecutar escribe una predicción:** ¿en qué documento aparecerá más la palabra? ¿Cambiará la comparación si atendemos a la extensión?

    **Primera comparación común:** usa `competencia`, `leguia_1921` y `alberto_fujimori_1991` hasta completar la tabla y los dos fragmentos. Tu modificación personal puede ser cambiar el ranking de 10 a 8 o el contexto de 100 a 180. Después de interpretar el caso común puedes explorar otra palabra o cambiar los documentos.

    Para esa exploración, cambia `palabra` o los identificadores de `ids_comparar` y vuelve a ejecutar comparación, gráfico, contextos y fragmentos. Una lista usa corchetes y separa sus elementos con comas. Usa una sola forma exacta, con tildes, y al menos dos documentos distintos.

    **Menciones por 1.000 palabras = 1.000 × menciones / palabras del mismo documento procesado.** La función preparada hace este cálculo. La tasa no es porcentaje de unidades con un rol. Ni normalizar ni aumentar documentos elimina las diferencias de ocasión.
    ''')
    respuesta("prediccion-lexica", "**Palabra y predicción inicial:** registra tu palabra, los documentos y tu expectativa antes de ejecutar la comparación.",
              "Palabra: competencia. Documentos: Leguía de 1921 y Alberto Fujimori de 1991. Anticipo más menciones absolutas en el segundo; todavía no sé cuánto de esa diferencia corresponde a su mayor extensión ni si la palabra describe el mismo concepto.")
    codigo("tasas", '''palabra = "competencia"
    ids_comparar = ["leguia_1921", "alberto_fujimori_1991"]
    comparacion = comparar_palabra(documentos, palabra, ids_comparar)
    display(comparacion.round({"menciones_por_1000": 3}))''')
    md("grafico-explicacion", '''**Predice e interpreta:** ¿cómo se vería la comparación de tasas? Usaremos **matplotlib** para representar números con un gráfico. [Documentación oficial](https://matplotlib.org/stable/tutorials/pyplot.html).

    La celda está preparada. Lee el eje y el título: comparamos menciones por 1.000 palabras, con el eje desde cero. Una diferencia numérica pequeña no prueba una diferencia sustantiva ni se presenta como estadísticamente significativa. Si falta tiempo, conserva la tabla como producto suficiente.
    ''')
    codigo("grafico", '''import matplotlib.pyplot as plt

    figura, eje = plt.subplots(figsize=(8, 3.5))
    eje.barh(comparacion["documento_id"], comparacion["menciones_por_1000"], color="#7A1F2B")
    eje.set_xlabel("Menciones por 1.000 palabras")
    eje.set_title("Forma exacta: " + comparacion.attrs["palabra"])
    eje.set_xlim(left=0)
    figura.tight_layout()
    figura.savefig("mi_comparacion.png", dpi=150, bbox_inches="tight")
    plt.show()''')
    respuesta("lectura-tasas", "**Interpretación provisional del resultado:** compara conteo y tasa. ¿Qué necesitas comprobar leyendo?",
              "Competencia aparece 2 veces entre 4.527 palabras en Leguía de 1921 y 11 entre 23.348 en Fujimori de 1991: aproximadamente 0,442 y 0,471 menciones por 1.000 palabras. La distancia relativa es pequeña frente a la diferencia de conteos. Necesito comprobar si los usos se refieren a mercados o a capacidades y si hay otros conceptos expresados con otras palabras.")
    md("recuperacion", '''## 66–74 minutos Dudas y recuperación

    Si ya tienes la comparación, comprueba el denominador y guarda tu copia. Si te perdiste, ejecuta la siguiente celda preparada: recupera las tablas y vuelve a calcular tu consulta, o usa competencia y los dos documentos iniciales si aún no elegiste. No borra tus respuestas de texto.

    Si reiniciaste el entorno, ejecuta primero Preparación; después esta recuperación. Puede haber una pausa breve según el ritmo del aula.
    ''')
    codigo("recuperar", '''# @title Recuperación de la comparación
    documentos, unidades, paginas, ejemplos, resultados_guardados = cargar_tablas()
    palabra = globals().get("palabra", "competencia")
    ids_comparar = globals().get("ids_comparar", ["leguia_1921", "alberto_fujimori_1991"])
    comparacion = comparar_palabra(documentos, palabra, ids_comparar)
    display(comparacion.round({"menciones_por_1000": 3}))''', True)
    md("contexto", '''## 74–90 minutos Palabras en contexto

    **Predice:** ¿la palabra significa lo que supusiste? Buscar en contexto significa localizar una palabra junto con el texto necesario para interpretarla. La función preparada busca en la extracción original, sin borrar signos ni negaciones; solo cambia saltos de línea a espacios en la ventana mostrada.

    Cambia `amplitud_contexto` de 100 a 180 para ampliar caracteres a cada lado. No son palabras. Revisa el resultado y luego abre la unidad completa y, si hace falta, la página original. Una ventana corta puede omitir una negación o el sujeto de una acción.

    Los conteos usan el texto procesado; esta búsqueda usa la forma literal en la extracción original. Guiones reparados o rótulos excluidos pueden hacer que no coincidan exactamente. Una búsqueda sin resultados no demuestra que un concepto esté ausente.
    ''')
    codigo("contextos", '''amplitud_contexto = 100
    contextos = buscar_contextos(documentos, unidades, paginas, palabra, ids_comparar, amplitud_contexto)
    print("Coincidencias en el original:", len(contextos))
    with pd.option_context("display.max_colwidth", None):
        display(contextos[["documento_id", "pagina_pdf", "unidad_id", "contexto"]])''')
    md("fragmentos-seleccion", '''Selecciona dos números de fila del resultado anterior, correspondientes a documentos distintos. Para la consulta inicial, 0 y 3 permiten una comparación. Si cambiaste la consulta, revisa esos números antes de ejecutar.

    La celda preparada muestra la unidad completa cuando la coincidencia tiene unidad asociada; también conserva la página y el enlace al PDF. El texto de una unidad es un segmento reconstruido y puede reunir varios temas. Si no tiene unidad, se recupera la página completa. Seleccionar estos pasajes no convierte el conjunto en una muestra estadística de roles.
    ''')
    codigo("evidencia", '''indices_fragmentos = [0, 3]
    evidencia = pd.DataFrame()
    if len(indices_fragmentos) != 2 or not all(i in contextos.index for i in indices_fragmentos):
        print("Elige dos filas válidas de contextos. Si no hay coincidencias, revisa palabra y documentos.")
    elif contextos.loc[indices_fragmentos, "documento_id"].nunique() != 2:
        print("Elige una fila de cada documento distinto.")
    else:
        evidencia = contextos.loc[indices_fragmentos].copy()
        for indice, hallazgo in evidencia.iterrows():
            documento = documentos.loc[documentos["documento_id"] == hallazgo["documento_id"]].iloc[0]
            unidad = unidades.loc[unidades["unidad_id"] == hallazgo["unidad_id"]]
            pagina = paginas.loc[(paginas["documento_id"] == hallazgo["documento_id"])
                                 & (paginas["pagina_pdf"] == hallazgo["pagina_pdf"])]
            texto = unidad.iloc[0]["texto"] if len(unidad) else pagina.iloc[0]["texto"]
            evidencia.loc[indice, "fragmento_completo"] = texto
            evidencia.loc[indice, "url_pdf"] = documento["url_pdf"]
            print("\\nDocumento:", hallazgo["documento_id"], "Página:", hallazgo["pagina_pdf"], "Unidad:", hallazgo["unidad_id"])
            print(texto)
            print("Original:", documento["url_pdf"])
        evidencia.attrs["palabra"] = contextos.attrs["palabra"]
        evidencia.attrs["ids"] = contextos.attrs["ids"]''')
    respuesta("interpretacion-fragmentos", "**Fragmentos y revisión:** identifica tus dos pasajes, conserva las citas impresas e interpreta qué muestra cada uno. ¿Mantienes o cambias tu hipótesis?",
              "En leguia_1921, p. 11, u00126, competencia describe la capacidad de especialistas en una campaña sanitaria; la unidad continúa con fomento agrícola. En alberto_fujimori_1991, p. 10, u14275, competencia se vincula con producción y comercialización privadas y políticas generales. Estos dos pasajes muestran usos diferentes, aunque las tasas de la forma exacta sean cercanas. No he revisado aquí todas las ocurrencias de Fujimori ni etiquetado cada uso.")
    md("etiquetas-intro", '''## 90–98 minutos Contraste con etiquetas existentes

    Conserva tu clasificación de A y B antes de ejecutar esta sección. Ahora se revela la procedencia y se carga un conjunto separado de etiquetas ya existentes. No se consulta un modelo en vivo ni se usa una clave.

    Las categorías proceden de un modelo de lenguaje, con justificación y confianza categórica; la confianza no es una probabilidad calibrada. El segundo anotador de la validación fue otro modelo, no un segundo humano. El conjunto de referencia de 30 unidades tiene solo un caso empresario y uno regulador.

    ¿Mantienes tu clasificación, la cambias o necesitas más contexto? Una explicación razonada puede disentir del modelo. No calcules porcentajes de roles con los ejemplos dirigidos.
    ''')
    secundarios = ["data/docente/clasificaciones_existentes.csv", "data/docente/referencias_ejemplos.csv"]
    codigo("etiquetas-preparadas", '''# @title Preparación de etiquetas existentes para el contraste final
    # Esta carga es independiente de los datos usados en el ejercicio inicial.
    ETIQUETAS_INCLUIDAS = "__ETIQUETAS__"
    with zipfile.ZipFile(io.BytesIO(base64.b64decode(ETIQUETAS_INCLUIDAS))) as paquete:
        etiquetas = pd.read_csv(io.BytesIO(paquete.read("data/docente/clasificaciones_existentes.csv")), keep_default_na=False)
        referencias = pd.read_csv(io.BytesIO(paquete.read("data/docente/referencias_ejemplos.csv")), keep_default_na=False)
    contraste = referencias.loc[referencias["uso"] == "comun"].merge(etiquetas, on=["unidad_id", "documento_id"], validate="one_to_one")
    with pd.option_context("display.max_colwidth", None):
        display(contraste[["ejemplo_id", "documento_id", "unidad_id", "pagina_inicio", "etiqueta_primaria", "etiqueta_secundaria", "confianza", "justificacion"]])
    '''.replace("__ETIQUETAS__", paquete_incluido(secundarios)), True)
    respuesta("respuesta-contraste", "**Clasificación manual y contraste:** conserva tu primera decisión y explica un acuerdo, desacuerdo o duda con la etiqueta existente.",
              "Mantengo empresario para A por expansión productiva estatal y regulador provisional para B por políticas generales y mercado. El modelo coincide en esas primarias, pero asigna asistencial como secundaria y confianza media a B. Esa coincidencia no valida por sí sola las etiquetas ni elimina la ambigüedad. Prefiero revisar las excepciones y servicios básicos antes de una conclusión más fuerte.")
    md("entrega", '''## 98–110 minutos Conclusión y entrega

    Completa las respuestas siguientes usando tu tabla y fragmentos. Si falta tiempo, la tabla basta; no necesitas personalizar el gráfico. Un resultado que no respalde tu hipótesis también es válido.
    ''')
    respuesta("conclusion", "**Conclusión en tres a cinco oraciones:** conecta el resultado numérico con tus fragmentos y delimita los documentos a los que se refiere.\n\nPuedes ordenar tu explicación así: qué documentos y palabra comparaste; qué muestran los conteos y tasas; qué cambia al leer los dos pasajes; hasta dónde llega tu conclusión. Escribe con tus propias palabras.",
              "En los mensajes de Leguía de 1921 y Alberto Fujimori de 1991, la forma competencia tiene tasas cercanas: 0,442 y 0,471 por 1.000 palabras, respectivamente. Dos fragmentos localizados muestran usos distintos: capacidad profesional en el primero y competencia de mercado en el segundo. El mayor conteo absoluto de Fujimori no equivale a una diferencia relativa de la misma magnitud. La comparación léxica localiza pasajes para interpretar; no permite asignar un rol a cada gobierno ni verificar lo que efectivamente hizo.")
    respuesta("limitacion", "**Limitación y consecuencia:** identifica una limitación concreta y qué afirmación impide sostener.",
              "Solo comparé dos documentos y dos pasajes, con una forma exacta que tiene varios sentidos y puede sustituirse por sinónimos. No puedo afirmar que toda mención sea competencia de mercado ni que estos mensajes representen todo el gobierno. La tasa describe exposición léxica en esta selección, no incidencia de un rol económico.")
    respuesta("aplicacion", "**Aplicación a mi carrera en dos o tres oraciones:** propone documentos, una pregunta y metadatos necesarios.",
              "En Administración podría comparar reportes empresariales para preguntar cómo se describen riesgos de abastecimiento. Necesitaría empresa, sector, año y tipo de reporte, y comprobaría cada mención en contexto antes de interpretar su frecuencia. Este procedimiento no determina por sí solo el riesgo efectivamente materializado.")
    md("autoevaluacion", '''### Autoevaluación sin puntajes

    Marca cada criterio como listo o por revisar:

    - Ejecuté y modifiqué código; expliqué mi cambio.
    - Identifiqué documentos, una fila y una transformación.
    - Mi tabla o gráfico permite comprobar conteos y denominadores.
    - Conservé dos fragmentos de documentos distintos con identificadores y contexto.
    - Mi conclusión conecta números y fragmentos.
    - Expliqué una limitación y qué afirmación restringe.
    - Justifiqué el contraste con las etiquetas sin tratarlas como verdad.
    - Propuse una aplicación a documentos de mi carrera.

    La comprobación técnica siguiente no evalúa tus respuestas: te ayuda a detectar una consulta cambiada sin volver a ejecutar resultados.
    ''')
    codigo("comprobacion-entrega", '''consulta_actual = palabra.strip().lower()
    tabla_actual = (comparacion.attrs.get("palabra") == consulta_actual and comparacion.attrs.get("ids") == ids_comparar)
    evidencia_actual = (not evidencia.empty and evidencia.attrs.get("palabra") == consulta_actual
                        and evidencia.attrs.get("ids") == ids_comparar)
    if tabla_actual and evidencia_actual:
        comparacion.to_csv("mi_comparacion.csv", index=False, encoding="utf-8")
        evidencia.to_csv("mi_evidencia.csv", index=False, encoding="utf-8")
        print("Tabla y dos fragmentos corresponden a tu consulta. Revisa ahora tus respuestas y guarda el notebook.")
    else:
        print("Revisa la comparación y los fragmentos: vuelve a ejecutar desde la consulta y selecciona dos filas válidas.")
    print("Origen de la tabla:", comparacion.attrs.get("origen", "no registrado"))''')
    md("guardar-entrega", '''### Guardar y entregar

    1. **Guarda:** confirma que tu copia conserva respuestas, tabla y dos fragmentos. Ejecuta **Comprobación antes de guardar** y revisa su mensaje. El mensaje comprueba la consulta; tú revisas tus explicaciones.
    2. **Descarga:** desde **Archivo → Descargar → Descargar .ipynb**, guarda `apellido_nombre_analisis_textual.ipynb`. Si se descargó con otro nombre, renómbralo conservando `.ipynb`.
    3. **Entrega:** entra con tu cuenta institucional de la UP a la carpeta que indique el docente, sube el archivo y comprueba que aparece con tu nombre. Conserva la copia descargada hasta confirmar recepción.

    Si aparece «Solicitar acceso» o no puedes subir el archivo, avisa a la persona de apoyo y conserva tu copia. La carpeta de clase debe tener acceso comprobado antes de utilizarse para la entrega.

    `mi_comparacion.csv`, `mi_evidencia.csv` y `mi_comparacion.png` son complementos; no sustituyen el notebook ni las respuestas. Si falla la subida, conserva el archivo descargado y avisa al docente. Los archivos del entorno de ejecución no se guardan automáticamente dentro de tu Drive: la entrega debe descargarse o guardarse expresamente. [Documentación de Colab](https://research.google.com/colaboratory/faq.html).
    ''')
    md("recuperacion-guardada", '''## Recuperación adicional solo si el docente la indica

    Los datos incluyen resultados guardados de estado, empresa, empresas, inversión y competencia. Activa la siguiente alternativa solo después de escribir tu predicción y si necesitas continuar interpretando mientras se resuelve un problema. Esta tabla se identifica como guardada; no demuestra que hayas recalculado la comparación. Retoma después tu ejecución individual.
    ''')
    codigo("usar-guardados", '''usar_resultados_guardados = False
    if usar_resultados_guardados:
        seleccion = resultados_guardados.loc[(resultados_guardados["palabra"] == palabra.strip().lower())
                                             & resultados_guardados["documento_id"].isin(ids_comparar)]
        if len(seleccion) == len(ids_comparar):
            comparacion = seleccion.set_index("documento_id").loc[ids_comparar].reset_index().copy()
            comparacion.attrs.update(palabra=palabra.strip().lower(), ids=list(ids_comparar), origen="guardada")
            display(comparacion.round({"menciones_por_1000": 3}))
        else:
            print("No hay resultados guardados para esta consulta. Usa la recuperación que recalcula.")''')
    md("desafio", '''## Desafío opcional y adaptación posterior

    Cuando termines el recorrido común, predice qué pasará al retirar un documento de la comparación conjunta de los seis. La tasa conjunta usa suma de menciones dividida por suma de palabras; no el promedio simple de tasas. El ejemplo está preparado y no es obligatorio. Tampoco convierte los seis mensajes en una muestra representativa.

    Para adaptar el procedimiento: formula una pregunta; reúne documentos con ocasión comparable; registra procedencia y metadatos; conserva originales; revisa extracción; define tu regla de conteo; y comprueba las diferencias con pasajes. Temas, sentimientos, entrenamiento de modelos y Probit quedan fuera de esta sesión.
    ''')
    codigo("desafio-codigo", '''hacer_desafio = False
    if hacer_desafio:
        seis = comparar_palabra(documentos, palabra, documentos["documento_id"].tolist())
        retirar = "alberto_fujimori_1991"
        cinco = seis.loc[seis["documento_id"] != retirar]
        tasa_seis = 1000 * seis["menciones"].sum() / seis["n_palabras_conteo"].sum()
        tasa_cinco = 1000 * cinco["menciones"].sum() / cinco["n_palabras_conteo"].sum()
        print("Tasa conjunta de los seis:", round(tasa_seis, 3))
        print("Tasa al retirar", retirar + ":", round(tasa_cinco, 3))
        print("Cambió la selección y su denominador; interpreta con ese alcance.")''')
    return {"nbformat": 4, "nbformat_minor": 5, "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "pygments_lexer": "ipython3"},
        "colab": {"name": "docente_resuelto.ipynb" if docente else "estudiantes.ipynb", "provenance": []},
        "curso": {"duracion_minutos": 110, "version": "2026-10-11", "datos_commit": "72fcac7d3ea06b737c3a3f35f37b818411c6dead", "colab_comprobado": False},
    }, "cells": celdas}


def main():
    DESTINO.mkdir(exist_ok=True)
    for docente, nombre in [(False, "estudiantes.ipynb"), (True, "docente_resuelto.ipynb")]:
        notebook = crear(docente)
        (DESTINO / nombre).write_text(json.dumps(notebook, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
        print(nombre, len(notebook["cells"]), "celdas")


if __name__ == "__main__":
    main()
