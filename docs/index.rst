django-admin-actions
####################

`django-admin-actions` is a small library to simplify the creation of custom admin actions.
Creating admin actions isn't necessarily difficult, but often they require some boilerplate
code, especially when dealing with long-running tasks or message queuing.

This library provides the :py:class:`~admin_actions.lib.AdminActionBaseClass` which can be
extended to create custom admin actions. Also provided are two ready-to-use action classes:
:py:class:`~admin_actions.actions.simple.SimpleAdminAction` and
:py:class:`~admin_actions.actions.queue_celery.CeleryQueueAdminAction`. You can use these
implementations directly, extend them for your own customizations, or use them as examples
for creating your own action classes.

.. toctree::
    :maxdepth: 1
    :caption: Contents:

    Example Library Usage <example_usage>
    Library modules<modules>
