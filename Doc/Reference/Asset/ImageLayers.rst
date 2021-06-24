.. _Image Layers:

**Image Layers**
=================

.. _ChangeImageFor:

**ChangeImageFor**
-------------------
Changes the image of a displayed character. The number represents which of the characters that are currently being displayed will have their image changed.
In combat, it will change the focused monster instead of a specific one. Typically for characters that don't make use of layers.

::

  "ChangeImageFor", "1", "ImageName"

In combat with ``"FocusOnMonster"``:

::

  "FocusOnMonster", "1", "ChangeImageFor", "ImageName"

.. _ChangeImageLayer:

**ChangeImageLayer**
---------------------
Changes a specific layer of art for the specified character in the scene, works almost the same as above.
If you set the image name to ``""``, it will stop displaying the layer. Excluding layers with ``"alwaysOn":`` enabled.

::

  "ChangeImageLayer", "LayerType", "1", "ImageName"

Make sure the LayerType field is the same as that layer’s name in the monster's json.

Instead of a number, you can instead designate a Monster's nameID. It will change their layer regardless of what position they are in from
:ref:`DisplayCharacters`. Also useful for tracking who’s face you’re changing.

.. _ActivateOverlay:

**ActiveOverlay & DeactivateOverlay**
""""""""""""""""""""""""""""""""""""""
::

  "ChangeImageLayer", "RightArm", "1", "ActivateOverlay"

  "ChangeImageLayer", "LeftArm", "1", "DeactivateOverlay"

``"ActivateOverlay"`` and ``"DeactivateOverlay"`` toggles the visibility of a layer.

**ImageSet & ImageSetPersist**
"""""""""""""""""""""""""""""""
::

  "ChangeImageLayer", "ImageSet", "1", "Plush"

``"ImageSet"`` will swap a set of images to the name of the set in the final string in the above. It will automatically carry over any current expressions and related.
Note this is not held persistently and would need to be called every time the character is called.

``"ImageSetPersist"`` will swap to the stated image set and stay on it whenever that character is called again, even in combat. Used for Aiko's body type variants.

::

  "ChangeImageLayer", "ImageSetPersist", "1", "Plush"

**ImageSetDontCarryOver**
""""""""""""""""""""""""""
Gives the ability to use Image Sets as alternate CGs without needing to be the exact same layer layout as the other sets.

::

  "ChangeImageLayer", "ImageSetDontCarryOver", "1", "Hypno"

.. Not confidant in how I've described the functions here, will go over it again when I make the expanded pages on the pictures key.
