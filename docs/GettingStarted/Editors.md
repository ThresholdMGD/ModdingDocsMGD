# Installing a Text Editor

The following text editors are ensured to properly read and understand
.json files, offer useful features, and generally ensure you have a much
more streamlined experience while modding. Other well-made text editors
exist beyond the three listed here, but these are among the best free
editors out there.

Don't get too worried about your choice, as you can easily change it at
any time.

These all have portable versions if you want your editor and modding to
work on a USB, separate from your main system.

## [Visual Studio Code](https://code.visualstudio.com/)

[Portable version](https://code.visualstudio.com/docs/editor/portable)

[Web version (Chrome-based browser recommended for local
development)](https://vscode.dev/)

- Supports all desktop platforms and the web.
- Most well-featured editor out of the box. JSON
    Linter pre-installed.
- Built-in project folder navigation and management.
- Extension support, with the largest and well-maintained collection.
- Best Git and GitHub integration.
- **MGD extension is available for some automated error checking and
  easing development.** Use `ctrl+shift+x` or `⌘+shift+x`, search for
  `MGD Language`.

## [Pulsar](https://pulsar-edit.dev/download.html#regular-releases)

For the portable version, go to the above link, and select "Portable"
for your given platform (currently only Windows as of writing).

- Supports all desktop platforms.
- Moderately featured.
- Built-in project folder navigation and management.
- Package support, including a JSON Linter. Open settings using
  `ctrl+,`, or `⌘+,`, go to Install,
  search `linter`, `linter-ui-default`, and `linter-jsonlint`.
  Say yes to any dependencies.
- Git and GitHub integration.

!!! info

    Previously known as Atom. The original version ceased
    development, continuing as Pulsar by the community.
    Pulsar currently has access to the same packages and provides continued
    security, bug fixes, compatibility, and feature updates for the editor.

## [Notepad++](https://notepad-plus-plus.org/resources/)

For the portable version, go to the Downloads page, select the latest
version, and grab the zip file.

- Windows only.
- Feature-lite.
- Has built-in folder navigation under View -\> Folder As Workspace.
  Cannot manage folders and files.
- Supports packages and customization (use 32-bit version), though not
  as convenient or powerful, with weak defaults.
- Fast boot times.
- Handles large multi-thousand-line files best.

!!! warning

    When using Notepad++, please use spaces for tabs, and utf-8
    encoding! This helps prevent indentation and whitespace errors between
    text editors.

- Settings -\> Preferences -\> Language -\> 'Replace by space' on
    the right.
- Settings -\> Preferences -\> New document -\> Encoding -\> choose
  UTF-8 *without BOM*.

## Linter

It's **HIGHLY** encouraged to use a built-in JSON linter in your editor
of choice. It will help you avoid critical errors that cause the game to
crash from improper JSON formatting in real-time. If you truly don't
wish to use one within your text editor, then you can use this [handy
website](https://jsonformatter.curiousconcept.com/) to check for JSON
formatting issues.
