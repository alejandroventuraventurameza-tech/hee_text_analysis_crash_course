"""Revisa estáticamente Beamer y crea un ZIP autocontenido para Overleaf.

No ejecuta XeLaTeX, Biber, un compilador de la app ni un renderizador.
"""

import csv
import hashlib
import json
from pathlib import Path
import re
import zipfile


RAIZ = Path(__file__).resolve().parents[1]
SLIDES = RAIZ / "slides"


def sin_comentarios(texto):
    return re.sub(r"(?<!\\)%[^\n]*", "", texto)


def balance_llaves(texto):
    nivel = 0
    for coincidencia in re.finditer(r"(?<!\\)[{}]", texto):
        nivel += 1 if coincidencia.group() == "{" else -1
        assert nivel >= 0, "Cierre de llave sin apertura"
    assert nivel == 0, "Llaves sin cerrar"


def balance_entornos(texto):
    pila = []
    for coincidencia in re.finditer(r"\\(begin|end)\{([^}]+)\}", texto):
        operacion, nombre = coincidencia.groups()
        if operacion == "begin":
            pila.append(nombre)
        else:
            assert pila and pila.pop() == nombre, "Entorno sin pareja: " + nombre
    assert not pila, "Entornos sin cerrar"


def main():
    textos = {p.name: sin_comentarios(p.read_text(encoding="utf-8")) for p in SLIDES.glob("*.tex")}
    assert set(textos) == {"1_main.tex", "2_preamble.tex", "3_content.tex"}
    for nombre, texto in textos.items():
        balance_llaves(texto)
        balance_entornos(texto)
        for entrada in re.findall(r"\\input\{([^}]+)\}", texto):
            ruta = SLIDES / (entrada if entrada.endswith(".tex") else entrada + ".tex")
            assert ruta.is_file(), (nombre, entrada)
        for bib in re.findall(r"\\addbibresource\{([^}]+)\}", texto):
            assert (SLIDES / bib).is_file(), (nombre, bib)
        for imagen in re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", texto):
            assert (SLIDES / "images" / imagen).is_file(), imagen
        assert "pd01/" not in texto
        assert not re.search(r"[A-Za-z]:\\", texto), "Ruta personal en LaTeX"
    contenido = textos["3_content.tex"]
    for tabla in re.findall(r"\\begin\{tabular\}.*?\\end\{tabular\}", contenido, re.S):
        for linea in tabla.splitlines():
            if "&" in linea:
                assert linea.rstrip().endswith(r"\\"), "Fila sin terminador: " + linea
    etiquetas = re.findall(r"label=([a-z0-9-]+)", contenido)
    assert len(etiquetas) == 34 and len(set(etiquetas)) == 34
    comun = contenido.split(r"\appendix")[0]
    assert len(re.findall(r"\\begin\{frame\}", comun)) == 27
    bib = (SLIDES / "4_bibliography.bib").read_text(encoding="utf-8")
    balance_llaves(bib)
    claves = set(re.findall(r"@\w+\{([^,]+),", bib))
    citadas = set()
    for lista in re.findall(r"\\(?:parencite|textcite|cite|nocite)\{([^}]+)\}", contenido):
        citadas.update(lista.split(","))
    assert len(claves) == 7 and citadas == claves
    with (SLIDES / "data/comparacion_competencia.csv").open(encoding="utf-8") as archivo:
        filas = list(csv.DictReader(archivo))
    assert len(filas) == 2
    for fila in filas:
        tasa = 1000 * int(fila["menciones"]) / int(fila["n_palabras_conteo"])
        assert abs(tasa - float(fila["menciones_por_1000"])) < 1e-12
        etiqueta = "Leguía 1921" if fila["documento_id"] == "leguia_1921" else "Fujimori 1991"
        numero = f"{int(fila['n_palabras_conteo']):,}".replace(",", ".")
        redondeada = f"{tasa:.3f}".replace(".", ",")
        assert f"{etiqueta} & {fila['menciones']} & {numero} & {redondeada}" in contenido
        assert f"({fila['menciones_por_1000']},{{{etiqueta}}})" in contenido
    procedencia = json.loads((SLIDES / "data/procedencia.json").read_text(encoding="utf-8"))
    unidades = [f["texto_unidad"] for f in procedencia["fuentes_fragmentos"]]
    citas = re.findall(r"\\enquote\{([^}]+)\}", contenido)
    citas_largas = [re.sub(r"\s+", " ", cita).strip() for cita in citas if len(cita.split()) > 4]
    assert len(citas_largas) == 5
    for cita in citas_largas:
        assert any(cita in re.sub(r"\s+", " ", unidad) for unidad in unidades), cita
    template = RAIZ.parent / "template_beamer"
    for entrada in procedencia["huellas_template_original"]:
        ruta = template / entrada["archivo_template"]
        assert hashlib.sha256(ruta.read_bytes()).hexdigest() == entrada["sha256"]
    assert (template / "images/UP_logo.jpg").read_bytes() == (SLIDES / "images/UP_logo.jpg").read_bytes()
    colores = re.findall(r"\\definecolor\{[^}]+\}\{[^}]+\}\{[^}]+\}", textos["2_preamble.tex"])
    colores_originales = re.findall(r"\\definecolor\{[^}]+\}\{[^}]+\}\{[^}]+\}", (template / "2_preamble_pd01.tex").read_text(encoding="utf-8"))
    assert colores == colores_originales, "La paleta original debe conservarse"
    informe = {"fecha": "2026-10-11", "frames_comunes": 27, "frames_apendice": 4,
        "frames_referencias": 3, "claves_bibliograficas": sorted(claves),
        "rutas_locales_existentes": True, "llaves_y_entornos_balanceados": True,
        "filas_tablas_cerradas": True, "etiquetas_unicas": True,
        "extractos_literales_contrastados": len(citas_largas),
        "tabla_y_grafico_coherentes_con_csv": True, "logo_identico": True,
        "template_original_sin_cambios": True, "paleta_conservada": True,
        "compilacion_verificada": False, "revision_visual_pdf_realizada": False,
        "limite": "La revisión estática no confirma compilación, referencias resueltas ni ajuste visual."}
    (SLIDES / "revision_estatica.json").write_text(json.dumps(informe, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    contenidos = {p.relative_to(SLIDES).as_posix(): p.read_bytes() for p in sorted(SLIDES.rglob("*"))
                  if p.is_file() and p.name != "README.md"}
    leeme = """# Proyecto Beamer para Overleaf

Importa este ZIP como proyecto nuevo. Selecciona 1_main.tex y el compilador XeLaTeX. La bibliografía usa Biber y estilo APA. Overleaf normalmente ejecuta Biber durante la compilación; si faltan referencias, recompila desde cero y revisa el log.

1_main.tex carga 2_preamble.tex y 3_content.tex desde la raíz. La bibliografía está en 4_bibliography.bib, el logo en images/ y la procedencia y datos en data/. No se requiere una carpeta pd01 ni acceso al repositorio de investigación.

La presentación conserva el formato 4:3 y la identidad del template original. Contiene 27 slides comunes, cuatro de consulta y tres de referencias. Las notas permanecen ocultas. Los resultados aparecen después de las actividades de predicción; el docente controla cuándo avanzar.

Dependencias de TeX: Beamer, fontspec, babel español, amsmath, amssymb, graphicx, geometry, multicol, TikZ, etoolbox, biblatex-apa con Biber e idioma español, csquotes, pgfplots y appendixnumberbeamer. El gráfico de reserva usa pgfplots con compatibilidad 1.18. No hay fuentes privadas, claves ni descargas durante la compilación.

Se revisaron estáticamente rutas, referencias, estructura y coherencia con los datos. NO se compiló localmente ni se verificó en Overleaf. Revisa allí portada, fragmento B, tabla de aplicaciones y bibliografía, además de los avisos del log. La revisión estática no prueba ausencia de desbordes ni ajuste visual.

SHA256SUMS.txt identifica los archivos incluidos, excepto el propio listado. El guion docente y los notebooks se distribuyen por separado desde el repositorio de clase.
"""
    contenidos["LEEME_OVERLEAF.md"] = leeme.encode("utf-8")
    contenidos["SHA256SUMS.txt"] = ("\n".join(f"{hashlib.sha256(datos).hexdigest()}  {nombre}" for nombre, datos in sorted(contenidos.items())) + "\n").encode("utf-8")
    destino = RAIZ / "paquetes/beamer_overleaf.zip"
    destino.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(destino, "w", compression=zipfile.ZIP_DEFLATED) as paquete:
        for nombre, datos in sorted(contenidos.items()):
            info = zipfile.ZipInfo(nombre, date_time=(2026, 10, 11, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            paquete.writestr(info, datos)
    with zipfile.ZipFile(destino) as paquete:
        assert paquete.testzip() is None
        for linea in paquete.read("SHA256SUMS.txt").decode("utf-8").splitlines():
            esperado, nombre = linea.split("  ", 1)
            assert hashlib.sha256(paquete.read(nombre)).hexdigest() == esperado
    print(json.dumps({"frames": len(etiquetas), "archivos_zip": len(contenidos),
        "revision_estatica": "correcta", "compilacion": "no realizada"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
