action\_hero.lib
================

Base classes and types for ``action_hero``.

------------
Base classes
------------

.. toctree::
   :maxdepth: 4

   AdminActionBaseClass <action_hero.lib.adminactionbaseclass>

-----
Types
-----

.. condition_:

Condition
---------

.. py:type::  Callable[[Any], bool]

``action_hero.lib.Condition`` is a type alias for a callable that takes a model
instance and returns a Boolean indicating whether some condition is met. This
acts as a :external:py:func:`filter`

.. function_:

Function
--------

.. py:type::  Callable[[Any], None]

``action_hero.lib.Function`` is a type alias for a callable that performs some
operation. The specific signature of the callable is not enforced, allowing for
flexibility in defining functions that can be used with actions.
