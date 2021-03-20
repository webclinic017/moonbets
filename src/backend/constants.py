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
CASHFLOW = 'cashflow_{}'
INCOMESTATEMENT = 'incomestatement_{}'
BALANCESHEET = 'balanacesheet_{}'
RATIOS = 'ratios_{}'
KEYMETRICS = 'keymetrics_{}'
COMPANYPROFILE = 'companyprofile_{}'
INSIDERTRADING = 'insider'
SEC = 'SEC'

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
