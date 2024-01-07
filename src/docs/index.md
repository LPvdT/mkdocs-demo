# MkDocs + MkDocstrings

## Project layout

```bash
tree -aL 2 --gitignore

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

## External: `installer.records`

See [installer.records][] to learn about records.
