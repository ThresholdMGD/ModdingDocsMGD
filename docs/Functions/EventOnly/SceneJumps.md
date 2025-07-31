---
tags:
  - jumptorandomscene
  - jumptorandom
  - call
---

# Scene Jumps

!!! info "See also"

    For making jumps to scenes in other events, see
    Event Jumps.

## JumpToScene

Goes to scene stated in the next string. Scenes are contained within an
event, see Event Jumps for jumping to
specific scenes outside of the event.

``` json
"JumpToScene", "SceneNameHere"
```

## JumpToRandomScene

Goes to one of the listed scenes at random. Close with `"EndLoop"`. You
can repeat a scene in the listing to make it more likely.

``` json
"JumpToRandomScene",
  "SceneName1",
  "SceneName2",
  "SceneName3",
  "SceneName4",
"EndLoop"
```

Can also use [Requirement Sub-Functions](Menu.md#requirement-sub-functions)
and [Displayed Requirement Sub-Functions](Menu.md#displayed-requirement-sub-functions)
(though they aren't displayed in this case), to weight or filter
choices based on conditions.

``` json
"JumpToRandomScene",
  "RequiresChoice", "1", "SceneName1",
  "SceneName2",
  "SceneName3",
"EndLoop"
```

## IfEventExists

Checks if the named event Exists, then does a scene jump if it does.
This is entirely for modders wanting to check if another active mod
exists in the game files.

``` json
"IfEventExists", "EventNameHere", "SceneInActiveEventNotTheEventYou'reChecking"
```

## CallSceneThenReturn

Allows you to jump into a scene then return to where it was called
initially. These can be called inside each other as well. Exiting one of
these calls is the same as ending an event, ensuring it eventually leads
to a scene with no jumps.

``` json
"CallSceneThenReturn", "SceneNameHere"
```

See [CallEventAndSceneThenReturn](../General/EventJumps.md#calleventandscenethenreturn) for
jumping to specific scenes outside of the event.

A note from Threshold:

> Be sure to end a call so it can return or weird shit will happen,
> zlike rewinding time. Check TimePassed.json or EndOfDay.json for
> examples of its use.

------------------------------------------------------------------------

## CallNextSceneJumpThenReturn
Turns the next scene jump into a call and return, just like
`"CallSceneThenReturn"`. Useful when in tandem with check based scene
jump functions, such as from Player Checks or [Monster Checks](../CombatOnly/MonsterChecks.md). The scene
jump function must be given directly after
`"CallNextSceneJumpThenReturn"` or it will expire.

``` json
"CallNextSceneJumpThenReturn",
"IfFetishLevelEqualOrGreater", "Legs", "25", "SceneName"
```
**This is NOT to be used with event jumps.**

## Bonus - FishingMiniGame

Starts a basic fishing mini game, fail and pass each jump to a different
event and there's a few setting you can alter. AppearTimerRange - the
random time range before the fish appears. 100 = 1 second.
FailTimerRange - The time before the player fails the minigame.
ReelsNeeded - How many times the player needs to hit the fish before the
mini game ends.

``` json
"FishingMiniGame",
  "AppearTimerRange", "50", "150",
  "FailTimerRange", "80", "80",
  "ReelsNeeded", "4",
  "FishingPassJump", "JumpToPassScene",
  "FishingFailJump", "JumpToFailScene",
"EndLoop"
```
