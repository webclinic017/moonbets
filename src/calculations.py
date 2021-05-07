from src import constants as cnst
from src import data_calls as dc
from src import data



def FCF_dataset(data: dict, ticker: str, period: str):
    """
        Test method produces the FCF. It returns a tuple with number of data sets and data available.
        It could return a maximum of 5 data sets
    """
    data = ()
    temp_data = {}
    index = 0
    cashflow_sheets = data[ticker][cnst.CASHFLOW.format(period)]
    for time_period in cashflow_sheets:
        temp_data[time_period['date']] = time_period['freeCashFlow']
        index+=1
    return data

def WACC_value(data: dict, ticker: str, period: str):
    """
    docstring
    """
    pass


def terminal_value(data: dict, ticker: str, period: str):
    """
    docstring
    """
    pass


def PV_future_cashflow(FCF_data: dict, discount_factor_value: int):
    """
    docstring
    """
    pass


def discount_factor(WACC_value: int, number_factors: int):
    """
    docstring
    """
    pass


def todays_stock_value(PV_value: dict):
    """
    docstring
    """
    pass


def fair_value_equity(data: dict, ticker: str, todays_value: int):
    """
    docstring
    """
    pass


