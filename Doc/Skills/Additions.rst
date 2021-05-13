.. _Skill Additions:

**Skill Additions**
====================
Making a Skill addition is non-destructive and thus will be compatible with any other mods making additions to the same Skill.

Check **_SkillAdditionExample.json** for an example.

The overview will proceed to go over each key you would find in a regular Adventure .json, how their role changes, and if they're required in a addition.

.. note::
  All other keys outside of the ones listed aren't used, and thus should not be included for tidiness,
  **excluding these five**:

  ::

    "removesStance": "Provide/replace string found in base skill",
    "restraintStruggle": "Provide/replace string found in base skill",
    "restraintStruggleCharmed": "Provide/replace string found in base skill",
    "restraintEscaped": "Provide/replace string found in base skill",
    "restraintEscapedFail": "Provide/replace string found in base skill"

**name**
---------

::

  "name": "Holy Headpat",

Required so you can tell the game which Skill you wish to make an addition to.

**skillType**
--------------

::

  "Addition": "Yes",

Required so you can tell the game that you're wishing to make an addition. Can be added into almost any part of the file.

**fetishTags**
---------------

::

  "fetishTags": ["Pats"],

Optional, adds to the existing array. The strings provided in the original ``"fetishTags":`` key will still be present, and not overridden.

**startsStance**
-----------------

::

  "startsStance": ["Cuddling"],

Optional, adds to the existing array. The strings provided in the original ``"startsStance":`` key will still be present, and not overridden.

Does not require the original file to have the key marked as an array.

**unusableIfStance**
---------------------

::

  "unusableIfStance": ["Spoon-feeding"],

Optional, adds to the existing array. The strings provided in the original ``"unusableIfStance":`` key will still be present, and not overridden.

**requiresTargetStance**
-------------------------

::

  "requiresTargetStance": ["Handholding"],

Optional, adds to the existing array. The strings provided in the original ``"requiresTargetStance":`` key will still be present, and not overridden.

**unusableIfTarget**
---------------------

::

  "unusableIfTarget": ["Oral"],

Optional, adds to the existing array. The strings provided in the original ``"unusableIfTarget":`` key will still be present, and not overridden.

**removeStance**
-----------------

::

  "removesStance": ["Sex"]

Optional, adds to the existing array. The strings provided in the original ``"removeStance":`` key will still be present, and not overridden.

Does not require the original file to have the key marked as an array.
