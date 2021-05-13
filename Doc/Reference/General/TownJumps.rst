.. _Town Jumps:

.. _Town Jumps GameOver:

**Town Jumps & GameOver**
==========================

.. tip::

  See :ref:`End Combat` for ending a combat encounter. The below functions are typically for use at the end of an event, or loss/victory scene.


.. _CallLossLevelUp:

**CallLossLevelUp**
--------------------

``"CallLossLevelUp"`` calls the loss level up scene.
For niche use in loss scenes that don’t game over you. You’ll still need to have all endings to that event go to town though.

.. _GameOver:

**GameOver**
-------------

``"GameOver"`` returns the player to the church as if they lost combat. Advances time by 1.

**TrueGameOver**
-----------------

``"TrueGameOver"`` ends the game and returns to the main menu. For bad/good ends.

**GoToTown**
-------------

``"GoToTown"`` sends the player directly back to the town. Good for ending quests with different dialogue/returns. Advances time by 1.

**BumpToTown**
---------------

``"BumpToTown"`` sends the player to the town square without advancing time.

**GoToChurch**
---------------

``"GoToChurch"`` sends the player to the church. Good for alternate scenes for game over returns. Advances time by 1.

**GoToRandomBrothel Scene Functions**
--------------------------------------

Functions that send the player to a random brothel scene, each variant utilizing a different :ref:`CardType` for brothel shifts as its selection,
consisting of the following.

* ``"GoToRandomBrothelWaiterScene"``
* ``"GoToRandomBrothelBarScene"``
* ``"GoToRandomBrothelHoleScene"``
* ``"GoToRandomBrothelDayScene"``
