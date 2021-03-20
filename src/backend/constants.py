import os

from dotenv import load_dotenv


# PATHS
BASE_PATH = os.getcwd()
DATA_PATH = BASE_PATH + '/data/'


# APIKEY
load_dotenv()
APIKEY = os.environ.get('APIKEY')


# Other URLS
SEC_URL = 'https://www.sec.gov/cgi-bin/browse-edgar?CIK={}&owner=exclude'


# File names for stats
CASHFLOW_YEAR = 'cashflow_Y_{}'
CASHFLOW_QUATER = 'cashflow_Q_{}'
INCOMESTATEMENT_YEAR = 'incomestatement_Y_{}'
INCOMESTATEMENT_QUARTER = 'incomestatement_Q_{}'
BALANCESHEET_YEAR = 'blanacesheet_Y_{}'
BALANCESHEET_QUATER = 'balancesheet_Q_{}'
RATIOS_YEAR = 'ratios_Y_{}'
RATIOS_QUATER = 'ratios_Q_{}'
KEYMETRICS_YEAR = 'keymetrics_Y_{}'
KEYMETRICS_QUATER = 'keymetrics_Q_{}'
COMPANYPROFILE = 'companyprofile_{}'
INSIDERTRADING = 'insider_{}'
SEC = 'SEC_{}'

# File Names for users
WATCH_LIST = 'Watch_Lists'
FAVORITE = 'Favorites'
WATCH = 'Watch_{}'

# Periods
ANNUAL = 'annual'
QUARTER = 'quarter'

# Other
NOTES = "Notes"
DESCRIPTION = "Description"
JSON = {}
