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

Checks if the focused monster level is greater than the specified
amount.

``` json
"IfMonsterLevelGreaterThan", "39", "SceneNameHere"
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

``` json
"IfMonsterArousalGreaterThan", "120", "SceneNameHere"
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
