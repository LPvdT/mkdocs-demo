from .interfaces import Language as Language
from dataclasses import dataclass
from pathlib import Path

@dataclass
class RefGenConfig:
    handler: Language = ...
    out_dir: Path = ...
    def __init__(self, handler, out_dir) -> None: ...
