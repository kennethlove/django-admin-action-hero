try:
    import celery
except ImportError as e:
    raise ImportError(
        "Celery integration requires celery to be installed. "
        "Install it with: pip install admin-actions[celery]"
    ) from e

from admin_actions.lib import AdminActionBaseClass, Condition


class QueueCeleryAction(AdminActionBaseClass):
    """Generates an admin action for queuing a Celery task for a chosen set of records.

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

    :param task: Required. Should be a Celery Task callable that takes a single
        model instance's primary key as an argument.
    :param condition: Optional. If provided, it should be a callable that takes a
        model instance and returns a boolean indicating whether to queue the task
        for that record.
    :param name: Optional. If provided, it will be used as the action's name in the
        admin interface. If it is omitted, the name of the task will be used instead.
    """

    function: celery.Task

    def handle_item(self, item):
        """Queues the Celery task for the given item."""
        self.function.delay(item.pk)

    def __init__(
        self,
        task: celery.Task,
        *,
        condition: Condition | None = None,
        name: str | None = None,
    ) -> None:
        """Initializes the action with a task and optional condition."""
        if not isinstance(task, (celery.Task,)):
            raise TypeError(f"The task must be a Celery task. Got {type(task)}")

        super().__init__(
            function=task, condition=condition, name=name or task.name
        )  # Note that `task` ends here. Use `self.function`.
