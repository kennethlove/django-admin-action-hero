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
    def sample_task(foo):  # Must take a single argument
        pass

    return sample_task


@pytest.fixture
def mock_task(celery_task):
    return mock.patch(
        autospec=True,
        target="tests.test_queue_celery.celery_task",
        attribute="__call__",
        wraps=celery_task.__call__,
    )


@pytest.fixture
def mock_delay(celery_task):
    with mock.patch.object(
        target="admin_actions.actions.QueueCeleryAction",
        attribute="delay",
        wraps=celery_task.delay,
    ) as mock_delay:
        return mock_delay


@pytest.mark.django_db
def test_task_is_delayed_appropriately(
    admin,
    model_instance,
    celery_task,
    mock_task,
    mock_delay,
    _request,
):
    """Using the action in the Admin should delay the provided task."""
    instance = model_instance()
    model_instance()
    r = _request("post", data={ACTION_CHECKBOX_NAME: [instance.pk]})

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
