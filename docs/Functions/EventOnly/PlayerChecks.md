---
tags:
  - ifstatuseffect
  - ifstatus
  - ifhas
---

# Player Checks

!!! info "See also"

    For checks exclusive to combat, see
    Player Combat Checks.

## StatEqualsOrMore

Checks the following stat against the given number, if the stat is equal
or higher, it jumps to the scene, else it continues. See
Stats.

``` json
"StatEqualsOrMore", "Power", "5", "SceneNameHere"
```

## IfStat

Checks one of the player's stats against a given value. If true, it
jumps to the given scene, else it continues.

See [Stat Reference](../../Reference/StatRef.md#ifstat-stat-names) for the
accepted stat names. Will actively reflect changes made to every
participant's stats within combat encounters.

By default, the comparison made checks if it is equal.
You can optionally change this from:

- `"Equals"` for exactly the given value.
- `"LesserThan"` for less than the given value.
- `"LesserOrEquals"` for less than or equal to the given value.
- `"GreaterThan"` for greater than the given value.
- `"GreaterOrEquals"` for greater or equal to the given value.

The given value for comparison is to be a whole number, the
`"FocusedMonster"`, or a monster ID name present in the encounter.

Percents are also accepted for `"Arousal"`, `"Energy"`, `"Spirit"`,
`"Exp"`, and `"GoddessFavor"`. Percentages always rounds down.

``` json
"IfStat", "Power", "GreaterOrEquals", "5", "SceneNameHere",
"IfStat", "Spirit", "34", "SceneNameHere",
"IfStat", "Energy", "LesserOrEquals", "FocusedMonster", "SceneNameHere",
"IfStat", "Arousal", "GreaterThan", "50%", "SceneNameHere"
```

------------------------------------------------------------------------

## IfResistances, IfSensitivities, & IfFetish

Equivalent to `"IfStat"` above for comparing resistance, sensitivity, or
fetish levels respectively instead of a stat. The optional operator value
defaults to `"Equals"`. See
[Resistances](../../Reference/StatusEffectRef.md#resistances),
[Sensitivities](../../Reference/StatRef.md#sensitivity-reference), and
[Fetishes](../../Manual/Fetishes/Fetishes.md) (including addictions) for
information on accepted comparisons.

``` json
"IfResistances", "Sleep", "LesserThan", "20", "SceneNameHere",
"IfSensitivities", "Sex", "GreaterOrEquals", "120", "SceneNameHere",
"IfFetish", "Oral", "Equals", "50", "SceneNameHere"
```

------------------------------------------------------------------------

## HasErosLessThan

If player has less eros than the given amount, it jumps to the scene,
else it continues.

``` json
"HasErosLessThan", "8008135", "SceneNameHere"
```

------------------------------------------------------------------------

## VirilityEqualsOrGreater

If the player virility is greater than the given number, it jumps to the
scene, else it continues.

``` json
"VirilityEqualsOrGreater", "100", "SceneNameHere"
```

------------------------------------------------------------------------

## IfPlayerOrgasm

Checks if the players current arousal is over their maximum arousal. If
true, it then goes to the given scene, else it continues.

``` json
"IfPlayerOrgasm", "SceneNameHere"
```

------------------------------------------------------------------------

## IfPlayerArousalOverPercentOfMax

Checks if the players current arousal is over a certain percent of their
maximum arousal. If true, it jump to the given scene, else it continues.

Note you can go over 100%, though it might be superseded by an orgasm
call when used while in combat if it isn't per-preemptive. The
percentage is compared exactly, it is not rounded.

``` json
"IfPlayerArousalOverPercentOfMax", "50", "SceneNameHere"
```

------------------------------------------------------------------------

## IfPlayerSpiritGone

Check if the player is out of spirit, if true, it jumps to the given
scene, else it continues.

``` json
"IfPlayerSpiritGone", "SceneNameHere"
```

------------------------------------------------------------------------

## IfPlayerEnergyGone

Same as above, but for the player's energy.

``` json
"IfPlayerEnergyGone", "SceneNameHere"
```

------------------------------------------------------------------------

## IfPlayerEnergyLessThanPercent

Checks if the player energy is less than the given percentage of their
maximum, if true, it jumps to the given scene, else it continues. The
percentage is compared exactly, it is not rounded.

``` json
"IfPlayerEnergyLessThanPercent", "50", "SceneNameHere"
```

------------------------------------------------------------------------

## IfSensitivityEqualOrGreater

Checks if the given sensitivity for the player is equal to or greater
than the given value. If true, it jumps to the given scene, else it
continues.

``` json
"IfSensitivityEqualOrGreater", "Sex", "120", "SceneNameHere"
```

------------------------------------------------------------------------

## IfHasFetish

Checks if the player has the following fetish, if true (level 25 or higher), it jumps to the given scene, else it
continues.

``` json
"IfHasFetish", "Oral", "SceneNameHere"
```

## IfHasFetishes

Checks the player for all given fetishes up till the EndLoop,
if all are true (level 25 or higher), it jumps to the given scene,
else it continues.

``` json
"IfHasFetishes", "Oral", "Ass", "EndLoop", "SceneNameHere"
```

------------------------------------------------------------------------

## IfFetishLevelEqualOrGreater

Checks if the player has an equal or greater level of the given fetish,
if true, it jumps to the given scene, else it continues.

``` json
"IfFetishLevelEqualOrGreater", "Ass", "63", "SceneNameHere"
```

------------------------------------------------------------------------

## IfHasSkill

Checks if the player has the following skill. If true, it jumps to the
given scene, else it continues.

``` json
"IfHasSkill", "Arousara", "SceneNameHere"
```

------------------------------------------------------------------------

## IfHasSkills

Takes a list of skills the play can have, and if all is true it jumps to
the given scene, else it continues.

``` json
"IfHasSkills", "Dildo", "Bondage Net", "EndLoop", "SceneNameHere",
```

------------------------------------------------------------------------

## IfHasItem & IfDoesntHaveItem

Checks if the player does or doesn't respectively have an item in their
inventory or equipped. 
**Supports checking for Item Tags instead of specific items.**

``` json
"IfHasItem", "Vandal's Note", "SceneNameHere"
```

``` json
"IfDoesntHaveItem", "Tags", "Collar", "Venefica's Confectioneries", "EndLoop", "SceneNameHere"
```

------------------------------------------------------------------------

## IfHasItems & IfDoesntHaveItems

Takes a list of items that the player has equipped or in their
inventory, and if all are found or not found respectively, it jumps to
the given scene, else it continues.

``` json
"IfHasItems", "Anaph Herb", "Ardor Potion", "EndLoop", "SceneNameHere",
```

``` json
"IfDoesntHaveItems", "Anaph Herb", "Ardor Potion", "EndLoop", "SceneNameHere",
```

------------------------------------------------------------------------

## IfHasItemEquipped & IfDoesntHaveItemEquipped

Checks if the player does or does not respectively have the specified
item equipped. If true, it jumps to the given scene, else it continues.
**Supports checking for Item Tags instead of specific items.**

``` json
"IfHasItemEquipped", "Hero's Cape", "SceneNameHere"
```

``` json
"IfDoesntHaveItemEquipped", "Tags", "Sofia's Rewards", "Camilla's Secret", "EndLoop", "SceneNameHere"
```

------------------------------------------------------------------------

## IfHasRunesEquipped

Checks if the player does or does not respectively have equal to or more
of the specified amount of the given rune equipped. If true, it jumps to
the given scene, else it continues. 
**Supports checking for Item Tags instead of specific items.**

``` json
"IfHasRunesEquipped", "Heart Rune", "2", "SceneNameHere",
"IfHasRunesEquipped", "Tags", "Graffiti Queen", "EndLoop", "1", "SceneNameHere"
```

------------------------------------------------------------------------

## IfHasItemInInventory & IfDoesntHaveItemInInventory

Checks if the player does or does not respectively have equal to or more
of the specified amount of the given item in their inventory, ignoring
their equipment slots. If true, it jumps to the given scene, else it
continues. 
**Supports checking for Item Tags instead of specific items.**

``` json
"IfHasItemInInventory", "Leek", "39", "SceneNameHere"
```

``` json
"IfDoesntHaveItemInInventory", "Tags", "Healing", "Combat", "EndLoop", "1", "SceneNameHere"
```

------------------------------------------------------------------------

## IfHasPerk

Checks if the player has the following perk. If true, it jumps to the
given scene, else it continues.

``` json
"IfHasPerk", "Sadist", "SceneNameHere"
```

## IfHasPerks

Checks the player for all given perks up till the EndLoop,
if all are true, it jumps to the given scene,
else it continues.

``` json
"IfHasPerks", "Sadist", "Pacing", "EndLoop", "SceneNameHere"
```

------------------------------------------------------------------------

## IfPlayerLevelGreaterThan

Checks if the player level is equal or greater than the specified
amount. If true, it jumps to the given scene, else it continues.

``` json
"IfPlayerLevelGreaterThan", "50", "SceneNameHere"
```

------------------------------------------------------------------------

## IfInExploration

If the player is in Exploration via the Grimoire, rather than an
Adventure. If true, it jumps to the given scene, else it continues.

``` json
"IfInExploration", "SceneNameHere"
```

------------------------------------------------------------------------

## IfRanAway

If the player has just run away from combat, if true, jump to the given
scene, else it continues.

``` json
"IfRanAway", "SceneNameHere"
```

------------------------------------------------------------------------

## IfPlayerHasStatusEffect & IfPlayerDoesntHaveStatusEffect

If the player does or doesn't respectively have *any* of the specified
status effects, jumps to the given scene.

Providing `"RequireAll"` prior to listing any status effects will make
it only match if the player does or doesn't respectively have *all*
given status effects.

Please keep in mind Time will eliminate
non-persistent status effects. See Status Effect.

``` json
"IfPlayerHasStatusEffect", "RequireAll", "Restraint", "Charm", "SceneNameHere",
"IfPlayerHasStatusEffect", "Restraint", "Charm", "AnotherSceneNameHere"
```

------------------------------------------------------------------------

## IfPlayerHasStatusEffectWithPotencyEqualOrGreater

Checks the player for a single status effect with the given amount of
potency. Note not all status effects use potency, see
Status Effect.

``` json
"IfPlayerHasStatusEffectWithPotencyEqualOrGreater", "Trance", "11", "SceneNameHere"
```

------------------------------------------------------------------------

## IfDifficultyIs

Checks the current difficulty of the playthrough, of the three possible
`"Easy"`, `"Normal"`, and `"Hard"` difficulties you can give. If true,
jumps to the given scene.

``` json
"IfDifficultyIs", "Hard", "SceneNameHere"
```
