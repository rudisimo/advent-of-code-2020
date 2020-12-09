import pytest

from aoc.day_03 import Node, answer


def identify(val):
    if isinstance(val, (Node,)):
        return str(val)


@pytest.mark.parametrize(
    "inputs,offset,expected",
    [
        pytest.param("without_trees", Node(3, 1), 0),
        pytest.param("example_input", Node(3, 1), 7),
        pytest.param("example_input", Node(1, 1), 2),
        pytest.param("example_input", Node(5, 1), 3),
        pytest.param("example_input", Node(7, 1), 4),
        pytest.param("example_input", Node(1, 2), 2),
        pytest.param("puzzle_input", Node(3, 1), 250),
        pytest.param("puzzle_input", Node(1, 1), 55),
        pytest.param("puzzle_input", Node(5, 1), 54),
        pytest.param("puzzle_input", Node(7, 1), 55),
        pytest.param("puzzle_input", Node(1, 2), 39),
    ],
    ids=identify,
)
def test_answers(fixtures, inputs, offset, expected):
    grid = fixtures.get(inputs, [])
    assert answer(grid, offset) == expected
