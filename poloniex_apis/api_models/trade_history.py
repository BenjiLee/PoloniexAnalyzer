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

    def group_trades_by_time_and_currency(self):
        result = {}
        # return self.history
        for stock in self.history:
            result[stock] = {}
            for trade in self.history[stock]:
                if not trade['date'] in result[stock]:
                    result[stock][trade['date']] = 0
                trade_total_btc = float(trade['total'])
                if trade['type'] == 'buy':
                    trade_total_btc *= -1
                trade_price = '{0:f}'.format(
                    trade_total_btc - float(trade['fee']))
                result[stock][trade['date']] += float(trade_price)
        return result

    def am_i_winning(self):
        current = list(reversed(self.history["BTC_XMR"]))
        average_rate = 0
        total_units = 0
        yeah = 0
        for trade in current:
            if trade['type'] == 'buy':
                average_rate = ((average_rate*total_units) + (float(trade['rate'])*float(trade['amount'])))/(total_units+float(trade['amount']))
                total_units += (float(trade['amount']))
            else:
                # For some reason, the total for sells do not include the fee
                total_units -= (float(trade['amount'])*(1-float(trade['fee'])))
                yeah += float(trade['amount'])*(float(trade['rate'])-average_rate)
                print yeah
        return current

        return self.history
