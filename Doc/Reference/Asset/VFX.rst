**VFX**
========
.. note::
  
  Each of these have what is called a channel, specific to the function itself.
  Each channel represents a layer on the screen, and will be overridden if it is called again, even if you intend to use it multiple times at once.
  You can avoid replacing a visual effect by mistake through the mentioned channels for each function, or by smartly mixing
  together the individual functions.

**PlayVisualEffect**
---------------------

::

  "PlayVisualEffect", "BlindingFlash", "pink.png"

``"PlayVisualEffect"`` plays a visual effect on channel 1. It will keep playing till ``"EndVisualEffect"`` is called.

``"PlayVisualEffect2"`` & ``"EndVisualEffect2"`` – channel 2

``"PlayVisualEffect3"`` & ``"EndVisualEffect3"`` – channel 3

**VFX Types**
""""""""""""""
To be placed after ``"PlayVisualEffect"`` so it knows how you want to manipulate the image provided in the next string.

* ``StartHaze`` start tier 1 haze effect, a low opacity screen cover.

* ``"GrowingHaze"`` tier 1 -> tier 2 haze.

* ``"IncreasingHaze"`` tier 2 -> tier 3 haze.

* ``"DecreasingHaze"`` tier 3 -> tier 2 haze.

* ``"FadingHaze"`` tier 2 -> tier 1 haze.

* ``"SuddenHaze"`` full, rapid tier 3 fade in.

* ``"BlackOut"`` blacks out the screen with the image. Stays dark till the channel is ended or changed.

* ``"ScreenPulse"`` pulses on the screen once at low opacity.

* ``"DoublePulse"`` pulses on the screen twice at low opacity.

* ``"TriplePulse"`` pulse on the screen thrice at low opacity.

* ``"RepeatingPulse"`` repeats low opacity pulse.

* ``"ScreenFlash"`` quick image flash. Note that using bright images might be unpleasant to the eye.

* ``"BlindingFlash"`` flash that lasts longer and fades slower. Still probably unpleasant to the eye.

* ``"OrgasmPulse"`` rapid pulse for orgasms. Eyes will definitely hurt with bright images, use with care.


**Channel-Independent VFX**
----------------------------
Pre-made and independent visual effect functions, with their own channel and images.

* ``"PlayKiss"`` plays the kiss effect.

* ``"PlayKissingBarrage"`` plays the kissing barrage effect, not stopping till ``"EndKissingBarrage"`` is called.

* ``"PlayKissingBarrageOnce"`` plays one full cycle of the kissing barrage.

* ``"PlayBlackOut"`` plays the screen black out effect, keeping the screen dark till ``"EndBlackOut"`` is called.

**PlayHypoSpiral**
-------------------

::

  "PlayHypnoSpiral", "5", "0.2", "Image.png", "1"

*Legend*:

::

  "PlayHypnoSpiral", "Speed, 1-100, default 5", "Opacity, 0.1-1", "Image.png", "In front of characters, 1/Behind, 0"

``"PlayHypnoSpiral"`` rotates an image by 360 degrees, meant for hypno spirals. End with ``"EndHypnoSpiral"``.

It has multiple parameters it uses to determine its effect, in a specific order, as shown in the above.

**PlayImagePulseLoopingList**
------------------------------

::

  "PlayImagePulseLoopingList", "1", "1", "0.9",

  "Image1.png",

  "Image2.png",

  "EndLoop"

*Legend*:

::

  "PlayImagePulseLoopingList", "PulseSpeed 0.2-2, default 1", "Zoom 0.2-2, default 1", "Opacity 0.1-1",

``"PlayImagePulseLoopingList"`` pulses an image on the screen based on the multiple parameters.
It will loop through any number of images provided after the parameters are set in the order shown above. Ends with ``"EndImagePulseLoopingList"``.

``"PlayImagePulseLoopingList"`` & ``"EndImagePulseLoopingList2"`` – channel 2

**PlayImagePulseLoopingRandom**
--------------------------------

::

  "PlayImagePulseLoopingRandom", "1", "1", "0.7",

  "Image1.png",

  "Image2.png",

  "EndLoop"

*Legend*:

::

  "PlayImagePulseLoopingRandom", "PulseSpeed, 0.2-2, default 1", "Zoom, 0.2-2, default 1", "Opacity, 0.1-1",

``"PlayImagePulseLoopingRandom"`` is the same as ``"PlayImagePulseLoopingList"``,
except it will select images in a random order. random plays randomly order. Ends with ``"EndImagePulseLoopingRandom"``.

**PlayCustomBarrage**
----------------------

::

  "PlayCustomBarrage", "1", "0.1",

  "Image1.png", "Image2.png", "Image3.png", "Image4.png",

  "EndLoop"

*Legend*:

::

  "PlayCustomBarrage", "PulseSpeed, 0.2-2, default 1", "Opacity, 0.1-1",


Display a barrage of images, values are for PulseSpeed and Opacity respectively. Ends with ``"EndCustomBarrage"``.

``"PlayCustomBarrage2"`` & ``"EndCustomBarrage2"`` - channel 2

**PlayMotionEffect**
---------------------

::

  "PlayMotionEffect", "Explosion"

``"PlayMotionEffect"`` will move the players view of the scene, using one of the selected motion effects below.
``"EndMotionEffect"`` can end the current motion effect if it’s taking too long.

Explosion - LongExplosion – Crash – SlowBounce – Bounce - Sway

**EndAllVisualEffects**
------------------------
``"EndAllVisualEffects"`` will stop all VFX currently playing, regardless of what it is.
