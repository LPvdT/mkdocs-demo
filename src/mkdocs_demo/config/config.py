"""This module contains MkDocstrings configuration objects."""

from dataclasses import dataclass
from pathlib import Path

from .interfaces import Language


@dataclass
class RefGenConfig:
    """Dataclass to store MkDocstrings configuration."""

    handler: Language = Language.PYTHON
    """Handler language."""

    out_dir: Path = Path("reference")
    """Output directory."""
