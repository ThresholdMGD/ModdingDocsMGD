# Get Event Choice

!!! info "See also"

    For Choice functions within event files, see
    [Choice](../../Functions/EventOnly/Choice.md).

## GetEventAndIfChoice

Check an events choices and check if the choice matches, if so, jump to
scene.

``` json
"GetEventAndIfChoice", "EventNameHere", "3", "The choice", "SceneToJumpToHere"
```

## GetEventAndSetChoice

Gets an event, and sets the specified choice to the given string.

``` json
"GetEventAndSetChoice", "EventNameHere", "1", "The new set choice."
```

## ChoiceToDisplayPlayerFromOtherEvent & ChoiceToDisplayMonsterFromOtherEvent

`"ChoiceToDisplayPlayerFromOtherEvent"` &
`"ChoiceToDisplayMonsterFromOtherEvent"` grabs the specified choice from
an external event's *value* for the
[Text Markup](../../Reference/Markup.md)
specified below, and is not reset until it's called again, so it will
affect other events. Thus, it should be called at the start of a scene
or event.

Both behave the same, each function titled with the intention as either
being used for setting a nickname for the player or monster. Or even
giving the Monster a different name in dialogue, say, giving a generic
monster in an event an actual name. They could be used for other
purposes.

``` json
"ChoiceToDisplayPlayerFromOtherEvent", "EventName", "1"
```

`[DisplayPlayerChoice]` and `[DisplayMonsterChoice]` in
EventTextMarkup is the markup to utilize
the functions.

See ChoiceToDisplayFunc for doing it
within the same event.

------------------------------------------------------------------------

## SetChoiceToPlayerNameFromOtherEvent

Sets the selected choice to the player's name in another event. For the
above functions.

``` json
"SetChoiceToPlayerNameFromOtherEvent", "EventName", "1"
```

See SetChoiceToPlayerNameFunc for doing
it within the same event.
