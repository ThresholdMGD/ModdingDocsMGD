**Adventure Creation**
=======================

Breaks down the :doc:`keys and :term:`strings` </Doc/Tutorials/TheJsonFormat>` used by Adventures.

Go to *Json/Adventures/*, and then see the *.json* files present for examples, and **_BlankAdventure.json** for a template.

**Assume all :term:`keys` are required, unless stated otherwise.**

**name**
---------

.. code-block:: javascript

  "name": "Name of an Adventure",

Sets the name of the adventure for the menu choice of a location on the map.

**Description**
----------------

.. code-block:: javascript

  "Description": "Description of the Adventure.",

Give a brief description of the adventure. Currently unused in-game, but is expected.

**requires & requiresEvent**
-----------------------------

.. code-block:: javascript

  "requires": ["Name of a required item", "Another item that may be required"],

Retrieve the ``"name:"`` key(s) of an :doc:`Item </Doc/Manual/Items/Items>` to use as a requirement for players to access the adventure. Typically a :term:`key` Item.

While the :term:`key` must still be included, the :term:`array` can be left empty if you do not wish to use it. You can leave either a blank :term:`string` or none at all.

.. code-block:: javascript

  "requiresEvent": [
    {
    "NameOfEvent": "",
    "Progress": "-99",
    "ChoiceNumber": "-1",
    "Choice": ""
    }
  ],

A more complex and optional :term:`key` that contains :term:`objects` that will check for progress or choice in a event. It can be used in alongside or as an alternative to ``"requires":``.

Given it's an array, you can introduce multiple requirements of the same type by providing duplicate :term:`objects` for as long as it contains all four of the given keys.

You need to provide a :term:`value` for ``"Progress":`` and ``"ChoiceNumber":``, else it will not work. If you don't wish to use one of them, use the default :term:`values` above.
``"NameOfEvent":`` and ``"Choice":`` need at least empty strings.

If in use, you cannot exclude unused :term:`keys` in the object, they must all be present.
If ``"requiresEvent":`` isn't being used at all, it can be excluded from the file entirely.

**MusicList**
--------------

.. code-block:: javascript

    "MusicList": [ "music/Mountain/Purple Planet Music - Chilled - Desert Winds (3_12).mp3"],

An optional :term:`key` for a default selection of music to loop through during adventures outside of events and encounters.

**Deck**
---------

.. code-block:: javascript

  "Deck": [
    "Event", "Name of an event",
    "Monster", "Elf", "EndLoop",
    "BreakSpot",
    "Monster", "Blue Slime", "Elf", "EndLoop",
    "RandomTreasure",
    "RandomEvent"
  ],

Specify the order of encounters and events the player will face upon starting the adventure, linearly as given from start to finish.
It can technically be left empty, but doing so will just send players straight back to town upon selection of the adventure, giving the adventure no purpose.

Below are all the :term:`values` you can provide within the :term:`array` to trigger various interactions.

========================= =====================================================================================================================================================================================================================================
Value                     Description                                                                                                                                                                                                                          
========================= =====================================================================================================================================================================================================================================
``"Event",``              Jumps to an event given in the following string.                                                                                                                                                                                     
``"Monster",``            Starts a monster encounter. Provide a :term:`string` of the IDname of each included monster, close the list with ``"EndLoop"``.                                                                                                      
``"RandomEvent",``        Random event from the **RandomEvents** :term:`key` below.                                                                                                                                                                            
``"RandomMonsters",``     Random encounter from the `RandomMonsters & MonsterGroups`_ :term:`keys` below.                                                                                                                                                      
``"RandomTreasure",``     Random treasure of random rarity from the `Treasure & Eros`_ :term:`keys` below.                                                                                                                                                     
``"CommonTreasure",``     Random common treasure from the `Treasure & Eros`_ ``"Common":`` :term:`keys` below.                                                                                                                                                 
``"UncommonTreasure",``   Random uncommon treasure from the `Treasure & Eros`_ ``"Uncommon":`` :term:`keys` below.                                                                                                                                             
``"RareTreasure",``       Random rare treasure treasure from the `Treasure & Eros`_ ``"Rare":`` :term:`keys` below.                                                                                                                                            
``"BreakSpot",``          Break spot. The player can choose to move on, rest, or return to town.                                                                                                                                                               
``"Unrepeatable"``        Upon reaching this :term:`string` in a deck, the adventure becomes unavailable for repeating, preventing the player from accessing the adventure again. **Do not use this if you want players to be able to replay the adventure**.  
========================= =====================================================================================================================================================================================================================================

Remember to make sure the last :term:`string` you provide doesn't have a trailing comma.

**RandomEvents**
-----------------
.. code-block:: javascript

  "RandomEvents": ["Lust Rune", "Elven Ambush"],

Set the random events that can be selected by the ``"RandomEvent"`` :term:`string` for the ``"Deck":`` :term:`key` above. If you wish to make certain events more likely, put it in multiple times.

.. Perhaps the :term:`string` name should be consistent to the :term:`key` name like the others, or the :term:`key` consistent to the string?

**RandomMonsters & MonsterGroups**
-----------------------------------
.. code-block:: javascript

  "RandomMonsters": ["Blue Slime", "Lizard Girl"],

Set the random monsters you can encounter for the ``"RandomMonsters"`` :term:`string` for the ``"Deck":`` :term:`key` above.
If you wish to make a certain monster more likely, put them in multiple times.
Requires use of the ``"MonsterGroups":``, found below.

.. code-block:: javascript

  "MonsterGroups": [
    {
    "Group": ["Blue Slime", "Elf"]
    },

    {
    "Group": ["Lizard Girl"]
    }
  ],

Sets the possible formations monsters in the ``"RandomMonsters":`` can take. Each :term:`object` with a ``"Group":`` :term:`key` will represent a different possible formation.
You can intermix different monsters via the arrays, even if the monster isn't present in ``"RandomMonsters":``.
Repeat an :term:`object` with a certain formation multiple times if you wish to make it more likely.
Works the same as a :doc:`Location's </Doc/Manual/Locations/Locations>` ``"MonsterGroups":``.

While the :term:`key` is required, you do not have to provide an :term:`object` if you do not wish to use formations.

**Treasure & Eros**
--------------------
.. code-block:: javascript

  "Treasure": [
    {
    "Common": ["Calming Potion", "Calming Potion", "Anaph Herb", "Ugli Herb"]
    },

    {
    "Uncommon": ["Calming Potion", "Energy Potion", "Luck Rune", "Luck Rune", "Soothing Potion"]
    },

    {
    "Rare": ["Panacea", "Stoic Rune", "Stoic Rune", "Gloves of Skill", "Gloves of Skill", "Power Belt"]
    }
  ],

Sets the possible items that can be earned from chests for each type of treasure rarity.
The listed :term:`objects` and their :term:`keys` must be included, and each :term:`array` must have at least one item.

.. code-block:: javascript

  "Eros": [
    {
    "Common": "25"
    },

    {
    "Uncommon": "75"
    },

    {
    "Rare": "150"
    }
  ]

Sets the amount of eros given from chests for each type of treasure rarity in the adventure from treasure in the `Deck`_.
The listed :term:`objects` and their :term:`keys` must be included, and each :term:`key` must provide a :term:`value` in their string.
