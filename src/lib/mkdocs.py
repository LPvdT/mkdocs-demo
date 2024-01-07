from lib.factory import factory

serve = factory(cmd="mkdocs serve --config-file src/mkdocs.yml")
build = factory(
    cmd="mkdocs build --config-file src/mkdocs.yml --clean --use-directory-urls --site-dir ../site"
)
