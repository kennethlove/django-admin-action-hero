from collections.abc import Callable, Mapping
from typing import Any, Generator
from unittest import mock
from unittest.mock import MagicMock, AsyncMock

import pytest
from django.contrib.admin import AdminSite
from django.contrib.sessions.backends.cache import SessionStore
from django.http import HttpRequest

from .app.admin import AdminActionsTestModelAdmin
from .app.models import AdminActionsTestModel


@pytest.fixture
def mock_function() -> mock.MagicMock:
    """Create a mock function."""

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
    """Create a new AdminSite."""
    return AdminSite()


@pytest.fixture
def admin(admin_site) -> AdminActionsTestModelAdmin:
    """Create an AdminActionsTestModelAdmin using the provided AdminSite."""
    return AdminActionsTestModelAdmin(AdminActionsTestModel, admin_site)


@pytest.fixture
def mock_messages(admin) -> Generator[MagicMock | AsyncMock, Any, None]:
    """Mock the `message_user` method on the Admin."""
    mock_messages = mock.patch("action_hero.lib.ModelAdmin.message_user").start()
    yield mock_messages
    mock_messages.stop()


@pytest.fixture
def model_instance(db, faker) -> Callable[[], AdminActionsTestModel]:
    """Create a new instance of AdminActionsTestModel."""

    def _create_instance() -> AdminActionsTestModel:
        return AdminActionsTestModel.objects.create(name=faker.word())

    return _create_instance


def request_with_messages(
    rf, admin_user
) -> Callable[[str, str, Mapping[str, list] | None], HttpRequest]:
    """Create a session- and messages-enabled request."""

    def _request(
        method: str = "get", path: str = "/", data: Mapping[str, list] | None = None
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


# Decorated like this for type hinting
request_fixture: Callable[[str, str, Mapping[str, list] | None], HttpRequest] = (
    pytest.fixture(request_with_messages, name="_request")
)
