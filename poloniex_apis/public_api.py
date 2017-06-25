"""
Public API for Poloniex

Poloniex's Public API. Not all public api methods are implemented and will
probably not be added unless it will actually be used.
"""
import json
from urllib.request import Request
from urllib.request import urlopen

import dev_utils
import settings

api_url = "https://poloniex.com/public"


def return_usd_btc():
    ticker = return_ticker()
    return float(ticker["USDT_BTC"]["last"])


def return_ticker():
    if settings.MOCK_API_RESPONSE:
        return dev_utils.file_to_dict("return_ticker.txt")
    url = "{}?command=returnTicker".format(api_url)
    return _call_public_api(url)


def return_24_hour_volume():
    url = "{}?command=return24hVolume".format(api_url)
    return _call_public_api(url)


def return_chart_data(period, currency_pair, start, end=9999999999):
    """
    Returns the candlestick chart data.

    :param period: (candlestick period in seconds; valid values are 300, 900, 1800, 7200, 14400, and 86400)
    :param currency_pair: The currency pair e.g. BTC_XMR
    :param start: UNIX Timestamp for start date
    :param end: UNIX Timestamp for end date
    """
    url = "{api_url}?command=returnChartData&currencyPair={currency_pair}&start={start}&end={end}&period={period}".format(
        api_url=api_url, currency_pair=currency_pair, start=start, end=end, period=period)
    return _call_public_api(url)


def _call_public_api(url):
    request = Request(url)
    response = urlopen(request)
    json_response = response.read().decode('utf8')
    return json.loads(json_response)
