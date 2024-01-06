import subprocess
from typing import Callable


def factory(*args: tuple) -> Callable[[], int | None]:
    cmd: str = args[0]

    def _func() -> int | None:
        try:
            return subprocess.call(cmd.split(" "), shell=False)
        except KeyboardInterrupt:
            pass

    return _func
