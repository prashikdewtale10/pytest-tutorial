import pytest

# paramateirizing test to run the test against multiple sets of inputs.
@pytest.mark.parametrize("num , output",[(1,11),(2,22),(3,35),(4,44),])

def test_multi_11(num,output):
    assert 11 * num == output
