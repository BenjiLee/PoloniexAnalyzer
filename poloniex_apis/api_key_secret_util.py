#!/usr/bin/env python
# -*- coding: latin-1 -*-
import os, sys
import ConfigParser


def get_api_key():
    """
    Retorna uma chave API da Poloniex do arquivo de configuração
    """
    config = ConfigParser.ConfigParser()
    config.read("api_keys.ini")
    key = config.get("ApiKeys", "key")
    return key


def get_api_secret():
    """
    Retorna um segredo de API da Poloniex do arquivo de configuração
    """
    config = ConfigParser.ConfigParser()
    config.read("api_keys.ini")
    secret = config.get("ApiKeys", "secret")
    return secret
