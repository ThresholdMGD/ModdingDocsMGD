# Monster Focus

Focus is given automatically whenever a monster is currently actively on
their turn in a round of combat, or when one of their
lineTriggers are active, including any
combat events they jump to from their skills or lineTriggers. The below
functions can manually alter the currently focused monster.

## FocusOnMonster

Focuses on the specified monster by their number in the encounter. If
the number is bigger than the encounter size, it will focus on the last
monster in the encounter. Starts at 1.

``` json
"FocusOnMonster", "3"
```

------------------------------------------------------------------------

## FocusOnRandomMonster

Focuses on a random monster in the encounter.

------------------------------------------------------------------------

## ShuffleMonsterEncounter

Shuffles the monster encounter and renumbers them. You must refocus the
monster for other functions if you want to do anything else after
calling it.

------------------------------------------------------------------------

## RefocusOnInitialMonster

Refocuses on the first monster you entered the function with. Will not
work if you used `"ShuffleMonsterEncounter"`.

------------------------------------------------------------------------

## FocusedSpeaks

The focused enemy SpeaksFunc.

------------------------------------------------------------------------

## FocusedSpeaksSkill

Same as above, but simply no quotations. Typically used for combat event
skill name displays.
