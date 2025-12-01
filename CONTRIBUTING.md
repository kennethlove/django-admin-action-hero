# Contributing to django-admin-action-hero

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
