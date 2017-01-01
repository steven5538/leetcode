class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int('{0:b}'.format(n).zfill(32)[::-1], 2)