import math

class Solution(object):
    def arrangeCoins(self, n):
        if n == 0:
            return 0
        if n <= 2:
            return 1
            
        n *= 2
            
        k = int(math.sqrt(n)) + 1
        
        while k * (k + 1) > n:
            k -= 1
            
        return k
        