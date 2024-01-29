# Make

A `Makefile` is used to determine which pieces of the program need to be recompiled. The `Makefile` is run using the [`make`](https://www.gnu.org/software/make/manual/make.html) command.

!!! tip
    If the `make` command is not available, the tool can be installed using the system's package manager, e.g. `sudo apt install make -y`.

## Why use a `Makefile`?

Honestly, I primarily use these in conjunction with compiled languages (e.g. within my [`Rust`](https://www.rust-lang.org/) or [`Mojo`](https://www.modular.com/max/mojo) projects). They make more sense in those contexts.

The main reason I have chosen to include one in this project is to demonstrate their application.

### `poetry` scripts approach

Within `poetry`'s `pyproject.toml`, you can define scripts. You can define these scripts under the `[tool.poetry.scripts]` header.

Subsequently, after running `poetry install` to register the script, you can run them using `poetry run <script_name>`.

!!! info
    The scripts in `poetry` are quite similar to those in a `package.json` file, for those familiar with [NodeJS](https://nodejs.org/en) projects.

However, the main drawback of these scripts is that they require a specific entrypoint within a source file (e.g., `gen-typings = "src.mkdocs_demo.scripts.mypy:gen_types"`).

Moreover, they will run "naively". Specifically, they will transpile/compile every single file encompassed by the script's command. If all but one source file has remained unchanged, it will still encompass all files.

!!! note
    Of course, this depends on the parameters passed to the *subprocess* command. I am generalising here for the sake of providing an example.

### `Makefile` approach

The `make` tool incorporates logic to determine what to recompile and what not to recompile (or re-transpile). For example, if a source file has not been changed, it will not be recompiled.

This seems trivial in a small project, but it makes a tremendous difference in build times for large projects.
