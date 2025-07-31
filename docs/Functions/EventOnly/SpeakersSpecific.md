# Speakers Specific

!!! info "See also"

    This page contains functions in direct relation to the
    SpeakersCreation key. See the Events manual
    for more information on the *keys*
    themselves.

    Additionally, see
    [Dialogue](../../Functions/General/Dialogue.md) for functions independent of the
    SpeakersCreation key.


## DisplayCharacters

Shows each specified`"Speakers":` image/card from a
[Event](../../Manual/Events/Events.md).

``` json
"DisplayCharacters",
  "1",
  "2",
"EndLoop"
```

Instead of a number you can also use the nameID of that monster file to
specify who you want to display, but they still must be listed in the
`"Speakers":`.

------------------------------------------------------------------------

## Speaks

Puts the first character's name in the `"Speakers":`
*key* in the next box for the next
string. Supplying a number in the function will make it move to the next
character in `"Speakers:"`.

Adding a numerical *value* directly at
the end within the function will use the other speakers in the order
their *objects* are included. Up to 12.

``` json
"Speaks2",
  "Are those imps?",
"Speaks",
  "They're coming this way!",
"Speaks7",
  "Hello it's me, an imp."
```

`"Speaks"` is also capable of being used in
[lossScenes and victoryScenes](../../Manual/Monsters/Monsters.md#combat-scenes), which will
refer to the
[Monster Creation](../../Manual/Monsters/Monsters.md)'s `"name"` *key* within the
json.

``` json
"Speaks",
  "Wow I didn't know you could lift that many imps at once!",
"Speaks2",
  "I didn't either someone help me."
```

------------------------------------------------------------------------

## SetPostName

Sets the end of a monsters name to a thing, can be used to make attack
titles appear in events. Will affect all speakers, and persist for all
`"Speaks"` calls until it's manually set blank.

``` json
"SetPostName", " - Fancy Attack Name!"
```

After the attack is performed\...

``` json
"SetPostName", ""
```

------------------------------------------------------------------------

## SetFlexibleSpeaker & FlexibleSpeaks

Using `"SetFlexibleSpeaker"` sets a speaker to be used from the
`"Speakers":` *key* whenever
`"FlexibleSpeaks"` is called.

`"FlexibleSpeaks"` otherwise works just like the `"Speaks"` function.
Used for niche cases where you want to change the speaker, but not the
entire scene. See Manticore, Onis, or Shizu.

``` json
"SetFlexibleSpeaker", "2",
"FlexibleSpeaks",
  "It's me, speaker2!",
"SetFlexibleSpeaker", "3",
"FlexibleSpeaks",
  "Now it's me, speaker3!"
```
