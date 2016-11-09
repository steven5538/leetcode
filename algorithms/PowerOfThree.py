import math

class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False

        return math.log10(n) / math.log10(3) % 1 == 0
        