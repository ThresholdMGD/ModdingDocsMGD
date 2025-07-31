# Text Markup

This page will primarily cover text
[markup](https://en.wikipedia.org/wiki/Markup_language) features, but
there is some general information to know when writing. It's important
to keep in mind a rough 400-430 character limit when writing to avoid
text trailing off the screen. Thankfully, most text editors give you a
character count when highlighting a selection of text, usually at the
bottom of its GUI.

However, there is an emphasis on it being a rough character limit. Since
each text character in the game can have varying lengths, it's
generally impossible to tell if it will fit till you test it in-game.
This is one of the many reasons play-testing your work is recommended.

Lastly, if you know Ren'Py for featuring a certain markup feature and
can't find it on this page, it likely means it doesn't work as
expected.

## Dialogue Text Markup <a id="dialogue-text-markup"></a>

`[ThePlayerName]` gets and displays the player name.

``` json
"Oh hey [ThePlayerName]!"
```

`[THEPLAYERNAME]` gets the player name and displays it in ALL CAPS

`[TPN]` gets the initials of the player's name.

`[PlayerMoney]` displays the amount of money the player has.

`[PlayerLevel]` displays the player's current level.

`|n|` splits the string, causing everything after the `|n|`, to display
on the next screen of text. Useful for long attack descriptions or
player orgasm lines. Can be used multiple times in a string. Commonly
used with `|f|`. Refer to any near any monster's `combatDialogue":` as
an example.

``` json
"Oh, oh no..|n|..That's not good.",
```

`|f|` places a function in the string, which will be immediately called
upon displaying the text. Use \|/\| to make the equivalent of another
*string* for additional function
parameters. **End the last function parameter with** `|n|`. To use
another function, simply start using `|f|` again. After `|n|` is called,
you may now proceed with any text you may wish to display.

``` json
"|f|PlaySoundEffect|/|sfx/Magic/Hypnosis effect 3.wav|n||f|ChangeImageLayer|/|Expression|/|1|/|Base|n|Oh, hello [ThePlayerName]."
```

`|c|` exists specifically for technical use with
OnPlayerOrgasm, ensuring any text in a
*string* after it's called is removed.

`\n` causes a line break, i.e. hitting the enter *key* in a text editor. Used primarily for description and
encyclopedia entries in
[Monster Creation](../Manual/Monsters/Monsters.md). It can also be used as the equivalent of a blank
*string* for functions done via `|f|`

## Text Styling Markup <a id="text-styling"></a>

This section is a mix of [Ren'Py derivative
markup](https://www.renpy.org/doc/html/text.html) and custom MGD markup.
You can combine the markup as you please.

`{u}` underline the following text. Close with `{/u}`.

`{i}` italicize the following text. Close with `{/i}`.

`{b}` bold the following text. Close with `{/b}`.

`{s}` strike through the following text. Close with `{/s}`.

`{plain}` ensures the following text is not influenced by any styling or
colored markup. Close with `{/plain}`.

``` json
"Oh you are {i}so {b}cute{/b}, so not {plain}plain{/plain}, and oh-so{/i} smart!",
```

### Advanced Styling

`{size=int}` will make the following text size equal to the given
integer *value* after `=` in the markup.
Close with `{/size}`. You can also make it relatively bigger or smaller
compared to its previous state based on the given
*value* through the use of either `+int`
or `-int`.

You can layer them inside one another, but note `{/size}` will not end
all instances of `{size=int}`, only one instance at a time.

``` json
"Heather has {size=+10}big boobs, {size=-20}small wings{/size}, and a {size=69}huge crush{/size}{/size} on Perpetua.",
```

`{space=int}` will insert horizontal space into the line of text based
on the given integer value.

`{vspace=int}` functions the same as `{space=int}`, but instead for
vertical space.

`{w}` will delay the displayed text till user input is given to signal
it to continue. It can be given an integer *value* via `{w=int}` to make it wait the given integer number in
seconds, though it can continue early through user input before the
given time has elapsed.

``` json
"Waiting for user input,{w} continues after 5 seconds have passed{w=5}, or if user input is given prior.",
```

`{p}` functions the same as `{w}`, but inserts line breaks for every
time it's called.

`{cps=int}` overrides the game's default text speed when displaying
text, standing for *characters per second*. Useful given the game by
default has all text displayed instantly.

``` json
"{cps=34}A fairly fast text speed,{/cps} {cps=8}a fairly slow text speed.{/cps}"
```

`{nw}` placed anywhere in the *string*
causes the displayed text to automatically move to the next screen once
the final character has been displayed. Given MGD by default has all
text display instantly, this typically won't be too useful unless
combined with the `{cps}`.

`{fast}` placed anywhere in the *string*
causes the displayed text to instantly move towards the markup
declaration. Given MGD by default has all text display instantly, this
typically won't be too useful unless combined with the `{cps}`.

## Colored Text Markup

This section is a mix of [Ren'Py
markup](https://www.renpy.org/doc/html/text.html) and custom MGD markup.
You can combine it with text styling markup as you please.

`{Pink}` sets the color of the text to pink. Was specifically made for
the hearts. Closes with `{/Pink}`.

``` json
"Oh, I absolutely {Pink}LOVE THIS{/Pink}! {Pink}♥{/Pink}"
```

`{color=hex}` can be used for custom text color. Close with `{/color}`.
`hex` is where you provide a [hex color
code](https://www.color-hex.com/). Accepts #rgb, #rgba, #rrggbb, and
#rrggbbaa format.

`[StoredColor]` can be alternatively used, utilizing
*values* set from
SetStoredColor. They are by default
``#F6BADC``. Closes with `[ColorEnd]`.

``` json
"SetStoredColor", "1", "#fe0000", "5", "#c21196"
"[StoredColor]This is red,[StoredColor5] and this is purple.[ColorEnd], this is back to red[ColorEnd], and this is back to normal."
```

You can store up to 7 colors at a time using numerical variants:
`[StoredColor]`-`[StoredColor7]`. Accepts #rgb, #rgba, #rrggbb, or
#rrggbbaa format.

## Event Text Markup
`[DisplayPlayerChoice]` via the functions
ChoiceToDisplayFunc and
ChoiceToDisplayFromOtherEventFunc.

`[DisplayMonsterChoice]` via the functions
ChoiceToDisplayFunc and
ChoiceToDisplayFromOtherEventFunc.

`[ProgressDisplay]` via Progress
functions.

`[PlayerOrgasmLine]` or `[MonsterOrgasmLine]` displays the orgasm line
for the player or monster respectively. To be used with
onPlayerOrgasm and
OnOrgasm lineTriggers utilizing events
respectively. If using it in a loop, use the
EmptySpiritCounterFunc function in the
next line to reset how much spirit is counted.

## Damage Text Markup

`[DamageToPlayer]`, `[DamageToEnemy]`, and `[FinalDamage]` provide
damage *values* for relevant functions.

## Skill Text Markup

Intended for use in lines for
[Skill Creation](../Manual/Skills/Skills.md)

`[AttackerName]` or `[TargetName]` gets respective name of the attacker
or target.

`[AttackerYouOrMonsterName]` or `[TargetYouOrMonsterName]` will check if
it's the player or monster. If it's the former, it will say "you".
If it's the latter, the monster's name.

`[FocusedMonsterName]` gets the currently focused monster name,
primarily for use with the random monster focus function when needing to
use their name in a line.

# Pronouns

-   `[AttackerHeOrShe]` or `[TargetHeOrShe]`
-   `[AttackerHisOrHer]` or `[TargetHisOrHer]`
-   `[AttackerHimOrHer]` or `[TargetHimOrHer]`

`[SexAdjective]` gets an adjective from the below bank, Vaginal or Anal
based depending on stance. Note the space after each word. The empty
string means it can roll a blank.

-   **Sex**: ["", "wet ", "tight ", "wet ", "tight ",
    "receptive ", "warm "]
-   **Anal**: ["", "tight ", "tight ", "curved ", "rounded ",
    "receptive "]

`[SexWord]` gets a sex word from the bank, Vaginal or Anal based
depending on stance. It will pick a *string* randomly from an array, depending on either sex or anal
stance:

-   **Sex**: \["pussy", "pussy", "slit", "honeypot"\]
-   **Anal**: \["ass", "ass", "rear", "behind", "derriere"\]

If you want to use both, remember `[SexAdjective]` words have a space at
the end. Thus, you should leave no space between them, like so:

``` json
"[AttackerName] thrusts his mighty steed into [TargetName]'s [SexAdjective][SexWord]!"
```

## Item Markup <a id="item-markup"></a>

`[ItemEnergy]`, `[ItemArousal]`, and `[ItemSpirit]` displays the values
from an item's [flat stat keys](../Manual/Items/Items.md#flat-stat-keys) for use
in the item's `"descrip":` key.
## Technical Markup

`[PlayersInput]` will display either `Tap` if the user is on a device
with touch screen input, or `Click` if no touch input is found. You can
alternatively use `[playersinput]` to get it in lowercase. It is
intended for rare situations that explain the controls for a game
mechanic, such as in the Fishing
minigame.
