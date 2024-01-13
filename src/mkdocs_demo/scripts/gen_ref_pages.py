"""This module generates reference pages for MkDocstrings."""

from mkdocs_demo.constants.config import RefGenConfig
from mkdocs_demo.lib.mkdocstrings import gen_ref_pages

gen_ref_pages(config=RefGenConfig)
