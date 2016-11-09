class Solution(object):
    def countBits(self, num):
        arr = []
        for i in range(0, num + 1):
            s = bin(i)
            arr.append(s.count('1'))
        return arr