# SwapLineIf
Lets you swap out individual lines for others based on specific
circumstances, or at random. **If no available line is found, it will
always grab the last one.**

If a line is blank, the line will be skipped. In case people want to add
new lines.

Note you can still use
[Text Markup](../../Reference/Markup.md) in
the possible lines if you want to change the expression, or just
generally put functions within them.

Given the function is for smaller scale changes, larger scale scene
changes would be better off with an entirely different scene based on a
scene jump.

In order to utilize the function, you must use an option alongside it.
The below header details each one.

## SwapLineIf Options
### Random
Random has no checks and will pick one of the lines at random to
display. You cannot provide it with sub-functions, you would need to use
something other than `"SwapLineIf"` or use
[Text Markup](../../Reference/Markup.md) to
achieve something to that effect.

You can repeat a *string* to increase the
chances that it's the chosen line.

``` json
"SwapLineIf", "Random",
  "Line 1",
  "Line 2",
  "Line 3",
  "Line 4",
  "Line 5",
  "Line 5",
"EndLoop"
```

------------------------------------------------------------------------

### Stat
Using `Stat` checks the player for the specified stat and numerical
condition for said stat in each given line. See
Stats, though note the below functions
for more convenient stat checks.

``` json
"SwapLineIf", "Stat",
  "Technique", "70", "Line 1",
  "Technique", "53", "Line 2",
  "Technique", "19", "Line 3",
"EndLoop"
```

------------------------------------------------------------------------

### Level
Using `"Level"` checks the current player level, each line featuring a
certain numerical amount as its condition.

``` json
"SwapLineIf", "Level",
  "0", "Line 1",
  "7", "Line 2",
  "100", "Line 3",
"EndLoop"
```

------------------------------------------------------------------------

### Arousal & ArousalByPercent & MaxArousal
Using `"Arousal"` checks the current condition of the players arousal,
each line featuring a certain numerical amount as its condition.

``` json
"SwapLineIf", "Arousal",
  "200", "Line 1",
  "86", "Line 2",
  "0", "Line 3",
"EndLoop"
```

Using `"ArousalByPercent"` checks the current condition of the players arousal against their maximum, each line featuring a certain percent amount as its condition.

``` json
"SwapLineIf", "Arousal",
  "100", "Line 1",
  "50", "Line 2",
  "0", "Line 3",
"EndLoop"
```

`"MaxArousal"` checks the player for their maximum arousal, each line
featuring a certain numerical amount as its condition.

``` json
"SwapLineIf", "MaxArousal",
  "360" "Line 1",
  "187" "Line 2",
  "91" "Line 3",
"EndLoop"
```

------------------------------------------------------------------------

### Energy & EnergyByPercent & MaxEnergy
Using `"Energy"` checks the current condition of the players energy,
each line featuring a certain numerical amount as its condition.

``` json
"SwapLineIf", "Energy",
  "150", "Line 1",
  "49", "Line 2",
  "0" "Line 3",
"EndLoop"
```

Using `"EnergyByPercent"` checks the current condition of the players energy against their maximum, each line featuring a certain percent amount as its condition.

``` json
  "SwapLineIf", "Arousal",
    "100", "Line 1",
    "50", "Line 2",
    "0", "Line 3",
  "EndLoop"
```

`"MaxEnergy"` checks the player for their maximum amount of energy they
have, each line featuring a certain numerical amount as its condition.

``` json
"SwapLineIf", "MaxArousal",
  "240" "Line 1",
  "100" "Line 2",
  "5" "Line 3",
"EndLoop"
```

------------------------------------------------------------------------

### Virility
Checks the player for their current virility, each line featuring a
certain numerical amount of virility as its condition.

``` json
"SwapLineIf", "Virility",
  "40", "Line 1",
  "33", "Line 2",
  "0", "Line 3",
"EndLoop"
```

------------------------------------------------------------------------

### HasFetish
Checks to see if the player qualifies for a given fetish (which requires
a minimum of 25 levels in the fetish).

