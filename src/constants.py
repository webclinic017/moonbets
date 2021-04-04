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
COMPARE = 'compare'
REPORT = 'report'


# Other
NOTES = "Notes"
DESCRIPTION = "Description"
JSON = {}

# Spreadsheet fields
CORE_PARAMS = [
    ('Date', 'date', 'NA', ''),
    ('Market Cap', 'marketCap', 'keymetrics', 'Market Cap'),
    ('Revenue', 'revenue', 'incomestatement', 'Total amount of income generated by sales'),
    ('DE', 'debtToEquity', 'keymetrics', 'D/E (debt/equity) \n higher D/E higher riskDifferent industries have different debt. \n 2 or less is a good number'),
    ('RoA', 'returnOnAssets', 'ratios', 'How profitable a company is relative to its total assets. \n ROA= (net income) / ( Total Assets) \n Higher ROA more efficiency'),
    ('FCF', 'freeCashFlow', 'cashflow', 'Cash left over after a company pays for its operating expenses and capital expenditures (buildings, land'),
    ('OCF', 'operatingCashFlow', 'cashflow', 'Cash left over after a company pays for its operating expenses. Does not take into consideration capital expenditures (buildings, plants...)'),
    ('GPM', 'grossProfitRatio', 'incomestatement', '[(Total Revenue ) - (Cost of Good) ] / Revenue \n The higher the gross margin, the more capital the company retain on each dollar of sales. \n'),
    ('OPM', 'operatingProfitMargin', 'ratios', '(Operating Earnings ) / (Revenues) \n measures how much profit a company makes on a dollar of sales after paying for variable costs of production, such as wages and raw materials, but before paying interest or tax. \n Increasing over time means company is more profitable'),
    ('NPM', 'netProfitMargin', 'ratios', '(gross profit) - (operating cost + tax + interest) /(revenue) \n how much net income or profit is generated as a percentage of revenue. \n company\'s overall financial health. Want increasing value over time. '),
    ('ROIC', 'roic', 'keymetrics', 'Return on invested capital. \n amount of return a company makes above the average cost it pays for its debt and equity capital. \n >2(0.02)% creating value, <2 destroying value'),
    ('BVPS', 'bookValuePerShare', 'keymetrics', 'Ratio of equity available to common shareholders devided by the number of outstanding shares. \n When stock is undervalued, it will have higher value than current share price'),
    ('EPS', 'eps', 'incomestatement', 'profit / outstanding shares \n higher value means investors will pay more for 1 company share'),
    ('R&DE', 'researchAndDevelopmentExpenses', 'incomestatement', 'Reasearch and Development Expense'),
    ('R&DER', 'researchAndDdevelopementToRevenue', 'keymetrics', 'Reasearch and Development Expense / Revenue'),
    ('EBITDA', 'ebitda', 'incomestatement', 'Earnings Before Interest, Taxes, Depreciation, and Amortization. This can be used as a proxy cash flow'),
    ('EV/EBITDA', 'enterpriseValueOverEBITDA', 'keymetrics', 'Enterprice Value / Earnings Before Interest, Taxes, Depreciation, and Amortization'),
    ('RoE', 'returnOnEquity', 'ratios', 'Return on Equity: good to compare against other of the same peer group. 10%-18% is a normal value good value '),
    ('P/S', 'priceToSalesRatio', 'ratios', 'Price to Share. Good to compare. low = company undervalued high = overvalued'),
    ('P/E', 'priceEarningsRatio', 'ratios', 'Price per share to earnings. Good to compare. price per share to earnings. High P/E means company is overvalued or expecting company growth.'),
    ('P/B', 'priceToBookRatio', 'ratios', 'Price book. Book value is total asset minus liability per share bases <3 undervalued '),
    ('P/FCF', 'priceToFreeCashFlowsRatio', 'ratios', 'Price to Free cash flow ratio.'),
    ('PEG', 'priceEarningsToGrowthRatio', 'ratios', 'Price earnings to growth ratio.'),
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
