# Pre-Combat

!!! info "See also"

    For ending a combat encounter, see End Combat. For functions to use while in combat, see
    [Encounter](../../Functions/CombatOnly/Encounter.md).

## CombatEncounter

Starts a combat encounter with the specified monster(s), returns to the
current scene after the combat IF the player wins. Supports up to 12
enemies.

``` json
"CombatEncounter",
  "Monster1",
  "Monster2",
"StartCombat"
```

The following are sub-functions to `"CombatEncounter"`, and must be
called before any monster is given. Order doesn't matter.

------------------------------------------------------------------------

### NoRunning

Prevents the player running from the combat encounter.

``` json
"CombatEncounter", "NoRunning",
  "Monster1",
  "Monster2",
  "Monster3",
"StartCombat"
```

------------------------------------------------------------------------

### SetBGOnRun

Sets a specified background to be displayed if the player runs from the
combat encounter, as running otherwise exits the event. See
*Events/SpidersLair.json* as a use case example.

``` json
"CombatEncounter", "SetBGOnRun", "ImagePathHere.png",
  "Monster1",
  "Monster2",
"StartCombat"
```

------------------------------------------------------------------------

### RunningWontSkipEvent

Ensures that if the player runs from the combat encounter, it won't end
the event prematurely.

``` json
"CombatEncounter", "RunningWontSkipEvent",
  "Monster1",
"StartCombat"
```

------------------------------------------------------------------------

### ApplyStance

Forces the player and specified monster to start in a stated stance.
Take caution to not apply incompatible stances simultaneously.

``` json
"CombatEncounter",
  "Monster1", "ApplyStance", "Blowjob", "ApplyStance", "Titfuck",
  "Monster2", "ApplyStance", "Making Out",
"StartCombat"
```

------------------------------------------------------------------------

### Restrainer

Forces the player to start in a restraint with a specified monster. Note
that the player isn't meant to be hit with more than one restraint.

``` json
"CombatEncounter",
  "Monster1", "ApplyStance", "Anal", "Restrainer",
"StartCombat"
```

------------------------------------------------------------------------

### DenyInventory

Prevents the player from using their items while in combat.

``` json
"CombatEncounter", "DenyInventory"
  "Monster1",
"StartCombat"
```
