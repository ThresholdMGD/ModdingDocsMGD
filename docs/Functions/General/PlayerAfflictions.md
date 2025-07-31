# Player Afflictions
::: seealso
For afflictions that can only be applied in combat, see
[Player Combat Afflictions](../../Functions/CombatOnly/PlayerCombatAfflictions.md).
:::

## SetArousalToXUnlessHigherThanX
Sets the player arousal to the first specified numerical value, unless
the current arousal is higher than the specified value. This is mostly
for cinematic purposes.

``` json
"SetArousalToXUnlessHigherThanX", "100"
```

------------------------------------------------------------------------

## SetArousalToXUnlessHigherThanXThenAddY
Same as the above, but if the current arousal is higher than the
specified value, it will add the second given *value* instead. Also mostly for cinematic purposes.

``` json
"SetArousalToXUnlessHigherThanXThenAddY", "100", "50",
```

------------------------------------------------------------------------

## SetArousalToMax
`"SetArousalToMax"` sets the player's arousal to max. The player is not
notified.

------------------------------------------------------------------------

## ChangeArousal & ChangeArousalQuietly
Will flatly alter the player's current arousal with the specified
number. Can be negative.

``` json
"ChangeArousal", "50"
```

`"ChangeArousalQuietly"` can be used to change the player's arousal
without notifying the player.

------------------------------------------------------------------------

## ChangeEnergy & ChangeEnergyQuietly
Same as the above, but for the players current energy. Note negative
*values* subtract.

``` json
"ChangeEnergy", "-30"
```

`"ChangeEnergyQuietly"` can be used to change the player's current
energy without notifying the player.

------------------------------------------------------------------------

## PlayerCurrentEnergyCost
Removes energy from the player based on their currently used skill. This
is for counter attack usage like the ghosts, where the skill technically
still goes through despite skipping the attack itself.

------------------------------------------------------------------------

## ChangeArousalByPercent & ChangeEnergyByPercent
Changes players current amount of their arousal or energy respectively
by a percent based on their maximum of the chosen stat. Can take
negative values. It does not notify the player.

``` json
"ChangeArousalByPercent", "-10"
"ChangeEnergyByPercent", "10"
```

------------------------------------------------------------------------

## SetSpirit
Set the players current spirit to a number. It will be rounded to the
maximum or 0 if the given number exceeds or is below respectively.

``` json
"SetSpirit", "1"
```

------------------------------------------------------------------------

## ChangeSpirit & ChangeSpiritQuietly
Changes the players current spirit by the given amount. Can take a
negative value. It will be rounded to the maximum or 0 if the given
number exceeds or is below respectively.

``` json
"ChangeSpirit", "2"
```

`"ChangeSpiritQuietly"` can be used to change the players current spirit
without notifying them.

``` json
"ChangeSpiritQuietly", "-2"
```

------------------------------------------------------------------------

## DamagePlayerFromMonster
Deal randomized damage to the player via a skill and monster, the
monster chosen is used as a stat reference. The skill chosen will not
apply status effects. Displaying dialogue has to be done manually, it
will not take dialogue from the skill. If you want to display the damage
number from the skill, use \[DamageToPlayer\] in the following
*string* after completing the function.

``` json
"DamagePlayerFromMonster", "Imp", "Blowjob"
```

------------------------------------------------------------------------

## DamageMonsterFromMonster
Deal randomized damage to the focused monster via a skill and called
monster, the monster chosen is used as a stat reference and doesn't
need to be in the active combat encounter. The skill chosen will not
apply status effects. Displaying dialogue has to be done manually, it
will not take dialogue from the skill. If you want to display the damage
number from the skill, use [\[DamageToEnemy\]]{.title-ref} in the
following *string* after completing the
function.

``` json
"DamageMonsterFromMonster", "Imp", "Arouse"
```

Check [HitPlayerWith](../CombatOnly/PlayerCombatAfflictions.md#hitplayerwith) for a combat
only equivalent.

------------------------------------------------------------------------

## ChangePerkDuration
Changes the duration of the given perk the player possesses by the set
amount. `"6"` would be a full day. See
[TimeDurationType](../../Reference/StatusEffectRef.md#duration-types) for reference.

``` json
"ChangePerkDuration", "Rut", "9"
```

------------------------------------------------------------------------

## ApplyStatusEffect
Applies a status effect to the player, specifically from skills. If used
while in combat, it will utilize the focused monster's stats during
application. It cannot miss.

It's recommended to use skills made specifically for this when out of
combat, as it can't fetch enemy information and use it to impact the
status effect.

``` json
"ApplyStatusEffect", "Drugged Food"
```

------------------------------------------------------------------------

## RemoveStatusEffect
Removes the specified status effect, not the skill used to apply it from
the above function.

``` json
"RemoveStatusEffect", "Stun"
```

You can choose from any within Status Effects.

------------------------------------------------------------------------

## ClearNonPersistentStatusEffects
`"ClearNonPersistentStatusEffects"` clears non-persistent status
effects, and perks with the perk type
[NonPersistentEffectType](../../Reference/StatusEffectRef.md#effect-types).

For clarity on persistent and non-persistent status effects, see
[Status Effects](../../Reference/StatusEffectRef.md).

------------------------------------------------------------------------

## ClearPlayerStatusEffects
`"ClearPlayerStatusEffects"` clears the player of all currently applied
status effects.

------------------------------------------------------------------------

## RefreshPlayer
`"RefreshPlayer"` fully heals the player and removes all currently
applied status effects.

------------------------------------------------------------------------

## HoldCurrentVirility
Using `"HoldCurrentVirility"` grabs the current virility of the player
and uses it for all checks until `"HoldCurrentVirilityEnd"` is called.
Persists across events and scenes.

``` json
"HoldCurrentVirility",
"... At a later scene or event..."
"HoldCurrentVirilityEnd",
```

------------------------------------------------------------------------

## PlayerOrgasm
Forces the player to cum, resets arousal to zero, then lowers spirit by
set amount. Displays no text/feedback.

``` json
"PlayerOrgasm", "1"
```

------------------------------------------------------------------------

## PlayerOrgasmNoSpiritLoss
`"PlayerOrgasmNoSpiritLoss"` causes the player to orgasm, reseting
current arousal, but they don't lose spirit. Used primarily to trigger
relevant status effects and events where losing spirit is not desired
from a design perspective, such as victory scenes.

------------------------------------------------------------------------

## EmptySpiritCounter
`"EmptySpiritCounter"` for specific uses when looping orgasm text/events
in a row during an event (EventTextMarkup) and displaying spirit lost in events so it doesnt stack
itself in the display.
