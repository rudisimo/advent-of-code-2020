import json
import os
import re

import pytest


def load_resources(name):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, f'{name}.json')
    with open(filename, 'r') as f:
        return json.load(f)


@pytest.fixture(scope='module')
def resources(request):
    return load_resources(*request.module.__name__.split('.')[-1:])
