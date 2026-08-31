# Stat Reference

This page is purely for ease of reference for functions and keys, and is
not meant to contain any information on how each stat or sensitivity
works. The information in-game, or on the
[wiki](https://monstergirldreams.miraheze.org/wiki/Main_Page) should
prove sufficient for that purpose.

## Stats

The plain stat range is used in places such as:

- [StatCheck](../Functions/EventOnly/StatCheck.md),
- [StatEqualsOrMore](../Functions/EventOnly/PlayerChecks.md#statequalsormore),
- [SwapLineIf's](../Functions/General/SwapLineIf.md) `"Stat"` option
- Skill [statType](../Manual/Skills/Skills.md#stattype-requiredstat).

`"Arousal"`, `"Energy"`, and `"Spirit"` are treated as the maximums, with
their current amounts prefixed with `"Current"`.

-   `"Power"`
-   `"Technique"`
-   `"Intelligence"`
-   `"Allure"`
-   `"Willpower"`
-   `"Luck"`
-   `"Arousal"`, `"Energy"`, `"Spirit"` (maximums)
-   `"CurrentArousal"`, `"CurrentEnergy"`, `"CurrentSpirit"` (current amounts)

## IfStat Stat Names

The IfStat range, used by
[IfStat](../Functions/EventOnly/PlayerChecks.md#ifstat) and
[IfMonsterStat](../Functions/CombatOnly/MonsterChecks.md#ifmonsterstat)
for their stat comparisons, and by SwapLineIf's `"Arousal"`,
`"Energy"`, `"MaxArousal"`, and `"MaxEnergy"` options.

`"Arousal"`, `"Energy"`, and `"Spirit"` are treated as the current amounts,
with their maximums prefixed with `"Max"`.

-   `"Arousal"`, `"Energy"`, `"Spirit"` (current amounts)
-   `"MaxArousal"`, `"MaxEnergy"`, `"MaxSpirit"` (maximums)
-   `"Level"`, `"Exp"`
-   `"Power"`, `"Technique"`, `"Intelligence"`, `"Allure"`, `"Willpower"`, `"Luck"`

The following are player only:

-   `"Virility"`, `"GoddessFavor"`, `"Strain"`

`"Arousal"`, `"Energy"`, `"Spirit"`, `"Exp"`, and `"GoddessFavor"` support percent
values.

## Sensitivity Reference

Above 100 is more sensitive, below 100 is less sensitive.

-   `"Sex"` (Counts as the player's Cock sensitivity and the Monster's
    Pussy sensitivity respectively)
-   `"Ass"`
-   `"Breasts"` (Counts as the player's Nipple sensitivity internally)
-   `"Mouth"`
-   `"Seduction"`
-   `"Magic"`
-   `"Pain"`
-   `"Holy"`
-   `"Unholy"`

## Equations

You can use the following equations when considering the balance of your
stats. You are free to deviate if you feel something needs tuned in a
particular way.

# Eros Per Enemy Level

For calculating how much Eros the player should earn when defeating a
enemy. `x` represents the given level.

``` python
(x)^2+(x*10)+48
```

# Exp Amount Per Player Level

For graphing how much Exp the player is required to collect before
leveling up. `x` represents the given level.

This can be used to decide how much Exp you want a monster to give.
Threshold typically does 60-100% of the Exp for the level the enemy is
at relative to the graph.

``` python
(0.4*(x*x))+(2*x)+(15*sqrt(x)-8)
```
