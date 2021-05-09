import sys
import os


sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.calculations import *
from src.data  import load_data

all_data = load_data('all_data')

def test_FCF_dataset():
    result = FCF_dataset(all_data, 'BABA', 'annual')
    for value in result:
        assert value > 135221000000

def test_difference_calculator():
    first = 0
    second = 1
    result = difference_calculator(first, second)
    assert result == 0
    first = 1
    second = -1
    result = difference_calculator(first, second)
    assert result == 2
    first = -1
    second = -1
    result = difference_calculator(first, second)
    assert result == 0

    