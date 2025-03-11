# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Add the package directory to sys.path
# import os
# import sys
# sys.path.insert(0, os.path.abspath('..'))  # Adjust the path as needed

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MIDRC-REACT'
copyright = '2025, MIDRC'
author = 'MIDRC'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',        # Extracts documentation from docstrings
    'sphinx.ext.autosummary',    # Generates summary tables for modules, classes, functions, etc.
    'sphinx.ext.napoleon'        # Supports Google and NumPy style docstrings
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': -1,
}

# html_theme = 'furo'

html_static_path = ['_static']


# Include __init__() in the documentation
napoleon_include_init_with_doc = True

# Use :ivar: style for class attributes so they’re only listed once in the Attributes section.
napoleon_use_ivar = True

def skip_member(app, what, name, obj, skip, options):
    if name in ("staticMetaObject", "FlowStyleListDumper"):
        return True
    return skip

def setup(app):
    app.connect("autodoc-skip-member", skip_member)


