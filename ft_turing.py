#!/usr/bin/env python3

import argparse
from json import JSONDecodeError
import sys

from utils import check_file_and_input
from turing_machine import run_machine


def main(jsonfile, user_input):
    machine_description = check_file_and_input(jsonfile, user_input)
    run_machine(machine_description, user_input)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('jsonfile', help='json description of the machine')
    parser.add_argument('input', help='input of the machine')
    args = parser.parse_args()

    try:
        main(args.jsonfile, args.input)
    except (FileNotFoundError, JSONDecodeError) as exc:
        sys.exit(f"FILE ERROR: {exc}")
    except Exception as exc:
        sys.exit(f"ERROR: {exc}")
