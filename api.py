import hashlib
import hmac
import json
import urllib2

import time

api_url = "https://poloniex.com/tradingApi"


class PoloniexApi:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def returnCompleteBalances(self):
        body = self.__build_body(command="returnCompleteBalances")
        return self.__call_api(body)

    def returnDepositsWithdrawals(self):
        parameters = {
            'start': '0',
            'end': time.time()
        }
        body = self.__build_body(
            command="returnDepositsWithdrawals",
            parameters=parameters
        )
        return self.__call_api(body)

    def __build_body(self, command, parameters=None):
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

    def __sign_header(self, post_body):
        hashed = hmac.new(self.api_secret, post_body, hashlib.sha512)
        return hashed.hexdigest()

    def __call_api(self, post_body):
        request = urllib2.Request(api_url)
        request.add_header("Key", self.api_key)
        request.add_header("Sign", self.__sign_header(post_body))
        request.add_data(post_body)
        response = urllib2.urlopen(request)
        json_response = response.read()
        return json.loads(json_response)
