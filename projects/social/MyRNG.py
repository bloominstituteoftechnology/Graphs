import time


class MyRandom():
    def __init__(self, seed=time.time()):
        self.seed = int(seed * 100000)

    def randomNumber(self, maxVal=4294967296):
        a = 16807
        c = 0
        self.seed = (a * self.seed + c) % 2147483647
        return self.seed % maxVal

    def randomChoice(self, fromArray):
        if type(fromArray) is dict:
            fromArray = [x for x in fromArray]
        maxValue = len(fromArray)
        if maxValue == 0:
            return None
        newValue = self.randomNumber(maxValue)
        return fromArray[newValue - 1]
