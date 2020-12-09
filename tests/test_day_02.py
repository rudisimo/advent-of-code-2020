import pytest

from aoc.day_02 import answer, filter_by_frequency, filter_by_position


@pytest.mark.parametrize(
    "inputs,filter,expected",
    [
        pytest.param("empty_list", filter_by_frequency, 0),
        pytest.param("empty_list", filter_by_position, 0),
        pytest.param("zero_min_max_policy", filter_by_frequency, 1),
        pytest.param("same_min_max_policy", filter_by_position, 0),
        pytest.param("example_input", filter_by_frequency, 2),
        pytest.param("puzzle_input", filter_by_frequency, 569),
        pytest.param("example_input", filter_by_position, 1),
        pytest.param("puzzle_input", filter_by_position, 346),
    ],
)
def test_answers(fixtures, inputs, filter, expected):
    policies = fixtures.get(inputs, [])
    assert answer(policies, filter) == expected
