import asyncio

from src.backend import external_endpoints as ee
from src.backend import spreadsheets as ss
from src.backend import constants as cnst
from src.backend import data_calls as dc
from src.backend import data


def main():
    #   date, symbol, eps, epsEstimated, time, revenuem revenueEstimated
    # singple_profile = dc.singple_profile('EAT')
    # profiles = dc.cleaning_profiles(singple_profile)

    from_date, to_date = dc.get_dates(20, 10)
    calendar_data = ee.get_earning_calendar(from_date, to_date)
    profiles = dc.cleaning_profiles(calendar_data)
    all_data = dc.technicals(profiles)
    data.dump_data_json(all_data, 'all_data')
    # all_data = data.load_data('all_data')
    ss.gen_xl(all_data)


if __name__ == "__main__":
    main()
