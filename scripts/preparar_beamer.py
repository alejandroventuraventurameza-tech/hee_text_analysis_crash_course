"""Adapta una copia del template y prepara recursos de trazabilidad.

No compila LaTeX y nunca modifica el template original ni investigación.
"""

import csv
import hashlib
import json
from pathlib import Path
import shutil
import fitz


RAIZ = Path(__file__).resolve().parents[1]
TEMPLATE = RAIZ.parent / "template_beamer"
SLIDES = RAIZ / "slides"

COVER = r"""\setbeamertemplate{title page}{
\begin{tikzpicture}[remember picture,overlay]
  \fill[UWWhite] ([yshift=30pt]current page.west) rectangle (current page.south east);
  \fill[UWBlack] ([yshift=30pt]current page.west) rectangle (current page.north east);
  \node[anchor=east] at ([yshift=-52pt,xshift=-15pt]current page.north east)
    {\includegraphics[width=0.34\paperwidth]{UP_logo.jpg}};
  \node[anchor=north west] at ([yshift=-35pt,xshift=15pt]current page.north west)
    {\parbox[t]{0.51\paperwidth}{\usebeamercolor[fg]{author}\Large\bfseries\insertauthor}};
  \node[anchor=north west] at ([yshift=-61pt,xshift=15pt]current page.north west)
    {\parbox[t]{0.51\paperwidth}{\hypersetup{urlcolor=UWWhite}\small\href{mailto:al.venturam@up.edu.pe}{al.venturam@up.edu.pe}}};
  \node[anchor=north west] at ([yshift=-82pt,xshift=15pt]current page.north west)
    {\parbox[t]{0.51\paperwidth}{\usebeamercolor[fg]{institute}\normalsize\insertinstitute}};
  \node[anchor=north] at ([yshift=-1pt]current page.center)
    {\parbox[t]{\textwidth}{\centering\usebeamercolor[fg]{title}\fontsize{22}{25}\selectfont\bfseries\inserttitle}};
  \node[anchor=north] at ([yshift=-60pt]current page.center)
    {\parbox[t]{\textwidth}{\centering\large Análisis textual con Python}};
  \node[anchor=north] at ([yshift=-90pt]current page.center)
    {\parbox[t]{\textwidth}{\centering\insertcourse}};
  \node[anchor=north] at ([yshift=-111pt]current page.center)
    {\parbox[t]{\textwidth}{\centering\small\insertclass}};
\end{tikzpicture}
}
"""


