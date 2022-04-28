#!/usr/bin/env python3

import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('jsonfile', help='json description of the machine')
    parser.add_argument('input', help='input of the machine')
    args = parser.parse_args()


if __name__ == "__main__":
    main()
