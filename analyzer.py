"""
Analyzer for running analysis on given data models :)

Hopefully all the methods in here will be uses for analyzing the data. If that
stops being true and if I were a good developer (it wouldn't have happened in
the first place) I would update this documentation.
"""
from poloniex_apis.api_models.balances import Balances
from poloniex_apis.api_models.deposit_withdrawal_history import DWHistory
from poloniex_apis.api_models.trade_history import TradeHistory

from poloniex_apis.public_api import return_usd_btc
import poloniex_apis.trading_api as trading_api


def get_overview():
    # TODO Should this take in the data models or call it itself
    balances = Balances(trading_api.return_complete_balances())
    dw_history = DWHistory(trading_api.return_deposits_withdrawals())

    balance, deposits, withdrawals = dw_history.get_btc_dw_history()
    current = balances.get_btc_total()

    usd_btc_price = return_usd_btc()
    balance_percentage = float("{:.4}".format(current / balance * 100))
    btc_balance_sum = current - balance
    usd_balance_sum = "{:.2f}".format(btc_balance_sum * usd_btc_price)

    # TODO This is really WET
    print "---Earnings/Losses Against Balance--"
    print "{} BTC/${}".format(btc_balance_sum, usd_balance_sum)
    if balance_percentage < 100:
        print "Stop trading, you're an idiot"
        print "{}%".format(balance_percentage)
    elif balance_percentage < 110:
        print "Put your funds in an index, dumb dumb"
        print "{}%".format(balance_percentage)
    elif balance_percentage < 150:
        print "Not bad"
        print "{}%".format(balance_percentage)
    elif balance_percentage < 175:
        print "You belong here"
        print "{}%".format(balance_percentage)
    elif balance_percentage < 200:
        print "Like striking crypto-oil"
        print "{}%".format(balance_percentage)
    elif balance_percentage < 250:
        print "On your way to becoming a bitcoin millionaire"
        print "{}%".format(balance_percentage)
    else:
        print "Cryptocurrencies can get heavy, you should send them over to me for safe keeping!"
        print "{}%".format(balance_percentage)

    deposits_percentage = float("{:.4}".format(current / deposits * 100))
    btc_deposits_sum = current - deposits
    usd_deposits_sum = "{:.2f}".format(btc_deposits_sum * usd_btc_price)

    print "--Earnings/Losses Against Deposits--"
    print "{} BTC/${}".format(btc_deposits_sum, usd_deposits_sum)
    if deposits_percentage < 100:
        print "Stop trading, you're an idiot"
        print "{}%".format(deposits_percentage)
    elif deposits_percentage < 110:
        print "Put your funds in an index, dumb dumb"
        print "{}%".format(deposits_percentage)
    elif deposits_percentage < 150:
        print "Not bad"
        print "{}%".format(deposits_percentage)
    elif deposits_percentage < 175:
        print "You belong here"
        print "{}%".format(deposits_percentage)
    elif deposits_percentage < 200:
        print "Like striking crypto-oil"
        print "{}%".format(deposits_percentage)
    elif deposits_percentage < 250:
        print "On your way to becoming a bitcoin millionaire"
        print "{}%".format(deposits_percentage)
    else:
        print "Cryptocurrencies can get heavy, you should send them over to me for safe keeping!"
        print "{}%".format(deposits_percentage)


def calculate_fees():
    # TODO Should this take in the data models or call it itself
    trade_history = TradeHistory(trading_api.return_trade_history())
    all_fees = trade_history.get_all_fees()

    print "--------------All Fees--------------"
    for stock, fees in all_fees.iteritems():
        print "{}={}".format(stock, fees)
