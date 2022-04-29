.. _Gridmap:

**Gridmap Stuff**
==============

Welcome to the Gridmap section of the modding guide!

It's a new and fun feature that is probably a little volatile and could be very frustrating and explodey for new users!

Cause it's kinda janky to use!

I'm also sure this guide on it will likely need some revisions and clarifications later on, so please bear that in mind if you decide to use the gridmap system.

There is also likely functionality you might want that doesn't exist yet!

The labyrinth files are your best bet to find full examples of it in action.

**Gridmap Creation**
------------

Okay so there's kind of a lot here, so I'll start by dropping a full gridmap example down, then breaking down whateverything means. Try not to have your brain melt! :D

.. code-block:: javascript

  "GoToMap",
    "Tileset",
      "0", "GridMap/floor.png", "Floor", "", "", "",
      "1", "GridMap/Wall.png", "Wall",  "", "", "",
      "E", "GridMap/LockedGate.png", "Interactable", "Labyrinth Floor 4", "Exit", "You stand before a large metal gate with multiple large locks...",
      "P", "GridMap/floorPoisoned.png", "Auto", "Labyrinth", "Posion", "The ground is laden in aphrodisiac.",
    "EndLoop",
    "YAdjust", "75",
    "PlayerCoord", "1", "6",
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
  "Row", "1","0","0","0","0","0","0","0","1","0","0","0","1","E","1",   "EndLoop",
  "Row", "1","0","1","0","1","1","1","0","1","0","1","0","1","0","1",   "EndLoop",
  "Row", "1","0","1","0","0","1","1","0","0","0","1","0","0","0","1",   "EndLoop",
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

So you still with me? Any of that make sense? No? Yes? Well hopefully I can explain all of that numbers and text!

.. _GridMapCreationBreakdown:

**GoToMap**
----------------------------------------
Call this one to start making your gridmap!

**StartMap**
----------------------------------------
This bit at the end will end the set up and send the player to the grid map! It must be called after everything else.

**Tileset**
----------------------------------------
this starts setting up your image tileset for the map! This is mandatory.

the fist box is the tiles ID, pick something singular, as it will make mapping way more sane.

the second is the image path for you tile, mgd uses 50x50 tiles.


the third is the type of tile it is

-"Floor" means it is just a simple tiles

-"Wall" means the players and npcs cant move into it.

-"Interactable" means it something that activates when the player is standing on it and hits the interact button.

-"Auto" means the event given triggers after the player steps on it no matter what!


the 4th and 5th are for the event .json title, and scene for an interactable or auto event

the last one is for flavour text! Which displays when the tile is stepped on by the player.

.. code-block:: javascript

  "Tileset",
    "0", "GridMap/floor.png", "Floor", "", "", "",
    "1", "GridMap/Wall.png", "Wall",  "", "", "",
    "E", "GridMap/LockedGate.png", "Interactable", "Labyrinth Floor 4", "Exit", "You stand before a large metal gate with multiple large locks...",
    "P", "GridMap/floorPoisoned.png", "Auto", "Labyrinth", "Posion", "The ground is laden in aphrodisiac.",
  "EndLoop",

**YAdjust**
----------------------------------------
This will adjust the position of the grid map on the screen, you likely need to do this depending on how large your gridmap is.

You'll likely need to just mess with it until it works if the map isn't where you want it.

**PlayerCoord**
----------------------------------------
The players starting coordinates. Mandatory.

dont stick them in a wall, I dont know what happens.

**Sight**
----------------------------------------
Toggles the sight on, not mandatory, so don't bother calling it unless you want sight toggled on from the start.

**NPC**
----------------------------------------
Okay this ones a doozey!

.. code-block:: javascript

  "NPC",
    "Name", "Key",
    "Img", "GridMap/Key.png",
    "Event", "Auto", "Labyrinth", "Key",
    "Movement", "Chase", "Player",
    "TurnEvent", "CerisGridAI", "Timer",
    "Obstacle",
  "EndLoop",

Give your NPC a name, thats what functions will call it by!

Img, is the image to display on map. You can also say Invisible to make it not have any image,

"Event", "Auto" means it will automatically trigger the given event when the player touches the NPC

"Movement", means you give it a movement type of some kind (Check ChangeGridNPCMovement for more details on that.)

"TurnEvent", means it will call the given function every grid map turn, aka every step.

"Obstacle" means it's skipped over in movement calls, and is also displayed under all other npcs.

**SpawnNPC**
----------------------------------------
Spawn one of the npcs you made on the grid map! The gridmap npc must be in the map file when it's created or it'l get mad at you.

You must give specific coordinates. Yes this is a pain in the ass.

.. code-block:: javascript

  "SpawnNPC", "Key", "5", "10",

**Rows**
----------------------------------------
The rows on the map go round and round!

These are what make up the map iteself, and its built with your tileset made earlier, aka the tile IDs, which is why i reccomend making it single letter/numbers, so it makes a nice even mappy

