class MaxSum:

    def __init__(self):
        self.integers = []
        self.accumulate = False

    def setIntegers(self, integers):
        self.integers = integers

    def setAccumulate(self, accumulate):
        self.accumulate = accumulate

    def max(self):
        return max(self.integers)

    def sum(self):
        return sum(self.integers)

    def run(self):
        if (self.accumulate):
            return f"The sum is: {self.sum()}"
        return f"The max is: {self.max()}"
