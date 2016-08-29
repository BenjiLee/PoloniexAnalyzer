class TradeHistory:
    def __init__(self, history):
        self.history = history

    def get_all_fees(self):
        result = {}
        for stock in self.history:
            result[stock] = 0
            for trade in self.history[stock]:
                result[stock] += float(trade["fee"])
        return result

    def group_trades_by_time(self):
        result = {}
        return self.history
        for stock in self.history:
            result[stock] = {}
            for trade in self.history[stock]:
                if not trade['date'] in result[stock]:
                    result[stock][trade['date']] = 0
                trade_price = '{0:f}'.format(float(trade['total']) - float(trade['fee']))
                result[stock][trade['date']] += float(trade_price)

        print result
        return result
