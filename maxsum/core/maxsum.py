import numpy as np

class MaxSum:

    def __init__(self):
        self.integers = None
        self.accumulate = False

    def setIntegers(self, integers):
        self.integers = np.array(integers)

    def setAccumulate(self, accumulate):
        self.accumulate = accumulate

    def max(self):
        return self.integers.max()

    def sum(self):
        return self.integers.sum()

    def run(self):
        if (self.accumulate):
            return f"The sum is: {self.sum()}"
        return f"The max is: {self.max()}"
