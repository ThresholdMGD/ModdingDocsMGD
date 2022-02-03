**Monster Creation**
=====================

Breaks down the :doc:`keys and strings </Doc/Tutorials/TheJsonFormat>` used by Monsters. Despite its name, this does encompass all characters, including town NPCs.

Go to */Json/Monsters/*, and then see the .json files present for examples, and **_BlankMonster.json** for a template.

**Assume all keys are required, unless stated otherwise.**

**name & IDname**
------------------

.. code-block:: javascript

  "name": "monster name",

Sets the name of the monster that will be displayed to the player in-game.

.. code-block:: javascript

  "IDname": "monster IDname",

The internal name of the monster for use in json files. You will be working with this whenever a function or key asks for which monster you wish to refer to.

**species**
------------

.. code-block:: javascript

  "species": "Monster species",

This currently has no functionality, but is best included for forward-compatibility if it is ever introduced to the game.

When making a monster, you can refer to existing monster .jsons to see what their species is as reference towards what you decide on for yours.

**gender**
-----------

.. code-block:: javascript

  "gender": "female",

The gender of the monster. It primarily exists at the moment to distinguish normal monster jsons, and :doc:`Monster Additions </Doc/Monsters/Additions>`.

**description & encyclopedia**
-------------------------------

.. code-block:: javascript

  "description": "Monster description goes here.\n\nNote how the markup was called twice, and that space wasn't used.",

The description of a monster. This is given to the player in a card if the monster has no art, or if they disabled it in the options menu.

See :ref:`DialogueTextMarkup` for more information on the markup example in the above.

The string can technically be left blank if you intend to use art from the get-go, but it is still recommended.

.. code-block:: javascript

  "encyclopedia": "Lore information",

Lore related information given about monsters on the right hand side of the Grimoire during exploration. Doesn't necessarily need to be a generic enemy.

The string can be left blank if you don't intend for the Monster to be available by themselves via the monster selection in the Grimoire.

**tags**
---------

.. code-block:: javascript

  "tags": "none",

Like ``"species":``, it currently has no functionality, but is best included in case of future use. All monsters are currently given a value of ``"none"``.

**generic**
------------

.. code-block:: javascript

  "generic": "True",

Decides whether system related combat dialogue should refer to the monster as a generic character, e.g. slimes, elves, etc. or as a unique character, e.g.
Trisha, Perpetua, etc.

If they are generic, provide a value of ``"True"``. If they are unique, a value of ``"False"``.

**requires & requiresEvent**
-----------------------------

.. code-block:: javascript

  "requires": ["Vandal Note"],

Retrieve the ``"name:"`` key(s) of an :doc:`Item </Doc/Items/Creation>` to use as a requirement for players to access the monster, primarily for the Grimoire. Typically a Key Item.
The key must be included, but the array can be left empty. You can leave either a blank string or none at all.

.. code-block:: javascript

  "requiresEvent": [
    {
    "NameOfEvent": "",
    "Progress": "-99",
    "ChoiceNumber": "-1",
    "Choice": ""
    }
  ],

A more complex and optional key that contains objects that will check for progress or choice in a event. It can be used in alongside or as an alternative to ``"requires":``.

Given it is an array, you can introduce multiple requirements of the same type by providing duplicate objects for as long as it contains all four of the given keys.

You need to provide a value for ``"Progress":`` and ``"ChoiceNumber":``, else it will not work. If you don't wish to use one of them, use the default values above.
``"NameOfEvent":`` and ``"Choice":`` need at least empty strings.

If in use, you cannot exclude unused keys in the object, they must all be present.
If ``"requiresEvent":`` isn't being used at all, it can be excluded from the file entirely.

**skillList**
--------------

.. code-block:: javascript

  "skillList": ["Caress", "Kiss", "Kiss"],

The list of :doc:`Skills </Doc/Skills/Creation>` the monster can use while in combat, based on the exact value provided to a Skill's ``"name":`` key.
Repeating a skill will increase the chances the monster shall randomly call it.

See */Json/Skills/* for skills found in the base game that the monster can use. This does include player skills.

Provide a blank string if you don't wish to use the key.

**perks**
----------

.. code-block:: javascript

  "perks": ["Semen Eater", "Semen Eater", "Monster Pacing"],

The list of :doc:`Perks </Doc/Perks/Creation>` the monster can use while in combat, based on the exact value provided to a Perk's ``"name":`` key.
Repeating a Perk will apply it twice.

See */Json/Perks/* for perks found in the base game. Of note is the folder */EnemyOnlyPerks/*.

Provide a blank string if you don't wish to use the key.

**stats**
----------

.. code-block:: javascript

  "stats": {
    "lvl": "1",
    "Exp":"10",
    "max_hp":"80",
    "max_ep":"10",
    "max_sp": "1",
    "Power": "6",
    "Technique": "4",
    "Willpower": "7",
    "Allure": "7",
    "Luck": "3"
  },

The stats of the monster in combat. While otherwise straightforward, there are three keys in particular to be aware of:

* ``"max_ep":`` only pertains towards how quickly the monster can fall asleep. They will recover it in its entirety on orgasm. Threshold likes to use 30-50 for normal enemies, 100 for most bosses.
* ``"lvl":`` does effect exp gain modifiers relative to the player's level, so be sure to scale it appropriately to be a rough match for the location and general stats of the monster. Do remember you still have total creative freedom though.
* ``"Exp":`` represents the amount of exp given at the end of combat.

**Fetishes**
-------------

.. code-block:: javascript

  "Fetishes": ["Cock|/|50", "Anal|/|25"],

The list of fetishes a monster may have. See */Json/Fetishes/* for all base game fetishes. This does include addictions.

To apply the level of the fetish, use \|/\| as a separator between the fetish and the level within the same string,
and then provide a positive numerical value on the other side.

Provide a blank string if you don't wish to use the key.

**BodySensitivity**
--------------------

.. code-block:: javascript

  "BodySensitivity": {
    "Sex": "100",
    "Ass":"100",
    "Breasts":"100",
    "Mouth":"100",
    "Seduction": "100",
    "Magic": "100",
    "Pain": "100",
    "Holy": "100",
    "Unholy": "100"
  },

The sensitivities of the monster. Going above 100 makes them more sensitive, going below makes them less sensitive.

**resistancesStatusEffects**
-----------------------------

.. code-block:: javascript

  "resistancesStatusEffects": {
      "Stun": "0",
      "Charm": "0",
      "Aphrodisiac": "0",
      "Restraints": "0",
      "Sleep": "0",
      "Trance": "0",
      "Paralysis": "0"
      "Debuff": "0"
  },

The status effect resistances of the monster. A positive value increases their resistance, a negative value will decrease.

**moneyDropped & itemDropList**
-------------------------------

.. code-block:: javascript

  "moneyDropped": "25",

The amount of eros the monster provides.

.. code-block:: javascript

  "ItemDropList": [
    {
    "name": "Anaph Herb",
    "dropChance": "75"
    },

    {
    "name": "Anaph Rune",
    "dropChance": "75"
    }
  ],

Specify the name of the :doc:`Item </Doc/Items/Creation>` in ``"name":``, and provide the percent chance the item drops in ``"dropChance":``.
Make a new object for every additional item the monster can drop. Repeating items will increase the potential quantity of times they drop the item.

.. _lossScenes and victoryScenes:

**lossScenes & victoryScenes**
-------------------------------

.. code-block:: javascript

  "lossScenes": [
    {
    "NameOfScene": "Anal Loss",
    "move": "Thrust",
    "stance": "Anal",
    "includes": ["Elf", "Elf"],
    "theScene":[
      "This can tack functions that aren't event only.",
      "Check monsters in the base game for examples of it in action.",
      "You are also free to point it to an event at any point in the scene.",
      "JumpToEvent", "Example Event"
      ]
    "picture":""
    }
    {
    "NameOfScene": "Universal Loss",
    "move": "",
    "stance": "",
    "includes": [""],
    "theScene":[
      "Players don't have to be sent back to town in a loss scene, but do remember to recover their spirit a bit.",
      "An example would be Vili's Trial Of Titties lossScenes.",
      "Really, they are up to you in how you wish to use them."
      ]
    "picture":""
    }
  ],

Each object represents a scene that will play on loss. Each must be individually identified via the ``"NameOfScene":`` key.

**Requirements**
"""""""""""""""""

You can optionally provide parameters which allow certain scenes to take priority over other scenes depending on how the encounter ended.
In order of priority, top to bottom...

* ``"includes":`` covers monsters that are needed for the scene.
* ``"move":`` name of the skill that concluded the encounter.
* ``"stance":`` the stance that the monster is currently in. It currently can only cover one stance.


``"picture":`` is unused but technically functional. This changes the background picture upon starting the scene, but is largely succeeded by :ref:`ChangeBGFunc`.

Ensure you have one universal use scene with no requirements, else players can potentially cause the game to crash
from going to a scene that doesn't exist.

If you want to have menus or just generally more advanced scene logic, you can point the loss scene to immediately jump to an event.

.. code-block:: javascript

  "victoryScenes": [
    {
    "NameOfScene": "Anal Victory",
    "move": "",
    "stance": "Anal",
    "includes": ["Elf"],
    "theScene":[
      "Speaks",
      "I'm okay with my current situation."
      ],
    "picture": ""
    }
  ],

Functions exactly the same as ``"lossScenes":``, but for when the player wins.

.. _combatDialogueCreation:

**combatDialogue**
-------------------

.. code-block:: javascript

  "combatDialogue": [
    {
    "lineTrigger": "HitWith",
    "move": "Thrust",
    "theText":[
      "The chosen string displayed is random.",
      "You can have as many as you want, and repeat as many as you want for increased odds.",
      "You can have as many as you want, and repeat as many as you want for increased odds.",
      "'Put something in single quotes if you want it to be seen as something the character is saying.'"
      ]
    },
    {
    "lineTrigger": "UsesMove",
    "move": "Tighten",
    "theText": [
      "You don't need to use multiple strings if you're looking for a singular result.",
      ]
    }
  ],

``"combatDialogue":`` contains triggers in the form of objects that are checked for during combat to bring a result if it is matched.
It extends well beyond just dialogue responses and reactions during combat.

``"lineTrigger":`` decides what the trigger is checking for. **For a list of all possible triggers and how they work**, see :ref:`lineTriggers`.

``"move":`` a conditional parameter, most commonly used to represent a skill that was used.
**Can be an array to compact responses into one object, as it is an** *or* **parameter, not an** *and***.**
Compacting where possible is recommended as it does help reduce game load times.

``"theText":`` contains a list of all possible results of the trigger. It is random, but you can repeat strings to make some more common over others.

Note all matching ``"lineTrigger":`` and ``"move":`` values will ultimately go into the same pool the game randomly pulls from, as the game takes every
trigger in combatDialogue and translates the values from ``"theText:"`` into the same pool.

**pictures**
-------------

.. code-block:: javascript

  "pictures": [
    {
    "Name":"Base",
    "StartOn": "1",
    "AlwaysOn": "1",
    "IsScene": "0",
    "TheBody": "1",
    "Overlay": "No",
    "setXalign": "0.0",
    "setYalign": "0.16",
    "Player": "Yes",
    "Images":[
      {
      "Name":"Base",
      "File": "NPCs/Lillian/Lillian-neutral.png",
      "setXalign": "0.0",
      "setYalign": "0.0"
      },

      {
      "Name":"Happy",
      "File": "NPCs/Lillian/Lillian-happy.png",
      "setXalign": "0.0",
      "setYalign": "0.0"
      }
    ]
    }
  ]

The ``"pictures":`` key contains an array of objects, each representing a functional layer of images for the character.
For example, one object for the body layer, and another for the expressions, would be a basic setup. Or Lillian in the above code-block, who has them combined, making
for a more digestible overview.

There is a lot of keys to unpack for each object layer, so here is a brief overview:

.. list-table::
  :widths: 1 5

  * - ``"Name":``
    - Name of the layer for functions to call upon.
  * - ``"StartOn":``
    - Whether the layer is on by default when the character is first displayed
  * - ``"AlwaysOn":``
    - Whether the layer can never be turned off and instead always get the first image.
  * - ``"IsScene":``
    - Whether it is a scene, also ensuring it is centered on the screen, ignoring x and y align
  * - ``"TheBody":``
    - If the layer is the characters base. The x and y align of this layer dictates the x and y of every other layer.
  * - ``"Overlay":``
    - Put the name of another layer here to overlay this one on it. Any images with matching name fields will sync up. Check Shizu and Elly for an example.
  * - ``"setXalign":``
    - Changes the alignment of the layer on the x axis.
  * - ``"setYalign":``
    - Changes the alignment of the layer on the y axis.
  * - ``"Player": "Yes"``
    - Informs the game to recolor the target based on the player appearance set. You generally wont need to have this feild in the file at all, as it only needs to be there for the turning on of this feature.
  * - ``"Player": "Silhouette"``
    -  Additionally when using Player "Yes", you need to have another seperate image layer with "Player": "Silhouette" for the game to auto swap to if the player has set the appearance as a silhouette.


The ``"Images":`` key features an array where all the images for the layer go, each image being contained in an object. The objects work as follows:

.. list-table::
  :widths: 1 5

  * - ``"Name":``
    - Name of the image in the layer to be called in functions.
  * - ``"File":``
    - The file path to the image.
  * - ``"setXalign":``
    - Changes the alignment of the image on the x axis.
  * - ``"setYalign":``
    - Changes the alignment of the image on the y axis.

Layers are displayed in the order they are added into the ``"pictures":`` array,
so make sure everything is in the desired order to display correctly.
Note that the body layer doesn't need to be first, you can put layers behind it, such as with Amber for her cloak.

A more in-depth explanation and tips on the topic out of the scope of this page will be given in the future, such as how to use **Image Sets**,
which can let you set preset image layer setups for especially complex characters.
They can ranging from minor to drastic changes in character presentation for immense ease of use when swapping between certain looks in various scenarios.
In the meanwhile, check Aiko’s file for an example of Image Sets, containing multiple full sets of layers to swap between.

Alternatively, you can give a blank array if you intend to use a text based card description.

.. code-block:: javascript

  "pictures": [

  ]

.. The information is lacking in-depth examples and explanations, particularly for Image Sets. A dedicated page like lineTriggers will eventually be done.
