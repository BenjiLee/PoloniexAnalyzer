"""
Analyzer for running analysis on given data models :)

Hopefully all the methods in here will be uses for analyzing the data. If that
stops being true and if I were a good developer (it wouldn't have happened in
the first place) I would update this documentation.
"""
import poloniex_apis.trading_api as trading_api
from poloniex_apis import public_api
from poloniex_apis.api_models.balances import Balances
from poloniex_apis.api_models.deposit_withdrawal_history import DWHistory
from poloniex_apis.api_models.ticker_price import TickerPrice
from poloniex_apis.api_models.trade_history import TradeHistory
from poloniex_apis.public_api import return_usd_btc


def get_overview():
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


def get_detailed_overview():
    ticker_price = TickerPrice(public_api.return_ticker())
    trade_history = trading_api.return_trade_history()
    print "Warning, if you made non BTC trades, for example, ETH to ETC, some"
    print "of the values may look unusual. Since non BTC trades have not been"
    print "calculated in."
    for ticker in trade_history:
        if ticker.startswith("BTC_"):
            current = list(reversed(trade_history[ticker]))
            btc_sum = 0
            for trade in current:
                if trade['type'] == 'buy':
                    btc_sum += float(trade["total"])
                else:
                    # For some reason, the total for sells do not include the
                    # fee so we include it here.
                    btc_sum -= (float(trade["total"]) * (1 - float(trade["fee"])))

            ticker_sum = 0
            for trade in current:
                if trade['type'] == 'buy':
                    ticker_sum += float(trade["amount"])  # Total
                    ticker_sum -= float(trade["amount"]) * float(trade["fee"])  # Fee
                else:
                    ticker_sum -= float(trade["amount"])
            if ticker_sum > 0.000000001:
                current_btc_sum = float(ticker_price.get_price_for_ticker(ticker)) * ticker_sum
                total_btc = btc_sum - current_btc_sum
                total_usd = float("{:.4}".format(ticker_sum * ticker_price.get_price_for_ticker(ticker) * ticker_price.get_price_for_ticker("USDT_BTC")))
                print "--------------{}----------------".format(ticker)
                print "You invested {} BTC for {} {}/{} BTC".format(btc_sum, ticker_sum, ticker.split("_")[1], current_btc_sum)
                print "If you sold it all at the current price (assuming enough sell orders)"
                print "{} BTC/{} USD".format(total_btc, total_usd)

    return current


def calculate_fees():
    # TODO Should this take in the data models or call it itself
    trade_history = TradeHistory(trading_api.return_trade_history())
    all_fees = trade_history.get_all_fees()

    print "--------------All Fees--------------"
    for stock, fees in all_fees.iteritems():
        print "{}={}".format(stock, fees)
