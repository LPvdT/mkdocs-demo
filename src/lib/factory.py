import subprocess
from typing import Callable


def factory(cmd: str) -> Callable[[], int | None]:
    def _func() -> int | None:
        try:
            return subprocess.call(cmd.split(" "), shell=False)
        except KeyboardInterrupt:
            pass

    return _func
