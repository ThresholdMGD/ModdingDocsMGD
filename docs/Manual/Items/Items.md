# Item Creation
Breaks down the keys and strings used by Items. See [The JSON Format](../../Tutorials/TheJsonFormat.md) for more information.

Go to *Json/Items/*, and then see the .json files present for examples,
and **_BlankItem.json** for a template.

**Assume all keys are required, unless stated otherwise.**

## name

``` json
"name": "Name of item",
```

Sets the name of the item that will be displayed to the player in-game,
and for internal referral.

## itemType

``` json
"itemType": "The item type",
```

Decides the behavior and use cases of the item, greatly influencing how
the following *keys* will behave.

::spantable::

| values              | Description                                 | Perks key Behavior      | Skills key Behavior     | Stats key Behavior      |
|---------------------|---------------------------------------------|-------------------------|-------------------------|-------------------------|
| `"Accessory"`         | A type of equipment. Only applied while worn.| Gives perk while worn.  | Gives skill while worn. | Alters stats while worn.|
| `"Rune"`              | A type of equipment. Only applied while worn.| Gives perk while worn.  | Gives skill while worn. | Alters stats while worn.|
| `"Consumable"`        | Can be used in and out of combat encounters. | None, see [useOutcome](#useoutcome) instead @span=2:4   |          | Alters stats when used. @span=1:4 |
| `"CombatConsumable"`  | Can only be used in combat encounters.       |                    |                    |                    |
| `"NotCombatConsumable"`| Can only be used outside of combat encounters.  |                    |                    |                    |
| `"DissonantConsumable"`| Uses skill's outcome in combat, useOutcome out of combat.|  |  |  |
| `"Key"`               | Called a Key Item in-game.                   | None @span                    |                    |                    |
| `"Loot"`              | Cannot be used by the player.                |                  |                    |                    |

::end-spantable::

## cost

``` json
"cost": "0",
```

The cost of the item in shops. For reference, the sell cost will always
be 50% of the provided value.

## descrip

``` json
"descrip": "",
```

The description of the item that is displayed both in shops and the
character inventory. Be sure to use [itemmarkup](../../Reference/Markup.md#item-markup) to grab the values from the item's [flat stat keys](#flat-stat-keys).

## tags
``` json
"tags": ["Tag Name Here", "Another Tag"],
```

Categorizes items together when they share a tag value, such as for use
in [Item Functions <itemFunctions>](../../Functions/General/Inventory.md).

## requires & requiresEvent

``` json
"requires": ["Name of a required item", "Another item that may be required"],
```

Retrieve the `"name:"` key(s) another item to use as a requirement for
players to access the item in shops. Typically a *key* Item.

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
alternative to "requires":.

Given it's an array, you can introduce multiple requirements of the
same type by providing duplicate *objects* for as long as it contains all four of the given keys.

You need to provide a *value* for
`"Progress":` and '"ChoiceNumber":', else it will not work. If you
don't wish to use one of them, use the default
*values* above. `"NameOfEvent":` and
`"Choice":` need at least empty strings.

If in use, you cannot exclude unused *keys* in the object, they must all be present. If
`"requiresEvent":` isn't being used at all, it can be excluded from the
file entirely.

## perks

``` json
"perks": [""],
```

To apply perks via equipment related item types.

## skills

``` json
"skills": [""],
```

For equipment item types, the *key* will
give all listed skills for as long as the item is equipped. **Take
caution that it means runes can give a skill multiples times.**

For consumable item types, it will utilize the given skill upon use.
**Note it can only take one skill, even if the key technically
accepts an array.** You have the option to provide a
*value* of `"UseableItem"`, which older
consumable items used to directly apply the [Flat Stats
Keys](#flat-stats-keys). Modern practices encourage using skills
directly over `"UseableItem"`.

## Flat Stats Keys <a id="flat-stat-keys"></a>

``` json
"hp": "0",
"ep": "0",
"sp": "0",

"Exp": "0",
```

For consumable item types, flatly recovers or alters the corresponding
stat based on the value. Negative *values* will have opposite effect.

Equipment and loot item types will instead flatly influence the
corresponding stat by its max, ignoring `"Exp":`. Can use negative
values.

It can be used in combination with `"skills":`.

## Core Stat & Resistance Keys

``` json
"Power": "0",
"Technique": "0",
"Intelligence": "0",
"Allure": "0",
"Willpower": "0",
"Luck": "0",

"BodySensitivity": {
    "Sex": "0",
    "Ass": "0",
    "Breasts": "0",
    "Mouth": "0",
    "Seduction": "0",
    "Magic": "0",
    "Pain": "0",
    "Holy": "0",
    "Unholy": "0"
},

"resistancesStatusEffects": {
    "Stun": "0",
    "Charm": "0",
    "Aphrodisiac": "0",
    "Restraints": "0",
    "Sleep": "0",
    "Trance": "0",
    "Paralysis": "0",
    "Debuff": "0"
},
```

Only applicable to equipment and loot item types. Alters the given stat
for the wielder, can use negative values.

## Status Effect Keys

``` json
"statusEffect": "None",
"statusChance": "0",
"statusPotency": "0",
```

Only applicable to consumable item types.

::spantable::

| Key | Description | Special values |
|-----|-------------|----------------|
| "statusEffect" | Cleanses the given status effect. | "all" will cleanse all status effects. Use "None" if you don't intend to use it. |
| "statusChance" | The percent chance for it to successfully cleanse on use. | "0" or "100" will ensure it always cleanses. |
| "statusPotency" | Subtracts by the given amount from status effect's potency if applicable. | "0" cleanses it entirely. |

::end-spantable::

See Status Effects.

## useOutcome
``` json
"useOutcome": "",
```

Provides a line of dialogue when using a consumable. Can use text markup
and in-text functions. Typically overridden by the listed Skill's
outcome line, unless the `"itemType":` is `"DissonantConsumable"`, or if
it has no skill at all.

## useMiss
``` json
"useMiss": ""
```

Currently not used by the game. The *key*
is optional and thus can be excluded, or be kept as placeholder.
