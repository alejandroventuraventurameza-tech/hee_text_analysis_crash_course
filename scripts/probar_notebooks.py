"""Ejecuta ambos notebooks en kernels nuevos y registra resultados locales.

Requiere el entorno docente con jupyter_client, ipykernel, pandas y matplotlib.
Las celdas preparan sus recursos NLP si faltan. No accede a investigación ni a Colab.
"""

import copy
import hashlib
import json
from pathlib import Path
import queue
import sys
import tempfile
import time

from jupyter_client import KernelManager


RAIZ = Path(__file__).resolve().parents[1]


def ejecutar(cliente, codigo, limite=600):
    mensaje = cliente.execute(codigo, allow_stdin=False)
    salidas, cuenta = [], None
    fin = time.monotonic() + limite
    while time.monotonic() < fin:
        try:
            respuesta = cliente.get_iopub_msg(timeout=1)
        except queue.Empty:
            continue
        if respuesta.get("parent_header", {}).get("msg_id") != mensaje:
            continue
        tipo, contenido = respuesta["msg_type"], respuesta["content"]
        if tipo == "status" and contenido["execution_state"] == "idle":
            return salidas, cuenta
        if tipo == "execute_input":
            cuenta = contenido["execution_count"]
        elif tipo in {"stream", "display_data", "execute_result", "error"}:
            salida = {"output_type": tipo}
            if tipo == "stream":
                salida.update(name=contenido["name"], text=contenido["text"])
            elif tipo == "error":
                raise RuntimeError(contenido["ename"] + ": " + contenido["evalue"])
            else:
                salida.update(data=contenido["data"], metadata=contenido.get("metadata", {}))
                if tipo == "execute_result":
                    salida["execution_count"] = contenido["execution_count"]
            salidas.append(salida)
    raise TimeoutError("Una celda no terminó dentro del límite de prueba.")


COMPROBACIONES = '''
import json, math, platform, sys, matplotlib
assert len(documentos) == 6 and len(unidades) == 619 and len(paginas) == 148
assert "etiqueta_primaria" not in unidades.columns
assert comparacion["menciones"].tolist() == [2, 11]
assert comparacion["n_palabras_conteo"].tolist() == [4527, 23348]
assert evidencia["documento_id"].nunique() == 2
assert evidencia["unidad_id"].tolist() == ["u00126", "u14275"]
assert Path("mi_comparacion.csv").exists() and Path("mi_evidencia.csv").exists()
assert Path("mi_comparacion.png").exists()
import nltk, spacy
assert len(sentences) == 2
assert words[-1] == "." and "bondad" in words
original_1920 = " ".join(documentos.loc[documentos["documento_id"] == "leguia_1920", "texto_original"].iloc[0].split())
original_1921 = " ".join(documentos.loc[documentos["documento_id"] == "leguia_1921", "texto_original"].iloc[0].split())
assert " ".join(sentences) in original_1920
assert "La bondad del procedimiento ha sido ratificada por sus resultados." in original_1921
assert text in original_1921
assert "No" in filtered_tokens and "No" in clean_tokens
assert "." not in clean_tokens and "no" in lower_tokens
assert stemmer.stem("empresas") == stemmer.stem("empresa")
assert "¿" in signos and "¡" in signos
assert [w.strip("".join(signos)) for w in nltk.word_tokenize("¿No?", language="spanish") if w.strip("".join(signos))] == ["No"]
assert normalizacion.loc[normalizacion["forma original"] == "empresas", "lema spaCy"].iloc[0] == "empresa"
assert normalizacion.loc[normalizacion["forma original"] == "gobiernos", "lema spaCy"].iloc[0] == "gobierno"
assert all(len(tokens_por_documento[f.documento_id]) == f.n_palabras_conteo for f in documentos.itertuples())
assert len(tokens_por_documento) == 6
assert normalizacion_discurso["forma original"].iloc[0] == "No"
assert "no" not in palabras_a_ocultar and "de" in palabras_a_ocultar
for _, fila in resultados_guardados.iterrows():
    nueva = comparar_palabra(documentos, fila["palabra"], [fila["documento_id"],
        next(x for x in documentos["documento_id"] if x != fila["documento_id"])]).iloc[0]
    assert nueva["menciones"] == fila["menciones"]
    assert math.isclose(nueva["menciones_por_1000"], fila["menciones_por_1000"])
assert buscar_contextos(documentos, unidades, paginas, "palabrainexistente", ids_comparar, 100).empty
assert comparar_palabra(documentos, "INVERSION", ids_comparar)["menciones"].sum() == 0
assert comparar_palabra(documentos, "INVERSIÓN", ids_comparar)["menciones"].sum() > 0
negaciones = buscar_contextos(documentos, unidades, paginas, "no", ids_comparar, 150)
assert len(negaciones) > 0 and all("no" in texto.lower() for texto in negaciones["contexto"])
for invalida in ["", "dos palabras", "empresa*"]:
    try:
        comparar_palabra(documentos, invalida, ids_comparar)
        raise AssertionError("Consulta inválida aceptada")
    except ValueError:
        pass
print(json.dumps({"python": sys.version.split()[0], "pandas": pd.__version__, "nltk": nltk.__version__, "spacy": spacy.__version__, "modelo_es": nlp_lemmas.meta["version"],
    "matplotlib": matplotlib.__version__, "sistema": platform.system(),
    "tabla": comparacion.to_dict(orient="records"),
    "unidades_evidencia": evidencia["unidad_id"].tolist()}, ensure_ascii=False))
'''


