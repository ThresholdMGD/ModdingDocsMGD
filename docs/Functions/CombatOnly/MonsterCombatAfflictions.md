# Monster Combat Afflictions

!!! info "See also"

    For functions that work out of combat, see
    [Change Monster](../../Functions/General/ChangeMonster.md).

## ChangeMonsterArousal, ChangeMonsterEnergy, & ChangeMonsterSpirit

Change the related stat to the focused monster. They can take negative
values, and it does reset upon leaving the event and/or encounter. These
do not produce dialogue.

``` json
"ChangeMonsterArousal", "50"
```

## MonsterOrgasm

Brings the focused monster to an orgasm, resetting their arousal and
deducting their spirit by the given amount.

``` json
"MonsterOrgasm", "1"
```

## DenyMonsterOrgasm

*All* monsters in the combat encounter are immune to normal orgasm calls
(e.g. `"MonsterOrgasm"` still works) for the entire round of combat.

Also see DenyCombatOrgasm.

## RefreshMonster

Fully heals the focused monster and removes all currently applied status
effects.

## ApplyStatusEffectToMonster & RemoveStatusEffectFromMonster

`"ApplyStatusEffectToMonster"` applies a status effect via the given
skill to the focused monster. Will not display the skill's
`"StatusOutcome":`.

`"RemoveStatusEffectFromMonster"` removes the given status effect (see
Status Effects) from the focused
monster.

``` json
"ApplyStatusEffectToMonster", "SkillName",
"RemoveStatusEffectFromMonster", "Charm"
```

------------------------------------------------------------------------

## HitMonsterWith

Hit the monster with a skill. Will not apply stances or status effects
from the skill, and does apply recoil damage. It will only damage to the
target, and can crit. It will never miss. Uses the player stats. **Do
not use any skill with a** targetTypeCreation **that isn't** `"single"`.

``` json
"HitMonsterWith", "Caress"
```

If you want to display the damage number from the skill, use
\[DamageToEnemy\] in the following *string* after calling the function.
