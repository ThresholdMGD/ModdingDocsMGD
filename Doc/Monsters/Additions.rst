.. _Monster Additions:

**Monster Additions**
======================
Making an addition to a Monster

Check **_MonsterAdditionExample.json** in */Json/Monsters/* for an example.

The overview will proceed to go over each key you would find in a regular Monster .json, how their role changes, and if they're required in a addition.

If you want to change the stats of a monster, you can currently on do so via :ref:`StartOfCombat`, and using the related functions found here.

.. Remember to link the related functions.

.. note:: All other keys outside of the ones listed aren't used, and thus should not be included for tidiness.

**IDname**
-----------
::

  "IDname": "Elf",

Required so you can tell the game which Monster you wish to make an addition to.

**gender**
-----------
::

  "Addition": "Yes",

Required so you can tell the game that you're wishing to make an addition. Can be added into almost any part of the file.

**skillList**
--------------
::

  "skillList": ["Blowjob", "Thirsty Blowjob", "Super Suck"],

Appends to the existing array. Leave a blank string in the array if you don't intend to use it.

**perks**
----------
::

    "perks": ["Pacing"],

Appends to the existing array. Leave a blank string in the array if you don't intend to use it.

**itemDropList**
-----------------
::

  "ItemDropList": [
    {
    "name": "Elven Herbs",
    "dropChance": "75"
    },

    {
    "name": "Frog Rune",
    "dropChance": "75"
    }
  ],

Appends to the existing array of objects. Don't give the key an object if you don't wish to use it.

**lossScenes & victoryScenes**
-------------------------------
::

  "lossScenes": [
    {
    "NameOfScene": "Cuddling Loss",
    "move": "",
    "stance": "Cuddling",
    "includes": ["Elf"],
    "theScene":[
      "Speaks",
      "Cuddling is nice but can we bang instead?"
      ],
    "picture": ""
    }
  ],

  "victoryScenes": [
    {
    "NameOfScene": "Cuddling Victory",
    "move": "",
    "stance": "Cuddling",
    "includes": ["Elf"],
    "theScene":[
      "Speaks",
      "C-could we at least bang while cuddling?"
      ],
    "picture": ""
    }
  ],

Appends to the existing array of objects. Don't give the keys an object if you don't wish to use it.

You currently cannot replace existing scenes by copying their conditions and scene name.

**combatDialogue**
-------------------
::

  "combatDialogue": [
    {
    "lineTrigger": "UsesMove",
    "move": "Blowjob",
    "theText": [
      "Replaced dialogue."
      ]
    },
    {
    "lineTrigger": "StanceStruggleFree",
    "move": "Cuddling",
    "theText": [
      "'Th-that felt nicer than I thought it would...'"
      ]
    }
  ],

Appends to the existing array of objects, if there are no other objects that match it in exact requirements.
Otherwise, if it matches the ``"move":`` and ``"lineTrigger":`` keys in values, it will replace ``"theText":`` key data, not append to it.
Remember that ``"move":`` arrays is an *or* parameter,
so any skills or stances listed across multiple objects for the same type of lineTrigger will add to the same pool.

**pictures**
-------------
::

  "pictures": [

  ]

You can and should exclude the pictures key entirely if you don't intend to use it.
Otherwise, it is recommended to copy and paste the character's pictures key and work from there.
A more in-depth explanation on how to more minimally make image related additions will be given in the future as soon as some unexpected issues are resolved.

.. Making additions to blank pictures key data and general picture data additions to existing sets seems to have some issues, need to review before completing this section. I suck.
