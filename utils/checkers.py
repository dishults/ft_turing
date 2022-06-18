import json
import os

from copy import deepcopy

from .utils import *


def check_transitions(transitions, alphabet, states, finals):
    transitions_required_keys = states - finals
    transition_required_keys = {"read", "to_state", "write", "action"}
    allowed_actions = {"LEFT", "RIGHT"}
    interstate_transitions = set()

    # transitions
    assert (
        type(transitions) == dict
        and transitions.keys() == transitions_required_keys
    ), value_error('transitions', None, [
        f"should be a dictionary with the following keys: {transitions_required_keys}",
    ])

    for state_name, state_transitions in transitions.items():
        # state transitions
        assert (
            type(state_transitions) == list
            and len(state_transitions)
        ), (f"transition for the {highlight(state_name)} state should be"
            " a non-empty list of dictionaries")

        # state transition
        for state_transition in state_transitions:
            assert (
                type(state_transition) == dict
                and state_transition.keys() == transition_required_keys
            ), value_error('transition', state_transition, [
                f"should be a dictionary with the following keys: {transition_required_keys}",
            ])

            # read and write
            for readwrite in ("read", "write"):
                value = state_transition[readwrite]
                assert type(value) == str and value in alphabet, value_error(readwrite, value, [
                    f" should be a part of the 'alphabet': {alphabet}",
                ])

            # to_state
            to_state = state_transition["to_state"]
            assert type(to_state) == str and to_state in states, value_error('to_state', to_state, [
                f" should be a part of the 'states': {states}",
            ])
            if to_state != state_name:
                interstate_transitions.add(to_state)

            # action
            action = state_transition["action"]
            assert type(action) == str and action in allowed_actions, value_error('action', action, [
                f" should be either of those: {allowed_actions}",
            ])

        # unique 'read' values
        read_values = [state_transition["read"]
                       for state_transition in state_transitions]
        assert len(read_values) == len(set(read_values)),\
            f"'{state_name}' transition contains duplicate 'read' field values"

    # interstate transitions
    missing_interstate_transitions = states - interstate_transitions
    assert len(states - finals) == 1 or not missing_interstate_transitions,\
        (f"'transitions' is missing the following interstate {highlight('to_state')}"
         f" transition(s): {missing_interstate_transitions}")


def check_data(machine_description, user_input):
    machine_description = deepcopy(machine_description)

    #########################  CHECK MACHINE DESCRIPTION #########################

    assert machine_description, "machine description cannot be empty"

    # name
    name = get_field(machine_description, "name")
    assert type(name) == str and len(name), value_error('name', name, [
        "should be a non-empty string",
    ])

    # alphabet
    alphabet = get_field(machine_description, "alphabet")
    assert (
        type(alphabet) == list
        and len(alphabet)
        and all(type(symbol) == str and len(symbol) == 1 for symbol in alphabet)
        and len(alphabet) == len(set(alphabet))
    ), value_error('alphabet', alphabet, [
        "should be a non-empty list of unique symbols",
        "each symbol should consist of just 1 string character",
    ])
    alphabet = set(alphabet)

    # blank
    blank = get_field(machine_description, "blank")
    assert type(blank) == str and blank in alphabet, value_error('blank', blank, [
        f"should be a part of the 'alphabet': {alphabet}",
    ])

    # states
    states = get_field(machine_description, "states")
    assert (
        type(states) == list
        and len(states) > 1
        and all(type(state) == str and len(state) for state in states)
        and len(states) == len(set(states))
    ), value_error('states', states, [
        "should be a list of at least 2 machine states",
        "each state should be a unique non-empty string",
    ])
    states = set(states)

    # initial
    initial = get_field(machine_description, "initial")
    assert type(initial) == str and initial in states, value_error('initial', initial, [
        f"should be a part of the 'states': {states}",
    ])

    # finals
    finals = get_field(machine_description, "finals")
    assert (
        type(finals) == list
        and len(finals)
        and all(type(final_state) == str and final_state in states for final_state in finals)
        and len(finals) == len(set(finals))
        and initial not in finals
    ), value_error('finals', finals, [
        "should be a non-empty list of unique final states",
        f"each final state must be part of the 'states': {states}",
        f"final states can't containt the 'initial' state: {initial}",
    ])
    finals = set(finals)

    # transitions
    transitions = get_field(machine_description, "transitions")
    check_transitions(transitions, alphabet, states, finals)

    ######################### CHECK USER INPUT #########################

    assert (
        user_input
        and blank not in user_input
        and all(char in alphabet for char in set(user_input))
    ), value_error('user_input', user_input, [
        f"cannot be empty",
        f"cannot include a 'blank' character: {blank}",
        f"should be a part of the 'alphabet': {alphabet}",
    ])


def check_file_and_input(filename, user_input):
    # Check file format
    if not (type(filename) == str and filename.endswith('.json')):
        raise json.JSONDecodeError("", "", 0)

    # Read file
    with open(filename, 'r') as json_file:
        machine_description = json.load(json_file)

    # Check for errors
    check_data(machine_description, user_input)

    # Return validated data
    return machine_description
