# Adventure Additions

Adventure additions cover overwriting the base Adventure's `"Deck":`
*key* with your own data, expanding the
random monsters, monster groups, events, and loot from treasure.

This does mean your addition would be incompatible with other mods that
make changes to the `"Deck":` *key* for
the same Adventure.

Check **_AdventureAdditionExample.json** in *Json/Adventures/* for an
example.

The overview will proceed to go over each *key* you would find in a regular Adventure .json, how their role
changes, and if they're required in a addition.

!!! note

    `"Eros":`, `"requires":`, `"requiresEvent":`, and `"Description":`
    aren't used, and thus should be excluded for tidiness.

## name & Addition

``` json
"name": "Forest Dungeon",
```

Required so you can tell the game which Adventure you wish to make an
addition to.

``` json
"Addition": "Yes",
```

Required so you can tell the game that you're wishing to make an
addition. Can be added into almost any part of the file.

## Deck

``` json
"Deck": [
  "Event", "Name of an event",
  "RandomTreasure",
  "BreakSpot",
  "Monster", "Imp", "EndLoop",
  "RandomEvent"
],
```

Required, `"Deck":` **cannot** be excluded, nor left empty, even if your
goal isn't to modify the deck.

It's advised to copy and paste the *array* from the Adventure's original `"Deck":`
*key* as the basis of your addition, and
go from there.

## RandomEvents

``` json
"RandomEvents": ["Lust Rune", "Ninja Rest Ambush"],
```

Using this *key* in a addition adds to
the existing array. The *strings*
provided in the original `"RandomEvents":` *key* will still be present, and not overridden. As such, you are
only increasing the selection of events, not replacing, unlike the
`"Deck":` key.

## RandomMonsters & MonsterGroups

``` json
"RandomMonsters": ["Elf"],
"MonsterGroups": [
  {
  "Group": ["Elf", "Elf"]
  }
],
```

Using these *keys* in an addition adds to
the existing arrays, so the *strings* and
*objects* provided in the original
*keys* will still be present, not
overwritten. As such, you are only increasing the selection of monster
groups, not replacing.

These *keys* are required, but the
*arrays* can be left empty if you do not
wish to use it. `"MonsterGroups":` does not require an object.

## Treasure

``` json
"Treasure": [
  {
  "Common": ["Anaph Herb", "Ugli Herb"]
  },

  {
  "Uncommon": ["Unbound Rune", "Unbound Rune", "Soothing Potion"]
  },

  {
  "Rare": ["Panacea", "Energy Potion", "Cock Ring of Justice", "Power Belt"]
  }
],
```

Using this *key* in a addition adds to
the existing array, so the *strings*
provided in the original *key* will still
be present, and will not be overridden. As such, you are only increasing
the selection of loot, not replacing.

`"Treasure":` and its *objects* are
required, but the *arrays* can be left
empty if you do not wish to use it.
