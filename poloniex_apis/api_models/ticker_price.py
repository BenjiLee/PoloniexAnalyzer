from poloniex_apis import public_api


class TickerData:
    def __init__(self):
        self.ticker_price = public_api.return_ticker()

    def get_price(self, ticker):
        try:
            return float(self.ticker_price[ticker]["last"])
        except KeyError:
            return 0
