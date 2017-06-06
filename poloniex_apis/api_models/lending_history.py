import time

from poloniex_apis import trading_api
from utils import create_time_stamp

BITCOIN_GENESIS_BLOCK_DATE = "1231006505"


class LendingHistory:
    def __init__(self):
        self.history = self._get_all_lending_history()

    def _get_all_lending_history(self):
        current_timestamp = time.time()
        lending_history = trading_api.return_lending_history(BITCOIN_GENESIS_BLOCK_DATE, current_timestamp)

        did_not_recieve_all_lending_history = True
        while did_not_recieve_all_lending_history:
            returned_end_time = create_time_stamp(lending_history[-1]['close'])
            lending_history_segment = trading_api.return_lending_history(BITCOIN_GENESIS_BLOCK_DATE, returned_end_time)
            if len(lending_history_segment) == 1:
                did_not_recieve_all_lending_history = False
            else:
                lending_history += lending_history_segment
        return lending_history


