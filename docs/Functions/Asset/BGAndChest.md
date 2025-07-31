# BG & Chest

## ChangeBG

Changes the background. Requires path to image afterwards.

``` json
"ChangeBG", "forest.png"
```

Night equivalents are automatically used and found by the game searching
for the same file name, but with 'Night.png' appended at the end:
`"ExampleNameNight.png"`. **Note this does mean the game expects your
image to be a png.**

------------------------------------------------------------------------

## StoreCurrentBG & UseHeldBG

Using `"StoreCurrentBG"` stores the current BG on-screen, while
`"UseHeldBG"` changes the BG back to the stored BG in the previous
function. Used when making dreams to ensure it can non-destructively
change the BG for the duration of the dream event.

``` json
"StoreCurrentBG",
"... Some scenes later at the end of the dream/when the player wakes up...",
"UseHeldBG"
```

------------------------------------------------------------------------

## ShowTreasureChest & HideTreasureChest

Using `"ShowTreasureChest"` displays the wooden chest art. Used to fool
the player during the mimic encounter. Beyond using it for chest traps,
making custom treasure events based on your own conditions and rewards
would also be applicable.

`"HideTreasureChest"` **needs** to be called to remove the wooden chest
art, or else it will not go away.
