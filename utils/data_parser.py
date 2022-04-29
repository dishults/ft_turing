import json


def get_field(machine_description, field):
    try:
        return machine_description[field]
    except KeyError:
        raise AssertionError(
            f"machine description is missing the '{field}' field")


def check_data(machine_description, user_input):

    #########################  CHECK MACHINE DESCRIPTION #########################

    assert machine_description, "machine description cannot be empty"

    # name
    name = get_field(machine_description, "name")
    assert type(name) == str and len(name),\
        "'name' field should be a non-empty string"

    # alphabet
    alphabet = get_field(machine_description, "alphabet")
    assert (
        type(alphabet) == list
        and len(alphabet)
        and all(type(symbol) == str and len(symbol) == 1 for symbol in alphabet)
        and len(alphabet) == len(set(alphabet))
    ), ("'alphabet' field should be a non-empty list of unique symbols."
        " Each symbol should consist of just 1 string character.")

    # blank
    blank = get_field(machine_description, "blank")
    assert blank in alphabet, "'blank' character must be part of the 'alphabet'"

    # states
    states = get_field(machine_description, "states")
    assert (
        type(states) == list
        and len(states)
        and all(type(state) == str and len(state) for state in states)
        and len(states) == len(set(states))
    ), ("'states' field should be a non-empty list of unique machine states."
        " Each state should be a non-empty string.")

    # initial
    initial = get_field(machine_description, "initial")
    assert initial in states, "'initial' state must be part of the 'states'"

    # finals
    finals = get_field(machine_description, "finals")
    assert (
        type(finals) == list
        and len(finals)
        and all(final_state in states for final_state in finals)
        and len(finals) == len(set(finals))
        and len(finals) < len(states)
    ), ("'finals' field should be a non-empty list of unique final states."
        " Each final state must be part of the 'states'."
        " Number of final states should be less then the number of 'states'.")

    # transitions
    transitions = get_field(machine_description, "transitions")
    assert (
        type(transitions) == dict
        and transitions.keys() == {state for state in states if state not in finals}
    ), ("'transitions' field should be a dictionary of state transitions."
        " The dictionary's keys should be part of the 'states'"
        " and shouldn't be part of the 'finals'")
    for state_name, state_transitions in transitions.items():
        assert (
            type(state_transitions) == list
            and len(state_transitions)
            and all(
                type(state_transition) == dict
                and state_transition.keys() == {"read", "to_state", "write", "action"}
                for state_transition in state_transitions
            )
        ), ("TODO")

        read_values = [state_transition["read"]
                       for state_transition in state_transitions]
        assert len(read_values) == len(set(read_values)),\
            f"'{state_name}' transition contains duplicate 'read' field values"

    ######################### CHECK USER INPUT #########################

    assert user_input, "user input cannot be empty"
    assert blank not in user_input, "user input cannot include a 'blank' character"


def check_file_and_input(filename, user_input):
    # Read file
    with open(filename, 'r') as json_file:
        machine_description = json.load(json_file)

    # Check for errors
    check_data(machine_description, user_input)

    # Return validated data
    return machine_description
