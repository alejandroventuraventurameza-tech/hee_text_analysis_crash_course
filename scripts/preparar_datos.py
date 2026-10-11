"""Prepara copias didácticas desde un commit fijo; nunca escribe en investigación.

Uso docente: python scripts/preparar_datos.py --repo-investigacion RUTA
Requiere Python y PyMuPDF (import fitz). No es código para ejecutar en la clase.
"""

import argparse
from bisect import bisect_right
from collections import Counter
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys

import fitz


RAIZ = Path(__file__).resolve().parents[1]
COMMIT = "72fcac7d3ea06b737c3a3f35f37b818411c6dead"
PATRON_PALABRAS = r"[a-záéíóúüñ]+"
EJEMPLOS = [
    ("A", "u11860", "comun", "Producción y ampliación de capacidad de una empresa estatal"),
    ("B", "u14275", "comun", "Promoción declarada y traslado de producción al sector privado"),
    ("C", "u00126", "reserva", "Polisemia de competencia y combinación de instrumentos"),
    ("D", "u00110", "reserva", "Reglas y protección de propiedad con segmentos de distinto tema"),
    ("E", "u00103", "reserva", "Expropiación y finalidad política frente a finalidad económica"),
    ("F", "u14474", "reserva", "Diagnóstico retrospectivo frente a instrumento propuesto"),
]


def huella(datos):
    return hashlib.sha256(datos).hexdigest()


