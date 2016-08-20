from balances import Balances
from deposit_withdrawal_history import DWHistory
from poloniex_apis.public_api import PublicApi
from poloniex_apis.trading_api import TradingApi


def get_api_key_from_file(file_path):
    f = open(file_path, 'r')
    key = f.readline().rstrip()
    secret = f.readline().rstrip()
    return key, secret


def calculate_percentage(start, current):
    percentage = float("{:.4}".format(current / start * 100))

    print "-----------Earnings/Loss------------"
    if percentage < 100:
        print "Stop trading, you're an idiot"
        print "{}%".format(percentage)
    elif percentage < 110:
        print "Put your funds in an index, idiot"
        print "{}%".format(percentage)
    elif percentage < 150:
        print "Not bad"
        print "{}%".format(percentage)
    else:
        print "Cryptocurrencies can get heavy, you should send them over to me for safe keeping!"
        print "{}%".format(percentage)


class main():
    key, secret = get_api_key_from_file(file_path="api_keys.txt")
    trading_api = TradingApi(key, secret)
    balances = Balances(trading_api.return_complete_balances())
    dw_history = DWHistory(trading_api.return_deposits_withdrawals())

    calculate_percentage(
        dw_history.get_btc_total(),
        balances.get_btc_total()
    )


if __name__ == '__main__':
    main()
