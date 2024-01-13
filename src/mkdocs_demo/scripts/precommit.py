"""This module generates script entrypoints for Poetry related to pre-commit."""


from mkdocs_demo.lib.factory import command_factory

install = command_factory(cmd="pre-commit install")
update = command_factory(cmd="pre-commit autoupdate")
run = command_factory(cmd="pre-commit run --all-files")
