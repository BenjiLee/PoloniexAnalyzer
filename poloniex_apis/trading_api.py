import ConfigParser
import hashlib
import hmac
import json
import urllib2

import time

api_url = "https://poloniex.com/tradingApi"


class InvalidKeySecretError(Exception):
    pass


class TradingApiError(Exception):
    pass


class TradingApi:
    def __init__(self):
        self.api_key, self.api_secret = self._get_api_keys_from_file()

    def return_complete_balances(self):
        body = self._build_body(command="returnCompleteBalances")
        return self._call_api(body)

    def return_deposits_withdrawals(self):
        parameters = {
            'start': '0',
            'end': time.time()
        }
        body = self._build_body(
            command="returnDepositsWithdrawals",
            parameters=parameters
        )
        return self._call_api(body)

    def return_trade_history(self):
        parameters = {
            'currencyPair': 'all',
            'start': '0',
            'end': time.time()
        }
        body = self._build_body(
            command="returnTradeHistory",
            parameters=parameters
        )
        return self._call_api(body)


    def _build_body(self, command, parameters=None):
        """
        Builds the body for the trading api. Api methods are specified by the
        'command' POST parameter. Additionally, each query must have the 'nonce'
        POST parameter which requires a greater int on each call.

        :type parameters: (dict) Extra parameters
        :param command: (String) API method

        :return: (String) POST body
        """
        body = "command={}".format(command)
        nonce_int = int(time.time() * 100)
        body += "&nonce={}".format(nonce_int)
        if parameters is not None:
            for key, value in parameters.iteritems():
                body += "&{}={}".format(key, value)
        return body


    def _sign_header(self, post_body):
        hashed = hmac.new(self.api_secret, post_body, hashlib.sha512)
        return hashed.hexdigest()


    def _call_api(self, post_body):
        request = urllib2.Request(api_url)
        request.add_header("Key", self.api_key)
        request.add_header("Sign", self._sign_header(post_body))
        request.add_data(post_body)
        response = urllib2.urlopen(request).read()
        response_dict = json.loads(response)
        if "error" in response_dict:
            if response_dict["error"] == "Invalid API key/secret pair.":
                raise InvalidKeySecretError
            else:
                raise TradingApiError(response_dict["error"])
        return json.loads(response)


    def _get_api_keys_from_file(self):
        config = ConfigParser.ConfigParser()
        config.read("api_keys.ini")
        key = config.get("ApiKeys", "key")
        secret = config.get("ApiKeys", "secret")
        return key, secret
