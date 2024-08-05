.. _Items:

**Item Creation**
==================

.. * **Items** | Contains consumables, equipment, and :term:`key` items, defining their :term:`values` and effects.

Breaks down the :doc:`keys and :term:`strings` </Doc/Tutorials/TheJsonFormat>` used by Items.

Go to *Json/Items/*, and then see the .json files present for examples, and **_BlankItem.json** for a template.

**Assume all :term:`keys` are required, unless stated otherwise.**

**name**
---------

.. code-block:: javascript

  "name": "Name of item",

Sets the name of the item that will be displayed to the player in-game, and for internal referral.

**itemType**
-------------

.. code-block:: javascript

  "itemType": "The item type",

Decides the behavior and use cases of the item, greatly influencing how the following :term:`keys` will behave.

+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+---------------------------------------+----------------------------+
| :term:`values`                     | Description                                                                                                                                | Perks :term:`key` Behavior            | Skills :term:`key` Behavior           | Stats :term:`key` Behavior |
+============================+====================================================================================================================================================+=======================================+=======================================+============================+
| ``"Accessory",``           | A type of equipment. Only applied while worn.                                                                                                      | Gives perk while worn.                | Gives skill while worn.               | Alters stats while worn.   |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+---------------------------------------+----------------------------+
| ``"Rune",``                | A type of equipment. Only applied while worn.                                                                                                      | Gives perk while worn.                | Gives skill while worn.               | Alters stats while worn.   |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+---------------------------------------+----------------------------+
| ``"Consumable",``          | Can be used in and out of combat encounters.                                                                                                       | None, see `useOutcome`_ instead.                                              | Alters stats when used.    |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+                                                                               +                            +
| ``"CombatConsumable",``    | Can only be used in combat encounters.                                                                                                             |                                                                               |                            |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+                                                                               +                            +
| ``"NotCombatConsumable",`` | Can only be used outside of combat encounters.                                                                                                     |                                                                               |                            |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+                                                                               +                            +
| ``"DissonantConsumable",`` | Uses the chosen skill's **outcome** :term:`key` :term:`value` in combat, and the Item's **useOutcome** :term:`key` :term:`value` out of combat.    |                                                                               |                            |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+---------------------------------------+----------------------------+
| ``"Key",``                 | Called a **Key Item** in-game.                                                                                                                     | None                                                                                                       |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+                                                                                                            +
| ``"Loot",``                | Cannot be used by the player. If you're looking to make it interactive, make it a **NotCombatConsumable** type and utilize the **useOutcome** key. |                                                                                                            |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+---------------------------------------+----------------------------+

**cost**
---------

.. code-block:: javascript

  "cost": "0",

The cost of the item in shops. For reference, the sell cost will always be 50% of the provided value.

**descrip**
------------

.. code-block:: javascript

  "descrip": "",

The description of the item that is displayed both in shops and the character inventory. 
Be sure to use :ref:`itemmarkup` to grab the values from the item's :ref:`itemflatstatkeys`.

.. _itemTags:

**tags**
---------

.. code-block:: javascript

  "tags": ["Tag Name Here", "Another Tag"],

Categorizes items together when they share a tag value, such as for use in :ref:`Item Functions <itemFunctions>`.


**requires & requiresEvent**
-----------------------------

.. code-block:: javascript

  "requires": ["Name of a required item", "Another item that may be required"],

Retrieve the ``"name:"`` key(s) another item to use as a requirement for players to access the item in shops. Typically a :term:`key` Item.

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

**perks**
----------

.. code-block:: javascript

  "perks": [""],

To apply perks via equipment related item types.

**skills**
-----------

.. code-block:: javascript

  "skills": [""],

For equipment item types, the :term:`key` will give all listed skills for as long as the item is equipped.
**Take caution that it means runes can give a skill multiples times.**

For consumable item types, it will utilize the given skill upon use. **Note it can only take one skill, even if the :term:`key` technically accepts an array.**
You have the option to provide a :term:`value` of ``"UseableItem"``, which older consumable items used to directly apply the `Flat Stats Keys`_. Modern practices encourage using skills directly over ``"UseableItem"``.

.. _ItemFlatStatKeys:

**Flat Stats Keys**
--------------------

.. code-block:: javascript

  "hp": "0",
  "ep": "0",
  "sp": "0",

  "Exp": "0",

For consumable item types, flatly recovers or alters the corresponding stat based on the value. Negative :term:`values` will have opposite effect.

Equipment and loot item types will instead flatly influence the corresponding stat by its max, ignoring ``"Exp":``.  Can use negative values.

It can be used in combination with ``"skills":``.

**Core Stat & Resistance Keys**
--------------------------------

.. code-block:: javascript

  "Power": "0",
  "Technique": "0",
  "Intelligence": "0",
  "Allure": "0",
  "Willpower": "0",
  "Luck": "0",

  "BodySensitivity": {
      "Sex": "0",
      "Ass": "0",
      "Breasts": "0",
      "Mouth": "0",
      "Seduction": "0",
      "Magic": "0",
      "Pain": "0",
      "Holy": "0",
      "Unholy": "0"
  },

  "resistancesStatusEffects": {
      "Stun": "0",
      "Charm": "0",
      "Aphrodisiac": "0",
      "Restraints": "0",
      "Sleep": "0",
      "Trance": "0",
      "Paralysis": "0",
      "Debuff": "0"
  },

Only applicable to equipment and loot item types. Alters the given stat for the wielder, can use negative values.

**Status Effect Keys**
-----------------------

.. code-block:: javascript

  "statusEffect": "None",
  "statusChance": "0",
  "statusPotency": "0",

Only applicable to consumable item types.

====================== =========================================================================== ========================================================================================== 
Key                    Description                                                                 Special :term:`values`                                                                            
====================== =========================================================================== ========================================================================================== 
``"statusEffect":``    Cleanses the given status effect.                                           ``"all"`` will cleanse all status effects. Use ``"None"`` if you don't intend to use it.  
``"statusChance":``    The percent chance for it to successfully cleanse on use.                   ``"0"`` or ``"100"`` will ensure it always cleanses.                                      
``"statusPotency":``   Subtracts by the given amount from status effect's potency if applicable.   ``"0"`` cleanses it entirely.                                                             
====================== =========================================================================== ========================================================================================== 

See :ref:`Status Effects`.

**useOutcome**
---------------

.. code-block:: javascript

  "useOutcome": "",

Provides a line of dialogue when using a consumable. Can use text markup and in-text functions.
Typically overridden by the listed Skill's outcome line, unless the ``"itemType":`` is ``"DissonantConsumable"``, or if it has no skill at all.


**useMiss**
------------

.. code-block:: javascript

  "useMiss": ""

Currently not used by the game. The :term:`key` is optional and thus can be excluded, or be kept as placeholder.
