class Solution(object):
    def integerBreak(self, n):
        if n <= 2:
            return 1
        elif n == 3 :
            return 2
        elif n == 4:
            return 4
        else:
            p = n % 3
            
            if p == 1:
                return 3 ** (n / 3 - 1) * 4
            elif p == 2:
                return 3 ** (n / 3) * 2
            else:
                return 3 ** (n / 3)
                    
                    
        