# PoloniexAnalyzer

## What does this do?
Queries to Poloniex API for Deposit/Withdrawal history and current balances, and then returns you percentage earned/lost.

## Setup
Add your api key and secret in the api_keys.ini file.
Example api_keys.txt file
```
[ApiKeys]
key:iAmAnApiKeyGetYoursAtTheirWebsite
secret:iAmASecretForMyApiKeyDontEverShareThisWithAnyone
```

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


