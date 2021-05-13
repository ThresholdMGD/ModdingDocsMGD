.. _Monster lineTriggers:

.. _lineTriggers:

**lineTriggers**
=================

See :ref:`combatDialogue` for general information on the keys used for lineTriggers.

Remember that the "move": key can be given an array, for any lineTrigger seen here. **However, it is so responses can be made compact**.
It does not at any point use the array as a multi-check requirement before it can trigger. That is, it is an *or* parameter, not an *and* parameter.
All matching lineTriggers matching the same ``"move":`` value will ultimately go into the same pool for it to randomly pull from.

For putting combat functions in strings, see :ref:`Dialogue Text Markup`

**Meta-Combat**
----------------

.. _SetMusicTo:

**SetMusicTo**
"""""""""""""""

::

  {
  "lineTrigger": "SetMusicTo",
  "move": [""],
  "theText":[
    "Path/To/Song/Here.mp3"
    ]
  },

Will change the current BGM at the start of combat.

Specify the song path in ``"theText":``. Paths start from */game/*. Additional strings will form a playlist, causing it to loop between each song, from top to bottom.

Other monsters at the start of the encounter will append to the playlist. Does not include monsters that are added to the encounter.

:ref:`ChangeBGM-OverrideCombatMusic` will override this lineTrigger.

**MonsterArrived**
"""""""""""""""""""

::

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

.. _StartOfCombat:

**StartOfCombat**
""""""""""""""""""

::

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

.. _EndOfRound:

**EndOfRound**
"""""""""""""""

::

  {
  "lineTrigger": "EndOfRound",
  "move": [""],
  "theText":[
    "Triggers at the end of every round of combat, before status effects tick down.",
    "A round would be whenever the player and all monsters present have each had at least one turn.",
    "Also must be called within the first 10 lineTriggers.",
    "Note that upon reaching the end of the round, it will trigger for each monster in the encounter."
    ]
  },

.. _StartOfRound:

**StartOfRound**
"""""""""""""""""

::

  {
  "lineTrigger": "StartOfRound",
  "move": [""],
  "theText":[
    "Triggers at the start of a round.",
    "That is, when the player and all monsters have not yet had their turn.",
    "Also must be called within the first 10 lineTriggers.",
    "Note that upon reaching the start of the round, it will trigger for each monster in the encounter."
    ]
  },

**Reactions**
--------------

These take place after an action or condition is performed or met by either the player or monster.

**HitWith & HitWithA**
"""""""""""""""""""""""

::

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

::

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

**UsesMove & UsesMoveA**
"""""""""""""""""""""""""

::

  {
  "lineTrigger": "UsesMove",
  "move": ["Tighten"],
  "theText":[
    "Triggers when the specified skill is used by the monster.",
    "It is displayed before the move.",
    "Biased towards Sex skills, but will use UsesMoveA pool as a fallback."
    ]
  },**

::

  {
  "lineTrigger": "UsesMoveA",
  "move": ["Tighten"],
  "theText":[
    "Triggers when the specified skill is used by the monster.",
    "It is displayed before the move.",
    "Biased towards Anal skills, but will use UsesMove pool as a fallback."
    ]
  },

**Escape**
"""""""""""

::

  {
  "lineTrigger": "Escape",
  "move": ["Distract"],
  "theText":[
    "Triggers when the player successfully uses an escape skill.",
    "Examples would be Teleport, or Distract.",
    "If "move": is given a blank string, it will apply to any instance of an escape skill."
    ]
  },

**LowHealth**
""""""""""""""

.. This might need a change to reset after orgasms? Verify if it isn't already the case.

::

  {
  "lineTrigger": "LowHealth",
  "move": [""],
  "theText":[
    "Triggers upon reaching less than 30% of their max health.",
    "Only happens once, heals will not reset it.",
    "The "move": key should be empty."
    ]
  },

**PlayerLowHealth**
""""""""""""""""""""

::

  {
  "lineTrigger": "PlayerLowHealth",
  "move": [""],
  "theText":[
    "Triggers upon the player reaching less than 35% of their max health.",
    "Only happens once, resetting on orgasms.",
    "The "move": key should be empty."
    ]
  },

**PlayerRecoil & PlayerRecoilA**
"""""""""""""""""""""""""""""""""

