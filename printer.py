"""
Some of the logic for printing and the print statements.
"""

class bcolors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    END_COLOR = '\033[0m'


def print_get_overview_results(btc_balance_sum, usd_balance_sum, balance_percentage):
    print("\nNote: Get Overview currently does not take the margin account into account.")

    print("---Earnings/Losses Against Balance--")
    print("{} BTC/${}".format(btc_balance_sum, usd_balance_sum))
    if balance_percentage < 100:
        print("Stop trading!")
        print("{}%".format(balance_percentage))
    elif balance_percentage < 110:
        print("Still worse than an index.")
        print("{}%".format(balance_percentage))
    elif balance_percentage < 150:
        print("Not bad")
        print("{}%".format(balance_percentage))
    elif balance_percentage < 175:
        print("You belong here")
        print("{}%".format(balance_percentage))
    elif balance_percentage < 200:
        print("Like striking crypto-oil")
        print("{}%".format(balance_percentage))
    elif balance_percentage < 250:
        print("On your way to becoming a Bitcoin millionaire")
        print("{}%".format(balance_percentage))
    else:
        print("Cryptocurrencies can get heavy, you should send them over to me for safe keeping!")
        print("{}%".format(balance_percentage))


def print_get_lending_history(currency, earnings, fees, average_rate):
    print("---------Your {} Lending History---------".format(currency))
    print("Total earned: {} {}".format(earnings, currency))
    print("Total fees: {} {}".format(fees, currency))
    print("Average rate: {}%".format(average_rate))


def print_dw_history(deposits, withdrawals):
    print("-----Deposit/Withdrawal History-----")
    print("------------------------------------")
    print("--Currency=Deposit-Withdrawal=Total-")
    for currency, deposit in deposits.items():
        withdrawal = withdrawals[currency] if currency in withdrawals else 0
        print("{}={}-{}={}".format(currency, deposit, withdrawal, deposit - withdrawal))
