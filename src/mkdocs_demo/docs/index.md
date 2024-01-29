# Project

This is an example website of static generated website using
[MkDocs](https://www.mkdocs.org/).

It demonstrates the application several seminal approaches and techniques. A summary of these is shown below. More details on these can be found in the [Features](./features/index.md) section.

## Project Layout

This section gives an overview of the layout of the repository.

### Tree

!!! info
    The code to generate this directory tree gets automatically executes
    and inserted upon building the documentation by the [`markdown-exec`](https://pypi.org/project/markdown-exec/) package.

```bash title="Directory Tree" exec="true" source="tabbed-right" result="ansi"
tree -haC --gitignore --du --dirsfirst -I ".git|*.pyc|*.pyi"
```
## Auto-generated documentation

The [API Reference](reference/mkdocs_demo/index.md) section contains the
documentation automatically generated from each docstring in the Python code.
This is built and compiled using the
[`mkdocstrings`](https://mkdocstrings.github.io/) package. For more details, refer to the [Auto-documentation section](./features/auto-documentation.md).

## Packaging

This project's packaging and dependency management is done using
[Poetry](https://python-poetry.org/). More details can be found in the [Packaging section](./features/packaging.md).

## Pre-commit hooks

This project uses [pre-commit hooks](https://pre-commit.com/). For more details on this subject, consult the [Pre-commit hooks section](./features/pre-commit.md).
