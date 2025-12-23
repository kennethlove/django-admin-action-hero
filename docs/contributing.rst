Contributing to django-admin-action-hero
########################################

Thank you for wanting to contribute to ``django-admin-action-hero``!
Contributions are *always* welcome [#]_! Here's how you can help:

* Improve documentation.
* Report bugs via GitHub issues.
* Suggest new features via GitHub discussions.
* Submit pull requests with bug fixes or new features (once approved).

Please ensure that you follow these steps before you start working on your
contribution:

1. Fork the repository. All following commands are assumed to be run in your
   fork's directory.
2. Set up git pre-commit hooks. (I recommend `prek <prek_>`_ for this)
3. Create a virtual environment and install dependencies. (I recommend using
   `uv <uv_>`_.)
4. Run tests to ensure everything is working.

Once you have everything working, follow these steps to submit your changes:

1. Create a feature branch.
2. Make your changes.
3. Test your changes.
4. Make sure the documentation is up to date and correct.
5. Commit your changes, making sure all checks pass.
6. Push to your branch.
7. Create a pull request.

Maintainers will want to review your changes, so please be patient. They may
request changes or improvements before merging. Once everything is approved,
your changes will be merged and will appear in the next appropriate release.

Contributing to code
---------------------

If you'd like to contribute code changes, please follow the steps outlined above
to set up your development environment. Bug fixes and new features are both
welcome but both should be accompanied by a `discussion <discussion_>`_ or an
`issue <issue_>`_.

When making code changes, please ensure that:

* Your code follows the existing style and conventions.
* You include appropriate docstrings and type hints. Make sure to
  document any new public functions, classes, or methods.
* You write tests that cover your changes. All tests must pass, of course.
  Try to cover your new code as much as possible. Tests should cover all
  branches. Follow existing test patterns, including fixtures.

You can run the tests using ``uv run pytest``.

Contributing to documentation
-----------------------------

Improving documentation is a great way to contribute, especially if you're new
to open source. You can help by:

* Fixing typos or grammatical errors.
* Clarifying confusing sections.
* Adding examples or tutorials.
* Updating outdated information.

To contribute to the documentation, simply follow the same steps as for code
changes, but focus on the documentation files located in the ``docs/``
directory.

You'll want to make sure you have the packages needed to build the docs. You can
install them using:

.. code-block:: sh

    uv pip install --group docs

You can use the provided `justfile <justfile_>`_ to easily build the
documentation locally:

.. code-block:: sh

    just build-docs

If you'd like to run a local server to view the documentation as you make
changes, you can use:

.. code-block:: sh

    just dev-docs

Release Process
---------------

.. admonition:: Note

   These steps are mostly for maintainers, but it's good to know how releases
   are made. They are written mostly for my own reference and may not be as
   complete as the rest of the documentation.

These are the steps to create a new release of ``django-admin-action-hero``:

1. All checks (tests, linters, etc.) are passing.
2. All involved pull requests are merged to ``main``.
3. The version in ``pyproject.toml``, ``docs/conf.py``, and
   ``action_hero/__init__.py`` is incremented appropriately.
4. The changelog is updated with `git-cliff <git-cliff_>`_.
5. Tag the release in git. ``git tag X.Y.Z -m "Release X.Y.Z"``
6. Push tags to repo. ``git push --tags``. This will also trigger a build on
   GitHub Actions that will publish the new version to TestPyPI and then PyPI.
7. Create a release on GitHub using the pushed tag.

.. rubric:: Footnotes

.. [#] Contributions are welcome from everyone. By contributing, you agree that
   your contributions will be licensed under the same license as
   ``django-admin-action-hero`` (`Apache 2.0 License <apache_>`_).

   Also, please note that all contributions are subject to review and may not
   be accepted if they do not align with the project's goals or standards.

.. _prek: https://github.com/j178/prek
.. _uv: https://docs.astral.sh/uv/
.. _discussion: https://github.com/kennethlove/django-admin-action-hero/discussions
.. _issue: https://github.com/kennethlove/django-admin-action-hero/issues
.. _justfile: https://just.systems/man/en/
.. _git-cliff: https://github.com/orhun/git-cliff
.. _apache: https://www.apache.org/licenses/LICENSE-2.0.html
