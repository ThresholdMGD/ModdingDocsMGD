# Get Event Progress

!!! info "See also"

    For Progress functions within event files, see
    Progress.

## GetEventAndChangeProgress

Gets an event and changes its progress based on the given value. Can be
negative.

``` json
"GetEventAndChangeProgress", "Mysterious Inn", "2"
```

------------------------------------------------------------------------

## GetEventAndSetProgress

Gets an event and sets its progress to the given value. Can be negative.

``` json
"GetEventAndSetProgress", "Enter 'Amber's Adventuring Shop'", "10"
```

------------------------------------------------------------------------

## GetAnEventsProgressThenIfEquals

Gets an event and then checks if it's equal to the provided value. If
true, it jumps to the given scene.

``` json
"GetAnEventsProgressThenIfEquals", "Imp Defeated", "5", "SceneNameHere"
```

------------------------------------------------------------------------

## GetAnEventsProgressThenIfEqualsOrGreater

Gets an event and then checks if it's equal or greater to the provided
value. If true, it jumps to the given scene.

``` json
"GetAnEventsProgressThenIfEqualsOrGreater", "Camillas Knitting Training", "5", "SceneNameHere"
```

------------------------------------------------------------------------

## GetAnEventsProgressThenIfEqualsOrLess

Gets an event and then checks if it's equal or greater to the provided
value. If true, it jumps to the given scene.

``` json
"GetAnEventsProgressThenIfEqualsOrLess", "Pray To The Goddess Statue.", "5", "SceneNameHere"
```

------------------------------------------------------------------------

## Event Comparing Functions

The following three jump functions are for specificly comparing across
between two events. They all work the same, but do change in how it's
decided.

------------------------------------------------------------------------

### EventsProgressEqualsOtherEventsProgress

Will check the first event specified to see if its progress is equal to
the event in the next string. If true, it will jump to the given scene.

``` json
"EventsProgressEqualsOtherEventsProgress", "'Bon Bon Bun'", "'Perpetuas Lemonade Stand'", "SceneNameHere"
```

------------------------------------------------------------------------

### IfEventsProgressEqualsOrLessThanOtherEventsProgress

Will check the first event specified to see if its progress is equal or
less than the event in the next string. If true, it will jump to the
given scene.

``` json
"IfEventsProgressEqualsOrLessThanOtherEventsProgress", "Mikas Foul Tongue", "Amys Wholesome Tongues", "SceneNameHere"
```

------------------------------------------------------------------------

### **EventsProgressEqualsOrGreaterThanOtherEventsProgress**,

Will check the first event specified to see if its progress is equal or
greater than the event in the next string. If true, it will jump to the
given scene.

``` json
"EventsProgressEqualsOrGreaterThanOtherEventsProgress", "Slime Clueless Levels", "Harpy Clueless Levels", "SceneNameHere"
```
