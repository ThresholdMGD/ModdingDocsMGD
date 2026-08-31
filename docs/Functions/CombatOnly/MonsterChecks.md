---
tags:
  - ifstatuseffect
  - ifstatus
---


# Monster Checks

!!! note

    **All of the functions below only work in [Event](../../Manual/Events/Events.md) based .json files.**

## IfThisMonsterIsInEncounter

Checks for the specified monster in the encounter, will ignore focused
monster if checking for other with the same name.

``` json
"IfThisMonsterIsInEncounter", "MonsterName", "SceneNameHere"
```

------------------------------------------------------------------------

## EncounterSizeGreaterOrEqualTo & EncounterSizeLessOrEqualTo

Checks if the current combat encounter has an equal or greater, or equal
or less than respectively, of the given number of enemies.

``` json
"EncounterSizeGreaterOrEqualTo", "2", "SceneNameHere"
```

------------------------------------------------------------------------

## IfMonsterLevelGreaterThan

Checks if the focused monster level is **equal** to greater than the specified
amount.

!!! warning

    To repeat, this checks equal to or greater than due to a mistake, and cannot be changed without breaking mod compatibility.

``` json
"IfMonsterLevelGreaterThan", "42", "SceneNameHere"
```

## IfMonsterStat

Checks one of the focused monster's stats against a given value. If
true, it jumps to the given scene, else it continues. 

See [Stat Reference](../../Reference/StatRef.md#ifstat-stat-names) for the
accepted stat names. Will actively reflect changes made to every participants stats
within combat encounters.

By default, the comparison made checks if it is equal. 
You can optionally change this from:

- `"Equals"` for exactly the given value.
- `"LesserThan"` for less than the given value.
- `"LesserOrEquals"` for less than or equal to the given value.
- `"GreaterThan"` for greater than the given value.
- `"GreaterOrEquals"`.  for greater or equal to the given value

The given value for comparison is to be a whole number, the `"Player"`, or a monster ID name present in the encounter.

Percents are also accepted for `"Arousal"`, `"Energy"`, `"Spirit"`, and `"Exp"`. Percentages always rounds down.

Note `"Virility"`, `"GoddessFavor"`, and `"Strain"` are **player only** and cannot be used.

``` json
"IfMonsterStat", "Power", "GreaterOrEquals", "5", "SceneNameHere",
"IfMonsterStat", "Spirit", "34", "SceneNameHere",
"IfMonsterStat", "Energy", "LesserOrEquals", "Player", "SceneNameHere",
"IfMonsterStat", "Arousal", "GreaterThan", "50%", "SceneNameHere"
```

------------------------------------------------------------------------

## IfMonsterResistances, IfMonsterSensitivities, & IfMonsterFetish

Equivalent to `"IfMonsterStat"` above for comparing resistance, sensitivity, or
fetish levels respectively instead of a stat. The optional operator value
defaults to `"Equals"`. See
[Resistances](../../Reference/StatusEffectRef.md#resistances),
[Sensitivities](../../Reference/StatRef.md#sensitivity-reference), and
[Fetishes](../../Manual/Fetishes/Fetishes.md) (including Addicitons) for information on accepted comparisons.

``` json
"IfMonsterResistances", "Sleep", "LesserThan", "20", "SceneNameHere",
"IfMonsterSensitivities", "Sex", "GreaterOrEquals", "120", "SceneNameHere",
"IfMonsterFetish", "Oral", "Equals", "50", "SceneNameHere"
```

------------------------------------------------------------------------

## IfMonsterHasStatusEffect & IfMonsterDoesntHaveStatusEffect

If the focused monster does or doesn't respectively have *any* of the
specified status effects, jump to the given scene.

Providing `"RequireAll"` prior to listing any status effects will make
it only match if the monster does or doesn't respectively have *all*
given status effects.

See Status Effect.

``` json
"IfMonsterHasStatusEffect", "RequireAll", "Restrain", "Charm", "SceneNameHere",
"IfMonsterHasStatusEffect", "Restrain", "Charm", "AnotherSceneNameHere"
```

------------------------------------------------------------------------

## IfOtherMonsterHasStatusEffect & IfOtherMonsterDoesntHaveStatusEffect

Same as the above, but requires first specifying another monster in the
encounter. Note that it will shift focus to that monster. Ignores the
currently focused monster.

Keep in mind `"RequireAll"` comes after specifying the monster.

``` json
"IfOtherMonsterHasStatusEffect", "Himika", "RequireAll", "Charm", "Restrain", "SceneNameHere"
"IfOtherMonsterHasStatusEffect", "Himika", "Restrain", "AnotherSceneNameHere"
```

------------------------------------------------------------------------

## IfMonsterHasStatusEffectWithPotencyEqualOrGreater

Checks the focused monster for a single status effect with the given
amount of potency. Will shift focus to that monster. Ignores the
currently focused monster.

Note not all status effects use potency, see
Status Effect.

``` json
"IfMonsterHasStatusEffectWithPotencyEqualOrGreater", "Aphrodisiac", "50", "SceneNameHere"
```

------------------------------------------------------------------------

## IfMonsterArousalGreaterThan

Checks if the monster's arousal is greater than the given number. 

The given value can be a percent of the maximum. Percentages always round down.

``` json
"IfMonsterArousalGreaterThan", "2319", "SceneNameHere"
"IfMonsterArousalGreaterThan", "80%", "SceneNameHere"
```

------------------------------------------------------------------------

## IfMonsterOrgasm

Checks if the current monster's arousal will make them cum.

``` json
"IfMonsterOrgasm", "SceneNameHere"
```

------------------------------------------------------------------------

## IfMonsterEnergyGone

Checks if the current monster's energy is 0.

``` json
"IfMonsterEnergyGone", "SceneNameHere"
```

------------------------------------------------------------------------

## CallMonsterEncounterOrgasmCheck

Checks if any monsters in a fight have orgasmed, and proceeds as if hit
in combat.

``` json
"CallMonsterEncounterOrgasmCheck"
```

------------------------------------------------------------------------

## IfMonsterSpiritGone

Checks if the monster is out of spirit. Made for use with enemies who
have more than one spirit.

``` json
"IfMonsterSpiritGone", "SceneNamehere"
```

------------------------------------------------------------------------

## IfMonsterHasSkill & IfMonsterHasPerk

Checks if the monster has the skill or perk respectively. Useful for
checking for skills or perks given to the monster by a separate event or
scene.

``` json
"IfMonsterHasSkill", "Caress", "SceneNameHere",
```
