from __future__ import annotations

import re

VALIDATE_BY_PRESENCE = {
    ("byr", lambda x: True),
    ("ecl", lambda x: True),
    ("eyr", lambda x: True),
    ("hcl", lambda x: True),
    ("hgt", lambda x: True),
    ("iyr", lambda x: True),
    ("pid", lambda x: True),
}

VALIDATE_BY_REGEX_VALUE = {
    ("byr", re.compile(r"^([1][9][2-9][0-9]|[2][0][0][0-2])$", re.I).match),
    ("ecl", re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$", re.I).match),
    ("eyr", re.compile(r"^([2][0][2][0-9]|[2][0][3][0])$", re.I).match),
    ("hcl", re.compile(r"^(#[\da-f]{6})$", re.I).match),
    ("hgt", re.compile(r"^([1][5-8][0-9]cm|[1][9][0-3]cm|[5][9]in|[6][0-9]in|[7][0-6]in)$", re.I).match),
    ("iyr", re.compile(r"^([2][0][1][0-9]|[2][0][2][0])$", re.I).match),
    ("pid", re.compile(r"^([\d]{9})$", re.I).match),
}


def split_batch(iterable, separators):
    """ Split a list each time we encounter an element matching any of the separator values provided. """
    group = []
    for x in iterable:
        if x not in separators:
            group.append(x)
        elif group:
            yield group
            group = []
    yield group


class Passport:
    def __init__(self, fields: dict):
        self.fields = fields

    def validate(self, validator):
        try:
            # validate fields using validator function
            return not [k for k, f in validator if not f(self.fields[k])]
        except KeyError:
            # fail immediately after encountering a missing field
            return False

    @staticmethod
    def from_batch(iterable) -> Passport:
        # convert batch data to Passport object
        field_list = list(" ".join(iterable).split(" "))
        field_dict = {name.lower(): value for name, value in [field.split(":", 1) for field in field_list]}
        return Passport(field_dict)


def answer(passports, validator):
    # merge individual passport fields into a single list
    parsed_passports = [Passport.from_batch(b) for b in split_batch(passports, [""]) if b]
    # return the passports that match the validator
    matched_passports = [p for p in parsed_passports if p.validate(validator)]
    return len(matched_passports)
