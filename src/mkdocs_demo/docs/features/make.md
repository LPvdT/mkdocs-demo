# Make

A `Makefile` is used to determine which pieces of the program need to be recompiled. The `Makefile` is run using the [`make`](https://www.gnu.org/software/make/manual/make.html) command.

!!! tip
    If the `make` command is not available, the tool can be installed using the system's package manager, e.g. `sudo apt install make -y`.

## Why use a `Makefile`?

Honestly, I primarily use these in conjunction with compiled languages (e.g. within my [`Rust`](https://www.rust-lang.org/) or [`Mojo`](https://www.modular.com/max/mojo) projects). They make more sense in those contexts (no need to use `.PHONY` everywhere). The main reason I have chosen to include one in this project is to demonstrate their application.

The `make` tool incorporates logic to determine what to recompile and what not to recompile (or re-transpile). For example, if a source file has not been changed, it will not be recompiled.

This seems trivial in a small project, but it makes a tremendous difference in build times for large projects. Furthermore, you can use `Makefile` to make specific command chains (recipes) dependant on another.

### Recipe: Default

The `help` recipe has been marked as the default recipe. Hence, it will show when calling `make` without a recipe specified.

```makefile
default: help

.PHONY: help
help: # Show help for each recipe.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done
```

```bash exec="true" title="Recipe: Default" result="ansi" source="material-block"
make
```

### Recipe: Package setup

The `all` recipe installs the project, installs the pre-commit hooks and then updates the pre-commit hooks to their latest version.

```makefile
.PHONY: all
all: pkg-install pc-install pc-update

.PHONY: pkg-install
pkg-install: # Installs the project.
	poetry install

.PHONY: pc-install
pc-install: pkg-install # Installs the pre-commit hooks.
	poetry run pre-commit install

.PHONY: pc-update
pc-update: pc-install # Updates the pre-commit hooks to their latest version.
	poetry run pre-commit autoupdate
```

```bash exec="true" title="Recipe: Set up package" result="console" source="material-block"
make all
```

### Recipe: Run pre-commit hooks

The `pc-run` recipe executes the pre-commits hooks on all files on demand.

!!! info
    This recipe depends on the `pc-install` recipe, which in turn depends on the `pkg-install` recipe. In other words, `make` ensures the package is installed, the pre-commit hooks are installed and then executes the `pc-run` recipe.

```makefile
.PHONY: pc-run
pc-run: pc-install # Run pre-commit hooks on all files immediately.
	poetry run pre-commit run --all-files
```

```bash exec="true" title="Recipe: Run pre-commit hooks" result="console" source="material-block"
make pc-run
```

#### Complete `Makefile`

??? example "Check out the full `Makefile` here."
    ```bash exec="true" result="makefile"
    cat Makefile
    ```

## Alternative: `poetry` scripts

Within `poetry`'s `pyproject.toml`, you can define scripts. You can define these scripts under the `[tool.poetry.scripts]` header.

Subsequently, after running `poetry install` to register the script, you can run them using `poetry run <script_name>`.

!!! info
    The scripts in `poetry` are quite similar to those in a `package.json` file, for those familiar with [NodeJS](https://nodejs.org/en) projects.

However, the main drawback of these scripts is that they require a specific entrypoint within a source file (e.g., `gen-typings = "src.mkdocs_demo.scripts.mypy:gen_types"`).

Moreover, they will run "naively". Specifically, they will transpile/compile every single file encompassed by the script's command. If all but one source file has remained unchanged, it will still encompass all files.

!!! note
    Of course, this depends on the parameters passed to the *subprocess* command. I am generalising here for the sake of providing an example.
