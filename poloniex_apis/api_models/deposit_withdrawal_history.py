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
        # TODO: Maybe the api calls should be in here and ticker_data could be a class object
        balance = 0
        for deposit_ticker, amount in self.deposits.items():
            if deposit_ticker != u'BTC':
                balance += amount * self._get_ticker_value(ticker_data, deposit_ticker)
            else:
                balance += amount
        for withdrawal_ticker, amount in self.withdrawals.items():
            if withdrawal_ticker != u'BTC':
                balance -= amount * self._get_ticker_value(ticker_data, withdrawal_ticker)
            else:
                balance -= amount
        return balance

    def _get_ticker_value(self, ticker_data, ticker):
        """
        Gets the ticker value against BTC. If it's delisted, 0 will be returned.

        Args:
            ticker_data (dict): Dict of all the ticker data
            ticker (str): The ticker we are getting the BTC value for 

        Returns:
            float
        """
        try:
            return float(ticker_data[u'BTC_' + ticker]['last'])
        except KeyError:
            # For delisted coins
            return 0
