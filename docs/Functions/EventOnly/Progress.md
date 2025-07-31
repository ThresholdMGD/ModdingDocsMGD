---
tags:
  - ifprogress
  - relatonship
---

# Progress

Progress is typically used to track relationship progress with
characters, but it can be used for more technical purposes.

**By default, progress for all events start at 0.**

!!! info "See also"

    You can display progress via the `[ProgressDisplay]`
    [Text Markup](../../Reference/Markup.md) .
    Also see
    [Get Event Progress](../../Functions/EventOnly/GetEventProgress.md) for progress functions outside of the given file.

## SetProgress

Will set the event's progress to the specified number. Can be negative.

``` json
"SetProgress", "0"
```

------------------------------------------------------------------------

## ChangeProgress

Changes the events progress based on the given value. Can be negative.

``` json
"ChangeProgress", "5"
```

------------------------------------------------------------------------

## ChangeProgressBasedOnVirility

Changes progress based on virility, with the following with the
*value* in the following
*string* being a multiplier. Base number
in the example translates to 0.1x scaling of the players virility total.
So if the player has 100 virility, it will result in progress increasing
by 10.

``` json
"ChangeProgressBasedOnVirility", "1"
```

Primarily designed for the blue balls system, but it can have other
uses.

------------------------------------------------------------------------

## IfProgressEquals
Checks if the progress of the event is equal to the following number. If
true, it jumps to the given scene. If false, it's ignored. Can be
negative.

``` json
"IfProgressEquals", "10", "SceneNameHere"
```

------------------------------------------------------------------------

## IfProgressEqualsOrGreater
Works the same as the previous function, but is still true even if the
event's *value* is greater than the
checked value. Can be negative.

``` json
"IfProgressEqualsOrGreater", "10", "SceneNameHere"
```

------------------------------------------------------------------------

## IfProgressEqualsOrLess
Same as the previous function, but instead is still true if the event's
*value* is less than the checked value.
Can be negative.

``` json
"IfProgressEqualsOrLess", "10", "SceneNameHere"
```
