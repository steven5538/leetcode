class NumArray(object):
    def __init__(self, nums):
        
        if len(nums) >= 1:
            self.sums = [nums[0]]
        else:
            self.sums = []
        
        for i in range(1, len(nums)):
            self.sums.append(self.sums[i - 1] + nums[i])
        

    def sumRange(self, i, j):
        if len(self.sums) == 0:
            return 0
            
        if i == 0:
            return self.sums[j]
            
        return self.sums[j] - self.sums[i - 1]1
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)