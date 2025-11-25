from collections.abc import Callable
from typing import Any, TypeAlias

from django.contrib import messages
from django.contrib.admin import ModelAdmin
from django.db.models import QuerySet
from django.http import HttpRequest

Condition: TypeAlias = Callable[[Any], bool]  # Condition to enable the action
Function: TypeAlias = Callable[[Any], None]


class AdminActionBaseClass:
    """Generates an admin action for calling a function for a chosen set of records.

    Yes, it's basically an abstracted ``map``.

    Example usage::

        conditional_action = MyAdminAction(
            function=my_function,
            condition=lambda record: record.should_process(),
            name="process_records",
        )

        def my_function(record_id):
            record = MyModel.objects.get(pk=record_id)
            ...

        class MyModelAdmin(admin.ModelAdmin):
            actions = [conditional_action]
            model = MyModel

    :param function: Required. Should be a callable that takes a single model instance's
        primary key as an argument.
    :param condition: Optional. If provided, it should be a callable that takes a model
        instance and returns a boolean indicating whether to queue the task for that record.
    :param name: Optional. If provided, it will be used as the action's name in the admin
        interface. If it is omitted, the name of the function will be used instead.
    """

    def handle_item(self, item):
        self.function(item.pk)

    # noinspection PyProtectedMember
    def __call__(
        self, modeladmin: ModelAdmin, request: HttpRequest, queryset: QuerySet
    ) -> None:
        """Admin action to call `self.function` for `queryset` records that pass `self.condition`."""
        _count: int = 0

        for record in queryset:
            if not self.condition(record):
                continue
            self.handle_item(record)
            _count += 1

        if _count:
            model_name = queryset.model._meta.verbose_name_plural.title()
            if _count == 1:
                model_name = queryset.model._meta.verbose_name.title()

            modeladmin.message_user(
                request,
                f"Called {self.__name__} for {_count} {model_name}.",
                messages.SUCCESS,
            )

    def __init__(
        self,
        function: Function,
        *,
        condition: Condition | None = None,
        name: str | None = None,
    ) -> None:
        """Initializes the action with a function and optional condition."""

        if condition is not None:
            if isinstance(condition, Callable):  # Cannot call a non-callable condition
                self.condition = condition
            else:
                raise TypeError("The condition must be a callable.")
        else:
            self.condition = lambda _: True  # The default condition always returns True

        if not callable(function):  # Cannot call a non-callable task
            raise TypeError("The function must be a callable.")

        self.name = name
        self.function = function

    @property
    def __name__(self) -> str:
        """Returns the name of the action."""
        if self.name:
            return self.name
        return self.function.__name__
