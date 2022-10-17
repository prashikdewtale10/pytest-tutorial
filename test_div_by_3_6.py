import pytest

# @pytest.fixture  importing from conftest.py file

def input_value():
    inp = 24
    return inp

def test_divi_by_3(input_value):
    assert input_value % 3 == 0

def test_divi_by_6(input_value):
    assert input_value % 6 == 0

