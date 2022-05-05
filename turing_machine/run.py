from utils import highlight, strigify_array

from .describe import stringify_transition


def get_transitions_dict(transitions):
    transitions_dict = {}
    for state_name, state_transitions in transitions.items():
        transitions_dict[state_name] = {}
        for state_transition in state_transitions:
            read = state_transition["read"]
            transitions_dict[state_name][read] = state_transition
    return transitions_dict


def stringify_tape(tape, i, blank, max_length=20):
    tape[i] = highlight(tape[i])
    if len(tape) < max_length:
        tape += [blank] * (max_length - len(tape))
    elif len(tape) > max_length:
        # TODO truncate
        pass
    return strigify_array(tape, sep='', padding='')


def run_machine(md, tape):
    state = md["initial"]
    finals = set(md["finals"])
    transitions = get_transitions_dict(md["transitions"])
    tape = list(tape)
    i = 0
    while i >= 0 and i <= len(tape):
        read = tape[i]
        transition = transitions[state][read]
        print(stringify_tape(tape, i, md["blank"]),
              stringify_transition(state, transition))
        tape[i] = transition["write"]
        state = transition["to_state"]

        if transition["action"] == "RIGHT":
            i += 1
        else:
            i -= 1

        if state in finals:
            break

    if state not in finals:
        raise RuntimeError("\n - ".join([
            "End of tape.",
            f"tape: {tape}",
            f"state: {state}",
            f"didn't reach any of the final states: {md['finals']}",
        ]))
