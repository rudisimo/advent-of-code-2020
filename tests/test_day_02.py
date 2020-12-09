import pytest

from aoc.day_02 import answer, filter_by_frequency, filter_by_position


@pytest.mark.parametrize(
    "filter,expected,input",
    [
        pytest.param(filter_by_frequency, 0, [], id="empty_policy_list_is_zero"),
        pytest.param(filter_by_frequency, 1, ["0-0 a: bbb"], id="zero_min_max_policy_is_match"),
        pytest.param(filter_by_position, 0, ["1-1 b: bbb"], id="same_min_max_position_is_zero"),
        pytest.param(filter_by_frequency, 2, "example"),
        pytest.param(filter_by_frequency, 569, "puzzle"),
        pytest.param(filter_by_position, 1, "example"),
        pytest.param(filter_by_position, 346, "puzzle"),
    ],
)
def test_answers(resources, filter, expected, input):
    policies = input if isinstance(input, list) else resources.get(input)
    assert answer(policies, filter) == expected