::

  {
  "lineTrigger": "PlayerRecoil",
  "move": ["Thrust"],
  "theText":[
    "Checks if the specified skill the player used had recoil, triggering after the attack. Triggers before HitWith/HitWithA.",
    "Biased towards Sex skills, but will use PlayerRecoilA pool as a fallback."
    ]
  },

::

  {
  "lineTrigger": "PlayerRecoilA",
  "move": ["Thrust"],
  "theText":[
    "Checks if the specified skill the player used had recoil, triggering after the attack. Triggers before HitWith/HitWithA.",
    "Biased towards Anal skills, but will use PlayerRecoil pool as a fallback."
    ]
  },

**OnSurrender**
""""""""""""""""

::

  {
  "lineTrigger": "OnSurrender",
  "move": [""],
  "theText":[
    "Triggers when the player surrenders.",
    "The "move": key should be empty."
    ]
  },

**onPlayerEdge**
"""""""""""""""""

::

  {
  "lineTrigger": "onPlayerEdge",
  "move": ["Thrust"],
  "theText":[
    "Displays when the player edges.",
    "The "move": key can optionally be given a specific skill to check for.",
    "It can also take stances, or be left blank to generally trigger."
  ]
  },

See the functions :ref:`DenyOrgasm` and :ref:`DenyPlayerOrgasm`.

**OnEdge**
"""""""""""

::

  {
  "lineTrigger": "OnEdge",
  "move": [""],
  "theText":[
    "Displays when the monster edges.",
    "The "move": key can optionally be given a specific skill to check for.",
    "It can also take stances, or be left blank to generally trigger."
  ]
  },

See the functions :ref:`DenyOrgasm` and :ref:`DenyMonsterOrgasm`.

.. _OnPlayerOrgasm:

**OnPlayerOrgasm**
"""""""""""""""""""

::

  {
  "lineTrigger": "OnPlayerOrgasm",
  "move": ["Deepthroat"],
  "theText":[
    "Displays when the player cums.",
    "The "move": key can optionally be given a specific skill to check for.",
    "It can also take stances, or be left blank to generally trigger.",
    "This trigger is only meant to call a combat event for technical reasons.",
    "This can be done via providing it with exclusively the following string...",
    "|f|CallCombatEventAndScene|/|EventNameHere|/|SceneNameHere|n||c|",
    "From there, you can have the scene you pointed it to use SwapLineIf to pick a random string.",
    "Also note you have the general flexibility of events available to you to use as you please.",
    "Lastly, OnPlayerOrgasm will not trigger OnPlayerOrgasm, only natural orgasms will do that."
    ]
  },

.. _OnOrgasm:

**OnOrgasm**
"""""""""""""

::

  {
  "lineTrigger": "OnOrgasm",
  "move": ["Thrust"],
  "theText":[
    "Displays when the monster cums.",
    "The "move": key can optionally be given a specific skill to check for.",
    "It can also take stances, or be left blank to generally trigger."
    ]
  },

The camelCase is known, and will be addressed at some point in the future during a breaking patch.

.. _PostOrgasm:

**PostOrgasm**
"""""""""""""""

::

  {
  "lineTrigger": "PostOrgasm",
  "move": [""],
  "theText":[
    "Displays after the monster orgasm line. This allows for some combat functions that may otherwise break up the orgasm line into janky parts.",
    "The "move": key can optionally be given a specific skill to check for.",
    "It can also take stances, or be left blank to generally trigger."
    ]
  },

.. _OnLoss:

**OnLoss**
"""""""""""

::

  {
  "lineTrigger": "OnLoss",
  "move": [""],
  "theText":[
    "Displays after the monster is defeated and taken out of the encounter. DOES NOT FUNCTION IN SINGLE MONSTER FIGHTS (game explodes otherwise). Intended for multi enemy fights, but this never triggers if it's the final monster in an encounter. This has many uses, but take care not to call a function that would specify the original monster specifically, or it will crash the game.",
    "The "move": key can optionally be given a specific skill to check for.",
    "It can also take stances, or be left blank to generally trigger."
    ]
  },

.. _Counters:

**Counters**
-------------

These work to counter their various of conditions before they take place.

The trigger order of priority for Counters matches the listed order, from top to bottom.

**AutoCounter**
""""""""""""""""

::

  {
  "lineTrigger": "AutoCounter",
  "move": ["Caress"],
  "theText":[
    "Triggers before the player uses the skill.",
    "Wait, Struggle, Run Away, Push Away, and Defend can also be used in "move":",
    "Note this can include skills used by items, or the item name itself."
    ]
  },

