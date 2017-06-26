from poloniex_apis import public_api


class TickerData:
    def __init__(self):
        self.ticker_price = public_api.return_ticker()

    def get_price(self, pair):
        transaction, settlement = pair.split("_")[0], pair.split("_")[1]
        if transaction == settlement:
            return 1
        try:
            return float(self.ticker_price[pair]["last"])
        except KeyError:
            return 0
