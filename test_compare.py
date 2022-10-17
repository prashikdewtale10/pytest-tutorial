import pytest
# giving markers to test in groups

@pytest.mark.xfail
@pytest.mark.great
def test_greater():
    num = 100 
    assert num > 100


@pytest.mark.xfail  #will be executed but the result will not be printed
@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100


@pytest.mark.skip  #skipping this test.
@pytest.mark.others
def test_less():
    num = 100
    assert num < 200 