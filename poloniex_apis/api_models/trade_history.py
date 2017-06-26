from poloniex_apis import trading_api


class TradeHistory:
    def __init__(self):
        self.history = trading_api.return_trade_history()

    def get_all_fees(self):
        result = {}
        for stock in self.history:
            result[stock] = 0
            for trade in self.history[stock]:
                result[stock] += float(trade["fee"]) * float(trade["total"])
        return result

