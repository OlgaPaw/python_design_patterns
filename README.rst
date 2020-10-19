**********************
Python Design Patterns
**********************

Run a project
#############

Usage examples can be found in ``design_pattern/tests``.

.. code-block:: python

   poetry install
   pytest .


Strategy
########

Problem description:

- There is a list of students with their final exam notes. 
- Examinator needs to present student notes with different formats:
    - Index Numbers + Notes ordered by Student Index Number
    - Index Numbers + Notes ordered by Notes
    - Full Names + Notes ordered by Notes
    - Full Names + Notes ordered by Surname


Command
#######

Problem description:

The calculator supporting undo/redo last command


Mediator
########

Problem description:

Multiple interfaces (mobile, online, ATM) have access to bank account (mediator).
When ay operation is perfomed through any interface, the mobile interface gets the notification.

A ``BankAccount`` performs as the ``Mediator`` and notifies ``mobile_interface`` about any operation performed.
Any other ``AccountInterface`` can be added.
