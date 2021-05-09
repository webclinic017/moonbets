
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src import data as d
from src import data_calls as dc


all_data = dc.technicals({'LFVN':{}})
# all_data = d.load_data('abc')
# all_data =  dc.technicals({'AAPL':{}, 'BABA':{}, 'CLF':{}})
# d.dump_data_json(all_data, 'abc')

# period = 'annual'
ticker = 'LFVN'
ticker2 = 'BABA'
ticker3 = 'CLF'

def test_get_dcf_company():
    result = dc.dcf_company(all_data, ticker)
    for key in result:
        assert float(result[key]) > 0