def guardar_json(ruta, objeto):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(objeto, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def guardar_csv(ruta, filas, columnas):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with ruta.open("w", encoding="utf-8", newline="") as salida:
        escritor = csv.DictWriter(salida, fieldnames=columnas, lineterminator="\n")
        escritor.writeheader()
        escritor.writerows(filas)


def clave_texto(texto):
    return re.sub(r"\s+", "", texto)


def indice_original(texto):
    """Reproduce descartes de encabezados del segmentador para localizar unidades.

    Mantiene un mapa al texto original. No se usa para calcular frecuencias.
    """
    omitir = set()
    inicio = 0
    for linea in texto.splitlines(keepends=True):
        limpia = linea.strip()
        letras = [c for c in limpia if c.isalpha()]
        encabezado = (
            bool(letras)
            and sum(c.isupper() for c in letras) / len(letras) > 0.85
            and len(limpia.split()) <= 10
        )
        if encabezado or re.fullmatch(r"\d{1,4}", limpia):
            omitir.update(range(inicio, inicio + len(linea)))
        inicio += len(linea)
    for corte in re.finditer("-\n", texto):
        omitir.update(range(corte.start(), corte.end()))
    posiciones = [i for i, c in enumerate(texto) if not c.isspace() and i not in omitir]
    return "".join(texto[i] for i in posiciones), posiciones


def cuerpo_para_conteos(paginas, seleccion):
    """Descartes editoriales explícitos; conserva encabezados internos y negaciones."""
    partes, descartes = [], []
    for numero, pagina in enumerate(paginas, start=1):
        lineas = pagina.splitlines()
        if numero == 1:
            saludo = seleccion["saludo_inicio"]
            limite = next(i for i, linea in enumerate(lineas) if linea.strip() == saludo)
            descartes.append({"pagina": 1, "motivo": "rotulo_y_subtitulo_inicial", "texto": "\n".join(lineas[:limite])})
            lineas = lineas[limite:]
        conservadas = []
        for linea in lineas:
            if linea.strip() == str(numero):
                descartes.append({"pagina": numero, "motivo": "numero_de_pagina", "texto": linea})
            elif linea.strip() in seleccion.get("notas_editoriales_excluir", []):
                descartes.append({"pagina": numero, "motivo": "nota_editorial", "texto": linea})
            else:
                conservadas.append(linea)
        partes.append("\n".join(conservadas))
    cuerpo = "\n".join(partes).replace("-\n", "")
    palabras = re.findall(PATRON_PALABRAS, cuerpo.lower())
    return cuerpo, " ".join(palabras), descartes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-investigacion", type=Path, default=RAIZ.parent / "discursos_presidenciales")
    args = parser.parse_args()
    fuente = args.repo_investigacion.resolve()
    assert fuente != RAIZ, "La fuente y el repositorio de la clase deben ser distintos."
    entradas = []

    def leer_fijo(ruta):
        datos = subprocess.check_output(["git", "-C", str(fuente), "show", f"{COMMIT}:{ruta}"])
        entradas.append({"ruta_en_investigacion": ruta, "commit": COMMIT, "sha256": huella(datos), "bytes": len(datos)})
        return datos

    def leer_csv(ruta):
        return list(csv.DictReader(io.StringIO(leer_fijo(ruta).decode("utf-8-sig"))))

    seleccion = json.loads((RAIZ / "data/seleccion.json").read_text(encoding="utf-8"))
    manifest = {r["archivo"]: r for r in leer_csv("02_datos/processed/manifest.csv")}
    seleccionados = {r["archivo"] for r in seleccion}
    unidades_fuente = [r for r in leer_csv("02_datos/processed/unidades.csv") if r["archivo"] in seleccionados]
    etiquetas_fuente = {r["unidad_id"]: r for r in leer_csv("02_datos/processed/clasificacion_llm.csv")}
    sha_fuente = leer_fijo("02_datos/raw/discursos/SHA256SUMS.txt").decode("utf-8")
    sumas = {linea.split(maxsplit=1)[1].strip().removeprefix("./"): linea.split()[0] for linea in sha_fuente.splitlines() if linea.strip()}
    documentos, paginas_filas, unidades, etiquetas, descartes, revision = [], [], [], [], [], []
    mapas = {}
    for item in seleccion:
        archivo = item["archivo"]
        original = manifest[archivo]
        assert original["duplicado"] == "False" and original["emisor"] == "oficial"
        assert original["tipo"] == "mensaje" and original["dia"] == "28" and original["mes"] == "7"
        assert int(original["anio"]) == item["anio"]
        ruta_fuente = f"02_datos/raw/discursos/{original['carpeta']}/{archivo}"
        pdf_bytes = leer_fijo(ruta_fuente)
        assert huella(pdf_bytes) == sumas[f"{original['carpeta']}/{archivo}"]
        assert huella(pdf_bytes) == item["sha256_pdf_web_verificado"]
        ruta_pdf = RAIZ / "data/originales" / archivo
        ruta_pdf.parent.mkdir(parents=True, exist_ok=True)
        ruta_pdf.write_bytes(pdf_bytes)
        with fitz.open(stream=pdf_bytes, filetype="pdf") as pdf:
            paginas = [pagina.get_text("text") for pagina in pdf]
        assert all(pagina.strip() for pagina in paginas), archivo
        texto_original = "\n".join(paginas)
        assert "\ufffd" not in texto_original, archivo
        cuerpo, texto_conteo, eliminados = cuerpo_para_conteos(paginas, item)
        texto_ruta = RAIZ / "data/textos_originales" / f"{item['documento_id']}.txt"
        texto_ruta.parent.mkdir(parents=True, exist_ok=True)
        texto_ruta.write_text(texto_original, encoding="utf-8", newline="\n")
        conteo_ruta = RAIZ / "data/textos_conteo" / f"{item['documento_id']}.txt"
        conteo_ruta.parent.mkdir(parents=True, exist_ok=True)
        conteo_ruta.write_text(texto_conteo + "\n", encoding="utf-8", newline="\n")
        documento = {
            "documento_id": item["documento_id"], "archivo": archivo,
            "gobierno": original["gobierno"], "orador": item["orador"],
            "fecha": f"{item['anio']}-07-28", "anio": item["anio"], "tipo": original["tipo"],
            "audiencia_declarada": item["audiencia_declarada"],
            "ocasion": "mensaje anual del 28 de julio posterior al inicio del gobierno",
            "observacion_comparabilidad": item["observacion_comparabilidad"],
            "emisor": original["emisor"], "duplicado": False,
            "n_paginas_pdf": len(paginas), "n_palabras_manifest": int(original["n_palabras"]),
            "n_palabras_conteo": len(texto_conteo.split()),
            "n_unidades": sum(r["archivo"] == archivo for r in unidades_fuente),
            "url_pagina": item["url_pagina"], "url_pdf": item["url_pdf"],
            "ruta_pdf": f"originales/{archivo}", "ruta_texto_original": f"textos_originales/{item['documento_id']}.txt",
            "ruta_texto_conteo": f"textos_conteo/{item['documento_id']}.txt",
            "sha256_pdf": huella(pdf_bytes), "sha256_texto_original": huella(texto_original.encode("utf-8")),
            "sha256_texto_conteo": huella((texto_conteo + "\n").encode("utf-8")),
            "commit_fuente": COMMIT, "texto_original": texto_original, "texto_conteo": texto_conteo,
        }
        documentos.append(documento)
        clave, posiciones = indice_original(texto_original)
        inicios, inicio = [], 0
        for n, pagina in enumerate(paginas, start=1):
            inicios.append(inicio)
            paginas_filas.append({"documento_id": item["documento_id"], "pagina_pdf": n,
                                  "char_inicio_original": inicio, "char_fin_original": inicio + len(pagina), "texto": pagina})
            inicio += len(pagina) + 1
        mapas[archivo] = (documento, clave, posiciones, inicios)
        descartes.extend({"documento_id": item["documento_id"], **r} for r in eliminados)
        revision.append({
            "documento_id": item["documento_id"], "paginas_pdf": len(paginas),
            "paginas_sin_texto": 0, "caracteres_reemplazo": 0,
            "palabras_por_pagina_split": [len(p.split()) for p in paginas],
            "inicio_extracto": paginas[0][:700], "cierre_extracto": paginas[-1][-700:],
            "sha256_web_igual_al_tag": True,
        })
    cursores = Counter()
    for u in unidades_fuente:
        documento, clave, posiciones, inicios = mapas[u["archivo"]]
        buscada = clave_texto(u["texto"])
        indice = clave.find(buscada, cursores[u["archivo"]])
        assert indice >= 0, f"Unidad no localizada: {u['unidad_id']}"
        cursores[u["archivo"]] = indice + len(buscada)
        inicio, fin = posiciones[indice], posiciones[indice + len(buscada) - 1] + 1
        unidades.append({
            "unidad_id": u["unidad_id"], "documento_id": documento["documento_id"],
            "archivo": u["archivo"], "gobierno": u["gobierno"], "fecha": documento["fecha"],
            "emisor": u["emisor"], "tipo": u["tipo"], "duplicado": False,
            "orden": int(u["orden"]), "n_palabras_unidad_fuente": int(u["n_palabras"]),
            "pagina_inicio": bisect_right(inicios, inicio), "pagina_fin": bisect_right(inicios, fin - 1),
            "char_inicio_original": inicio, "char_fin_original": fin, "texto": u["texto"],
        })
        etiqueta = etiquetas_fuente[u["unidad_id"]]
        etiquetas.append({"unidad_id": u["unidad_id"], "documento_id": documento["documento_id"],
                          **{k: etiqueta[k] for k in ["etiqueta_primaria", "etiqueta_secundaria", "confianza", "justificacion"]},
                          "procedencia_etiqueta": "modelo_de_lenguaje", "commit_fuente": COMMIT})
    guardar_json(RAIZ / "data/documentos.json", documentos)
    metadatos = [{k: v for k, v in r.items() if k not in {"texto_original", "texto_conteo"}} for r in documentos]
    guardar_csv(RAIZ / "data/metadatos.csv", metadatos, list(metadatos[0]))
    guardar_csv(RAIZ / "data/paginas.csv", paginas_filas, list(paginas_filas[0]))
    guardar_csv(RAIZ / "data/unidades.csv", unidades, list(unidades[0]))
    guardar_csv(RAIZ / "data/docente/clasificaciones_existentes.csv", etiquetas, list(etiquetas[0]))
    por_id = {u["unidad_id"]: u for u in unidades}
    ejemplos, referencias = [], []
    for ejemplo_id, unidad_id, uso, motivo in EJEMPLOS:
        unidad = por_id[unidad_id]
        ejemplos.append({"ejemplo_id": ejemplo_id, "uso": uso, "texto": unidad["texto"]})
        referencias.append({"ejemplo_id": ejemplo_id, "uso": uso, "unidad_id": unidad_id,
                            "documento_id": unidad["documento_id"], "pagina_inicio": unidad["pagina_inicio"],
                            "pagina_fin": unidad["pagina_fin"], "motivo_didactico": motivo})
    guardar_csv(RAIZ / "data/ejemplos_manuales.csv", ejemplos, list(ejemplos[0]))
    guardar_csv(RAIZ / "data/docente/referencias_ejemplos.csv", referencias, list(referencias[0]))
    guardar_json(RAIZ / "data/trazabilidad/entradas.json", entradas)
    guardar_json(RAIZ / "data/trazabilidad/descartes_conteo.json", descartes)
    guardar_json(RAIZ / "data/trazabilidad/revision_extraccion.json", {
        "fecha_revision": "2026-10-10", "pymupdf_version": fitz.VersionBind,
        "python_version": sys.version.split()[0], "patron_palabras": PATRON_PALABRAS,
        "documentos": revision, "unidades_localizadas": len(unidades),
    })
    tasas = []
    for documento in documentos:
        conteos = Counter(documento["texto_conteo"].split())
        for palabra in ["estado", "empresa", "empresas", "inversión", "competencia"]:
            tasas.append({"documento_id": documento["documento_id"], "palabra": palabra,
                          "menciones": conteos[palabra], "n_palabras_conteo": documento["n_palabras_conteo"],
                          "menciones_por_1000": 1000 * conteos[palabra] / documento["n_palabras_conteo"]})
    guardar_csv(RAIZ / "data/resultados_guardados/comparacion_palabras.csv", tasas, list(tasas[0]))
    assert len(documentos) == 6 and len(unidades) == len(etiquetas) == 619
    assert len({u["unidad_id"] for u in unidades}) == len(unidades)
    assert all(int(u["n_palabras_unidad_fuente"]) == len(u["texto"].split()) for u in unidades)
    archivos = sorted(p for p in (RAIZ / "data").rglob("*") if p.is_file() and p.name != "SHA256SUMS.txt")
    sumas_salida = [f"{huella(p.read_bytes())}  {p.relative_to(RAIZ).as_posix()}" for p in archivos]
    (RAIZ / "data/SHA256SUMS.txt").write_text("\n".join(sumas_salida) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"documentos": len(documentos), "unidades": len(unidades), "ejemplos": len(ejemplos),
                      "paginas": len(paginas_filas), "archivos_con_huella": len(archivos)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
