class Balances:
    def __init__(self, all_balances):
        self.all_balances = all_balances

    def get_active_balances(self):
        active_balances = {}
        for stock, balances in self.all_balances.iteritems():
            for balance_type, value in balances.iteritems():
                if float(value) > 0:
                    active_balances[stock] = balances
        return active_balances

    def get_btc_total(self):
        total_btc = 0
        for stock, balances in self.get_active_balances().iteritems():
            total_btc += float(balances['btcValue'])
        print "----------Current Balances----------"
        print "Total BTC={}".format(total_btc)
        return total_btc
