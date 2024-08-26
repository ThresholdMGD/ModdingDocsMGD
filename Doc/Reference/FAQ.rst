**FAQ**
========

**I got an error at startup!**
-------------------------------

Errors should tell you JSON formatting errors or incorrect file paths for media assets. If this pops up in the error:

.. code-block:: python

  ValueError: Expecting , delimiter: line ## column ## ext

You missed a comma at the line number in the stated .json file. From there, you can simply follow where it directs you.

The next likely error is that you have a trailing comma at the end of an array, string, or object, like so:

.. code-block:: javascript

  ["String A", "String B", "String B",]


This is more troublesome and will require manually locating.

*Unless* you have a :ref:`Linter` installed, which can warn you of JSON formatting errors and their locations while editing in real-time.

See :ref:`Music And Art Summary` for errors related to media asset paths.

**Loading my save isn't showing my changes?**
----------------------------------------------

You have to relaunch the game whenever you wish to fully see the changes you've made.
While nothing bad will happen, you cannot apply changes to your JSON files while the game is running.
If you changed a perk and your character currently possesses it in your save,
you will want to go to the options menu and update your save to apply the changes you made to the perk.

.. _notJumping:

**I'm not jumping to the scene I set!**
----------------------------------------

You can check your event's scene jumping validity by enabling the game's debug log.
If you want to turn it on, you can go to the in-game options menu and toggle **``'Debug Game Data On Startup'``**, 
or press the debug button on the game reload prompt via the in-game mod menu.

Then, on game startup or reload, the game will rewrite the files in the *game/debug* folder, where you can either view individual error types per file, or all error types in one file via *scene_validator.json*.

This will have a notable impact on game startup time. You can turn it off when you're done using it or rely just on manually reloading via the mod menu reload prompt each time you want to use it.

**Manually progressing my saves to test stuff is painful!**
-------------------------------------------------------------

The in-game console can be very useful for debugging and testing your mod at a rapid pace, without having to manually build up a save towards what you want.
`See the game wiki for further information. <https://monstergirldreams.miraheze.org/wiki/Console>`_

**None of these answered my question!**
----------------------------------------

If you need help, please get on the `MGD Discord <https://discord.com/invite/monstergirldreams>`_.
There are tons of knowledgeable, depraved, and friendly people there willing to help you, no matter how big or small your problem is.
Head to the #modding-help forum channel towards the bottom of the channel list.
