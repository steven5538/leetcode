class Solution(object):
    def reverse(self, x):
        x = str(x)
        if x[0] == '-':
            return int(x[0] + x[1:][::-1]) if -(2 ** 31) < int(x[0] + x[1:][::-1]) < 2 ** 31 else 0
        else:
            return int(x[::-1]) if -(2 ** 31) < int(x[::-1]) < 2 ** 31 else 0
            
        