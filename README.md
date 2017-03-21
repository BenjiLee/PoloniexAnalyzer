# PoloniexAnalyzer

## What does this do?
Queries to Poloniex API for Deposit/Withdrawal history and current balances, and then returns you percentage earned/lost.

## Setup
Some scripts do not require an api key. For script that require an api key...
Copy the `api_keys.ini.example` file as `api_keys.ini` and add your api key 
and secret.

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
    GetDetailedOverview
        Returns detailed overall balance and percentage earned/lost
    CalculateFees
        Returns the total amount in fees
    GetChangeOverTime
        Public function: Returns percent change over a series of time periods
        for currencies exceeding a volume threshold

```

## Example output 

```
>>> python poloniex.py -a GetOverview

-----Deposit/Withdrawal History-----
Deposits=25.1500546
Withdrawals=5.150214
Total=19.9998406
----------Current Balances----------
Total BTC=17.73191744
---Earnings/Losses Against Balance--
-2.26792316 BTC/$-2533.27
Stop trading!
88.66%

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

>>> python poloniex.py -a GetChangeOverTime

Change over time for BTC traded currencies with volume > 1000 BTC
Currency: BTC_ETH, Volume: 19603.2832472
  1H: 0.54%, 24H: -3.75%, 2D: 10.49%, 3D: 16.54%, 4D: 17.22%, 1W: 40.44%
Currency: BTC_DASH, Volume: 17187.0818907
  1H: 4.43%, 24H: 14.24%, 2D: -4.32%, 3D: 30.18%, 4D: 53.17%, 1W: 68.00%
Currency: BTC_XMR, Volume: 3681.22693121
  1H: -0.33%, 24H: 4.62%, 2D: 8.32%, 3D: 2.83%, 4D: 11.44%, 1W: 8.63%
Currency: BTC_ETC, Volume: 1195.23748895
  1H: -0.11%, 24H: 6.82%, 2D: 4.01%, 3D: 8.66%, 4D: 9.88%, 1W: 12.92%
Currency: BTC_XRP, Volume: 1004.84598195
  1H: -0.40%, 24H: 1.63%, 2D: 7.30%, 3D: 9.41%, 4D: 8.46%, 1W: 2.25%

```

## Want to help out?
Grab your mechanical keyboard and build up those hand calluses. Use the issues page for any of the following!
* Request a feature! What kinds of information do you want to know about your trading?
* Instructions not clear? Complain!
* Did something crash? Complain!
* Hard to use? Want a GUI? What kind?!
