# Church
Keep in mind that using Church functions will trigger fixed dialogue
from the Goddess, listed below.

-   "Oh chosen hero\... If you donate enough eros, I can remove the
    fetishes you have gained from your trials."
-   "You dump eros into the donation cup and they disappear
    instantly."
-   "A chill runs through your skull as your fantasies return to
    normal."
-   "Oh, chosen hero\... Your mind is as pure as it can be, but you may
    still donate if you wish."
-   "Oh, chosen hero\... It seems you don't have enough eros. I
    believe in you to get some so I may aid you."
-   "Oh chosen hero\... If you donate enough eros, I can remove the
    fetishes you have gained from your trials."
-   "Oh, chosen hero\... Your body is not in need of restoration, but
    you may still donate if you wish."

It's recommended to check
*/Json/Events/Town/Church/1VenereaeStatue.json* for a full context
example of how it works in practice.

## DonateToGoddess
`"DonateToGoddess"` lets the player provide an inputted amount to donate
to the goddess.

------------------------------------------------------------------------

## SensitivityRestore
`"SensitivityRestore"` lets the player use the sensitivity restore
functionality.

------------------------------------------------------------------------

## PurgeFetishes
`"PurgeFetishes"` lets the player use the fetish purging functionality.

------------------------------------------------------------------------

## AddTributeToProgress
`"AddTributeToProgress"` takes money spent in a church function and adds
it to the current events progress. Thus, it cannot be used for anything
but the church.

``` json
"AnyChurchFunctionHere",
"AddTributeToProgress"
```

See [Input](../EventOnly/Input.md) you're looking for similar,
general functionality. Though it's currently limited to debt or payment
systems related to eros.
