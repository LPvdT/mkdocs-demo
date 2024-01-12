"""This module contains MkDocstrings configurations."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class Language(Enum):
    """
    Enum that represents different programming languages.
    """

    PYTHON: str = "*.py"
    """Python language."""

    BASH: str = "*.sh"
    """Bash language."""


@dataclass
class RefGenConfig:
    """Dataclass to store MkDocstrings configuration."""

    handler: Language = Language.PYTHON
    """Handler language."""

    out_dir: Path = Path("reference")
    """Output directory."""