**AutoCounterSkillTag**
""""""""""""""""""""""""

::

  {
  "lineTrigger": "AutoCounterSkillTag",
  "move": ["Seduction"],
  "theText":[
    "Same as AutoCounter, but will instead check a skill's "skillTags": list."
    ]
  },

**AutoCounterSkillFetish**
"""""""""""""""""""""""""""

::

  {
  "lineTrigger": "AutoCounterSkillFetish",
  "move": ["Legs"],
  "theText":[
    "Same as AutoCounterSkillTag, but for the skill's "fetishTags": list."
    ]
  },

**OffenceCounter**
"""""""""""""""""""

::

  {
  "lineTrigger": "OffenceCounter",
  "move": [""],
  "theText":[
    "This will trigger before the player can use any form of offence. That is, anything that affects the monster.",
    "This won't trigger from the player using something on themselves, like healing or buffing.",
    "The "move": key should be left empty."
    ]
  },

**AnyCounter**
"""""""""""""""

::

  {
  "lineTrigger": "AnyCounter",
  "move": [""],
  "theText":[
    "Like OffenceCounter, but this will trigger prior to the player doing ANYTHING, including consumables, even if the monster is stunned.",
    "... ANYTHING, excludes Wait, Struggle, Run Away, Push Away, and Defend. Use AutoCounter to cover those.",
    "The "move": key should be left empty."
    ]
  },

.. _Stance Restraints:

**Stance, Restraints**
-----------------------

As the title suggests, contains lineTriggers specifically around stances and restraints.


**StanceStruggle**
"""""""""""""""""""

::

  {
  "lineTrigger": "StanceStruggle",
  "move": ["Making Out"],
  "theText":[
    "Triggers upon the player trying to escape a stance prior to whether or not it succeeds or fails.",
    "It is recommended to make a one for each possible stance the monster can be in.",
    "Remember that the player can only initiate Sex, Making Out, or Anal on their own."
    ]
  },

**StanceStruggleFail**
"""""""""""""""""""""""

::

  {
  "lineTrigger": "StanceStruggleFail",
  "move": ["Making Out"],
  "theText":[
    "Triggers upon the player failing to escape a stance."
    ]
  },

**StanceStruggleComment**
""""""""""""""""""""""""""

::

  {
  "lineTrigger": "StanceStruggleComment",
  "move": ["Making Out"],
  "theText":[
    "Like StanceStruggleFail, triggers after the player fails to escape a stance.",
    "Takes place after StanceStruggleFail, meant monster dialogue responses."
    ]
  },

**StanceStruggleFree**
"""""""""""""""""""""""

::

  {
  "lineTrigger": "StanceStruggleFree",
  "move": ["Making Out"],
  "theText":[
    "Triggers upon the player successfully escaping a stance."
  },

**StanceStruggleFreeComment**
""""""""""""""""""""""""""""""

::

  {
  "lineTrigger": "StanceStruggleFreeComment",
  "move": ["Making Out"],
  "theText":[
    "Like StanceStruggleComment, triggers after the player successfully escapes a stance.",
    "Takes place after StanceStruggleFree, meant for monster dialogue responses."
    ]
  },

**RestraintStruggle**
"""""""""""""""""""""

::

  {
  "lineTrigger": "RestraintStruggle",
  "move": ["Soft Amber Embrace"],
  "theText":[
    "Triggers upon the player trying to escape a restraint, whether or not it succeeds or fails.",
    "Specify the specific restraint in the "move": key."
    ]
  },

**RestraintStruggleCharmed**
"""""""""""""""""""""""""""""

::

  {
  "lineTrigger": "RestraintStruggleCharmed",
  "move": ["Soft Amber Embrace"],
  "theText":[
    "Like RestraintStruggle, but usurps it if the player is charmed."
    ]
  },

**RestraintEscaped**
"""""""""""""""""""""

::

  {
  "lineTrigger": "RestraintEscaped",
  "move": ["Soft Amber Embrace"],
  "theText":[
    "Triggers if the player successfully escapes the specified restraint."
    ]
  },

**RestraintEscapedFail**
"""""""""""""""""""""""""

::

  {
  "lineTrigger": "RestraintEscapedFail",
  "move": ["Soft Amber Embrace"],
  "theText":[
    "Triggers if the player fails to escape the specified restraint."
    ]
  },
