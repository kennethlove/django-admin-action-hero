"""Provides the simplest possible implementation of AdminActionBaseClass."""

from __future__ import annotations

from django.db.models import Model

from action_hero.lib import AdminActionBaseClass

__all__ = ["SimpleAction"]


class SimpleAction(AdminActionBaseClass):
    """Generates an admin action calling a function for a chosen set of records.

    This is the simplest "useful" implementation of ``AdminActionBaseClass``. It
    only calls the provided ``function`` with the primary key of each record in
    the ``queryset``. Because the default ``condition`` is always ``True``, this
    action will be carried out for every record.

    Example usage::

        titlecase_titles_action = SimpleAction(function=str.title)

        class MyModelAdmin(admin.ModelAdmin):
            actions = [titlecase_titles_action]
            model = MyModel

    This will call ``str.title`` on each record's ``title`` attribute. Because
    this doesn't involve a database write, the change is immediately discarded.
    """

    def handle_item(self, item: Model):
        """Handles a single item from the queryset.

        Args:
            item: The model instance being processed.
        """
        self.function(item.pk)
