from collections import defaultdict

import time

import dev_utils
from poloniex_apis import public_api, trading_api
import matplotlib.pyplot as plot
import matplotlib.dates as mpldate


def graph_it():
    # dev_utils.dict_to_file(trading_api.return_trade_history(), 'trade_history.txt')
    # dev_utils.dict_to_file(trading_api.return_deposits_withdrawals(), 'dw_history.txt')

    trade_history = dev_utils.file_to_dict('trade_history.txt')
    dw_history = dev_utils.file_to_dict('dw_history.txt')

    master_dict = defaultdict(int)
    sorted_dw = _get_sorted_dw_history(dw_history)

    for date, value in sorted_dw:
        master_dict[date] += value
    non_btc_dict = {}
    for currency, trades in trade_history.items():
        for trade in trades:
            epoch = _get_epoch(trade["date"])
            value = float(trade["total"])
            if trade["type"] == "sell":
                value = -float(value)

            if currency.startswith("BTC"):
                master_dict[epoch] += value
            else:
                if currency in non_btc_dict:
                    non_btc_dict[currency][epoch] += value
                else:
                    non_btc_dict[currency] = defaultdict(int)
                    non_btc_dict[currency][epoch] += value

    for currency, data in non_btc_dict.items():
        for item in data:
            ticker = currency if currency == "USDT_BTC" else "BTC_" + currency.split("_")[0]
            estimated_price = public_api.return_chart_data(300, ticker, epoch, epoch+300)[0]['weightedAverage']
            master_dict[epoch] += estimated_price*float(data[item])

    master_list = []
    for epoch, value in master_dict.items():
        master_list.append((epoch, value))
    master_list.sort(key=lambda tup: tup[0])

    dates = []
    values = []
    balance = 0
    for item in master_list:
        dates.append(mpldate.epoch2num(item[0]))
        balance += item[1]
        values.append(balance)

    graph_data_dict = {'x': dates, 'y': values, "colors": None}
    _plot_graph(graph_data_dict)


def _get_epoch(date_string):
    pattern = '%Y-%m-%d %H:%M:%S'
    epoch = int(time.mktime(time.strptime(date_string, pattern)))
    return epoch


def _get_sorted_dw_history(dw_history):
    flat_dw_list = []
    for deposit in dw_history["deposits"]:
        flat_dw_list.append((deposit["timestamp"], float(deposit["amount"])))
    for withdrawal in dw_history["withdrawals"]:
        flat_dw_list.append((withdrawal["timestamp"], -float(withdrawal["amount"])))
    flat_dw_list.sort(key=lambda tup: tup[0])
    return flat_dw_list

    dates = []
    values = []
    balance = 0
    for item in flat_dw_list:
        dates.append(mpldate.epoch2num(item[0]))
        balance += item[1]
        values.append(balance)

    return dates, values


def _plot_graph(graph_data_dict):
    x = graph_data_dict['x']
    y = graph_data_dict['y']
    colors = graph_data_dict['colors']

    plot.plot_date(x, y, marker=None)
    plot.plot(x, y)
    plot.scatter(x, y, color=colors)
    plot.axes().grid(color='k', linestyle='-', linewidth=.1)
    plot.xticks(rotation=30)
    plot.show()
