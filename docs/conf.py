project = "django-admin-actions"
author = "klove"
copyright = "2025-%Y, klove"
version = "1.0.0"
release = "1.0.0"

extensions = [
    "sphinx.ext.apidoc",
    "sphinx.ext.intersphinx",
]
apidoc_modules = [
    {
        "path": "../src/admin_actions/",
        "destination": "dist/",
        "apidoc_module_first": True,
    }
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "django": ("https://docs.djangoproject.com/en/4.2", None),
    "celery": ("https://docs.celeryq.dev/en/stable/", None),
}
intersphinx_disabled_reftypes = ["*"]

exclude_patterns = ["dist"]
