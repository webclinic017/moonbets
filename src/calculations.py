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

    FCF_growth_data = calculate_growth_rate(fcf_sheet, 'freeCashFlow', period)
    revenue_growth_data = calculate_growth_rate(incstm_sheet, 'revenue', period)
    netprofitmargin_growth_data = calculate_lowest_positive_netprofitmargin_value(ratio_sheet,
                                                                                  'netProfitMargin',
                                                                                  period)

    revenue = []
    current_revenue = revenue_growth_data[1][0]
    for index in range(0, 4):
        current_revenue = current_revenue * (1+revenue_growth_data[0])
        revenue.append(current_revenue)

    net_income = []
    for index in range(0, 4):
        net_income.append(revenue[index] * netprofitmargin_growth_data)

    FCF_predict = []
    for index in range(0, 4):
        FCF_predict.append((1+FCF_growth_data[0])*net_income[index])
    return FCF_predict


def calculate_lowest_positive_netprofitmargin_value(data: list, data_key: str, period: str):
    """
        returns lowest net proft margin value
    """
    index = 0
    data_index = 0
    temp_data = []
    lowest = 0
    temp = 0
    if period == cnst.ANNUAL:
        data_index = 6
    if period == cnst.QUARTER:
        data_index = 12

    # get data from sheet
    for time_period in data:
        if not time_period[data_key] or index >= data_index:
            break
        temp_data.append(time_period[data_key])
        index += 1

    for value in temp_data:
        if temp == 0 and value > 0:
            temp = value
            lowest = temp
        if temp != 0 and value < temp and value > 0:
            lowest = temp
    return lowest


def calculate_growth_rate(data: list, data_key: str, period: str):
    """
        It takes a dict and a data key
        grabs lowest growth rate, grabbing 2 lowest closest to the mean. 
        it returns a dictionary with three entries: growth,
        dataset(list), set_length
    """
    index = 0
    data_index = 0
    temp_data = []
    lowest = 0

    if period == cnst.ANNUAL:
        data_index = 6
    if period == cnst.QUARTER:
        data_index = 12

    # get data from sheet
    for time_period in data:
        if not time_period[data_key] or index >= data_index:
            break
        temp_data.append(time_period[data_key])
        index += 1

    # lowest value
    for range_index in range(0, index-1):
        temp = difference_calculator(temp_data[range_index], temp_data[range_index+1])
        if lowest == 0:
            lowest = temp
        elif temp < lowest:
            lowest = temp
    return (lowest, temp_data, index)


def difference_calculator(current: int, prev: int):
    """
        takes two inputs, and returns 
    """
    result = 0
    if current != 0:
        result = (current - prev)/current
    return abs(result)


def calculate_discount_factor(wacc_value: int, number_factors: int):
    """
        takes in the wacc value and the number of factors to multiply
    """
    discount_factor = []
    for factor in range(1, number_factors+1):
        temp = (1+(wacc_value/100))
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


def calculate_fcf_terminal_value(wacc_value: float, fcf_prev_year: float):
    """
        calculate terminal value for FCF, discount factor, and PV of future cash flow
        retuns float value
    """
    perpetual_growth = float(cnst.PERPETUAL_GROWTH)/100

    terminal_value = (fcf_prev_year * (1+perpetual_growth)) / ((wacc_value/100) - perpetual_growth)
    return terminal_value


def calculate_pv_future_cashflow(fcf_data: list, fcf_terminal_value: float, discount_factor: list):
    """
        takes in fcf prediction data, terminal value for fcf, and discount factors
    """
    fcf_new = []
    fcf_new.extend(fcf_data)
    fcf_new.append(fcf_terminal_value)

    disc_new = []
    disc_new.extend(discount_factor)
    disc_new.append(discount_factor[-1])
    future_cashflow = []
    for index in range(0, len(fcf_new)):
        future_cashflow.append(fcf_new[index] / disc_new[index])
    return future_cashflow


def calculate_todays_stock_value(pv_data: dict):
    """
        add array of pv future cash data and returns the value
    """
    result = 0
    for value in pv_data:
        result += value
    return result


def calculate_fair_value_equity(data: dict, ticker: str, period: str, todays_value: int):
    """
        calculates fair value
    """
    # shares out
    sharesout = data[ticker][cnst.INCOMESTATEMENT.format(period)][0]['weightedAverageShsOut']
    instrinsic_value = todays_value / sharesout
    return instrinsic_value
