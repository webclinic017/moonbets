import datetime as dt
import time

from src import external_endpoints as ee
from src import constants as cnst
from src import calculations as calcs


#   calendar dates
def get_dates(business_days: int = 5, days_from_date: int = 0):
    from_date = dt.datetime.today() + dt.timedelta(days=days_from_date)
    to_date = ''
    total_days = 1
    index = 1
    while index <= business_days:
        to_date = from_date + dt.timedelta(days=total_days)
        is_weekend = to_date.weekday()
        if is_weekend == 5 or is_weekend == 6:
            index -= 1
        total_days += 1
        index += 1
    return from_date.strftime('%Y-%m-%d'), to_date.strftime('%Y-%m-%d')


#   clean data: if not etf and is active
#   return data only with stocks profiled
#   profiles with 2 or more of beta
def cleaning_profiles(data: list, multi_profile: bool = True):
    data_cleaned = {}
    temp_profile, is_etf, is_active_trading = '', '', ''
    beta = int
    for index, ticker in enumerate(data):
        temp_profile = ee.get_company_profile(ticker['symbol'])
        if temp_profile:
            is_etf = temp_profile[0]['isEtf']
            is_active_trading = temp_profile[0]['isActivelyTrading']
            beta = temp_profile[0]['beta']
            if multi_profile:
                if not is_etf and is_active_trading and beta >= 1.5:
                 data_cleaned[ticker['symbol']] = {'profile': temp_profile,
                                                    'calendar': ticker}
            else:
                data_cleaned[ticker['symbol']] = {'profile': temp_profile,
                                'calendar': ticker}
        check = index % 10
        if index == 0:
            time.sleep(0.75)
    return data_cleaned


def singple_profile(ticker: str):
    return ee.get_company_profile(ticker)


#   get technical data data
#   need balancesheet, cashflow, incomestatement, keymetrics, ratios
#   no period need insider, sec
def technicals(profiles):
    all_data = profiles
    for ticker in profiles:
        prof = ee.get_company_profile(ticker)
        all_data[ticker][cnst.COMPANYPROFILE] = prof
        for period in [cnst.ANNUAL, cnst.QUARTER]:
            cf = ee.get_cash_flow_statment(ticker, period)
            all_data[ticker][cnst.CASHFLOW.format(period)] = cf
            incs = ee.get_income_statment(ticker, period)
            all_data[ticker][cnst.INCOMESTATEMENT.format(period)] = incs
            km = ee.get_key_metrics(ticker, period)
            all_data[ticker][cnst.KEYMETRICS.format(period)] = km
            r = ee.get_ratios(ticker, period)
            all_data[ticker][cnst.RATIOS.format(period)] = r
            bs = ee.get_balance_sheet_statement(ticker, period)
            all_data[ticker][cnst.BALANCESHEET.format(period)] = bs
            time.sleep(0.5)
    return all_data


def compare_industry(data: dict,
                     upper_mc: float = None,
                     lower_mc: float = None,
                    ):
    key = list(data.keys())[0]
    industry = data[key]['profile'][0]['industry']
    sector = data[key]['profile'][0]['sector']
    cmpl_data = {}
    companies = ee.get_industry(industry, sector, upper_mc, lower_mc)
    for ticker in companies:
        ticker = ticker['symbol']
        if '.' not in ticker:
            cmpl_data[ticker] = {}
            cmpl_data[ticker][cnst.COMPANYPROFILE] = ticker
            incs = ee.get_income_statment(ticker, cnst.QUARTER, 2)
            cmpl_data[ticker][cnst.INCOMESTATEMENT.format(cnst.QUARTER)] = incs
            km = ee.get_key_metrics(ticker, cnst.QUARTER, 2)
            cmpl_data[ticker][cnst.KEYMETRICS.format(cnst.QUARTER)] = km
            r = ee.get_ratios(ticker, cnst.QUARTER, 2)
            cmpl_data[ticker][cnst.RATIOS.format(cnst.QUARTER)] = r
            time.sleep(0.5)
    return cmpl_data


def get_dcf_company(data: dict, ticker:str):
    result = {}
    try:
        for period in [cnst.ANNUAL, cnst.QUARTER]:
            fcf_result = calcs.calculate_fcf_dataset(data, ticker, period)
            wacc_result = calcs.calculate_wacc_value(data, ticker, period)
            discount_fact = calcs.calculate_discount_factor(wacc_result, 4)
            terminal_value_result = calcs.calculate_fcf_terminal_value(data, ticker, period)
            future_cashflow = calcs.calculate_pv_future_cashflow(fcf_result,
                                                        terminal_value_result,
                                                        discount_fact)
            todays_stock_value = calcs.calculate_todays_stock_value(future_cashflow)
            fair_value = calcs.calculate_fair_value_equity(data, ticker, period, todays_stock_value)
            result[period] = fair_value
    except:
        print("Issue getting dcf")
    finally:
        return result


def get_wacc_value(data: dict, ticker:str):
    result = {}
    try:
        for period in [cnst.ANNUAL, cnst.QUARTER]:
            fcf_result = calcs.calculate_fcf_dataset(data, ticker, period)
            wacc_result = calcs.calculate_wacc_value(data, ticker, period)
            result[period] = wacc_result
    except:
        print("Issue getting wacc")
    return result
