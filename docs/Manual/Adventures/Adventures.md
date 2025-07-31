# Adventure Creation

Breaks down the keys and strings used by Adventures. See [The JSON Format](../../Tutorials/TheJsonFormat.md) for more information.

Go to *Json/Adventures/*, and then see the *.json* files present for
examples, and **_BlankAdventure.json** for a template.

**Assume all keys are required, unless stated otherwise.**

## name

``` json
"name": "Name of an Adventure",
```

Sets the name of the adventure for the menu choice of a location on the
map.

## Description

``` json
"Description": "Description of the Adventure.",
```

Give a brief description of the adventure. Currently unused in-game, but
is expected.

## requires & requiresEvent

``` json
"requires": ["Name of a required item", "Another item that may be required"],
```

Retrieve the `"name:"` key(s) of an
[Item](../../Manual/Items/Items.md) to use as
a requirement for players to access the adventure. Typically a
*key* Item.

While the *key* must still be included,
the *array* can be left empty if you do
not wish to use it. You can leave either a blank
*string* or none at all.

``` json
"requiresEvent": [
  {
  "NameOfEvent": "",
  "Progress": "-99",
  "ChoiceNumber": "-1",
  "Choice": ""
  }
],
```

A more complex and optional *key* that
contains *objects* that will check for
progress or choice in a event. It can be used in alongside or as an
alternative to `"requires":`.

Given it's an array, you can introduce multiple requirements of the
same type by providing duplicate *objects* for as long as it contains all four of the given keys.

You need to provide a *value* for
`"Progress":` and `"ChoiceNumber":`, else it will not work. If you
don't wish to use one of them, use the default
*values* above. `"NameOfEvent":` and
`"Choice":` need at least empty strings.

If in use, you cannot exclude unused *keys* in the object, they must all be present. If
`"requiresEvent":` isn't being used at all, it can be excluded from the
file entirely.

## MusicList

``` json
"MusicList": [ "music/Mountain/Purple Planet Music - Chilled - Desert Winds (3_12).mp3"],
```

An optional *key* for a default selection
of music to loop through during adventures outside of events and
encounters.

## Deck

``` json
"Deck": [
  "Event", "Name of an event",
  "Monster", "Elf", "EndLoop",
  "BreakSpot",
  "Monster", "Blue Slime", "Elf", "EndLoop",
  "RandomTreasure",
  "RandomEvent"
],
```

Specify the order of encounters and events the player will face upon
starting the adventure, linearly as given from start to finish. It can
technically be left empty, but doing so will just send players straight
back to town upon selection of the adventure, giving the adventure no
purpose.

Below are all the *values* you can
provide within the *array* to trigger
various interactions.

::spantable::

| Value                   | Description                                                      |
|-------------------------|------------------------------------------------------------------|
| "Event,"                | Jumps to an event given in the following string.                 |
| "Monster,"              | Starts a monster encounter. Provide a *string* of the ID name of each included monster, close the list with "EndLoop."                                                                                            |
| "RandomEvent,"          | Random event from the **RandomEvents** *key* below.              |
| "RandomMonsters,"       | Random encounter from the [RandomMonsters & MonsterGroups](#randommonsters-monstergroups) *keys* below.                                                                                       |
| "RandomTreasure,"       | Random treasure of random rarity from the [Treasure & Eros](#treasure-eros) *keys* below.                                                                                       |
| "CommonTreasure,"       | Random common treasure from the [Treasure & Eros](#treasure-eros) `"Common":` *keys* below.                                                                                       |
| "UncommonTreasure,"     | Random uncommon treasure from the [Treasure & Eros](#treasure-eros) `"Uncommon":` *keys* below.                                                                                       |
| "RareTreasure,"         | Random rare treasure from the [Treasure & Eros](#treasure-eros) `"Rare":` *keys* below.                                                                                       |
| "BreakSpot,"            | Break spot. The player can choose to move on, rest, or return to town.                                                                                        |
| "Unrepeatable"          | Upon reaching this *string* in a deck, the adventure becomes unavailable for repeating, preventing the player from accessing the adventure again. **Do not use this if you want players to be able to replay the adventure**. |

::end-spantable::

Remember to make sure the last *string*
you provide doesn't have a trailing comma.

## RandomEvents

``` json
"RandomEvents": ["Lust Rune", "Elven Ambush"],
```

Set the random events that can be selected by the `"RandomEvent"`
*string* for the `"Deck":`
*key* above. If you wish to make certain
events more likely, put it in multiple times.

## RandomMonsters & MonsterGroups

``` json
"RandomMonsters": ["Blue Slime", "Lizard Girl"],
```

Set the random monsters you can encounter for the `"RandomMonsters"`
*string* for the `"Deck":`
*key* above. If you wish to make a
certain monster more likely, put them in multiple times. Requires use of
the `"MonsterGroups":`, found below.

``` json
"MonsterGroups": [
  {
  "Group": ["Blue Slime", "Elf"]
  },

  {
  "Group": ["Lizard Girl"]
  }
],
```

Sets the possible formations monsters in the `"RandomMonsters":` can
take. Each *object* with a `"Group":`
*key* will represent a different possible
formation. You can intermix different monsters via the arrays, even if
the monster isn't present in `"RandomMonsters":`. Repeat an
*object* with a certain formation
multiple times if you wish to make it more likely. Works the same as a
[Location's](../../Manual/Locations/Locations.md) `"MonsterGroups":`.

While the *key* is required, you do not
have to provide an *object* if you do not
wish to use formations.

## Treasure & Eros

``` json
"Treasure": [
  {
  "Common": ["Calming Potion", "Calming Potion", "Anaph Herb", "Ugli Herb"]
  },

  {
  "Uncommon": ["Calming Potion", "Energy Potion", "Luck Rune", "Luck Rune", "Soothing Potion"]
  },

  {
  "Rare": ["Panacea", "Stoic Rune", "Stoic Rune", "Gloves of Skill", "Gloves of Skill", "Power Belt"]
  }
],
```

Sets the possible items that can be earned from chests for each type of
treasure rarity. The listed *objects* and
their *keys* must be included, and each
*array* must have at least one item.

``` json
"Eros": [
  {
  "Common": "25"
  },

  {
  "Uncommon": "75"
  },

  {
  "Rare": "150"
  }
]
```

Sets the amount of eros given from chests for each type of treasure
rarity in the adventure from treasure in the [Deck](#deck). The listed
*objects* and their *keys* must be included, and each
*key* must provide a *value* in their string.
