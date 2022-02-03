**Perk Creation**
==================

Breaks down the :doc:`keys and strings </Doc/Tutorials/TheJsonFormat>` used by Perks.

Go to *Json/Perks/*, and then see the *.json* files present for examples, and **_BlankPerk.json** for a template.

Assume all keys are required, unless stated otherwise.

**name**
---------

.. code-block:: javascript

  "name": "Blank Perk",

Sets the name of the perk to be presented to the player in-game, and for internal referral.

**description**
----------------

.. code-block:: javascript

  "description": "",

The description of the perk that is displayed both in the level up menu and the players list of perks in the character menu.
``|perkDuration|`` can be inserted at the end of the description to display the time remaining.

**LevelReq**
-------------

.. code-block:: javascript

  "LevelReq": "0",

Level needed to be able to acquire the perk. Leave a value of 0 if not desired.

**PerkReq**
------------

.. code-block:: javascript

  "PerkReq": [""],

Perks required to be able to acquire the perk. Useful for tiered perks intended for the level up menu. Leave an empty string if not desired.

**StatReq & StatReqAmount**
----------------------------

.. code-block:: javascript

  "StatReq": ["Allure", "Power"],

Stats required to be able to acquire the perk. See :ref:`Stats`
Leave an empty string in the array if not desired.

.. code-block:: javascript

  "StatReqAmount": ["6", "9"],

The amount the player needs for each stat in ``"StatReq":``. It is set to match each string from ``"StatReq":``.

As an example, the first string of ``"6"`` would go to ``"Allure"``, and the following string ``"9"`` would go to the following string ``"Power"``, and so forth.

**PerkType**
-------------

.. code-block:: javascript

  "PerkType": ["PenetrationBoost"],

The perk types, deciding what the perk does to the perk owner. See :doc:`Perk Types </Doc/Perks/Types>` for the list of perk types and their respective effects.

**EffectPower**
----------------

.. code-block:: javascript

  "EffectPower": ["-34"],

The strength/variable for the corresponding perk types from ``"PerkType":`` based on their positions in their respective arrays to the other.

Varies by effect. See :doc:`Perk Types </Doc/Perks/Types>` for the list of perk types and their respective effects.

**PlayerCanPurchase**
----------------------

.. code-block:: javascript

  "PlayerCanPurchase": "No"

Decides whether or not the player can purchase it with perk points from the level up menu.

* ``"Yes"`` will let the player view and purchase it with perk points from the level up menu.

* ``"No"`` will prevent the player from purchasing it via the level up menu.

* ``"HiddenCompletelyFromPlayer"`` will both prevent the player from purchasing it via the level up menu and prevent it from showing in the player's list of perks in the character menu. Used for perks meant for :doc:`Items </Doc/Items/Creation>`.
