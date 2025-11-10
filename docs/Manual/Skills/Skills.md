# Skill Creation
Breaks down the *keys* and
*strings* used by Skills.

Go to *Json/Skill/*, and then see the .json files present for examples,
and **\_BlankSkill.json** for a template.

**Assume all keys are required, unless stated otherwise.**. If it requires a non-blank (e.g. `""`)
*value* depends on the given
`"skillType":` *value* and any noted
technicalities.

## name
``` json
"name": "Name of Skill",
```

Sets the name of the skill, presented to the player in various locations
throughout the game and interface, and for internal referral.

## costType & cost
``` json
"costType": "ep",
```

The type of cost the skill requires in order to be casted. The `"cost":`
*key* seen below decides the amount based
on its given value.

There are three possible types:

-   `"ep"` consumes the caster's current energy by a given amount.
-   `"hp"` inflicts arousal on the caster by the given flat amount plus
    an additional percent based on `(max health - 100) * 0.15`.
-   `"sp"` deducts the given amount of spirit from the caster. This is a
    flat deduction, so it does run the risk of the player defeating
    themselves by mistake.

``` json
"cost": "10",
```

The given numerical amount of the requirement cost and deduction for the
caster, based on the given resource from `"costType"`.

Negative numbers technically work to allow the cost to benefit the
caster, though that means the skill will have no visible downside,
unless intended to be countered in a combat event.

## requiredLevel & learningCost
``` json
"requiredLevel": "1",
```

Level required for the player to learn the skill from a vendor. Does not
prevent the player from using the skill if they later don't meet its
requirements while still possessing the skill.

The *key* does not apply to monsters, and
thus can be safely removed for tidiness in such cases.

``` json
"learningCost": "100",
```

Ero cost of the skill from vendors in-game.

The *key* does not apply to monsters, and
thus can be safely removed for tidiness in such cases.

## skillType
``` json
"skillType": "attack",
```

The type of skill it's, deciding its overall functionality. This
influences the behavior of later keys. The following table presents all
possible *values* it can be given.

  ------------------ -----------------------------------------------------------
  `"attack"`         Increase the target's arousal, and can apply a status
                     effect via the `"statusEffect":` key.

  `"Healing"`        Recover the target's arousal, and can remove a given
                     status effect via the `"statusEffect":` key. *+75
                     initiative*.

  `"HealingEP"`      Recover the target's EP, and can remove a given status
                     effect via the `"statusEffect":` key. *+75 initiative*.

  `"HealingSP"`      Recover the target's SP, and can remove a given status
                     effect via the `"statusEffect":` key. *+75 initiative*.

  `"statusEffect"`   The skill is intended to inflict a status effect on the
                     target.

  `"Afflict"`        Like the `statusEffect` type, but specifically for
                     consumables, ensuring the player can use the item as
                     expected when outside of combat.
  ------------------ -----------------------------------------------------------

## statType & requiredStat
``` json
"statType": "Luck",
```

The type of stat the skill scales off of, used by various keys. See
Stats.

``` json
"requiredStat": "10",
```

The required amount of the given `"statType":` in order to learn the
skill from vendors in-game. It does not prevent the player from using
the skill if they later don't meet its requirements while still
possessing the skill.

## skillTags
``` json
"skillTags": ["Ass", "Breasts"],
```

What locations on the body that the skill targets, allowing it to appear
in the relevant section of the player's list of skills, assisting
monster AI, and how the damage scales. See
Sensitivity for all applicable tags.

Note skills given the tag of `"Holy"` will scale with the player's
virility.

Additionally, prefixing a tag with `display` (e.g. `"displayAss"`,
`"displayPain"`, etc.) will display the skill in the corresponding
section of the player's list of skills, without making it scale or be
recognized internally as a part of the given sensitivity. **They're
required for** `"Holy"` **and** `"Unholy"` **tagged skills that
otherwise feature no other tags.**

## fetishTags
``` json
"fetishTags": ["Oral", "Handholding"],
```

What fetishes (and addictions) the skill targets, scaling the damage
accordingly, and assisting monster AI. See *Json/Fetishes/* for all base
game fetishes and addictions.

Some tips to take note of:

-   `"Penetration"` can also be used to cover both `"Sex"` and `"Anal"`,
    for flexible damage calculations, game logic, and assisting monster
    AI.
-   Monsters can have a `"Cock"` fetish for any player and monster
    skills related to the player's magnum rod.
-   Monsters initiating Sex and Anal stances should have the
    corresponding fetish used in their penetrating skill, while using
    `"Penetration"` for skills that take place in either stance.

## targetType
``` json
"targetType": "single",
```

What participants in the encounter are intended to be struck by the
caster's skill.

  ------------ -----------------------------------------------------------
  `"self"`     The caster uses the skill on themselves.

  `"single"`   Hits the chosen target with the skill once.

  `"2Hits"`    Like `"single"`, but loops 2 times.

  `"3Hits"`    Loops 3 times.

  `"4Hits"`    Loops 4 times.

  `"5Hits"`    Loops 5 times.

  `"all"`      Hits all targets present in the encounter. Player only.

  `"Escape"`   The caster uses the skill to try and escape all given
               stances, and if applicable, restraint. Player only.
  ------------ -----------------------------------------------------------

## Stance & Control Keys
Take heed to think through the logic of your stance control
*keys* to avoid any potential mishaps or
errors that'd prevent them from working as expected. Ensure
capitalization is correct. Also keep in mind that stances are nebulous,
see [Stance Reference](../../Reference/StanceRef.md).

You can optionally apply or remove a stance via the following keys.

  -----------------------------------------------------------------------------------------------------
  `"startsStance": ["Sex", "Making Out"],`   Applies any of the given stances.

  `"removesStance": ["Penetration"],` Removes the listed stances for both the caster and target.
  `"All"` removes all current stances. `"Target"` removes all
  stances from the target.
  -----------------------------------------------------------------------------------------------------

Critically, the skill can be made unavailable to the player or monster
AI depending on the conditions of the following technically optional
keys. If you aren't using it and it doesn't mention using `""`, `"0"`,
or `"None"`, you should remove it to avoid confusing the AI.

  ----------------------------------------------------------------------------------------------- -----------------------------------------------------------
  `"requiresStance": ["Sex"],` Requires the **caster** to be in the specified stances. You can also use `"Any"` or `"None"`.

  `"unusableIfStance": ["Anal"],` **Caster** cannot be in any of the specified stances. You can also use `"Any"` or `"None"`.

  `"requiresTargetStance": ["Sex"],` **Target** must be in all of the specified stances. You can also use `"Any"` or `"None"`.

  `"unusableIfTarget": ["Cuddle"],` **Target** cannot be in any of the specified stances. You can also use `"Any"` or `"None"`.

  `"unusableIfTargetHasTheseSets": [[ "Blowjob", "Blowjob", "Blowjob", "Blowjob", "Blowjob"]],` **Target** cannot have any of these sets of
  *arrays* for active stances, meaning all of the listed stances at once. As per the
  example, if the target is in the blowjob stance 5 times (see imps), the skill cant be used.

  `"requiresStatusEffect": "Charm",` Requires **target** to have this status effect. You can also use `"None"`/`""`.

  `"requiresStatusPotency": "1",` Required **target** status effect must have a minimum of the given potency value. A reminder that it's optional, such as if only checking for Charm. Buffs and Debuffs check for the combination of all current stacks of potency to the given type.

  `"unusableIfStatusEffect": ["Paralyze"],` **Target** cannot have any of the specified status effects.

  `"unusableIfStatusPotency": ["5"],` **Target** cannot have potency equal to or higher for specified status effects in the previous key. You can also
  use `"0"` to simply check if it exists.

  `"requiresStatusEffectSelf": "Trance",` Requires **caster** to have this status effect. You can also use `"None"`/`""`.

  `"requiresStatusPotencySelf": "3",` Required **caster** status effect must have a minimum of the given potency value. A reminder that it's optional, such as if only checking for Charm.

  `"unusableIfStatusEffectSelf": [""],` **Caster** cannot have any of the specified status effects.
  You can also use `"None"`/`""`.

  `"requiresPerk": ["Action Rune!"],` **Target** must have all the specified perks. Can repeat a
  perk to require multiple stacks of the same perk.

  `"requiresOnePerk": "Swift",` **Target** must have the specified perk.

  `"unusableIfPerk": ["Rut"],` **Target** cannot have any of the specified perks.

  `"requiresPerkSelf": ["Pacing"],` **Caster** must have all the specified perks. Can repeat a perk to require multiple stacks of the same perk.

  `"requiresOnePerkSelf": ["Overlimit"],` **Caster** must have the specified perk. Can repeat a perk
  to require multiple stacks of the same perk.

  `"unusableIfPerkSelf": ["Well Fed"],` **Caster** cannot have any of the specified perks.
  ----------------------------------------------------------------------------------------------- -----------------------------------------------------------

Also see stanceconditions for adding
stance logic in a single spot, which works in any skill json, not just
skill additions.

## attack & healing Keys
``` json
"power": "10",
"minrange": "90",
"maxrange": "110",
"recoil": "25",
```

The following *keys* are required for
`"attack"` or any healing based `"skillType":` skills.

  ---------------------------------------------------------------------------------
  `"power": "25",`       Base damage or healing *value* of the skill.

  `"minRange": "70",`    The randomized percent minimum damage or healing range of
                         the skill.

  `"maxRange": "125",`   The randomized percent maximum damage or healing range of
                         the skill.

  `"recoil": "35",`      Percentage of the damage dealt to the target recoiled back
                         at the caster. Cannot be a negative value.
  ---------------------------------------------------------------------------------

``` json
"scalesWithStatusEffect": "Aphrodisiac",
"flatDamageSF-FlatScaling": "5",
"flatDamageSF-PercentScaling": "0",
"fotalDamageSF-PercentScaling": "0",
"critDamage": "60",
"initiative": "30",
"accuracy": "-10",
```

The following *keys* are optional for
`"attack"` or any healing based `"skillType":` skills.

  ---------------------------------------------------------------------------------------------------
  `"critDamage": "20",`                    Percent damage modifier for the critical damage dealt.
                                           Flatly additive/subtractive to any existing modifiers.

  `"initiative": "-30",`                   Flat initiative modifier for the skill's turn order.
                                           Flatly additive/subtractive to any existing modifiers.

  `"accuracy": "10",`                      Flat accuracy modifier for whether the skill successfully
                                           lands. Flatly additive/subtractive to any existing
                                           modifiers.

  `"scalesWithStatusEffect": "Drowsy",`    Scales the damage or healing if the given status effect is
                                           on the target. Stacks on potency, see
                                           Status Effects for potency
                                           reference.

  `"flatDamageSF-FlatScaling": "20",`      Flat base damage boost for each stack of
                                           `"scalesWithStatusEffect":`.

  `"flatDamageSF-PercentScaling": "10",`   Percent damage boost for each stack of
                                           `"scalesWithStatusEffect":`. Take caution with high percent
                                           values.

  `"TotalDamageSF-PercentScaling": "5",`   Boost to **total** skill damage for each stack of
                                           `"scalesWithStatusEffect":`. This means it bypasses defense
                                           reductions, and applies *after* other damage boosts. **Take
                                           extreme care.** If using this key, set the other SF damage
                                           scaling *key*
                                           *values* to `"0"`, or remove
                                           entirely.
  ---------------------------------------------------------------------------------------------------

Lastly, see `"statusOutcome":` in [Dialogue Keys](#dialogue-keys) below
for a note on combat event based skills.

## statusEffect Keys
``` json
"statusEffect": "Aphrodisiac",
"statusChance": "20",
"statusDuration": "3",
"statusPotency": "30",
"statusResistedBy": "Power",
"statusText": "Laced Magnum Rod",
"statusResistedBy": "Power",
```

The following *keys* are required for
`"statusEffect"` or `"Afflict"` `"skillType":` skills, optional for all
others depending on if they use the `"statusEffect"` key. See
Status Effect.

  -------------------------------------------------------------------------------------------
  `"statusEffect": "Power",`       What status effect it uses. Use `"EventRestrain"` for
                                   combat event based restrain application, ensuring combat
                                   event based restrain skills don't chain.

  `"statusChance": "25",`          Base percent chance of the effect successfully applying on
                                   the target.

  `"statusDuration": "5",`         How many turns the effect lasts.

  `"statusPotency": "30",`         Ranges from: Aphrodisiac flat arousal per turn (can stack),
                                   Restrain durability, Sleep flat energy drain per turn (can
                                   stack), how much of a given stat Buff/Debuff, or number of
                                   stacks for Paralysis or Trance.

  `"statusResistedBy": "",`        Which target stat resists the affect for avoiding
                                   application. Irrelevant to Buffs/Debuffs.

  `"statusText": "Oni's Gains",`   Will change status effect name in game. Making it unique
                                   for Buff/Debuff skills ensures they don't overlap with
                                   others in tracking.
  -------------------------------------------------------------------------------------------

The following *keys* are optional for all
possible `"skillType":` values.

  ------------------------------------------------------------------------------------------
  `"statusEffectScaling": "25"`   For stat buff/debuff skills, deciding their scaling based
                                  on the set `"statType":` *value* of the caster's stats. 100% of a given stat
                                  is equal to `stat * 1`, 50% `stat * 0.5`, etc. Can also be
                                  used for scaling healing `"skillType:"` skills with the
                                  skill's given `"statType":`.

  `"statusStacks": "1",`          Set to 1 to enable a buff/debuff effect to stack instead of only resetting 
                                  the duration when reapplied. 

  ------------------------------------------------------------------------------------------

## descrip
``` json
"descrip": "Cuddles the target till they don't feel like battlefucking anymore!",
```

The skill's tooltip description. Duration is automatically provided in
the tooltip, refer to existing skills in-game, and compare it to their
JSON's `"descrip":` key.

`"PlayWhilePlayerSleeping"` can be provided as a
*value* for Monster skills to trigger the
skills `"statusOutcome":` while the player is asleep. Useful for combat
events. Refer to Sofia's InciteDreams.json skill for reference.

## Dialogue Keys
The following *keys* are conditional
triggers based on the outcome of the skill, similar to
lineTriggers. This can use
[text markup](../../Reference/Markup.md), and
thus in extension, [functions](../../Functions/index.md) for starting combat events, using vfx/sfx, and so forth.

The following are required for `"attack"` or any healing based
`"skillType":` skills.

  ------------------ -----------------------------------------------------------
  `"outcome": "",`   Triggers on the skill successfully landing.

  `"miss": "",`      Triggers on the skill missing.
  ------------------ -----------------------------------------------------------

The following are required for `"statusEffect"` or `"Afflict"`
`skillType:` skills utilizing `"Restrain"` or `"EventRestrain"`.

  ----------------------------------- -----------------------------------------------------------
  `"restraintStruggle": "",`          Triggers displayable text when the target struggles.

  `"restraintStruggleCharmed": "",`   Triggers displayable text when the charmed target
                                      struggles.

  `"retraintEscaped": "",`            Triggers displayable text when the target breaks the
                                      restraints.

  `"retraintEscapedFail": "",`        Triggers displayable text when the target fails to break
                                      the restraints.
  ----------------------------------- -----------------------------------------------------------

The following are optional for `"statusEffect"` or `"Afflict"`
`skillType:` skills utilizing `"Restrain"` or `"EventRestrain"` status
effects:

  -------------------------- -----------------------------------------------------------
  `"restraintOnLoss": "",`   Triggers displayable text if the target loses while
                             restrained. Made for Pin, but could have other uses.

  -------------------------- -----------------------------------------------------------

The following *keys* are required for
`"statusEffect"` or `"Afflict"` based `skillType:` skills.

  ------------------------ -----------------------------------------------------------
  `"statusOutcome": "",`   Triggers displayable text upon the skill hitting its
                           target. Providing `"IgnoreAttack"` will allow for combat
                           event based `"attack"` or any healing `"skillType":` skills
                           to miss normally.

  `"statusMiss": ""`       Triggers displayable text upon the skill missing its
                           target. Can take functions for combat events and related.
  ------------------------ -----------------------------------------------------------
