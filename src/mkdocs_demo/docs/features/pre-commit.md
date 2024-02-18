# Pre-commit Hooks

[Pre-commit hooks](https://pre-commit.com/) are by default executed, as their name suggests, before every commit. They serve as a guardrail to ensure code quality and other useful stuff.

The hooks can perform tasks, such as formatting code or trimming trailing whitespace, or perform specific checks. When a key check fails (such as `mypy` static type checking), the commit cannot be made until the issue has been resolved.

!!! tip
    Pre-commit hooks can be called on more events than *on commit*. All options, and their descriptions, can be found [here](https://pre-commit.com/#supported-git-hooks).

## Using pre-commit hooks

**In order to use pre-commit hooks in your projects:**

1. The `pre-commit` package needs to be installed:
      + Refer to my `pyproject.toml`.
      + Accomplished using `poetry add --group="dev" pre-commit`.
2. The desired hooks need to be defined in `.pre-commit-config.yaml`.
3. The hooks need to be installed:
     + Run `pre-commit install`

??? example "Manually executing and updating pre-commit hooks"
    Pre-commit hooks can be run on demand, as well as automatically updated to the latest version.

    I have elected to create `poetry` scripts for both applications (refer to `pyproject.toml`).

    !!! tip "Executing pre-commit hooks on demand"
        To run your pre-commit hooks on demand, instead of only when their trigger condition is met, use the command `pre-commit run --all-files`.

    !!! tip "Updating pre-commit hooks"
        To update all pre-commit hooks to their latest version, use the command `pre-commit autoupdate`.

### [Pre-commit](https://github.com/pre-commit)

These hooks are from the default [`pre-commit`](https://github.com/pre-commit/pre-commit-hooks) repository:

+ **`check-yaml`:**
    + Validates YAML files.
+ **`end-of-file-fixer`:**
    + Ensures a blank line at each file's end.
+ **`trailing-whitespace`:**
    + Trims trailing whitespace from each line's end.

### [Mypy](https://mypy-lang.org/)

These hooks are from the [`mypy`](https://github.com/pre-commit/mirrors-mypy) repository:

+ **`mypy`:**
    + Static type checking for Python code.

### [Ruff](https://docs.astral.sh/ruff/)


These hooks are from the [`rust`](https://github.com/astral-sh/ruff-pre-commit) repository:

For those of you who have not yet heard about Ruff; it is a drop-in replacement for `isort`, `black` and `flake8` combined. Within VSCode, it takes care of linting, formatting and import sorting.

Ruff works out of the box, and completely blows aforementioned packages out of the water in terms of performance, due to it being written in Rust.

+ **`ruff`:**
    + Linter for Python code.
+ **`ruff-format`:**
    + Formatter for Python code.

## Full configuration

??? example "Check out the full `.pre-commit-config.yaml` here."
    ```bash exec="true" result="yaml"
    cat .pre-commit-config.yaml
    ```
