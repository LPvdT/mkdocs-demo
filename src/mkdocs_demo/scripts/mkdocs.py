"""This module generates script entrypoints for Poetry related to MkDocs."""

from mkdocs_demo.lib.factory import command_factory

serve = command_factory(cmd="mkdocs serve --config-file src/mkdocs_demo/mkdocs.yml")
build = command_factory(
    cmd="mkdocs build --config-file src/mkdocs_demo/mkdocs.yml --clean --use-directory-urls"
)
