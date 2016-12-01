class Solution(object):
        
    def climbStairs(self, n):
        a = 1
        b = 1
        
        for i in xrange(n):
            a, b = b, a + b
            
        return a
