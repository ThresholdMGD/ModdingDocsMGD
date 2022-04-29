.. _Gridmap:

**Gridmap**
============

This page will give a comprehensive overview of the Gridmaps feature in Events.

You can find examples from the base game in *Json/Events/Labyrinth/* and check each floor file in their respective folder.

.. warning::

  Gridmaps is a new and developing feature 
  which could be prone to issues that could be in need of further revisions and clarifications in the future.

  Functionality may be considered limited till future updates.

.. seealso:: 

    For Gridmap functions meant to be defined outside the Gridmap in an event, see :ref:`Gridmap Functions`

**Creating a Gridmap**
-----------------------

A Gridmap doesn't require a specific CardType from an event, it only needs a scene to be placed in.

Everything that defines a Gridmap starts with the function ``"GoToMap"``, and ends upon calling ``"StartMap"``,
where the player is then placed in the defined Gridmap.

What you place between these two functions permantently defines how the scenes Gridmap will work, 
you cannot alter it thereafter without making an entire new Gridmap.

Assume all functions are required, unless stated otherwise.

This page will break down the following example:

.. code-block:: javascript

  "GoToMap",
    "Tileset",
      "0", "GridMap/floor.png", "Floor", "", "", "",
      "1", "GridMap/Wall.png", "Wall",  "", "", "",
      "E", "GridMap/LockedGate.png", "Interactable", "Labyrinth Floor 4", "Exit", "You stand before a large metal gate with multiple large locks...",
      "A", "GridMap/floorPoisoned.png", "Auto", "Labyrinth", "Poison", "The ground is laden in aphrodisiac.",
    "EndLoop",
    "YAdjust", "75",
    "PlayerCoord", "2", "4",
    "Sight", "4",
  "NPC",
    "Name", "Key",
    "Img", "GridMap/Key.png",
    "Event", "Auto", "Labyrinth", "Key",
    "Obstacle",
  "EndLoop",
  "NPC",
    "Name", "Ceris",
    "Img", "GridMap/CerisIcon.png",
    "Event", "Auto", "CerisGridAI", "Caught",
    "Movement", "Chase", "Player",
    "TurnEvent", "CerisGridAI", "Timer",
  "EndLoop",
  "NPC",
    "Name", "RecallPoint",
    "Img", "Invisible",
  "EndLoop",
  "NPC",
    "Name", "ShadowsTile",
    "Img", "GridMap/ShadowsTile.png",
    "Event", "Auto", "ShadowsTile", "ShadowsTile",
    "Obstacle",
  "EndLoop",


  "SpawnNPC", "Key", "5", "10",

  "Row", "1","1","1","1","1","1","1","1","1","1","1","1","1","1","1",   "EndLoop",
  "Row", "1","0","0","0","T","0","0","0","1","0","0","0","1","E","1",   "EndLoop",
  "Row", "1","0","1","0","1","1","1","0","1","0","1","0","1","0","1",   "EndLoop",
  "Row", "1","3","1","0","0","1","1","0","0","0","1","0","0","0","1",   "EndLoop",
  "Row", "1","0","1","1","0","0","0","1","1","0","1","1","1","1","1",   "EndLoop",
  "Row", "1","1","1","0","0","1","0","0","1","0","0","0","0","0","1",   "EndLoop",
  "Row", "1","0","0","0","1","0","1","1","1","1","1","1","0","1","1",   "EndLoop",
  "Row", "1","1","1","0","1","0","0","1","1","1","0","0","0","1","1",   "EndLoop",
  "Row", "1","0","0","0","1","0","1","1","0","0","0","1","0","0","1",   "EndLoop",
  "Row", "1","0","1","1","1","0","0","0","0","1","1","1","1","0","1",   "EndLoop",
  "Row", "1","0","1","0","0","0","1","1","1","1","0","0","0","0","1",   "EndLoop",
  "Row", "1","0","0","0","1","0","0","0","0","0","0","1","1","0","1",   "EndLoop",
  "Row", "1","1","1","1","1","1","1","1","1","1","1","1","1","1","1",   "EndLoop",

  "StartMap"

.. _GridmapCreationBreakdown:

**Gridmap Example Breakdown**
------------------------------

**GoToMap**
"""""""""""""
``"GoToMap'`` starts the creation of your Gridmap.

**StartMap**
""""""""""""""
``"StartMap"`` finalizes the setup and sends the player into the defined Gridmap. 

It must be called after everything else, nor should any of the other functions in this breakdown be used after it.

.. _Tileset:

**Tileset**
"""""""""""""

.. code-block:: javascript

    "Tileset",
      "0", "GridMap/floor.png", "Floor", "", "", "",
      "3", "GridMap/darkfloor.png", "Floor", "", "", "",
      "1", "GridMap/Wall.png", "Wall",  "", "", "",
      "E", "GridMap/LockedGate.png", "Interactable", "Labyrinth Floor 4", "Exit", "You stand before a large metal gate with multiple large locks...",
      "T", "GridMap/floorPoisoned.png", "Auto", "Labyrinth", "Poison", "The ground is laden in aphrodisiac.",
    "EndLoop",

The ``"Tileset"`` function loop defines the tiles that will visually make up your Gridmap.

Each tile is defined on a 6-string interval. Even if a string value goes unused, an empty string will still count towards the tile.

The disambiguation will use the following tile example:

.. code-block:: javascript

  ``"T", "GridMap/floorPoisoned.png", "Auto", "Labyrinth", "Poison", "The ground is laden in aphrodisiac.",``

**First String Value**:
~~~~~~~~~~~~~~~~~~~~~~~~

The tile ID used to tell the game which tile to place, in this case ``"T"`` to denote a poisoned tile.

It's encouraged to make this a single character, 
as the similar width will make the later placement of these tiles easier to visually follow. 

.. tip:: 
  
  Also see setting a monospace font in your respective text editors settings to make all characters the same width.

**Second String Value**:
~~~~~~~~~~~~~~~~~~~~~~~~~

The image path used for your tile. 

The pixel width and length used by MGD is 50x50 tiles. Any other size, such as 64x64 tilesets, will not work as expected.

**Third-Sixth String Values**:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The third string value defines the type of tile, defining how it behaves.

.. list-table::
  :widths: 1 5

  * - ``"Floor"``
    - A simple tile the player and an NPC could traverse.
  * - ``"Wall"``
    - Blocks players and NPCs from moving into it, such as for walls, pits, etc.
  * - ``"Interactable"``
    - Calls an Event when the player is standing on it and hits the interact button. Players and NPCs traverse them like a Floor.
  * - ``"Auto"``
    - Calls an Event after the player steps on it no matter what. NPCs traverse them like a Floor.

The fourth and fifth string value is for Interactables and Auto tiles to define the name of the Event and then Scene to call. Floors and Walls leave it blank.

In this case, the tile type is ``"Auto"``, and calls the event ``"Labyrinth"``, and goes to the scene ``"Poison"``.

The sixth string value is for optionally displaying flavor text when the tile is stepped by the player.
Walls can't make use of it, given players cannot step in Walls.

In this case, ``"The ground is laden in aphrodisiac.",`` will play after the Auto tile event is done being called.

**YAdjust**
"""""""""""""
``"YAdjust"`` alters the position of the Gridmap on the screen via the following string value.
The value necessary  will vary depending on the amount of Rows your Gridmap has.

You'll likely need to adjust this manually from reviewing the Gridmap in-game till the positioning is considered correct.

.. tip::

  Ensuring your event can be readily accessed in-game by temporarily defining it as a town CardType is useful during early iterations.

**PlayerCoord**
""""""""""""""""
``"PlayerCoord"`` sets the players starting coordinates on the Gridmap in the following two string values.

The first given string value represents the X position, increasing in numerical value from left to right.
The second string value represents the Y position, increasing in numerical value from top to bottom.

Note how in the above example Gridmap, the player spawns on the Floor tile of ID ``"3"``, with the given player coordinates of ``"2", "4"``.

**Avoid placing the player inside a wall**, it's currently unknown what this will cause.

.. _Grid Sight:

**Sight**
""""""""""
Declaring ``"Sight"`` enables the fog of war, only letting player see as far as the following string value. 
Each numerical value increases the players sight radius in a 50px interval. Vision is blocked by Wall tiles.

It's optional and can thus be excluded if you want to disable fog of war and let the player see the entire Gridmap, including through walls.

.. tip::

  If you just want to limit player vision through walls, you can set the sight to the maximum possible length of a column or row on the map.

.. _Gridmap NPC:

**NPC**
"""""""""

.. code-block:: javascript

  "NPC",
    "Name", "Key",
    "Img", "GridMap/Key.png",
    "Event", "Auto", "Labyrinth", "Key",
    "Obstacle",
  "EndLoop",
  "NPC",
    "Name", "Ceris",
    "Img", "GridMap/CerisIcon.png",
    "Event", "Auto", "CerisGridAI", "Caught",
    "Movement", "Chase", "Player",
    "TurnEvent", "CerisGridAI", "Timer",
  "EndLoop",
  "NPC",
    "Name", "RecallPoint",
    "Img", "Invisible",
  "EndLoop",
  "NPC",
    "Name", "ShadowsTile",
    "Img", "GridMap/ShadowsTile.png",
    "Event", "Auto", "ShadowsTile", "ShadowsTile",
    "Obstacle",
  "EndLoop",

Each use of the ``"NPC"`` function will define a NPC. 
Not only for monsters, can also be an object, like a key, or to define a RecallPoint.

The following table breaks down all following sub-functions you can provide it before closing the loop:

.. list-table::
  :widths: 1 5

  * - ``"Name"``
    - Name of your NPC, for what other Gridmap functions will call the NPC by.
  * - ``"Img"``
    - Image to display on map in the following string value, which is either the file path, or ``"Invisible"`` to not use any image.
  * - ``"Event"``
    - Upon player collision with the NPC, calls an event, featuring the same possible paramaters as :ref:`Tileset`.
  * - ``"Movement"``
    - Movement type the NPC will use to navigate the Gridmap. See :ref:`ChangeGridNPCMovement` for possible parameters.
  * - ``"TurnEvent"``
    -  Calls the given event then given scene every Gridmap turn, aka every step. See base game examples and :ref:`Gridmap Functions`.
  * - ``"Obstacle"``
    - Skips the NPC in movement calls, and sets it to be displayed under all other NPCs.

**SpawnNPC**
"""""""""""""
.. code-block:: javascript

  "SpawnNPC", "Key", "5", "10",

``"SpawnNPC"`` spawns the given NPC at the coordinates provided in the following two string values. 

The NPC must be defined in the Gridmap when it's created to avoid issues.

The first given string value represents the X position, increasing in numerical value from left to right.
The second string value represents the Y position, increasing in numerical value from top to bottom.

**Rows**
"""""""""

.. code-block:: javascript

  "Row", "1","1","1","1","1","1","1","1","1","1","1","1","1","1","1",   "EndLoop",
  "Row", "1","0","0","0","T","0","0","0","1","0","0","0","1","E","1",   "EndLoop",
  "Row", "1","0","1","0","1","1","1","0","1","0","1","0","1","0","1",   "EndLoop",
  "Row", "1","3","1","0","0","1","1","0","0","0","1","0","0","0","1",   "EndLoop",
  "Row", "1","0","1","1","0","0","0","1","1","0","1","1","1","1","1",   "EndLoop",
  "Row", "1","1","1","0","0","1","0","0","1","0","0","0","0","0","1",   "EndLoop",
  "Row", "1","0","0","0","1","0","1","1","1","1","1","1","0","1","1",   "EndLoop",
  "Row", "1","1","1","0","1","0","0","1","1","1","0","0","0","1","1",   "EndLoop",
  "Row", "1","0","0","0","1","0","1","1","0","0","0","1","0","0","1",   "EndLoop",
  "Row", "1","0","1","1","1","0","0","0","0","1","1","1","1","0","1",   "EndLoop",
  "Row", "1","0","1","0","0","0","1","1","1","1","0","0","0","0","1",   "EndLoop",
  "Row", "1","0","0","0","1","0","0","0","0","0","0","1","1","0","1",   "EndLoop",
  "Row", "1","1","1","1","1","1","1","1","1","1","1","1","1","1","1",   "EndLoop",


Each ``"Row"`` function loops through the defined the Gridmap layout, and is repeated till done. 
Values will use the defined :ref:`Tileset` tiles.

Each Row must have the same legth, or errors may occur. In other words, make sure no row is too longer or shorter than another. 

It's recommended to take screenshots of your map as you make it for references and positioning of NPCs/tiles.

.. tip:: 
  You can select each row by click and dragging your mouse across it to get a selected character count in the bottom right as a way to test this.
  
  Also see using a monospace font in your text editors settings to make all text characters the same width.