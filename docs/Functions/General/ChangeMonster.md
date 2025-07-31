# Change Monster
::: seealso
For functions that only work while in combat, see
[Monster Combat Afflictions](../CombatOnly/MonsterCombatAfflictions.md). Note that
these also only work in combat.
:::

## ChangeMonster Functions
Changes the given stat of the focused monster by the given amount. They
can take negative values, and it does reset upon leaving the event
and/or encounter. These do not produce dialogue.

-   `"ChangeMonsterLevel"`
-   `"ChangeMonsterErosDrop"`
-   `"ChangeMonsterExpDrop"`
-   `"ChangeMonsterMaxSpirit"`
-   `"ChangeMonsterMaxArousal"`
-   `"ChangeMonsterMaxEnergy"`
-   `"ChangeMonsterPower"`
-   `"ChangeMonsterWill"`
-   `"ChangeMonsterTech"`
-   `"ChangeMonsterAllure"`
-   `"ChangeMonsterLuck"`
-   `"ChangeMonsterInt"`

``` json
"ChangeMonsterMaxSpirit", "2"
```

------------------------------------------------------------------------

## LevelUpMonster
Levels up the focused monster semi randomly based on their existing stat
leanings. This can take a number, 'MatchPlayer', 'GoUpByProgress' or
'GoUpByProgressFromOtherEvent'.

``` json
"LevelUpMonster", "5"
```

------------------------------------------------------------------------

## RecalculateMonsterExpDrop
Recalculates the focused monsters exp drop based on the games
progression curve of the following formula.

``` python
(0.4*(lvl*lvl))+(2*lvl)+(15*sqrt(lvl)-8)
```

You can use its sub-function `"AlterByPercent"` to alter the result. The
below example is 70% of the recalculation used for boss fights.

``` json
"RecalculateMonsterExpDrop"
"RecalculateMonsterExpDrop", "AlterByPercent", "70",
```

------------------------------------------------------------------------

## RecalculateMonsterErosDrop
Recalculates the focused monsters eros drop based on the games
progression curve of the following formula.

``` python
(lvl)^2+(lvl*10)+48)
```

You can use its sub-function `"AlterByPercent"` to alter the result. The
below example is 70% of the recalculation used for boss fights.

``` json
"RecalculateMonsterErosDrop"
"RecalculateMonsterErosDrop", "AlterByPercent", "70",
```

------------------------------------------------------------------------

## ChangeMonsterSensitivity
Changes the given sensitivity by specified amount for the focused
monster. They can take negative values, and it does reset upon leaving
the event and/or encounter. These do not produce dialogue.

``` json
"ChangeMonsterSensitivity", "Pain", "20"
```

------------------------------------------------------------------------

## ChangeMonsterStatusEffectResistances
Changes the given status effect resistance by specified amount for the
focused monster. They can take negative values, and it does reset upon
leaving the event and/or encounter. These do not produce dialogue. See
[Resistances](../../Reference/StatusEffectRef.md#resistances)

``` json
"ChangeMonsterStatusEffectResistances", "Sleep", "20"
```

------------------------------------------------------------------------

## ChangeMonsterFetish
Changes the given fetish by the specified level amount for the focused
monster. They can take negative values, and it does reset upon leaving
the event and/or encounter. These do not produce dialogue.

``` json
"ChangeMonsterFetish", "Cock", "4"
```

------------------------------------------------------------------------

## GivePerkToMonster & RemovePerkFromMonster
Gives or removes the perk respectively from the focused monster. Can
give duplicates. It does reset upon leaving the event and/or encounter.
These do not produce dialogue.

``` json
"GivePerkToMonster", "PerkName"
```

------------------------------------------------------------------------

## GiveSkillToMonster & RemoveSkillFromMonster
Gives or removes the skill respectively from the focused monster. Can
give duplicates to increase chances. It does reset upon leaving the
event and/or encounter. These do not produce dialogue.

``` json
"GiveSkillToMonster", "SkillName"
```

------------------------------------------------------------------------

## ClearMonsterPerks & ClearMonsterSkillList
Clears the focused monster's perk or skill list respectively, in case
you want to rebuild their entire skill list or perks in the middle of
combat. It does reset upon leaving an encounter. These do not produce
dialogue.
