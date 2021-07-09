.. _Dialogue:

**Dialogue**
=============

.. tip::

  For :ref:`Speakers` specific functions, see the page :ref:`Speakers Specific`.

**PlayerSpeaks**
-----------------

Puts the player name in the text box header for the next string.

.. code-block:: javascript

  "PlayerSpeaks",
    "I don't get to talk very often."

**PlayerSpeaksSkill - Combat Only**
------------------------------------

Generally for use in combat events where the skill name is called still, and quotation marks are needed to be removed.

.. code-block:: javascript

  "PlayerSpeaksSkill",
    "I don't get to talk very often."

.. _Speak:

**Speak**
----------

Displays the given text in the text box header for the following string of text. Doesn't need to be in ``"Speaker":``, see :ref:`Speaks` for that.

.. code-block:: javascript

  "Speak", "Elena and Elly",
    "Paperwork sucks!"

**SaveNextLine, UseSavedLineInMenu, & DisplaySavedLine**
----------------------------------------------------------

Using ``"SaveNextLine"`` saves the next line that’s going to be displayed. Will then automatically be displayed during the next :ref:`Menu`.
This normally does happen already, but can be useful for more complex cases. See the logic for the Will-Power Temple's random encounters as an example.

``"DisplaySavedLine"`` will display the current saved line manually.
Was originally intended for the displaying with menus, but didn't work as intended. It was left it in just in case.

``"UseSavedLineInMenu"`` will display the saved line in a menu upon returning to it, where it'd otherwise not change or display anything at all.
See the logic for the Will-Power Temple's navigation as an example.
