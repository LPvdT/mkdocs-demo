default: help

.PHONY: all pkg-install pkg-update pc-install pc-update pc-run md-serve md-build

help: ## Show help for each recipe.
	@echo "Usage:\n\tmake <recipe>"
	@echo "\nAvailable recipes:"
	@awk 'BEGIN {FS = ":.*##"; } /^[$$()% a-zA-Z_-]+:.*?##/ \
	{ printf "\t\033[36m%-30s\033[0m %s\n", $$1, $$2 } /^##@/ \
	{ printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

all: pkg-install pc-install pc-update

# Package recipes
pkg-install: ## Installs the project.
	poetry install

pkg-update: pkg-install ## Updates the project's dependencies to their latest versions.
	poetry update

# Pre-commit recipes
pc-install: pkg-install ## Installs the pre-commit hooks.
	poetry run pre-commit install

pc-update: pc-install ## Updates the pre-commit hooks to their latest version.
	poetry run pre-commit autoupdate

pc-run: pc-install ## Run pre-commit hooks on all files immediately.
	poetry run pre-commit run --all-files

# MkDocs recipes
md-serve: all ## Run MkDocs' builtin development server.
	poetry run mkdocs serve --config-file src/mkdocs_demo/mkdocs.yml

.DELETE_ON_ERROR:
md-build: all pkg-update ## Build the MkDocs documentation.
	poetry run mkdocs build --config-file src/mkdocs_demo/mkdocs.yml --clean --use-directory-urls
