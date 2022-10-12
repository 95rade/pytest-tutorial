import pytest

@pytest.fixture
def input_value():
    input = 36
    #input = int(input('Enter number:\n'))
    """ pytest -s would invoke user input """
    return input