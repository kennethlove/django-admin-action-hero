from typing import Any
from unittest import mock

import pytest
from django.contrib.admin import AdminSite

from ._app.admin import AdminActionsTestModelAdmin
from ._app.models import AdminActionsTestModel


@pytest.fixture
def mock_function():
    def _empty_function(*args, **kwargs):
        """A no-op function for testing purposes."""
        pass

    with mock.patch.object(
        _empty_function,
        "__call__",
        wraps=_empty_function.__call__,
        __name__="empty_function",
    ) as mock_fn:
        yield mock_fn


@pytest.fixture
def admin_site():
    yield AdminSite()


@pytest.fixture
def admin(admin_site):
    yield AdminActionsTestModelAdmin(AdminActionsTestModel, admin_site)


@pytest.mark.django_db
@pytest.fixture
def model_instance(faker):
    def _create_instance():
        yield AdminActionsTestModel.objects.create(name=faker.word())

    yield _create_instance


@pytest.fixture(name="_request")
def request_with_messages(rf, admin_user):
    """Create a session- and messages-enabled request."""

    def _request(method="get", path="/", data=None):
        request: Any = None
        match method.lower():
            case "get":
                request = rf.get(path, data=data or {})
            case "post":
                request = rf.post(path, data or {})
            case _:
                raise ValueError(f"Unsupported method: {method}")

        request.user = admin_user
        setattr(request, "session", "session")
        setattr(request, "_messages", mock.MagicMock())

        yield request

    yield _request
