import subprocess


def install() -> int:
    """
    The function `install` installs a pre-commit hook using the `pre-commit install` command.

    Returns
    -------
        The `install()` function is returning an integer value.

    """

    cmd = "pre-commit install"

    try:
        return subprocess.call(cmd.split(" "), shell=False)
    except KeyboardInterrupt:
        pass


def run() -> int:
    """
    The function runs the command "pre-commit run --all-files" and returns the exit code.

    Returns
    -------
        an integer value.

    """

    cmd = "pre-commit run --all-files"

    try:
        return subprocess.call(cmd.split(" "), shell=False)
    except KeyboardInterrupt:
        pass
