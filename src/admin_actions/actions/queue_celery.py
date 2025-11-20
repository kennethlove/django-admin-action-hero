from collections.abc import Callable
from types import FunctionType
from typing import TypeAlias

import celery
from django.contrib import messages
from django.contrib.admin import ModelAdmin
from django.db.models import QuerySet
from django.http import HttpRequest


class QueueCeleryAction:
    """Generates an admin action for queuing a Celery task for a chosen set of records.

    Usage:
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

    The `task` parameter is required and should be a Celery task callable that takes a single model
    instance's primary key as an argument.

    The `condition` parameter is optional. If provided, it should be a callable that takes
    a model instance and returns a boolean indicating whether to queue the task for that record.
    """

    Condition: TypeAlias = Callable[[type], bool]  # Condition to enable the action
    Task: TypeAlias = FunctionType  # Celery task to be called

    def __call__(
        self, modeladmin: ModelAdmin, request: HttpRequest, queryset: QuerySet
    ) -> None:
        """Admin action to queue task for selected records."""
        _count: int = 0

        for record in queryset:
            if not self.condition(record):
                continue
            self.task.delay(record.pk)
            _count += 1

        if _count:
            model_name = queryset.model._meta.verbose_name_plural.title()
            if _count == 1:
                model_name = queryset.model._meta.verbose_name.title()

            modeladmin.message_user(
                request,
                f"Queued tasks for {_count} {model_name}.",
                messages.SUCCESS,
            )

    def __init__(
        self, task: Task, *, condition: Condition | None = None, name: str | None = None
    ) -> None:
        """Initializes the action with optional condition and task."""

        self.name = name

        if condition is not None:
            if isinstance(condition, Callable):  # Cannot call a non-callable condition
                self.condition = condition
            else:
                raise TypeError("The condition must be a callable.")
        else:
            self.condition = lambda _: True  # Default condition always returns True

        if not callable(task):  # Cannot call a non-callable task
            raise TypeError("The task must be a callable.")

        if not isinstance(
            task, (celery.Task,)
        ):  # Currently only Celery tasks are supported
            raise TypeError(f"The task must be a Celery task. Got {type(task)}")

        self.task = task

    @property
    def __name__(self) -> str:
        """Returns the name of the action."""
        if self.name:
            return self.name
        return self.task.name
