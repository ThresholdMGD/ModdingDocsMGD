---
tags:
  - ifstatuseffect
  - ifstatus
---


# Player Combat Checks

!!! note

    **All of the functions below only work in [Event](../../Manual/Events/Events.md) based .json files.**

!!! info "See also"

    For checks that can be used outside of combat, see
    Player Checks.

## IfPlayerStunnedByParalysis

!!! warning

    This function can never be triggered, as paralysis no longer has a stun.
    It remains documented for awareness as the game still detects the
    function.

If player is currently stunned by paralysis, jump to the given scene.

``` json
"IfPlayerStunnedByParalysis", "SceneNameHere"
```

------------------------------------------------------------------------

## IfPlayerIsUsingThisSkill

If the player is using the skill this turn, jump to the given scene. For
more advanced cases where lineTriggers
isn't flexible enough. Check Sofia for it's usage.

``` json
"IfPlayerIsUsingThisSkill", "Demon Layer", "Scene"
```
