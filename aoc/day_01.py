from functools import reduce
from itertools import combinations


def answer(expenses: list, size: int, value: int):
    # find all combinations where the sum equals the value
    sequences = (e for e in combinations(expenses, size) if sum(e) == value)
    # return the product of the first combination
    for sequence in sequences:
        return reduce((lambda x, y: x * y), list(sequence))
    return 0
