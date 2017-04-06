"""
API Privada para Trades na Poloniex. Nem todos os métodos de api privados estão implementados e provavelemente
não serão adicionados à menos que sejam realmente utilizados. Para usar esses métodos API
uma chave API e um segredo devem estar configurados. Nem todos os métodos precisam
da opção "Habilitar Trade" na chave API.
"""

import hashlib
import hmac
import json
import time
import urllib2

from api_key_secret_util import get_api_key, get_api_secret

api_url = "https://poloniex.com/tradingApi"


class InvalidKeySecretError(Exception):
    """
    Exceção causada por um par inválido de chave API/segredo.
    """
    pass


class TradingApiError(Exception):
    """
    Exceção cauada por um erro geral do TradingApi.
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
    Chama o API de Trading da Poloniex.

    Esse API requer dois cabeçalhos com a chave api e um body com POST assinado
    dentro do segredo.

    :param post_body: (str) POST parameters
    :return: (dict) Response
    :raises: InvalidKeySecretError
    :raises: TradingApiError
    """
    request = urllib2.Request(api_url)
    request.add_header("Key", get_api_key())
    request.add_header("Sign", _sign_header(post_body))
    request.add_data(post_body)
    response = urllib2.urlopen(request).read()
    response_dict = json.loads(response)
    if "error" in response_dict:
        if response_dict["error"] == "Chave API/segredo inválidos.":
            raise InvalidKeySecretError
        else:
            raise TradingApiError(response_dict["error"])
    return json.loads(response)


def _build_body(command, parameters=None):
    """
    Constrói o corpo do Trading API. Os métodos API são especificados pelo 
    parâmentro 'command' do POST. Adicionalmente, cada requisição eve ter o parâmetro
    POST 'nonce' que  requer um int maior em cada .

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
