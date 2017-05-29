from poloniex_apis import trading_api


class Balances:
    def __init__(self):
        self.all_balances = trading_api.return_complete_balances()

    def get_btc_total(self):
        total_btc = 0
        for stock, balances in self._get_active_balances().items():
            total_btc += float(balances['btcValue'])
        print("----------Current Balances----------")
        print("Total BTC={}".format(total_btc))
        return total_btc

    def _get_active_balances(self):
        active_balances = {}
        for stock, balances in self.all_balances.items():
            for balance_type, value in balances.items():
                if float(value) > 0:
                    active_balances[stock] = balances
        return active_balances
