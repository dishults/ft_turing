import ft_turing
from copy import deepcopy

from utils import check_data
from test_resources import *


class TestErrorMachineDescription:

    def test_files(self, user_input):
        with pytest.raises(json.JSONDecodeError):
            ft_turing.main('test_resources/error_empty.json', user_input)
        with pytest.raises(json.JSONDecodeError):
            ft_turing.main(
                'test_resources/error_wrong_structure.json', user_input)
        with pytest.raises(json.JSONDecodeError):
            ft_turing.main('test_resources/unary_sub.py', user_input)
        with pytest.raises(json.JSONDecodeError):
            ft_turing.main('test_resources/.json', user_input)
        with pytest.raises(json.JSONDecodeError):
            ft_turing.main('test_errors.py', user_input)
        with pytest.raises(AssertionError):
            ft_turing.main('test_resources/error_incomplete.json', user_input)

    def test_machine_description(self, machine_description, user_input):
        with pytest.raises(AssertionError):
            desctiption_copy = deepcopy(machine_description)
            desctiption_copy.pop('states')
            check_data(desctiption_copy, user_input)

    def test_name(self, machine_description, user_input):
        with pytest.raises(AssertionError):
            desctiption_copy = deepcopy(machine_description)
            desctiption_copy["name"] = ""
            check_data(desctiption_copy, user_input)
        with pytest.raises(AssertionError):
            desctiption_copy["name"] = 15
            check_data(desctiption_copy, user_input)

    def test_alphabet(self, machine_description, user_input):
        with pytest.raises(AssertionError):
            desctiption_copy = deepcopy(machine_description)
            desctiption_copy["alphabet"].append(
                desctiption_copy["alphabet"][0])
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

    def test_blank(self, machine_description, user_input):
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

    def test_states(self, machine_description, user_input):
        with pytest.raises(AssertionError):
            desctiption_copy = deepcopy(machine_description)
            desctiption_copy["states"].append(desctiption_copy["states"][0])
            check_data(desctiption_copy, user_input)
        with pytest.raises(AssertionError):
            desctiption_copy = deepcopy(machine_description)
            state = desctiption_copy["states"][0]
            desctiption_copy["states"] = [state]
            desctiption_copy["finals"] = [state]
            desctiption_copy["transitions"] = {
                state: desctiption_copy["transitions"][state]
            }
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

    def test_initial(self, machine_description, user_input):
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

    def test_finals(self, machine_description, user_input):
        with pytest.raises(AssertionError):
            desctiption_copy = deepcopy(machine_description)
            desctiption_copy["finals"].append(desctiption_copy["finals"][0])
            check_data(desctiption_copy, user_input)
        with pytest.raises(AssertionError):
            desctiption_copy["finals"] = [
                desctiption_copy["finals"][0], desctiption_copy["states"][0]
            ]
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

    def test_unhashable(self, machine_description, user_input):
        unhashable_variable = {"1": 1}

        for field in {"name", "alphabet", "blank", "states", "initial", "finals"}:
            with pytest.raises(AssertionError):
                desctiption_copy = deepcopy(machine_description)
                desctiption_copy[field] = unhashable_variable
                check_data(desctiption_copy, user_input)

        for field in ("alphabet", "finals", "states"):
            with pytest.raises(AssertionError):
                desctiption_copy = deepcopy(machine_description)
                desctiption_copy[field][-1] = unhashable_variable
                check_data(desctiption_copy, user_input)

        desctiption_copy = deepcopy(machine_description)
        desctiption_copy["transitions"]["scanright"] = unhashable_variable

        for key in {"read", "to_state", "write", "action"}:
            with pytest.raises(AssertionError):
                desctiption_copy = deepcopy(machine_description)
                desctiption_copy["transitions"]["scanright"][0][key] = unhashable_variable
                check_data(desctiption_copy, user_input)


class TestErrorTransition:

    def test_transitions(self, machine_description, user_input):
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

    def test_transition(self, machine_description, user_input, state_transition):
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
            desctiption_copy["transitions"]["subone"] = [
                state_transition, "read"]
            check_data(desctiption_copy, user_input)

    def test_state_transitions(self, machine_description, user_input):
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

    def test_state_transition(self, machine_description, user_input):
        for readwrite in ("read", "write"):
            with pytest.raises(AssertionError):
                desctiption_copy = deepcopy(machine_description)
                desctiption_copy["transitions"]["subone"][0][readwrite] = 1
                check_data(desctiption_copy, user_input)
            with pytest.raises(AssertionError):
                desctiption_copy = deepcopy(machine_description)
                desctiption_copy["transitions"]["subone"][0][readwrite] = "2"
                check_data(desctiption_copy, user_input)

        with pytest.raises(AssertionError):
            desctiption_copy = deepcopy(machine_description)
            desctiption_copy["transitions"]["subone"][0]["to_state"] = "unknown_state"
            check_data(desctiption_copy, user_input)
        with pytest.raises(AssertionError):
            desctiption_copy = deepcopy(machine_description)
            desctiption_copy["transitions"]["subone"][0]["to_state"] = None
            check_data(desctiption_copy, user_input)

        with pytest.raises(AssertionError):
            desctiption_copy = deepcopy(machine_description)
            desctiption_copy["transitions"]["subone"][0]["action"] = None
            check_data(desctiption_copy, user_input)
        with pytest.raises(AssertionError):
            desctiption_copy = deepcopy(machine_description)
            desctiption_copy["transitions"]["subone"][0]["action"] = "UP"
            check_data(desctiption_copy, user_input)
        with pytest.raises(AssertionError):
            desctiption_copy = deepcopy(machine_description)
            desctiption_copy["transitions"]["subone"][0]["action"] = "left"
            check_data(desctiption_copy, user_input)

    def test_read_values(self, machine_description, user_input, state_transition):
        with pytest.raises(AssertionError):
            desctiption_copy = deepcopy(machine_description)
            desctiption_copy["transitions"]["subone"] = [state_transition, {
                "read": state_transition["read"], "to_state": "HALT", "write": ".", "action": "LEFT"
            }]
            check_data(desctiption_copy, user_input)

    def test_interstate_transitions(self, machine_description, user_input):
        with pytest.raises(AssertionError):
            desctiption_copy = deepcopy(machine_description)
            desctiption_copy["transitions"]["eraseone"][1]["to_state"] = "scanright"
            check_data(desctiption_copy, user_input)
        with pytest.raises(AssertionError):
            desctiption_copy = deepcopy(machine_description)
            desctiption_copy["transitions"]["subone"][1]["to_state"] = "scanright"
            check_data(desctiption_copy, user_input)
        with pytest.raises(AssertionError):
            desctiption_copy = deepcopy(machine_description)
            new_state = "new_state"
            desctiption_copy["states"].append(new_state)
            desctiption_copy["finals"].append(new_state)
            check_data(desctiption_copy, user_input)


class TestErrorUserInput:

    def test_user_input(self, machine_description, user_input):
        with pytest.raises(AssertionError):
            ft_turing.main('machine_descriptions/unary_sub.json', '')
        with pytest.raises(AssertionError):
            check_data(machine_description, user_input + '.')
        with pytest.raises(AssertionError):
            check_data(machine_description, user_input + '2')
