# PoloniexAnalyzer

## What does this do?
Queries to Poloniex API for Deposit/Withdrawal history and current balances, and then returns you percentage earned/lost.

## Setup
Create a file called api_keys.txt with your api key on the first line and api secret on the second.

## How to run
```
python poloniex.py
```

## Example output 

```
>>>python poloniex.py

-----Deposit/Withdrawal History-----
Deposits=999999
Withdrawals=998394
Total BTC=999998
----------Current Balances----------
Total BTC=1000
-----------Earnings/Loss------------
Difference=-1602 BTC/$-363000
Stop trading, you're an idiot
62.30%
```


