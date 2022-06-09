**Perk Types**
===============

.. tip::

   Use the navigation column on the left to navigate and review the page headers quickly.

**Perk Modifiers**
-------------------
These types modify the behavior of the perk itself, rather than the wielder of the perk.

**StatusIcon**
"""""""""""""""
.. code-block:: javascript

  "PerkType": ["StatusIcon"],
  "EffectPower": ["../Mods/ModName/Folder/Icon.png"],

Declares a status icon for the perk whenever the player or monster possesses it.
The provided file path to your image will be displayed as an icon in the status bar.

**TurnDuration**
"""""""""""""""""
.. code-block:: javascript

  "PerkType": ["TurnDuration"],
  "EffectPower": ["5"],

Removes the perk from the wielder once the set duration has depleted to 0. Ticks down for every step or combat turn.

.. _TimeDurationType:

**TimeDuration**
"""""""""""""""""
.. code-block:: javascript

  "PerkType": ["TimeDuration"],
  "EffectPower": ["18"],

Removes the perk from the wielder once the set duration has depleted to 0. Ticks down for every time jump (e.g. Morning -> Noon),
note sleeping till morning will take a variable number of ticks depending on the current time. ``"6"`` would be a full day.

**RemovedOnOrgasm**
""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["RemovedOnOrgasm"],
  "EffectPower": ["0"],

Perk is removed when the wielder orgasms. Set a value of 0, as ``"EffectPower":`` is not needed.

**EndMessage**
"""""""""""""""

.. code-block:: javascript

  "PerkType": ["EndMessage"],
  "EffectPower": ["PerkName's effects have faded away!"],

Displays the given text via its correlating ``"EffectPower":`` string when the perk ends via `TurnDuration`_ or `TimeDuration`_.
This can use :doc:`Text Markup </Doc/Reference/Markup>`, and thus in extension, :doc:`Functions </Doc/Reference/Functions>`.

.. _NonPersistentEffectType:

**NonPersistentEffect**
""""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["NonPersistentEffect"],
  "EffectPower": ["0"],

Declare the perk as a NonPersistentEffect, removing it whenever a Non-Persistent Status Effect (e.g. Charm) would be removed by the game.
Set a value of 0, as ``"EffectPower":`` is not needed.

**RemovablePersistantEffect**
""""""""""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["RemovablePersistantEffect"],
  "EffectPower": ["0"],

Declare the perk as a RemovablePersistantEffect, removing it whenever a RemovablePersistantEffect Status Effect (e.g. Aphrodisiac) would be removed by the game. Aka sleep or church wake up.
Set a value of 0, as ``"EffectPower":`` is not needed.

**RemovableEffect**
""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["RemovableEffect "],
  "EffectPower": ["0"],

Declare the perk as a RemovableEffect , that allows the effect to be cleared on use of a panacea(currently just this), or on combat end like NonPersistentEffect.
Set a value of 0, as ``"EffectPower":`` is not needed.


**Reward**
-----------

.. note::

    These are primarily written from the perspective of it being a perk type for the player, however,
    it will be disclaimed if the type is available for monsters as well.

**EroBoost**
"""""""""""""

.. code-block:: javascript

  "PerkType": ["ErosBoost"],
  "EffectPower": ["10"],

Alters eros found by a percent.
If wielded by a monster, alters their own eros dropped. Positive values increase eros, negative values decrease.

**ItemDropChance**
"""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["ItemDropChance"],
  "EffectPower": ["-10"],

Alters item drop chance from monsters by a percent.
If wielded by a monster, alters their own item drop chance. Positive values increase the chance, negative values decrease.

**TreasureFindChance**
"""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["TreasureFindChance"],
  "EffectPower": ["15"],

Alters percent chance of finding treasure during exploration, and by extension, higher chance of rare treasure.
Positive values increase the chance, negative values decrease.

