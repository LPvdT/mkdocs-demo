# Welcome to MkDocs

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

```shell
.
├── .editorconfig
├── .gitattributes
├── .gitignore
├── .pre-commit-config.yaml
├── .venv
├── .vscode
│   └── settings.json
├── README.md
├── dist
├── poetry.lock
├── pyproject.toml
├── site
└── src
    ├── docs
    │   └── index.md
    ├── lib
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── factory.py
    │   ├── mkdocs.py
    │   ├── precommit.py
    │   └── test_class.py
    ├── mkdocs.yml
    ├── mkdocs_testing
    │   └── __init__.py
    └── templates
        └── .gitkeep
```

## Reference

::: src.lib.factory.factory

::: src.lib.test_class.TestClass

## External: `installer.records`

See [installer.records][] to learn about records.
