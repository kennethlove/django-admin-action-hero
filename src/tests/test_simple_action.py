import pytest
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME

from admin_actions.actions import SimpleAction
from tests.app.models import AdminActionsTestModel


@pytest.mark.django_db
def test_function_is_called_appropriately(
    admin,
    model_instance,
    mock_function,
    _request,
):
    """Using the action in the Admin should call the provided function."""
    instance = model_instance()
    model_instance()
    r = _request(method="post", data={ACTION_CHECKBOX_NAME: [instance.pk]})

    def _filter(obj: AdminActionsTestModel) -> bool:
        return obj.pk == instance.pk

    queue_action = SimpleAction(mock_function, condition=_filter)
    queue_action(admin, r, AdminActionsTestModel.objects.all())

    mock_function.assert_called_once_with(instance.pk)
