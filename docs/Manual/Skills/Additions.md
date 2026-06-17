# Skill Additions
Making a Skill addition is non-destructive and thus will be compatible
with any other mods making additions to the same Skill.

Check **\_SkillAdditionExample.json** for an example.

The overview will proceed to go over each *key* you would find in a regular Adventure .json, how their role
changes, and if they're required in a addition.

!!! note

    All other *keys* outside of the ones
    listed aren't used, and thus should not be included for tidiness,
    **excluding these five**:

``` json
"removesStance": "Provide/replace string found in base skill",
"restraintStruggle": "Provide/replace string found in base skill",
"restraintStruggleCharmed": "Provide/replace string found in base skill",
"restraintEscaped": "Provide/replace string found in base skill",
"restraintEscapedFail": "Provide/replace string found in base skill"
```
::::

## name
``` json
"name": "Holy Headpat",
```

Required so you can tell the game which Skill you wish to make an
addition to.

## skillType
``` json
"Addition": "Yes",
```

Required so you can tell the game that you're wishing to make an
addition. Can be added into almost any part of the file.

## fetishTags
``` json
"fetishTags": ["Pats"],
```

Optional, adds to the existing array. The *strings* provided in the original `"fetishTags":`
*key* will still be present, and not
overridden.

## startsStance
``` json
"startsStance": ["Cuddling"],
```

Optional, adds to the existing array. The *strings* provided in the original `"startsStance":`
*key* will still be present, and not
overridden.

Does not require the original file to have the *key* marked as an array.

## unusableIfStance
``` json
"unusableIfStance": ["Spoon-feeding"],
```

Optional, adds to the existing array. The *strings* provided in the original `"unusableIfStance":`
*key* will still be present, and not
overridden.

## requiresTargetStance
``` json
"requiresTargetStance": ["Handholding"],
```

Optional, adds to the existing array. The *strings* provided in the original `"requiresTargetStance":`
*key* will still be present, and not
overridden.

## unusableIfTarget
``` json
"unusableIfTarget": ["Oral"],
```

Optional, adds to the existing array. The *strings* provided in the original `"unusableIfTarget":`
*key* will still be present, and not
overridden.

## removeStance
``` json
"removesStance": ["Sex"]
```

Optional, adds to the existing array. The *strings* provided in the original `"removeStance":`
*key* will still be present, and not
overridden.

Does not require the original file to have the *key* marked as an array.

## stanceConditions
``` json
"stanceConditions": [
    {
        "theStance": "Leg Lock",
        "addingToSkills": {
            "unusableIfStance": ["Arousara"],
            "requiresStance": ["Arousero"],
            "unusableIfTarget": ["Arousara"],
            "requiresTargetStance": ["Calm Mind"]
        }
    },
    {
        "theStanceSet": ["Leg Lock", "Leg Lock"],
        "unusableIfTargetHasTheseSets": ["Caress"]
    }
]
```

Optional key structure that allows you to append to the
stance control keys of other skills in a
single location. While meant for modders, this can be done in any skill
json, not just additions. You can freely choose to use either or both
the original keys or `"stanceConditions":` to manage stances.
