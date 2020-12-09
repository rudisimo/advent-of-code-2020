import os

import pytest
import yaml


def load_fixture_data(name):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "fixtures", f"{name}.yaml")
    with open(filename, "r") as f:
        return yaml.load(f, Loader=yaml.SafeLoader)
    return {}


@pytest.fixture(scope="module")
def fixtures(request):
    return load_fixture_data(*request.module.__name__.split(".")[-1:])
