.. meta::
    :keywords: ifprogress

.. _Progress:

**Progress**
=============

Progress is typically used to track relationship progress with characters, but it can be used for more technical purposes.

**By default, progress for all events start at 0.**

.. tip::

  You can display progress via the ``{DisplayProgress}`` :ref:`Text Markup`. Also see :ref:`Get Event Progress` for progress functions outside of the given file.

**SetProgress**
----------------
Will set the event's progress to the specified number. Can be negative.

::

  "SetProgress", "0"

**ChangeProgress**
-------------------
Changes the events progress based on the given value. Can be negative.

::

  "ChangeProgress", "5"

**ChangeProgressBasedOnVirility**
----------------------------------
Changes progress based on virility, with the following with the value in the following string being a multiplier.
Base number in the example translates to 0.1x scaling of the players virility total. So if the player has 100 virility, it will result in progress increasing by 10.

::

  "ChangeProgressBasedOnVirility", "1"

Primarily designed for the blue balls system, but it can have other uses.

**ProgressEquals**
-------------------
Checks if the progress of the event is equal to the following number. If true, it jumps to the given scene. If false, it is ignored.
Can be negative.

::

  "ProgressEquals", "10", "SceneNameHere"

**ProgressEqualsOrGreater**
----------------------------
Works the same as the previous function, but is still true even if the event's value is greater than the checked value.
Can be negative.

::

  "ProgressEqualsOrGreater", "10", "SceneNameHere"

**ProgressEqualsOrLess**
-------------------------
Same as the previous function, but instead is still true if the event's value is less than the checked value.
Can be negative.

::

  "ProgressEqualsOrLess", "10", "SceneNameHere"
