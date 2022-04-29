import pytest
import json

import ft_turing

from utils import check_data


@pytest.fixture
def machine_description():
    with open('machine_descriptions/unary_sub.json', 'r') as json_file:
        return json.load(json_file)


@pytest.fixture
def user_input():
    return '111-11='


def test_files(user_input):
    with pytest.raises(json.JSONDecodeError):
        ft_turing.main('test_descriptions/error_empty.json', user_input)
    with pytest.raises(AssertionError):
        ft_turing.main('test_descriptions/error_incomplete.json', user_input)


def test_machine_description(machine_description, user_input):
    with pytest.raises(AssertionError):
        desctiption_copy = machine_description.copy()
        desctiption_copy.pop('states')
        check_data(desctiption_copy, user_input)

    with pytest.raises(AssertionError):
        desctiption_copy = machine_description.copy()
        desctiption_copy["name"] = ""
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["name"] = 15
        check_data(desctiption_copy, user_input)

    with pytest.raises(AssertionError):
        desctiption_copy = machine_description.copy()
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

    with pytest.raises(AssertionError):
        desctiption_copy = machine_description.copy()
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

    with pytest.raises(AssertionError):
        desctiption_copy = machine_description.copy()
        desctiption_copy["states"] = 1
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy = machine_description.copy()
        desctiption_copy["states"] = []
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy = machine_description.copy()
        desctiption_copy["states"] = ["scanright", ""]
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy = machine_description.copy()
        desctiption_copy["states"] = ["scanright", 1]
        check_data(desctiption_copy, user_input)

    with pytest.raises(AssertionError):
        desctiption_copy = machine_description.copy()
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

    with pytest.raises(AssertionError):
        desctiption_copy = machine_description.copy()
        desctiption_copy["finals"] = "HALT"
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["finals"] = []
        check_data(desctiption_copy, user_input)
    with pytest.raises(AssertionError):
        desctiption_copy["finals"] = ["HALT", "unknownstate"]
        check_data(desctiption_copy, user_input)


def test_user_input(machine_description, user_input):
    with pytest.raises(AssertionError):
        ft_turing.main('machine_descriptions/unary_sub.json', '')
    with pytest.raises(AssertionError):
        check_data(machine_description, user_input + '.')