def main():
    original = (TEMPLATE / "2_preamble_pd01.tex").read_text(encoding="utf-8")
    preambulo = original.replace(" % Configuración de XeLaTeX (necesaria para símbolos como ☠ y mejor soporte para español e inglés)",
                                "% Preámbulo adaptado del template. Compilador: XeLaTeX.")
    preambulo = preambulo.replace(r"\usepackage[english]{babel}", r"\usepackage[spanish,es-noquoting]{babel}")
    preambulo = preambulo.replace("% Para texto en ingles y español", "% Idioma de la clase")
    preambulo = preambulo.replace(r"\graphicspath{{pd01/images/}{logos/}{pd01/}}", r"\graphicspath{{images/}}")
    preambulo = preambulo.replace(r"\addbibresource{pd01/4_bibliography_pd01.bib}",
        "\\addbibresource{4_bibliography.bib}\n\\DeclareLanguageMapping{spanish}{spanish-apa}\n\\usepackage{csquotes}\n\\usepackage{pgfplots}\n\\pgfplotsset{compat=1.18}")
    preambulo = preambulo.replace(r"\setbeamercolor{normal text}{fg=UWGrayL3}", r"\setbeamercolor{normal text}{fg=UWGrayL4}")
    preambulo = preambulo.replace(r"\setbeamercolor{frametitle}{fg=UWMathPinkL2, bg=UWGrayL1}", r"\setbeamercolor{frametitle}{fg=UWMathPinkL4, bg=UWGrayL1}")
    preambulo = preambulo.replace("{Definition \\thedefcounter", "{Definición \\thedefcounter")
    preambulo = preambulo.replace("{Theorem \\thetheocounter", "{Teorema \\thetheocounter")
    preambulo = preambulo.replace("{Example \\theexcounter", "{Ejemplo \\theexcounter")
    inicio = preambulo.index("% Cargar una fuente que tenga el símbolo")
    fin = preambulo.index("% Comandos para campos comunes")
    preambulo = preambulo[:inicio] + preambulo[fin:]
    inicio = preambulo.index(r"\setbeamertemplate{title page}")
    fin = preambulo.index("% Configuración de la cabecera", inicio)
    preambulo = preambulo[:inicio] + COVER + "\n" + preambulo[fin:]
    preambulo = preambulo[:preambulo.index(r"\title[")]
    preambulo += r"""\title[Análisis textual]{Discursos presidenciales\\bajo la lupa}
\author[Alejandro V.]{Alejandro Ventura}
\institute[UP]{Universidad del Pacífico}
\course{Historia Económica y Empresarial}
\class{2026 II}
\setbeameroption{hide notes}
\setbeamertemplate{bibliography item}{}
\setbeamercolor{bibliography entry author}{fg=UWBlack}
\setbeamercolor{bibliography entry title}{fg=UWBlack}
\setbeamercolor{bibliography entry location}{fg=UWBlack}
\setbeamercolor{bibliography entry note}{fg=UWBlack}
\hypersetup{colorlinks=true,linkcolor=UWBlack,citecolor=UWBlack,urlcolor=peacockblue}
\setbeamercolor{description item}{fg=UWMathPinkL4}
\setbeamercolor{item projected}{fg=UWMathPinkL4}
\newcommand{\fuente}[1]{\par\vspace{0.15cm}{\scriptsize #1\par}}
"""
    SLIDES.mkdir(exist_ok=True)
    (SLIDES / "2_preamble.tex").write_text(preambulo, encoding="utf-8", newline="\n")
    (SLIDES / "images").mkdir(exist_ok=True)
    shutil.copyfile(TEMPLATE / "images/UP_logo.jpg", SLIDES / "images/UP_logo.jpg")
    facsimiles = []
    for nombre in ("28_07_1921_leguia", "28_07_1920_leguia", "28_07_1969_velasco", "28_07_1991_alberto_fujimori"):
        origen = RAIZ / "data/originales" / (nombre + ".pdf")
        destino = SLIDES / "images" / (nombre + "_pagina1.png")
        with fitz.open(origen) as pdf:
            pdf[0].get_pixmap(matrix=fitz.Matrix(2, 2), clip=fitz.Rect(75, 65, 520, 770)).save(destino)
        facsimiles.append({"imagen": destino.relative_to(SLIDES).as_posix(), "original": origen.relative_to(RAIZ).as_posix(), "pagina_pdf": 1, "recorte_puntos": [75,65,520,770], "sha256_original": hashlib.sha256(origen.read_bytes()).hexdigest(), "sha256_imagen": hashlib.sha256(destino.read_bytes()).hexdigest()})
    datos = SLIDES / "data"
    datos.mkdir(exist_ok=True)
    with (RAIZ / "data/resultados_guardados/comparacion_palabras.csv").open(encoding="utf-8") as archivo:
        filas = [r for r in csv.DictReader(archivo) if r["palabra"] == "competencia"
                 and r["documento_id"] in {"leguia_1921", "alberto_fujimori_1991"}]
    with (datos / "comparacion_competencia.csv").open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=list(filas[0]), lineterminator="\n")
        escritor.writeheader()
        escritor.writerows(filas)
    huellas = [{"archivo_template": p.relative_to(TEMPLATE).as_posix(),
                "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
               for p in sorted(TEMPLATE.rglob("*")) if p.is_file()]
    originales = json.loads((RAIZ / "data/documentos.json").read_text(encoding="utf-8"))
    unidades = {}
    with (RAIZ / "data/unidades.csv").open(encoding="utf-8") as archivo:
        unidades = {r["unidad_id"]: r for r in csv.DictReader(archivo)
                    if r["unidad_id"] in {"u11860", "u14275", "u00126"}}
    fuentes = [{"unidad_id": u["unidad_id"], "documento_id": u["documento_id"],
                "pagina_inicio": int(u["pagina_inicio"]), "texto_unidad": u["texto"],
                "url_pdf": next(d["url_pdf"] for d in originales if d["documento_id"] == u["documento_id"])}
               for u in unidades.values()]
    (datos / "procedencia.json").write_text(json.dumps({"commit_investigacion": "72fcac7d3ea06b737c3a3f35f37b818411c6dead",
        "huellas_template_original": huellas, "fuentes_fragmentos": fuentes, "facsimiles": facsimiles}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print("Preámbulo, logo y procedencia preparados. Sin compilación local.")


if __name__ == "__main__":
    main()
