# Configuration file for the Sphinx documentation builder.

# -- Project information
import sphinx_theme


project = 'Kristiania-HPC'
copyright = '2022, Kristiania University College'
author = 'Guru Prasad Bhandari'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
# html_theme = 'renku'
# html_theme = 'nature'
# html_theme = 'stanford_theme'
# html_theme_path = [sphinx_theme.get_html_theme_path('stanford-theme')]

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_logo = 'images/logo.png'

html_theme_options = {
    'logo_only': False,
    'display_version': False,
    # 'prev_next_buttons_location': 'both',
    # 'style_external_links': True,
    # 'style_nav_header_background': '#f5f',
    # 'github_url': 'https://kristiania-hpc.github.io/',
}
