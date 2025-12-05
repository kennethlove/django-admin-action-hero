from action_hero import __version__

project = "django-admin-action-hero"
author = "klove"
copyright = "2025-%Y, klove"
version = __version__
release = __version__

exclude_patterns = ["dist"]

extensions = [
    "sphinx_copybutton",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",
    "sphinx.ext.napoleon",
]

html_theme = "alabaster"

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
    "exclude-members": "__weakref__, _meta",
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
autodoc_typehints = "description"  # options: signature, description, both, none
autodoc_typehints_description_target = (
    "all"  # options: all, documented, documented_params
)
autodoc_typehints_format = "short"  # options: full-qualified, short
autodoc_preserve_defaults = True

# copybutton settings
copybutton_exclude = ".linenos, .gp, .go"

html_theme_options = {
    "description": "Easily add bulk actions to Django admin",
    "github_banner": True,
    "github_button": False,
    "github_repo": "django-admin-action-hero",
    "github_user": "kennethlove",
}

# intersphinx settings
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "django": ("https://docs.djangoproject.com/en/4.2", None),
    "celery": ("https://docs.celeryq.dev/en/stable/", None),
}
intersphinx_disabled_reftypes = ["*"]

# napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_type_aliases = {
    "Condition": "action_hero.lib.Condition",
    "Function": "action_hero.lib.Function",
}
