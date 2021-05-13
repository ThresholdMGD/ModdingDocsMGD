.. _Change Stats:

**Change Stats**
=================

**Change Stat Functions**
--------------------------
Changes the players given stat by the given amount, permanently. Take caution using these. See :ref:`Eros` and :ref:`GiveExp` as well.

* ``"ChangeMaxArousal"``
* ``"ChangeMaxEnergy"``
* ``"ChangeMaxSpirit"``
* ``"ChangePower"``
* ``"ChangeWill"``
* ``"ChangeTech"``
* ``"ChangeAllure"``
* ``"ChangeLuck"``
* ``"ChangeInt"``

::

  "ChangeInt", "2"


**ChangeSensitivity**
----------------------
Changes the target sensitivity for the player by the given amount.

::

  "ChangeSensitivity", "Sex", "5"

See :ref:`Sensitivity`.

**PermanentlyChangeSensitivity**
---------------------------------
Same as above but will permanently affect the player. This prevents the church from recovering the player stats. Take caution.

See :ref:`Sensitivity`.

**PermanentChangeStatusEffectResistances**
-------------------------------------------
Permanently alters the players status effect resistance. It is recommended to use perks for less permanent afflictions.

::

  "PermanentChangeStatusEffectResistances", "Charm", "10"

See :ref:`Resistances`.

**ChangeFetish**
-----------------
Changes the target fetish for the player by the given amount. Often used in loss scenes.

::

  "ChangeFetish", "Kissing", "25"

See *Json/Fetishes/* for all current fetishes. This includes addictions.

At level 25, the player is considered to have the fetish. Maximum of level 100, minimum of 0, ignoring perks and items.

**PermanentlyChangeFetish**
----------------------------
Same as above but will permanently affect the player. This prevents the church from recovering the player stats. Take caution.

**SetFetish**
----------------------------
Same as above but sets the fetish/addiction to the number given. This change is permanent and prevents the church from recovering the player stats. Take caution. It's primary intent is for event based addictions and fetishes to be managed easier.

**RespecPlayer**
-----------------
Gives the player the ability to reinvest all of their stat points, perk points, and sensitivity points earned thus far.
