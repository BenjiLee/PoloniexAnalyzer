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
>>>python poloniex.py

This analyzes information from your Poloniex account

optional arguments:
  -h, --help            show this help message and exit
  -a ACTION, --action ACTION
                        Script action (see below).

script actions/tasks:
    GetOverview
        Returns overall balance and percentage earned/lost
    CalculateFees
        Returns the total amount in fees

```

## Example output 

```
>>>python poloniex.py -a GetOverview

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

>>>python poloniex.py -a CalculateFees

--------------All Fees--------------
BTC_NXT=0.0245
BTC_ETC=0.356
ETH_ETC=0.01
BTC_XMR=0.0105
BTC_DASH=0.0295
BTC_ETH=0.143

```

## Want to help out?
Grab your mechanical keyboard and build up those hand calluses. Use the issues page for any of the following!
* Request a feature! What kinds of information do you want to know about your trading?
* Instructions not clear? Complain!
* Did something crash? Complain!
* Hard to use? Want a GUI? What kind?!
