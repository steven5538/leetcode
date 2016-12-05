class Solution(object):
    def numberOfArithmeticSlices(self, A):
        lena = len(A)
        combine = 0
        slices = 0
        
        for i in xrange(2 , lena):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                combine += 1
                slices += combine
            else:
                combine = 0

        return slices
            