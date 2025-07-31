# Menu System

## Menu

Gives the player an option menu of choices. Each choice is a scene in
the same event file. Make sure the scene names exactly match the choice.
Will always end current scene and jump to a new one, thus it's
recommended to only have them at the end of a scene.

``` json
"Menu",
  "I hate tacos.",
  "I love tacos.",
  "Tacos are okay.",
  "I like taco soup!",
"EndLoop"
```

By default, if there are more than 6 choices, page arrows will
automatically be added.

See SceneAdditions for appending to base
game menus in a mod-friendly manner.

## Meta Functions

### MaxMenuSlots

Sets the max number of menu options available per menu page, not
counting [FinalOption](#finaloption). **MaxMenuSlots must be called
first at the start of the `"Menu"` loop. Maximum of 6, minimum
of 1**

This is useful if the menu choices have a high character count, which
can otherwise clip with the player status and dialogue box.

``` json
"Menu", "MaxMenuSlots", "2",
  "A choice",
  "Another choice.",
  "This will be on the second page",
  "This choice is also on the second page",
  "A choice on the third page.",
"EndLoop"
```

------------------------------------------------------------------------

### ShuffleMenu

Randomly shuffles the menu choices, to be declared at the start of the
menu.

Keep in mind [FinalOption](#finaloption) disregards this.

``` json
"Menu", "ShuffleMenu",
  "Touch the butt.",
  "Don’t touch the butt.",
"EndLoop"
```

------------------------------------------------------------------------

### FinalOption

Forces a menu option to always be the last available option in the list.
**If there are multiple pages, it will be at the bottom of every page,
and does not count towards** [MaxMenuSlots](#maxmenuslots).

It's recommended to avoid using [Requirement
Sub-Functions](#requirement-sub-functions) alongside this function's
target, as this is intended for giving the player back-out options. If
you do use the functionality for your `"FinalOption"` choice, please
ensure `"FinalOption"` is the last sub-function that's provided prior
to the choice.

``` json
"Menu",
  "FinalOption", "Done talking.",
  "Ask if they ever wondered why we're here in this box canyon.",
  "Something that was added in with a menu addition.",
"EndLoop"
```

------------------------------------------------------------------------

### EventJump & ThenJumpToScene

Makes the following option jump to the given event instead of a scene.
`"ThenJumpToScene"` has it jump to a specific scene in that event.

These can be used with [FinalOption](#finaloption) if desired.

``` json
"Menu",
  "EventJump", "Lumiren's Song", "Final Option", "See the Lumiren.",
  "EventJump", "Lava Hot Spring", "Go and hear dad jokes.",
  "EventJump", "'Bon Bon Bun'", "ThenJumpToScene", "StoreMenuReal", "Candy!",
"EndLoop"
```

------------------------------------------------------------------------

### HideOptionOnRequirementFail

Can be called before a choice with any requirement check to hide that
options requirements/existence from the player. Note this only applies
to [Displayed Requirement
Sub-Functions](#displayed-requirement-sub-functions)

``` json
"Menu",
  "HideOptionOnRequirementFail", "RequiresEnergy", "50", "Climb the mountain!",
  "Take the elevator.",
"EndLoop"
```

------------------------------------------------------------------------

### InverseRequirement

Can be called before a choice with any requirement check to reverse the
true/false conditions of any requirement checks for a given choice. Can
be used with
[HideOptionOnRequirementFail](#hideoptiononrequirementfail), and
technically [FinalOption](#finaloption).

``` json
"Menu",
  "InverseRequirement", "RequiresPerk", "Swift", "I'm very slow.",
  "RequiresPerk", "Swift", "I'm fast!",
  "HideOptionOnRequirementFail", "InverseRequirement", "RequiresSkill", "Teleport", "I can't teleport.",
"EndLoop"
```

------------------------------------------------------------------------

## Displayed Requirement Sub-Functions

You can use any of the functions here to make require the player to meet
a condition before being presented with the menu choice. **If the player
fails the requirement, the conditions will be displayed.**

Multiple check conditions can be given before providing the choice. Do
note only the first requirement given in a multi-condition choice can
display upon failing. Threshold usually prefers to disable it via
[HideOptionOnRequirementFail](#hideoptiononrequirementfail) where
sensible.

------------------------------------------------------------------------

### RequiresStat

Checks the player's stat in the following *string* with the provided value. Passes if it's equal or greater
than. See Stats.

``` json
"Menu",
  "RequiresStat", "Allure", "5", "Seduce her first.",
  "HideOptionOnRequirementFail", "RequiresStat", "Willpower", "5", "Don't get seduced.",
  "Mutual seducing.",
"EndLoop"
```

------------------------------------------------------------------------

### RequiresItem

Checks the player's inventory for the specified item.

``` json
"Menu",
  "RequiresItem", "Ring", "Propose",
  "What's your favorite color?",
"EndLoop"
```

------------------------------------------------------------------------

### RequiresSkill

Checks the player for a skill.

``` json
"Menu",
  "RequiresSkill", "Charm", "Cast charm on her.",
  "Use a pickup line.",
"EndLoop"
```

------------------------------------------------------------------------

### RequiresPerk

Checks the player for a perk.

``` json
"Menu",
  "RequiresPerk", "Swift", "Run away!",
  "Run away but slower!",
"EndLoop"
```

------------------------------------------------------------------------

### RequiresEnergy

Checks the player for a specified amount of energy.

``` json
"Menu",
  "RequiresEnergy", "900", "Test the project before releasing.",
  "Release the project.",
"EndLoop"
```

------------------------------------------------------------------------

### RequiresVirility

Checks the player to see if they have the specified amount of virility.

``` json
"Menu",
  "RequiresVirility", "100", "I can take on all of you!",
  "I cannot take on all of you!?",
"EndLoop"
```

------------------------------------------------------------------------

## Requirement Sub-Functions

You can use any of the functions here to make require the player to meet
a condition before being presented with the menu choice. Multiple check
conditions can be given before providing the choice.

------------------------------------------------------------------------

### RequiresItemEquipped

Checks if the player has the specified item equipped.

``` json
"Menu",
  "RequiresItemEquipped", "Condom", "I'm ready!",
  "Not ready yet!",
"EndLoop"
```

------------------------------------------------------------------------

### RequiresTime

Checks to see if it's the given
[Time](../../Functions/General/Time.md).

``` json
"Menu",
  "RequiresTime", "Noon", "It's high noon.",
  "Aw heck.",
"EndLoop"
```

------------------------------------------------------------------------

### RequiresFetishLevelEqualOrGreater & RequiresFetishLevelEqualOrLess

Will check the specified fetish for the given *value* to be equal or greater, or equal or less respectively.

``` json
"Menu",
  "RequiresFetishLevelEqualOrLess", "Breasts", "3", "Not big on melons.",
  "RequiresFetishLevelEqualOrGreater", "Breasts", "6", "Man I love melons.",
  "RequiresFetishLevelEqualOrLess", "Ass", "4", "Not a fan of peaches.",
  "RequiresFetishLevelEqualOrGreater", "Ass" "9", "I love peaches!",
  "Actually, I like holding hands.",
"EndLoop"
```

------------------------------------------------------------------------

### RequiresMinimumProgress & RequiresMinimumProgressFromEvent

Checks for a minimum amount of specified progress.

``` json
"Menu",
  "RequiresMinimumProgress", "10", "Ten cards!",
"EndLoop"
```

Using `"RequiresMinimumProgressFromEvent"` checks for a minimum amount
of specified progress from the given event.

``` json
"Menu",
  "RequiresMinimumProgressFromEvent", "EventToCheckHere", "5", "Five cards~",
"EndLoop"
```

------------------------------------------------------------------------

### RequiresLessProgress & RequiresLessProgressFromEvent

Checks to see if progress is less than the specified amount.

``` json
"Menu",
  "RequiresLessProgress", "50", "Too many cards!",
"EndLoop"
```

Using `"RequiresLessProgressFromEvent"` checks to see if progress less
than the specified amount from the given event.

``` json
"Menu",
  "RequiresLessProgressFromEvent", "EventToCheckHere", "20", "Too many cards!",
"EndLoop"
```

------------------------------------------------------------------------

### RequiresChoice & RequiresChoiceFromEvent

Checks for the specified choice.

``` json
"Menu",
  "RequiresChoice", "3", "A choice.", "SceneName",
"EndLoop"
```

Using `"RequiresChoiceFromEvent"` checks for the specified choice from
the given event.

``` json
"Menu",
  "RequiresChoiceFromEvent", "EventName", "3", "A choice.", "SceneName",
"EndLoop"
```
