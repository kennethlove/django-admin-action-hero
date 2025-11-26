project = "django-admin-actions"
author = "klove"
copyright = "2025-%Y, klove"
version = "1.0.0"
release = "1.0.0"

extensions = [
    "sphinx.ext.apidoc",
]
apidoc_modules = [
    {
        "path": "../src/admin_actions/",
        "destination": "dist/",
        "apidoc_module_first": True,
    }
]

exclude_patterns = ["dist"]