**BetterPrices**
"""""""""""""""""

.. code-block:: javascript

  "PerkType": ["BetterPrices"],
  "EffectPower": ["-5"],

Alter all shop prices by a percent, for both selling and buying.
Positive values lower purchase cost and increases sale price, negative values increase cost and lowers sale price.

**BuyPrices**
""""""""""""""

.. code-block:: javascript

  "PerkType": ["BuyPrices"],
  "EffectPower": ["50"],


Alter all shop prices by a percent, for both selling and buying. Positive values lower cost, negative values increase cost.

**SellPrices**
"""""""""""""""

.. code-block:: javascript

  "PerkType": ["SellPrices"],
  "EffectPower": ["-50"],

Alter all shop prices by a percent, for both selling and buying. Positive values increase sale price, negative values lower sell price.

**ExpBoost**
"""""""""""""

.. code-block:: javascript

  "PerkType": ["ExpBoost"],
  "EffectPower": ["120"],

Alter all exp gains by a percent. Effect is halved when applied to LossExp effects, see below.
If wielded by a monster, alters their own exp drop amount. Positive values increase exp, negative values decrease.

**LossExp**
""""""""""""

.. code-block:: javascript

  "PerkType": ["LossExp"],
  "EffectPower": ["-20"],

Alter exp gains from monster exp on loss by a percent. Positive values increase exp, negative values decrease.

**Damage**
-----------

.. note::

    Features the same behavior when used for either the player or monsters.

**DamageBoost**
""""""""""""""""

.. code-block:: javascript

  "PerkType": ["DamageBoost"],
  "EffectPower": ["50"],

Alters all types of damage dealt by a percent. Positive values increase damage, negative values decrease.

**MagicBoost**
"""""""""""""""

.. code-block:: javascript

  "PerkType": ["MagicBoost"],
  "EffectPower": ["-30"],

Alters magic damage dealt by a percent. Positive values increase damage, negative values decrease.

**NonPenMagicBoost**
"""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["NonPenMagicBoost"],
  "EffectPower": ["19"],

Alters non-penetrative (e.g. fire dildo, pole beam, ethereal hands) magic damage dealt by a percent. Positive values increase damage, negative values decrease.

**BreastBoost**
""""""""""""""""

.. code-block:: javascript

  "PerkType": ["BreastBoost"],
  "EffectPower": ["40"],

Alters breast/nipple damage by a percent. Positive values increase damage, negative values decrease.

**NonPenSeductionBoost**
"""""""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["NonPenSeductionBoost"],
  "EffectPower": ["-30"],

Alters non-penetrative seduction damage dealt by a percent. Positive values increase damage, negative values decrease.

**SeductionBoost**
"""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["SeductionBoost"],
  "EffectPower": ["-30"],

Alters seduction damage dealt by a percent. Positive values increase damage, negative values decrease.

**KissBoost**
""""""""""""""

.. code-block:: javascript

  "PerkType": ["KissBoost"],
  "EffectPower": ["69"],

Alters kiss damage dealt by a percent. Positive values increase damage, negative values decrease.

**SexBoost**
"""""""""""""

.. code-block:: javascript

  "PerkType": ["SexBoost"],
  "EffectPower": ["5"],

Alters sex damage dealt by a percent. Positive values increase damage, negative values decrease.

**NonPenSexBoost**
"""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["NonPenSexBoost"],
  "EffectPower": ["20"],

Alters non-penetrative sex (e.g. dildo, fingering, stroking, etc.) damage dealt by a percent. Positive values increase damage, negative values decrease.

**AssBoost**
"""""""""""""

.. code-block:: javascript

  "PerkType": ["AssBoost"],
  "EffectPower": ["-10"],

Alters ass damage dealt by a percent. Positive values increase damage, negative values decrease.

**NonPenAssBoost**
"""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["NonPenAssBoost"],
  "EffectPower": ["20"],

Alters non-penetrative ass (e.g. dildo, fingering, etc.) damage dealt by a percent. Positive values increase damage, negative values decrease.

**PainBoost**
""""""""""""""

.. code-block:: javascript

  "PerkType": ["PainBoost"],
  "EffectPower": ["50"],

Alters pain damage dealt by a percent. Positive values increase damage, negative values decrease.

**PenetrationBoost**
"""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["PenetrationBoost"],
  "EffectPower": ["15"],

