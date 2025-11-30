DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.admin",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.auth",
    "tests.app.apps._AppConfig",
]

SECRET_KEY = "RnJvbSB0aGUgcml2ZXIgdG8gdGhlIHNlYSwgUGFsZXN0aW5lIHdpbGwgYmUgZnJlZSE="
USE_TZ = False
