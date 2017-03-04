import argparse
import textwrap
from collections import OrderedDict

import time

import analyzer


def main():
    actions = OrderedDict([
        ("GetOverview", {
            'function': analyzer.get_overview,
            'help': 'Returns overall balance and percentage earned/lost',
        }),
        ("GetDetailedOverview", {
            'function': analyzer.get_detailed_overview,
            'help': 'Returns detailed overall balance and percentage earned/lost',
        }),
        ("CalculateFees", {
            'function': analyzer.calculate_fees,
            'help': 'Returns the total amount in fees',
        }),
        ("GetChangeOverTime", {
            'function': analyzer.get_change_over_time,
            'help': 'Public function: Returns percent change over a series of time periods for currencies exceeding a volume threshold'
        })
    ])

    parser = argparse.ArgumentParser(
        description="This analyzes information from your Poloniex account",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('-a', '--action', help='Script action (see below).',
                        default='', required=True)
    parser.add_argument('-l', '--loop', help='Run every n seconds',
                        default='', required=False)

    parser.epilog = "script actions/tasks:"
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