Alters penetration damage dealt by a percent. Positive values increase damage, negative values decrease.

**OralBoost**
""""""""""""""

.. code-block:: javascript

  "PerkType": ["OralBoost"],
  "EffectPower": ["-35"],

Alters oral damage dealt by a percent. Positive values increase damage, negative values decrease.

**ForeplayBoost**
""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["ForeplayBoost"],
  "EffectPower": ["8"],

Alters foreplay damage dealt by a percent. Positive values increase damage, negative values decrease.

**IndulgentBoost**
"""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["IndulgentBoost"],
  "EffectPower": ["-1"],

Alters indulgent damage dealt by a percent. Positive values increase damage, negative values decrease.

**SexToyBoost**
""""""""""""""""

.. code-block:: javascript

  "PerkType": ["SexToyBoost"],
  "EffectPower": ["34"],

Alters sex toy damage dealt by a percent. Positive values increase damage, negative values decrease.

**BaselineAllureFlatBuff**
"""""""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["BaselineAllureFlatBuff"],
  "EffectPower": ["15"],

Alters Allure’s natural flat damage buff scaling to everything by a flat amount. Positive values increase damage, negative values decrease.

**BaselineAllureFlatPercentBoost**
"""""""""""""""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["BaselineAllureFlatPercentBoost"],
  "EffectPower": ["2"],

Alters Allure’s natural flat damage buff scaling to everything by a percent. Positive values increase damage, negative values decrease.

**ForeplayFlatDamage**
"""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["ForeplayFlatDamage"],
  "EffectPower": ["5"],

Alters foreplay damage dealt by a flat amount. Positive values increase damage, negative values decrease.

**CritChanceBoost**
""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["CritChanceBoost"],
  "EffectPower": ["20"],

Alters chance for the wielder's skills to crit by a flat amount. Positive values increase chance, negative values decrease.

**CritDamageBoost**
""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["CritDamageBoost"],
  "EffectPower": ["-100"],

Alters critical damage dealt by a percent amount on top of the original calculation. Positive values increase damage, negative values decrease.

**RecoilBoost**
""""""""""""""""

.. code-block:: javascript

  "PerkType": ["RecoilBoost"],
  "EffectPower": ["10"],

Alters overall recoil damage dealt to opponents. Positive values increase damage, negative values decrease.

**AllureRecoilBoost**
""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["AllureRecoilBoost"],
  "EffectPower": ["33"],

Alters the percent of allure based recoil damage dealt to opponents. Positive values increase damage, negative values decrease.

**Defense**
------------

.. note::

    Features the same behavior when used for either the player or monsters, unless stated otherwise.

**DamageReduction**
""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["DamageReduction"],
  "EffectPower": ["-10"],

Alters all damage taken by a percent, take caution. Positive values increase mitigation, negative values decrease.

**ForeplayEnergyRegen**
""""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["ForeplayEnergyRegen"],
  "EffectPower": ["40"],

Alters energy regeneration through foreplay skills by a percent of the wielders max. Positive values recover energy, negative values remove energy.

**ForeplayArousalRegen**
"""""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["ForeplayArousalRegen"],
  "EffectPower": ["20"],

Alters arousal regeneration through foreplay skills by a percent of the wielders max. Positive values recover arousal, negative values remove arousal.

**RegenMaxArousal**
""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["RegenMaxArousal"],
  "EffectPower": ["5"],

Restores a percent of the max arousal of the wielder. Take caution. Positive values recover arousal, negative values remove arousal.

**RegenMaxEnergy**
"""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["RegenMaxEnergy"],
  "EffectPower": ["2"],

Restores a percent of the max arousal of the wielder. Take caution. Positive values recover energy, negative values remove energy.

**VirilityBoost**
""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["VirilityBoost"],
  "EffectPower": ["40"],

Alters the players Virility by a percent. Positive values increase virility, negative values reduce. **Player only**.

**RecoilDamageTaken**

.. code-block:: javascript

  "PerkType": ["RecoilDamageTaken"],
  "EffectPower": ["-66"],

