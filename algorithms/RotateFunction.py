class Solution(object):
    def maxRotateFunction(self, A):
        sums = sum(A)
        
        v = 0
        for key, value in enumerate(A):
            v += key * value
        
        maximum = v
        for i in A[::-1]:
            v = v + sums - i * len(A)
            if maximum < v:
                maximum = v
        
        return maximum