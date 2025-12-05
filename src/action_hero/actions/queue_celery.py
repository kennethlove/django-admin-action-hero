"""Provides an admin action to queue Celery tasks for selected records."""

from __future__ import annotations

from django.db.models import Model

# Guard import for Celery integration
try:
    import celery
except ImportError as e:
    raise ImportError(
        "Celery integration requires celery to be installed. You can install "
        "it with: pip install django-admin-action-hero[celery]"
    ) from e

from action_hero.lib import AdminActionBaseClass, Condition

__all__ = ["QueueCeleryAction"]


class QueueCeleryAction(AdminActionBaseClass):
    """Generates an admin action for queuing a Celery task for a chosen set of
    records.

    Example usage::

        conditional_action = QueueCeleryAction(
            task=my_celery_task,
            condition=lambda record: record.should_process(),
        )
        another_action = QueueCeleryAction(...)

        @celery.task
        def my_celery_task(record_id):
            record = MyModel.objects.get(pk=record_id)
            ...

        class MyModelAdmin(admin.ModelAdmin):
            actions = [conditional_action, QueueCeleryAction(...), another_action]
            model = MyModel
    """

    function: celery.Task

    def handle_item(self, item: Model):
        """Queues the Celery task for the given item.

        Args:
            item: The model instance being processed.
        """
        self.function.delay(item.pk)

    def __init__(
        self,
        task: celery.Task,  # Not just any function.
        *,
        condition: Condition | None = None,
        name: str | None = None,
        short_description: str | None = None,
    ) -> None:
        """Initializes the action with a Celery task and an optional condition.

        Args:
            task: Should be a Celery Task callable that takes a single model
                instance's primary key as an argument.
            condition: A callable that takes a model instance and returns a
                Boolean indicating whether to queue the task for that record.
            name: The action's name in the admin. If it is omitted, the name
                of the task will be used instead.
            short_description: The action's name displayed in the admin.
              Overrides ``name``.
        """
        if not isinstance(task, (celery.Task,)):
            raise TypeError(f"The task must be a Celery task. Got {type(task)}")
        super().__init__(
            function=task,
            condition=condition,
            name=name or task.name,
            short_description=short_description,
        )  # Note that `task` ends here. Use `self.function` in other methods.
