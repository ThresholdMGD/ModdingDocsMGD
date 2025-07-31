# Encounter

!!! info "See also"

    See Pre-Combat for information on
    starting an encounter, and End Combat on
    methods of ending an encounter.

## HideMonsterEncounter & ShowMonsterEncounter

`"HideMonsterEncounter"` temporarily hides the encounter. It's still
very much so in effect, just the visibility and selectibility of all
currently displayed monsters monsters from the encounter are gone. It's
meant for combat events, but nothing stops you from using it elsewhere,
just do take caution. Using DisplayCharactersFunc for its duration of use intended.

It will continue to persist until `"ShowMonsterEncounter"` is called,
showing the monsters in the encounter again. Be sure to remove all
monsters from DisplayCharactersFunc
first before calling it to avoid visual oddities.

``` json
"HideMonsterEncounter",
"DisplayCharacters", "1", "2", "4", "EndLoop"
"... sometime later in another scene, or possibly another event...",
"ShowMonsterEncounter",
```

------------------------------------------------------------------------

## AddMonsterToEncounter

`"AddMonsterToEncounter"` Add the monster to the encounter. Will
renumber all the monsters in the encounter. Can add infinitely, so make
sure there's a check to stop it from going above three. Is always added
to the end of the encounter list.

``` json
"AddMonsterToEncounter", "Blue Slime"
```

### ChangeForm

`"ChangeForm"` is used with `"AddMonsterToEncounter"`, switching out the
currently focused monster with the given Monster. Maintains arousal,
spirit, stances, and status effects. See Focus for information on focus functions.

``` json
"AddMonsterToEncounter", "ChangeForm", "Imp"
```

------------------------------------------------------------------------

## AllowRunning

`"AllowRunning"` Allows the player to run from the current combat
encounter if it started off disabled.

``` json
"AllowRunning",
```