Alters recoil damage taken by a percent. Positive values increase recoil damage taken, negative values reduce.

**CritDamageBoostSelf**
""""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["CritDamageBoostSelf"],
  "EffectPower": ["-20"],

Alters critical damage the wielder receives prior to the final calculation. Positive values increase damage received, negative values reduce.

**Edging**
"""""""""""

.. code-block:: javascript

  "PerkType": ["Edging"],
  "EffectPower": ["50"],

Experimental perk type that gives percent chance to resist orgasm, stacks with other sources. Positive values increase the base percent chance, negative values reduce.

**MultiplySpirit Loss**
"""""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["MultiplySpirit Loss"],
  "EffectPower": ["2"],

Multiply the spirit lost by the given number. Caution going above 2, for a base amount of 3 spirit, it is practically an instant loss.

`RemovedOnOrgasm`_ plays well with the perk type.

.. It still uses spaces, assuming it will be addressed later?

**Status Effects**
-------------------

.. note::

    Features the same behavior when used for either the player or monsters, unless stated otherwise.

**StatusEffectDuration**
"""""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["StatusEffectDuration"],
  "EffectPower": ["1"],

Alters the duration of the users status effects, take caution. Positive values increase duration, negative values reduce.

**StatusChanceBoost**
"""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["StatusChanceBoost"],
  "EffectPower": ["-10"],

Alter status effect application chances from skills. Positive values increase chance, negative values reduce.

**StartDeeperInTrance**
"""""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["StartDeeperInTrance"],
  "EffectPower": ["5"],

Player starts this many steps deeper in trance when hit with a trance related move. Anything below 1-10 will trigger instant trance.

**CantBreakFreeOfTranceWithoutItems**
""""""""""""""""""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["CantBreakFreeOfTranceWithoutItems"],
  "EffectPower": ["0"],

Can no longer automatically start to break free of trance after 3 consecutive turns without getting stunned.
Set a value of 0, as ``"EffectPower":`` is not needed.

**TranceStunChance**
"""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["TranceStunChance"],
  "EffectPower": ["10"],

Alters the chance for the player to be stunned each turn while fully tranced by a percent. Positive values increase chance, negative values reduce.

**ForeplayDefDown**
""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["ForeplayDefDown"],
  "EffectPower": ["-40"],


Applies a status effect that reduces the defense to the enemy targeted with a foreplay skill for 3 turns.
Positive values reduce defense, negative values increase.

**StunDelay**
""""""""""""""

.. code-block:: javascript

  "PerkType": ["StunDelay"],
  "EffectPower": ["1"],

Alters the delay between stun status effects. Positive values increase the delay, negative values reduce.

**SleepAmp**
"""""""""""""

.. code-block:: javascript

  "PerkType": ["SleepAmp"],
  "EffectPower": ["-50"],


Alters the flat amount of energy lost per turn upon being afflicted by Sleep. Positive values increase drain energy, negative values reduce drained energy.

**ParalysisAmp**
"""""""""""""""""

.. code-block:: javascript

  "PerkType": ["ParalysisAmp"],
  "EffectPower": ["-10"],

Alters the chance to be stunned by paralysis. Positive values increase chance, negative values reduce.

**AphrodisiacAmp**
""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["AphrodisiacAmp"],
  "EffectPower": ["10"],

Alters the damage taken from aphrodisiacs by a percent. Positive values increase damage, negative values reduce.

**AphrodisiacTurnCure**
""""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["AphrodisiacTurnCure"],
  "EffectPower": ["5"],

Removes set amount from aphrodisiac potency every turn.  Positive values reduce set potency, negative values increase set potency.

**DisableRun**
"""""""""""""""

.. code-block:: javascript

  "PerkType": ["DisableRun"],
  "EffectPower": ["0"],

Can disable the players ability to run from all fights. Set a value of 0, as ``"EffectPower":`` is not needed.

**Stances & Evasion**
----------------------

.. note::

    Features the same behavior when used for either the player or monsters, unless stated otherwise.

