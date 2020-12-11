from __future__ import annotations

import re
from typing import Callable, Iterator, List, Set

PATTERN_REQUIRED_FIELDS = {
    ("byr", lambda x: True),
    ("ecl", lambda x: True),
    ("eyr", lambda x: True),
    ("hcl", lambda x: True),
    ("hgt", lambda x: True),
    ("iyr", lambda x: True),
    ("pid", lambda x: True),
}

PATTERN_REQUIRED_FIELD_FORMAT = {
    ("byr", re.compile(r"^([1][9][2-9][0-9]|[2][0][0][0-2])$", re.I).match),
    ("ecl", re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$", re.I).match),
    ("eyr", re.compile(r"^([2][0][2][0-9]|[2][0][3][0])$", re.I).match),
    ("hcl", re.compile(r"^(#[\da-f]{6})$", re.I).match),
    ("hgt", re.compile(r"^([1][5-8][0-9]cm|[1][9][0-3]cm|[5][9]in|[6][0-9]in|[7][0-6]in)$", re.I).match),
    ("iyr", re.compile(r"^([2][0][1][0-9]|[2][0][2][0])$", re.I).match),
    ("pid", re.compile(r"^([\d]{9})$", re.I).match),
}


class Passport:
    def __init__(self, fields: List[str]):
        structured_fields = " ".join(fields).split(" ")
        self.fields = {k: v for k, v in [f.split(":", 1) for f in structured_fields]}

    def is_valid(self, validator: Set[str, Callable]) -> bool:
        try:
            return not [k for k, f in validator if not f(self.fields[k])]
        except KeyError:
            return False


def parse_input(input: List[str]) -> Iterator[Passport]:
    group = []
    for line in input:
        if line not in ("", None):
            group.append(line)
        else:
            yield group
            group.clear()
    if group:
        yield group


def calculate_total(passports: Iterator[Passport], validator: Set[str, Callable]) -> int:
    return sum([1 for p in passports if p.is_valid(validator)])


def answer1(input: List[str]) -> int:
    passports = map(Passport, parse_input(input))
    return calculate_total(passports, PATTERN_REQUIRED_FIELDS)


def answer2(input: List[str]) -> int:
    passports = map(Passport, parse_input(input))
    return calculate_total(passports, PATTERN_REQUIRED_FIELD_FORMAT)
