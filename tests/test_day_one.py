import pytest

from aoc.day_one import answer


@pytest.mark.parametrize(
    "value,size,expected,input",
    [
        pytest.param(2020, 2, 0, [], id="empty_expense_list_is_zero"),
        pytest.param(2020, 2, 0, [2020, 0], id="product_of_zero_is_zero"),
        pytest.param(2020, 3, 2018, [2018, 1, 1], id="product_of_one_is_value"),
        pytest.param(2020, 2, 514579, "example", id="part_1_example"),
        pytest.param(2020, 2, 996996, "puzzle", id="part_1_puzzle"),
        pytest.param(2020, 3, 241861950, "example", id="part_2_example"),
        pytest.param(2020, 3, 9210402, "puzzle", id="part_2_puzzle"),
    ],
)
def test_answers(resources, value, size, expected, input):
    expenses = input if isinstance(input, list) else resources.get(input)
    assert answer(expenses, size, value) == expected
