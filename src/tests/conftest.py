from collections.abc import Callable
from unittest import mock

import pytest
from django.contrib.admin import AdminSite
from django.contrib.sessions.backends.cache import SessionStore
from django.http import HttpRequest

from .app.admin import AdminActionsTestModelAdmin
from .app.models import AdminActionsTestModel


@pytest.fixture
def mock_function() -> mock.MagicMock:
    # noinspection PyUnusedLocal
    def _empty_function(*args, **kwargs):
        """A no-op function for testing purposes."""
        pass

    with mock.patch.object(
        _empty_function,
        "__call__",
        wraps=_empty_function.__call__,
        __name__="empty_function",
    ) as mock_fn:
        return mock_fn


@pytest.fixture
def admin_site() -> AdminSite:
    return AdminSite()


@pytest.fixture
def admin(admin_site) -> AdminActionsTestModelAdmin:
    return AdminActionsTestModelAdmin(AdminActionsTestModel, admin_site)


# noinspection PyUnusedLocal
@pytest.fixture
def model_instance(db, faker) -> Callable[[], AdminActionsTestModel]:
    def _create_instance() -> AdminActionsTestModel:
        return AdminActionsTestModel.objects.create(name=faker.word())

    return _create_instance


@pytest.fixture(name="_request")
def request_with_messages(
    rf, admin_user
) -> Callable[[str, str, dict | None], HttpRequest]:
    """Create a session- and messages-enabled request."""

    def _request(
        method: str = "get", path: str = "/", data: dict | None = None
    ) -> HttpRequest:
        if method.lower() == "get":
            request = rf.get(path, data=data or {})
        elif method.lower() == "post":
            request = rf.post(path, data or {})
        else:
            raise ValueError(f"Unsupported method: {method}")

        request.user = admin_user
        setattr(request, "session", SessionStore())
        setattr(request, "_messages", mock.MagicMock())

        return request

    return _request
