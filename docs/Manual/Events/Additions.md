# Event Additions
Event additions cover replacing specific scenes, adding new scenes, and
appending to the list of `"Speakers"`.

This does mean your addition would be incompatible with other mods that
make an addition to the same scenes in an Event. This excludes scenes
solely using MenuAdditions and SceneAdditions, for example, when adding to the night life menu in the
brothel.

Check **_EventAdditionExample.json** in *Json/Events/* for an example.

The overview will proceed to go over valid *keys* in event additions, how they're added to the base event
json, and if their inclusion is required.

!!! note

    `"CardType":` `"CardLimit":`, `"Description":`, `"requires"`, and
    `"requiresEvent":` aren't used, and thus should be excluded for
    tidiness.

## name & Addition

``` json
"name": "Lust Rune",
```

Required so you can tell the game which Event you wish to make an
addition to.

``` json
"Addition": "Yes",
```

Required so the game knows you are making an addition.

## Speakers

``` json
"Speakers": [
  {
  "name": "IDname of Monster you're adding",
  "postName": "",
  "SpeakerType": ""
  }
],
```

While required, it can be left without any *objects* if you don't intend to use it. All added
*objects* will be additions, no
exceptions.

This means if you want to say, add a `"postName":` to a character, you
will be limited to appending the character again and using the
appropriate `"Speaks"` function to use it. This isn't behavior specific
to Additions either, this is intended base game behavior as seen for
labeling multiple generics.

Note multiple mods adding to the Speakers *key* *could* throw `"Speaks"` out of order depending on which
mod is loaded first. Thus, it may be best to rely on
[SpeakFunc](../../Functions/General/Dialogue.md) for any new speakers instead
to avoid compatibility issues between mods.

## IgnoredDebugChoices

``` json
"IgnoredDebugChoices": [
  {"11": []},
  {"12": ["SpecificValue1", "SpecificValue2"]}
],
```

Not required, will append specified choices to be ignored by the 'Debug
Game Data On Startup' feature (found in game options), including new
event choices and choice values specific to your mod.

See [Choice](../../Functions/EventOnly/Choice.md) for more information on event choices.

## EventText

``` json
"EventText": [
  {
  "NameOfScene": "Name of a Scene already in the game.",
  "theScene": [
    "The new strings provided to theScene."
    "Entirely replacing the original one."
    "JumpToScene", "A New Scene"
    ]
  },
  {
  "NameOfScene": "A New Scene",
  "theScene": [
    "An entirely new scene added to the event."
    ]
  }
]
```

Required, though you technically don't have to provide it with any
objects.

Every new *object* will be appended,
unless `"NameOfScene":` within the *object* matches an existing `"NameOfScene":` within the event, in
which case it will override and replace the entirety of `"theScene":`
with the one provided via the new object. The exception to this behavior
is when using `"MenuAddition"`.

### Scene Additions

There are standout instances where you wish to append to options in an
existing scene, without causing incompatibility issues with other mods.
The game supports special
[functions](../../Functions/index.md) for
this purpose:

-   `"MenuAddition"` for appending to scenes (e.g. night life menu via
    Brothel) with [MenuFunc](../../Functions/EventOnly/Menu.md). Meta
    functions are included.
-   `"ShopAddition"` for appending to scenes (e.g. Amber's item shop)
    with a [ShoppingMenu](../../Functions/General/Shop.md).
-   `"SkillShopAddition"` for appending to scenes (e.g. Elena's skill
    shop) with a [SkillShoppingMenu](../../Functions/General/Shop.md#skill-shopping)
-   `"PrependScenes"` for prepending to scenes. (e.g. NPC scene jump
    congratulations for beating a new location dungeon)
-   `"AppendScenes"` for appending to scenes. (e.g. extra fluff dialogue
    to a scene without a jump at the end.)

You can make use of them through a duplicate scene in the event addition
with the same `"NameOfScene":` value. Then, start with one of the three
above variants depending on the function you're adding to, only one per
scene. **The first and last string of the scene must be the
variant, and `"EndLoop"` respectively.**

For `MenuAddition"`, if the menu you are appending to doesn't have a
`"FinalOption"` in use already, you will have to add it yourself. it's
intended to be applied to 'back out' or 'leave' options, ensuring
they are always at the bottom of the game menu. When addressing this,
duplicate the 'leave' choice of the base game, and prepend it with the
*strings*
`"OverrideOption", "FinalOption"`. This ensures it ignores duplicates
from other mods also trying to address the issue.

See the examples below for details of the implementation, and the
**_SceneAdditionExample.json** file in the *Json/Events/* for more
advanced examples.

``` json
"EventText": [
  {
  "NameOfScene": "The Menu's Scene Name",
  "theScene": [
    "MenuAddition",
      "New menu choice",
      "RequiresEnergy", "50",
      "The other new menu choice",
      "OverrideOption", "FinalOption", "Leave",
    "EndLoop"
    ]
  }
]
```

``` json
"EventText": [
  {
  "NameOfScene": "The Shop's Scene Name",
  "theScene": [
    "ShopAddition",
      "Imp Juice",
      "A new mod item",
    "EndLoop"
    ]
  }
]
```

``` json
"EventText": [
  {
  "NameOfScene": "The Skill Shop's Scene Name",
  "theScene": [
    "SkillShopAddition",
      "A new mod skill",
      "Another new mod skill",
    "EndLoop"
    ]
  }
]
```

``` json
"EventText": [
  {
  "NameOfScene": "NPC Intro Jump Event",
  "theScene": [
    "PrependScene",
    "GetEventAndIfChoice", "Dungeon's Tracking Event"
      "1", "DungeonCompletedValue", "NPCCongratulationToJumpToHere"
    ]
  }
]
```