**GetOutOfStance**
"""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["GetOutOfStance"],
  "EffectPower": ["20"],

Alters chance to get out of stance by a percent. Positive values increase chance, negative values reduce.

**OutOfStanceEvade**
"""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["OutOfStanceEvade"],
  "EffectPower": ["-25"],

Alters evade chance when out of stances by a percent. Positive values increase chance, negative values reduce.

**RemoveRestraints**
"""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["RemoveRestraints"],
  "EffectPower": ["15"],

Alters restraint escape chance by a percent. Positive values increase chance, negative values reduce.

**RestraintBoost**
"""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["RestraintBoost"],
  "EffectPower": ["30"],

Increases the effectiveness of your own restraints. Positive values improve effectiveness, negative values reduce.

**StanceBoost**
""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["StanceBoost"],
  "EffectPower": ["-20"],

Increases the effectiveness of your own stances. Positive values improve effectiveness, negative values reduce.

**RunChance**
""""""""""""""

.. code-block:: javascript

  "PerkType": ["RunChance"],
  "EffectPower": ["25"],

Alters run chance by a percent. Positive values increase chance, negative values reduce.

**OpponentRunChance**
""""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["OpponentRunChance"],
  "EffectPower": ["25"],

Monsters with this perk type alters the players run chance by a percent. Positive values increase chance, negative values reduce.

**Unbounded**
""""""""""""""

.. code-block:: javascript

  "PerkType": ["Unbounded"],
  "EffectPower": ["0"],

If your action is interrupted by a restraint, you will struggle instead of doing nothing by default.
Set a value of 0, as ``"EffectPower":`` is not needed.

**Unshackled**
"""""""""""""""

.. code-block:: javascript

  "PerkType": ["Unshackled"],
  "EffectPower": ["0"],

If you break a restraint with struggle, you get to act immediately.
Set a value of 0, as ``"EffectPower":`` is not needed.

**OrgasmEnergyDrain**
""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["OrgasmEnergyDrain"],
  "EffectPower": ["25"],

Drains flat amount of energy upon the target orgasming. Has no stance restrictions.
Positive values drain energy.

**StanceStuck**
""""""""""""""""

.. code-block:: javascript

  "PerkType": ["StanceStuck"],
  "EffectPower": ["-20"],

Alters chance of stance escape by a percent. Positive values reduce chance, negative values increase.

**InitiativeBonus**
""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["InitiativeBonus"],
  "EffectPower": ["25"],

Flatly alters perk type owners initiative, influencing turn order. Positive values increase initiative, negative values reduce.

**MinStatCheckDie**
""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["MinStatCheckDie"],
  "EffectPower": ["2"],

Flatly alters the minimum dice your d20 can roll in a stat check, take caution. Positive values increases base number, negative values reduce.

**RestSpiritRestored**
"""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["RestSpiritRestored"],
  "EffectPower": ["1"],

Recovers flat amount of spirit when resting at rest points, take caution. Positive values increase, negative values reduce.

**RestEnergyRestored**
"""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["RestEnergyRestored"],
  "EffectPower": ["20"],

Recovers percent amount of max energy when resting at rest points, take caution. Positive values increase, negative values reduce.

**RestArousalRestored**
""""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["RestArousalRestored"],
  "EffectPower": ["-20"],

Recovers percent amount of max arousal when resting at rest points, take caution. Positive values increase, negative values reduce.

.. _StatPerkTypes:

**Stat Perk Types**
--------------------

Alters the given stat of the wielder by the given amount. Positive values increase, negative values reduce. See :ref:`Stats`.

* ``"GainEnergy"``
* ``"GainArousal"``
* ``"Power"``
* ``"Technique"``
* ``"Intelligence"``
* ``"Willpower"``
* ``"Allure"``
* ``"Luck"``
* ``"StunRes"``
* ``"CharmRes"``
* ``"AphrodisiacRes"``
* ``"RestraintsRes"``
* ``"TranceRes"``
* ``"ParalysisRes"``
* ``"SleepRes"``
* ``"DebuffRes"``
* ``"SexSensitivity"``
* ``"AssSensitivity"``
* ``"BreastsSensitivity"``
* ``"MouthSensitivity"``
* ``"SeductionSensitivity"``
* ``"MagicSensitivity"``
* ``"PainSensitivity"``
* ``"HolySensitivity"``
* ``"UnholySensitivity"``

