# VFX

!!! note

    Each of these have what is called a channel, specific to the function
    itself. Each channel represents a layer on the screen, and will be
    overridden if it's called again, even if you intend to use it multiple
    times at once. You can avoid replacing a visual effect by mistake
    through the mentioned channels for each function, or by smartly mixing
    together the individual functions.

## PlayVisualEffect

``` json
"PlayVisualEffect", "BlindingFlash", "pink.png"
```

`"PlayVisualEffect"` plays a visual effect on channel 1. It will keep
playing till `"EndVisualEffect"` is called.

`"PlayVisualEffect2"` & `"EndVisualEffect2"` -- channel 2

`"PlayVisualEffect3"` & `"EndVisualEffect3"` -- channel 3

### VFX Types

After declaring `"PlayVisualEffect"`, use any of the following types of
image manipulation sub-functions to create your VFX:

-   `StartHaze` start tier 1 haze effect, a low opacity screen cover.
-   `"GrowingHaze"` tier 1 -\> tier 2 haze.
-   `"IncreasingHaze"` tier 2 -\> tier 3 haze.
-   `"DecreasingHaze"` tier 3 -\> tier 2 haze.
-   `"FadingHaze"` tier 2 -\> tier 1 haze.
-   `"SuddenHaze"` full, rapid tier 3 fade in.
-   `"MajorHazeToBlackOut"` tier 3-\>BlackOut
-   `"BlackOut"` blacks out the screen with the image. Stays dark till
    the channel is ended or changed.
-   `"ScreenPulse"` pulses on the screen once at low opacity.
-   `"DoublePulse"` pulses on the screen twice at low opacity.
-   `"TriplePulse"` pulse on the screen thrice at low opacity.
-   `"RepeatingPulse"` repeats low opacity pulse.
-   `"Kiss"` like ScreenPulse, but holds the image onscreen for a brief
    moment.
-   `"ScreenFlash"` quick image flash. Note that using bright images
    might be unpleasant to the eye.
-   `"BlindingFlash"` flash that lasts longer and fades slower. Still
    probably unpleasant to the eye.
-   `"OrgasmPulse"` rapid pulse for orgasms. This will hurt the eyes
    when using bright images, use with care.

------------------------------------------------------------------------

## Channel-Independent VFX
Pre-made and independent visual effect functions, with their own channel
and images.

-   `"PlayKiss"` plays the kiss effect.
-   `"PlayKissingBarrage"` plays the kissing barrage effect, not
    stopping till `"EndKissingBarrage"` is called.
-   `"PlayKissingBarrageOnce"` plays one full cycle of the kissing
    barrage.
-   `"PlayBlackOut"` plays the screen black out effect, keeping the
    screen dark till `"EndBlackOut"` is called.

------------------------------------------------------------------------

## PlayHypnoSpiral

``` json
"PlayHypnoSpiral", "5", "0.2", "Image.png", "1"
```

*Legend*:

``` json
"PlayHypnoSpiral", "Speed, 1-100, default 5", "Opacity, 0.1-1", "Image.png", "In front of characters, 1/Behind, 0"
```

`"PlayHypnoSpiral"` rotates an image by 360 degrees, meant for hypno
spirals. End with `"EndHypnoSpiral"`.

It has multiple parameters it uses to determine its effect, in a
specific order, as shown in the above.

------------------------------------------------------------------------

## PlayPendulum

``` json
"PlayPendulum", "5", "60", "Image.png", "1"
```

*Legend*:

``` json
"PlayPendulum", "Speed, 0-Any, default 5", "Angle, 0-360, default 60", "Image.png",
```

`"PlayPendulum"` rotates an image 'back and forth' on screen like a
pendulum. End with `"EndPendulum"`.

The image used itself needs to be set up a specific way if you want it
to display properly, check 'pendulumTest.png' in the game files for an
example. -To be specific the image needs to be double the screen height,
and the rotation point needs to be centered on the image, as that's
there the rotation will occur on screen.

It has multiple parameters it uses to determine its effect, in a
specific order, as shown in the above.

------------------------------------------------------------------------

## PlayImagePulseLoopingList

``` json
"PlayImagePulseLoopingList", "1.0", "1", "0.9",

"Image1.png",

"Image2.png",

"EndLoop"
```

*Legend*:

``` json
"PlayImagePulseLoopingList", "PulseSpeed seconds, decimal required", "Zoom 0.2-2, default 1", "Opacity 0.1-1",
```

`"PlayImagePulseLoopingList"` pulses an image on the screen based on the
multiple parameters. It will loop through any number of images provided
after the parameters are set in the order shown above. Ends with
`"EndImagePulseLoopingList"`.

