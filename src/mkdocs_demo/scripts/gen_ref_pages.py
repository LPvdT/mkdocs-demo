"""This module generates reference pages for MkDocstrings."""

from mkdocs_demo.config.config import RefGenConfig
from mkdocs_demo.lib.mkdocstrings import gen_ref_pages

_ = gen_ref_pages(config=RefGenConfig)
