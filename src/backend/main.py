import asyncio

from src.backend import external_endpoints as ee
from src.backend import spreadsheets as ss
from src.backend import constants as cnst
from src.backend import data_calls as dc
from src.backend import data




def main():
    from_date, to_date = dc.get_dates(business_days=30)
    #date, symbol, eps, epsEstimated, time, revenuem revenueEstimated
    calendar_data = ee.get_earning_calendar(from_date, to_date)
    profiles = dc.cleaning_profiles(calendar_data)
    all_data = dc.technicals(profiles)
    ss.gen_xl(profiles)



if __name__ == "__main__":
    main()
