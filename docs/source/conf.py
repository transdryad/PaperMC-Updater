# Configuration file for the Sphinx documentation builder.
import sphinx_pdj_theme
# -- Project information

project = 'PaperMC Updater'
copyright = '2025, Hazel Viswanath'
author = 'Hazel Viswanath'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_pdj_theme',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx-pdj-theme'
html_theme_path = [sphinx_pdj_theme.get_html_theme_path()]

# -- Options for EPUB output
epub_show_urls = 'footnote'
