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

