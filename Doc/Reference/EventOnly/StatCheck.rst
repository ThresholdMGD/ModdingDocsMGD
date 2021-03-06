**Stat Checks**
================

**StatCheck**
--------------
Rolls a `d20 <https://en.wikipedia.org/wiki/D20_System>`_ with the specified player stat, against the given number. If the roll is higher than the given opposed check number, it jumps the given scene.
If it fails, it will go to the scene specified after ``"Fail"``. Note you can also check for ``"Temptation"``, as a specialized stat check
based on Willpower, Allure, and Intelligence. See :ref:`Stats`.

::

  "StatCheck", "Power", "15",
  "Pass Scene", "Fail", "Failed Scene"

.. tabs::

   .. tab:: Formula

      ::

        D20 + Stat*0.15 + LuckDie + Defend - 2

      Using Defend gives a bonus depending on how many times the player used it in a row:
      ``+5`` the first time, ``+3`` the second time, and ``+1`` the third and subsequent times.
      It is recovered for every turn gone without using Defend. ``LuckDie`` is a die roll with a floor minimum of ``+1`` to a ceiling of their Luck times ``0.1``.

   .. tab:: Temptation Formula

      **Note**: The combined values of Willpower, Allure, and Intelligence in the below formula has a combined ceiling cap of 15.

      ::

        D20 + Willpower*0.1 + Allure*0.1 + Intelligence*0.1 + LuckDie + Defend - 2

      Using Defend gives a bonus depending on how many times the player used it in a row:
      ``+5`` the first time, ``+3`` the second time, and ``+1`` the third and subsequent times.
      It is recovered for every turn gone without using Defend. ``LuckDie`` is a die roll with a floor minimum of ``+1`` to a ceiling of their Luck times ``0.1``.

   .. tab:: Surpass Failure Formula

      Players can surpass failure at the cost of their energy based on the following formula. It will always cost a minimum of 10 energy.
      Note that ``statToCheck`` is the player stat times ``0.15``, or for Temptation checks, Willpower, Allure, and Intelligence times ``0.1``.

      ::

        (opposedCheck / 5)*20 - (statToCheck*0.75)*5 - 10

For reference, here is how Threshold has benchmarked the mathematics of stat checks and their intended difficulty.
Note lower level players will fare worse, and higher level players will gradually fare better. See what numbers the base game uses for the stat checks
relative to the monster's level for reference.

* Very easy = 5
* Easy = 10
* Medium = 15
* Hard = 20
* Very hard = 25
* Nearly impossible = 30



**ChangeStatCheckDifficulty**
""""""""""""""""""""""""""""""
A sub-function that can be used before the check to alter the stat check's difficulty. Each entry of the sub-function is checked for, regardless if any previous
entries were found to be true or false.
The last given value in each instance of the sub-function is the stat check modifier, and can be a negative number to subtract instead.

::

  "StatCheck",
  "ChangeStatCheckDifficulty", "IfEncounterSizeGreaterOrEqualTo", "2", "5",
  "ChangeStatCheckDifficulty", "IfPlayerHasStatusEffect", "Charm", "10",
  "Technique", "10", "PassScene",
  "Fail", "FailScene"

The following sub-sub-functions can be checked for:

**IfPlayerHasStatusEffect**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  "ChangeStatCheckDifficulty", "IfPlayerHasStatusEffect", "Charm", "10"


**IfHasPerk**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  "ChangeStatCheckDifficulty", "IfHasPerk", "Swift", "-10"

**IfHasFetish**
~~~~~~~~~~~~~~~~

::

  "ChangeStatCheckDifficulty", "IfHasFetish", "Ass", "8"

**IfFetishLevelEqualOrGreater**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  "ChangeStatCheckDifficulty", "IfHasFetishEqualOrGreater", "Ass", "65", "9"

**IfVirilityEqualsOrGreater**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  "ChangeStatCheckDifficulty", "IfVirilityEqualOrGreater", "65", "9"

**IfEncounterSizeGreaterOrEqualTo & IfEncounterSizeLessOrEqualTo**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


::

  "ChangeStatCheckDifficulty", "IfEncounterSizeGreaterOrEqualTo", "5", "10",
  "ChangeStatCheckDifficulty", "IfEncounterSizeLessOrEqualTo", "3", "-5"

**IfProgressEqualsOrGreater & GetAnEventsProgressThenIfEqualsOrGreater**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  "ChangeStatCheckDifficulty", "IfProgressEqualsOrGreater", "15", "-8",
  "ChangeStatCheckDifficulty", "GetAnEventsProgressThenIfEqualsOrGreater", "40", "-20"

**IfChoice & GetEventAndIfChoice**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  "ChangeStatCheckDifficulty", "IfChoice", "1", "A Choice", "-100",
  "ChangeStatCheckDifficulty", "GetEventAndIfChoice", "2", "A Differnt Choice", "100"

**StatCheckRollUnder**
-----------------------
Functions the exact same as ``StatCheck`` but the player instead fails if the roll is higher than the opposed checked amount, and passes if it is lower.
Also informs the player that the goal of the check is to roll under for clarity. **Players cannot surpass failure, nor use ChangeStatCheckDifficulty.**

::

  "StatCheckRollUnder", "Technique", "15",
  "Pass Scene", "Fail", "Failed Scene"

**ChangeNextStatCheckDifficulty**
----------------------------------
For edge cases where it doesn't work as a sub-function to ``"StatCheck"``.
Alters the next stat check across any scene or event.
Can stack, and also lower the difficulty. Does not persist after a stat check is called. Displays no dialogue for the change.
Use in tandem with check functions such as :ref:`Player Checks` or :ref:`Monster Checks` to indirectly provide it with conditions depending on the resulting scene.

::

  "ChangeNextStatCheckDifficulty", "5"

**ResetStatCheckDifficultyModifer**
------------------------------------
``"ResetStatCheckDifficultyModifer"`` resets the modifier to 0. Useful when there’s still a way to avoid a stat check after calling a modifier.
