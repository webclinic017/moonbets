import datetime as dt
import requests as rq
import os

from src.backend import external_endpoints as ee


def get_dates(days: int = 21):
    from_date = dt.datetime.today().strftime('%Y-%m-%d')
    days_leap = dt.timedelta(days=days)
    to_date = from_date + days_leap
    return from_date, to_date


def main():
    from_date, to_date = get_dates()
    calendar_data = ee.get_earning_calendar(from_date, to_date)



if __name__ == "__main__":
    pass
