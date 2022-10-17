import pytest

"""
we are defining fixture function in this file to make it available / accessible in all the test file.
"""

@pytest.fixture
def input_value():
    num = 1020
    return num

