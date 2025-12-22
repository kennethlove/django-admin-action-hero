Contributing to django-admin-action-hero
########################################

Thank you for wanting to contribute to ``django-admin-action-hero``!
Contributions are _always_ welcome (even if they may not all be accepted).
Here's how you can help:

* Improve documentation.
* Report bugs via GitHub issues.
* Suggest new features via GitHub discussions.
* Submit pull requests with bug fixes or new features (once approved).

If your contribution requires code changes, please ensure that you follow these
steps:

1. Fork the repository.
2. Set up git pre-commit hooks. (I recommend
   `prek <https://github.com/j178/prek>`__ for this)
3. Create a virtual environment and install dependencies. (I recommend using
   `uv <https://docs.astral.sh/uv/>`__.)
4. Run tests to ensure everything is working. You'll use ``pytest`` for writing
   and running tests.

Once you have everything working, follow these steps to submit your changes:

1. Create a feature branch.
2. Make your changes.
   Changes should follow the existing code style, include docstrings, and be
   type-hinted.
3. Test your changes.
   All tests must pass, of course. Try to cover your new code as much as
   possible. Tests should cover all branches.
4. Commit your changes, passing all checks.
5. Update the changelog with `git-cliff <https://github.com/orhun/git-cliff>`__.
6. Make sure the documentation is up to date and correct.
7. Push to the branch.
8. Create a pull request.

Maintainers will want to review your changes, so please be patient. They may
request changes or improvements before merging. Once everything is approved,
your changes will be merged and will appear in the next appropriate release.

Release Process
---------------

1. All checks (tests, linters, etc.) are passing.
2. All involved pull requests are merged to ``main``.
3. The version in ``pyproject.toml``, ``docs/conf.py``, and ``action_hero/__init__.py`` is
   incremented appropriately.
4. The changelog is updated with
   `git-cliff <https://github.com/orhun/git-cliff>`__.
5. Tag the release in git. ``git tag X.Y.Z -m "Release X.Y.Z"``
6. Push tags to GitHub. ``git push --tags``. This will also trigger a build on
   GitHub Actions that will publish the new version to TestPyPI and then PyPI.
7. Create a release on GitHub using the pushed tag.
