class Solution(object):
    def findTheDifference(self, s, t):
        r = 0
        
        for c in s:
            r += ord(c)
        for c in t:
            r -= ord(c)
            
        return chr(abs(r))
            
        