import argparse

class MaxSumArgparse:

    def parse(self, args):

        parser = argparse.ArgumentParser(description='Calculate the max or the sum of a list of integers.')
        parser.add_argument(
            'integers',
            metavar='N',
            type=int,
            nargs='+',
            help='an integer for the accumulator'
        )
        parser.add_argument(
            '--sum',
            dest='accumulate',
            action='store_true',
            help='sum the integers (default: find the max)'
        )

        return parser.parse_args(args)

