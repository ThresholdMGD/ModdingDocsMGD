.. _Player Afflictions:

**Player Afflictions**
=======================

.. tip::

  See :ref:`Player Combat Afflictions` for afflictions that can only be applied in combat.

**SetArousalToXUnlessHigherThanX**
-----------------------------------

Sets the player arousal to the first specified numerical value, unless the current arousal is higher than the specified value.
This is mostly for cinematic purposes.

::

  "SetArousalToXUnlessHigherThanX", "100"

**SetArousalToXUnlessHigherThanXThenAddY**
-------------------------------------------

Same as the above, but if the current arousal is higher than the specified value, it will add the second given value instead.
Also mostly for cinematic purposes.

::

 "SetArousalToXUnlessHigherThanXThenAddY", "100", "50",

**SetArousalToMax**
--------------------

``"SetArousalToMax"`` sets the player's arousal to max. The player is not notified.

**ChangeArousal & ChangeArousalQuietly**
-----------------------------------------

Will flatly alter the player's current arousal with the specified number. Can be negative.

::

  "ChangeArousal", "50"

``"ChangeArousalQuietly"`` can be used to change the player's arousal without notifying the player.

**ChangeEnergy & ChangeEnergyQuietly**
---------------------------------------

Same as the above, but for the players current energy. Note negative values subtract.

::

  "ChangeEnergy", "-30"

``"ChangeEnergyQuietly"`` can be used to change the player's current energy without notifying the player.

**ChangeArousalByPercent & ChangeEnergyByPercent**
---------------------------------------------------

Changes players current amount of their arousal or energy respectively by a percent based on their maximum of the chosen stat. Can take negative values.
It does not notify the player.

::

  "ChangeArousalByPercent", "-10"
  "ChangeEnergyByPercent", "10"

**SetSpirit**
--------------

Set the players current spirit to a number. It will be rounded to the maximum or 0 if the given number exceeds or is below respectively.

::

  "SetSpirit", "1"

**ChangeSpirit & ChangeSpiritQuietly**
---------------------------------------

Changes the players current spirit by the given amount. Can take a negative value.
It will be rounded to the maximum or 0 if the given number exceeds or is below respectively.

::

  "ChangeSpirit", "2"

``"ChangeSpiritQuietly"`` can be used to change the players current spirit without notifying them.

::

  "ChangeSpiritQuietly", "-2"

.. _DamagePlayerFromMonster:

**DamagePlayerFromMonster**
----------------------------

Deal randomized damage to the player via a skill and monster, the monster chosen is used as a stat reference.
The skill chosen will not apply status effects. Displaying dialogue has to be done manually, it will not take dialogue from the skill.
If you want to display the damage number from the skill, use {DamageToPlayer} in the following string after completing the function.

::

  "DamagePlayerFromMonster", "Imp", "Blowjob"


.. _DamageMonsterFromMonster:

**DamageMonsterFromMonster**
----------------------------

Deal randomized damage to the focused monster via a skill and called monster, the monster chosen is used as a stat reference and doesn't need to be in the active combat encounter.
The skill chosen will not apply status effects. Displaying dialogue has to be done manually, it will not take dialogue from the skill.
If you want to display the damage number from the skill, use {DamageToMonster} in the following string after completing the function.

::

  "DamageMonsterFromMonster", "Imp", "Arouse"


Check :ref:`HitPlayerWith` for a combat only equivalent.

**ChangePerkDuration**
-----------------------

Changes the duration of the given perk the player possesses by the set amount. ``"6"`` would be a full day. See :ref:`TimeDuration` for reference.

::

    "ChangePerkDuration", "Rut", "9"

**ApplyStatusEffect**
----------------------

Applies a status effect to the player, specifically from skills. If used while in combat, it will utilize the focused monster's stats during application.
It cannot miss.

It's recommended to use skills made specifically for this when out of combat, as it can’t fetch enemy information and use it to impact the status effect.

::

  "ApplyStatusEffect", "Drugged Food"

**RemoveStatusEffect**
-----------------------

Removes the specified status effect, not the skill used to apply it from the above function.

::

   "RemoveStatusEffect", "Stun"

You can choose from any within :ref:`Status Effects`.

**ClearNonPersistentStatusEffects**
------------------------------------

``"ClearNonPersistentStatusEffects"`` clears non-persistent status effects, and perks with the perk type :ref:`NonPersistentEffect`.

For clarity on persistent and non-persistent status effects, see :ref:`Status Effects`.

**ClearPlayerStatusEffects**
-----------------------------

``"ClearPlayerStatusEffects"`` clears the player of all currently applied status effects.

**RefreshPlayer**
------------------

``"RefreshPlayer"`` fully heals the player and removes all currently applied status effects.

**HoldCurrentVirility**
------------------------

Using ``"HoldCurrentVirility"`` grabs the current virility of the player and uses it for all checks until ``"HoldCurrentVirilityEnd"`` is called.
Persists across events and scenes.

::

  "HoldCurrentVirility",
  "... At a later scene or event..."
  "HoldCurrentVirilityEnd",

**PlayerOrgasm**
-----------------

Forces the player to cum, resets arousal to zero, then lowers spirit by set amount. Displays no text/feedback.

::

  "PlayerOrgasm", "1"

**PlayerOrgasmNoSpiritLoss**
-----------------------------

``"PlayerOrgasmNoSpiritLoss"`` causes the player to orgasm, reseting current arousal, but they don't lose spirit.
Used primarily to trigger relevant status effects and events where losing spirit is not desired from a design perspective, such as victory scenes.

**EmptySpiritCounter**
-----------------------------

``"EmptySpiritCounter"`` for specific uses when looping orgasm text and displaying spirit lost in events so it doesnt stack itself in the display.
