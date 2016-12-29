class Solution(object):
    def rotate(self, nums, k):
        l = len(nums)
        nums[:] = nums[l - k:] + nums[:l - k]
