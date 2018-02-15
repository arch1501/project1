#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
from io import open
print(sys.version)

oldFil=os.path.join("build", "latex", "ibpsa_project1_workplan_draft.tex")
newFil=os.path.join("build", "latex", "ibpsa_project1_workplan_draft.tex-new")

def freplace(old, new):
    with open(oldFil, mode="rt", encoding="utf-8") as fin, open(newFil, mode="wt", encoding="utf-8") as fout:
        for line in fin:
            fout.write(line.replace(old, new))
    os.remove(oldFil)
    os.rename(newFil, oldFil)


freplace('\\tableofcontents', '')
freplace('\\phantomsection\\label{index::doc} \\clearpage', '')
#replace('\def\sphinxdocclass{report}',
#        '%\def\sphinxdocclass{report}')
freplace('sphinxmanual',
        'report')
freplace('\documentclass[letterpaper,11pt, openany]{sphinxmanual}',
        '\documentclass[letterpaper,11pt,english]{report}')
freplace('\maketitle',
        '\input{../../source/titlepage.tex} \setcounter{page}{2}')
freplace('\phantomsection\label{index::doc}',
        '\phantomsection\label{index::doc} \clearpage')
freplace('\subsection{',
        '\subsubsection{')
freplace('\section{',
        '\subsection{')
freplace('\chapter{',
        '\section{')
#freplace('\\begin{thebibliography}{1}',
#        '''\\chapter{References}
#\\begin{thebibliography}{1}''')
