from poloniex_apis import public_api


class TickerData:
    def __init__(self):
        self.ticker_price = public_api.return_ticker()

    def get_price(self, symbol):
        try:
            return float(self.ticker_price[symbol]["last"])
        except KeyError:
            return 0