def main():
    resultados = []
    for nombre in ["estudiantes.ipynb", "docente_resuelto.ipynb"]:
        ruta = RAIZ / "notebooks" / nombre
        notebook = json.loads(ruta.read_text(encoding="utf-8"))
        ejecutado = copy.deepcopy(notebook)
        gestor = KernelManager(kernel_name="python3")
        with tempfile.TemporaryDirectory(prefix="curso_prueba_") as temporal:
            try:
                gestor.start_kernel(cwd=temporal)
                cliente = gestor.client()
                cliente.start_channels()
                cliente.wait_for_ready(timeout=30)
                ejecutar(cliente, "%matplotlib inline")
                for celda in ejecutado["cells"]:
                    if celda["cell_type"] != "code":
                        continue
                    celda["outputs"], celda["execution_count"] = ejecutar(cliente, "".join(celda["source"]))
                    print(nombre, celda["id"], "correcta", flush=True)
                salidas, _ = ejecutar(cliente, COMPROBACIONES)
                datos = json.loads(next(s["text"] for s in salidas if s["output_type"] == "stream" and s["name"] == "stdout"))
                # Probar el ZIP distribuido con la misma lectura usada por carga manual.
                preparacion = "".join(next(c["source"] for c in notebook["cells"] if c["id"] == "preparacion"))
                zip_local = preparacion.replace('modo_carga = "incluida"', 'modo_carga = "zip_local"')
                zip_local = zip_local.replace('ruta_zip_local = ""', "ruta_zip_local = " + repr(str(RAIZ / "paquetes/datos_estudiantes.zip")))
                ejecutar(cliente, zip_local)
                ejecutar(cliente, 'assert len(documentos) == 6 and len(unidades) == 619\nassert "etiqueta_primaria" not in unidades.columns')
                # La interfaz de subida de Colab no está disponible localmente.
                # Simular únicamente los bytes que devolvería files.upload().
                simular_subida = '''
import types, sys
colab_simulado = types.ModuleType("google.colab")
bytes_subida = Path(ruta_zip_local).read_bytes()
colab_simulado.files = types.SimpleNamespace(upload=lambda: {"datos_estudiantes.zip": bytes_subida})
sys.modules["google.colab"] = colab_simulado
'''
                ejecutar(cliente, simular_subida)
                ejecutar(cliente, preparacion.replace('modo_carga = "incluida"', 'modo_carga = "manual"'))
                ejecutar(cliente, 'assert len(documentos) == 6 and len(unidades) == 619')
                # Recuperación y salidas guardadas después de perder variables de resultados.
                ejecutar(cliente, 'del comparacion, contextos, evidencia')
                recuperar = "".join(next(c["source"] for c in notebook["cells"] if c["id"] == "recuperar"))
                ejecutar(cliente, recuperar)
                guardados = "".join(next(c["source"] for c in notebook["cells"] if c["id"] == "usar-guardados"))
                ejecutar(cliente, guardados.replace("usar_resultados_guardados = False", "usar_resultados_guardados = True"))
                ejecutar(cliente, 'assert comparacion.attrs["origen"] == "guardada"\nassert comparacion["menciones"].tolist() == [2, 11]')
                desafio = "".join(next(c["source"] for c in notebook["cells"] if c["id"] == "desafio-codigo"))
                ejecutar(cliente, desafio.replace("hacer_desafio = False", "hacer_desafio = True"))
                imagenes = sum("image/png" in s.get("data", {}) for c in ejecutado["cells"] if c["cell_type"] == "code" for s in c["outputs"])
                assert imagenes >= 1, "El gráfico debe quedar guardado en las salidas del notebook."
                ejecutado["metadata"]["curso"]["prueba_local"] = {"fecha": "2026-10-12", **{clave: datos[clave] for clave in ["sistema", "python", "pandas", "matplotlib", "nltk", "spacy", "modelo_es"]}}
                if nombre == "docente_resuelto.ipynb":
                    ruta.write_text(json.dumps(ejecutado, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
                resultados.append({"notebook": nombre, "celdas_codigo": sum(c["cell_type"] == "code" for c in ejecutado["cells"]),
                    "ejecucion_completa": True, "imagenes_en_salidas": imagenes,
                    "sha256_notebook_final": hashlib.sha256(ruta.read_bytes()).hexdigest(), **datos})
            finally:
                if "cliente" in locals():
                    cliente.stop_channels()
                gestor.shutdown_kernel(now=True)
    informe = {"fecha": "2026-10-12", "pruebas": resultados,
        "casos_adicionales": ["tokenización de oraciones españolas", "ejemplos NLTK localizados en originales", "puntuación española", "stop words con negaciones protegidas", "stemming frente a lemas españoles", "denominadores de seis textos tokenizados con NLTK", "30 tasas contra resultados guardados", "tildes y mayúsculas", "consulta sin coincidencias", "negaciones conservadas", "consultas inválidas rechazadas", "ZIP manual real", "recepción de bytes de files.upload simulada", "recuperación sin variables de resultados", "salidas guardadas identificadas", "desafío opcional"],
        "colab_comprobado": False, "subida_colab_comprobada": False,
        "url_publica_comprobada": False, "nota": "Este registro documenta únicamente la ejecución local. La evidencia recibida de la interfaz de Colab está separada en prueba_colab_guiada.json; no se extiende automáticamente a modificaciones posteriores de instrucciones o títulos."}
    (RAIZ / "notebooks/prueba_local.json").write_text(json.dumps(informe, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print("Prueba local completa; evidencia de Colab registrada por separado.")


if __name__ == "__main__":
    main()
