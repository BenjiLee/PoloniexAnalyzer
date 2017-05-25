import argparse
import textwrap
from collections import OrderedDict

import time
import sys

if sys.version_info[0] < 3:
    raise Exception("This project has move to using python 3. If you would like to use the python 2 snapshot, checkout"
                    " the v1.0.0 tag. `git checkout v1.0.0`")

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
        ("GetLendingHistory", {
            'function': analyzer.get_lending_history,
            'help': 'Returns your total lending interest and fees.',
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
        print(args.action)
        return

    if not args.loop:
        actions[args.action]['function']()
    else:
        while True:
            actions[args.action]['function']()
            time.sleep(int(args.loop))


if __name__ == '__main__':
    main()
