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
  -l LOOP, --loop LOOP  Run every n seconds

script actions/tasks:
    GetOverview
        Returns overall balance and percentage earned/lost
    CalculateFees
        Returns the total amount in fees

```

## Example output 

```
>>> python poloniex.py -a GetOverview

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

>>> python poloniex.py -a CalculateFees

--------------All Fees--------------
BTC_NXT=0.0245
BTC_ETC=0.356
ETH_ETC=0.01
BTC_XMR=0.0105
BTC_DASH=0.0295
BTC_ETH=0.143

>>> python poloniex.py -a GetDetailedOverview

Warning, if you made non BTC trades, for example, ETH to ETC, some
of the values may look unusual. Since non BTC trades have not been
calculated in.
--------------BTC_NXT----------------
You invested 0.244053161185 BTC for 13256.4747085 NXT/0.432293640244 BTC
If you sold it all at the current price (assuming enough sell orders)
-0.188240479059 BTC/265.6 USD
--------------BTC_GRC----------------
You invested 0.47414196 BTC for 27307.2163235 GRC/0.405785234568 BTC
If you sold it all at the current price (assuming enough sell orders)
0.0683567254324 BTC/249.3 USD
--------------BTC_XMR----------------
You invested -12.8932790568 BTC for 259.526345896 XMR/4.40545712632 BTC
If you sold it all at the current price (assuming enough sell orders)
-17.2987361831 BTC/2707.0 USD
...

```

## Want to help out?
Grab your mechanical keyboard and build up those hand calluses. Use the issues page for any of the following!
* Request a feature! What kinds of information do you want to know about your trading?
* Instructions not clear? Complain!
* Did something crash? Complain!
* Hard to use? Want a GUI? What kind?!
