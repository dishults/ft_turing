import pytest
import json

import ft_turing
from copy import deepcopy

from utils import check_data


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


def test_files(user_input):
    with pytest.raises(json.JSONDecodeError):
        ft_turing.main('test_descriptions/error_empty.json', user_input)
    with pytest.raises(AssertionError):
        ft_turing.main('test_descriptions/error_incomplete.json', user_input)


def test_machine_description(machine_description, user_input):
    with pytest.raises(AssertionError):
        desctiption_copy = deepcopy(machine_description)
        desctiption_copy.pop('states')
        check_data(desctiption_copy, user_input)


def test_name(machine_description, user_input):
    with pytest.raises(AssertionError):
        desctiption_copy = deepcopy(machine_description)
        desctiption_copy["name"] = ""
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["name"] = 15
        check_data(desctiption_copy, user_input)


def test_alphabet(machine_description, user_input):
    with pytest.raises(AssertionError):
        desctiption_copy = deepcopy(machine_description)
        desctiption_copy["alphabet"].append(desctiption_copy["alphabet"][0])
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["alphabet"] = ""
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["alphabet"] = []
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["alphabet"] = ["1", 2]
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["alphabet"] = ["1", "22"]
        check_data(desctiption_copy, user_input)


def test_blank(machine_description, user_input):
    with pytest.raises(AssertionError):
        desctiption_copy = deepcopy(machine_description)
        desctiption_copy["blank"] = 1
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["blank"] = "2"
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["blank"] = "11"
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["blank"] = ["1", "."]
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        check_data(machine_description, '')


def test_states(machine_description, user_input):
    with pytest.raises(AssertionError):
        desctiption_copy = deepcopy(machine_description)
        desctiption_copy["states"].append(desctiption_copy["states"][0])
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["states"] = 1
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy = deepcopy(machine_description)
        desctiption_copy["states"] = []
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy = deepcopy(machine_description)
        desctiption_copy["states"] = ["scanright", ""]
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy = deepcopy(machine_description)
        desctiption_copy["states"] = ["scanright", 1]
        check_data(desctiption_copy, user_input)


def test_initial(machine_description, user_input):
    with pytest.raises(AssertionError):
        desctiption_copy = deepcopy(machine_description)
        desctiption_copy["initial"] = ""
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["initial"] = ["scanright"]
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["initial"] = 1
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["initial"] = "unknownstate"
        check_data(desctiption_copy, user_input)


def test_finals(machine_description, user_input):
    with pytest.raises(AssertionError):
        desctiption_copy = deepcopy(machine_description)
        desctiption_copy["finals"].append(desctiption_copy["finals"][0])
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["finals"] = "HALT"
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["finals"] = []
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["finals"] = ["HALT", "unknown_state"]
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["finals"] = desctiption_copy["states"]
        check_data(desctiption_copy, user_input)


def test_transitions(machine_description, user_input):
    with pytest.raises(AssertionError):
        desctiption_copy = deepcopy(machine_description)
        desctiption_copy["transitions"]["HALT"] = desctiption_copy["transitions"]["skip"]
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy = deepcopy(machine_description)
        desctiption_copy["transitions"]["unexpected_transition"] = desctiption_copy["transitions"]["skip"]
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["transitions"].pop("scanright")
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["transitions"].pop(
            "unexpected_transition")
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["transitions"] = "scanright"
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["transitions"] = {}
        check_data(desctiption_copy, user_input)


def test_transition(machine_description, user_input, state_transition):
    with pytest.raises(AssertionError):
        desctiption_copy = deepcopy(machine_description)
        desctiption_copy["transitions"]["subone"] = []
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["transitions"]["subone"] = "read"
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["transitions"]["subone"] = state_transition
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["transitions"]["subone"] = []
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["transitions"]["subone"] = [state_transition, "read"]
        check_data(desctiption_copy, user_input)


def test_state_transitions(machine_description, user_input, state_transition):
    with pytest.raises(AssertionError):
        desctiption_copy = deepcopy(machine_description)
        desctiption_copy["transitions"]["subone"] = [state_transition, {
            "read": state_transition["read"], "to_state": "HALT", "write": ".", "action": "LEFT"
        }]
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy = deepcopy(machine_description)
        desctiption_copy["transitions"]["subone"][1] = {}
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy = deepcopy(machine_description)
        desctiption_copy["transitions"]["subone"][0].pop("write")
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy = deepcopy(machine_description)
        desctiption_copy["transitions"]["subone"][0]["rewrite"] = "UP"
        check_data(desctiption_copy, user_input)


def test_user_input(machine_description, user_input):
    with pytest.raises(AssertionError):
        ft_turing.main('machine_descriptions/unary_sub.json', '')
    with pytest.raises(AssertionError):
        check_data(machine_description, user_input + '.')
