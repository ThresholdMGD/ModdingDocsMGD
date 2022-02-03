**Location Additions**
=======================
Making a Location addition is non-destructive and thus will be compatible with any other mods making additions to the same Location.

Check **_ForestAdditionExample.json** in *Json/Locations/* for an example.

The overview will proceed to go over each key you would find in a regular Location .json, how their role changes, and if they're required in a addition.

.. note:: 
  
  All other keys outside of the ones listed aren't used, and thus should not be included for tidiness.

**name & exploreTitle**
------------------------
.. code-block:: javascript

  "name": "Mystic Forest",

Required so the game knows which location you wish to make an addition to.

.. code-block:: javascript

  "Addition": "Yes",


Required so the game knows you wish to make an addition. Can be added into almost any part of the file.

**Monsters & MonsterGroups**
-----------------------------
.. code-block:: javascript

  "Monsters": ["Minotaur", "Nicci"],

.. code-block:: javascript

  "MonsterGroups": [
    {
    "Group": ["Blue Slime", "Blue Slime", "Blue Slime", "Blue Slime"]
    },
    {
    "Group": ["Demon Queen", "Blue Slime"]
    }
  ],

Using these keys in an addition adds to the existing arrays, so the strings provided in the original keys will still be present, and will not be overridden.
As such, you are only increasing the selection of monster and monster groups, not replacing.

These keys are required, but the arrays can be left empty if you do not wish to use it. ``"MonsterGroups":`` does not require an object.

**Events**
-----------
.. code-block:: javascript

    "Events": ["NewEvent"],

Appends to the existing array. Leave a blank string in the array if you don't intend to use it.

Duplicates are checked for and ignored, avoiding mod conflicts.

**Quests**
-----------

.. code-block:: javascript

    "Quests": ["NewQuest"],

Appends to the existing array. Leave a blank string in the array if you don't intend to use it.

Duplicates are checked for and ignored, avoiding mod conflicts.

**Adventures**
---------------

.. code-block:: javascript

    "Adventures": ["NewAdventure"],

Appends to the existing array. Leave a blank string in the array if you don't intend to use it.

Duplicates are checked for and ignored, avoiding mod conflicts.

**Treasure**
-------------

.. code-block:: javascript

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
