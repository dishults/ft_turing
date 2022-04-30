import pytest
import json


@pytest.fixture
def machine_description():
    with open('machine_descriptions/unary_sub.json', 'r') as json_file:
        return json.load(json_file)


@pytest.fixture
def user_input():
    return '111-11='


@pytest.fixture
def state_transition():
    return {"read": "1", "to_state": "subone", "write": "=", "action": "LEFT"}
