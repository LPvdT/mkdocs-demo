"""This module generates script entrypoints for Poetry related to Mypy typings
generation."""

from mkdocs_demo.lib.factory import command_factory

gen_types = command_factory("stubgen -p mkdocs_demo -o typings")
