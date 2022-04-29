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

.. code-block:: javascript

  "IfThisMonsterIsInEncounter", "MonsterName", "SceneNameHere"

----

**EncounterSizeGreaterOrEqualTo & EncounterSizeLessOrEqualTo**
---------------------------------------------------------------
Checks if the current combat encounter has an equal or greater, or equal or less than respectively, of the given number of enemies.

.. code-block:: javascript

  "EncounterSizeGreaterOrEqualTo", "2", "SceneNameHere"

----

**IfMonsterLevelGreaterThan**
------------------------------
Checks if the focused monster level is greater than the specified amount.


.. code-block:: javascript

  "MonsterLevelGreaterThan", "39", "SceneNameHere"

----

**IfMonsterHasStatusEffect & IfMonsterDoesntHaveStatusEffect**
---------------------------------------------------------------
Checks if the focused monster does or doesn't have the specified status effect respectively. See :ref:`Status Effect`.

.. code-block:: javascript

  "IfMonsterHasStatusEffect", "Restraint", "SceneNameHere"

----

**IfOtherMonsterHasStatusEffect & IfOtherMonsterDoesntHaveStatusEffect**
-------------------------------------------------------------------------
Same as the above, but checks for another monster. Note that it will shift focus to that monster. Ignores the currently focused monster.


.. code-block:: javascript

  "IfOtherMonsterHasStatusEffect", "Himika", "Restraint", "SceneNameHere"

----

**IfMonsterHasStatusEffectWithPotencyEqualOrGreater**
------------------------------------------------------
Checks if the focused monster has a status effect with the given amount of potency. Note not all status effects use potency. Will shift focus to that monster.
Ignores the currently focused monster.

.. code-block:: javascript

  "IfOtherMonsterHasStatusEffect", "Aphrodisiac", "50", "SceneNameHere"

----

**IfMonsterArousalGreaterThan**
--------------------------------
Checks if the monster's arousal is greater than the given number.

.. code-block:: javascript

  "IfMonsterArousalGreaterThan", "120", "SceneNameHere"

----

**IfMonsterOrgasm**
--------------------
Checks if the current monster's arousal will make them cum.

.. code-block:: javascript

  "IfMonsterOrgasm", "SceneNameHere"

----

**IfMonsterEnergyGone**
-------------------------

Checks if the current monster's energy is 0.

.. code-block:: javascript

  "IfMonsterEnergyGone", "SceneNameHere"

----

**CallMonsterEncounterOrgasmCheck**
------------------------------------
Checks if any monsters in a fight have orgasmed, and proceeds as if hit in combat.

.. code-block:: javascript

  "CallMonsterEncounterOrgasmCheck", "SceneNameHere"

----

**IfMonsterSpiritGone**
------------------------
Checks if the monster is out of spirit. Made for use with enemies who have more than one spirit.

.. code-block:: javascript

  "IfMonsterSpiritGone", "SceneNamehere"

----

**IfMonsterHasSkill & IfMonsterHasPerk**
-----------------------------------------
Checks if the monster has the skill or perk respectively. Useful for checking for skills or perks given to the monster by a separate event or scene.

.. code-block:: javascript

  "IfMonsterHasSkill", "Caress", "SceneNameHere",
