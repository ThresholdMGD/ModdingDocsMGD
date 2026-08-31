# Eros
## ChangeEros
`"ChangeEros"` alters the player's current amount of eros by a flat
amount given in the following string. Can be negative. The given value
can be a percent of the current eros. Percentages always round down.

``` json
"ChangeEros", "100"
"ChangeEros", "-15%"
```

------------------------------------------------------------------------

## ChangeErosByPercent
`"ChangeErosByPercent"` alters the player's current amount of eros by a
percent in the following string. Can be negative. Percentages always round down.

``` json
"ChangeErosByPercent", "-10"
```

------------------------------------------------------------------------

## SetEros
`"SetEros"` will set the player's eros to a certain amount. For very
specific uses. **Take caution**.

``` json
"SetEros", "0"
```
