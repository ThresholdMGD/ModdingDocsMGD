# Inventory
## AllowInventory
`"AllowInventory"` lets the player access their inventory and use skills
out of combat. Intended for use with Adventures and Events.

Note: Remember to use `"DenyInventory"` to undo this, or else the player
may have access to their inventory in moments you didn't intend for
them to.

------------------------------------------------------------------------

## DenyInventory
`"DenyInventory"` prevents the player from accessing their inventory.

------------------------------------------------------------------------

## EquipPlayer

Equips the given item from the players inventory into the given slot.
Provide any value of `"1"`, `"2"`, or `"3"` for the according Rune slots, and `"Accessory"` is for the Accessory slot. 

The item type must match the slot. If the slot is occupied, the previously equipped item is returned to the inventory first. Does nothing if the player does not own the item.

``` json
"EquipPlayer", "Frog Rune", "1",
"EquipPlayer", "Hero's Cape", "Accessory"
```

!!! tip

    You can check player item
    ownership with
    [IfHasItem](../EventOnly/PlayerChecks.md#ifhasitem-ifdoesnthaveitem)
    prior to use.


------------------------------------------------------------------------

## UnequipPlayer

Unequips whatever is in the given slot, returning it to the players
inventory. Takes the same slot values as `"EquipPlayer"`.

``` json
"UnequipPlayer", "1",
"UnequipPlayer", "Accessory"
```
