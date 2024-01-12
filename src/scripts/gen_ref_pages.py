"""This module generates reference pages for MkDocstrings."""

from constants.config import RefGenConfig
from lib.mkdocstrings import gen_ref_pages

gen_ref_pages(config=RefGenConfig)
