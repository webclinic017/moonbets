from dateutil.relativedelta import relativedelta
import datetime

from src import constants as cnst
from src import data_calls as dc
from src import data

def FCF_dataset(data: dict, ticker: str, period: str):
    """
        Function produces the FCF. It returns a tuple with number of data sets and data dict available.
        It could return a maximum of 5 data sets
    """
    # revenue
    incstm_sheet = data[ticker][cnst.INCOMESTATEMENT.format(period)]
    #free cash flow
    fcf_sheet = data[ticker][cnst.CASHFLOW.format(period)]
    # net profit margin
    ratio_sheet = data[ticker][cnst.RATIOS.format(period)]

    FCF_growth_data = growth_rate(fcf_sheet, 'freeCashFlow')
    revenue_growth_data = growth_rate(incstm_sheet, 'revenue')
    netprofitmargin_growth_data = growth_rate(incstm_sheet, 'netProfitMargin')
    
    revenue = list
    current_revenue = revenue_growth_data[1][0]
    for index in range(0,4):
        current_revenue = current_revenue * revenue_growth_data[0]
        revenue.append(current_revenue)

    net_income = list
    for index in range(0,4):
        net_income.append(revenue[index] * netprofitmargin_growth_data[0])
    
    FCF_predict = list
    for index in range(0,4):
        FCF_predict.append(revenue[index]*net_income[index])
    return (4, FCF_predict)


def growth_rate(data: list, data_key: str):
    """
        It takes a dict and a data key
        grabs lowest growth rate, grabbing 2 lowest closest to the mean. 
        it returns a dictionary with three entries: growth,
        dataset(list), set_length
    """
    index = 1
    temp_data = []
    lowest = 0
    lowest_positive = 0
    average = 0
    for time_period in data:
        if index == 5:
            break
        temp_data.append(time_period[data_key])
        if index == 1:
            lowest = time_period[data_key]
        if time_period[data_key] < lowest and index != 1:
            lowest = time_period[data_key]
        if lowest > 0:
            if lowest_positive == 0:
                lowest_positive = time_period[data_key]
            if time_period[data_key] < lowest_positive:
                lowest_positive = time_period[data_key]
        index +=1
        average += time_period[data_key]
    average += average/index
    # lowest positive in case lowest has a negative rate
    if lowest < 0:
        if average > 0 and average < lowest_positive:
            lowest = average
        else:
            lowest = lowest_positive
    return (lowest, temp_data, index)


def discount_factor(WACC_value: int, number_factors: int):
    """
    docstring
    """
    pass


def WACC_value(data: dict, ticker: str, period: str):
    """
        Funtion returns WACC value as an integer
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


