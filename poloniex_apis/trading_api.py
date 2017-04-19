"""
Poloniex's Trading API. Not all trading api methods are implemented and will
probably not be added unless it will actually be used. In order for these API
methods to work, an API key and secret must be configured. Not all methods need
the "Trading Enabled" option on their API key.
"""

import hashlib
import hmac
import json
import time
import urllib2

import sys

from api_key_secret_util import get_api_key, get_api_secret

api_url = "https://poloniex.com/tradingApi"


class InvalidKeySecretError(Exception):
    """
    Exception raised for an invalid API key/secret pair.
    """
    pass


class TradingApiError(Exception):
    """
    Exception raised for a general TradingApi error.
    """
    pass


def return_complete_balances():
    body = _build_body(command="returnCompleteBalances")
    return _call_trading_api(body)


def return_deposits_withdrawals():
    parameters = {
        'start': '0',
        'end': time.time()
    }
    body = _build_body(
        command="returnDepositsWithdrawals",
        parameters=parameters
    )
    return _call_trading_api(body)


def return_trade_history():
    parameters = {
        'currencyPair': 'all',
        'start': '0',
        'end': time.time()
    }
    body = _build_body(
        command="returnTradeHistory",
        parameters=parameters
    )
    return _call_trading_api(body)


def _sign_header(post_body):
    hashed = hmac.new(get_api_secret(), post_body, hashlib.sha512)
    return hashed.hexdigest()


def _call_trading_api(post_body):
    """
    Calls the Poloniex Trading API.

    The Poloniex trading API required two headers with the api key, and a
    signed POST body signed with the secret.

    :param post_body: (str) POST parameters
    :return: (dict) Response
    :raises: InvalidKeySecretError
    :raises: TradingApiError
    """
    request = urllib2.Request(api_url)
    request.add_header("Key", get_api_key())
    request.add_header("Sign", _sign_header(post_body))
    request.add_data(post_body)
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError as err:
        if err.code == 422:
            print "HTTP Error 422. Use a new API key/secret. From the Poloniex API doc:\n" \
                  "    Additionally, all queries must include a 'nonce' POST parameter.\n" \
                  "    The nonce parameter is an integer which must always be greater \n" \
                  "    than the previous nonce used.\n\n" \
                  "If you have used another script or the api directly, the nonce value\n" \
                  "is persistent may be greater than what this script is setting. This" \
                  "script uses the Epoch time to determine the nonce."
            sys.exit(0)
    response_dict = json.loads(response.read())
    if "error" in response_dict:
        if response_dict["error"] == "Invalid API key/secret pair.":
            raise InvalidKeySecretError
        else:
            raise TradingApiError(response_dict["error"])
    return response_dict


def _build_body(command, parameters=None):
    """
    Builds the body for the trading api. Api methods are specified by the
    'command' POST parameter. Additionally, each query must have the 'nonce'
    POST parameter which requires a greater int than the previous  call.

    :type parameters: (dict) Extra parameters
    :param command: (str) API method

    :return: (str) POST body
    """
    body = "command={}".format(command)
    nonce_int = int(time.time() * 100)
    body += "&nonce={}".format(nonce_int)
    if parameters is not None:
        for key, value in parameters.iteritems():
            body += "&{}={}".format(key, value)
    return body
