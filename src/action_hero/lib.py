"""Provides an abstract base class for generating admin action classes."""

from __future__ import annotations

import abc
from collections.abc import Callable
from typing import Any

from django.contrib import messages
from django.contrib.admin import ModelAdmin
from django.db.models import Model, QuerySet
from django.http import HttpRequest

__all__ = ["AdminActionBaseClass", "Condition", "Function"]

# Condition to enable the function for an item.
type Condition = Callable[[Any], bool]
# Function to call for each item.
type Function = Callable[[Any], None]


class AdminActionBaseClass(abc.ABC):
    """
    Generates an admin action that calls a function for a chosen set of records.

    Yes, it's basically an abstracted ``map``.

    Example usage::

        class MyAdminAction(AdminActionBaseClass):
            def handle_item(self, item):
                self.function(item)
                print(f"{item.pk} has been handled.")

        # Example 1: Using only name (auto-generated short_description)
        conditional_action = MyAdminAction(
            function=my_function,
            condition=lambda record: record.should_process(),
            name="process_records",
        )

        # Example 2: Explicitly overriding short_description (recommended Django-style)
        custom_label_action = MyAdminAction(
            function=my_function,
            name="bulk_process",
            short_description="Process Selected Records",
        )

        def my_function(record):
            # perform work on a single model instance

        class MyModelAdmin(admin.ModelAdmin):
            actions = [conditional_action, custom_label_action]
            model = MyModel

    If you need custom behavior, subclass ``AdminActionBaseClass`` and override
    the appropriate method(s). See implementations in ``actions`` for details.
    """

    @abc.abstractmethod
    def handle_item(self, item: Model):
        """Handles a single item from the queryset.

        This method will be called for each item in the queryset that passes the
        condition. Any subclass must implement this method to define how to
        process each item.

        Note:
            This method *is not* asynchronous or in another thread/process;
            large quantities of work should be done in other ways or places, not
            solely in this method.

        Args:
            item: The model instance being processed.
        """

    def __call__(
        self, modeladmin: ModelAdmin, request: HttpRequest, queryset: QuerySet[Model]
    ) -> None:
        """Calls ``self.handle_item`` for each item in ``queryset`` that passes
        ``self.condition``.

        Args:
            modeladmin: The admin instance for the model being processed.
            request: The current HTTP request object.
            queryset: The queryset of records to process.
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
        short_description: str | None = None,
    ) -> None:
        """
        Initializes the action with a function and an optional condition.

        Args:
            function: Callable that takes a model instance.
            condition: Callable for whether to process each record.
            name: Internal identifier used by Django admin if
                ``short_description`` is not provided.
            short_description: User-facing label shown in the Django admin
                dropdown.
        """

        if condition is not None:
            if isinstance(condition, Callable):
                self.condition = condition
            else:
                raise TypeError("The condition must be a callable.")
        else:
            self.condition = lambda _: True

        if not callable(function):
            raise TypeError("The function must be a callable.")

        self.function = function

        # Internal action identifier
        self.name = name or function.__name__
        self.__name__ = self.name

        self.short_description = short_description
