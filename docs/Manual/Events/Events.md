# Event Creation
Breaks down the *keys* and
*strings* used by Events.

Base game Event .jsons are located at *Json/Events/*. The bubble slime
events showcase modern practices well, located at
*Mountain/FizzySpring.json*, and
*CombatEvents/BubbleSlimeCombatEvents.json*.

A blank template can be found at *Events/\_BlankEvent.json*.

**Assume all keys are required, unless stated otherwise.**

## name

``` json
"name": "Name of Event",
```

The name of the event is presented in the Grimoire and for internal
referral.

## CardType

``` json
"CardType": "Event",
```

Changes how the game calls and utilizes the event. See [CardType
Values](#cardtype-values) below for all possible values.

### CardLimit

-   `"CardLimit": "0",` sets the maximum limit of `"Event"` CardTypes
    that can be added to the Grimoire by the player. Set to `"0"` if not
    used by the CardType, or for no limit to the amount of events.

### CardType Values

#### Grimoire CardType

::spantable::

| CardType | Description | Example |
| -------- | ----------- | ------- |
| `"Event"` | Will appear in the Grimoire in the "Events:" section. The only *value* with interacts with `"CardLimit":`. | *Events/Labyrinth/ExploreLaby/WanderingVenefica* |
| `"Quest"` | Will appear in the Grimoire in the "Quests:" section. | *Events/Quests/* |

::end-spantable::

#### Town CardType

::spantable::

| CardType | Description | Example |
| -------- | ----------- | ------- |
| `"Shopping"` | Will appear as an option for the respective location in the town. Putting `"EnterArea"` in the `"Description":` *key* will make it trigger when the player enters that location. @span | *Events/Town/* @span |
| `"Church"` |             |         |
| `"Guild"` |             |         |
| `"Inn"` |             |         |

::end-spantable::

#### Brothel CardType

::spantable::

| CardType | Description | Example |
| -------- | ----------- | ------- |
| `"BarShift"` | Will be called for the shift choice the player or Belle makes. Putting another shift type in the `"Description":` *key* will make it count for that shift too. Repeating the same shift type increases its chances. @span | *Events/Town/Brothel/* @span |
| `"WaiterShift"` |             |         |
| `"GloryHoleShift"` |             |         |
| `"DayShift"` | Used for shifts during the day. Can also be combined with the previous three shift types via `"Description":`, or repeated for higher chances. | |

::end-spantable::

#### Triggered CardType

::spantable::

| CardType | Description | Example |
| -------- | ----------- | ------- |
| `""` | Not automatically triggered by anything. Typically used for combat events and dedicated loss/victory events. Can be accessed through Event Jumps. | *Events/CombatEvents/Mountain/CamillaCombatEvents.json* |
| `"EndOfDay"` | Triggers upon the start of a new day. Useful for tracking addictions. | *Events/TimePassing/EndOfDay.json* |
| `"TimePassed"` | Triggers when any amount of time has passed. Useful for tracking player status effects. | *Events/TimePassing/TimePassed.json* |
| `"StepTaken"` | Triggers when players transition between events or encounters during adventures. Also useful for triggering player status effects. | *Events/TimePassing/StepTaken.json* |
| `"EndOfTurn"` | Triggers specifically at the end of turn, primarily for player functions as it triggers every turn regardless of who's fighting. | *Events/CombatEvents/PlayerEndOfTurn.json* |
| `"EndOfCombat"` | Triggers at the end of combat. For specific player skills such as Pin, see as an example. | *Events/CombatEvents/Player/PlayerEndOfCombat.json* |
| `"StartOfTurn"` | Triggers specifically at the start of turn, primarily for player functions as they Triggers every turn regardless of who's fighting. | *Events/CombatEvents/PlayerStartOfTurn.json* |
| `"StartOfCombat"` | Triggers at the start of every combat, generally for player combat event use. | *Events/CombatEvents/Player/PlayerStartOfCombat.json* |
| `"PlayerOrgasm"` | Triggers every time the player orgasms, including out of combat. | *Events/CombatEvents/OrgasmEvents.json* |
| `"Dream"` | Called when the player sleeps, via the [SleepPlayerFunc](../../Functions/General/Time.md#sleep-functions) function. Note that no dreams will be called if `"SleepPlayer"` is followed with `"DelayNotifications"`. | *Events/TimePassing/Dreams/* |

::end-spantable::

## Description

``` json
"Description": "A description of the event",
```

When used for a Grimoire [CardType](#cardtype), it will present the
*string* you provide on the right hand
side of in the Grimoire when players are reviewing events and quests for
selection.

When used for town card types, providing it with the
*string* `"EnterArea"` will make it
trigger when the player enters that location.

When used for brothel shift card types, using a different shift type
will make it count for that shift too. Repeating the same shift type
increase its chances.

## requires & requiresEvent

``` json
"requires": ["Vandal Note"],
```

Retrieve the `"name:"` key(s) of an
[Item](../../Manual/Items/Items.md) to use as
a requirement for players to access the event, primarily for the
Grimoire. Typically a *key* Item. The
*key* must be included, but the
*array* can be left empty. You can leave
either a blank *string* or none at all.

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

## Speakers

``` json
"Speakers": [
  {
  "name": "IDname of Monster",
  "postName": "",
  "SpeakerType": ""
  },
  {
  "name": "IDname of another Monster",
  "postName": " A postName.",
  "SpeakerType": ""
  }
],
```

`"Speakers":` gives functionality for the `"Speaks"` function, used in
dialogue. Each speaker will need to be put in a separate object. Each
*object* added is correlated to a number
in the `"Speaks"` function, starting from 2 for the second
*object* to a maximum of 12 added
speakers, ordered by each *object* added
from top to bottom. See
[Dialogue](../../Functions/General/Dialogue.md) for more information on the `"Speaks"` function.

`"name":` must be from the `"IDname":` *key* of a
[Monster](../../Manual/Monsters/Monsters.md).
Don't worry, it will proceed to display the *string* in the monster's `"name":`, not the IDname.

`"postName":` will place the data provided in the
*string* after their name, for example,
if you wanted to differentiate multiple generic monsters (Elf 1, Elf 2,
etc). Can use the `"SetPostName"` function to override it for all
characters. See the function page
[Speakers Specific](../../Functions/EventOnly/SpeakersSpecific.md) for more information.

`"SpeakerType":` currently only serves one purpose. If set to `"?"` will
let you put in any name you wish for the `"name":` key, regardless if
they even have a monster json. Alternatively, the `"Speak"` function can
be used instead. Otherwise, it can be left with an empty string.

While `"Speakers":` and at least one *object* with the listed *keys* must
be included, it doesn't necessarily need to be used. All
*keys* in the *objects* require at least an empty string.

## IgnoredDebugChoices

``` json
"IgnoredDebugChoices": [
  {"11": []},
  {"12": ["SpecificValue1", "SpecificValue2"]}
],
```

`"IgnoredDebugChoices":` is an optional *key* that allows you to specify which choices should be ignored
by the 'Debug Game Data On Startup' feature (found in game options)
when checking for unused choices. Used when implementing choices for not
yet developed content and other edge cases.

In the example above, the event's choices will be handled as follows: -
All values for choice number 11 will be ignored. It *has* to be
formatted like this with the empty list in order to be accepted by the
game. - Only "SpecificValue1" and "SpecificValue2" will be ignored
for choice number 12.

See [Choice](../../Functions/EventOnly/Choice.md) for more information on event choices.

## EventText

``` json
"EventText": [
  {
  "NameOfScene": "EventStart",
  "theScene": [
    "While walking an intricate pink rune suddenly appears beneath you!",
    "Menu",
    "Do something!",
    "See what happens.",
    "EndLoop"
    ]
  },
  {
  "NameOfScene": "Do something!",
  "theScene": [
    "You trip on the pink rune and suffer a bad headache."
    ]
  },
  {
  "NameOfScene": "See what happens.",
  "theScene": [
    "It's a pink rune. It continues to exist defiantly."
    ]
  }
]
```

`"EventText":` is an *array* of
*objects* containing the series of scenes
that will make up your event. Each *object* will contain the exact same keys.

`"NameOfScene":`, which takes a *string*
you provide it to uniquely identify the scene. They can contain whatever
you please.

`"theScene":` which takes an *array* of
*strings* that make up the scene. These
*objects* are plainly called scenes. Your
*strings* will be displayed to the user
as narrative text, unless it's identified as a function.

The first scene added will always display first for your average event
jump from any of the `"CardType":` values. However, specific scenes in a
event can be jumped to, either by a game feature or by a function.

See [functions](../../Functions/index.md) for
the vast range of functions that can be used in scenes.

### Optional Scenes

When debugging scenes (see [FAQ](../../Reference/FAQ.md) for debugging info), you may find yourself with scenes you don't intend to ever be
linked to by a function. In this case, you can declare it as an optional
scene to the game by prepending its `"NameOfScene":`
*value* with any of the following:

-   An `_` underscore. Intended for any scenario where you want the
    debugger to ignore the scene, such as internal notes, cut content,
    or in-progress work not meant to be accessed by the player yet.
-   `event` or uppercased `Event`. Loosely intended for your starting
    and ending scenes, such as `"EventStart"` (your very first scene)
    and `"EventBroke"` (your very last scene).
-   `debug` or uppercased `Debug`. Loosely intended for scenes made for
    debugging purposes while making the event. Sometimes used in place
    of `"EventBroke"` as last scene.

``` json
{
"NameOfScene": "_EllyProgression",
"theScene": [
  "Get through forest dungeon.: 5",
  "Clear temple: 5",
  "True Power Sigil Event: 5",
  "PLANS:",
    "+34 progress on a picnic outing with Venefica and Perpetua.",
    "+69 progress on silent mutual studying sessions together."
  ]
},
{
"NameOfScene": "EventBroke",
"theScene": [
  "Something went wrong when scene jumping! Event Progress: [ProgressDisplay]."
  ]
}
```

!!! tip

    Using `"EventStart"` and `"EventBroke"` as advised is a recommended
    practice.

    The games in certain scenarios will jump to the first event in your
    scene, meaning you may not have any links to your first scene at all.
    Using `"EventStart"` consistently for this makes it never a guess to
    remember, and causes it to be flagged as optional.

    If you accidentally jump to a scene that doesn't exist due to accidents
    like spelling errors, the game will always jump to the last scene in the
    event. Having `"EventBroke"` as your last scene with an error message
    will better inform you when testing your mod, and causes it to be
    flagged as optional.

