"""Alinea Colab con el ZIP final, que se lee y nunca se reescribe."""
import base64
import hashlib
import json
import re
import textwrap
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
ZIP = RAIZ / "paquetes/hee_text_analysis_crash_course.zip"


def adaptar(notebook, docente=False):
    anteriores = {c['id']: c for c in notebook['cells']}
    celdas = []
    with zipfile.ZipFile(ZIP) as archivo:
        contenido = archivo.read('3_content.tex').decode('utf-8')
        preambulo = archivo.read('2_preamble.tex').decode('utf-8')
        apertura = archivo.read('apertura.tex').decode('utf-8')
        titulo = re.search(r'\\title\[[^\]]*\]\{([^}]+)\}', preambulo)
        # Algunas versiones usan una variable para el título: el ZIP es la autoridad.
        titulo = titulo.group(1) if titulo else 'Las palabras como datos: análisis textual de discursos presidenciales con Python'
        if '\\' in titulo:
            titulo = 'Las palabras como datos: análisis textual de discursos presidenciales con Python'
        bloques = re.findall(r'\\begin\{colabcode\}(.*?)\\end\{colabcode\}', contenido, re.S)
        logo = base64.b64encode(archivo.read('images/UP_logo.jpg')).decode('ascii') if 'images/UP_logo.jpg' in archivo.namelist() else base64.b64encode(archivo.read('UP_logo.jpg')).decode('ascii')
        def imagen(nombre, ancho=420):
            datos = base64.b64encode(archivo.read(nombre)).decode('ascii')
            tipo = 'png' if nombre.endswith('.png') else 'jpeg'
            return f'<img src="data:image/{tipo};base64,{datos}" width="{ancho}" alt="Ilustración del Beamer: {Path(nombre).stem}">'
        roles_imagen = imagen('images/roles_por_gobierno.png', 650)

    def nueva(tipo, identificador, texto):
        celda = {'cell_type': tipo, 'id': identificador, 'metadata': {},
                 'source': textwrap.dedent(texto).strip().splitlines(keepends=True)}
        if tipo == 'code':
            celda.update(execution_count=None, outputs=[])
        celdas.append(celda)

    def md(i, t): nueva('markdown', i, t)
    def codigo(i, t): nueva('code', i, t)
    def conservar(*ids):
        celdas.extend(anteriores[i] for i in ids)
    def respuesta(i, consigna, ejemplo):
        md(i, consigna + ('\n\n**Ejemplo docente para discutir:** ' + ejemplo if docente else '\n\n**Mi respuesta:** completa aquí.'))

    md('portada', f'''<img src="data:image/jpeg;base64,{logo}" width="210" alt="Universidad del Pacífico">

# 🔎 {titulo}

**Historia Económica y Empresarial · Semestre 2026 II**

**Alejandro Ventura**  
al.venturam@up.edu.pe  
Departamento de Economía y Finanzas · Universidad del Pacífico

*El contenido expuesto en esta sesión es responsabilidad única del expositor.*

{'Versión resuelta para el docente: las respuestas son ejemplos para discutir.' if docente else 'Notebook individual: ejecuta, modifica y explica con tus propias palabras.'}
''')
    md('objetivos-final', '''## 🎯 ¿Qué aprenderemos hoy?

Al finalizar esta clase deberías poder:

- Entender el NLP y su flujo: **raw text → preprocessing → feature extraction → model → output**.
- Aplicar tokenización, stop words, manejo de puntuación y normalización.
- Modificar una instrucción y explicar su efecto.
- Comparar menciones considerando la extensión de los documentos.
- Interpretar palabras en contexto y contrastar una etiqueta automática.
- Formular una conclusión con evidencia, límites y una aplicación a tu carrera.
''')
    conservar('uso')
    md('problematica-final', '''## 💬 Una pregunta para entrar en calor

**¿Cómo estudiarían el rol del Estado peruano en el desarrollo económico, reduciendo la influencia de nuestras afinidades políticas?**

Discute tu idea antes de mirar los resultados. ¿Qué evidencia permitiría cuestionar tu primera impresión?
''')
    respuesta('respuesta-problema', '**Mi propuesta inicial:**', 'Definiría instrumentos de intervención, observaría documentos comparables y explicitaría reglas de clasificación que permitan contrastar mis expectativas.')
    md('proxy-final', '''## 🔍 Un buen punto de partida: métricas observables

La apertura conecta al Estado con el tejido social y la cooperación masiva, siguiendo a Harari: incluso una tiranía involucra múltiples personas. ¿Podemos identificar a todas las personas que toman decisiones y conocer en detalle sus criterios y prioridades? La explicación en la pizarra conecta este problema de **inobservabilidad** con una **variable proxy**: una medida observable que aproxima un concepto difícil de observar directamente.

### Esbozando una proxy variable

¿Quién personifica a la nación? Las diapositivas plantean esta pregunta en un contexto de democracia de corte occidental y abren la discusión sobre otras concepciones de democracia con Cunningham, Saich y Turiel (2020). Usamos el artículo 110 de la Constitución peruana como punto de partida institucional: «El Presidente de la República es el Jefe del Estado y personifica a la Nación». Después preguntamos si los discursos permiten aproximar orientaciones económicas declaradas y categorizar instrumentos de intervención.

**Para discutir:** ¿por qué justificar los criterios de clasificación es una parte difícil de un trabajo cuantitativo? Un discurso permite observar lo declarado; para comprobar decisiones ejecutadas necesitamos otras fuentes. La Constitución actual orienta la discusión institucional y no se aplica retroactivamente a todos los mensajes históricos.

### ¿Cómo entender el pensamiento de un presidente?

Entrevistas, redes sociales y discursos presidenciales son posibles fuentes. Aquí trabajaremos con **discursos presidenciales**. Siguiendo la analogía del caballo y el jinete de las diapositivas: los documentos son el insumo y el NLP aporta herramientas para analizarlos.
''')
    md('api-final', '''## 🔌 ¿Y si usáramos posts de X?

Una **API** es una interfaz con reglas para que un programa solicite datos a un servicio. En la analogía del restaurante, el programa hace el pedido y el mesero comunica la solicitud y devuelve la respuesta.

| Paso | Tu programa | API | Servicio de la plataforma |
|---|---|---|---|
| Solicitud → | Define qué solicita | Recibe y comunica la consulta | Busca los datos permitidos |
| ← Respuesta | Recibe el resultado | Devuelve la respuesta | Entrega datos o informa un error |

**Pregunta para después del curso:** ¿cómo adaptarías nuestro ejercicio a publicaciones de X? ¿Qué metadatos necesitarías? No realizamos llamadas a esa API en este notebook. El enlace de las diapositivas permite consultar sus condiciones: [documentación de X](https://developer.x.com/#pricing).
''')
    md('nlp-final', '''## 🧠 ¿Qué es el NLP?

La motivación de las diapositivas parte del lenguaje humano y su capacidad de sostener significados compartidos, a partir de la lectura de Harari. ¿Cómo puede una computadora trabajar con ese lenguaje?

El **procesamiento del lenguaje natural (NLP)** reúne métodos para analizar lenguaje con herramientas computacionales. Nuestro recorrido sigue el flujo de las diapositivas:

| Etapa | En este ejercicio |
|---|---|
| Raw text | Mensajes presidenciales y sus metadatos |
| Preprocessing | Tokenizar, explorar stop words y puntuación, normalizar |
| Feature extraction | Frecuencias y menciones por 1.000 palabras |
| Model | Contrastar etiquetas ya producidas por un modelo de lenguaje |
| Output | Tabla, gráfico, evidencia textual e interpretación |

No entrenamos un modelo ni enviamos textos a un servicio de IA. El último contraste utiliza resultados preparados.
''')
    md('raw-final', '''## 📚 Raw text: nuestros documentos

El archivo de [mensajes presidenciales del Congreso](https://www3.congreso.gob.pe/participacion/museo/congreso/mensajes-presidenciales/) contiene nuestro material de partida. Las diapositivas presentan un panorama de 31 gobiernos desde el inicio del Oncenio de Leguía y preguntan por qué gobierno y presidente no son equivalentes. Como el mineral bruto de cobre de las diapositivas, el texto extraído necesita revisión antes de contar.

En esta práctica seleccionamos **seis mensajes del 28 de julio**: Leguía (1920 y 1921), Velasco (1969 y 1970) y Alberto Fujimori (1991 y 1992). La selección permite aprender el procedimiento; no representa todos los discursos ni gobiernos completos.
''')
    md('roles-imagen-final', '## 🏛️ Tres roles del Estado\n\n¿Hasta qué punto las caracterizaciones generales de un gobierno describen todos sus instrumentos? El gráfico de las diapositivas abre esa discusión.\n\n' + roles_imagen + '\n\nDistingue gobiernos, mensajes y unidades de texto: no son la misma unidad de análisis.')
    conservar('roles', 'fragmentos-ciegos', 'hipotesis-manual', 'decision-manual')
    conservar('python-colab', 'primera-celda', 'pandas', 'preparacion', 'metadatos', 'tabla-documentos', 'respuesta-fila', 'recuperacion-carga')
    md('nltk-final', '''## 🧰 Preprocessing: herramientas en español

Usaremos **NLTK** para tokenizar, consultar stop words y aplicar stemming en español. Para **lematizar**, y solo para esa comparación, usaremos **spaCy con un modelo español**: `WordNetLemmatizer` de NLTK está pensado para inglés.

Ejecuta en orden. La primera instalación y la descarga de recursos necesitan conexión. Los documentos ya están incluidos; no se envían a un servicio externo para procesarlos.
''')
    codigo('instalar-nltk', '''# @title 🧰 Preparar NLTK
import importlib.util
import subprocess
import sys

if importlib.util.find_spec("nltk") is None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "nltk==3.10.3", "--quiet"])
import nltk
if not nltk.download("punkt_tab", quiet=True):
    raise RuntimeError("No se pudo descargar punkt_tab. Revisa la conexión y vuelve a ejecutar.")
if not nltk.download("stopwords", quiet=True):
    raise RuntimeError("No se pudieron descargar las stop words. Revisa la conexión.")
print("NLTK listo: tokenización y stop words en español.")
''')
    md('tokenizacion-final', '''## ✂️ Tokenization

Un token es una pieza del texto. Primero separamos **oraciones** y después **palabras y signos**. Antes de ejecutar, predice cuántas oraciones aparecerán y si el punto será un token.

### Sentence tokenization

Este es el mismo ejemplo de las diapositivas: Leguía, 1920, página PDF 4, unidad `u00052`.
''')
    codigo('nltk-oraciones', '# @title ✂️ Sentence tokenization en español\n' + bloques[0].strip())
    md('palabras-final', '''### Word tokenization

La oración de Leguía de 1921 es la misma de las diapositivas. Observa que separar palabras todavía no implica eliminar puntuación ni convertir a minúsculas.
''')
    codigo('nltk-palabras', '# @title 🔤 Word tokenization en español\n' + bloques[1].strip())
    respuesta('respuesta-tokens', '**Oraciones y tokens:** explica qué cambió entre las dos operaciones.', 'La primera operación devuelve dos oraciones; la segunda devuelve palabras y el punto final como elementos separados. No asigna significados ni categorías económicas.')
    md('stopwords-final', '''## 🧹 Stop words

Explora la lista española de NLTK, tal como en las diapositivas. Después aplícala a un pasaje real: **«No ha descuidado mi Gobierno el incremento de la agricultura y ganadería.»**, Leguía, 1921.

**Predice:** ¿qué le ocurriría a la interpretación si borráramos «no»? Para esta tarea protegemos las negaciones; una palabra frecuente puede contener información decisiva.
''')
    codigo('nltk-stop-lista', '# @title 📋 Stop words en español\n' + bloques[2].strip())
    codigo('nltk-stop-remover', '''# @title 🧹 Aplicar stop words conservando negaciones
text = "No ha descuidado mi Gobierno el incremento de la agricultura y ganadería."
tokens = nltk.word_tokenize(text, language="spanish")
negaciones = {"no", "ni", "nunca", "sin", "tampoco"}
stop_words_protegidas = set(stop_words) - negaciones
filtered_tokens = [word for word in tokens if word.lower() not in stop_words_protegidas]
print("Antes:", tokens)
print("Después:", filtered_tokens)
''')
    md('puntuacion-final', '''## ✏️ Manejo de signos de puntuación

Para esta exploración de frecuencias quitamos los signos de los extremos de cada token y descartamos los elementos vacíos. `string.punctuation` contiene signos ASCII; añadimos signos habituales en español, como **¿** y **¡**, que pueden quedar pegados a una palabra al tokenizar. La puntuación puede ser útil para otras tareas y se conserva en el original para la lectura.
''')
    codigo('nltk-puntuacion', '''# @title ✏️ Retirar puntuación
import string
print("Puntuación ASCII:", string.punctuation)
signos = set(string.punctuation + "¿¡«»“”‘’—–…")
tokens_sin_bordes = [word.strip("".join(signos)) for word in filtered_tokens]
clean_tokens = [word for word in tokens_sin_bordes if word]
print(clean_tokens)
''')
    md('normalizacion-final', '''## 🔧 Common text normalization techniques

### Lowercasing

Pasar a minúsculas reúne formas que solo se diferencian por las mayúsculas. Conservamos las tildes. Esta transformación no resuelve polisemia ni une singular y plural.
''')
    codigo('nltk-minusculas', '''# @title 🔡 Lowercasing
lower_text = text.lower()
print(lower_text)
lower_tokens = [word.lower() for word in clean_tokens]
print(lower_tokens)
''')
    md('stemming-final', '''### Stemming con NLTK

`SnowballStemmer("spanish")` reduce formas mediante reglas para el español. Las raíces obtenidas pueden no ser palabras del diccionario. Predice qué ocurrirá con «empresas» y «gobiernos».
''')
    codigo('nltk-stemming', '''# @title 🌱 Stemming en español
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer("spanish")
tokens_ejemplo = ["empresa", "empresas", "gobierno", "gobiernos"]
stemmed = [stemmer.stem(word) for word in tokens_ejemplo]
display(pd.DataFrame({"palabra": tokens_ejemplo, "raíz NLTK": stemmed}))
print("Raíces del pasaje:", [stemmer.stem(word) for word in lower_tokens])
''')
    md('lemmas-final', '''### Lemmatization: excepción con spaCy

En esta técnica buscamos el **lema**, una forma base que considera información lingüística. NLTK no ofrece un lematizador general nativo para español: su `WordNetLemmatizer` no resuelve este caso. **Únicamente aquí utilizamos spaCy**, con `es_core_news_sm`, y comparamos con el stemming de NLTK sobre las mismas palabras del mismo pasaje.

Mantendremos el análisis morfosintáctico necesario para los lemas, aunque no necesitamos reconocimiento de entidades ni análisis de dependencias. El modelo puede cometer errores; revisa el resultado. Un mayor costo corresponde al procesamiento y la carga del modelo, no a que debamos compilar nuestros textos.

[Modelos de spaCy](https://spacy.io/usage/models) · [SnowballStemmer de NLTK](https://www.nltk.org/api/nltk.stem.SnowballStemmer.html).
''')
    codigo('instalar-lematizacion', '''# @title 🧰 Preparar solo el lematizador español
from importlib import metadata
import importlib

version_spacy = "3.8.16"
modelo_version = "3.8.0"
try:
    instalado = metadata.version("spacy")
except metadata.PackageNotFoundError:
    instalado = None
if instalado != version_spacy:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "spacy==" + version_spacy, "--quiet"])
    importlib.invalidate_caches()
try:
    modelo_instalado = metadata.version("es-core-news-sm")
except metadata.PackageNotFoundError:
    modelo_instalado = None
if modelo_instalado != modelo_version:
    url_modelo = "https://github.com/explosion/spacy-models/releases/download/es_core_news_sm-3.8.0/es_core_news_sm-3.8.0-py3-none-any.whl"
    subprocess.check_call([sys.executable, "-m", "pip", "install", url_modelo, "--quiet"])
    importlib.invalidate_caches()
import spacy
nlp_lemmas = spacy.load("es_core_news_sm", disable=["parser", "ner"])
print("Lematizador español listo.")
''')
    codigo('comparar-normalizacion', '''# @title 🔬 Comparar stemming y lematización en contexto
texto_normalizacion = "Las empresas y los gobiernos promovieron la agricultura."
tokens_nltk = nltk.word_tokenize(texto_normalizacion, language="spanish")
palabras_nltk = [word for word in tokens_nltk if word.isalpha()]
doc_lemmas = nlp_lemmas(texto_normalizacion)
tokens_spacy = [token for token in doc_lemmas if token.is_alpha]
# Comprobamos que comparamos las mismas palabras, no listas desalineadas.
assert palabras_nltk == [token.text for token in tokens_spacy]
normalizacion = pd.DataFrame({
    "forma original": palabras_nltk,
    "minúsculas": [word.lower() for word in palabras_nltk],
    "stemming NLTK": [stemmer.stem(word.lower()) for word in palabras_nltk],
    "lema spaCy": [token.lemma_ for token in tokens_spacy],
})
display(normalizacion)
print("Oración didáctica creada para comparar; no es una cita presidencial.")
print("Ahora, el pasaje real de Leguía de 1921:")
normalizacion_discurso = pd.DataFrame([
    {"forma original": token.text,
     "stemming NLTK": stemmer.stem(token.text.lower()),
     "lema spaCy": token.lemma_}
    for token in nlp_lemmas(text) if token.is_alpha
])
display(normalizacion_discurso)
''')
    respuesta('respuesta-normalizacion', '**Comparación:** señala una raíz que no sea una palabra del diccionario y explica qué diferencia observas con el lema. ¿Qué perderíamos al reemplazar siempre el original?', 'El stemming puede devolver empres y gobiern; el lema conserva empresa y gobierno. Agrupar formas puede ser útil, pero no identifica qué rol económico tiene cada uso. Conservo el original para interpretar el pasaje.')
    md('aplicar-corpus-final', '''## 📏 Menciones por 1.000 palabras

**Tasa = 1.000 × menciones / palabras del mismo documento procesado.**

Para reproducir la tabla de las diapositivas necesitamos una regla estable: excluir rótulos editoriales, reparar guiones de fin de línea y contar formas exactas en minúsculas conservando tildes. La versión `texto_conteo` contiene ese trabajo documentado; a continuación la tokenizamos con NLTK para los seis mensajes.

**Las técnicas no son una receta que debamos aplicar completa:** el stemming y los lemas se compararon como alternativas. No los aplicamos a la consulta de forma exacta «competencia». Las stop words se pueden ocultar en el ranking, pero permanecen en el denominador. Así conservamos las 4.527 y 23.348 palabras de la tabla del Beamer. Los signos y las cabeceras no cuentan como palabras en esta regla.
''')
    codigo('nltk-corpus', '''# @title 📚 Tokenizar los seis discursos para conteos
tokens_por_documento = {
    fila.documento_id: nltk.word_tokenize(fila.texto_conteo, language="spanish")
    for fila in documentos.itertuples()
}
for fila in documentos.itertuples():
    assert len(tokens_por_documento[fila.documento_id]) == fila.n_palabras_conteo
print("Seis documentos tokenizados; denominadores comprobados.")
''')
    conservar('transformacion', 'original-conteo', 'frecuencias-explicacion', 'frecuencias', 'respuesta-transformacion')
    celdas[-2]['source'] = [line.replace('documento["texto_conteo"].split()', 'tokens_por_documento[documento["documento_id"]]') for line in celdas[-2]['source']]
    conservar('comparacion', 'prediccion-lexica', 'tasas', 'grafico-explicacion', 'grafico', 'lectura-tasas', 'recuperacion', 'recuperar', 'contexto', 'contextos', 'fragmentos-seleccion', 'evidencia', 'interpretacion-fragmentos')
    inicio = list(anteriores).index('etiquetas-intro')
    conservar(*list(anteriores)[inicio:])
    md('referencias-final', '''## 📚 Lecturas de la apertura y herramientas

- Harari, Y. N. (2014). *Sapiens: De animales a dioses. Una breve historia de la humanidad*. Debate.
- Cunningham, E., Saich, T. y Turiel, J. (2020). *Understanding CCP Resilience: Surveying Chinese Public Opinion Through Time*. Harvard Kennedy School. [Documento citado en las diapositivas](https://rajawali.hks.harvard.edu/wp-content/uploads/sites/2/2020/07/final_policy_brief_7.6.2020.pdf).
- Ministerio de Justicia y Derechos Humanos (2025). *Constitución Política del Perú*, 21.ª edición oficial, actualizada al 5 de diciembre de 2025. Artículo 110. [Edición citada en las diapositivas](https://cdn.www.gob.pe/uploads/document/file/9139522/7498785-constitucion-politica_2025-final-dic-2025.pdf?v=1765572191).
- [Tokenización de NLTK](https://www.nltk.org/api/nltk.tokenize.html), [stemming de NLTK](https://www.nltk.org/api/nltk.stem.SnowballStemmer.html) y [modelos de spaCy](https://spacy.io/usage/models).

Las referencias de la apertura se transcriben de la bibliografía incluida en el Beamer final.
''')

    # Evitar afirmaciones antiguas y sincronizar el conteo también en las ayudas.
    for celda in celdas:
        fuente = ''.join(celda['source'])
        fuente = fuente.replace('funciona sin descargar modelos ni usar claves', 'no requiere claves; más adelante descargaremos los recursos lingüísticos')
        fuente = fuente.replace('Los textos están preparados para evitar una instalación de modelos.', 'Los textos preparados conservan una regla de conteo reproducible.')
        fuente = fuente.replace('`split()` separa por espacios la versión ya preparada;', 'NLTK tokeniza la versión ya preparada;')
        if celda['id'] == 'preparacion':
            fuente = fuente.replace('palabras = documento["texto_conteo"].split()', 'import nltk\n        palabras = nltk.word_tokenize(documento["texto_conteo"], language="spanish")')
        if celda['id'] == 'frecuencias':
            fuente = re.sub(r'palabras_a_ocultar = \[[^\n]+\]', 'palabras_a_ocultar = sorted(stop_words_protegidas)', fuente)
        if celda['id'] == 'frecuencias-explicacion':
            fuente = fuente.replace('Las palabras de `palabras_a_ocultar`', 'Usamos la lista española de NLTK, con negaciones protegidas, como `palabras_a_ocultar`. Esas palabras')
        if celda['id'] == 'recuperacion':
            fuente = fuente.replace('ejecuta primero Preparación;', 'ejecuta primero Preparación y Preparar NLTK;')
        celda['source'] = fuente.splitlines(keepends=True)
    notebook['cells'] = celdas
    notebook['metadata']['curso'].update(version='2026-10-12', beamer_fuente=str(ZIP.name),
        beamer_sha256=hashlib.sha256(ZIP.read_bytes()).hexdigest(),
        procesamiento='NLTK español; spaCy exclusivamente para lematización', colab_comprobado=False)
    notebook['metadata']['curso'].pop('duracion_minutos', None)
    secuencia = contenido.replace(r'\input{apertura}', apertura)
    titulos = re.findall(r'\\begin\{frame\}(?:\[[^\]]*\])?(?:\{([^\n]*)\})?', secuencia)
    destinos = ['portada', 'objetivos-final', 'problematica-final', *['proxy-final'] * 6,
                'proxy-final', 'proxy-final', 'api-final', 'nlp-final', 'nlp-final', 'nlp-final',
                'raw-final', 'roles-imagen-final', 'roles-imagen-final', 'roles',
                'fragmentos-ciegos', 'fragmentos-ciegos', 'tabla-documentos', 'nltk-final',
                'tokenizacion-final', 'tokenizacion-final', 'nltk-oraciones', 'nltk-palabras',
                'stopwords-final', 'nltk-stop-lista', 'puntuacion-final', 'normalizacion-final',
                'nltk-minusculas', 'nltk-stemming', 'comparar-normalizacion', 'aplicar-corpus-final',
                'frecuencias', 'prediccion-lexica', 'tasas', 'contexto', 'evidencia',
                'etiquetas-preparadas', 'etiquetas-intro']
    assert len(titulos) == len(destinos), 'Revisar alineación: cambió la secuencia del ZIP final.'
    assert set(destinos).issubset({c['id'] for c in celdas})
    auditoria = {'beamer_sha256': notebook['metadata']['curso']['beamer_sha256'],
                 'fecha': '2026-10-12', 'frames': [
                     {'numero': i + 1, 'titulo_tex': t or 'Portada', 'celda_colab': d}
                     for i, (t, d) in enumerate(zip(titulos, destinos))],
                 'conservado_del_colab_anterior': ['carga incluida y manual', 'recuperación',
                     'preguntas individuales', 'entrega sin calificación', 'desafío opcional'],
                 'excepcion_autorizada': 'spaCy exclusivamente para lematización española'}
    (RAIZ / 'notebooks/alineacion_beamer.json').write_text(json.dumps(auditoria, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return notebook
