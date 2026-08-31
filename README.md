# Monster Girl Dreams Modding Documentation

Built using Zensical.

## Building

To get started, run one of the following via console in the directory:

```bash
build.bat       # Windows wrapper to build.py
./build.sh        # Unix wrapper to build.py
python build.py # The actual build script
```

## Manual Build

```bash
pip install -r requirements.txt
python generate_nav.py
python -m zensical build
```

## Iterating

- `python -m zensical serve` gives you live reloading in the browser, the best choice for editing existing files or even css.
- `python -m zensical build` can be used for manual rebuilds but is slower for iterating.
- Use `python ./generate_nav.py` directly to regenerate navigation when not using the build scripts.

## Resources

Zensical reads `mkdocs.yml` configuration and generates html from Python Markdown formatted content.

- [Zensical](https://zensical.org/)
- [neoteroi spantables](https://www.neoteroi.dev/mkdocs-plugins/spantable/)

Minor design rules:

- Use spantables instead of normal tables as that is the only one themed at the moment.
- Index pages should be the only use of cards,
use spantables instead for situations needing horizontal density.
