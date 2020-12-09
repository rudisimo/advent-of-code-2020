import pytest

from aoc.day_01 import answer


@pytest.mark.parametrize(
    "inputs,value,size,expected",
    [
        pytest.param("empty_list", 2020, 2, 0),
        pytest.param("product_of_zero", 2020, 2, 0),
        pytest.param("product_of_self", 2020, 3, 2018),
        pytest.param("example_input", 2020, 2, 514579),
        pytest.param("puzzle_input", 2020, 2, 996996),
        pytest.param("example_input", 2020, 3, 241861950),
        pytest.param("puzzle_input", 2020, 3, 9210402),
    ],
)
def test_answers(fixtures, inputs, value, size, expected):
    expenses = fixtures.get(inputs, [])
    assert answer(expenses, size, value) == expected
