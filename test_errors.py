import pytest

from json import JSONDecodeError

import ft_turing


def test_parser():
    with pytest.raises(JSONDecodeError):
        ft_turing.main('machine_descriptions/error_empty.json', '111-11=')
    with pytest.raises(AssertionError):
        ft_turing.main('machine_descriptions/error_incomplete.json', '111-11=')
    with pytest.raises(AssertionError):
        ft_turing.main('machine_descriptions/unary_sub.json', '')
