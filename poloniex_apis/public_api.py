import json
import urllib2

api_url = "https://poloniex.com/public"


class PublicApi:
    def return_usd_btc(self):
        ticker = self.return_ticker()
        return float(ticker["USDT_BTC"]["last"])

    def return_ticker(self):
        url = "{}?command=returnTicker".format(api_url)
        return self.__call_api(url)

    def __call_api(self, url):
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        json_response = response.read()
        return json.loads(json_response)