It's binary, in that it checks for the given fetish for the fetish
line, and then a blank *string* for the
line if the player doesn't qualify for the fetish.

``` json
"SwapLineIf", "HasFetish",
  "Breasts", "Line with Breast Fetish",
  "", "Line without Breast Fetish",
"EndLoop"
```

------------------------------------------------------------------------

### HasFetishLevelEqualOrGreater
Checks the players fetish level against the given fetish, each line
featuring a certain numerical amount of the fetish as its condition.

``` json
"SwapLineIf", "HasFetishLevelEqualOrGreater", "Breasts",
  "100", "Line 1",
  "75", "Line 2",
  "50", "Line 3",
  "25", "Line 4",
  "0", "Line 0",
"EndLoop"
```

------------------------------------------------------------------------

### Perk
Checks to see if the player possesses a given perk, each line featuring
a given perk as its condition.

``` json
"SwapLineIf", "Perk",
  "Kotone's Hypno Slave", "Line 1",
  "Kotone's Hypno Lover", "Line 2",
  "", "Line 3",
"EndLoop"
```

------------------------------------------------------------------------

### EncounterSize
Checks the current size of a combat encounter, each line featuring a
certain numerical amount of enemies as its condition.

``` json
"SwapLineIf", "EncounterSize",
  "3", "Line 1",
  "2", "Line 2",
  "1", "Line 3",
"EndLoop"
```

------------------------------------------------------------------------

### Item
Checks the player to see if they have an item.

It's binary, in that you check for the given item for the item line,
and then a blank *string* for the line if
the player doesn't have the item.

``` json
"SwapLineIf", "Item",
  "AnaphHerb", "Line with Anaph Herb",
  "", "Line without Anaph Herb",
"EndLoop"
```

------------------------------------------------------------------------

### Eros
Checks the players current maximum amount of eros, each line featuring a
certain numerical amount of eros as its condition.

``` json
"SwapLineIf", "Eros",
  "1000", "Line 1",
  "0", "Line 2",
"EndLoop"
```

------------------------------------------------------------------------

### IfTimeIs
Checks to see what time it currently is. The order of the potential
lines in this case doesn't matter, as only one can potentially be true.

``` json
"SwapLineIf", "IfTimeIs",
  "Day", "Line during Day",
  "Night", "Line during Night",
"EndLoop"
```

------------------------------------------------------------------------

### Progress & OtherEventsProgress
Using `"Progress"` checks the current progress of the event, each line
featuring a certain numerical amount of progress as its condition.

``` json
"SwapLineIf", "Progress",
  "50", "Line 1",
  "0", "Line 2",
"EndLoop"
```

`"OtherEventsProgress"` lets you check the progress of the given event,
each line featuring a certain numerical amount of progress as its
condition.

``` json
"SwapLineIf", "OtherEventsProgress", "EventName",
  "60", "Line 1",
  "20", "Line 2",
  "0", "Line 3",
"EndLoop"
```

------------------------------------------------------------------------

### Choice & OtherEventsChoice
Using `"Choice"` checks the chosen choice number's
*string* value, each line representing a
potential choice and *value* as its
condition.

The order of priority in this case depends entirely on the context of
the reason you're using the given choice number. However, do remember
to account for if the choice number's *value* is blank, if relevant to your use case.

``` json
"SwapLineIf", "Choice",
  "1", "ThisChoice", "Line 1",
  "1", "OrThisChoice", "Line 2",
  "2", "AlsoThisChoice", "Line 3",
  "1", "", "Line 3",
"EndLoop"
```

Using `"OtherEventsChoice"` checks the specified event's chosen choice
number's *string* value, each line
representing a potential choice and *value* as its condition.

``` json
"SwapLineIf", "OtherEventsChoice", "EventName",
  "1", "ThisChoice", "Line 1",
  "1", "OrThisChoice", "Line 2",
  "2", "AlsoThisChoice", "Line 3",
  "1", "", "Line 3",
"EndLoop"
```
