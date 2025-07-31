# Time
## PlayerStep
`"PlayerStep"` operates like the passage of time for turns in combat.

This triggers persistent status effects, covering `"Trance"`,
`"Hypnotized"`, `"Paralysis"`, and `"Aphrodisiac"`, letting their
duration and/or potency tick down.

------------------------------------------------------------------------

## AdvanceTime
Moves forward time. Note there are 6 chunks in a single day.

``` json
"AdvanceTime", "1"
```

`"DelayNotifications"` can optionally be used thereafter, delaying perk
decay notifications until the next time jump, so you don't interrupt a
scene.

------------------------------------------------------------------------

## RestPlayer
`"RestPlayer"` heals the player as if using a rest point and advances
time by 1 chunk.

`"DelayNotifications"` can optionally be used thereafter, delaying perk
decay notifications until the next time jump, so you don't interrupt a
scene.

------------------------------------------------------------------------

## SleepPlayer <a id="sleep-functions"></a>
`"SleepPlayer"` advances time until morning and fully heals the player.
Also will trigger a dream unless stated otherwise via
'DelayNotifications'.

`"DelayNotifications"` can optionally be used thereafter, delaying perk
decay notifications until the next time jump, so you don't interrupt a
scene.

------------------------------------------------------------------------

## IfDelayingNotifications
Lets you check if `"DelayNotifications"` was called letting you jump to
a different scene if true. **Only works in events.** This is so
`"TimePassed"` events can comply with the above functions, but still let
them have the opportunity to silently operate.

``` json
"IfDelayingNotifications", "SilentScenes"
```

------------------------------------------------------------------------

## TimeBecomesNight & TimeBecomesDay
`"TimeBecomesNight"` sets the time to false night, while
`"TimeBecomesDay"` sets it to false day respectively. The former will
clear false days and start false nights, the latter, vice versa.

False nights last until you return to town, use `"TimeBecomesNormal"`
below, or the next day starts. False days during the night ends in the
next time advancement or when returning to town.

------------------------------------------------------------------------

## TimeBecomesNormal
`"TimeBecomesNormal"` returns a false night or day back to its normal
variant. Does nothing if there is no false night or day.

------------------------------------------------------------------------

## IfTimeIs
Can check for the following: Day, Night, DayFaked, DayTrue, NightFaked,
NightTrue, Morning, Noon, Afternoon, Dusk, Evening, Midnight.

# Only works in events.
``` json
"IfTimeIs", "Night", "SceneNameHere"
```

------------------------------------------------------------------------

## HealingSickness
`"HealingSickness"` starts a global trigger for tracking if the player
healed with a refresh point. Lasts a whole day, or 6 chunks.

------------------------------------------------------------------------

## IfHealingSickness
Jumps to the given scene if healing sickness is active. Used to actually
avoid the refresh scenes for rest points. **Only works in events.**

``` json
"IfHealingSickness", "SceneNameHere"
```
