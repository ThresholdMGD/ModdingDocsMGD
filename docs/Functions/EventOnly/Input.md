---
tags:
  - progress
---

# Input

!!! note

    This was primarily built and internally labeled for the debt functions.
    Their uses towards general modding is limited at the moment, to more or
    less more debt or payment systems.

## InputProgress

`"InputProgress"` calls to take an inputted number from the player and
stores it. The player must specifically provide numbers for input.

## HasErosLessThanInput

Checks if the player has less eros than the inputted number. If true, it
jumps to the given scene. Used to avoiding putting the players eros
below zero, and keeping it free from potential abuse.

``` json
"HasErosLessThanInput", "SceneNameHere"
```

## IfInputEquals

Checks to see if the inputted number is a match to the specified value.
If true, it jumps to the given scene. Previously for checking for zero,
however `"IfInputEqualsOrLessThan"` below is favored for catching
negative inputs.

``` json
"IfInputEquals", "350", "SceneNameHere"
```

------------------------------------------------------------------------

## IfInputEqualsOrLessThan

Checks to see if the inputted number is equal to or less than the
specified value. Used for catching undesirable inputs such as 0, or
negative numbers that have the potential to abuse the input system. If
you wish to use negative numbers, it's best to interpret the input from
the player as such using the below functions, rather than to require
them to input a negative number, which can be unintuitive.

``` json
"IfInputEqualsOrLessThan", "0", "SceneNameHere"
```

------------------------------------------------------------------------

## RemoveInputFromPlayerEros

`"RemovesInputFromPlayerEros"` removes the inputted number from the
players eros.

------------------------------------------------------------------------

## AddInputToProgress & RemoveInputFromProgress

`"AddInputToProgress"` and `"RemoveInputFromProgress"` adds or removes
the input from the event's progress respectively.

------------------------------------------------------------------------

## RemoveProgressFromEros

`"RemoveProgressFromEros"` uses the events progress to subtract from the
players eros.
