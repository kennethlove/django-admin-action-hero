project = "django-admin-action-hero"
author = "klove"
copyright = "2025-%Y, klove"
version = "0.1.0"
release = "0.1.0"

exclude_patterns = ["dist"]

extensions = [
    "sphinx_copybutton",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.extlinks",
]

html_theme = "furo"

# apidoc settings
apidoc_modules = [
    {
        "path": "../src/action_hero/",
        "destination": "api/",
        "module_first": True,
        "separate_modules": True,
    }
]

# autodoc settings
autodoc_class_signature = "separated"
autodoc_default_options = {
    "exclude-members": "__weakref__,_meta",
    "ignore-module-all": False,
    "private-members": "__init__, __call__",
    "show-inheritance": True,
    "special-members": "__init__, __call__",
}
autodoc_inherit_docstrings = True
autodoc_type_aliases = {
    "Function": "action_hero.lib.Function",
    "Condition": "action_hero.lib.Condition",
}
autodoc_typehints = "description"  # signature, description, both, none
autodoc_typehints_description_target = "all"  # all, documented, documented_params
autodoc_typehints_format = "short"  # full-qualified, short
autodoc_preserve_defaults = False

# copybutton settings
copybutton_exclude = ".linenos, .gp, .go"

# intersphinx settings
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "django": ("https://docs.djangoproject.com/en/4.2", None),
    "celery": ("https://docs.celeryq.dev/en/stable/", None),
}
intersphinx_disabled_reftypes = ["*"]
