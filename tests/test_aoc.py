from __future__ import annotations

import importlib
from functools import lru_cache
from glob import glob
from pathlib import Path
from typing import List, Tuple

import pytest


@lru_cache()
def get_fixtures(day: int, part: int) -> Tuple[List[str], Tuple[str, str]]:
    fixtures = glob(f"{Path().absolute()}/tests/fixtures/{day:0{2}}*.txt")
    for fixture in fixtures:
        try:
            with open(fixture) as f:
                samples = f.read().split("---------------------\n")
        except FileNotFoundError:
            yield ([], ("", ""))
        else:
            yield (samples[0].splitlines(), (samples[1].strip(), samples[2].strip()))
    if not fixtures:
        raise FileNotFoundError(f"no fixtures: tests/fixtures/{day:0{2}}*.txt")


def parameter_label(name):
    def wrapper(val):
        return f"{name}+{val}"

    return wrapper


def solve(day: int, part: int, input: List[str]) -> str:
    try:
        solver = getattr(importlib.import_module(f"aoc.day_{day:0{2}}"), f"answer{part}")
    except (AttributeError, ModuleNotFoundError):
        raise NotImplementedError(f"no implementation: aoc.day_{day:0{2}}:answer{part}")
    else:
        return str(solver(input))


@pytest.mark.parametrize("part", [1, 2])
@pytest.mark.parametrize("day", range(1, 25))
def test_solutions(day: int, part: int) -> None:
    try:
        fixtures = get_fixtures(day, part)
        for (input, expected) in fixtures:
            assert solve(day, part, input) == expected[part - 1]
    except (FileNotFoundError, NotImplementedError) as e:
        pytest.skip(f"Skipping {day}.{part} ({e})")
