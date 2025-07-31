---
tags:
  - callevent
  - call
---

# Event Jumps
::: seealso
For making jumps to scenes within an event, see
[Scene Jumps](../EventOnly/SceneJumps.md).
:::

## JumpToEvent
Goes to an event stated in the next string. Remember that it will pick
the first scene listed by default.

``` json
"JumpToEvent", "EventNameHere"
```

------------------------------------------------------------------------

### JumpToNPCEvent
Goes to the event stated in the next string, used for events from the
town.

``` json
"JumpToNPCEvent", "EventNameHere"
```

------------------------------------------------------------------------

### JumpToLossEvent
Goes to the event stated in the next string, used for event loss scenes.

``` json
"JumpToLossEvent", "EventNameHere"
```

------------------------------------------------------------------------

## JumpToEventThenScene
Goes to an event, then a scene via the two following strings. Useful
when you want to avoid it going to the first scene in an event. **Note
that it will leave combat encounters.**

``` json
"JumpToEventThenScene", "EventNameHere", "SceneNameHere"
```

------------------------------------------------------------------------

### CallCombatEventAndScene
Variant of `"JumpToEventThenScene"`, but stays in in combat. Used for
events with combat functions.

``` json
"CallCombatEventAndScene", "EventNameHere", "SceneNameHere"
```

------------------------------------------------------------------------

### JumpToNPCEventThenScene
Variant of `"JumpToEventThenScene"` for town.

``` json
"JumpToNPCEventThenScene", "EventNameHere", "SceneNameHere"
```

------------------------------------------------------------------------

## CallEventAndSceneThenReturn
Functions the same as CallSceneThenReturn, but allows you to call to another event, then scene.

``` json
"CallEventAndSceneThenReturn", "EventNameHere", "SceneNameHere"
```
