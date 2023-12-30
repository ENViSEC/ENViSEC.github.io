# Configuration file for the Sphinx documentation builder.
# -- Project information
project = 'Kristiania-HPC'
copyright = '2024, SEIT, Kristiania University College'
author = 'Guru Prasad Bhandari'
release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    "sphinx.ext.napoleon",
    'sphinx_rtd_theme',
    'myst_parser',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
