"""Provides the simplest possible implementation of AdminActionBaseClass."""

from admin_actions.lib import AdminActionBaseClass


class SimpleAction(AdminActionBaseClass):
    """Generates an admin action for calling a function for a chosen set of records.

    This is the simplest possible implementation of AdminActionBaseClass. It only calls the
    provided function with the primary key of each record in the queryset. Because the default
    condition is always True, this action will be carried out for every record.
    """

    def handle_item(self, item):
        """Handles a single item from the queryset.

        :param item: The model instance being processed.
        """
        self.function(item.pk)
