import pytest

from aoc.day_03 import Node, answer


@pytest.mark.parametrize(
    "offset,expected,input",
    [
        pytest.param(Node(3, 1), 0, ["....", "....", "....", "...."], id="grid_without_any_trees"),
        pytest.param(Node(3, 1), 7, "example"),
        pytest.param(Node(1, 1), 2, "example"),
        pytest.param(Node(5, 1), 3, "example"),
        pytest.param(Node(7, 1), 4, "example"),
        pytest.param(Node(1, 2), 2, "example"),
        pytest.param(Node(3, 1), 250, "puzzle"),
        pytest.param(Node(1, 1), 55, "puzzle"),
        pytest.param(Node(5, 1), 54, "puzzle"),
        pytest.param(Node(7, 1), 55, "puzzle"),
        pytest.param(Node(1, 2), 39, "puzzle"),
    ],
)
def test_answers(resources, offset, expected, input):
    grid = input if isinstance(input, list) else resources.get(input)
    assert answer(grid, offset) == expected
