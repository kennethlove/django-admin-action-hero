django-admin-action-hero
########################

`django-admin-action-hero` is a small library to simplify the creation of custom
:external+django:std:doc:`admin actions <ref/contrib/admin/actions>`.

Creating one-off admin actions isn't difficult. You write a function and put
that function name into your list of `actions`. If you are only writing the
occasional action, or every action you write is unique, this library won't be of
much help for you.

If you find yourself building the same kinds of actions in multiple admins or
projects, though, `django-admin-action-hero` is here for you. This library is
meant to reduce the boilerplate necessary when writing similar kinds of actions
over and over. For example, you might write multiple actions to queue different
Celery tasks for different models. Using `django-admin-action-hero`, you can
reduce most of that work into just writing the tasks you need to run without
worrying about the action side of the problem.

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

    Want to contribute? <contributing>

Installation
------------

To use ``django-admin-action-hero``, you need to install it into your Python
environment. You can do this using either ``uv``, ``poetry``, ``pip``, or any
package manager you prefer. The following examples show how to add the library
as a dependency in your project.

.. tabs::

    .. tab:: pyproject.toml

        .. tabs::

            .. tab:: uv

                .. parsed-literal::

                    [dependencies]
                    django-admin-action-hero = "|version|"

            .. tab:: poetry

                .. parsed-literal::

                    [tool.poetry.dependencies]
                    django-admin-action-hero = "|version|"


    .. tab:: requirements.txt

        .. parsed-literal::

            django-admin-action-hero = "|version|"

    .. tab:: uv

        .. parsed-literal::

            uv add django-admin-action-hero=="|version|"

    .. tab:: pip

        .. parsed-literal::

            pip install django-admin-action-hero=="|version|"

``django-admin-action-hero`` does not require any additional setup after
installation. You can start using the provided action classes or create your own
custom action classes right away.
