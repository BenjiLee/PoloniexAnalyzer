"""
Poloniex's Public API. Not all public api methods are implemented and will
probably not be added unless it will actually be used.
"""
import json
import urllib2

api_url = "https://poloniex.com/public"


class PublicApi:
    """
    Public API for Poloniex

    Probably does not need to be a class at the time of writing, but it makes
    calling all these methods from other files more readable.
    """
    def return_usd_btc(self):
        ticker = self.return_ticker()
        return float(ticker["USDT_BTC"]["last"])

    def return_ticker(self):
        url = "{}?command=returnTicker".format(api_url)
        return self.__call_api(url)

    @staticmethod
    def __call_api(url):
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        json_response = response.read()
        return json.loads(json_response)
