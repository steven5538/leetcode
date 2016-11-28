class Solution(object):
    def isSubsequence(self, s, t):
        for i in s:
            if i in t:
                t = t[t.index(i) + 1:]
            else:
                return False
                
        return True
        