from utils import get_terminal_size, get_file_name, strigify_array, wrap_string


def stringify_transition(state_name, state_transition):
    return(f"({state_name}, {state_transition['read']}) -> "
           f"({state_transition['to_state']}, {state_transition['write']}, "
           f"{state_transition['action']})")


def print_machine_description_info(md_name, machine_description):
    columns, lines = get_terminal_size()
    md_name = get_file_name(md_name)

    # Name
    print(wrap_string(md_name, columns))

    # Machine description
    print(f"Alphabet: {strigify_array(machine_description['alphabet'])}",
          f"States: {strigify_array(machine_description['states'])}",
          f"Initial: {machine_description['initial']}",
          f"Finals: {strigify_array(machine_description['finals'])}", sep='\n')

    # Transitions
    for state_name, state_transitions in machine_description["transitions"].items():
        for state_transition in state_transitions:
            print(stringify_transition(state_name, state_transition))

    print('*' * columns)
