import re


def filter_by_frequency(match):
    min, max, character, password = match.groups()
    # find all matching characters
    matches = re.findall(rf"{character}", password, flags=re.IGNORECASE)
    # validate range via interval comparison
    if int(min) <= len(matches) <= int(max):
        return True
    return False


def filter_by_position(match):
    min, max, character, password = match.groups()
    # match password character at first position
    try:
        first = password[int(min) - 1] == character
    except IndexError:
        first = False
    # match password character at last position
    try:
        last = password[int(max) - 1] == character
    except IndexError:
        last = False
    # XOR first and last password character matches
    return first ^ last


def answer(policies, filter):
    policy_re = re.compile(r"(?P<min>\d+)-(?P<max>\d+)\s+(?P<character>\w):\s(?P<password>.*)", flags=re.IGNORECASE)
    matched_policies = [p for p in policies if filter(policy_re.match(p))]
    return len(matched_policies)
