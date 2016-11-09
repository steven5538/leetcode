import math

class Solution(object):
    def isPowerOfFour(self, num):
        if num <= 0:
            return False

        return math.log10(num) / math.log10(4) % 1 == 0
        