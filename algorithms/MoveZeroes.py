class Solution(object):
    def moveZeroes(self, nums):
        position = 0
        
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[i], nums[position] = nums[position], nums[i]
                position += 1