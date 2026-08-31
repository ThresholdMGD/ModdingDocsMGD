# Player Give & Take
## GiveExp
Despite its name, flatly alters the amount of exp the player has. 
This means it can both remove and give exp, depending on if you give a
negative or positive value respectively. 
After altering the exp, it checks to see if the player can
level up. The value ignores exp modifiers such as from perks.

The given value can also be a percent of the exp needed to reach the
next level, for example, for 50/100 needed to level up, `"50%"` would give 25 exp.
Percentages always round down.

``` json
"GiveExp", "96",
"GiveExp", "-43"
```

------------------------------------------------------------------------

## LevelUpPlayer

Levels up the player by the given number of levels immediately.
Grants the exp needed for each level, also triggering level up rewards.
Note level ups work within combat encounters.

It does not take negative values, for that, see
[DrainLevel](#drainlevel).

The given value can be a percent of the current level. Percentages always round down.

``` json
"LevelUpPlayer", "2",
"LevelUpPlayer", "10%"
```

## DrainLevel

Drains the player by the given number of levels immediately, stopping at level 1.
Note this also resets the player's current exp as part of the process, 
and works within combat encounters.

The given value can be a percent of the current level. Percentages always round down.

``` json
"DrainLevel", "3",
"DrainLevel", "50%"
```

------------------------------------------------------------------------

## GiveItem & GiveItemQuietly
Despite its name, `"GiveItem"` changes the specified amount of the
following item that the player owns. This means it can both remove and
give items, depending on if you give a negative or positive
*value* respectively. You are free to
remove as much of the given item as you please, it will not cause any
technical issues.

``` json
"GiveItem", "1", "Calming Potion"
```

`"GiveItemQuietly"` does the same, but does not notify the player.

``` json
"GiveItemQuietly", "-1", "Calming Potion"
```

------------------------------------------------------------------------

## GiveTreasure
`"GiveTreasure"` takes either `"Common"`, `"Uncommon"`, or `"Rare"`, and
rewards the player drops from the respective treasure table rewards for
the respective location or adventure the event takes place within.

**Requires the player** to be in an active location exploration or on an
adventure to function properly.

``` json
"GiveTreasure", "Common"
```

------------------------------------------------------------------------

## GiveSkill & RemoveSkillFromPlayer
Using `"GiveSkill"` gives player a skill if they don't have it already.

``` json
"GiveSkill", "Arousara"
```

`"RemoveSkillFromPlayer"` does the opposite, taking away a skill if they
have it. `"RemoveSkillFromPlayerQuietly"` can be used to do it without
notifying the player.

``` json
"RemoveSkillFromPlayer", "Arousara"
```

An example use case would be to remove skills at the end of combat you
gave to the player at the start of combat. Say, a gimmick skill specific
to the fight.

------------------------------------------------------------------------

## GiveSkillQuietly & RemoveSkillFromPlayerQuietly
`"GiveSkillQuietly"` & `"RemoveSkillFromPlayerQuietly"` are, as
expected, quiet variants of the above functions that won't notify the
player.

------------------------------------------------------------------------

## RemoveSkillFromPlayerTemporarily & GiveSkillThatWasTemporarilyRemoved
`"RemoveSkillFromPlayerTemporarily"` &
`"GiveSkillThatWasTemporarilyRemoved"` are quiet variants of give skill
specifically for temporarily removing a skill with thet intent of later giving it back,
ensuring they go back into the same spot in skill order to not
disorganize player skills. Check the skill `"Pin"` for an example.

`"GiveSkillThatWasTemporarilyRemoved"` can optionally take a value of the skill to give back, or `"All"`
for all skills temporarily removed.

The game will automatically give back all skills upon end of combat or return to town.

For temporary skills that only last the duration of the encounter, see
[Player Combat Skills](../../Functions/CombatOnly/PlayerCombatSkills.md).

``` json
"RemoveSkillFromPlayerTemporarily", "Calm Mind",
"Some time later...",
"GiveSkillThatWasTemporarilyRemoved"
```

------------------------------------------------------------------------

## GivePerk & RemovePerk
Using `"GivePerk"` gives the player a perk, even if they already have
it. `"RemovePerk"` doing the opposite.

``` json
"GivePerk", "Pacing",
"RemovePerk", "Pacing"
```

------------------------------------------------------------------------

## GivePerkQuietly & RemovePerkQuietly
`"GivePerkQuietly"` & `"RemovePerkQuietly"` are, as expected, quiet
variants of the above functions that won't notify the player.

``` json
"GivePerkQuietly", "Pacing",
"RemovePerkQuietly", "Pacing"
```
