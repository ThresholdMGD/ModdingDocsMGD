# lineTriggers

See combatDialogueCreation for general
information on the *keys* used for
lineTriggers.

Remember that The "move": *key* can be
given an array, for any lineTrigger seen here. **However, it's so
responses can be made compact**. It does not at any point use the
*array* as a multi-check requirement
before it can trigger. That is, it's an *or* parameter, not an *and*
parameter. All matching lineTriggers matching the same `"move":`
*value* will ultimately go into the same
pool for it to randomly pull from.

For putting combat functions in strings, see [Dialogue Text Markup](../../Reference/Markup.md#dialogue-text-markup).

## Meta-Combat

### SetMusicTo

``` json
{
"lineTrigger": "SetMusicTo",
"move": [""],
"theText":[
  "Path/To/Song/Here.mp3"
  ]
},
```

Will change the current BGM at the start of combat.

Specify the song path in `"theText":`. Paths start from */game/*.
Additional *strings* will form a
playlist, causing it to loop between each song, from top to bottom.

Other monsters at the start of the encounter will append to the
playlist. Does not include monsters that are added to the encounter.

`"OverrideCombatMusicFunc"` will override
this lineTrigger.

### MonsterArrived

``` json
{
"lineTrigger": "MonsterArrived",
"move": [""],
"theText":[
  "This is triggered whenever the monster is added to an encounter.",
  "Triggers before StartOfCombat if monsters are added at the start of combat.",
  "Also must be called within the first 10 lineTriggers.",
  "The "move": key should be left empty"
  ]
},
```

### StartOfCombat

``` json
{
"lineTrigger": "StartOfCombat",
"move": [""],
"theText":[
  "This is triggered at the start of combat.",
  "Only for the first enemy listed in the encounter.",
  "It will also replace the generic line of enemies approaching.",
  "Also must be called within the first 10 lineTriggers.",
  "The "move": key should be left empty."
  ]
},
```

### EndOfRound

``` json
{
"lineTrigger": "EndOfRound",
"move": [""],
"triggersOnce": "ForAllMonsters",
"theText":[
  "Triggers at the end of every round of combat, before status effects tick down.",
    "A round would be whenever the player and all monsters present have each had at least one turn.",
    "Also must be called within the first 10 lineTriggers.",
    "Note that upon reaching the end of the round, it will trigger for each monster in the encounter.",
  "triggersOnce is a optional key unique to EndOfRound and StartOfRound.",
    "If set to 'ForAllMonsters', it will prevent the EndOfRound for any monsters after this one from being called.",
    "If set to 'ForSameMonsters', it will only prevent monsters of the same nameID from doing additional triggers.",
    "You can exclud the key entirely if you don't need it."
  ]
},
```

### StartOfRound

``` json
{
"lineTrigger": "StartOfRound",
"move": [""],
"triggersOnce": "ForSameMonsters",
"theText":[
  "Triggers at the start of a round.",
  "That is, when the player and all monsters have not yet had their turn.",
  "Also must be called within the first 10 lineTriggers.",
  "Note that upon reaching the start of the round, it will trigger for each monster in the encounter."
  "triggersOnce is a optional key unique to EndOfRound and StartOfRound.",
    "If set to 'ForAllMonsters', it will prevent the StartOfRound for any monsters after this one from being called.",
    "If set to 'ForSameMonsters', it will only prevent monsters of the same nameID from doing additional triggers.",
    "You can exclud the key entirely if you don't need it."
  ]
},
```

## Reactions

These take place after an action or condition is performed or met by
either the player or monster.

### HitWith & HitWithA

``` json
{
"lineTrigger": "HitWith",
"move": ["Thrust"],
"theText":[
  "Text is displayed after successfully hitting a monster with a skill.",
  "Only shown after they are hit.",
  "Note this can include skills used by items, or the item name itself.",
  "Biased towards Sex skills, but will use HitWithA pool as a fallback."
  ]
},
```

``` json
{
"lineTrigger": "HitWithA",
"move": ["Thrust"],
"theText":[
  "Text is displayed after successfully hitting a monster with a skill.",
  "Only shown after they are hit.",
  "Note this can include skills used by items, or the item name itself.",
  "Biased towards Anal skills, but will use HitWith pool as a fallback."
  ]
},
```

### UsesMove & UsesMoveA

``` json
{
"lineTrigger": "UsesMove",
"move": ["Tighten"],
"theText":[
  "Triggers when the specified skill is used by the monster.",
  "It's displayed before the move.",
  "Biased towards Sex skills, but will use UsesMoveA pool as a fallback."
  ]
},**
```

``` json

{
"lineTrigger": "UsesMoveA",
"move": ["Tighten"],
"theText":[
  "Triggers when the specified skill is used by the monster.",
  "It's displayed before the move.",
  "Biased towards Anal skills, but will use UsesMove pool as a fallback."
  ]
},
```

### UsesMovePre & HitWithPre

These happen prior to UsesMove and HitWith respectively, allowing you to
enforce expression changes or VFX or other functions in a neat bundle,
while ignoring low health line calls.

``` json
{
"lineTrigger": "UsesMovePre",
"move": ["Tighten"],
"theText":[
  "This gets put before a tighten used by the monster.",
  "You can use it for multiple random lines, but useally it will be a single line bundle as shown in the next example."
  ]
},**
```

``` json
{
"lineTrigger": "HitWithPre",
"move": ["Tighten"],
"theText":[
  "|f|ChangeEnergyQuietly|/|15|n|"
  ]
},
```

### Escape

``` json
{
"lineTrigger": "Escape",
"move": ["Distract"],
"theText":[
  "Triggers when the player successfully uses an escape skill.",
  "Examples would be Teleport, or Distract.",
  "If "move": is given a blank string, it will apply to any instance of an escape skill."
  ]
},
```

### EscapedRestraint

``` json
{
"lineTrigger": "EscapedRestraint",
"move": [""],
"theText":[
  "Triggers when the monster successfully escapes a restraint.",
  "It's uses are pretty neiche."
  ]
},
```

### LowHealth

``` json
{
"lineTrigger": "LowHealth",
"move": [""],
"theText":[
  "Triggers upon reaching less than 30% of their max health.",
  "Only happens once, heals will not reset it.",
  "The "move": key should be empty."
  ]
},
```

### PlayerLowHealth

``` json
{
"lineTrigger": "PlayerLowHealth",
"move": [""],
"theText":[
  "Triggers upon the player reaching less than 35% of their max health.",
  "Only happens once, resetting on orgasms.",
  "The "move": key should be empty."
  ]
},
```

### PlayerRecoil & PlayerRecoilA

``` json
{
"lineTrigger": "PlayerRecoil",
"move": ["Thrust"],
"theText":[
  "Checks if the specified skill the player used had recoil, triggering after the attack. Triggers before HitWith/HitWithA.",
  "Biased towards Sex skills, but will use PlayerRecoilA pool as a fallback."
  ]
},
```

``` json
{
"lineTrigger": "PlayerRecoilA",
"move": ["Thrust"],
"theText":[
  "Checks if the specified skill the player used had recoil, triggering after the attack. Triggers before HitWith/HitWithA.",
  "Biased towards Anal skills, but will use PlayerRecoil pool as a fallback."
  ]
},
```

### OnSurrender

``` json
{
"lineTrigger": "OnSurrender",
"move": [""],
"theText":[
  "Triggers when the player surrenders.",
  "The "move": key should be empty."
  ]
},
```

### OnPlayerEdge

``` json
{
"lineTrigger": "OnPlayerEdge",
"move": ["Thrust"],
"theText":[
  "Displays when the player edges.",
  "The "move": key can optionally be given a specific skill to check for.",
  "It can also take stances, or be left blank to generally trigger."
]
},
```

See the functions [DenyCombatOrgasm](../../Functions/CombatOnly/PlayerCombatAfflictions.md#denyplayerorgasm) and
[DenyPlayerOrgasmFunc](../../Functions/CombatOnly/IgnoreOrgasm.md).

### OnEdge

``` json
{
"lineTrigger": "OnEdge",
"move": [""],
"theText":[
  "Displays when the monster edges.",
  "The "move": key can optionally be given a specific skill to check for.",
  "It can also take stances, or be left blank to generally trigger."
]
},
```

See the functions [DenyCombatOrgasm](../../Functions/CombatOnly/MonsterCombatAfflictions.md#changemonsterarousal-changemonsterenergy-changemonsterspirit) and
[DenyMonsterOrgasmFunc](../../Functions/CombatOnly/IgnoreOrgasm.md).

### OnPlayerOrgasm

``` json
{
"lineTrigger": "OnPlayerOrgasm",
"move": ["Deepthroat"],
"theText":[
  "Displays when the player cums.",
  "The "move": key can optionally be given a specific skill to check for.",
  "It can also take stances, or be left blank to generally trigger.",
  "Lastly, the function PlayerOrgasm will not trigger OnPlayerOrgasm, only natural orgasms will do that."
  ]
},
```

### OnOrgasm

``` json
{
"lineTrigger": "OnOrgasm",
"move": ["Thrust"],
"theText":[
  "Displays when the monster cums.",
  "The "move": key can optionally be given a specific skill to check for.",
  "It can also take stances, or be left blank to generally trigger."
  ]
},
```

### PostOrgasm

``` json
{
"lineTrigger": "PostOrgasm",
"move": [""],
"theText":[
  "Displays after the monster orgasm line. This allows for some combat functions that may otherwise break up the orgasm line into janky parts.",
  "The "move": key can optionally be given a specific skill to check for.",
  "It can also take stances, or be left blank to generally trigger."
  ]
},
```

### OnLoss

``` json
{
"lineTrigger": "OnLoss",
"move": [""],
"theText":[
  "Displays after the monster is defeated and taken out of the encounter. DOES NOT FUNCTION IN SINGLE MONSTER FIGHTS (game explodes otherwise). Intended for multi enemy fights, but this never triggers if it's the final monster in an encounter. This has many uses, but take care not to call a function that would specify the original monster specifically, or it will crash the game.",
  "The "move": key can optionally be given a specific skill to check for.",
  "It can also take stances, or be left blank to generally trigger."
  ]
},
```

### PlayerRanAway

``` json
{
"lineTrigger": "PlayerRanAway",
"move": [""],
"theText":[
  "Displays when the player has run away from an encounter! Pretty neiche, but can be useful for monsters that aren't in full events, like the Salarisi."
  ]
},
```

## Counters

These work to counter their various of conditions before they take
place.

The trigger order of priority for Counters matches the listed order,
from top to bottom.

### AutoCounter

``` json
{
"lineTrigger": "AutoCounter",
"move": ["Caress"],
"theText":[
  "Triggers before the player uses the skill.",
  "Wait, Struggle, Run Away, Push Away, and Defend can also be used in "move":",
  "Note this can include skills used by items, or the item name itself."
  ]
},
```

### AutoCounterSkillTag

``` json
{
"lineTrigger": "AutoCounterSkillTag",
"move": ["Seduction"],
"theText":[
  "Same as AutoCounter, but will instead check a skill's "skillTags": list."
  ]
},
```

### AutoCounterSkillFetish

``` json
{
"lineTrigger": "AutoCounterSkillFetish",
"move": ["Legs"],
"theText":[
  "Same as AutoCounterSkillTag, but for the skill's "fetishTags": list."
  ]
},
```

### OffenceCounter

``` json
{
"lineTrigger": "OffenceCounter",
"move": [""],
"theText":[
  "This will trigger before the player can use any form of offence. That is, anything that affects the monster.",
  "This won't trigger from the player using something on themselves, like healing or buffing.",
  "The "move": key should be left empty."
  ]
},
```

### AnyCounter

``` json
{
"lineTrigger": "AnyCounter",
"move": [""],
"theText":[
  "Like OffenceCounter, but this will trigger prior to the player doing ANYTHING, including consumables, even if the monster is stunned.",
  "... ANYTHING, excludes Wait, Struggle, Run Away, Push Away, and Defend. Use AutoCounter to cover those.",
  "The "move": key should be left empty."
  ]
},
```

## Stance, Restraints

As the title suggests, contains lineTriggers specifically around stances
and restraints.

### StanceStruggle

``` json
{
"lineTrigger": "StanceStruggle",
"move": ["Making Out"],
"theText":[
  "Triggers upon the player trying to escape a stance prior to whether or not it succeeds or fails.",
  "It's recommended to make a one for each possible stance the monster can be in.",
  "Remember that the player can only initiate Sex, Making Out, or Anal on their own."
  ]
},
```

### StanceStruggleFail

``` json
{
"lineTrigger": "StanceStruggleFail",
"move": ["Making Out"],
"theText":[
  "Triggers upon the player failing to escape a stance."
  ]
},
```

### StanceStruggleComment

``` json
{
"lineTrigger": "StanceStruggleComment",
"move": ["Making Out"],
"theText":[
  "Like StanceStruggleFail, triggers after the player fails to escape a stance.",
  "Takes place after StanceStruggleFail, meant monster dialogue responses."
  ]
},
```

### StanceStruggleFree

``` json
{
"lineTrigger": "StanceStruggleFree",
"move": ["Making Out"],
"theText":[
  "Triggers upon the player successfully escaping a stance."
},
```

### StanceStruggleFreeComment

``` json
{
"lineTrigger": "StanceStruggleFreeComment",
"move": ["Making Out"],
"theText":[
  "Like StanceStruggleComment, triggers after the player successfully escapes a stance.",
  "Takes place after StanceStruggleFree, meant for monster dialogue responses."
  ]
},
```

### RestraintStruggle

``` json
{
"lineTrigger": "RestraintStruggle",
"move": ["Soft Amber Embrace"],
"theText":[
  "Triggers upon the player trying to escape a restraint, whether or not it succeeds or fails.",
  "Specify the specific restraint in The "move": key."
  ]
},
```

### RestraintStruggleCharmed

``` json
{
"lineTrigger": "RestraintStruggleCharmed",
"move": ["Soft Amber Embrace"],
"theText":[
  "Like RestraintStruggle, but usurps it if the player is charmed."
  ]
},
```

### RestraintEscaped

``` json
{
"lineTrigger": "RestraintEscaped",
"move": ["Soft Amber Embrace"],
"theText":[
  "Triggers if the player successfully escapes the specified restraint."
  ]
},
```

### RestraintEscapedFail

``` json
{
"lineTrigger": "RestraintEscapedFail",
"move": ["Soft Amber Embrace"],
"theText":[
  "Triggers if the player fails to escape the specified restraint."
  ]
},
```