The resulting rows and columns must match up, or it will probably explode, aka one row cant be shorter than the others. Just fill the extra space with empty tiles or something.

Also yes you have to do this by hand! Maybe someday some mad lad will make something to make this whole grid creation easier, but until that day this will be very monotonous!

I reccomend taking screenshots of your map as you make it for references and positioning of npcs/tiles.

.. code-block:: javascript

  "Row", "1","1","1","1","1",   "EndLoop",
  "Row", "1","0","0","0","1",   "EndLoop",
  "Row", "1","1","1","1","1",   "EndLoop",

==============

.. _GridmapEventFunctions:

**Gridmap Event Functions**
==============

.. _ExitGridmap:

**ExitGridmap**
----------------------------------------
Leaves the active gridmap the player is in!

This MUST be called to properly exist a gridmap, ensure exits to it are avalible somehow!!!

.. _StunGridPlayer:

**StunGridPlayer**
----------------------------------------
Stuns the players map movement for X turns. Good for traps!

.. code-block:: javascript

  "StunGridPlayer", "1"

  .. _StunGridPlayer:

.. _IfGridPlayerStunned:

**IfGridPlayerStunned**
----------------------------------------
If the player is stunned by the above stunning function for grid movement, do an event jump! Otherwise continue onwards.

.. code-block:: javascript

  "IfGridPlayerStunned", "SceneToJumpTo"

.. _RemoveGridNPC:

**RemoveGridNPC**
----------------------------------------
Removes a grid npc from the map, comes in 'Current' and 'Specific' flavours! Current meaning the focused event npc that's called for the player interaction.

.. code-block:: javascript

  "RemoveGridNPC", "Current"
  "RemoveGridNPC", "Specific", "NPCName"

.. _SetPlayerGridPosition:

**SetPlayerGridPosition**
----------------------------------------
Move the player to another location on the grid coordinates!

.. code-block:: javascript

  "SetPlayerGridPosition", "0", "0"

.. _ChangeGridNPCMovement:

**ChangeGridNPCMovement**
----------------------------------------
Changes the focused event NPCs movement type if applicable!

Takes a target the player, NPC, or coords, and acts accordingly.


"" - None! They stand still.

Chase - Directly chases the target! Uses Astar pathfinding.

Ambush - tries to move to a square 4 spaces infront of the target.

Whimsical - Picks a square within the given range of the target, and moves to that location. If called again while active it finds a new square to target.

Wander - wanders randomly in any direction, can hit walls.

.. code-block:: javascript

  "ChangeGridNPCMovement", "", ""
  "ChangeGridNPCMovement", "Chase", "Player"
  "ChangeGridNPCMovement", "Chase", "Coord", "6", "9"
  "ChangeGridNPCMovement", "Ambush", "Player"
  "ChangeGridNPCMovement", "Whimsical", "Player", "5"
  "ChangeGridNPCMovement", "Wander"

.. _IfGridNPCSeesPlayer:

**IfGridNPCSeesPlayer**
----------------------------------------
If the focused NPC sees the player with the given paramaters, do a scene jump, else continue onwards.

Has option of IgnoreWalls, and can have a range to represent the sight, otherwise it makes a direct line to the player unless it hits a wall.

.. code-block:: javascript

  "IfGridNPCSeesPlayer", "EnsuredChase",
  "IfGridNPCSeesPlayer", "Range", "3", "SceneJumpy",
  "IfGridNPCSeesPlayer", "IgnoreWalls", "Range", "4", "SceneJumpy",

.. _IfGridNPCThere:

**IfGridNPCThere**
----------------------------------------
Checks if the named NPC is on the gridmap, if they are, jump to the scene, otherwise continue on.

.. code-block:: javascript

  "IfGridNPCThere", "Key", "Nothing",

.. _ChangeGridVision:

**ChangeGridVision**
----------------------------------------
Changes the active vision on the gridmap for the player, unless set on map creation or this is called, vision is across the entire map.

When active, vision is blocked by walls.

Can be set to 0 to to toggle vision back to global.

.. code-block:: javascript

  "ChangeGridVision", "5",

.. _IfGridVisonOn:

**IfGridVisonOn**
----------------------------------------
If the vision system for the gridmap is active, do a scene jump! Otherwise continue onwards.

.. code-block:: javascript

  "IfGridVisonOn", "TheSceneJump",

.. _SpawnGridNPC:

**SpawnGridNPC**
----------------------------------------
Spawns the named npc (must be exist in the map creation) and slaps it down at the current event location, or at specific coordinates.

.. code-block:: javascript

  "SpawnGridNPC", "LazyNPC", "Here"
  "SpawnGridNPC", "PickyNPC", "3", "4"

.. _ChangeMapTile:

**ChangeMapTile**
----------------------------------------
Change a map tile at specific coordinates to another tile that's in the map's list of tiles!

.. code-block:: javascript

  "ChangeMapTile", "6", "9", "TileName",
