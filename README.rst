**********************
Python Design Patterns
**********************

Run a project
#############

Usage examples can be found in ``design_pattern/tests``.

.. code-block:: python

   poetry install
   pre-commit install
   pytest .


Command
#######

Example problem:

The calculator supporting undo/redo last command


Mediator
########

Example problem:

Multiple interfaces (mobile, online, ATM) have access to bank account (mediator).
When ay operation is perfomed through any interface, the mobile interface gets the notification.

A ``BankAccount`` performs as the ``Mediator`` and notifies ``mobile_interface`` about any operation performed.
Any other ``AccountInterface`` can be added.


Singleton / Monostate
#####################

Example problem:

A Blog Post App with global font configuration.
``Font`` settings (color and base size) acts like singleton/monostate, a single object shared between all  ``TextField`` objects.
It can be accessed from any part of application (including tests).
Any change made to Font module affects all other ``TextField`` objects.


Strategy
########

Example problem:

- There is a list of students with their final exam notes. 
- Examinator needs to present student's notes report with different formats:
    - Index Numbers + Notes ordered by Student Index Number
    - Index Numbers + Notes ordered by Notes
    - Full Names + Notes ordered by Notes
    - Full Names + Notes ordered by Surname
