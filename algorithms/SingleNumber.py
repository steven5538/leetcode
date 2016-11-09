class Solution(object):
    def singleNumber(self, nums):
        result = nums[0]
        for i in nums[1:]:
            result ^= i
        return result