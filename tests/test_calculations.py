import sys
import os


sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.calculations import *
from src.data  import load_data


all_data = load_data('all_data')


def test_FCF_dataset():
    result = calculate_fcf_dataset(all_data, 'BABA', 'annual')
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


def test_calculate_wacc_value():
    wacc_result = calculate_wacc_value(all_data, 'BABA', 'annual')
    assert wacc_result == 6.365228830736834
    

def test_calculatediscount_factor():
    wacc_result = calculate_wacc_value(all_data, 'BABA', 'annual')
    discount_fact = calculate_discount_factor(wacc_result, 4)
    assert len(discount_fact) == 4
    discount_fact = calculate_discount_factor(wacc_result, 10)
    assert len(discount_fact) == 10