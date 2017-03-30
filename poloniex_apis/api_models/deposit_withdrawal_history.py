from collections import defaultdict


class DWHistory:
    def __init__(self, history):
        self.withdrawals = defaultdict(float)
        self.deposits = defaultdict(float)
        self.history = history

    def get_dw_history(self):
        for deposit in self.history['deposits']:
            if deposit['currency'] in self.deposits:
                self.deposits[deposit['currency']] += float(deposit['amount'])
            else:
                self.deposits[deposit['currency']] = float(deposit['amount'])
        for withdrawal in self.history['withdrawals']:
            if withdrawal['currency'] in self.withdrawals:
                self.withdrawals[withdrawal['currency']] += float(withdrawal['amount'])
            else:
                self.withdrawals[withdrawal['currency']] = float(withdrawal['amount'])
        return self.deposits, self.withdrawals

    def get_btc_balance(self, ticker_data):
        balance = 0
        for deposit, amount in self.deposits.iteritems():
            if deposit != u'BTC':
                balance += amount * float(ticker_data[u'BTC_' + deposit]['last'])
            else:
                balance += amount
        for withdrawal, amount in self.withdrawals.iteritems():
            if withdrawal != u'BTC':
                balance -= amount * float(ticker_data[u'BTC_' + withdrawal]['last'])
            else:
                balance -= amount
        return balance
