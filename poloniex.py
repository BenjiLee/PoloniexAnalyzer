#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import argparse
import textwrap
from collections import OrderedDict

import time

import analyzer


def main():
    actions = OrderedDict([
        ("GetOverview", {
            'function': analyzer.get_overview,
            'help': 'Retorna o balanço geral e porcentagem ganhada/perdida',
        }),
        ("GetDetailedOverview", {
            'function': analyzer.get_detailed_overview,
            'help': 'Retorna um balanço geral detalhado e porcentagem ganhada/perdida',
        }),
        ("CalculateFees", {
            'function': analyzer.calculate_fees,
            'help': 'Retorna o valor total em taxas',
        }),
        ("GetChangeOverTime", {
            'function': analyzer.get_change_over_time,
            'help': 'Função pública: Retorna a mudança da porcentagem em uma série de períodos de tempo para moedas que excedam um volume mínimo'
        })
    ])

    parser = argparse.ArgumentParser(
        description="Isso analisa informação da sua conta na Poloniex",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('-a', '--action', help='Ação do script (veja abaixo).',
                        default='', required=True)
    parser.add_argument('-l', '--loop', help='Roda a cada n segundos',
                        default='', required=False)

    parser.epilog = "ações/tarefas do script:"
    for action in actions:
        parser.epilog += "\n    {}".format(action)
        line_length = 80
        indents = 8
        for line in textwrap.wrap(actions[action]['help'],
                                  line_length - indents):
            parser.epilog += "\n        {}".format(line)

    args = parser.parse_args()

    if args.action not in actions or args.action is None:
        parser.print_help()
        print args.action
        return

    if not args.loop:
        actions[args.action]['function']()
    else:
        while True:
            actions[args.action]['function']()
            time.sleep(int(args.loop))


if __name__ == '__main__':
    main()
