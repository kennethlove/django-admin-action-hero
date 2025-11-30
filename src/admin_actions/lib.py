"""Provides an abstract base class for generating admin actions."""

import abc
from collections.abc import Callable
from typing import Any, TypeAlias

from django.contrib import messages
from django.contrib.admin import ModelAdmin
from django.db.models import Model, QuerySet
from django.http import HttpRequest

Condition: TypeAlias = Callable[
    [Any], bool
]  # Condition to enable the function for an item.
Function: TypeAlias = Callable[[Any], None]  # Function to call for each item.


class AdminActionBaseClass(abc.ABC):
    """Generates an admin action for calling a function for a chosen set of records.

    Yes, it's basically an abstracted ``map``.

    Example usage::

        class MyAdminAction(AdminActionBaseClass):
            def handle_item(self, item):
                self.funtion(item)
                print(f"{item.pk} has been handled.")
                
        conditional_action = MyAdminAction(
            function=my_function,
            condition=lambda record: record.should_process(),
            name="process_records")

        def my_function(record_id):
            record = MyModel.objects.get(pk=record_id)
            ...

        class MyModelAdmin(admin.ModelAdmin):
            actions = [conditional_action]
            model = MyModel

    :param function: Required. Should be a callable that takes a single model instance as an argument.
    :param condition: Optional. If provided, it should be a callable that takes a model
        instance and returns a Boolean indicating whether to queue the task for that record.
    :param name: Optional. If provided, it will be used as the action's name in the admin
        interface. If it is omitted, the function name will be used instead.
    """

    @abc.abstractmethod
    def handle_item(self, item):
        """Handles a single item from the queryset.

        This method will be called for each item in the queryset that passes the condition. Any
        subclass must implement this method to define how to process each item.

        NOTE: This method *is not* asynchronous or in another thread/process; large quantities of
        work should be done in other ways or places, not solely in this method.

        :param item: The model instance being processed.
        """

    def __call__(
        self, modeladmin: ModelAdmin, request: HttpRequest, queryset: QuerySet[Model]
    ) -> None:
        """Calls ``self.handle_item`` for each item in ``queryset`` that passes ``self.condition``.

        :param modeladmin: The admin instance for the model being processed.
        :param request: The current HTTP request object.
        :param queryset: The queryset of records to process.
        """
        _count: int = 0  # Number of records successfully processed

        for record in queryset:
            if not self.condition(
                record
            ):  # Skip any records that don't meet the condition
                continue
            self.handle_item(record)  # Apply the function to the record
            _count += 1  # Increment the counter, record was successfully processed

        if _count:  # If any records were processed, notify the user
            # Get the appropriate plural model name, or a reasonable fallback
            model_name = (
                queryset.model._meta.verbose_name_plural
                or queryset.model.__name__ + "s"
            )
            if _count == 1:
                # Get the appropriate singular model name, or a reasonable fallback
                model_name = (
                    queryset.model._meta.verbose_name or queryset.model.__name__
                )

            model_name = model_name.title()

            modeladmin.message_user(  # Add a success message for the user
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
        """Initializes the action with a function and an optional condition.

        :param function: Required. Should be a callable that takes a single model instance.
        :param condition: Optional. If provided, it should be a callable that takes a model instance and returns a
            Boolean indicating whether to queue the task for that record.
        :param name: Optional. If provided, will be used as the action's name in the admin interface.
        """

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
        self.__name__ = name if name else function.__name__
