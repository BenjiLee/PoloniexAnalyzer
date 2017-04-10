#!/usr/bin/env python
# -*- coding: latin-1 -*-
import os, sys

class bcolors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    END_COLOR = '\033[0m'


def print_dw_history(deposits, withdrawals): 
    print "-----Histórico de Depósitos/Retiradas-----"
    print "------------------------------------"
    print "--Moeda=Depósitos-Retiradas=Total-"
    for currency, deposit in deposits.iteritems():
        withdrawal = withdrawals[currency] if currency in withdrawals else 0
        print "{}={}-{}={}".format(currency, deposit, withdrawal, deposit - withdrawal)
