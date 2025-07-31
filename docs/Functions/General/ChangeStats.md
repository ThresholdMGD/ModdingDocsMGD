# Change Stats
## Change Stat Functions
Changes the players given stat by the given amount, permanently. Take
caution using these. See
[Eros](../../Functions/General/Eros.md) and
[GiveExp](PlayerGiveAndTake.md#giveexp) as well.

-   `"ChangeMaxArousal"`
-   `"ChangeMaxEnergy"`
-   `"ChangeMaxSpirit"`
-   `"ChangePower"`
-   `"ChangeWill"`
-   `"ChangeTech"`
-   `"ChangeAllure"`
-   `"ChangeLuck"`
-   `"ChangeInt"`

``` json
"ChangeInt", "2"
```

------------------------------------------------------------------------

## ChangeSensitivity
Changes the target sensitivity for the player by the given amount.

``` json
"ChangeSensitivity", "Sex", "5"
```

See Sensitivity.

------------------------------------------------------------------------

## PermanentlyChangeSensitivity
Same as above but will permanently affect the player. This prevents the
church from recovering the player stats. Take caution.

See Sensitivity.

------------------------------------------------------------------------

## PermanentChangeStatusEffectResistances
Permanently alters the players status effect resistance. It's
recommended to use perks for less permanent afflictions.

``` json
"PermanentChangeStatusEffectResistances", "Charm", "10"
```

[Resistances](../../Reference/StatusEffectRef.md#resistances)

------------------------------------------------------------------------

## ChangeFetish
Changes the target fetish for the player by the given amount. Often used
in loss scenes.

``` json
"ChangeFetish", "Kissing", "25"
```

See *Json/Fetishes/* for all current fetishes. This includes addictions.

At level 25, the player is considered to have the fetish. Maximum of
level 100, minimum of 0, ignoring perks and items.

------------------------------------------------------------------------

## PermanentlyChangeFetish
Same as above but will permanently affect the player. This prevents the
church from recovering the player stats. **Use with caution**.

------------------------------------------------------------------------

## SetFetish
Same as above but sets the fetish/addiction to the number given. This
change is permanent and prevents the church from recovering the player
stats. The primary intent is for event based addictions and fetishes to
be managed easier. **Use with caution**.

------------------------------------------------------------------------

## RespecPlayer
Gives the player the ability to reinvest all of their stat points, perk
points, and sensitivity points earned thus far.
