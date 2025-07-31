# Player Combat Afflictions

!!! info "See also"

    For afflictions that can be applied out of combat, see
    [Player Afflictions](../../Functions/General/PlayerAfflictions.md).

## DenyPlayerOrgasm

The player is immune to normal orgasm calls (e.g. `"PlayerOrgasm"` still
works) for the entire round of combat.

Also see DenyCombatOrgasm.

------------------------------------------------------------------------

## HitPlayerWith

Hit the player with a skill. Will not apply stances or status effects
from the skill, and does apply recoil damage. It will only damage the
target and can crit. It will never miss the target. Uses the stats of
the focused monster. **Do not use any skill with a**
targetTypeCreation **that isn't** `"single"`.

``` json
"HitPlayerWith", "Caress"
```

Displaying dialogue has to be done manually, it will not take dialogue
from the skill. If you want to display the damage number from the skill,
use [DamageToPlayer] in the following *string* after completing the function.

Check DamagePlayerFromMonsterFunc for an
out of combat equivalent. Check
DamageMonsterFromMonsterFunc for an in
of combat way to hit monsters with another monster.

------------------------------------------------------------------------

## SkipPlayerAttack

Skips the players attack. Specifically intended for use with
Counters. This also prevents the player
from consuming the skill costType<costType>, and using consumables.
