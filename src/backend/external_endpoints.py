import requests
import os

import fmpsdk as api

from src.backend.constants import SEC_URL, APIKEY

#   Date should be in YYYY:MM:DD
#   only three months maximum if range is given
def get_earning_calendar(from_date: str = None, to_date: str = None):
    try:
        raw_data = api.earning_calendar(APIKEY, from_date=from_date, to_date=to_date)
        return raw_data
    except:
        print("no data found")


def get_cash_flow_statment(ticker, period='annual'):
    try:
        raw_data = api.cash_flow_statement(apikey=APIKEY, symbol=ticker, period=period)
        return raw_data
    except:
        print("no data found")


def get_income_statment(ticker, period='annual'):
    try:
        raw_data = api.income_statement(apikey=APIKEY, symbol=ticker, period=period)
        return raw_data
    except:
        print("no data found")


def get_balance_sheet_statement(ticker, period='annual'):
    try:
        raw_data = api.balance_sheet_statement(apikey=APIKEY, symbol=ticker, period=period)
        return raw_data
    except:
        print("no data found")


def get_ratios(ticker, period='annual'):
    try:
        raw_data = api.financial_ratios(apikey=APIKEY, symbol=ticker, period=period)
        return raw_data
    except:
        print("no data found")


def get_key_metrics(ticker, period='annual'):
    try:
        raw_data = api.key_metrics(apikey=APIKEY, symbol=ticker, period=period)
        return raw_data
    except:
        print("no data found")


def get_company_profile(ticker):
    try:
        raw_data = api.company_profile(apikey=APIKEY, symbol=ticker)
        return raw_data
    except:
        print("no data found")


def get_insider_trading(ticker):
    try:
        raw_data = api.insider_trading(apikey=APIKEY, symbol=ticker)
        return raw_data
    except:
        print("no data found")


def sec_statements(ticker):
    try:
        raw_data = requests.get(SEC_URL.format(ticker))
        return raw_data.url
    except:
        print("no data found")
