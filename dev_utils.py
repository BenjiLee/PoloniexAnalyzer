#!/usr/bin/env python
# -*- coding: latin-1 -*-
import os, sys
"""
Métodos utilitários para desenvolvimento
"""
import json


def dict_to_file(dict_input):
    with open('dump.json', 'w') as f:
        json.dump(dict_input, f, indent=4, sort_keys=True)


def file_to_dict():
    with open('dump.json', 'r') as f:
        return json.load(f)
