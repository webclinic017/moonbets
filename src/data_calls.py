import datetime as dt
import time

from src import external_endpoints as ee
from src import constants as cnst



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
    for index, stonk in enumerate(data):
        temp_profile = ee.get_company_profile(stonk['symbol'])
        if temp_profile:
            is_etf = temp_profile[0]['isEtf']
            is_active_trading = temp_profile[0]['isActivelyTrading']
            beta = temp_profile[0]['beta']
            if multi_profile:
                if not is_etf and is_active_trading and beta >= 1.5:
                 data_cleaned[stonk['symbol']] = {'profile': temp_profile,
                                                    'calendar': stonk}
            else:
                data_cleaned[stonk['symbol']] = {'profile': temp_profile,
                                'calendar': stonk}
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
    for stonk in profiles:
        for period in [cnst.ANNUAL, cnst.QUARTER]:
            cf = ee.get_cash_flow_statment(stonk, period)
            all_data[stonk][cnst.CASHFLOW.format(period)] = cf
            incs = ee.get_income_statment(stonk, period)
            all_data[stonk][cnst.INCOMESTATEMENT.format(period)] = incs
            km = ee.get_key_metrics(stonk, period)
            all_data[stonk][cnst.KEYMETRICS.format(period)] = km
            r = ee.get_ratios(stonk, period)
            all_data[stonk][cnst.RATIOS.format(period)] = r
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
    for stonk in companies:
        ticker = stonk['symbol']
        if '.' not in ticker:
            cmpl_data[ticker] = {}
            cmpl_data[ticker][cnst.COMPANYPROFILE] = stonk
            cf = ee.get_cash_flow_statment(ticker, cnst.ANNUAL, 2)
            cmpl_data[ticker][cnst.CASHFLOW.format(cnst.ANNUAL)] = cf
            incs = ee.get_income_statment(ticker, cnst.ANNUAL, 2)
            cmpl_data[ticker][cnst.INCOMESTATEMENT.format(cnst.ANNUAL)] = incs
            km = ee.get_key_metrics(ticker, cnst.ANNUAL, 2)
            cmpl_data[ticker][cnst.KEYMETRICS.format(cnst.ANNUAL)] = km
            r = ee.get_ratios(ticker, cnst.ANNUAL, 2)
            cmpl_data[ticker][cnst.RATIOS.format(cnst.ANNUAL)] = r
            time.sleep(0.5)
    return cmpl_data

