class Solution(object):
    def removeDuplicates(self, nums):
        l = len(nums)
        
        if l < 2:
            return l
            
        index = 1
        for i in range(1, l):
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1
                
        return index