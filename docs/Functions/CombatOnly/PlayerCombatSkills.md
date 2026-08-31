# Player Combat Skills

!!! info "See also"

    For skills given permanently, see
    [Player Give & Take](../../Functions/General/PlayerGiveAndTake.md).

## GiveTemporarySkill & RemoveTemporarySkill

`"GiveTemporarySkill"` gives the player a skill that is automatically
removed at the end of a combat encounter.
`"RemoveTemporarySkill"` removes temporarily given skills early if found, otherwise ignored.

``` json
"GiveTemporarySkill", "Tail Cuddle",
"RemoveTemporarySkill", "Tail Cuddle"
```
