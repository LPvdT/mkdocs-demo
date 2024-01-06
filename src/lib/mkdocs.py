import subprocess


def serve() -> int:
    cmd = "mkdocs serve --config-file src/mkdocs.yml"

    try:
        return subprocess.call(cmd.split(" "), shell=False)
    except KeyboardInterrupt:
        pass


def build() -> int:
    cmd = "mkdocs build --config-file src/mkdocs.yml --clean --use-directory-urls --site-dir ../site"

    try:
        return subprocess.call(cmd.split(" "), shell=False)
    except KeyboardInterrupt:
        pass
