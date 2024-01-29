# Unit Testing

This project demonstrates the use of unit testing using [pytest](https://docs.pytest.org).

The tests are located in the `tests` folder in the root of the repository.

!!! warning
    For this specific project, while functional, the tests are kind of trivial, because there is not that much to be tested in this project. The tests mainly serve demonstrate the approach.

## Running the tests

Execute the command `poetry run pytest -v` to execute all tests and view the result in the *Terminal*.

!!! tip
    Running the tests can be made a requirement of the *pre-commit hooks* and/or the *CI-CD* pipeline.
