# Choice

!!! info "See also"

    For Choice functions outside of the given file, see
    Get Event Choice.

## SetChoice

Will set the specified choice number to the following
*string* value. Think of them as
numerically organized flag markers you can set for an event, not as
variables.

``` json
"SetChoice", "1", "Stole the panty"
```

------------------------------------------------------------------------

## IfChoice

Will check for a choice. If the choice number's possible
*value* is a match to the stored value,
it then goes to the specified scene. If it's not a match, it will
ignore the scene jump, and continue the scene.

``` json
"IfChoice", "1", "Stole the panty", "PlayerGoesToHornyJail"
```

By default, all `"SetChoice"` functions not yet triggered by the player
exist as blank *strings* `""`, which can
be checked for.

------------------------------------------------------------------------

## ChoiceToDisplayPlayer and ChoiceToDisplayMonster

`"ChoiceToDisplayPlayer"` & `ChoiceToDisplayMonster` grabs the specified
choice's *value* for the
[Text Markup](../../Reference/Markup.md)
specified below, and is not reset until it's called again, so it will
affect other events. Thus, it should be called at the start of an event.

Both are exactly the same, each function simply titled with the
intention of either being used for setting a nickname for the player or
monster. Or even giving the Monster a different name in dialogue, say,
giving a generic monster in an event an actual name. They could be used
for other purposes.

``` json
"ChoiceToDisplayPlayer", "1"
```

`[DisplayPlayerChoice]` and `[DisplayMonsterChoice]` in
EventTextMarkup is the markup to utilize
the functions.

------------------------------------------------------------------------

## SetChoiceToPlayerName

Sets the selected choice to the player's name. For the above
function's intended use case.

``` json
"SetChoiceToPlayerName", "1"
```

See SetChoiceToPlayerNameFromOtherEvent
for setting a choice to an external event.
