import pytest
import math

"""
here all the 3 test will be failed but we are stopping the test after one failutre
using --maxfail 1
"""

def test_sqrt_failure():
    num = 25
    assert math.sqrt(num) == 6

def test_square_failure():
    num = 7
    assert num*num == 40

def test_equality_failure():
    assert 10 == 11