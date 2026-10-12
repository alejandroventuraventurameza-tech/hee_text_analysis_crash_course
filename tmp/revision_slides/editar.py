from pathlib import Path
import re

p=Path('slides/3_content.tex')
s=p.read_text(encoding='utf-8')

def frame(label,body,title=None):
    global s
    pattern=r'\\begin\{frame\}\[([^\]]*label='+re.escape(label)+r'[^\]]*)\]\{([^\n]+)\}\n(.*?)\\end\{frame\}'
    m=re.search(pattern,s,re.S)
    assert m,label
    note=re.search(r'  \\note\{.*\}\n',m[3],re.S)
    new='\\begin{frame}['+m[1]+']{'+(title or m[2])+'}\n'+body.strip()+'\n'+(note[0] if note else '')+'\\end{frame}'
    s=s[:m.start()]+new+s[m.end():]

frame('apertura',r'''
  \begin{columns}[T,onlytextwidth]
    \begin{column}{0.48\textwidth}
      {\Large ¿Cómo estudiar cientos de discursos?\par}
      \vspace{0.5cm}
      Propón un procedimiento.\par
      \vspace{0.3cm}
      ¿Qué contarías?\par
      ¿Qué comprobarías leyendo?
    \end{column}
    \begin{column}{0.45\textwidth}
      \centering
      \includegraphics[height=5.1cm]{28_07_1921_leguia_pagina1.png}\par
      \fuente{Mensaje de 1921, p. 1. Archivo del Congreso.}
    \end{column}
  \end{columns}
''','Los discursos como fuente histórica')

frame('pregunta',r'''
  {\Large ¿Cómo se describe la intervención económica del Estado?\par}
  \vspace{0.45cm}
  Compararemos palabras y leeremos los pasajes donde aparecen.\par
  \vspace{0.4cm}
  \textbf{Lo declarado en un discurso}\par
  Para comprobar lo que se ejecutó necesitamos otras fuentes.\par
  \vspace{0.4cm}
  Tu conclusión debe unir un resultado numérico y evidencia textual.
''','Intervención económica en los discursos')

frame('historia',r'''
  \textbf{Análisis de contenido}\par
  Categorías y reglas para interpretar. Berelson, 1952.\par
  \vspace{0.3cm}
  \textbf{Conteos y diccionarios}\par
  Comparar palabras a escala. General Inquirer.\par
  \vspace{0.3cm}
  \textbf{Modelos de lenguaje}\par
  Clasificar mediante instrucciones. Gilardi y coautores, 2023.\par
  \vspace{0.35cm}
  ¿Qué aporta cada enfoque a nuestra pregunta?
  \fuente{\parencite{berelson1952,inquirer,gilardi2023}}
''')

frame('roles',r'''
  \textbf{Empresario}\par
  El Estado posee y controla la producción.\par
  \vspace{0.4cm}
  \textbf{Regulador}\par
  Establece reglas generales y supervisa mercados.\par
  \vspace{0.4cm}
  \textbf{Facilitador}\par
  Promueve actividades de forma selectiva, sin requerir propiedad estatal.\par
  \vspace{0.4cm}
  ¿Qué instrumento encuentras en A y B?
  \fuente{Categorías del proyecto. También distingue asistencial y no aplica.}
''')

frame('seleccion',r'''
  \begin{columns}[T,onlytextwidth]
    \begin{column}{0.31\textwidth}
      \centering
      \textbf{Leguía}\par
      1920 y 1921\par\vspace{0.15cm}
      \includegraphics[height=3.65cm]{28_07_1920_leguia_pagina1.png}
    \end{column}
    \begin{column}{0.31\textwidth}
      \centering
      \textbf{Velasco}\par
      1969 y 1970\par\vspace{0.15cm}
      \includegraphics[height=3.65cm]{28_07_1969_velasco_pagina1.png}
    \end{column}
    \begin{column}{0.31\textwidth}
      \centering
      \textbf{Alberto Fujimori}\par
      1991 y 1992\par\vspace{0.15cm}
      \includegraphics[height=3.65cm]{28_07_1991_alberto_fujimori_pagina1.png}
    \end{column}
  \end{columns}
  \vspace{0.2cm}
  Todos son mensajes del 28 de julio. Audiencias y ocasiones difieren.
  \fuente{Primera página de 1920, 1969 y 1991. Archivo oficial del Congreso; copias de \texttt{v1.0-ccl}. Regla de selección anterior al conteo.}
''')

