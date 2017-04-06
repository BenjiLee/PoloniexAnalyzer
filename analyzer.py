"""
Analisador para execuções analíticas sobre deterinados modelos de dados :)

Espero que todos os métodos aqui sejam usados para a análise dos dados. Se isso
deixar de ser verdade e se eu fosse um bom desenvolvedordeveloper (isso não aconteceria,
em primeiro lugar) eu atualizaria a documentação.
"""
import operator

import time

import poloniex_apis.trading_api as trading_api
import utils
from poloniex_apis import public_api
from poloniex_apis.api_models.balances import Balances
from poloniex_apis.api_models.deposit_withdrawal_history import DWHistory
from poloniex_apis.api_models.ticker_price import TickerPrice
from poloniex_apis.api_models.trade_history import TradeHistory
from poloniex_apis.public_api import return_usd_btc


def get_overview():
    balances = Balances(trading_api.return_complete_balances())
    dw_history = DWHistory(trading_api.return_deposits_withdrawals())
    deposits, withdrawals = dw_history.get_dw_history()
    utils.print_dw_history(deposits, withdrawals)
    balance = dw_history.get_btc_balance(public_api.return_ticker())
    current = balances.get_btc_total()

    usd_btc_price = return_usd_btc()
    balance_percentage = float("{:.4}".format(current / balance * 100))
    btc_balance_sum = current - balance
    usd_balance_sum = "{:.2f}".format(btc_balance_sum * usd_btc_price)

    print "---Ganhos/Perdas vs Balanço--"
    print "{} BTC/${}".format(btc_balance_sum, usd_balance_sum)
    if balance_percentage < 100:
        print "Pare de fazer trading!"
        print "{}%".format(balance_percentage)
    elif balance_percentage < 110:
        print "Ainda pior que um índice."
        print "{}%".format(balance_percentage)
    elif balance_percentage < 150:
        print "Nada mal"
        print "{}%".format(balance_percentage)
    elif balance_percentage < 175:
        print "Você está em casa"
        print "{}%".format(balance_percentage)
    elif balance_percentage < 200:
        print "Mastermind"
        print "{}%".format(balance_percentage)
    elif balance_percentage < 250:
        print "À caminho de tornar-se um milionário do bitcoin"
        print "{}%".format(balance_percentage)
    else:
        print "Criptomoedas podem ficar pesadas, então você deveria enviá-las à mim para ficarem seguras!"
        print "{}%".format(balance_percentage)


def get_detailed_overview():
    ticker_price = TickerPrice(public_api.return_ticker())
    trade_history = trading_api.return_trade_history()
    print "Aviso, se você fez trades não BTC, como ETH/ETC por exemplo, alguns"
    print "dos valore podem parecer estranhos, já que nenhum trade de BTC foi"
    print "devidamente calculado."
    for ticker in trade_history:
        if ticker.startswith("BTC_"):
            current = list(reversed(trade_history[ticker]))
            btc_sum = 0
            for trade in current:
                if trade['type'] == 'buy':
                    btc_sum += float(trade["total"])
                else:
                    # Por alguma razão, o total de vendas nçao inclui a
                    # taxa, então a incluímos aqui.
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
                total_btc = current_btc_sum - btc_sum
                total_usd = float("{:.4}".format(total_btc * ticker_price.get_price_for_ticker("USDT_BTC")))
                print "--------------{}----------------".format(ticker)
                print "Você investiu {} BTC por {} {}/{} BTC".format(btc_sum, ticker_sum, ticker.split("_")[1],
                                                                    current_btc_sum)
                print "Se você vender tudo no preço atual (assumindo que tenha ordens de venda)"

                if total_btc < 0:
                    print utils.bcolors.RED,
                else:
                    print utils.bcolors.GREEN,
                print "{} BTC/{} USD".format(total_btc, total_usd)
                print utils.bcolors.END_COLOR,

    return current


def calculate_fees():
    # TODO Should this take in the data models or call it itself
    trade_history = TradeHistory(trading_api.return_trade_history())
    all_fees = trade_history.get_all_fees()

    print "--------------Todas as Taxas--------------"
    for stock, fees in all_fees.iteritems():
        print "{}={}".format(stock, fees)


def get_change_over_time():
    """
    Retorna uma lista de moedas com volume acima do limite mínimo.
    :return:
    """
    threshold = 1000
    currency_list = []

    volume_data = public_api.return_24_hour_volume()
    for item in volume_data:
        if item.startswith('BTC'):
            if float(volume_data.get(item).get('BTC')) > threshold:
                currency_list.append(item)

    currencies = {}
    for currency_pair in currency_list:
        currencies[currency_pair] = float(volume_data.get(currency_pair).get(u'BTC'))
    sorted_currencies = sorted(currencies.items(), key=operator.itemgetter(1), reverse=True)

    period = 300
    print "Mudança no decorrer do tempo para moedas cnegociadas por BTC com volume > 1000 BTC"
    for currency in sorted_currencies:
        now = int(time.time())
        last_week = now - 604800
        history = public_api.return_chart_data(
            period=period,
            currency_pair=currency[0],
            start=last_week,
        )
        print "Moeda: {}, Volume: {}".format(currency[0], currency[1])
        print "  1H: {}, 24H: {}, 2D: {}, 3D: {}, 4D: {}, 1S: {}".format(
            _to_percent_change(history[-1]['close']/history[-(3600/period-1)]['close']),
            _to_percent_change(history[-1]['close']/history[-(86400/period-1)]['close']),
            _to_percent_change(history[-1]['close']/history[-(172800/period-1)]['close']),
            _to_percent_change(history[-1]['close']/history[-(259200/period-1)]['close']),
            _to_percent_change(history[-1]['close']/history[-(345600/period-1)]['close']),
            _to_percent_change(history[-1]['close']/history[-(604800/period-1)]['close']),
        )
        time.sleep(1)


def _to_percent_change(number):
    if not isinstance(number, float):
        number = float(number)
    return "{:.2f}%".format(number * 100 - 100)



