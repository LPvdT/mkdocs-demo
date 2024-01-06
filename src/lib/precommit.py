import subprocess


def install() -> int:
    cmd = "pre-commit install"

    try:
        return subprocess.call(cmd.split(" "), shell=False)
    except KeyboardInterrupt:
        pass


def run() -> int:
    cmd = "pre-commit run --all-files"

    try:
        return subprocess.call(cmd.split(" "), shell=False)
    except KeyboardInterrupt:
        pass
