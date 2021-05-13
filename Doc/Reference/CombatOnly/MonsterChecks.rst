.. meta::
    :keywords: ifstatuseffect ifstatus

.. _Monster Checks:

**Monster Checks**
===================

.. note::

  **All of the functions below only work in :doc:`Event </Doc/Events/Creation>` based .json files.**

**IfThisMonsterIsInEncounter**
-------------------------------
Checks for the specified monster in the encounter, will ignore focused monster if checking for other with the same name.

::

  "IfThisMonsterIsInEncounter", "MonsterName", "SceneNameHere"

**EncounterSizeGreaterOrEqualTo & EncounterSizeLessOrEqualTo**
---------------------------------------------------------------
Checks if the current combat encounter has an equal or greater, or equal or less than respectively, of the given number of enemies.

::

  "EncounterSizeGreaterOrEqualTo", "2", "SceneNameHere"

**IfMonsterLevelGreaterThan**
------------------------------
Checks if the focused monster level is greater than the specified amount.


::

  "MonsterLevelGreaterThan", "39", "SceneNameHere"

**IfMonsterHasStatusEffect & IfMonsterDoesntHaveStatusEffect**
---------------------------------------------------------------
Checks if the focused monster does or doesn't have the specified status effect respectively. See :ref:`Status Effect`.

::

  "IfMonsterHasStatusEffect", "Restraint", "SceneNameHere"

**IfOtherMonsterHasStatusEffect & IfOtherMonsterDoesntHaveStatusEffect**
-------------------------------------------------------------------------
Same as the above, but checks for another monster. Note that it will shift focus to that monster. Ignores the currently focused monster.


::

  "IfOtherMonsterHasStatusEffect", "Himika", "Restraint", "SceneNameHere"

**IfMonsterHasStatusEffectWithPotencyEqualOrGreater**
------------------------------------------------------
Checks if the focused monster has a status effect with the given amount of potency. Note not all status effects use potency. Will shift focus to that monster.
Ignores the currently focused monster.

::

  "IfOtherMonsterHasStatusEffect", "Aphrodisiac", "50", "SceneNameHere"


**IfMonsterArousalGreaterThan**
--------------------------------
Checks if the monster's arousal is greater than the given number.

::

  "IfMonsterArousalGreaterThan", "120", "SceneNameHere"

**IfMonsterOrgasm**
--------------------
Checks if the current monster’s arousal will make them cum.

::

  "IfMonsterOrgasm", "SceneNameHere"

**CallMonsterEncounterOrgasmCheck**
------------------------------------
Checks if any monsters in a fight have orgasmed, and proceeds as if hit in combat.

::

  "CallMonsterEncounterOrgasmCheck", "SceneNameHere"

**IfMonsterSpiritGone**
------------------------
Checks if the monster is out of spirit. Made for use with enemies who have more than one spirit.

::

  "IfMonsterSpiritGone", "SceneNamehere"


**IfMonsterHasSkill & IfMonsterHasPerk**
-----------------------------------------
Checks if the monster has the skill or perk respectively. Useful for checking for skills or perks given to the monster by a separate event or scene.

::

  "IfMonsterHasSkill", "Caress", "SceneNameHere",
