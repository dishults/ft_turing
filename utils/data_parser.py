import json


def check_data(machine_description, user_input):
    assert machine_description, "machine description cannot be empty"
    assert user_input, "user input cannot be empty"


def check_file_and_input(filename, user_input):
    # Read file
    with open(filename, 'r') as json_file:
        machine_description = json.load(json_file)

    # Check for errors
    check_data(machine_description, user_input)

    # Return validated data
    return machine_description
