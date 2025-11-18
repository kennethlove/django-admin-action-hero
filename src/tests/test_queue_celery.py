from unittest import mock

import pytest
from django.contrib.admin import AdminSite
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME

from admin_actions.actions.queue_celery import QueueCeleryAction

from .admin import AdminActionsTestModelAdmin
from .models import AdminActionsTestModel


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
def admin_site():
    return AdminSite()

@pytest.fixture
def admin(admin_site):
    return AdminActionsTestModelAdmin(AdminActionsTestModel, admin_site)

@pytest.fixture
def model_instance(faker):
    return AdminActionsTestModel.objects.create(name=faker.word())

@pytest.fixture
def celery_task(celery_session_app):
    @celery_session_app.task
    def sample_task(_):  # Must take a single argument
        ...

    return sample_task

@pytest.fixture
def mocked_task(celery_task):
    with mock.patch.object(celery_task, 'delay', wraps=celery_task.delay) as mock_delay:
        yield mock_delay

def test_generated_action_is_registrable(self, admin, rf, celery_task, admin_user):
    """The Admin should have a sample_task action, generated from QueueCeleryAction."""
    r = rf.get('/')
    r.user = admin_user

    queue_action = QueueCeleryAction(
        task=celery_task
    )
    admin.actions += (queue_action,)

    actions = admin.get_actions(r)
    expected = 'sample_task'
    assert expected in actions.keys(), f"Expected action '{expected}' not found in admin actions."

def test_generated_action_is_callable(self, admin, admin_user, rf, mocked_task, celery_task, model_instance):
    """The Admin should have a sample_task action"""
    r = rf.post("/", data={ACTION_CHECKBOX_NAME: [model_instance.pk]})
    r.user = admin_user

    from django.contrib.messages.storage.fallback import FallbackStorage
    setattr(r, "session", "session")
    setattr(r, "_messages", FallbackStorage(r))

    queue_action = QueueCeleryAction(task=celery_task)
    queue_action(admin, r, AdminActionsTestModel.objects.filter(pk=model_instance.pk))

    mocked_task.assert_called_once_with(model_instance.pk)
