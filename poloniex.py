import argparse
import textwrap
from collections import OrderedDict

from analyzer import Analyzer


def main():
    actions = OrderedDict([
        ("GetOverview", {
            'function': Analyzer.get_overview,
            'help': 'Returns overall balance and percentage earned/lost',
        }),
        ("CalculateFees", {
            'function': Analyzer.calculate_fees,
            'help': 'Returns the total amount in fees',
        }),
    ])

    parser = argparse.ArgumentParser(
        description="This analyzes information from your Poloniex account",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('-a', '--action', help='Script action (see below).',
                        default='', required=True)

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

    actions[args.action]['function'](Analyzer())


if __name__ == '__main__':
    main()
