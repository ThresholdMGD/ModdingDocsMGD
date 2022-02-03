.. _Items:

**Item Creation**
==================

Breaks down the :doc:`keys and strings </Doc/Tutorials/TheJsonFormat>` used by Items.

Go to *Json/Items/*, and then see the .json files present for examples, and **_BlankItem.json** for a template.

**Assume all keys are required, unless stated otherwise.**

**name**
---------

.. code-block:: javascript

  "name": "Name of item",

Sets the name of the item that will be displayed to the player in-game, and for internal referral.

**itemType**
-------------

.. code-block:: javascript

  "itemType": "The item type",

Decides the behavior and use cases of the item, greatly influencing how the following keys will behave.

.. list-table::
  :widths: 1 5

  * - ``"Key",``
    - You can apply perks through them, but not skills.
  * - ``"Accessory",``
    - You can apply both perks and skills through them.
  * - ``"Rune",``
    - You can apply both perks and skills through them.
  * - ``"Consumable",``
    - Can be used in and out of combat.
  * - ``"CombatConsumable",``
    - Can only be used in combat.
  * - ``"NotCombatConsumable",``
    - Can only be used outside of combat.
  * - ``"DissonantConsumable",``
    - Uses the chosen skill's **outcome** key value in combat, and the Item's **useOutcome** key value out of combat.
  * - ``"Loot",``
    - Cannot be used by the player. If you're looking to make it interactive, make it a **NotCombatConsumable** type and utilize the **useOutcome** key.

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

**requires & requiresEvent**
-----------------------------

.. code-block:: javascript

  "requires": ["Name of a required item", "Another item that may be required"],

Retrieve the ``"name:"`` key(s) another item to use as a requirement for players to access the item in shops. Typically a Key Item.

While the key must still be included, the array can be left empty if you do not wish to use it. You can leave either a blank string or none at all.

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

**perks**
----------

.. code-block:: javascript

  "perks": [""],

To apply perks via equipment related item types.

**skills**
-----------

.. code-block:: javascript

  "skills": [""],

For equipment item types, the key will give all listed skills for as long as the item is equipped.
**Take caution that it means runes can give a skill multiples times.**

For consumable item types, it will utilize the given skill upon use. **Note it can only take one skill, even if the key technically accepts an array.**
You have the option to provide a value of ``"UseableItem"``, which older consumable items used to directly apply the `Flat Stats Keys`_. Modern practices encourage using skills directly over ``"UseableItem"``.

**Flat Stats Keys**
--------------------

.. code-block:: javascript

  "hp": "0",
  "ep": "0",
  "sp": "0",

  "Exp": "0",

For consumable item types, flatly recovers or alters the corresponding stat based on the value. Negative values will have opposite effect.

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

* ``"statusEffect":`` cleanses the given status effect. Can use ``"all"`` to cleanse all status effects, or ``"None"`` if you don't intend to use it.
* ``"statusChance":`` represents a percent chance for it to successfully cleanse on use. A value of ``"0"`` or ``"100"`` will ensure it always cleanses.
* ``"statusPotency":`` for relevant status effects will clear the given amount of potency. A value of ``"0"`` cleanses it entirely.

See :ref:`Status Effects`.

**useOutcome & useMiss**
-------------------------

.. code-block:: javascript

  "useOutcome": "",

Provides a line of dialogue when using a consumable. Can use text markup and in-text functions.
Typically overridden by the listed Skill's outcome line, unless the ``"itemType":`` is ``"DissonantConsumable"``, or if it has no skill at all.


.. code-block:: javascript

  "useMiss": ""

Currently not used by the game. The key is optional and thus can be excluded, or be kept as placeholder.
