from functools import reduce
from itertools import combinations
from typing import Iterator, List


def calculate_total(expenses: Iterator[int], length: int, total: int) -> int:
    sequences = {e for e in combinations(expenses, length) if sum(e) == total}
    for sequence in sequences:
        return reduce((lambda x, y: x * y), list(sequence))
    return 0


def answer1(input: List[str]) -> int:
    expenses = map(int, input)
    return calculate_total(expenses, length=2, total=2020)


def answer2(input: List[str]) -> int:
    expenses = map(int, input)
    return calculate_total(expenses, length=3, total=2020)
