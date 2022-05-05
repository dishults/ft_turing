#!/usr/bin/env python3

import argparse
import sys

from json import JSONDecodeError

from utils import check_file_and_input
from turing_machine import print_machine_description_info, run_machine


def main(jsonfile, user_input):
    machine_description = check_file_and_input(jsonfile, user_input)
    print_machine_description_info(jsonfile, machine_description)
    run_machine(machine_description, user_input)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('jsonfile', help='json description of the machine')
    parser.add_argument('input', help='input of the machine')
    args = parser.parse_args()

    try:
        main(args.jsonfile, args.input)
    except (FileNotFoundError, JSONDecodeError) as err:
        sys.exit(
            "ERROR: make sure the file exists, it's not empty,"
            " has a name and a correct json format and structure,"
            " as well as all the necessary fields"
        )
    except Exception as err:
        sys.exit(f"ERROR: {err}")
