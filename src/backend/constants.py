import os

from dotenv import load_dotenv
from openpyxl.styles import Font, Alignment

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
BALANCESHEET = 'balancesheet_{}'
RATIOS = 'ratios_{}'
KEYMETRICS = 'keymetrics_{}'
COMPANYPROFILE = 'profile'
INSIDERTRADING = 'insider'
SEC = 'SEC'

# Periods
ANNUAL = 'annual'
QUARTER = 'quarter'
REPORT = 'report'

# Other
NOTES = "Notes"
DESCRIPTION = "Description"
JSON = {}

# Spreadsheet fields
CORE_PARAMS = [
    ('Date', 'date', 'NA'),
    ('MC', 'marketCap', 'keymetrics'),
    ('Revenue', 'revenue', 'incomestatement'),
    ('DE', 'debtToEquity', 'keymetrics'),
    ('RoA', 'returnOnAssets', 'ratios'),
    ('FCF', 'freeCashFlow', 'cashflow'),
    ('OCF', 'operatingCashFlow', 'cashflow'),
    ('GPM', 'grossProfitRatio', 'incomestatement'),
    ('OPM', 'operatingProfitMargin', 'ratios'),
    ('NPM', 'netProfitMargin', 'ratios'),
    ('ROIC', 'roic', 'keymetrics'),
    ('BVPS', 'bookValuePerShare', 'keymetrics'),
    ('EPS', 'eps', 'incomestatement'),
    ('R&DE', 'researchAndDevelopmentExpenses', 'incomestatement'),
    ('R&DER', 'researchAndDdevelopementToRevenue', 'keymetrics'),
    ('EBITDA', 'ebitda', 'incomestatement'),
    ('EV/EBITDA', 'enterpriseValueOverEBITDA', 'keymetrics'),
    ('P/S', 'priceToSalesRatio', 'ratios'),
    ('P/E', 'priceEarningsRatio', 'ratios'),
    ('P/B', 'priceToBookRatio', 'ratios'),
    ('P/FCF', 'priceToFreeCashFlowsRatio', 'ratios'),
    ('PEG', 'priceEarningsToGrowthRatio', 'ratios'),
]
PROFILE_PARAMS = [
    ('Symbol', 'symbol'),
    ('Price', 'price'),
    ('Current MC', 'mktCap'),
    ('Beta', 'beta'),
    ('Description', 'description'),
    ('Company Name', 'companyName'),
    ('Industry', 'industry'),
    ('Sector', 'sector'),
]
CALENDAR_PARAMS = [
    ('Earnings date', 'date'),
    ('Time', 'amc'),
    ('EPS est', 'epsEstimated'),
    ('Revenue est', 'revenueEstimated'),
]



#   Style
STYLE_PARAM = Font(bold=True, color='00000000')
STYLE_ALIGN = Alignment(horizontal='left')
