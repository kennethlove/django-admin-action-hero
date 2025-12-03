import os

def pytest_configure(config):
    if os.getenv("CI") != "true":
        # Local only — try loading pytest_sugar
        try:
            config.pluginmanager.import_plugin("pytest_sugar")
        except ImportError:
            # Plugin not installed locally — ignore silently
            pass
