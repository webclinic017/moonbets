import sys
import os


sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.data import load_data
from src.calculations import *
from src.data_calls import technicals


all_data = load_data('all_data')
# all_data =  technicals({'AAPL':{}})
# period = 'annual'
# ticker = 'AAPL'

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


def test_calculate_discount_factor():
    wacc_result = calculate_wacc_value(all_data, 'BABA', 'annual')
    discount_fact = calculate_discount_factor(wacc_result, 4)
    assert len(discount_fact) == 4
    discount_fact = calculate_discount_factor(wacc_result, 10)
    assert len(discount_fact) == 10


def test_calculate_fcf_terminal_value():
    terminal_value_result = calculate_fcf_terminal_value(all_data, 'BABA', 'annual')
    assert terminal_value_result == 3585855613458.678


def test_calculate_pv_future_cashflow():
    fcf_result = calculate_fcf_dataset(all_data, 'BABA', 'annual')
    for value in fcf_result:
        assert value > 135221000000
    wacc_result = calculate_wacc_value(all_data, 'BABA', 'annual')
    discount_fact = calculate_discount_factor(wacc_result, 4)
    assert len(discount_fact) == 4
    terminal_value_result = calculate_fcf_terminal_value(all_data, 'BABA', 'annual')
    assert terminal_value_result == 3585855613458.678
    future_cashflow = calculate_pv_future_cashflow(fcf_result,
                                                   terminal_value_result,
                                                   discount_fact)
    assert len(future_cashflow) == 5


def test_todays_stock_value():
    fcf_result = calculate_fcf_dataset(all_data, 'BABA', 'annual')
    for value in fcf_result:
        assert value > 135221000000
    wacc_result = calculate_wacc_value(all_data, 'BABA', 'annual')
    discount_fact = calculate_discount_factor(wacc_result, 4)
    assert len(discount_fact) == 4
    terminal_value_result = calculate_fcf_terminal_value(all_data, 'BABA', 'annual')
    assert terminal_value_result == 3585855613458.678
    future_cashflow = calculate_pv_future_cashflow(fcf_result,
                                                   terminal_value_result,
                                                   discount_fact)
    add_test_result = 0
    for pv_value in future_cashflow:
        add_test_result += pv_value
    todays_stock_value = calculate_todays_stock_value(future_cashflow)
    assert todays_stock_value == add_test_result


def test_fair_value_equity():
    fcf_result = calculate_fcf_dataset(all_data, 'BABA', 'annual')
    for value in fcf_result:
        assert value > 135221000000
    wacc_result = calculate_wacc_value(all_data, 'BABA', 'annual')
    discount_fact = calculate_discount_factor(wacc_result, 4)
    assert len(discount_fact) == 4
    terminal_value_result = calculate_fcf_terminal_value(all_data, 'BABA', 'annual')
    assert terminal_value_result == 3585855613458.678
    future_cashflow = calculate_pv_future_cashflow(fcf_result,
                                                   terminal_value_result,
                                                   discount_fact)
    add_test_result = 0
    for pv_value in future_cashflow:
        add_test_result += pv_value
    todays_stock_value = calculate_todays_stock_value(future_cashflow)
    assert todays_stock_value == add_test_result
    fair_value = calculate_fair_value_equity(all_data, 'BABA', 'annual', todays_stock_value)
    assert fair_value > 0
