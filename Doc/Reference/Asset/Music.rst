**Music/BGM**
==============

**StopBGM**
------------

Using ``"StopBGM"`` stops any music that's currently playing with a 1 second fade out.

**StopBGMHard**
------------

Using ``"StopBGMHard"`` stops any music that's currently playing immediately. This also allows you to start up a song again properly if it's the same song, as it wont play if still fading out. 

**ChangeBGM**
--------------

Changes the music to the path provided in the next string.

::

  "ChangeBGM", "music/Battle/Shiva_Dance.mp3"

**ChangeBGM-List**
-------------------

Clears the current music and starts the given queue of music, playing in the order they're given. Close with ``"EndMusicList"``.

::

  "ChangeBGM-List",
  "music/Battle/Shiva_Dance.mp3", "music/Battle/Comet_Highway.mp3", "music/Battle/Goodbye.mp3",
  "EndLoop"

.. _ChangeBGM-OverrideCombatMusic:

**ChangeBGM-OverrideCombatMusic**
---------------------------------

``"ChangeBGM-OverrideCombatMusic"`` functions the same as ``"ChangeBGM"``, but overrides and ignores music from :ref:`SetMusicTo`.

Note events called within the encounter can still change the BGM via any of the functions on this page.

**ChangeBGM-NoFade**
---------------------

Using ``"ChangeBGM-NoFade"`` ensures the BGM doesn't fade in or out at the start or end of the song. Useful when the music needs seamless loops.

**PlayThisSongAfterCombat**
----------------------------

Using ``"PlayThisSongAfterCombat"`` will play the specified song after combat instead of reverting to the locations song.

.. _StoreCurrentBGM:

**StoreCurrentBGM & PlayStoredBGM**
------------------------------------

Using ``"StoreCurrentBGM"`` stores the currently playing BGM, while ``"PlayStoredBGM"`` changes the BGM to the song stored in the previous function.
Used when making dreams to ensure it can non-destructively change the BGM for the duration of the dream event.

::

  "StoreCurrentBGM",
  "...Some scenes later at the end of the dream/when the player wakes up..",
  "PlayStoredBGM"
