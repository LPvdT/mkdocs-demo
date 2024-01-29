# Packaging

Dependency management and packaging for this project is managed by [Poetry](https://python-poetry.org/).

## Poetry

> *Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. Poetry offers a lockfile to ensure repeatable installs, and can build your project for distribution.*[^fn_1]

### Why Poetry?

Personally, I find `poetry` dependable and easy to use. Of course, there are alternatives to `poetry`. Examples of these are:

+ [PDM](https://pdm-project.org/latest/)
+ [Rye](https://rye-up.com/)

Using a dependency management tool allows us to easily set up repeatable installations (through a lockfile, such as `poetry.lock`), as well as package distribution.

!!! tip "Building the package"
    To build your package, simply run `poetry build`. This will compile your package to the `dist` directory.

    By default, both an `sdist` and a `wheel` distribution will be compiled.

The entire package configuration is managed through a single `pyproject.toml` file located in the repository's root. This is a big improvement compared to the clunky procedure using a classic approach with a `setuptools` backend.

Moreover, `poetry` allows easy distinguishing between *core*, *development* and *test* dependencies. This enables the user to choose what to install in an easy manner using the `pip` CLI.

*[CLI]: Command-Line Interface

### Drawbacks

A principal drawback I find, is that the `.venv` (*Virtual Environment*) folder created by Poetry can become quite large.

For projects that require complex dependencies (e.g., [PyTorch](https://pytorch.org/) projects, which ship with *GPU/CUDA* drivers, etc.), I often use `micromamba` to create a specific `conda` environment for the project. This way, I can re-use the same environment for multiple projects.

> *`micromamba` is a tiny version of the mamba package manager. It is a statically linked `C++` executable with a separate command line interface. It does not need a base environment and does not come with a default version of Python.*[^fn_2]

These environments can be persisted in a `YAML` file to create a functionality similar to a lockfile.

??? info "Why `micromamba` as opposed to `conda`?"
    `micromamba`[^fn_2] is very lightweight, and written in `C++`. As a result, it is much faster than a vanilla [Anaconda](https://www.anaconda.com/) set-up, and requires less space to boot.

[^fn_1]: https://python-poetry.org/docs/
[^fn_2]: https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html
