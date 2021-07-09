.. _Text Markup:

.. _Markup:

.. _Text:

**Text Markup**
================

.. Note, anytime Markup is used in code blocks, it is best to use ".. code-block:: javascript" to ensure the syntax highlighting doesn't mess up.

This page will primarily cover text `markup <https://en.wikipedia.org/wiki/Markup_language>`_ features, but there is some general information to know when writing.
It is important to keep in mind a rough 430-450 character limit when writing to avoid text trailing off the screen.
Thankfully, most text editors gives you a character count when highlighting a selection of text, usually at the bottom of its GUI.

However, there is an emphasis on it being a rough character limit. Since each text character in the game can have varying length, it is generally impossible to tell if it will
actually fit till you test it in-game. This is one of the many reasons play-testing your work is recommended.

Lastly, if you know RenPy for featuring a certain markup feature and can't find it on this page, it likely means it doesn't work as expected.

.. _Dialogue Text Markup:

**Dialogue Text Markup**
-------------------------

``{ThePlayerName}`` gets and displays the player name.

.. code-block:: javascript

  "Oh hey {ThePlayerName}!"

``{THEPLAYERNAME}`` gets the player name and displays it in ALL CAPS

``{TPN}`` gets the initials of the player name.

``{PlayerMoney}`` displays the amount of money the player has.


``|n|`` splits the string, causing everything after the ``|n|``, to display on the next screen of text.
Useful for long attack descriptions or player orgasm lines. Can be used multiple times in a string. Commonly used with ``|f|``.
Refer to any near any monster's ``combatDialogue":`` as an example.

.. code-block:: javascript

  "Oh, oh no..|n|..That's not good.",

``|f|`` places a function in the string, which will be immediately called upon displaying the text. Use \|/\| to make the equivalent of another string for additional
function parameters. **End the last function parameter with** ``|n|``.  To use another function, simply start using ``|f|`` again.
After ``|n|`` is called, you may now proceed with any text you may wish to display.

.. code-block:: javascript

  "|f|PlaySoundEffect|/|sfx/Magic/Hypnosis effect 3.wav|n||f|ChangeImageLayer|/|Expression|/|1|/|Base|n|Oh, hello {ThePlayerName}."

``|c|`` exists specifically for technical use with :ref:`OnPlayerOrgasm`, ensuring any text in a string after it is called is removed.

``\n`` causes a line break, i.e. hitting the enter key in a text editor. Used primarily for description and encyclopedia entries in :ref:`Monster Creation`.
It can also be used as the equivalent of a blank string for functions done via ``|f|``

.. _Text Styling Markup:

**Text Styling Markup**
------------------------
This section a mix of `Renpy derivative markup <https://www.renpy.org/doc/html/text.html>`_ and custom MGD markup. You can combine the markup as you please.

.. Excluding markup containing any periods, since it generates an error at the moment.

``{u}`` underline the following text. Close with ``{/u}``.

``{i}`` italicize the following text. Close with ``{/i}``.

``{b}`` bold the following text. Close with ``{/b}``.

``{s}`` strike through the following text. Close with ``{/s}``.

``{plain}`` ensures the following text is not influenced by any styling or colored markup. Close with ``{/plain}``.

.. code-block:: javascript

  "Oh you are {i}so {b}cute{/b}, so not {plain}plain{/plain}, and oh-so{/i} smart!",

