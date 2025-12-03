import os

def pytest_configure(config):
    # Disable pytest-sugar automatically in CI environments
    if os.getenv("CI") == "true":
        config.pluginmanager.set_blocked("pytest_sugar")
