"""
Public API for Poloniex

Poloniex's Public API. Not all public api methods are implemented and will
probably not be added unless it will actually be used.
"""
import json
import urllib2

api_url = "https://poloniex.com/public"


def return_usd_btc():
    ticker = return_ticker()
    return float(ticker["USDT_BTC"]["last"])


def return_ticker():
    url = "{}?command=returnTicker".format(api_url)
    return __call_public_api(url)


def __call_public_api(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    json_response = response.read()
    return json.loads(json_response)
