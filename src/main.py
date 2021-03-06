import os
import sys

from PyInquirer import prompt

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src import cli
from src import data
from src import data_calls as dc
from src import constants as cnst
from src import spreadsheets as ss
from src import external_endpoints as ee


def main():
    while(True):
        first_choice = prompt(cli.main_menu)
        if "QUICK Single stonk report" in first_choice['theme']:
            ticker = prompt(cli.stonk_report)
            singple_profile = dc.singple_profile(ticker['ticker'].upper())
            profile = dc.cleaning_profiles(singple_profile, False)
            all_data = dc.technicals(profile)
            ss.gen_xl_single(all_data)
            print(f"Report created; look for report {ticker['ticker'].upper()}.xlsx")
        elif "Single stonk report" in first_choice['theme']:
            ticker = prompt(cli.stonk_report)
            singple_profile = dc.singple_profile(ticker['ticker'].upper())
            profile = dc.cleaning_profiles(singple_profile, False)
            all_data = dc.technicals(profile)
            compare_data = dc.compare_industry(all_data)
            ss.gen_xl_single(all_data, compare_data)
            print(f"Report created; look for report {ticker['ticker'].upper()}.xlsx")
        elif "Future earnings report" in first_choice['theme']:
            input_dates = prompt(cli.report_dates)
            from_date, to_date = dc.get_dates(int(input_dates['business_days']),
                                              int(input_dates['days_from_today']))
            calendar_data = ee.get_earning_calendar(from_date, to_date)
            profiles = dc.cleaning_profiles(calendar_data)
            all_data = dc.technicals(profiles)
            ss.gen_xl(all_data, from_date)
            print(f"Data generated; look for report {from_date}.xlsx")
        elif 'Exit' in first_choice['theme']:
            break


if __name__ == "__main__":
    main()
