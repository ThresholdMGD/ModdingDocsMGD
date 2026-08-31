# Fetish & Addiction Creation

This json type serves a dual purpose system covering both fetishes and addictions in the game. Addictions are invisible trackers using the same systems in the game as fetishes, but not exposed to the player in the game menus.

## Reference

See [The JSON Format](../../Tutorials/TheJsonFormat.md) for optional information on JSONs if terminology like "Key", "String", "Array" or "Value" are unfamiliar.

Base game Fetish .jsons can be found in the game folder *Json/Fetishes/* for both fetish **and** addictions alike. 

A blank template can be found at *_BlankFetish.json*

When not making an Addition, **assume all keys are required, unless stated otherwise.**

## Additions

When a JSON file contains `"Addition": "Yes"`, the game does not create a new entry. Instead, it looks up an existing entry by its identifier (in this case `"name"`) and applies the addition data based on the default behavior for each key.

For additions, only `"name"` is required and cannot be changed. **All other keys are optional and can be excluded for tidiness.**

| Key | Strategy |
|---|---|
| `name` | identifier |
| All other keys | overwrite |

For an overview of behaviors for keys, see [Additions](../../Reference/Additions.md).

## Fetishes

Making a custom fetish comes down to making a .json like the following
code block:

``` json
{
"FetishList": [
    {
    "Name": "Atom",
    "BaseLevel": "0",
    "Type": "Fetish",
    "CreationOn": "Enlightened!",
    "CreationOff": "Heathen.",
    "ToolTip": "How much you love to mod with the Atom text editor.\n\nVerdict: ",
    "LevelText": [
      ["0", "You'd rather use Notepad++"],
      ["25", "You'll use Atom just a little bit..."],
      ["50", "You can't help but use Atom as your text editor."],
      ["75", "You're overflowing with installed packages..."],
      ["100", "You're completely obsessed with Atom! Hopefully it never shuts down in the future..."]
    ]
    }
  ]
}
```

`"FetishList":` will contain an *array*
of *objects* representing each fetish.
See *Fetishes/fetishList.json* for reference.

All *keys* are required unless stated
otherwise.

### Name

`"Name":` decides the name of your fetish, used for both internal
reference and to be shown to the player in menus and skills.

### BaseLevel

`"BaseLevel":` can optionally give a default amount of the fetish,
regardless if it's selected by the player in the creation menu. Give it
a *string* of "0" if you do not wish to
use it.

### Type

`"Type":` should be set to "Fetish", unless making an Addiction, as
documented below.

### CreationOn & CreationOff

The provided *strings* will be the
dialogue the Goddess gives in the creation menu when starting a new
game. `"CreationOn":` being if the player selects the fetish,
`"CreationOff":` if the player unselects the fetish.

### ToolTip

`"ToolTip":` will display the given *value* when viewing a fetish in the character menu and character
creation. Be sure to keep `\n\nVerdict:` as the end of your
*string* value.

Only for Fetishes.

### LevelText

`"LevelText":` will conditionally display one of the given
*values* based on whether it meets the
given fetish level.

``` json
"LevelText": [
  ["0", "You still can't get over the loss of Atom."],
  ["34", "You think VS Code might be a worthy supplement with the One Dark theme..."],
  ["69", "You can't help but salivate at the quality git implementation."],
  ["100", "You're completely obsessed with VS Code. You have a hard time not fantasizing about its built-in terminal."]
  ]
```

Only for Fetishes.

## Addictions

Addictions, being technically fetishes, use all the same functions and
*keys* as their counterpart, with the
exception of being invisible to the player. They can be put in the same
JSON file together, or optionally separated for organization, like the
base game.

It's recommended to go to *Fetishes/addictionList.json* and see the
comments Threshold provided for each base game addiction, and use your
editor's search features to review how they are used throughout the
base game via the *strings* provided to
the `"Name":` keys.

!!! note

    Addictions don't use the `"ToolTip":` and `"LevelText":`
    *keys* and thus can be excluded.

``` json
{
"FetishList": [
    {
    "Name": "Required for internal reference of the addiction.",
    "BaseLevel": "0",
    "Type": "Addiction",
    "CreationOn": "This text won't appear in-game, but still needs filled out so the game doesn't generate an error.",
    "CreationOff": ""
    }
  ]
}
```

As one can see, you really only need to provide `"Type":` with
`"Addiction"`, and provide `"Name":` with a unique
*string* to use for internal referral.
The rest is unused, but required to prevent an error on runtime.
