.. _Event Additions:

**Event Additions**
====================

Making an addition to an Event can be as little or as much involved as desired. It is recommended to keep it as minimal as possible to avoid
compatibility issues with other mods making additions to the same events. It covers the scope of replacing specific scenes, adding new scenes,
and appending to the list of ``"Speakers"``.

This does mean your addition would be incompatible with other mods that make an addition to the same scenes in an Event.
This is excluding scenes solely using :ref:`MenuAddition` for the brothel and the likes.

Check **_EventAdditionExample.json** in *Json/Events/* for an example.

The overview will proceed to go over each key you would find in a regular Event .json, how their role changes, and if they're required in a addition.

.. note::

  ``"CardLimit"``, ``"Description":``, ``"requires"``, and ``"requiresEvent":`` are not checked for, and thus are irrelevant to Event additions. It is advised to exclude them for tidiness.

**name & CardType**
--------------------

::

  "name": "Lust Rune",

Required so you can tell the game which Event you wish to make an Addition to.

::

  "Addition": "Yes",

Required so you can tell the game you wish to make an addition. Can be added into almost any part of the file.

**Speakers**
-------------

::

  "Speakers": [
    {
    "name": "IDname of Monster you're adding",
    "postName": "",
    "SpeakerType": ""
    }
  ],

While required, it can be left without any objects if you don't intend to use it. All added objects will be additions, no exceptions.

This means if you want to say, add a ``"postName":`` to a character, you will be limited to appending the character again and using the appropriate
``"Speaks"`` function to use it. This isn't behavior specific to Additions either, this is intended base game behavior as seen for labeling multiple generics.

Note multiple mods adding to the Speakers key *could* throw ``"Speaks"`` out of order. Thus, it may be best to rely on :ref:`Speak` instead to avoid
compatibility issues between mods.

**EventText**
--------------

::

  "EventText": [
    {
    "NameOfScene": "Name of a Scene already in the game.",
    "theScene": [
      "The new strings provided to theScene."
      "Entirely replacing the original one."
      "JumpToScene", "A New Scene"
      ]
    },
    {
    "NameOfScene": "A New Scene",
    "theScene": [
      "An entirely new scene added to the event."
      ]
    }
  ]

Required, though you technically don't have to provide it with any objects.

Every new object will be appended, unless ``"NameOfScene":`` within the object matches an existing ``"NameOfScene":`` within the event, in which case
it will override and replace the entirety of ``"theScene":`` with the one provided via the object.

.. _MenuAddition:

**MenuAddition**
"""""""""""""""""
``"MenuAddition"`` will append additional choices to a :ref:`Menu` through a duplicate scene in the Addition with the same ``"NameOfScene":`` value.

This is for avoiding compatibility issues with other mods making additions to menus, notably those adding additional choices to say, the night life menu
for the Brothel. See the example below for details of the implementation.
Be sure to add the new scenes for these options in the same file. Do not override the scene you're adding the menu to.

If the menu you are adding to doesn't have a "FinalOption" for what is supposed to be the back-out choice you can safely add it to the choice in the scene under the presumption that other modders would do the same.

::

  "EventText": [
    {
    "NameOfScene": "The Scene Name",
    "theScene": [
      "MenuAddition",
        "New menu choice",
        "RequiresEnergy", "50",
        "The other new menu choice",
        "FinalOption", "Leave",
      "EndLoop"
      ]
    }
  ]
