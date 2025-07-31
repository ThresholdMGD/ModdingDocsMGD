# End Combat or Monster

!!! info "See also"

    For starting combat, see Pre-Combat. For
    sending the player back to town after a loss scene, see
    Town Jumps.

## PlayerLosesCombat

Player instantly loses combat and goes to loss scene based on focused
monster. Has no display text, it happens instantly. Note you can use the
GameOver function to make your own loss
scenes as well without having to go back to the combat loss scenes. Up
to you.

------------------------------------------------------------------------

## EndCombat

Immediately ends combat and goes to combat reward screen.

------------------------------------------------------------------------

## ClearFightForVictory

Clears out monster encounter, immediately ending combat and gives
rewards.

------------------------------------------------------------------------

## ClearMonsterEncounter

Clears out monster encounter. Use if you want to completely leave combat
when you jump to an event.

In a loss scene, `"ClearMonsterEncounter"` followed by a jump to event
function can be used to ignore a game over. Just remember to use
CallLossLevelUpFunc before clearing the
monster encounter for loss exp gains.

------------------------------------------------------------------------

## ClearMonsterEncounterBossFight

Same as above but doesn't return the players ability to run.

------------------------------------------------------------------------

## RemoveMonster

Removes focused monster from encounter, rewards no exp money or loot.

------------------------------------------------------------------------

## DefeatMonster

Defeats the focused monster, still ensuring their exp and loot for the
player when combat ends.
