# django-admin-action-hero

`django-admin-action-hero` is a library designed to make it easier to create custom
repetitive admin actions for Django's admin interface. It provides a simple way
to create classes that encapsulate admin actions, allowing for better code reuse
and organization.

* [Read the full docs](https://django-admin-action-hero.readthedocs.io/)
* [Want to contribute?](CONTRIBUTING.md)

## Installation

To install `django-admin-action-hero`, you'll use `pip install django-admin-action-hero`
or add `django-admin-action-hero` to your `pyproject.toml` or `requirements.txt`.
You don't need to add anything to your `INSTALLED_APPS`.

## Quick example

An example of how to use `django-admin-action-hero` to create a simple admin action:

```py
from django.contrib import admin

from action_hero.actions import SimpleAction


def my_admin_function(item_pk):
    # Your admin action logic here
    pass


class MyAdmin(admin.ModelAdmin):
    actions = [
        SimpleAction(
            my_admin_function,
            name="my_custom_action",
        ),
    ]
```

Your `MyAdmin` class now has a custom admin action called "my_custom_action"
that executes `my_admin_function` for each selected item.
