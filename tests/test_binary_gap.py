import pytest
from binary_gap import binaryGap


def test_valid_input_example_1():
    assert binaryGap(22) == 2

def test_valid_input_example_2():
    assert binaryGap(8) == 0

def test_valid_input_example_3():
    assert binaryGap(5) == 1

def test_no_adjacent_1s():
    assert binaryGap(1) == 0

def test_power_of_2():
    assert binaryGap(16) == 0

def test_all_1s():
    assert binaryGap(15) == 0

def test_leading_zeros():
    assert binaryGap(4) == 1

def test_trailing_zeros():
    assert binaryGap(12) == 1

def test_large_number_long_gap():
    assert binaryGap(529) == 4

def test_boundary_max_input():
    assert binaryGap(1073741824) == 0

def test_single_gap():
    assert binaryGap(9) == 2

def test_multiple_gaps_different_lengths():
    assert binaryGap(22) == 2
