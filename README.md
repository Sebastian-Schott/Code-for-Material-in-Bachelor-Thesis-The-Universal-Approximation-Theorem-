# Code-for-Material-in-Bachelor-Thesis-The-Universal-Approximation-Theorem-
This repository contains my own code developed for my bachelor thesis "The Universal Approximation Theorem". It includes mainly Python scripts and TikZ files used to generate material, figures, and visualizations for the thesis.

Anyone is free to use the provided code as long as credit is given (referenced).

TikZ Code

Each .tex file contains the raw source code for a TikZ image. They cannot be compiled as standalone LaTeX files and must be included (with \input{FILENAME.tex}) in a properly formatted LaTeX document.
Overall, for the TikZ code I used the libraries:
\usepackage{tikz}
\usetikzlibrary{
  decorations.pathmorphing,
  arrows.meta,
  calc,
  positioning,
  shapes.misc,
  patterns,
  decorations.pathreplacing
}

All TikZ material in my thesis:
- Figure 1.1: network_intro.tex
- Figure 1.2: neuron_calc.tex
- Figure 1.3 (left): network_example1.tex
- Figure 1.3 (right): network_example2.tex
- Figure 3.1: network_depth.tex
- Figure 4.1: interpolation_gap.tex
- Figure 5.1: network_mulitoutput.tex


Python Code

In my thesis I used SVG files created with Python. It is important to note that several libraries must be installed to run the code. In the repository root (current directory), run in the terminal:
pip install <MODULE_NAME>

<MODULE_NAME> are the library names, e.g. numpy, matplotlib, scikit-learn, etc.
WARNING: Python itself must be installed on your system in order to run the code. In some cases, it may be necessary (or recommended) to create a virtual environment before installing the required libraries.

All Python material in my thesis:
- Figure 5.2: manifold.py
- Figure 5.3 + 5.4: The code can be found in the Jupyter notebook swiss_roll_notebook.ipynb, which will generate the SVG files if the relevant code cells are uncommented.

To my Jupyter notebook:
Its purpose is to implement a neural network which tries to approximate a function, which unfolds the Swiss Roll in the 2 dimensional space.
It runs on python code and is depended of some libraries, which need to be installed first. List of required libraries:
- numpy
- matplotlib
- IPython
- mpl_toolkits
- scikit-learn
- warnings

Alternatively, one can use the online Jupyter Notebook service by uploading the notebook there, which avoids the need for local installation.
