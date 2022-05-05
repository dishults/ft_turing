from utils import get_terminal_size, get_file_name, strigify_array, wrap_string


def print_machine_description_info(md_name, machine_description):
    columns, lines = get_terminal_size()
    md_name = get_file_name(md_name)

    # Name
    print(wrap_string(md_name, columns))

    # Machine description
    print(f"Alphabet: {strigify_array(machine_description['alphabet'])}")
    print(f"States: {strigify_array(machine_description['states'])}")
    print(f"Initial: {machine_description['initial']}")
    print(f"Finals: {strigify_array(machine_description['finals'])}")

    # Transitions
    for state_name, state_transitions in machine_description["transitions"].items():
        for state_transition in state_transitions:
            print(f"({state_name}, {state_transition['read']}) -> "
                  f"({state_transition['to_state']}, {state_transition['write']}, "
                  f"{state_transition['action']})")

    print('*' * columns)


def run_machine(machine_description, user_input):
    pass
