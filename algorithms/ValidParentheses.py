class Solution(object):
    def isValid(self, s):
        while s != '':
            prev = len(s)
            
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
            
            if prev == len(s):
                break
            
        return len(s) == 0
        