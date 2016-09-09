"""
Analyzer for running analysis on given data models :)

Hopefully all the methods in here will be uses for analyzing the data. If that
stops being true and if I were a good developer (it wouldn't have happened in
the first place) I would update this documentation.
"""
from poloniex_apis.api_models.balances import Balances
from poloniex_apis.api_models.deposit_withdrawal_history import DWHistory
from poloniex_apis.api_models.trade_history import TradeHistory

from poloniex_apis.public_api import PublicApi
from poloniex_apis.trading_api import TradingApi


def get_overview():
    # TODO Should this take in the data models or call it itself
    balances = Balances(TradingApi().return_complete_balances())
    dw_history = DWHistory(TradingApi().return_deposits_withdrawals())

    start = dw_history.get_btc_total()
    current = balances.get_btc_total()

    usd_btc_price = PublicApi().return_usd_btc()
    percentage = float("{:.4}".format(current / start * 100))
    btc_sum = current - start
    usd_sum = "{:.2f}".format(btc_sum * usd_btc_price)
    print "----------Earnings/Losses-----------"
    print "Difference={} BTC/${}".format(btc_sum, usd_sum)
    if percentage < 100:
        print "Stop trading, you're an idiot"
        print "{}%".format(percentage)
    elif percentage < 110:
        print "Put your funds in an index, dumb dumb"
        print "{}%".format(percentage)
    elif percentage < 150:
        print "Not bad"
        print "{}%".format(percentage)
    else:
        print "Cryptocurrencies can get heavy, you should send them over to me for safe keeping!"
        print "{}%".format(percentage)


def calculate_fees():
    # TODO Should this take in the data models or call it itself
    trade_history = TradeHistory(TradingApi().return_trade_history())
    print trade_history.history
    all_fees = trade_history.get_all_fees()

    print "--------------All Fees--------------"
    for stock, fees in all_fees.iteritems():
        print "{}={}".format(stock, fees)
