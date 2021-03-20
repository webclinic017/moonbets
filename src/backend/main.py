import datetime as dt
import asyncio
import http
import os

from src.backend import external_endpoints as ee
from src.backend import constants as cnst
from src.backend import data


#   calendar dates
def get_dates(business_days: int = 5):
    current_date = dt.datetime.today() + dt.timedelta(days=3)
    to_date = ''
    total_days = 1
    index = 1
    while index <= business_days:
        to_date = current_date + dt.timedelta(days=total_days)
        is_weekend = to_date.weekday()
        if is_weekend == 5 or is_weekend == 6:
            index -= 1
        total_days += 1
        index += 1
    return current_date.strftime('%Y-%m-%d'), to_date.strftime('%Y-%m-%d')


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
def technicals(profiles: dict):
    all_data = profiles
    balancesheet, cashflow, = '', ''
    incomestatement, keymetrics, ratios = '', '', ''
    insider, sec = '', ''
    for stonk in profiles:
        for period in [cnst.ANNUAL, cnst.QUARTER]:
            balancesheet = ee.get_balance_sheet_statement(stonk, period)
            all_data[stonk][cnst.BALANCESHEET.format(period)] = balancesheet
            cashflow = ee.get_cash_flow_statment(stonk, period)
            all_data[stonk][cnst.CASHFLOW.format(period)] = cashflow
            incomestatement = ee.get_income_statment(stonk, period)
            all_data[stonk][cnst.INCOMESTATEMENT.format(period)] = incomestatement
            keymetrics = ee.get_key_metrics(stonk, period)
            all_data[stonk][cnst.KEYMETRICS.format(period)] = keymetrics
            ratios = ee.get_ratios(stonk, period)
            all_data[stonk][cnst.RATIOS.format(period)] = ratios
        insider = ee.get_insider_trading(stonk)
        all_data[stonk][cnst.INSIDERTRADING] = insider
        sec = ee.sec_statements(stonk)
        all_data[stonk][cnst.SEC] = sec
    return all_data

def main():
    from_date, to_date = get_dates()
    # date, symbol, eps, epsEstimated, time, revenuem revenueEstimated
    # calendar_data = ee.get_earning_calendar(from_date, to_date)
    # profiles = cleaning_profiles(calendar_data)
    # data.dump_data_json(profiles, 'PROFILES')
    profiles = data.load_data('PROFILES')
    all_data = technicals(profiles)
    data.dump_data_json(all_data, 'ALL_DATA')


if __name__ == "__main__":
    main()