frame('tasas',r'''
  \renewcommand{\arraystretch}{1.25}
  \begin{tabular}{@{}lrrr@{}}
    \textbf{Mensaje} & \textbf{Menciones} & \textbf{Palabras} & \textbf{Por 1.000}\\
    Leguía 1921 & 2 & 4.527 & 0,442\\
    Fujimori 1991 & 11 & 23.348 & 0,471\\
  \end{tabular}\par
  \vspace{0.12cm}
  \centering
  \begin{tikzpicture}
    \begin{axis}[
      xbar,xmin=0,xmax=0.6,width=0.92\textwidth,height=3.25cm,
      symbolic y coords={Leguía 1921,Fujimori 1991},ytick=data,
      enlarge y limits=0.7,bar width=11pt,axis lines*=left,
      xmajorgrids=true,grid style={draw=UWGrayL1},
      tick label style={font=\footnotesize},label style={font=\footnotesize},
      xticklabel style={/pgf/number format/use comma},
      xlabel={Menciones por 1.000 palabras}]
      \addplot[fill=UWGoldL3,draw=UWBlack] coordinates {
        (0.4417936823503424,{Leguía 1921})
        (0.4711324310433442,{Fujimori 1991})
      };
    \end{axis}
  \end{tikzpicture}\par
  \raggedright
  ¿Qué cambió al considerar la extensión?
  \fuente{Forma exacta: competencia. Datos didácticos; tasas redondeadas.}
''')

frame('recuperacion',r'''
  \textbf{Si perdiste una variable}\par
  Ejecuta Preparación y después Recuperación de la comparación.\par
  \vspace{0.5cm}
  \textbf{Si reiniciaste la sesión}\par
  Sigue el mismo orden: Preparación y Recuperación.\par
  \vspace{0.5cm}
  Antes de continuar, comprueba tu tabla y su denominador.\par
  \vspace{0.2cm}
  Si el gráfico tarda, conserva la tabla para discutir el resultado.
''')

frame('polisemia',r'''
  \begin{columns}[T,onlytextwidth]
    \begin{column}{0.47\textwidth}
      \textbf{Leguía, 1921}\par
      \begin{quote}
        \enquote{cuya competencia se ha evidenciado en la campaña que, para extirpar la fiebre amarilla, desarrollóse en el norte de la República}
      \end{quote}
      \fuente{\texttt{u00126}, p. 11.}
    \end{column}
    \begin{column}{0.47\textwidth}
      \textbf{Alberto Fujimori, 1991}\par
      \begin{quote}
        \enquote{el que se dará bajo condición de competencia y de mercado.}
      \end{quote}
      \fuente{\texttt{u14275}, p. 10.}
    \end{column}
  \end{columns}
  \vspace{0.5cm}
  ¿Qué significa competencia en cada pasaje?\par
  ¿Qué cambia en tu interpretación de los conteos?
''')

frame('entrega',r'''
  \textbf{Resultado}\par
  Una tabla o gráfico con denominador y una conclusión.\par
  \vspace{0.3cm}
  \textbf{Evidencia}\par
  Dos fragmentos originales con documento y página.\par
  \vspace{0.3cm}
  \textbf{Alcance}\par
  Una limitación y su consecuencia; una aplicación a tu carrera.\par
  \vspace{0.35cm}
  Conserva tu predicción, el cambio de código y el contraste manual.\par
  \fuente{Entrega individual, sin calificación.}
''','Tu análisis en el notebook')

frame('cierre',r'''
  \begin{enumerate}
    \item Guarda tu copia con respuestas y salidas visibles.
    \item Descarga el notebook.
    \item Súbelo a la carpeta de Drive indicada y comprueba la recepción.
  \end{enumerate}
  \vspace{0.3cm}
  {\small\texttt{apellido\_nombre\_analisis\_textual.ipynb}\par}
  \vspace{0.5cm}
  ¿Qué afirmación todavía no permiten tus datos?
''')

# Las tablas y ecuaciones terminan su párrafo; el texto no debe fluir a su lado.
s=s.replace('\\end{tabular}\n','\\end{tabular}\\par\n')
s=s.replace('\\end{verbatim}\n','\\end{verbatim}\\par\n')
s=s.replace('  El denominador incluye las palabras ocultas solo del ranking.','  El denominador incluye las palabras ocultas solo del ranking.\\par')
s=s.replace('  \\textbf{Al minuto 90:} resultado numérico y dos fragmentos identificados.','  Antes del contraste: resultado numérico y dos fragmentos identificados.')
s=s.replace('  ¿Coincides con el modelo? Justifica tu decisión con el instrumento descrito y el contexto.','  ¿Coincides con el modelo?\\par\n  Justifica tu decisión con el instrumento descrito y el contexto.')
# Actualizar la nota de comparación; ya no se reserva el gráfico al apéndice.
s=s.replace('Mostrar el gráfico en el notebook solo después de la tabla.','El gráfico proyectado y el notebook usan los mismos valores; mostrar después de las predicciones y la ejecución.')
p.write_text(s,encoding='utf-8',newline='\n')
print('Contenido actualizado; 34 frames conservados.')
