class bcolors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    END_COLOR = '\033[0m'


def print_dw_history(deposits, withdrawals):
    print "-----Deposit/Withdrawal History-----"
    print "------------------------------------"
    print "--Currency=Deposit-Withdrawal=Total-"
    for currency, deposit in deposits.iteritems():
        withdrawal = withdrawals[currency] if currency in withdrawals else 0
        print "{}={}-{}={}".format(currency, deposit, withdrawal, deposit - withdrawal)
