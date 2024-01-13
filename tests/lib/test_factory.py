import pytest
from mkdocs_demo.lib.factory import command_factory


@pytest.mark.parametrize(
    ("cmd", "expected"),
    [
        ("echo 'Hello, World!'", 0),
        ("ls /nonexistent", 2),
        ("sleep 1", 0),
    ],
)
def test_command_factory(cmd: str, expected: int) -> None:
    func = command_factory(cmd)

    assert func() == expected
