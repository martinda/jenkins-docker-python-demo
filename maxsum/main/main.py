from ..core import maxsum
from ..cli import argparse

class Main:

    def __init__(self):
        self.args = None

    def setArgs(self,args):
        self.args = args

    def run(self):
        parser = argparse.MaxSumArgparse()
        args = parser.parse(self.args)
        p = maxsum.MaxSum()
        p.setIntegers(args.integers)
        p.setAccumulate(args.accumulate)
        print(p.run())

def main(args):
    main = Main()
    main.setArgs(args)
    main.run()

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
