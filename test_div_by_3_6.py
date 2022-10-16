import pytest

"""
@pytest.fixture
def input_value():
    input=39
    return input
# CONFTEST.PY HAS THE FIXTURE FUNCTION
"""
# pytest -k divisible -v -s  --> WILL CALL INPUT_VALUE DEFINED IN @pytest.fixture FUNCTION TO ASSERT TESTS CONTAINING DIVISIBLE WORD
def test_divisible_by_3(input_value):
    assert input_value % 3 == 0

def test_divisible_by_6(input_value):
    assert input_value % 6 == 0