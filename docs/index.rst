django-admin-action-hero
########################

`django-admin-action-hero` is a small library to simplify the creation of custom
:external+django:std:doc:`admin actions <ref/contrib/admin/actions>`.

Creating one-off admin actions isn't difficult. You write a function and put
that function name into your list of `actions`. If you are only writing the
occasional action, or every action you write is unique, this library won't be of
much help for you.

If you find yourself building the same kinds of actions in multiple admins or
projects, though, `django-admin-action-hero` is here for you. This library is meant
to reduce the boilerplate necessary when writing similar kinds of actions over
and over. For example, you might write multiple actions to queue different
Celery tasks for different models. Using `django-admin-action-hero`, you can reduce
most of that work into just writing the tasks you need to run without worrying
about the action side of the problem.

This library provides the :py:class:`~action_hero.lib.AdminActionBaseClass`,
which can be extended to create custom admin actions. Also provided are two
ready-to-use action classes:
:py:class:`~action_hero.actions.simple.SimpleAction` and
:py:class:`~action_hero.actions.queue_celery.QueueCeleryAction`. You can
use these implementations directly, extend them for your own customizations, or
use them as examples for creating your own action classes.

.. toctree::
    :maxdepth: 1
    :caption: Contents:

    How to use existing action classes <example_library_usage>
    How to create your own action classes <example_custom_actions>
    Library module reference <api/modules>

Installation
------------

To install ``django-admin-action-hero``, you'll use
``pip install django-admin-action-hero`` or add ``django-admin-action-hero`` to your
``pyproject.toml`` or ``requirements.txt``. You don't need to add anything to
your ``INSTALLED_APPS`` to use this library.

Contributing
------------

Thanks for wanting to contribute to ``django-admin-action-hero``! Contributions are
always welcome (even if they may not all be accepted). Here's how you can help:

* Improve documentation.
* Report bugs via GitHub issues.
* Suggest new features via GitHub discussions.
* Submit pull requests with bug fixes or new features (once approved).

If your contribution requires code changes, please ensure that you follow these
steps:

1. Fork the repository.
2. Set up git pre-commit hooks.
   (I recommend `prek <https://github.com/j178/prek>`__ for this)
3. Create a virtual environment and install dependencies.
   (I recommend using `uv <https://docs.astral.sh/uv/>`__.)
4. Run tests to ensure everything is working.
   You'll use `pytest <https://docs.pytest.org/en/stable/>`__ for writing and
   running tests.

Once you have everything working, follow these steps to submit your changes:

1. Create a feature branch.
2. Make your changes.
   Changes should follow the existing code style, include docstrings, and be
   type-hinted.
3. Test your changes.
   All tests must pass, of course. Try to cover your new code as much as
   possible. Tests should cover all branches.
4. Commit your changes, passing all checks.
5. Make sure the documentation is up to date and correct.
6. Push to the branch.
7. Create a pull request.

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
