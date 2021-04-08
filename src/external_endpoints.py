import requests
import os

import fmpsdk as api

from src.constants import SEC_URL, APIKEY


def get_earning_calendar(from_date: str = None, to_date: str = None):
    try:
        raw_data = api.earning_calendar(APIKEY,
                                        from_date=from_date,
                                        to_date=to_date)
        return raw_data
    except:
        print("no data found")


def get_cash_flow_statment(ticker: str, period: str = 'annual', default_limit=60):
    try:
        if period == 'annual':
            default_limit = 15
        raw_data = api.cash_flow_statement(apikey=APIKEY,
                                           symbol=ticker,
                                           period=period,
                                           limit=default_limit)
        return raw_data
    except:
        print("no data found")


def get_income_statment(ticker: str, period: str = 'annual', default_limit=60):
    try:
        if period == 'annual':
            default_limit = 15
        raw_data = api.income_statement(apikey=APIKEY,
                                        symbol=ticker,
                                        period=period,
                                        limit=default_limit)
        return raw_data
    except:
        print("no data found")


def get_balance_sheet_statement(ticker: str, period: str = 'annual', default_limit: int = 60):
    try:
        if period == 'annual':
            default_limit = 15
        raw_data = api.balance_sheet_statement(apikey=APIKEY,
                                               symbol=ticker,
                                               period=period,
                                               limit=default_limit)
        return raw_data
    except:
        print("no data found")


def get_ratios(ticker: str, period: str = 'annual', default_limit: int = 60):
    try:
        if period == 'annual':
            default_limit = 15
        raw_data = api.financial_ratios(apikey=APIKEY,
                                        symbol=ticker,
                                        period=period,
                                        limit=default_limit)
        return raw_data
    except:
        print("no data found")


def get_key_metrics(ticker: str, period: str = 'annual', default_limit=60):
    try:
        if period == 'annual':
            default_limit = 15
        raw_data = api.key_metrics(apikey=APIKEY,
                                   symbol=ticker,
                                   period=period,
                                   limit=default_limit)
        return raw_data
    except:
        print("no data found")


def get_company_profile(ticker: str):
    try:
        raw_data = api.company_profile(apikey=APIKEY,
                                       symbol=ticker)
        return raw_data
    except:
        print("no data found")


# Returns array with a dic. Also MC, price, and exchange.
def get_industry(industry: str,
                 sector: str,
                 upper_mc: float = None,
                 lower_mc: float = None,
                 default_limit=1000
                 ):
    try:
        raw_data = api.stock_screener(apikey=APIKEY,
                                      industry=industry,
                                      market_cap_more_than=lower_mc,
                                      market_cap_lower_than=upper_mc,
                                      is_etf=False,
                                      is_actively_trading=True,
                                      limit=default_limit)
        return raw_data
    except:
        print("no data found")


def get_insider_trading(ticker: str):
    try:
        raw_data = api.insider_trading(apikey=APIKEY,
                                       symbol=ticker,
                                       limit=30)
        return raw_data
    except:
        print("no data found")


def sec_statements(ticker: str):
    try:
        raw_data = requests.get(SEC_URL.format(ticker))
        return raw_data.url
    except:
        print("no data found")