**Advanced Styling**
"""""""""""""""""""""
``{size=int}`` will make the following text size equal to the given integer value after ``=`` in the markup. Close with ``{/size}``.
You can also make it relatively bigger or smaller compared to its previous state based on the given value through the use of either ``+int`` or ``-int``.

You can layer them inside one another, but note ``{/size}`` will not end all instances of ``{size=int}``, only one instance at a time.

.. code-block:: javascript

  "Heather has {size=+10}big boobs, {size=-20}small wings{/size}, and a {size=69}huge crush{/size}{/size} on Perpetua.",

``{space=int}`` will insert horizontal space into the line of text based on the given integer value.

``{vspace=int}`` functions the same as ``{space=int}``, but instead for vertical space.

``{w}`` will delay the displayed text till user input is given to signal it to continue. It can be given an integer value via ``{w=int}`` to make it wait the
given integer number in seconds, though it can continue early through user input before the given time has elapsed.

.. code-block:: javascript

    "Waiting for user input,{w} continues after 5 seconds have passed{w=5}, or if user input is given prior.",

``{p}`` functions the same as ``{w}``, but inserts line breaks for every time it is called.

``{cps=int}`` overrides the games default text speed when displaying text, standing for *characters per second*.
Useful given the game by default has all text display instantly.

.. code-block:: javascript

    "{cps=34}A fairly fast text speed,{/cps} {cps=8}a fairly slow text speed.{/cps}"

``{nw}`` placed anywhere in the string causes the displayed text to automatically move to the next screen once the final character has been displayed.
Given MGD by default has all text display instantly, this typically won't be too useful unless combined with the ``{cps}``.

``{fast}`` placed anywhere in the string causes the displayed text to instantly move towards the markup declaration.
Given MGD by default has all text display instantly, this typically won't be too useful unless combined with the ``{cps}``.

.. _Colored Text Markup:

**Colored Text Markup**
------------------------
This section a mix of `Renpy derivative markup <https://www.renpy.org/doc/html/text.html>`_ and custom MGD markup.
You can combine it with text styling markup as you please.

``{Pink}`` sets the color of the text to pink. Was specifically made for the hearts.

``{ColorEnd}`` ends the current color setting.

.. code-block:: javascript

  "Oh, I absolutely {Pink}LOVE THIS{ColorEnd}! {Pink}♥{ColorEnd}"

``{SetTextColor}{Done}`` can be used for custom text color.
Simply specify a `hex color code <https://www.color-hex.com/>`_ between ``{SetTextColor}`` and ``{Done}``.
``{ColorEnd}`` closes ``{SetTextColor}`` as well.

.. code-block:: javascript

  "{SetTextColor}#fe0000{Done}This is red,{ColorEnd} and this is {SetTextColor}#c21196{Done}purple.{ColorEnd}"

``{UseSetColor}`` is stored universally up to seven times for every use of ``{SetTextColor}`` in a given string.

As an example, if you use ``{SetTextColor}`` four times in a string, it will map the fourth use of ``{SetTextColor}`` to ``{UseSetColor4}``. Till
another string uses ``{SetTextColor}`` four times, ``{UseSetColor4}`` will remain that color henceforth.

.. code-block:: javascript

  "{SetTextColor}#fe0000{Done}This is red{ColorEnd}, {SetTextColor}#fdfe02{Done}this is yellow{ColorEnd}, {SetTextColor}#c21196{Done}and this is purple{ColorEnd}.",
  "As a result, {UseSetColor3}this is purple{ColorEnd}, and {UseSetColor}this is red{ColorEnd}, but {SetTextColor}#0bff01{Done}now it is green{ColorEnd}.",
  "{UseSetColor}See?{ColorEnd} But {UseSetColor2}this is still yellow.{ColorEnd}"

``{color=hex}`` is a more simple alternative to ``{SetTextColor}``, simply changing the containing text to the given color.
Close with ``{/color}``. Overrides ``{SetTextColor}``. Accepts #rgb, #rgba, #rrggbb, or #rrggbbaa format.

``{outlinecolor=hex}`` changes the text color outline to the given color.  Close with ``{/outlinecolor}``. Overrides all of the above markup where relevant.
Accepts #rgb, #rgba, #rrggbb, or #rrggbbaa format.

.. _Event Text Markup:

**Event Text Markup**
----------------------

``{DisplayPlayerChoice}`` via the functions :ref:`ChoiceToDisplay` and :ref:`ChoiceToDisplayFromOtherEvent`.

``{DisplayMonsterChoice}`` via the functions :ref:`ChoiceToDisplay` and :ref:`ChoiceToDisplayFromOtherEvent`.

``{ProgressDisplay}`` via :ref:`Progress` functions.

``{PlayerOrgasmLine}`` or ``{MonsterOrgasmLine}`` displays the orgasm line for the player or monster respectively.
To be used with :ref:`onPlayerOrgasm` and :ref:`OnOrgasm` lineTriggers utilizing events respectively.
.. _Damage Text Markup:

**Damage Text Markup**
-----------------------

``{DamageToPlayer}``, ``{DamageToEnemy}``, and ``{FinalDamage}`` provide damage values for relevant functions.

.. _Skill Text Markup:

**Skill Text Markup**
----------------------

Intended for use in lines for skills jsons.

``{AttackerName}`` or ``{TargetName}`` gets respective name of the attacker or target.

``{AttackerYouOrMonsterName}`` or ``{TargetYouOrMonsterName}`` will check if it's the player or monster. If it's the former, it will say "you", the latter, the monster name.

**Pronouns**

* ``{AttackerHeOrShe}`` or ``{TargetHeOrShe}``

* ``{AttackerHisOrHer}`` or ``{TargetHisOrHer}``

* ``{AttackerHimOrHer}`` or ``{TargetHimOrHer}``

``{SexAdjective}`` gets an adjective from the below bank, Vaginal or Anal based depending on stance. Note the space after each word. The empty string
means it can roll a blank.

* **Sex**: ["", "wet ", "tight ", "wet ", "tight ", "receptive ", "warm "]

* **Anal**: ["", "tight ", "tight ", "curved ", "rounded ", "receptive "]

``{SexWords}`` gets a sex word from the bank, Vaginal or Anal based depending on stance. It will pick a string randomly from an array, depending on either sex or anal stance:

* **Sex**: ["pussy", "pussy", "slit", "honeypot"]

* **Anal**: ["ass", "ass", "rear", "behind", "derriere"]

If you want to use both, remember ``{SexAdjective}`` words have a space at the end. Thus, you should leave no space between them, like so:

.. code-block:: javascript

  "{AttackerName} thrusts his mighty steed into {TargetName}'s {SexAdjective}{SexWords}!"
