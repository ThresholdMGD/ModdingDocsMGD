# Music & Art

!!! warning

    If using assets found online, always review licenses of copyrighted
    materials, and give credit to your sources.

## Mod Pathing

Whenever a *key* or function asks for an
image asset path, the game expects it to be in a base game directory by
default. This means *game/music/*, *game/sfx/*, or *game/images/*.

This is a problem if you want to use assets stored within your mod
folder since the game won't find it if it's looking for the asset file
like this:

``` json
"images/Mods/<modName>/folder/file.png"
```

To correct this behavior, one has to prepend the file path to their
asset file with `../`. This will tell the game to go back up by one
folder directory, landing it in */game*. It will look like so:

``` json
"../Mods/<modName>/folder/file.extensiontype"
```

Map related assets are the exception, as they're two directories deep
for the base game assets: *images/map/*. You will need to use `../`
twice in cases where you are making a new location on the map:

``` json
"../../Mods/<modName>/folder/file.extensiontype"
```

## Images

MGD supports the following image file types:

-   **PNG**: .png (recommended, and also specifically required for
    Location image backgrounds)
-   **WEBP**: .webp (comparatively smaller at the same levels of quality
    as PNG)
-   **JPG/JPEG** .jpg (not recommended due to transparency being
    unsupported by JPG files)

## Audio

Supported audio file types:

-   **Opus**: .opus
-   **Ogg Vorbis**: .ogg
-   **MP3**: .mp3
-   **WAV**: .wav (uncompressed 16-bit signed PCM only)

## Other

Additionally, when your mod is extracted in the Mods screen in-game, the
following file types will be extracted as well:

-   **Plain text**: .txt (Plain text files you'd write in a text
    editor, often for documentation purposes.)
-   **Markdown**: .md (Like plain text, except it adheres to the
    Markdown markup standard.)
-   **Avif**: .avif (A recently standardized image format, though it
    can't yet be used by the game.)
