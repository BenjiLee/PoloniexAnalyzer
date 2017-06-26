from collections import defaultdict

from poloniex_apis.api_models.ticker_price import TickerData


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

    def get_btc_balance(self, ticker):
        balance = 0
        for deposit_symbol, amount in self.deposits.items():
            if deposit_symbol == u"USDT":
                balance += amount * ticker.get_price("USDT_BTC")
            if deposit_symbol != u'BTC':
                balance += amount * ticker.get_price("BTC_" + deposit_symbol)
            else:
                balance += amount
        for withdrawal_symbol, amount in self.withdrawals.items():
            if withdrawal_symbol == u"USDT":
                balance += amount * ticker.get_price("USDT_BTC")
            if withdrawal_symbol != u'BTC':
                balance -= amount * ticker.get_price("BTC_" + withdrawal_symbol)
            else:
                balance -= amount
        return balance
