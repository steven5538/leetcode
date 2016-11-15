class Solution(object):
    def titleToNumber(self, s):
        sum = 0
        for i in xrange(0, len(s)):
            sum = (ord(s[i]) - ord('A') + 1) + (26 * sum)
            
        return sum
        