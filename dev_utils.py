#!/usr/bin/env python
# -*- coding: latin-1 -*-
import os, sys
"""
Métodos utilitários para desenvolvimento
"""
import simplejson


def dict_to_file(dict_input):
    string_input = str(dict_input)
    result = string_input.replace("u'", '"')
    result = result.replace("'", '"')

    f = open('dump.json', 'w')
    f.write(simplejson.dumps(simplejson.loads(result), indent=4, sort_keys=True))
    f.close()


def file_to_dict():
    f = open('dump.json', 'r')
    string = f.read()
    f.close()
    return simplejson.loads(string)
