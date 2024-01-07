from lib.factory import factory

install = factory(cmd="pre-commit install")
run = factory(cmd="pre-commit run --all-files")
