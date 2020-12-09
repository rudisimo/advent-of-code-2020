import re

policy_re = re.compile(r"^(\d+)-(\d+)\s+(\w):\s(.*)$", flags=re.IGNORECASE)


def filter_by_frequency(low, high, character, password):
    # find all matching characters
    matches = re.findall(rf"[{character}]", password, flags=re.IGNORECASE)
    # validate range via interval comparison
    if int(low) <= len(matches) <= int(high):
        return True
    return False


def filter_by_position(first, second, character, password):
    # match character at first password position
    try:
        first_match = password[int(first) - 1] == character
    except IndexError:
        first_match = False
    # match character at second password position
    try:
        second_match = password[int(second) - 1] == character
    except IndexError:
        second_match = False
    # XOR first and second password character matches due to constraints
    return first_match ^ second_match


def answer(policies, filter):
    # parse each password policy into its separate components
    parsed_policies = (policy_re.match(p).groups() for p in policies if policy_re.match(p))
    # return the password policies that match the filter
    matched_policies = [p for p in parsed_policies if filter(*p) == True]
    return len(matched_policies)
