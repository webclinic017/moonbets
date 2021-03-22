import datetime as dt
import time

from src.backend import external_endpoints as ee
from src.backend import constants as cnst



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
def cleaning_profiles(data: list):
    data_cleaned = {}
    temp_profile, is_etf, is_active_trading = '', '', ''
    beta = int
    for stonk in data:
        temp_profile = ee.get_company_profile(stonk['symbol'])
        if temp_profile:
            is_etf = temp_profile[0]['isEtf']
            is_active_trading = temp_profile[0]['isActivelyTrading']
            beta = temp_profile[0]['beta']
            if not is_etf and is_active_trading and beta > 2:
                data_cleaned[stonk['symbol']] = {'profile': temp_profile,
                                                 'calendar': stonk}
    return data_cleaned


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
        sec = ee.sec_statements(stonk)
        all_data[stonk][cnst.SEC] = sec
    return all_data