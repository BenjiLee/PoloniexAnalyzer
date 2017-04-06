#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
"""
API Pública para Poloniex

API Pública para Poloniex. Nem todos os métodos de api pública estão implementados e provavelemente
não serão adicionados à menos que sejam realmente utilizados.
"""
import json
import urllib2

api_url = "https://poloniex.com/public"


def return_usd_btc():
    ticker = return_ticker()
    return float(ticker["USDT_BTC"]["last"])


def return_ticker():
    url = "{}?command=returnTicker".format(api_url)
    return _call_public_api(url)


def return_24_hour_volume():
    url = "{}?command=return24hVolume".format(api_url)
    return _call_public_api(url)


def return_chart_data(period, currency_pair, start, end=9999999999):
    """
    Retorna os dados do gráfico de candlesticks.

    :param period: (período de candlestick em segundos, vaores válidos são 300, 900, 1800, 7200, 14400 e 86400)
    :param currency_pair: O par em questão. Ex: BTC_XMR
    :param start: UNIX Timestamp para data de início
    :param end: UNIX Timestamp para data de término
    """
    url = "{api_url}?command=returnChartData&currencyPair={currency_pair}&start={start}&end={end}&period={period}".format(
        api_url=api_url, currency_pair=currency_pair, start=start, end=end, period=period)
    return _call_public_api(url)


def _call_public_api(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    json_response = response.read()
    return json.loads(json_response)
