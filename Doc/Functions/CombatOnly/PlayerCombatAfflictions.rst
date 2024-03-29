**Player Combat Afflictions**
==============================

.. seealso:: 

    For afflictions that can be applied out of combat, see :doc:`Player Afflictions </Doc/Functions/General/PlayerAfflictions>`.

.. _DenyPlayerOrgasmFunc:

**DenyPlayerOrgasm**
-----------------------
The player is immune to normal orgasm calls (e.g. ``"PlayerOrgasm"`` still works) for the entire round of combat.

Also see :ref:`DenyCombatOrgasm`.

----

.. _HitPlayerWithFunc:

**HitPlayerWith**
------------------
Hit the player with a skill.
Will not apply stances or status effects from the skill, and does apply recoil damage.
It will only damage the target and can crit. It will never miss the target. Uses the stats of the focused monster.
**Do not use any skill with a** :ref:`targetTypeCreation` **that isn't** ``"single"``.

.. code-block:: javascript

  "HitPlayerWith", "Caress"

Displaying dialogue has to be done manually, it will not take dialogue from the skill.
If you want to display the damage number from the skill, use [DamageToPlayer] in the following :term:`string` after completing the function.

Check :ref:`DamagePlayerFromMonsterFunc` for an out of combat equivalent.
Check :ref:`DamageMonsterFromMonsterFunc` for an in of combat way to hit monsters with another monster.

----

**SkipPlayerAttack**
---------------------
Skips the players attack. Specifically intended for use with :ref:`Counters`. This also prevents the player from consuming the skill :ref:`costType<costType>`, and using consumables.
