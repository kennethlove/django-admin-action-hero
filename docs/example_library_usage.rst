Example Library Usage
#####################

.. highlight:: python3

We need an :external+django:py:func:`admin action <django.contrib.admin.action>`
that will take a batch of records, selected in the admin, make sure each record
is valid, and then spawn a
:external+celery:doc:`background task <userguide/tasks>`, for each record, that
will apply our :ref:`custom processing function <Function>` to it. We may need
this same kind of action in multiple admins or even projects.
``django-admin-action-hero`` helps us avoid this repetition by giving us classes
to handle common scenarios and an :external:std:term:`abstract base class` to
use for our own custom action types.

First, let's define a simple
:external+celery:doc:`background task <userguide/tasks>` using
:external+celery:class:`Celery <celery.Celery>`. This task will perform the
processing on each record. In this case, we're just going to simulate processing
with a :external:py:func:`print()` call.

.. code-block:: python
    :caption: tasks.py

    from celery import shared_task

    @shared_task
    def process_record(record_id):
        # Simulate processing the record
        print(f"Processing record {record_id}")

.. admonition:: Important
    :class: important

    Make sure Celery is set up and configured properly to run background tasks.

.. admonition:: Important
    :class: important

    The Celery task must accept a single argument which will be the ``.pk`` of
    the model instance to process. This design is intentional to promote the
    best practice of providing identifiers to tasks instead of full objects.

Now we can add a :ref:`filter <Condition>` function so that any invalid records
are skipped. This function works like Python's built-in
:external:py:func:`filter` function, returning ``True`` for valid records and
``False`` for invalid ones. We can do any validation we need here but we must
keep in mind that this function will be blocking the admin action until it
completes, so we should avoid long-running operations.

.. code-block:: python
    :caption: action_filters.py

    def is_valid_record(record):
        # Example validation logic
        return record.is_active  # Only process active records

We now have everything we need to create our custom admin action. For this
example, we're going to use the provided
:py:class:`~action_hero.actions.queue_celery.QueueCeleryAction` class.
It shows a lot of the features of the library and is a common use case.

We already have an ``admin.py`` for our :external+django:py:class:`Django model <django.db.models.Model>`. This is the most logical
place to put our custom admin action to use. Once we import the class for our
type of action, like the :py:class:`QueueCeleryAction` when using Celery, we can
create our action instance.

.. code-block:: python
    :caption: admin.py

    from django.contrib import admin
    from action_hero.actions.queue_celery import QueueCeleryAction
    from .action_filters import is_valid_record
    from .models import Record
    from .tasks import process_record

    celery_action = QueueCeleryAction(
        task=process_record,     # The Celery task to call, required
        condition=is_valid_record,  # Our validation function, optional
        name="Process Records",  # Unique name for the action, optional
    )

    @admin.register(Record)
    class RecordAdmin(admin.ModelAdmin):
        actions = [celery_action]

We created an instance of :py:class:`QueueCeleryAction`, passing in our Celery task
and validation function. We also gave our action a name, which is optional. If
we didn't provide one, a default name would be generated based on the task name
(e.g., ``process_records``). After that, we registered our action with the admin
by adding it to the ``actions`` list of our ``RecordAdmin`` class. All
:py:class:`~action_hero.lib.AdminActionBaseClass` subclasses can be called
like functions, so Django will happily run them for us.

Now it's time to test our new admin action. Start or restart the Django server
and navigate to the admin for ``RecordAdmin``. If we select a few records, the
"Process Records" action should appear in the action dropdown. Selecting the
action and submitting the form will trigger our custom action. The action will
validate each selected record using the ``is_valid_record`` function. Then, for
each valid record, our action will add a new Celery task to the queue for later
processing.
