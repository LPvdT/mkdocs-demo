# CI-CD

The CI/CD pipelines for this project are defined using [GitHub Actions](https://docs.github.com/en/actions).

## What is *GitHub Actions*?

> *GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production.*[^fn_1]

*[CI/CD]: Continuous Integration - Continuous Development
[^fn_1]: https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions

## Full workflow

!!! example "Full `ci-cd.yml`:"
    ```yaml
    name: CI-CD

    on: # (1)!
        push:
            branches:
            - main
            - master
        pull_request:
            branches:
            - main
            - master
        workflow_dispatch:

    permissions:
        contents: write # (2)!

    env: # (3)!
        PYTHON_VERSION: "3.11"
        POETRY_VERSION: "1.7.1"
        POETRY_URL: https://install.python-poetry.org

    jobs:
        deploy-docs: # (4)!
            runs-on: ubuntu-latest # (5)!
            steps: # (6)!
              - name: Checkout
                  uses: actions/checkout@v4

              - name: Configure Git credentials
                run: |
                    git config user.name github-actions[bot]
                    git config user.email 41898282+github-actions[bot]@users.noreply.github.com

              - name: Set up Python ${{ env.PYTHON_VERSION }}
                uses: actions/setup-python@v4
                id: setup_python
                with:
                    python-version: ${{ env.PYTHON_VERSION }}
                    cache: poetry

              - name: Poetry caching
                uses: actions/cache@v3
                with:
                    path: ~/.cache/pypoetry
                    key: poetry-cache-${{ runner.os }}-${{ steps.setup_python.outputs.python-version }}-${{ env.POETRY_VERSION }}

              - name: Cache packages
                uses: actions/cache@v3
                with:
                    path: ~/.local
                    key: poetry-local-${{ runner.os }}-${{ steps.setup_python.outputs.python-version }}-${{ hashFiles('**/poetry.lock') }}-${{ hashFiles('.github/workflows/*.yml') }}

              - name: Install Poetry ${{ env.POETRY_VERSION }}
                run: |
                    curl -sSL ${{ env.POETRY_URL }} | python - --version ${{ env.POETRY_VERSION }}
                    echo "$HOME/.local/bin" >> $GITHUB_PATH

              - name: Install dependencies
                run: poetry install --without test

              - name: Deploy site # (7)!
                run: |
                    poetry run \
                        mkdocs gh-deploy \
                        --config-file src/mkdocs_demo/mkdocs.yml \
                        --clean \
                        --use-directory-urls \
                        --force
    ```

    1. Define the events that can trigger the workflow:

          + `push:` On a push to the `master`/`main` branch.
          + `pull_request:` On pull request to the `master`/`main` branch.
          + `workflow_dispatch:` Enables the workflow to be triggered manually (from *GitHub*'s UI).
    2. Assign `write` permissions to the workflow.
    3. Define a map of environment variables available in the workflow.
    4. The name of the job in the workflow.
    5. The type of machine for the job to run on.
    6. The sequence of steps the job will perform.
    7. This final step performs the actual deployment of the documentation to *GitHub Pages*.
