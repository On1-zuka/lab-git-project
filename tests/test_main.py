from src import add_numbers, multiply_numbers


def test_add_numbers(a, b):
    assert add_numbers(2, 4) == 6


def test_multiply_numbers(a, b):
    assert multiply_numbers(2, 2) == 4
