from unittest import mock

import pytest
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME

from admin_actions.actions import QueueCeleryAction
from tests.app.models import AdminActionsTestModel


@pytest.fixture(scope="session")
def celery_enable_logging():
    return True


@pytest.fixture(scope="session")
def celery_config():
    return {
        "broker_url": "memory://",
        "result_backend": "rpc://",
        "task_always_eager": True,
    }


@pytest.fixture
def celery_task(celery_session_app):
    @celery_session_app.task
    def sample_task(sample_pk: int):  # Must take a single argument
        print(f"Processing record {sample_pk}")

    return sample_task


@pytest.fixture
def mock_delay(celery_task, monkeypatch):
    mock_delay = mock.Mock()
    monkeypatch.setattr(celery_task, "delay", mock_delay)
    return mock_delay


@pytest.mark.django_db
def test_task_is_delayed_appropriately(
    admin,
    model_instance,
    celery_task,
    mock_delay,
    _request,
):
    """Using the action in the Admin should delay the provided task."""
    instance = model_instance()
    model_instance()
    r = _request(method="post", data={ACTION_CHECKBOX_NAME: [instance.pk]})  # type: ignore # kwargs are unexpected?

    def _filter(obj: AdminActionsTestModel) -> bool:
        return obj.pk == instance.pk

    # noinspection PyTypeChecker
    queue_action = QueueCeleryAction(celery_task, condition=_filter)
    queue_action(admin, r, AdminActionsTestModel.objects.all())
    mock_delay.assert_called_once_with(instance.pk)


def test_non_celery_task_raises():
    """Providing a non-celery task should raise an error."""

    def not_a_celery_task(_):
        return 0

    with pytest.raises(TypeError):
        # noinspection PyTypeChecker
        QueueCeleryAction(task=not_a_celery_task)  # pyright: ignore[reportArgumentType]


def test_celery_not_available(monkeypatch):
    """Without Celery installed, `from admin_actions.actions import *` should not include `QueueCeleryAction`."""
    import sys
    from importlib import reload

    if "admin_actions.actions" in sys.modules:
        del sys.modules["admin_actions.actions"]
    if "admin_actions.actions.queue_celery" in sys.modules:
        del sys.modules["admin_actions.actions.queue_celery"]

    monkeypatch.setitem(sys.modules, "celery", None)

    import admin_actions.actions

    reload(admin_actions.actions)
    assert "QueueCeleryAction" not in admin_actions.actions.__all__


def test_celery_not_available_raises(monkeypatch):
    """Celery not being installed should raise an ImportError."""
    import sys
    from importlib import reload

    if "admin_actions.actions.queue_celery" in sys.modules:
        del sys.modules["admin_actions.actions.queue_celery"]

    monkeypatch.setitem(sys.modules, "celery", None)

    with pytest.raises(
        ImportError, match="Celery integration requires celery to be installed"
    ):
        import admin_actions.actions.queue_celery

        reload(admin_actions.actions.queue_celery)
