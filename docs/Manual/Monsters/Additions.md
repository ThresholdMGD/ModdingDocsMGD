# Monster Additions

Monster additions cover the scope of expanding their skills, perks, item
drops, loss and victory scenes, combatDialogue, and overwriting the
pictures key.

If you want to change the stats of a monster, you can currently do so
via StartOfCombat, and using the related
functions found
[here](../../Functions/General/ChangeMonster.md).

Check **_MonsterAdditionExample.json** in */Json/Monsters/* for an
example.

The overview will proceed to go over each *key* you would find in a regular Monster .json, how their role
changes, and if they're required in a addition.

!!! note

    All other *keys* outside of the ones
    listed aren't used, and thus should be excluded for tidiness.

## IDname & Addition

``` json
"IDname": "Elf",
```

Required so you can tell the game which Monster you wish to make an
addition to.

``` json
"Addition": "Yes",
```

Required so the game knows you are making an addition.

## skillList

``` json
"skillList": ["Blowjob", "Thirsty Blowjob", "Super Succ"],
```

Appends to the existing array. Leave a blank *string* in the *array* if you don't
intend to use it.

## perks

``` json
"perks": ["Pacing"],
```

Appends to the existing array. Leave a blank *string* in the *array* if you don't
intend to use it.

## itemDropList

``` json
"ItemDropList": [
  {
  "name": "Elven Herbs",
  "dropChance": "75"
  },

  {
  "name": "Frog Rune",
  "dropChance": "75"
  }
],
```

Appends to the existing *array* of
objects. Don't give the *key* an
*object* if you don't wish to use it.

## lossScenes & victoryScenes

``` json
"lossScenes": [
  {
  "NameOfScene": "Cuddling Loss",
  "move": "",
  "stance": "Cuddling",
  "includes": ["Elf"],
  "theScene":[
    "Speaks",
    "Cuddling is nice but can we bang instead?"
    ],
  "picture": ""
  }
],

"victoryScenes": [
  {
  "NameOfScene": "Cuddling Victory",
  "move": "",
  "stance": "Cuddling",
  "includes": ["Elf"],
  "theScene":[
    "Speaks",
    "C-could we at least bang while cuddling?"
    ],
  "picture": ""
  }
],
```

Appends to the existing *array* of
objects. Don't give the *keys* an
*object* if you don't wish to use it.

You currently cannot replace existing scenes by copying their conditions
and scene name.

## combatDialogue

``` json
"combatDialogue": [
  {
  "lineTrigger": "UsesMove",
  "move": "Blowjob",
  "theText": [
    "Replaced dialogue."
    ]
  },
  {
  "lineTrigger": "StanceStruggleFree",
  "move": "Cuddling",
  "theText": [
    "'Th-that felt nicer than I thought it would...'"
    ]
  }
],
```

Appends to the existing *array* of
objects, if there are no other *objects*
that match it in exact requirements. Otherwise, if it matches the
`"move":` and `"lineTrigger":` *keys* in
values, it will replace `"theText":` *key* data, not append to it. Remember that `"move":`
*arrays* is an *or* parameter, so any
skills or stances listed across multiple *objects* for the same type of lineTrigger will add to the same pool.

## pictures

``` json
"pictures": [

]
```

You can and should exclude the pictures *key* entirely if you don't intend to use it. Otherwise, it's
recommended to copy and paste the character's pictures
*key* and work from there. A more
in-depth explanation on how to do minimal image related additions will
be given in the future as soon as some unexpected issues are resolved,
in the meanwhile, building on top of a copy/paste will work.
