class DWHistory:
    def __init__(self, history):
        self.history = history

    def get_btc_total(self):
        deposits = 0
        withdrawals = 0

        for deposit in self.history['deposits']:
            deposits += float(deposit['amount'])

        for withdrawal in self.history['withdrawals']:
            withdrawals += float(withdrawal['amount'])

        print "-----Deposit/Withdrawal History-----"
        print "Deposits={}".format(deposits)
        print "Withdrawals={}".format(withdrawals)
        total = deposits - withdrawals
        print "Total BTC={}".format(total)
        return total
