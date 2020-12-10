import pytest

from aoc.day_04 import answer, VALIDATE_BY_PRESENCE, VALIDATE_BY_REGEX_VALUE


@pytest.mark.parametrize(
    "inputs,validator,expected",
    [
        pytest.param("empty_list", VALIDATE_BY_PRESENCE, 0),
        pytest.param("example_input", VALIDATE_BY_PRESENCE, 2),
        pytest.param("puzzle_input", VALIDATE_BY_PRESENCE, 202),
        pytest.param("example_invalid_input", VALIDATE_BY_REGEX_VALUE, 0),
        pytest.param("example_valid_input", VALIDATE_BY_REGEX_VALUE, 4),
        pytest.param("puzzle_input", VALIDATE_BY_REGEX_VALUE, 137),
    ],
)
def test_answers(fixtures, inputs, validator, expected):
    passports = fixtures.get(inputs, [])
    assert answer(passports, validator) == expected
