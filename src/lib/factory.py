import subprocess
from typing import Callable


def factory(cmd: str) -> Callable[..., int | None]:
    """
    The `factory` function takes a command as input and returns a function that, when called, executes
    the command and returns the exit code or None if the execution is interrupted.

    Parameters
    ----------
    cmd : str
        The `cmd` parameter is a string that represents a command to be executed.

    Returns
    -------
    The factory function returns a callable object, which is a function. The function takes no
    arguments and returns either an integer or None.
    """

    def _func(_cmd: str = cmd) -> int | None:
        try:
            return subprocess.call(_cmd.split(" "), shell=False)
        except KeyboardInterrupt:
            pass

        return None

    return _func
