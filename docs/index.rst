django-admin-actions
####################

`django-admin-actions` is a small library to simplify the creation of custom
:external+django:std:doc:`admin actions <ref/contrib/admin/actions>`.

Creating one-off admin actions isn't difficult. You write a function and put
that function name into your list of `actions`. If you are only writing the
occasional action, or every action you write is unique, this library won't be of
much help for you.

If you find yourself building the same kinds of actions in multiple admins or
projects, though, `django-admin-actions` is here for you. This library is meant
to reduce the boilerplate necessary when writing similar kinds of actions over
and over. For example, you might write multiple actions to queue different
Celery tasks for different models. Using `django-admin-actions`, you can reduce
most of that work into just writing the tasks you need to run without worrying
about the action side of the problem.

This library provides the :py:class:`~admin_actions.lib.AdminActionBaseClass`
which can be extended to create custom admin actions. Also provided are two
ready-to-use action classes:
:py:class:`~admin_actions.actions.simple.SimpleAction` and
:py:class:`~admin_actions.actions.queue_celery.QueueCeleryAction`. You can
use these implementations directly, extend them for your own customizations, or
use them as examples for creating your own action classes.

.. toctree::
    :maxdepth: 1
    :caption: Contents:

    Example library usage <example_library_usage>
    Example custom actions <example_custom_actions>
    Library module reference <modules>

Installation
------------

To install ``django_admin_actions``, you'll use
``pip install django_admin_actions`` or add ``django_admin_actions`` to your
``pyproject.toml`` or ``requirements.txt``. You don't need to add anything to
your ``INSTALLED_APPS`` to use this library.

Contributing
------------

Thanks for wanting to contribute to ``django_admin_actions``! Contributions are
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
3. Test your changes.
4. Commit your changes, passing all checks.
5. Push to the branch.
6. Create a pull request.
