# django_admin_actions

`django_admin_actions` is a library designed to make it easier to create custom
repetitive admin actions for Django's admin interface. It provides a simple way
to create classes that encapsulate admin actions, allowing for better code reuse
and organization.

[Read the full docs](https://django-admin-actions.readthedocs.io/)

## Installation

To install `django_admin_actions`, you'll use `pip install django_admin_actions`
or add `django_admin_actions` to your `pyproject.toml` or `requirements.txt`.
You don't need to add anything to your `INSTALLED_APPS`.

## Usage

An example of how to use `django_admin_actions` to create a simple admin action:

```py
from django.contrib import admin

from admin_actions.actions import SimpleAction

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

## Contributing

Thanks for wanting to contribute to `django_admin_actions`! Contributions are
always welcome (even if they may not all be accepted). Here's how you can help:

* Improve documentation.
* Report bugs via GitHub issues.
* Suggest new features via GitHub discussions.
* Submit pull requests with bug fixes or new features (once approved).

If your contribution requires code changes, please ensure that you follow these
steps:

1. Fork the repository.
2. Set up git pre-commit hooks. (I recommend [`prek`](https://github.com/j178/prek) for this)
3. Create a virtual environment and install dependencies. (I recommend using [`uv`](https://docs.astral.sh/uv/).)
4. Run tests to ensure everything is working. You'll use `pytest` for writing and running tests.

Once you have everything working, follow these steps to submit your changes:

1. Create a feature branch.
2. Make your changes.
3. Test your changes.
4. Commit your changes, passing all checks.
5. Push to the branch.
6. Create a pull request.
