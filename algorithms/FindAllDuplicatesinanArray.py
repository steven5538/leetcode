class Solution(object):
    def findDuplicates(self, nums):
        ans = []
        for n in nums:
            if nums[abs(n) - 1] < 0:
                ans.append(abs(n))
            else:
                nums[abs(n) - 1] *= -1
                
        return ans