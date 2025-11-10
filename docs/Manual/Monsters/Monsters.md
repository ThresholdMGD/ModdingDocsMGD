# Monster Creation

Breaks down the keys and strings used by Monsters. See [The JSON Format](../../Tutorials/TheJsonFormat.md) for more information. Despite
its name, this does encompass all characters, including town NPCs.

Go to */Json/Monsters/*, and then see the .json files present for
examples, and **_BlankMonster.json** for a template.

**Assume all keys are required, unless stated otherwise.**

## name & IDname

``` json
"name": "monster name",
```

Sets the name of the monster that will be displayed to the player
in-game.

``` json
"IDname": "monster IDname",
```

The internal name of the monster for use in json files. You will be
working with this whenever a function or *key* asks for which monster you wish to refer to.

## species

``` json
"species": "Monster species",
```

This currently has no functionality, but is best included for
forward-compatibility if it's ever introduced to the game.

When making a monster, you can refer to existing monster .jsons to see
what their species is as reference towards what you decide on for yours.

## gender

``` json
"gender": "female",
```

The gender of the monster. It primarily exists at the moment to
distinguish normal monster jsons, and
[Monster Additions](../../Manual/Monsters/Additions.md).

## description & encyclopedia

``` json
"description": "Monster description goes here.\n\nNote how the markup was called twice, and that space wasn't used.",
```

The description of a monster. This is given to the player in a card if
the monster has no art, or if they disabled it in the options menu.

See DialogueTextMarkup for more
information on the markup example in the above.

The *string* can technically be left
blank if you intend to use art from the get-go, but it's still
recommended.

``` json
"encyclopedia": "Lore information",
```

Lore related information given about monsters on the right hand side of
the Grimoire during exploration. Doesn't necessarily need to be a
generic enemy.

The *string* can be left blank if you
don't intend for the Monster to be available by themselves via the
monster selection in the Grimoire.

## tags

``` json
"tags": "none",
```

Like `"species":`, it currently has no functionality, but is best
included in case of future use. All monsters are currently given a
*value* of `"none"`.

## generic

``` json
"generic": "True",
```

Decides whether system related combat dialogue should refer to the
monster as a generic character, e.g. slimes, elves, etc. or as a unique
character, e.g. Trisha, Perpetua, etc.

If they are generic, provide a *value* of
`"True"`. If they are unique, a *value*
of `"False"`.

## requires & requiresEvent

``` json
"requires": ["Vandal Note"],
```

Retrieve the `"name:"` key(s) of an
[Item](../../Manual/Items/Items.md) to use as
a requirement for players to access the monster, primarily for the
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

## skillList

``` json
"skillList": ["Caress", "Kiss", "Kiss"],
```

The list of [Skills](../../Manual/Skills/Skills.md) the monster can use while in combat, based on the exact
*value* provided to a Skill's `"name":`
key. Repeating a skill will increase the chances the monster shall
randomly call it.

See */Json/Skills/* for skills found in the base game that the monster
can use. This does include player skills.

Provide a blank *string* if you don't
wish to use the key.

## perks

``` json
"perks": ["Semen Eater", "Semen Eater", "Monster Pacing"],
```

The list of [Perks](../../Manual/Perks/Perks.md) the monster can use while in combat, based on the exact
*value* provided to a Perk's `"name":`
key. Repeating a Perk will apply it twice.

See */Json/Perks/* for perks found in the base game. Of note is the
folder */EnemyOnlyPerks/*.

Provide a blank *string* if you don't
wish to use the key.

## stats

``` json
"stats": {
  "lvl": "1",
  "Exp":"10",
  "max_hp":"80",
  "max_ep":"10",
  "max_sp": "1",
  "Power": "6",
  "Technique": "4",
  "Willpower": "7",
  "Allure": "7",
  "Luck": "3"
},
```

The stats of the monster in combat. While otherwise straightforward,
there are three *keys* in particular to
be aware of:

-   `"max_ep":` only pertains towards how quickly the monster can fall
    asleep. They will recover it in its entirety on orgasm. Threshold
    likes to use 30-50 for normal enemies, 100 for most bosses.
-   `"lvl":` does effect exp gain modifiers relative to the player's
    level, so be sure to scale it appropriately to be a rough match for
    the location and general stats of the monster. Do remember you still
    have total creative freedom though.
-   `"Exp":` represents the amount of exp given at the end of combat.

## Fetishes

``` json
"Fetishes": ["Cock|/|50", "Anal|/|25"],
```

The list of fetishes a monster may have. See */Json/Fetishes/* for all
base game fetishes. This does include addictions.

To apply the level of the fetish, use \|/\| as a separator between the
fetish and the level within the same string, and then provide a positive
numerical *value* on the other side.

Provide a blank *string* if you don't
wish to use the key.

## BodySensitivity

``` json
"BodySensitivity": {
  "Sex": "100",
  "Ass":"100",
  "Breasts":"100",
  "Mouth":"100",
  "Seduction": "100",
  "Magic": "100",
  "Pain": "100",
  "Holy": "100",
  "Unholy": "100"
},
```

The sensitivities of the monster. Going above 100 makes them more
sensitive, going below makes them less sensitive.

## resistancesStatusEffects

``` json
"resistancesStatusEffects": {
    "Stun": "0",
    "Charm": "0",
    "Aphrodisiac": "0",
    "Restraints": "0",
    "Sleep": "0",
    "Trance": "0",
    "Paralysis": "0"
    "Debuff": "0"
},
```

The status effect resistances of the monster. A positive
*value* increases their resistance, a
negative *value* will decrease.

## moneyDropped & itemDropList

``` json
"moneyDropped": "25",
```

The amount of eros the monster provides.

``` json
"ItemDropList": [
  {
  "name": "Anaph Herb",
  "dropChance": "75"
  },

  {
  "name": "Anaph Rune",
  "dropChance": "75"
  }
],
```

Specify the name of the
[Item](../../Manual/Items/Items.md) in
`"name":`, and provide the percent chance the item drops in
`"dropChance":`. Make a new *object* for
every additional item the monster can drop. Repeating items will
increase the potential quantity of times they drop the item.

## lossScenes & victoryScenes <a id="combat-scenes"></a>

``` json
"lossScenes": [
  {
  "NameOfScene": "Anal Loss",
  "move": "Thrust",
  "stance": "Anal",
  "includes": ["Elf", "Elf"],
  "theScene":[
    "This can tack functions that aren't event only.",
    "Check monsters in the base game for examples of it in action.",
    "You are also free to point it to an event at any point in the scene.",
    "JumpToEvent", "Example Event"
    ]
  "picture":""
  }
  {
  "NameOfScene": "Universal Loss",
  "move": "",
  "stance": "",
  "includes": [""],
  "theScene":[
    "Players don't have to be sent back to town in a loss scene, but do remember to recover their spirit a bit.",
    "An example would be Vili's Trial Of Titties lossScenes.",
    "Really, they are up to you in how you wish to use them."
    ]
  "picture":""
  }
],
```

Each *object* represents a scene that
will play on loss. Each must be individually identified via the
`"NameOfScene":` key.

### Requirements

You can optionally provide parameters which allow certain scenes to take
priority over other scenes depending on how the encounter ended. In
order of priority, top to bottom...

-   `"includes":` covers monsters that are needed for the scene.
-   `"move":` name of the skill that concluded the encounter.
-   `"stance":` the stance that the monster is currently in. It
    currently can only cover one stance.

`"picture":` is unused but technically functional. This changes the
background picture upon starting the scene, but is largely succeeded by
ChangeBGFunc.

Ensure you have one universal use scene with no requirements, else
players can potentially cause the game to crash from going to a scene
that doesn't exist.

If you want to have menus or just generally more advanced scene logic,
you can point the loss scene to immediately jump to an event.

``` json
"victoryScenes": [
  {
  "NameOfScene": "Anal Victory",
  "move": "",
  "stance": "Anal",
  "includes": ["Elf"],
  "theScene":[
    "Speaks",
    "I'm okay with my current situation."
    ],
  "picture": ""
  }
],
```

Functions exactly the same as `"lossScenes":`, but for when the player
wins.

## combatDialogue

``` json
"combatDialogue": [
  {
  "lineTrigger": "HitWith",
  "move": "Thrust",
  "theText":[
    "The chosen string displayed is random.",
    "You can have as many as you want, and repeat as many as you want for increased odds.",
    "You can have as many as you want, and repeat as many as you want for increased odds.",
    "'Put something in single quotes if you want it to be seen as something the character is saying.'"
    ]
  },
  {
  "lineTrigger": "UsesMove",
  "move": "Tighten",
  "theText": [
    "You don't need to use multiple strings if you're looking for a singular result.",
    ]
  }
],
```

`"combatDialogue":` contains triggers in the form of
*objects* that are checked for during
combat to bring a result if it's matched. It extends well beyond just
dialogue responses and reactions during combat.

`"lineTrigger":` decides what the trigger is checking for. **For a list
of all possible triggers and how they work**, see
lineTriggers.

`"move":` a conditional parameter, most commonly used to represent a
skill that was used. **Can be an** ***array*** **to compact responses into one object, as it's an**
***or*** **parameter, not an** ***and*** **parameter.** Compacting where
possible is recommended as it does help reduce game load times.

`"theText":` contains a list of all possible results of the trigger.
It's random, but you can repeat *strings* to make some more common than others.

Note all matching `"lineTrigger":` and `"move":`
*values* will ultimately go into the same
pool the game randomly pulls from, as the game takes every trigger in
combatDialogue and translates the *values* from `"theText:"` into the same pool.

## pictures

You can give a blank *array* if you
intend to use a text-based card based on the given
*value* to `"description":` for temporary
or permanent use:

``` json
"pictures": [

]
```

Otherwise, this section will go over the following example:

``` json
"pictures": [
  {
    "Name": "Base",
    "StartOn": "1",
    "AlwaysOn": "1",
    "IsScene": "0",
    "TheBody": "1",
    "Overlay": "No",
    "setXalign": "0.0",
    "setYalign": "0.13",
    "Images": [
      {
        "Name": "Base",
        "File": "Monsters/Bubble Slime/body_BubbleSlime.png",
        "setXalign": "0.0",
        "setYalign": "0.0"
      }]
  },
  {
    "Name": "Face",
    "StartOn": "1",
    "AlwaysOn": "1",
    "IsScene": "0",
    "TheBody": "0",
    "Overlay": "No",
    "setXalign": "0.0",
    "setYalign": "0.0",
    "Images": [
      {
        "Name": "Base",
        "File": "Monsters/Bubble Slime/face_BubbleSlime_Base.png",
        "setXalign": "0.0",
        "setYalign": "0.0"
      },
      {
        "Name": "Blush",
        "File": "Monsters/Bubble Slime/face_BubbleSlime_Blush.png",
        "setXalign": "0.0",
        "setYalign": "0.0"
      }]
  },
  {
  "Name": "Expression",
  "StartOn": "1",
  "AlwaysOn": "1",
  "IsScene": "0",
  "TheBody": "0",
  "Overlay": "No",
  "setXalign": "0.0",
  "setYalign": "0.0",
  "Images": [
    {
        "Name": "Base",
        "File": "Monsters/Bubble Slime/expression_BubbleSlime_Base.png",
        "setXalign": "0.0",
        "setYalign": "0.0"
    },
    {
        "Name": "Curious",
        "File": "Monsters/Bubble Slime/expression_BubbleSlime_Curious.png",
        "setXalign": "0.0",
        "setYalign": "0.0"
    }]}]
```

The `"pictures":` *key* contains an
*array* of objects, each representing a
functional layer of images for the character.

The Bubble Slime above is chosen as an example of a standard setup,
featuring a body (e.g. Clothed or Nude), face (e.g. Blush or no-blush),
and expression (e.g. Happy, Pouting) setup.

There are many *keys* to unpack so each
*object* will be gone over in separate
parts, starting with the base object, representing a single image layer.
Here is an overview:

``` json
{
  "Name": "Base",
  "StartOn": "1",
  "AlwaysOn": "1",
  "IsScene": "0",
  "TheBody": "1",
  "Overlay": "No",
  "setXalign": "0.0",
  "setYalign": "0.13",
  "Images": [
    {
    }
  ]
}
```

The following *keys* are required:

::spantable::

| Key | Description |
|-----|-------------|
| `"Name"` | Name of the layer for functions to call upon. |
| `"StartOn"` | Whether the layer is on by default when the character is first displayed |
| `"AlwaysOn"` | Whether the layer can never be turned off and instead always get the first image. |
| `"IsScene"` | Whether it's a scene, also ensuring it's centered on the screen, ignoring x and y align |
| `"TheBody"` | If the layer is the character's base. The x and y alignment of this layer dictates the x and y of every other layer. |
| `"Overlay"` | Put the name of another layer here to overlay this one on it. Any images with matching name fields will sync up. Check Shizu and Elly for an example. |
| `"setXalign"` | Changes the alignment of the layer on the x-axis. Generally done in increments of 0.01 or 0.1 depending. |
| `"setYalign"` | Changes the alignment of the layer on the y-axis. Generally done in increments of 0.01 or 0.1 depending. |

::end-spantable::

The following predetermined key-value combinations are optional, there should only be one at a time in a single image layer object:

::spantable::

| Key | Description |
|-----|-------------|
| `"Player": "Yes"` | If the image layer is for representing the player, use this key-value combination. This will recolor the layer based on the player's appearance settings. Excluding the key causes it to be considered off. |
| `"Player": "Silhouette"` | When representing the player in an image layer, you need to make another variant of it for use with this key-value combination. If the player set their appearance to silhouette, this image layer will be automatically used by the game. |

::end-spantable::

The `"Images":` *key* in these layer *objects* feature an *array* where the image and all its variants are declared, each image variant being contained in its object. They are handled using functions found in the [Image Layers documentation](#image-layers-documentation). The *object* works as follows:

::spantable::

| Key | Description |
|-----|-------------|
| `"Name"` | Name of the image in the layer to be called in functions. |
| `"File"` | The file path to the image. |
| `"setXalign"` | Changes the alignment of the image on the x-axis. |
| `"setYalign"` | Changes the alignment of the image on the y-axis. |

::end-spantable::

!!! note

    The image layers within `"pictures":` are displayed in the order they
    are added, so make sure everything is in the intended arrangement to
    avoid layering conflicts.

### Image Sets

`"Set":` is an optional *array* for
making preset image layer setups intended for especially complex
characters.

They can range from minor to drastic changes in character presentation
for immense ease of use when swapping between certain looks in various
scenarios.

Examples would be Aiko and Vili with alternative body proportions, the
former having an especially complex setup you can review with their
clothing layers.

They are handled with specific functions via
Image Layers documentation.

``` json
"pictures": [
  {
      "Name": "Base",
      "Set": [
        {
          "Name":"Base",
          "StartOn": "1",
          "AlwaysOn": "1",
          "IsScene": "0",
          "TheBody": "1",
          "Overlay": "No",
          "setXalign": "0.0",
          "setYalign": "0.0",
          "Images":[
            {
            "Name":"Base",
            "File": "Monsters/Imp/Imp_Body.png",
            "setXalign": "0.0",
            "setYalign": "0.0"
            }
            ]
      }
    ]
  },
  {
      "Name": "Sex",
      "Set": [
        {
          "Name": "Sex",
          "StartOn": "1",
          "AlwaysOn": "1",
          "IsScene": "0",
          "TheBody": "1",
          "Overlay": "No",
          "setXalign": "0.0",
          "setYalign": "0.0",
          "Images":[
            {
            "Name": "Base",
            "File": "Monsters/Imp/SexCG/impCG_Background.png",
            "setXalign": "0.0",
            "setYalign": "0.0"
            }
            ]
      }
    ]
  }
]
```

Further examples would be CGs found among Beris, Aiko, Minotaur, Blue
Slime, and other base game monster .jsons.

It is highly recommended to look these files over to help understand
this system till a proper tutorial can be made in the future.

### Roles

``` json
"pictures": [
{
  "Name": "Sex",
  "Set": [
    {
      "TextBoxXAdjust": "55",
      "Role": "FaceRider",
      "StanceRequired": "Face Sit",
      "MonsterRequired": "Imp",
      "CGTranslator": [
        {
          "In": "Expression",
          "Out": "FaceImpExpressionRide"
        }],
        "TogglesLayers": [
          "FaceImpExpressionRide",
          "FaceImp"
        ],
        "ActiveRequirment": "Yes"
    },
    {
      "Name": "Sex",
      "StartOn": "1",
      "AlwaysOn": "1",
      "IsScene": "0",
      "TheBody": "1",
      "Overlay": "No",
      "setXalign": "0.0",
      "setYalign": "0.0",
      "Images":[
        {
          "Name": "Base",
          "File": "Monsters/Imp/SexCG/impCG_Background.png",
          "setXalign": "0.0",
          "setYalign": "0.0"
        }
  ]}]}
]
```

`"Role:"` is an alternative *object* with
different *keys* compared to the typical
image layer object, for use only under `"Set"`.

When a monster uses a role, it takes the role's 'slot', meaning only
one instance of the monster can use a single role at a time.

Each role *object* is checked in the
order they are added to the image set. Roles are checked relative to the
encounter order. (e.g. Each listed role checks Imp 1 -\> Imp 2 -\> Imp
12).

This means you can declare as many roles as you want, but only up to 12
will ever be used at a time, as that is the maximum number of monsters
in an encounter.

All *keys* are required unless stated otherwise, but all *values* can be blank `""` or empty `[]` unless stated otherwise:

::spantable::

| Key           | Description |
|---------------|-------------|
| `"Role"`              | The name of the role's 'slot'. This must not be blank. |
| `"StanceRequired"`    | The required stance in order to allocate the role. |
| `"MonsterRequired"`   | Looks for the given `"nameID"` of the monster that is required to consider the role active and fulfilled. |
| `"TextBoxXAdjust"`    | Optional, adjust position of the dialogue box for CG visibility. |

::end-spantable::

`"CGTranslator"` takes *objects* in its *array* for translating any number of image layers (e.g. Expressions) to their equivalent image layer elsewhere while the role is allotted to the instance of the monster.

This allows for different layers to automatically utilize the same [ChangeImageLayer](#changeimagelayer) functions across the overall CG.

::spantable::

| Key      | Description |
|----------|-------------|
| `"In"`  | The layer it is checking for as its equivalent. |
| `"Out"` | The layer that is changed instead. |

::end-spantable::

```json
"CGTranslator": [
  {
    "In": "Expression",
    "Out": "FaceImpExpressionRide"
  }],
```

`"TogglesLayers"` Turns on the given *array* of image layers, still adhering to the layer's settings. They will turn off when the role is no longer allotted to any monster.

``` json
"TogglesLayers": [
  "FaceImpExpressionRide",
  "FaceImp"
],
```

`"ActiveRequirment": "Yes"` will require this role for the image set CG to be enabled, otherwise, the CG will automatically be turned off. Any number of roles can have this *key* set to `"Yes"`.


!!! tip

    See [ImageSetRoleStart](#imagesetrolestart) and [RoledCGEnd](#roledcgend) functions for turning it on and off respectively.
