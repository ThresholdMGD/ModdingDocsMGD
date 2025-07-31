# Player Give & Take
## GiveExp
Despite its name, flatly alters the amount of exp the player has. This
means it can both remove and give exp, depending on if you give a
negative or positive *value*
respectively. After altering the exp, it checks to see if the player can
level up. The *value* ignores exp
modifiers such as from perks.

``` json
"GiveExp", "96",
"GiveExp", "-43"
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
`"GiveSkillThatWasTemporarilyRemoved"` a quiet variant of give skill
specifically for temporarily removing skills then giving them back,
ensuring they go back into the same spot in skill order to not
disorganize player skills. Check the skill `"Pin"` for an example. If
you want to give the player a temp skill for a fight, like, tail cuddle,
you do not need to use this set of functions.

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
