# Monster Girl Dreams Modding Documentation

Built using MkDocs Material.

## Building

To get started, run one of the following:

```bash
./build.bat       # Windows wrapper to build.py
./build.sh        # Unix wrapper to build.py
python ./build.py # The actual build script
```

## Manual Build

```bash
pip install -r requirements.txt
python generate_nav.py
mkdocs build
```

## Iterating

- `mkdocs serve` gives you live reloading in the browser, the best choice for editing existing files or even css. 
- `mkdocs build` can be used for manual rebuilds but is slower for iterating.
- Use `python ./genereate_nav.py` directly to regenerate navigation when not using the build scripts.

## Resources

MkDocs is formatted in a variant of markdown, so if you've used Discord at all
you are already off to a good start.

- [MkDocs User Guide](https://www.mkdocs.org/user-guide/)
- [MkDocs Material Reference](https://squidfunk.github.io/mkdocs-material/reference/)
- [MkDocs Macros Plugin](https://mkdocs-macros-plugin.readthedocs.io/en/latest/)
- [MkDocs Redirects](https://github.com/mkdocs/mkdocs-redirects#using)
- [neoteroi spantables](https://www.neoteroi.dev/mkdocs-plugins/spantable/)

Minor design rules:

- Use spantables instead of normal tables as that is the only one themed at the moment.
- Index pages should be the only use of cards,
use spantables instead for situations needing horizontal density.
