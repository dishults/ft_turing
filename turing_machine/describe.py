from utils import get_terminal_size, strigify_array, wrap_string


def stringify_transition(state_name, state_transition):
    return(f"({state_name}, {state_transition['read']}) -> "
           f"({state_transition['to_state']}, {state_transition['write']}, "
           f"{state_transition['action']})")


def print_machine_description_info(machine_description):
    columns, lines = get_terminal_size()

    # General machine description info
    print(wrap_string(machine_description['name'], columns),
          f"Alphabet: {strigify_array(machine_description['alphabet'])}",
          f"States: {strigify_array(machine_description['states'])}",
          f"Initial: {machine_description['initial']}",
          f"Finals: {strigify_array(machine_description['finals'])}", sep='\n')

    # Transitions info
    for state_name, state_transitions in machine_description["transitions"].items():
        for state_transition in state_transitions:
            print(stringify_transition(state_name, state_transition))

    print('*' * columns)
