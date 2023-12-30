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

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': True,
    'display_version': False,
    'navigation_depth': 3,
    'includehidden': True,
    'titles_only': False,
    'style_external_links': False,
    'prev_next_buttons_location': 'bottom',
    'style_nav_header_background': '#2980B9',
    'logo_only': True,
}
