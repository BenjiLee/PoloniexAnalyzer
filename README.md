# PoloniexAnalyzer

## What does this do?
Queries to Poloniex API for Deposit/Withdrawal history and current balances, and then returns you percentage earned/lost.

## Setup
Add your api key and secret in the api_keys.ini file.

Example api_keys.ini file
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

## Want to help out?
Grab your mechanical keyboard and build up those hand calluses. Use the issues page for any of the following!
* Request a feature! What kinds of information do you want to know about your trading?
* Instructions not clear? Complain!
* Did something crash? Complain!
* Hard to use? Want a GUI? What kind?!
