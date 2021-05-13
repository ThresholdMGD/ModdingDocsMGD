.. _Adventure Additions:

**Adventure Additions**
========================
Making an addition to an Adventure will replace the base Adventure's ``"Deck":`` key with your own data.
This does mean your addition would be incompatible with other mods that make an addition to the same Adventure.

Check **_AdventureAdditionExample.json** in *Json/Adventures/* for an example.

The overview will proceed to go over each key you would find in a regular Adventure .json, how their role changes, and if they're required in a addition.

.. note::

  ``"Eros":``, ``"requiresEvent":``, and ``"Description":`` are not checked for, and thus are irrelevant to Adventure additions. It is advised to exclude them for tidiness.

**name**
---------

::

  "name": "Forest Dungeon",

Required so you can tell the game which Adventure you wish to make an addition to.

**requires**
-------------

::

  "Addition": "Yes",

Required so you can tell the game that you're wishing to make an addition. Can be added into almost any part of the file.

**Deck**
---------

::

  "Deck": [
    "Event", "Name of an event",
    "RandomTreasure",
    "BreakSpot",
    "Monster", "Imp", "EndLoop",
    "RandomEvent"
  ],

Required, ``"Deck":`` **cannot** be excluded, nor left empty, even if your goal isn't to modify the deck.

It is advised to copy and paste the array from the Adventure's original ``"Deck":`` key as the basis of your addition, and go from there.

**RandomEvents**
-----------------

::

  "RandomEvents": ["Lust Rune", "Ninja Rest Ambush"],

Using this key in a addition adds to the existing array. The strings provided in the original ``"RandomEvents":`` key will still be present, and not overridden.
As such, you are only increasing the selection of events, not replacing, unlike the ``"Deck":`` key.

**RandomMonsters & MonsterGroups**
-----------------------------------

::

  "RandomMonsters": ["Elf"],
  "MonsterGroups": [
    {
    "Group": ["Elf", "Elf"]
    }
  ],

Using these keys in an addition adds to the existing arrays, so the strings provided in the original keys will still be present, and will not be overridden.
As such, you are only increasing the selection of monster groups, not replacing.

These keys are required, but the arrays can be left empty if you do not wish to use it. ``"MonsterGroups":`` does not require an object.

**Treasure**
-------------

::

  "Treasure": [
    {
    "Common": ["Anaph Herb", "Ugli Herb"]
    },

    {
    "Uncommon": ["Unbound Rune", "Unbound Rune", "Soothing Potion"]
    },

    {
    "Rare": ["Panacea", "Energy Potion", "Cock Ring of Justice", "Power Belt"]
    }
  ],

Using this key in a addition adds to the existing array, so the strings provided in the original key will still be present, and will not be overridden.
As such, you are only increasing the selection of loot, not replacing.

``"Treasure":`` and its objects are required, but the arrays can be left empty if you do not wish to use it.
