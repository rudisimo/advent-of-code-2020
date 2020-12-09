import itertools
from functools import reduce


def answer(expenses: list, size: int, value: int):
    # find all combinations where the sum equals the value
    combinations = (e for e in itertools.combinations(expenses, size) if sum(e) == value)
    # return the product of the first combination
    for combination in combinations:
        return reduce((lambda x, y: x * y), list(combination))
    return 0
