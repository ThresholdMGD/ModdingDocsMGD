---
search:
  exclude: true
---

# Welcome to the Monster Girl Dreams Modding Documentation for {{ config.extra.versionMGD }}

Create and modify game content the exact same way Threshold
makes game content. Complete coverage of all possible features and systems,
featuring a quick starter guide from the first minutes in making a basic mod,
all the way to publishing mods.

It is assumed readers are already experienced with the game and
understand its various stats by hovering over them in the in-game
character menu's 'Stats' tab.

Potential game spoilers ahead.

!!! warning
    Monster Girl Dreams is still in active alpha development. Mods you make aren't
    guaranteed to work with the latest version of the game.
    Your mods are entirely up to you to maintain, unless someone decides to
    patch your mod for you. Warning sounds scarier than it actually is.

## Is Modding Hard?

Most will find that the things they thought were going to be hard while modding,
were actually the easiest parts.
You will not read or touch a single line of actual code,
just using already predefined actions with basic checks.
This multiple choice scene for example,
is in a minimal format very close to writing in plain english what you want to happen.

``` json
"Speak", "Perpetua",
   "What will it be, [ThePlayerName]?"
"Menu",
  "'You will never defeat me!'",
  "'I just want to go home...'",
  "'Wanna hold hands?'",
"EndLoop"
```

As long as you are not actively avoiding testing in-game till the end of development,
your more likely problem will be writing the actual content players will read.
The challenge of the natural creative process has led to far more
struggling modders than any potential 'technical' or 'complicated'
problems while modding.

Beginning the tutorial in the Getting Started section should only take minutes
to get to visible results in-game you can toy with, even if you have never
modded any other game before.

## Navigating The Docs

All topics and pages in the documentation can be found using the navigation menu
to the left.

Use the 'Search' box in the top right to quickly find
specific information you're looking for. It will try to autocomplete your words.

Your browser supports searching for words on any page as well.
You can press `Ctrl + F` or `⌘ + F` to open it at any time.

See the overview below for a summary of the documentations layout.

## Getting Help

If you're having trouble, there are a couple of options:

* Try looking through the [FAQ](Reference/FAQ.md).
* Ask yourself once more what you need to know in its most specific fundamental
steps, then try navigating the navigation menu down to the most relevant topics.
For example,
> I need to learn how to add an item I made as a drop to a Blue Slime,
  which is a monster, so I should check for information on Monsters.
  I see there is a section for Monsters under the JSON Manual.
  It says to check out Monster Additions for adding to existing content.
  It shows how to get a blank template. It looks like
  I can add the item to the `itemDropList` object field and then test in-game,
  I will give it a guaranteed drop rate for now to make sure.
* If all else fails, you're encouraged to try getting help on the [MGD Discord](https://discord.com/invite/monstergirldreams).
There are knowledgeable, depraved, and friendly people who may be able to help you.
Head to the `#modding-help` forum channel towards the bottom of the channel list.

## Overview


<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Getting Started__

    ---

    If you are working on your first mod, starting here is highly recommended.

    - [Text Editors](GettingStarted/Editors.md)
    - [Making A Mod](GettingStarted/MakingAMod.md)
    - [Music And Art](GettingStarted/MusicAndArt.md)
    - [Meta Creation](GettingStarted/MetaCreation.md)
    - [Publishing Mods](GettingStarted/PublishingMods.md)

-   :material-script-text-play:{ .lg .middle } __Tutorials__

    ---

    Specialized tutorials on specific modding situations for
    novice to advanced modders.

    - [Tutorials Index](Tutorials/index.md)
    - [File Hosting Your Mod](Tutorials/FileHostingYourMod.md)
    - [Get Map Icon Position](Tutorials/GetImagePos.md)

-   :simple-json:{ .lg .middle } __JSON Manual__

    ---

    Comprehensive information on each type of JSON modders can use to add
    and modify game content.

    - [Adventures](Manual/Adventures/index.md)
    - [Events](Manual/Events/index.md)
    - [Fetishes](Manual/Fetishes/Fetishes.md)
    - [Items](Manual/Items/Items.md)
    - [Locations](Manual/Locations/index.md)
    - [Monsters](Manual/Monsters/index.md)
    - [Perks](Manual/Perks/index.md)
    - [Skills](Manual/Skills/index.md)

-   :material-notebook:{ .lg .middle } __Reference__

    ---

    General information you will consistently use while modding,
    from how to embolden text, available options for stats and stances,
    updating to incompatible mods to newer versions, and more.

    - [Markup](Reference/Markup.md)
    - [Stance Reference](Reference/StanceRef.md)
    - [Status Effect Reference](Reference/StatusEffectRef.md)
    - [Stat Reference](Reference/StatRef.md)
    - [FAQ](Reference/FAQ.md)
    - [Breaking](Reference/Breaking.md)
    - [Gridmap](Reference/Gridmap.md)

-   :material-dice-d20:{ .lg .middle } __Function Reference__

    ---

    Everything there is to know about functions, used for scripting
    your content with choices, progression, specialized combat behavior, and more.
    Modders refer to this section while writing content the most!

    - [Index](Functions/index.md)
    - [General](Functions/index.md#General)
    - [Asset](Functions/index.md#Asset)
    - [Event Only](Functions/index.md#Event-Only)
    - [Combat Only](Functions/index.md#Combat-Only)
</div>