.. code-block:: javascript

  "PerkType": ["GainArousal"],
  "EffectPower": ["50"],


.. _FetishPerkTypes:

**Fetish Perk Types**
----------------------

Alters fetish level by # of times added.

* ``"IncreaseFetish"``
* ``"DecreaseFetish"``

.. code-block:: javascript

    "PerkType": ["IncreaseFetish", "DecreaseFetish"],
    "EffectPower": ["Ass",              "Sex"],

**Player Specific**
--------------------

**GiveSensitivityPoints**
"""""""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["GiveSensitivityPoints"],
  "EffectPower": ["2"],

Give player points to reduce sensitivity. Only works if acquired at level up. Take caution.

**GainSpirit**
"""""""""""""""

.. code-block:: javascript

  "PerkType": ["GainSpirit"],
  "EffectPower": ["1"],

Give the player spirit. Only works if acquired at level up. Take caution.

**ResistFinalOrgasm**
""""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["ResistFinalOrgasm"],
  "EffectPower": ["4"],

Gives a luck chance plus a base amount to resist their last orgasm. Monsters have more interactive methods to implement this kind of feature in combat events.
Refer to *Json/Perks/LevelUp/Will/HeroicCumback.json* for how it works.

**Monster Specific**
---------------------

.. note::

  The following three perk types are multiplied in effect by the player's Virility * 0.01 + 1.

**SemenEnergyDrain**
"""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["SemenEnergyDrain"],
  "EffectPower": ["20"],

Player loses given amount of energy on orgasm with monster if in sex, anal, blowjob, tailfuck, or titfuck stance.
Positive values increase base flat drain, negative values reduce.

.. _SemenHealPerkType:

**SemenHeal**
""""""""""""""

.. code-block:: javascript

  "PerkType": ["SemenHeal"],
  "EffectPower": ["-10"],

Monster recovers given amount of arousal on player orgasm if in sex, anal, blowjob, tailfuck, or titfuck stance.
Positive values increase base flat drain, negative values reduce.

**SemenAttackBoost**
"""""""""""""""""""""

.. code-block:: javascript

  "PerkType": ["SemenAttackBoost"],
  "EffectPower": ["25"],

Percent damage alteration if player orgasms in sex, anal, blowjob, tailfuck, or titfuck stance.
Positive values increase, negative values reduce.

.. _AdversePerkTypes:

**Adverse Perk Types**
"""""""""""""""""""""""

The following perk types tell the monster to try to get out of the related stance even if they have a skill for it, unless they're charmed.
Set a value of 0, as ``"EffectPower":`` is not needed.

* ``"KissingAdverse"``
* ``"AnalAdverse"``
* ``"SexAdverse"``

.. code-block:: javascript

  "PerkType": ["KissingAdverse", "AnalAdverse"],
  "EffectPower": ["0"                 "0"],

.. _NoPartPerkTypes:

**No Part Perk Types**
"""""""""""""""""""""""

The following perk types make it impossible for the player to initiate or attack the given stances, excluding grope attacks on chests.
It is highly recommend you use combat events instead of them, but they do still work.
Set a value of 0, as ``"EffectPower":`` is not needed.

* ``"NoAnus"``
* ``"NoChest"``
* ``"NoMouth"``
* ``"NoPussy"``

.. code-block:: javascript

  "PerkType": ["NoAnus", "NoMouth"],
  "EffectPower": ["0",      "0"],

.. _MonsterDamageBoostPerkTypes:

**Monster Damage Boost Perk Types**
"""""""""""""""""""""""""""""""""""""

Damage boosts by a percent for the related fetish. Positive values increase, negative values reduce.

* ``"MonstrousBoost"``
* ``"FeetUseBoost"``
* ``"BreastUseBoost"``
* ``"AssUseBoost"``

.. code-block:: javascript

  "PerkType": ["MonstrousBoost"],
  "EffectPower": ["66"],
