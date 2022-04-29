# Documentation: https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

needs_sphinx = '4.4.0'

project = "Monster Girl Dreams"
copyright = '2017-2021, Threshold'
author = 'Threshold'
release = 'v24'

# -- General configuration ---------------------------------------------------

extensions = [
        'sphinx_rtd_theme',
        'notfound.extension',
        'sphinx_search.extension',
        'sphinx.ext.imgmath',
        'sphinx_tabs.tabs'
]

# Add any paths that contain templates here, always relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = '.rst'
source_encoding = 'utf-8-sig'
master_doc = 'Homepage'
# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    # logo_only ensures this shows only the logo, with no title text.
    'logo_only': True,
    'collapse_navigation': True,
    'navigation_depth': 4,
}

html_context = {
    # "display_github": True, # Integrate GitHub
    # "github_user": "MyUserName", # Username
    # "github_repo": "MyDoc", # Repo name
    # "github_version": "master", # Version
    # "conf_py_path": "/source/", # Path in the checkout to the docs root
}

notfound_urls_prefix = ''

html_logo = 'img/banner.png'

# Custom static files are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/custom.css'
]

html_js_files = [
]

htmlhelp_basename = 'MonsterGirlDreamsDoc'
