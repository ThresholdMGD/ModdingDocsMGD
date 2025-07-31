# Store Events

!!! info "See also"

    Not to be confused with in-game shops. See
    [Shop](../../Functions/General/Shop.md) for
    those.


## StoreCurrentEventSpotSkippingLines

Stores the current event, scene, and *string* you're on. The following *string* is provided with a numerical *value* to skip the number of lines after it when called by
`GoBackToStoredEvent` then add on any number of lines to jump forward
when called by `"GoBackToStoredEvent"`. Will stay stored until called
again or it's used.

``` json
"StoreCurrentEventSpotSkippingLines", "3",
"SkippedLine1",
"SkippedLine2",
"SkippedLine3",
"You stand in a room."
```

Useful for skipping functions.

------------------------------------------------------------------------

## GoBackToStoredEvent

`"GoBackToStoredEvent"` jumps back to the stored event, as called above,
then proceeding to skip the number of lines specified. **Upon being
called, it will clear the stored event.**
