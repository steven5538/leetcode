class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.split()[-1]) if len(s.split()) >= 1 else 0
        