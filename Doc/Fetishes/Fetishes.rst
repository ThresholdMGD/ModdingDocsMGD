.. _FetishesAddictions:

**Fetishes & Addictions**
==========================

See *Json/Fetishes/* for all related fetish **and** addiction .json files for reference. All keys are required.

.. _Fetishes:

**Fetishes**
-------------

Making a custom fetish comes down to making a .json like the following code block:

::

  {
  "FetishList": [
      {
      "Name": "Atom",
      "BaseLevel": "0",
      "Type": "Fetish",
      "CreationOn": "Enlightened!",
      "CreationOff": "Heathen."
      }
    ]
  }

``"FetishList":`` will contain an array of objects representing each fetish. See *Fetishes/fetishList.json* for reference.

All keys are required.

**Name**
"""""""""

``"Name":`` decides the name of your fetish, used for both internal reference and to be shown to the player in menus and skills.

**BaseLevel**
""""""""""""""

``"BaseLevel":`` can optionally give a default amount of the fetish, regardless if it is selected by the player in the creation menu. Give it a string of "0"
if you do not wish to use it.

**Type**
"""""""""

``"Type":`` should be set to "Fetish", unless making an Addiction, as documented below.

**CreationOn & CreationOff**
"""""""""""""""""""""""""""""

The provided strings will be the dialogue the Goddess gives in the creation menu when starting a new game. ``"CreationOn":`` being if the player selects the fetish,
``"CreationOff":`` if the player unselects the fetish.

.. _Addictions:

**Addictions**
---------------

Addictions, being technically fetishes, use all the same functions and keys as their counterpart, with the exception of being invisible to the player.
They can be put in the same JSON file together, or optionally separated for organization, like the base game.

It is recommended to go to *Fetishes/addictionList.json* and see the comments Threshold provided for each base game addiction, and use your editor's search features
to review how they are used throughout the base game via the strings provided to the ``"Name":`` keys.

::

  {
  "FetishList": [
      {
      "Name": "Required for internal reference of the addiction.",
      "BaseLevel": "0",
      "Type": "Addiction",
      "CreationOn": "This text won't appear in-game, but still needs filled out so the game doesn't generate an error.",
      "CreationOff": ""
      }
    ]
  }

As one can see, you really only need to provide ``"Type":`` with ``"Addiction"``, and provide ``"Name":`` with a unique string to use for internal referral.
The rest is unused, but required to prevent an error on runtime.
