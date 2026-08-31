# JSON Additions

An **Addition** is a JSON file that changes an existing JSON instead of creating a new one. The game looks up the entry by its identifier (`"name"` for most types, `"IDname"` for Monsters) and applies only the keys you include.

## How To Make An Addition

1.  Examine the JSON of the entry you want to change.
2.  Add `"Addition": "Yes"` to a new addition file in your mod in the correct JSON type category (`ModName/Events/AdditionName.json`, `ModName/Locations/AdditionName.json`, etc.). The addition file's name is unimportant, as long as you personally can recognize it.
3. Add `"name"` (or `"IDname"` for Monsters) with the same value as the entry you're modifying. It must match exactly, or the addition is ignored.
4.  Add **only** the keys you need to change, referring to the JSON type's modding documentation.
5.  Check the JSON type's **Additions** table (see relevant Manual documentation) for how each key behaves in additions by default.

``` json
{
  "IDname": "Elf",
  "Addition": "Yes",
  "skillList": ["Blowjob", "Anal Penetration"]
}
```

!!! tip
    Only include the keys you intend to change. This minimizes brittleness with future game updates and reduces chances of conflicts with other mods.

## Key Behaviors

Each key has a default behavior, listed in the Additions section table for a JSON type's Manual page. It will be one of the following:

:::spantable::

| Behavior | Lists | Strings | Numbers |
|---|---|---|---|
| `overwrite` | Replaces the list. | Replaces the text. | Replaces the number. |
| `append` | Adds entries to the end. | Adds text to the end. | Adds the number on. |
| `prepend` | Adds entries to the front. | Adds text to the front. | Adds the number on. |
| `unique_append` | Adds entries only if they aren't already in the list. | Adds text only if it isn't already in there. | Adds the number on. |
| `unique_prepend` | Adds entries to the front only if they aren't already in the list. | Adds text to the front only if it isn't already in there. | Adds the number on. |
| `replace_or_append` | Replaces a matching entry, otherwise adds to the end. | Adds text only if it isn't already in there. | Adds the number on. |
| `replace_or_prepend` | Replaces a matching entry, otherwise adds to the front. | Adds text to the front only if it isn't already in there. | Adds the number on. |
| `merge` | Updates only the sub-keys you list inside a nested object, the rest are kept. Not used on lists, strings, or numbers. @span | | |
| `custom` | Special handling. See the key's documentation on its Manual page. @span | | |

:::end-spantable::

> Only keys labelled `custom` or `merge` limit which behaviors you can use. They will be mentioned in their respective *Override restriction* column.

You should only change the default behavior if it is the only option, or if you think it will improve compatibility with other mods and future updates.

### `unique_append` vs `replace_or_append`

The differences primarily come down to the intended key's structure you are making an addition to.

For a plain list (key structures that use square brackets `[]`, like an item's `tags`), `unique_append` skips entries that are already present from before your addition,
while `replace_or_append` behaves like a normal `append`, it wasn't meant for lists.

For a list of objects (key structures that use curly braces `{}`, like a Monster's
`lossScenes`), `replace_or_append` matches by the key's documented identifying field.

The below example of `"lossScenes"` performs a
`replace_or_append` by default. It checks a scene's `"NameOfScene"`, and replaces the
match, or appends if there is no match.

``` json
{
  "IDname": "Elf",
  "Addition": "Yes",
  "lossScenes": [
    {
      "NameOfScene": "Elf Blew It",
      "move": "Blowjob",
      "stance": "Blowjob",
      "includes": ["Elf"],
      "theScene": [
        "If an existing lossScene has the same NameOfScene, it gets replaced.",
        "Otherwise, this scene is appended to the lossScenes list.",
        "This lets you overwrite the values for the other keys.",
        "In this case moves, stances, includes, etc."
      ],
      "picture": ""
    }
  ]
}
```

For `append`, a scene with the same `"NameOfScene"` would have been added as a
duplicate. The game finds the original first, so your replacement would never play.
`unique_append` can't replace it either, as it compares whole entries and no two scene
objects are exactly equal.

## Changing A Key's Behavior

You override by adding the key `"additionOverrides"`, including the name of each key you wish to override, and setting its value to the intended behavior.
See the following item addition example:

``` json
{
  "name": "Adventurer's Bookmark",
  "Addition": "Yes",
  "additionOverrides": {
    "descrip": "append",
    "perks": "append"
  },
  "descrip": " A favorite among adventurers!",
  "perks": ["Bookmark"]
}
```

What this does in practice:

- **`descrip`** defaults to `overwrite` for items, so without the override " A favorite among adventurers!" would replace the item's entire description. With `"append"` it's instead added to the end of the existing description, see how it adds a space at the start to avoid adding 'favorite' with no spacing to the original text.
- **`perks`** defaults to `unique_append` for items, where it ignores adding perks that already exist in the key's list. Changing to `append` would let you add the same perk multiple times, in this case adding `"Bookmark"` again even though the item already grants it. With the default `unique_append`, an already present perk is skipped.

## The Three Rules

- You can't change the identifier key.
- Empty values (`""`, `[]`, `"0"`) are ignored in additions, so blanking a value won't erase it. Regardless, you should avoid including these. If you wish to intentionally set a value to zero, make it a negative zero: `"-0"`.
- Mods should follow best practices to avoid overwriting data from other mods, done by using additive key behaviors. `append`, `unique_append`, `replace_or_append`, `prepend`, `merge`, and Event scene behaviors all help avoid accidentally modifying other mods.

## Legacy Safety Feature

For backwards compatibility, some keys may be ignored in mods with a [meta JSON](../GettingStarted/MetaCreation.md) that declares a `testedFor` version prior to `v28.1`. 
After updating `testedFor` to access the modern addition system, keep yourself in constant referral to each JSON type's modding documentation, 
remove any and all keys in your mod not relevant to your actual mod contents, actually test all content in-game, and keep an eye out for abnormalities.

Here's the kind of thing you'd need to fix. An old monster addition copies a key it isn't changing — `moneyDropped`, which has no addition behavior of its own:

``` json
{
  "IDname": "Elf",
  "Addition": "Yes",
  "skillList": ["Blowjob", "Anal Penetration"],
  "moneyDropped": "50"
}
```

While `testedFor` is below v28.1, `moneyDropped` is silently ignored, so nothing breaks. The moment you update `testedFor` to v28.1+, 
the same key is applied as an overwrite, forcing the Elf's `moneyDropped` to `"50"` and stomping whatever the current game or another mod set. 
The fix is to prune the addition to only what you're actually changing:

``` json
{
  "IDname": "Elf",
  "Addition": "Yes",
  "skillList": ["Blowjob", "Anal Penetration"]
}
```

Examples:

- `"exploreTitle":` in Location JSONs set to `"Addition"` in especially old mods before `"Addition": "Yes"` existed.
- Monster additions copying stat keys they aren't changing, causing it to insert dated stat values that modern game versions have since changed.
- Listing the Event's `Speakers` key you aren't using. 