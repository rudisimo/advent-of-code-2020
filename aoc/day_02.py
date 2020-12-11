import re
from typing import List

POLICY_RE = re.compile(r"^(?P<lower>\d+)-(?P<upper>\d+)\s+(?P<character>\w):\s(?P<password>.*)$", flags=re.I)


def answer1(input: List[str]) -> int:
    count = 0
    for policy in input:
        (minimum, maximum, character, password) = POLICY_RE.findall(policy)[0]
        if int(minimum) <= password.count(character) <= int(maximum):
            count += 1
    return count


def answer2(input: List[str]) -> int:
    count = 0
    for policy in input:
        (first_pos, second_pos, character, password) = POLICY_RE.findall(policy)[0]
        first_match = password[int(first_pos) - 1] == character
        last_match = password[int(second_pos) - 1] == character
        if first_match ^ last_match:
            count += 1
    return count
