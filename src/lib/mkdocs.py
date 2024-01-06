import subprocess


def serve() -> int:
    cmd = "mkdocs serve -f src/mkdocs.yml"

    try:
        return subprocess.call(cmd.split(" "), shell=False)
    except KeyboardInterrupt:
        pass
