# Project

An example website of static generated content using
[MkDocs](https://www.mkdocs.org/).

## Packaging

This project's packaging and dependency management is done using
[Poetry](https://python-poetry.org/).

## Pre-commit hooks

The [pre-commit hooks](https://pre-commit.com/) for this project are defined in
the `.pre-commit-config.yaml` located in the root directory of the project.

### Pre-commit

+ Check YAML
  + Validates YAML files.
+ End-of-file fixer
  + Ensures a blank line at each file's end.
+ Trailing whitespace
  + Trims trailing whitespace from each line's end.

### [Mypy](https://mypy-lang.org/)

+ Static type checking for Python code.

### [Ruff](https://docs.astral.sh/ruff/)

+ Linter for Python code.
+ Formatter for Python code.

## Auto-generated documentation

The [API Reference](reference/mkdocs_demo/index.md) section contains the
documentation automatically generated from each docstring in the Python code.
This is built and compiled using the
[`mkdocstrings`](https://mkdocstrings.github.io/) package.
