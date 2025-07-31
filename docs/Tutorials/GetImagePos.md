# Getting Image Position Coordinates
This tutorial will show you how to get the X and Y coordinates for
positioning location icons and clouds on the MGD world map using
Photopea, a free photo editor you can use within your browser without
any download or sign up. Any other image editor should allow for similar
functionality if you already have a prefered choice.

-   Go to <https://www.photopea.com/>
-   Open and drag and drop the MGD world map image located at
    `/game/images/map/map.png`
-   Either drag and drop your iocn, or along the top of the window,
    press `File`, then `Open & Place...`

![image](../img/photopeaopen.png)

-   Ensure your icon is dragged above the map in the list of layers
    along the right side of the window.

![image](../img/photopealayer.png)

-   Click your icon on the canvas, and ensure along the top of the
    window that `Distances` is checked.

![image](../img/photopeadistances.png)

-   Lastly, drag your icon to the desired spot on the map. Zoom in to
    ensure it is pixel perfect.
-   Zooming back out, the left and top coordinates the red lines
    attached to your icon are the X and Y coordinates you need to put
    into `"mapIconXpos":` and `"mapIconYpos":` respectively.

![image](../img/photopeapositions.png)

With these aquired values you can now return to
[Locations](../Manual/Locations/Locations.md)
