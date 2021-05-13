.. meta::
    :keywords: ifhas ifstatus ifstatuseffect

.. _Player Checks:

**Player Checks**
==================

.. tip::

  See :ref:`Player Combat Checks` for checks exclusive to combat.

**IfStatEqualsOrMore**
-----------------------
Checks the following stat against the given number, if the stat is equal or higher, it jumps to the scene, else it continues. See :ref:`Stats`.

::

  "StatEqualsOrMore", "Power", "5", "SceneNameHere"

**HasErosLessThan**
--------------------
If player has less eros than the given amount, it jumps to the scene, else it continues.

::

  "HasErosLessThan", "100", "SceneNameHere"

**VirilityEqualsOrGreater**
----------------------------
If the player virility is greater than the given number, it jumps to the scene, else it continues.

::

  "VirilityEqualsOrGreater", "100", "SceneNameHere"

**IfPlayerOrgasm**
-------------------
Checks if the players current arousal is over their maximum arousal. If true, it then goes to the given scene, else it continues.

::

    "IfPlayerOrgasm", "SceneNameHere"

**IfPlayerArousalOverPercentOfMax**
------------------------------------
Checks if the players current arousal is over a certain percent of their maximum arousal. If true, it jump to the given scene, else it continues.

Note you can go over 100%, though it might be superseded by an orgasm call when used while in combat if it isn't per-preemptive.

::

  "IfPlayerArousalOverPercentOfMax", "50", "SceneNameHere"

**IfPlayerSpiritGone**
-----------------------
Check if the player is out of spirit, if true, it jumps to the given scene, else it continues.

::

  "IfPlayerSpiritGone", "SceneNameHere"

**IfPlayerEnergyGone**
-----------------------
Same as above, but for the player’s energy.

::

  "IfPlayerEnergyGone", "SceneNameHere"

**IfPlayerEnergyLessThanPercent**
----------------------------------
Checks if the player energy is less than the given percentage of their maximum, if true, it jumps to the given scene, else it continues.

::

  "IfPlayerEnergyLessThanPercent", "50", "SceneNameHere"

**IfSensitivityEqualOrGreater**
--------------------------------
Checks if the given sensitivity for the player is equal to or greater than the given value. If true, it jumps to the given scene, else it continues.

::

  "IfSensitivityEqualOrGreater", "Sex", "120", "SceneNameHere"



**IfHasFetish**
----------------
Checks if the player has the following fetish (which requires being level 25 or higher), if true, it jumps to the given scene, else it continues.


::

  "IfHasFetish", "Oral", "SceneNameHere"

**IfFetishLevelEqualOrGreater**
--------------------------------
Checks if the player has an equal or greater level of the given fetish, if true, it jumps to the given scene, else it continues.

::

  "IfFetishLevelEqualOrGreater", "Ass", "60", "SceneNameHere"

**IfHasSkill**
---------------
Checks if the player has the following skill. If true, it jumps to the given scene, else it continues.

::

  "IfHasSkill", "Arousara", "SceneNameHere"

**IfHasItem & IfDoesntHaveItem**
---------------------------------
Checks if the player does or doesn't respectively have an item in their inventory or equipped.

::

  "IfHasItem", "Vandal's Note", "SceneNameHere"

::

  "IfDoesntHaveItem", "Vandal's Note", "SceneNameHere"

**IfHasItemEquipped**
----------------------
Checks if the player has the specified item equipped. If true, it jumps to the given scene, else it continues.

::

  "IfHasItemEquipped", "Hero's Cape", "SceneNameHere"

**IfHasItemInInventory**
-------------------------
Checks if the player has the specified amount of an item in their inventory, ignoring their equipment slots. If true, it jumps to the given scene, else it continues.

::

  "IfHasItemInInventory", "Anaph Herb", "1", "SceneNameHere"

**IfHasPerk**
--------------
Checks if the player has the following perk. If true, it jumps to the given scene, else it continues.

::

  "IfHasPerk", "Sadist", "SceneNameHere"

**IfPlayerLevelGreaterThan**
-----------------------------
Checks if the player level is equal or greater than the specified amount. If true, it jumps to the given scene, else it continues.

::

  "IfPlayerLevelGreaterThan", "50", "SceneNameHere"

**IfInExploration**
--------------------
If the player is in Exploration via the Grimoire, rather than an Adventure. If true, it jumps to the given scene, else it continues.

::

  "IfInExploration", "SceneNameHere"
