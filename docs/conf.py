project = "django-admin-action-hero"
author = "klove"
copyright = "2025-%Y, klove"
version = "0.1.0"
release = "0.1.0"

extensions = [
    "sphinx.ext.apidoc",
    "sphinx.ext.intersphinx",
]
apidoc_modules = [
    {
        "path": "../src/action_hero/",
        "destination": "api/",
        "apidoc_module_first": True,
        "apidoc_separate_modules": True,
    }
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "django": ("https://docs.djangoproject.com/en/4.2", None),
    "celery": ("https://docs.celeryq.dev/en/stable/", None),
}
intersphinx_disabled_reftypes = ["*"]

exclude_patterns = ["dist"]
