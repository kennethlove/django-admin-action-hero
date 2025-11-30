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
:py:class:`~admin_actions.actions.simple.SimpleAdminAction` and
:py:class:`~admin_actions.actions.queue_celery.QueueCeleryAction`. You can
use these implementations directly, extend them for your own customizations, or
use them as examples for creating your own action classes.

.. toctree::
    :maxdepth: 1
    :caption: Contents:

    Example library usage <example_library_usage>
    Example custom actions <example_custom_actions>
    Library module reference <modules>
