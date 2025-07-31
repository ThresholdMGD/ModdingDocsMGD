# Attacker

!!! info "See also"

    For functions attacking the player, see
    [Monster Attacks](../../Functions/CombatOnly/MonsterAttack.md), and
    [Player Combat Afflictions](../../Functions/CombatOnly/PlayerCombatAfflictions.md)

    For functions attacking the monster, see
    [Monster Combat Afflictions](../../Functions/CombatOnly/MonsterCombatAfflictions.md).

## IfAttackCrits

`"IfAttackCrits"` will check if the attacker from the last source of
skill damage managed to Crit. If true, it will jump to the given scene.

Note this counts for both monsters and players, and also works with
combat functions applying damaging skills.

Meant to be used with combat events called by
CallCombatEventAndScene within skills.

``` json
"IfAttackCrits", "SceneNameHere"
```
