**SFX**
========

There are the following sound banks that can be provided instead of the specific file paths to an audio file:

QuickKiss – LongKiss – MakeOut

BlowjobLicking – BlowjobSucking – BlowjobDeepSuction - BlowjobVigorous

Ejaculation - EjaculationLong

.. note::
  
  Each of these functions count as an individual audio channel.
  If you call the same exact function again before the audio file has finished playing, it will prematurely stop it and play the newly provided audio file.

----

**PlaySoundEffect**
--------------------
Plays the selected audio file from the following string, or from one of the sound banks above.

.. code-block:: javascript

  "PlaySoundEffect", "sfx/Erotic/Hand/Handjob (only once).wav",
  "PlaySoundEffect", "LongKiss"

``"PlaySoundEffect2"`` exists, which allows you to play another audio file simultaneously regardless if the base function has finished or not.

----

**PlaySoundBankOnce**
----------------------
Using ``"PlaySoundBankOnce"`` plays through the entire selected sound bank one time, rather than a single file via `PlaySoundEffect`_.
Used for Sofia's singular kiss barrage.

.. code-block:: javascript

  "PlaySoundBankOnce", "BlowjobVigorous"

----

**PlayLoopingSoundEffect & StopSoundEffectLoop**
-------------------------------------------------
``"PlayLoopingSoundEffect"`` plays an audio file on loop, or a sound bank on loop.

.. code-block:: javascript

  "PlayLoopingSoundEffect", "sfx/Erotic/Hand/Handjob (low speed).wav",
  "PlayLoopingSoundEffect", "QuickKiss"


``"StopSoundEffectLoop`` Stops the looping sound, looping sounds are separate from one off sounds.

``"PlayLoopingSoundEffect2"`` and ``"StopSoundEffectLoop2"`` exists for a secondary loop channel.
