class Solution(object):
    def singleNumber(self, nums):
        x = 0
        for i in nums:
            x ^= i
            
        mask = x
        mask &= -x
        
        a = 0
        b = 0
        
        for i in nums:
            if mask & i:
                a ^= i
            else:
                b ^= i
                
        return [a, b]
