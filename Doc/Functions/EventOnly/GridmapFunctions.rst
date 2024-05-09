.. _Gridmap Functions:

**Gridmap Functions**
======================

.. seealso::

    For defining a GridMap in an event, see :ref:`Gridmap`

.. _ExitGridmap:

**ExitGridmap**
-----------------------------------------------
``"ExitGridmap"`` leaves the active Gridmap the player is in.

**Must be called to properly exit the gridmap**. Ensure you design your Gridmap events to always have an intended exit of some form.

.. _StunGridPlayer:

**StunGridPlayer**
-----------------------------------------------
Stuns the players map movement for X number of turns. Useful for traps.

.. code-block:: javascript

  "StunGridPlayer", "1"

.. _IfGridPlayerStunned:

**IfGridPlayerStunned**
-----------------------------------------------
``"IfGridPlayerStunned"`` checks if the player is stunned by ``StunGridPlayer``.
If true, jumps to the given event scene, else, silently continues the scene.

.. code-block:: javascript

  "IfGridPlayerStunned", "YourStunGridSceneName"

.. _SetPlayerGridPosition:

**SetPlayerGridPosition**
-----------------------------------------------
Move the player to another location on the map using the coordinates provided in the following two :term:`string` values.

The first given :term:`value` represents the X position, increasing in numerical :term:`value` from left to right.
The second :term:`value` represents the Y position, increasing in numerical :term:`value` from top to bottom.

.. code-block:: javascript

  "SetPlayerGridPosition", "0", "0"

.. _IfGridNPCSeesPlayer:

**IfGridNPCSeesPlayer**
-----------------------------------------------
``"IfGridNPCSeesPlayer"`` checks if the focused NPC sees the player in a direct line of sight
within the given sub-function paramaters.

First, optinally declare ``"IgnoreWalls"`` if the NPC is meant to see through Wall tiles.

Next you can add  ``"NPC", "theNameOfGridNPC"`` to make them look for an npc with a name instead of the player. This must be called before Range.

Then, optionally declare ``"Range"`` to declare a limited Tile range to their vision. By default, they see as far as possible.

Lastly, declare the scene name it's meant to jump to if true. If false, silently continues the scene.

.. code-block:: javascript

  "IfGridNPCSeesPlayer", "EnsuredChase",
  "IfGridNPCSeesPlayer", "Range", "3", "SceneJumpy",
  "IfGridNPCSeesPlayer", "IgnoreWalls", "Range", "4", "SceneJumpy",
  "IfGridNPCSeesPlayer", "NPC", "WayPoint1", "Range", "1", "GoToWaypoint2",

.. _ChangeGridVision:

**ChangeGridVision**
-----------------------------------------------
``"ChangeGridVision"`` changes the active :ref:`Grid Sight` of the player for the active Gridmap.

Can be set to a :term:`value` of ``"0"`` to toggle vision back to global range.

.. code-block:: javascript

  "ChangeGridVision", "5",

.. tip::

  If you just want to limit player vision through walls, you can set the sight to the maximum possible length of a column or row on the map.

.. _IfGridVisonOn:

**IfGridVisonOn**
-----------------------------------------------
``"IfGridVisionOn"`` checks if the player :ref:`Grid Sight` is on. If true, jump to the given scene, else, silently continues the scene.

.. code-block:: javascript

  "IfGridVisonOn", "TheSceneJump",

.. _ChangeGridNPCMovement:

**ChangeGridNPCMovement**
-----------------------------------------------
``"ChangeGridNPCMovement"`` changes the FocusedEvent NPCs movement type given
in the following :term:`string` values.

  * - ``"", ""``
    - Empty :term:`string` means none, meaning they always stand still. Needs two empty strings.
  * - ``"Chase"``
    - Directly chases the defined target. Uses Astar pathfinding.
  * - ``"Ambush"``
    - Tries to move to a valid tile 4 spaces infront of the defined target.
  * - ``"Whimsical"``
    - For the given Target, picks any valid tile within the following given tile range of the target. If called again while active, it finds a new tile.
  * - ``"Wander"``
    - Wanders randomly in any direction, can sometimes hit against Wall tiles.
  * - ``"Projectile'Direction'"``
    - These go in a straight line and if they hit a wall they destroy themselves.

Targets can be any of the following :term:`string` values:
* ``"Player"`` for targeting the players position.
* ``"NPCName"`` meaning for targeting a NPCs position. :term:`value` is meant to be their Gridmap NPC Name.
* ``"Coord"", "", ""`` for targeting a specific X and Y coordinate on the grid.

.. code-block:: javascript

  "ChangeGridNPCMovement", "", ""
  "ChangeGridNPCMovement", "Chase", "Player"
  "ChangeGridNPCMovement", "Chase", "Coord", "6", "9"
  "ChangeGridNPCMovement", "Ambush", "Player"
  "ChangeGridNPCMovement", "Whimsical", "Ceris", "5"
  "ChangeGridNPCMovement", "Wander",
  "ChangeGridNPCMovement", "ProjectileUp",
  "ChangeGridNPCMovement", "ProjectileDown",
  "ChangeGridNPCMovement", "ProjectileLeft",
  "ChangeGridNPCMovement", "ProjectileRight"

.. _IfGridNPCThere:

**IfGridNPCThere**
-----------------------------------------------
``"IfGridNPCThere"`` checks if the named NPC is on the gridmap.
If true, jump to the given scene, else, silently continues the scene.

.. code-block:: javascript

  "IfGridNPCThere", "Key", "Nothing",

.. _SetActiveGridNPC:

**SetActiveGridNPC**
-----------------------------------------------
``"SetActiveGridNPC"`` checks if the named NPC is on the gridmap, then sets the currently focused NPC to them for the sake of functions, should only be used for uniquely named NPCS.

.. code-block:: javascript

  "SetActiveGridNPC", "Ushris",

.. _SpawnGridNPC:

**SpawnGridNPC**
-----------------------------------------------
``SpawnGridNPC`` spawns a Gridmap :ref:`Gridmap NPC` from on the map,
either at the current event location via ``"Here"``, or at specific X and Y coordinates.
You can also alter the timer of an NPC if it has one.

.. code-block:: javascript

  "SpawnGridNPC", "LazyNPC", "Here"
  "SpawnGridNPC", "PickyNPC", "3", "4"
  "SpawnGridNPC", "PickyNPC", "Timer", "6", "TimerMax", "7", "3", "4"

.. _RemoveGridNPC:

**RemoveGridNPC**
-----------------------------------------------
``RemoveGridNPC`` removes a Gridmap :ref:`Gridmap NPC` from the map,
taking either the following :term:`value` of ``"Current"`` or ``"Specific"``.

``"Current"`` uses the NPCs TurnEvent triggered event to select the NPC.

``"Specific"`` takes the given NPCs defined Name to select the NPC.

.. code-block:: javascript

  "RemoveGridNPC", "Current"
  "RemoveGridNPC", "Specific", "NPCName"

.. _ChangeMapTile:

**ChangeMapTile**
-----------------------------------------------
``"ChangeMapTile"`` changes a Gridmap Tile in a :ref:`Tileset` at a given X and Y coordinate to another tile based on the tiles ID in the TileSet.

.. code-block:: javascript

  "ChangeMapTile", "6", "9", "TileID",
