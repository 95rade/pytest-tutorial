import pytest
import math

def test_sqrt_failure():
    '''
    num = 6
    '''
    num = input('Enter number ')
    assert math.sqrt(num) == 6
def test_square_failure():
    num=7
    assert 7*7 == 40
def test_equality_failure():
    assert 10 == 11