default: help

.PHONY: help
help: # Show help for each recipe.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: all
all: pkg-install pc-install pc-update

.PHONY: pkg-install
pkg-install: # Installs the project.
	poetry install

.PHONY: pkg-update
pkg-update: pkg-install # Updates the project's dependencies to their latest versions.
	poetry update

.PHONY: pc-install
pc-install: pkg-install # Installs the pre-commit hooks.
	poetry run pre-commit install

.PHONY: pc-update
pc-update: pc-install # Updates the pre-commit hooks to their latest version.
	poetry run pre-commit autoupdate

.PHONY: pc-run
pc-run: pc-install # Run pre-commit hooks on all files immediately.
	poetry run pre-commit run --all-files

.PHONY: md-serve
md-serve: all # Run MkDocs' builtin development server.
	poetry run mkdocs serve --config-file src/mkdocs_demo/mkdocs.yml

.PHONY: md-build
.DELETE_ON_ERROR:
md-build: all pkg-update # Build the MkDocs documentation.
	poetry run mkdocs build --config-file src/mkdocs_demo/mkdocs.yml --clean --use-directory-urls
