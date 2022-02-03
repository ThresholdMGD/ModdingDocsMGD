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

**I'm not jumping to the scene I set!**
----------------------------------------

You can check your event's scene jumping validity by turning on **LoadValidator**.
If you want to turn it on, you'll need to go to line 9 of *game/gamecode/LoadDatabase.rpy* and change the value from ``False`` to ``True``.
Then, on game start up, a .txt file will be printed out into the *game/* folder, titled ``validator_log.txt``.

**Manually progressing my saves to test stuff is painful!**
-------------------------------------------------------------

The in-game console can be very useful for debugging and testing your mod at a rapid pace, without having to manually build up a save towards what you want.
`See the game wiki for further information. <https://monstergirldreams.miraheze.org/wiki/Console>`_

**None of these answered my question!**
----------------------------------------

If you need help, please get on the `MGD Discord <https://discord.com/invite/monstergirldreams>`_.
There are tons of knowledgeable, depraved, and friendly people there willing to help you, no matter how big or small your problem is.
Head to the #modding-help channel towards the bottom of the channel list.
