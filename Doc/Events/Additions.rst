.. _Event Additions:

**Event Additions**
====================

Event additions cover replacing specific scenes, adding new scenes, and appending to the list of ``"Speakers"``.

This does mean your addition would be incompatible with other mods that make an addition to the same scenes in an Event.
This is excluding scenes solely using :ref:`MenuAddition`, for example, when adding to the night life menu in the brothel.

Check **_EventAdditionExample.json** in *Json/Events/* for an example.

The overview will proceed to go over valid keys in event additions, how they're added to the base event json, and if their inclusion is required.

.. note::

  ``"CardType":`` ``"CardLimit":``, ``"Description":``, ``"requires"``, and ``"requiresEvent":`` aren't used, and thus should be excluded for tidiness.

**name & Addition**
--------------------

.. code-block:: javascript

  "name": "Lust Rune",

Required so you can tell the game which Event you wish to make an addition to.

.. code-block:: javascript

  "Addition": "Yes",

Required so the game knows you are making an addition.


**Speakers**
-------------

.. code-block:: javascript

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

Note multiple mods adding to the Speakers key *could* throw ``"Speaks"`` out of order depending on which mod is loaded first.
Thus, it may be best to rely on :ref:`SpeakFunc` for any new speakers instead to avoid compatibility issues between mods.

**EventText**
--------------

.. code-block:: javascript

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
it will override and replace the entirety of ``"theScene":`` with the one provided via the new object.
The exception to this behavior is when using ``"MenuAddition"``.

.. _MenuAddition:

**MenuAddition**
"""""""""""""""""

The :doc:`function </Doc/Reference/Functions>`  ``"MenuAddition"`` will append additional choices to a :ref:`MenuFunc` through a duplicate scene in the addition with the same ``"NameOfScene":`` value.

This is for avoiding compatibility issues with other mods making additions to menus, notably those adding additional choices to say, the night life menu
for the Brothel. See the example below for details of the implementation, and the _MenuAdditionExample.json file in the game folders for a further example to experiment with if needed.

If the menu you are adding to from the base doesn't have a ``"FinalOption"`` in use already, it is intended to be applied to back out or leave options so it's always at the bottom of the menu,
``"OverrideOption"`` must be used prior to a menu choice such as ``"FinalOption"`` so it properly clears any duplicates of the original choice in the menu while ensuring no compatibility issues should arise with other mods.

.. code-block:: javascript

  "EventText": [
    {
    "NameOfScene": "The Scene Name",
    "theScene": [
      "MenuAddition",
        "New menu choice",
        "RequiresEnergy", "50",
        "The other new menu choice",
        "OverrideOption", "FinalOption", "Leave",
      "EndLoop"
      ]
    }
  ]
