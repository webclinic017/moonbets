from dateutil.relativedelta import relativedelta
import datetime

from src import constants as cnst
from src import data_calls as dc
from src import data


def calculate_fcf_dataset(data: dict, ticker: str, period: str):
    """
        Function produces the FCF. It returns data dict with FCF.
        It could return a maximum of 5 data sets
    """
    # revenue
    incstm_sheet = data[ticker][cnst.INCOMESTATEMENT.format(period)]
    # free cash flow
    fcf_sheet = data[ticker][cnst.CASHFLOW.format(period)]
    # net profit margin
    ratio_sheet = data[ticker][cnst.RATIOS.format(period)]

    FCF_growth_data = calculate_growth_rate(fcf_sheet, 'freeCashFlow')
    revenue_growth_data = calculate_growth_rate(incstm_sheet, 'revenue')
    netprofitmargin_growth_data = calculate_growth_rate(ratio_sheet, 'netProfitMargin')

    revenue = []
    current_revenue = revenue_growth_data[1][0]
    for index in range(0, 4):
        current_revenue = current_revenue * (1+revenue_growth_data[0])
        revenue.append(current_revenue * (1+revenue_growth_data[0]))

    net_income = []
    for index in range(0, 4):
        net_income.append(revenue[index] * netprofitmargin_growth_data[0])

    FCF_predict = []
    for index in range(0, 4):
        FCF_predict.append((1+FCF_growth_data[0])*net_income[index])
    return FCF_predict


def calculate_growth_rate(data: list, data_key: str):
    """
        It takes a dict and a data key
        grabs lowest growth rate, grabbing 2 lowest closest to the mean. 
        it returns a dictionary with three entries: growth,
        dataset(list), set_length
    """
    index = 0
    temp_data = []
    lowest = 0
    lowest_list = []
    average = 0

    # get data from sheet
    for time_period in data:
        if index == 6:
            break
        temp_data.append(time_period[data_key])
        index += 1

    # lowest value
    for range_index in range(0, index-1):
        temp = difference_calculator(temp_data[range_index], temp_data[range_index+1])
        lowest_list.append(temp)
        if range_index == 0:
            lowest = temp
        if temp < lowest and range_index != 0:
            lowest = temp
        average += temp
    average += average/(index-1)

    # lowest positive in case lowest has a negative rate
    if lowest < 0:
        positve_lowest = 0
        for gr_per_year in lowest_list:
            if positve_lowest == 0:
                positve_lowest = gr_per_year
            if gr_per_year > 0 and gr_per_year < positve_lowest:
                positve_lowest = gr_per_year
        if positve_lowest > 0:
            lowest = positve_lowest
        else:
            lowest = average
    return (lowest, temp_data, index)


def difference_calculator(current: int, prev: int):
    """
        takes two inputs, and returns 
    """
    result = 0
    if current != 0:
        result = (current - prev)/current
    return result


def calculate_discount_factor(WACC_value: int, number_factors: int):
    """
    docstring
    """
    discount_factor = []
    for factor in range(1, number_factors+1):
        temp = (1+(WACC_value/100))
        disc_temp = 0
        for iteration in range(1, factor+1):
            if iteration == 1:    
                disc_temp = temp
            else:
                disc_temp = disc_temp * temp   
        discount_factor.append(disc_temp)
    return discount_factor


def calculate_wacc_value(data: dict, ticker: str, period: str):
    """
        Funtion returns WACC value as an integer
    """
    # interest expense, income before tax, income tax expense
    incstm = data[ticker][cnst.INCOMESTATEMENT.format(period)][0]
    # totaldebt
    bsheet = data[ticker][cnst.BALANCESHEET.format(period)][0]
    # marketcap
    keymtcs = data[ticker][cnst.KEYMETRICS.format(period)][0]
    # beta 
    profile = data[ticker][cnst.COMPANYPROFILE][0]

    int_expense = incstm['interestExpense']
    inc_b4_tax = incstm['incomeBeforeTax']
    inc_tax_expense = incstm['incomeTaxExpense']
    ttl_debt = bsheet['totalDebt']
    mk_cap = keymtcs['marketCap']
    beta = profile['beta']

    rate = (1 - (difference_calculator(inc_b4_tax, inc_tax_expense)))
    r_debt = difference_calculator(ttl_debt, int_expense)
    w_debt = ttl_debt/(ttl_debt + mk_cap)
    w_equity = mk_cap/(ttl_debt + mk_cap)
    r_equity = float(cnst.TREASURY_RATE) + (beta*(float(cnst.AVG_RATE_OF_RETURNS)-float(cnst.TREASURY_RATE)))

    wacc = (w_debt*r_debt*rate) + (w_equity*r_equity)
    return wacc


def calculate_fcf_terminal_value(data: dict, ticker: str, period: str, disc_factor: list):
    """
        calculate terminal value for FCF, discount factor, and PV of future cash flow
    """
    fcf_current_yr = data[ticker][cnst.CASHFLOW.format(period)][0]['free']

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
