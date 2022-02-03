**Monster Attacks**
====================

**SemenHeal**
--------------

Heals the focused monster based on the given number and the same calculation as the semen eater perk type.
``"{FinalDamage}"`` can be used in the following string to display how much arousal is recovered.

.. code-block:: javascript

  "SemenHeal", "25"

----

**EnergyDrain**
----------------

Drains energy from the player using the same calculation as the energy drain perk. ``"{FinalDamage}"`` can be used in the following string to display how much energy is lost.

It can be used out of combat.

.. code-block:: javascript

  "EnergyDrain", "25"

----

**SetSkipMonsterAttack**
-------------------------

``"SetSkipMonsterAttack"`` sets the focused monster to skip their attack call for the round.

----

**SetResumeMonsterAttack**
---------------------------

``"SetResumeMonsterAttack"`` sets the focused monster to attack for the round again.

----

**SkipAllMonsterAttacks**
--------------------------

``"SkipAllMonsterAttacks"`` sets all monsters in the fight to no longer attack for the round.

----

**ResumeAllMonsterAttacks**
----------------------------

``"ResumeAllMonsterAttacks"`` sets all monsters in the fight to attack for the round again.

----

**CallMonsterAttack**
----------------------

Calls the focused monster’s turn attack turn. Intended for use at the end of turn if a counter attack set up fails, but has other applications.

.. code-block:: javascript

  "CallMonsterAttack"

You can use its sub-function ``SpecificAttack`` to make the focused monster cast a specific skill.

.. code-block:: javascript

  "CallMonsterAttack", "SpecificAttack", "Charm",

Note that this wouldn't use the monsters skill selection AI, so they may end up trying to use a skill that won't work.
This is a good method for having a combat event use a status effect check normally.

----

**EndCounterChecks**
---------------------

``"EndCounterChecks"`` is used and *required* for characters with multiple separate counters from :ref:`lineTriggers`
to stop them from overlapping when you don’t want to.
