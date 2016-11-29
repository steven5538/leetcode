class Solution(object):
    def maxSubArray(self, nums):
        t = 0
        sub = nums[0]
        
        for i in nums:
            t += i
            
            if i > t:
                t = i
            
            if t > sub:
                sub = t
            
        return sub
        