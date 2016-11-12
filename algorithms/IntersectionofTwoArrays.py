class Solution(object):
    def intersection(self, nums1, nums2):
        answers = []
        for num in nums1:
            if num in nums2:
                nums2.pop(nums2.index(num))
                answers.append(num)
        return list(set(answers))