import json
import os
import re

import pytest


def load_resources():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "test_resources.json")
    with open(filename, "r") as f:
        return json.load(f)


@pytest.fixture(scope="module")
def resources(request):
    return load_resources().get(request.module.__name__)
