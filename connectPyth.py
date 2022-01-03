from json.decoder import JSONDecoder
import time
import dateparser
import pytz
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import requests
#import mplfinance as fplt

from datetime import datetime
from binance.client import Client


def date_to_milliseconds(date_str):
    """Convert UTC date to milliseconds
    If using offset strings add "UTC" to date string e.g. "now UTC", "11 hours ago UTC"
    See dateparse docs for formats http://dateparser.readthedocs.io/en/latest/
    :param date_str: date in readable format, i.e. "January 01, 2018", "11 hours ago UTC", "now UTC"
    :type date_str: str
    """
    # get epoch value in UTC
    epoch = datetime.utcfromtimestamp(0).replace(tzinfo=pytz.utc)
    # parse our date string
    d = dateparser.parse(date_str)
    # if the date is not timezone aware apply UTC timezone
    if d.tzinfo is None or d.tzinfo.utcoffset(d) is None:
        d = d.replace(tzinfo=pytz.utc)

    # return the difference in time
    return int((d - epoch).total_seconds() * 1000.0)


def interval_to_milliseconds(interval):
    """Convert a Binance interval string to milliseconds
    :param interval: Binance interval string 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w
    :type interval: str
    :return:
         None if unit not one of m, h, d or w
         None if string not in correct format
         int value of interval in milliseconds
    """
    ms = None
    seconds_per_unit = {
        "m": 60,
        "h": 60 * 60,
        "d": 24 * 60 * 60,
        "w": 7 * 24 * 60 * 60
    }

    unit = interval[-1]
    if unit in seconds_per_unit:
        try:
            ms = int(interval[:-1]) * seconds_per_unit[unit] * 1000
        except ValueError:
            pass
    return ms

"""def options_ping(sumbol):
    Test connectivity

    https://binance-docs.github.io/apidocs/voptions/en/#test-connectivity

    
    # create the Binance client, no need for api key
    client = Client("", "")

    # init our list
    output_data = []

    return"""

def options_time(options_symbol):
     """Get current trading pair info

     https://binance-docs.github.io/apidocs/voptions/en/#get-current-trading-pair-info

     """




"""def options_info(symbol):
    Get current trading pair info

    https://binance-docs.github.io/apidocs/voptions/en/#get-current-trading-pair-info

    
    
    # create the Binance client, no need for api key
    client = Client("", "")
    temp_data = client.options_info(
        symbol=symbol,
        interval=interval,
        limit=limit,
        startTime=start_ts,
        endTime=end_ts
    )
    return """


#symbol = "ETHBTC"
#start = "1 Dec, 2017"
#end = "1 Jan, 2018"
#interval = Client.KLINE_INTERVAL_30MINUTE

#klines = get_historical_klines(symbol, interval, start, end)

options_symbol = "BTC-211231-60000-C"
file_pub = open('public.gitignore','r')
file_pri = open('private.gitignore','r')
public_key = file_pub.read()
private_key = file_pri.read()
client = Client(public_key, private_key)

d = {'col1'}
symbol = "BTCUSDT"
interval = "1h"
#interval = interval_to_milliseconds("1h")
client_time_request = client.get_server_time()
client_time = client_time_request["serverTime"]
print(client_time)
#interval_minus_client = client_time - (500*interval)

#client = Client(base_url='https://testnet.binance.vision')
#print(client.time())
#end = Client.get_server_time()
interval = Client.KLINE_INTERVAL_1HOUR
futures_klines = client.futures_klines(symbol = "BTCUSDT",interval = "1h", limit = 500)

#futures_klines = client.futures_klines(symbol,interval, limit = 500)
# open a file with filename including symbol, interval and start and end converted to milliseconds
with open(
    "Binance_{}_{}_{}.json".format(
        symbol,
        interval,
        client_time
    ),
    'w'  # set file write mode
) as f:
    f.write(json.dumps(futures_klines))





#futures_klines = client.futures_klines(symbol,interval, limit = 500)

options_mark_get_BTC = client.options_index_price(underlying = "BTCUSDT")
options_exchange_info = client.options_exchange_info()
print(options_mark_get_BTC)

options_df = pd.json_normalize(options_exchange_info)

print(options_df)
interval = interval_to_milliseconds("1h")
#Client.get_server_time()

"""

#index
labels = ['Time stamp','Open time','High','Low','Close','Volume','Close time','Quote asset volume',
'Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore']
data_indexed = pd.DataFrame(futures_klines, columns = labels)
#data_indexed = pd.read_json(futures_klines)

print("TestData\n")
print(data_indexed)

"""



""""




interval = Client.KLINE_INTERVAL_30MINUTE

klines = get_historical_klines(symbol, interval, start, end)

# open a file with filename including symbol, interval and start and end converted to milliseconds
with open(
    "Binance_{}_{}_{}-{}.json".format(
        symbol,
        interval,
        date_to_milliseconds(start),
        date_to_milliseconds(end)
    ),
    'w'  # set file write mode
) as f:
    f.write(json.dumps(klines))"""






"""
size of list = window of lookup
returns list of lists. futures_kline_get[[Opentime, open, ...][i+1 in list][...]]
"""

#index
futures_labels = ['Time stamp','Open time','High','Low','Close','Volume','Close time','Quote asset volume',
'Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore']
data_indexed = pd.DataFrame(futures_klines, columns = futures_labels)
#data_indexed = pd.read_json(futures_klines)

print("TestData\n")
print(data_indexed)

#fig = go.
#data_indexed.columns(['Time stamp','Open time','High','Low','Close','Volume','Close time','Quote asset volume',
#'Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore'])
#data_indexed = pd.DataFrame(data=futures_kline_get.transpose(), columns.set_index('Time stamp'), drop = False)

#print(futures_kline_get)
#pd.TimedeltaIndex()
#parse = True
#window = pd.DataFrame.from_records(futures_kline_get)
#window.index

#Open time
# Index(['Open','High','Low','Close','Volume','Close time','Quote asset volume','Close time','Quote asset volume'
# ,'Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore',])

#Open
#High
#Low
#Close
#Volume
#Close time
#Quote asset volume
#Number of trades
#Taker buy base asset volume
#Taker buy quote asset volume
#Ignore

#output_data = client.options_time()


#snip non-relevent data and load output into item frames
#while(parse){
    
#}



