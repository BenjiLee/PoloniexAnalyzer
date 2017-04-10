#!/usr/bin/env python
# -*- coding: latin-1 -*-
import os, sys
class TickerPrice:
    def __init__(self, ticker_price):
        self.ticker_price = ticker_price

    def get_price_for_ticker(self, ticker):
        return float(self.ticker_price[ticker]["last"])
