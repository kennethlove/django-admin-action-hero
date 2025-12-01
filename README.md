# django-admin-action-hero

`django-admin-action-hero` is a library designed to make it easier to create custom
repetitive admin actions for Django's admin interface. It provides a simple way
to create classes that encapsulate admin actions, allowing for better code reuse
and organization.

[Read the full docs](https://django-admin-action-hero.readthedocs.io/)

## Installation

To install `django-admin-action-hero`, you'll use `pip install django-admin-action-hero`
or add `django-admin-action-hero` to your `pyproject.toml` or `requirements.txt`.
You don't need to add anything to your `INSTALLED_APPS`.

## Usage

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

## Contributing

Thanks for wanting to contribute to `django-admin-action-hero`! Contributions are
always welcome (even if they may not all be accepted). Here's how you can help:

* Improve documentation.
* Report bugs via GitHub issues.
* Suggest new features via GitHub discussions.
* Submit pull requests with bug fixes or new features (once approved).

If your contribution requires code changes, please ensure that you follow these
steps:

1. Fork the repository.
2. Set up git pre-commit hooks. (I recommend
   [`prek`](https://github.com/j178/prek) for this)
3. Create a virtual environment and install dependencies. (I recommend using
   [`uv`](https://docs.astral.sh/uv/).)
4. Run tests to ensure everything is working. You'll use `pytest` for writing
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
5. Update the changelog with [`git-cliff`](https://github.com/orhun/git-cliff).
6. Make sure the documentation is up to date and correct.
7. Push to the branch.
8. Create a pull request.
