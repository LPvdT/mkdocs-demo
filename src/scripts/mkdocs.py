"""This module generates script entrypoints for Poetry related to MkDocs."""

from lib.factory import factory

serve = factory(cmd="mkdocs serve --config-file src/mkdocs.yml")
build = factory(
    cmd="mkdocs build --config-file src/mkdocs.yml --clean --use-directory-urls"
)
