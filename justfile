build-html:
    @echo "Building HTML documentation..."
    uv run sphinx-build -M html docs dist

dev-docs:
    @echo "Starting live-reload server for documentation..."
    uv run sphinx-autobuild --open-browser docs dist/html
