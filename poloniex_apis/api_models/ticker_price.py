class TickerPrice:
    def __init__(self, ticker_price):
        self.ticker_price = ticker_price

    def get_price_for_ticker(self, ticker):
        try:
            return float(self.ticker_price[ticker]["last"])
        except KeyError:
            return 0