`"PlayImagePulseLoopingList"` & `"EndImagePulseLoopingList2"` -- channel
2

------------------------------------------------------------------------

## PlayImagePulseLoopingRandom

``` json
"PlayImagePulseLoopingRandom", "1", "1", "0.7",

"Image1.png",

"Image2.png",

"EndLoop"
```

*Legend*:

``` json
"PlayImagePulseLoopingRandom", "PulseSpeed, 0.2-2, default 1", "Zoom, 0.2-2, default 1", "Opacity, 0.1-1",
```

`"PlayImagePulseLoopingRandom"` is the same as
`"PlayImagePulseLoopingList"`, except it will select images in a random
order. random plays randomly order. Ends with
`"EndImagePulseLoopingRandom"`.

------------------------------------------------------------------------

## PlayCustomBarrage

``` json
"PlayCustomBarrage", "1", "0.1",

"Image1.png", "Image2.png", "Image3.png", "Image4.png",

"EndLoop"
```

*Legend*:

``` json
"PlayCustomBarrage", "PulseSpeed, 0.2-2, default 1", "Opacity, 0.1-1",
```

Display a barrage of images, *values* are
for PulseSpeed and Opacity respectively. Ends with `"EndCustomBarrage"`.

`"PlayCustomBarrage2"` & `"EndCustomBarrage2"` - channel 2

------------------------------------------------------------------------

## PlayMotionEffect

``` json
"PlayMotionEffect", "Explosion"
```

`"PlayMotionEffect"` will play a preset motion on screen (or moving the
screen), using one of the selected motion effects below.
`"EndMotionEffect"` can end the current motion effect if it's taking
too long on the next line, or to end a PlayMotionEffectLoop as mentioned
shortly below.

Motion Effects on Characters: Bounce, BounceSlow, BounceFast,
BounceOnce, Sway, SwaySlow, SwayFast, SwayOnce, Pump, PumpSlow,
PumpFast, Ride, RideSlow, RideFast, and Vibrate. Realign can also be
called to fix any transforms that can potentially jank out.

Motion Effects for entire Screen: ScreenBounce, SlowScreenBounce,
ScreenSway, Explosion, LongExplosion, Crash, CrashSmol, and Quake.

The screen motion effects will move everything, including the text box
and other UI elements. The other one only applies to onscreen
characters. To effect a single character or body part on a character or
CG, see [PlayMotionEffectCustom](#playmotioneffectcustom). Motion
effects for the entire screen have no custom variant.

------------------------------------------------------------------------

## PlayMotionEffectLoop

Works the same as PlayMotionEffect, but will maintain the effect even as
the scene moves to the next line, until EndMotionEffect is called.

------------------------------------------------------------------------

## PlayMotionEffectCustom

Plays a custom motion effect.

``` json
"PlayMotionEffectCustom", "Bounce", "Characters", "1.0", "15"
"PlayMotionEffectCustom", "Sway", "Character", "1", "2.0", "5"
"PlayMotionEffectCustom", "Ride", "Bodypart", "Aiko", "Expression", "0.5", "10"
```

*Legend*:

``` json
"PlayMotionEffectCustom", "EffectHere", "Characters", "speed, 1.0", "distance, 5"
"PlayMotionEffectCustom", "EffectHere", "Character", "Target", "speed, 1.0", "distance, 5"
"PlayMotionEffectCustom", "EffectHere", "Bodypart", "Target", "LayerTarget", "speed, 1.0", "distance, 5"
```

`"EffectHere:"` can take the following effect values: Bounce, Sway,
Pump, Ride, Vibrate.

  ---------------- -----------------------------------------------------------
  `"Characters"`   Hits everyone on screen.

  `"Character"`    Requires you to add a target by name or by display position
                   like an image change, e.g.: `"Aiko"` or `"1"`.

  `"Bodypart"`     Specify the target, then the layer you want to apply the
                   transform to, e.g.: `"Expression"`.
  ---------------- -----------------------------------------------------------

To end single-target custom effects such as `"Character"` and
`"Bodypart"`, you need to call a blank use of the function:

``` json
"PlayMotionEffectCustom", "", "Character", "Aiko", "0", "0"
"PlayMotionEffectCustom", "", "Bodypart", "Aiko", "Expression", "0", "0"
```

------------------------------------------------------------------------

## EndAllVisualEffects

`"EndAllVisualEffects"` will stop all active VFX. With an exclusion of
`"PlayMotionEffectCustom"` VFX, they need to be manually stopped.
